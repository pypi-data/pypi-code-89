from contextlib import contextmanager
from functools import wraps
import importlib
import inspect
import logging
import os
from types import ModuleType
from typing import (
    Any,
    cast,
    Callable,
    Dict,
    Generator,
    List,
    MutableMapping,
    Optional,
    Sequence,
    Union,
)
from inspect import Parameter

from ray.runtime_context import get_runtime_context
from ray.util.inspect import (is_class_method, is_function_or_method,
                              is_static_method)
import ray.worker

logger = logging.getLogger(__name__)


class _OpenTelemetryProxy:
    """
    This proxy makes it possible for tracing to be disabled when opentelemetry
    is not installed on the cluster, but is installed locally.

    The check for `opentelemetry`'s existence must happen where the functions
    are executed because `opentelemetry` may be present where the functions
    are pickled. This can happen when `ray[full]` is installed locally by `ray`
    (no extra dependencies) is installed on the cluster.
    """
    allowed_functions = {"trace", "context", "propagate", "Context"}

    def __getattr__(self, name):
        if name in _OpenTelemetryProxy.allowed_functions:
            return getattr(self, f"_{name}")()
        else:
            raise AttributeError(f"Attribute does not exist: {name}")

    def _trace(self):
        return self._try_import("opentelemetry.trace")

    def _context(self):
        return self._try_import("opentelemetry.context")

    def _propagate(self):
        return self._try_import("opentelemetry.propagate")

    def _Context(self):
        context = self._context()
        if context:
            return context.context.Context
        else:
            return None

    def try_all(self):
        self._trace()
        self._context()
        self._propagate()
        self._Context()

    def _try_import(self, module):
        try:
            return importlib.import_module(module)
        except ImportError:
            if os.getenv("RAY_TRACING_ENABLED",
                         "False").lower() in ["true", "1"]:
                raise ImportError(
                    "Install opentelemetry with "
                    "'pip install opentelemetry-api==1.0.0rc1' "
                    "and 'pip install opentelemetry-sdk==1.0.0rc1' to enable "
                    "tracing. See more at docs.ray.io/tracing.html")


_opentelemetry = _OpenTelemetryProxy()
_opentelemetry.try_all()

_nameable = Union[str, Callable[..., Any]]
_global_is_tracing_enabled = False


def sort_params_list(params_list: List[Parameter]):
    """Given a list of Parameters, if a kwargs Parameter exists,
    move it to the end of the list."""
    for i, param in enumerate(params_list):
        if param.kind == Parameter.VAR_KEYWORD:
            params_list.append(params_list.pop(i))
            break
    return params_list


def add_param_to_signature(function: Callable, new_param: Parameter):
    """Add additional Parameter to function signature."""
    old_sig = inspect.signature(function)
    old_sig_list_repr = list(old_sig.parameters.values())
    # If new_param is already in signature, do not add it again.
    if any(param.name == new_param.name for param in old_sig_list_repr):
        return old_sig
    new_params = sort_params_list(old_sig_list_repr + [new_param])
    new_sig = old_sig.replace(parameters=new_params)
    return new_sig


def is_tracing_enabled() -> bool:
    """Checks environment variable feature flag to see if tracing is turned on.
    Tracing is off by default."""
    return _global_is_tracing_enabled


class ImportFromStringError(Exception):
    pass


def import_from_string(import_str: Union[ModuleType, str]) -> ModuleType:
    """Given a string that is in format "<module>:<attribute>",
    import the attribute."""
    if not isinstance(import_str, str):
        return import_str

    module_str, _, attrs_str = import_str.partition(":")
    if not module_str or not attrs_str:
        message = ('Import string "{import_str}" must be in format'
                   '"<module>:<attribute>".')
        raise ImportFromStringError(message.format(import_str=import_str))

    try:
        module = importlib.import_module(module_str)
    except ImportError as exc:
        if exc.name != module_str:
            raise exc from None
        message = 'Could not import module "{module_str}".'
        raise ImportFromStringError(message.format(module_str=module_str))

    instance = module
    try:
        for attr_str in attrs_str.split("."):
            instance = getattr(instance, attr_str)
    except AttributeError:
        message = 'Attribute "{attrs_str}" not found in module "{module_str}".'
        raise ImportFromStringError(
            message.format(attrs_str=attrs_str, module_str=module_str))

    return instance


class DictPropagator:
    def inject_current_context() -> Dict[Any, Any]:
        """Inject trace context into otel propagator."""
        context_dict: Dict[Any, Any] = {}
        _opentelemetry.propagate.inject(context_dict)
        return context_dict

    def extract(context_dict: Dict[Any, Any]) -> "_opentelemetry.Context":
        """Given a trace context, extract as a Context."""
        return cast(_opentelemetry.Context,
                    _opentelemetry.propagate.extract(context_dict))


@contextmanager
def use_context(parent_context: "_opentelemetry.Context"
                ) -> Generator[None, None, None]:
    """Uses the Ray trace context for the span."""
    if parent_context is not None:
        new_context = parent_context
    else:
        new_context = _opentelemetry.Context()
    token = _opentelemetry.context.attach(new_context)
    try:
        yield
    finally:
        _opentelemetry.context.detach(token)


def _function_hydrate_span_args(func: Callable[..., Any]):
    """Get the Attributes of the function that will be reported as attributes
    in the trace."""
    runtime_context = get_runtime_context().get()

    span_args = {
        "ray.remote": "function",
        "ray.function": func,
        "ray.pid": str(os.getpid()),
        "ray.job_id": runtime_context["job_id"].hex(),
        "ray.node_id": runtime_context["node_id"].hex(),
    }

    # We only get task ID for workers
    if ray.worker.global_worker.mode == ray.worker.WORKER_MODE:
        task_id = (runtime_context["task_id"].hex()
                   if runtime_context["task_id"] else None)
        if task_id:
            span_args["ray.task_id"] = task_id

    worker_id = getattr(ray.worker.global_worker, "worker_id", None)
    if worker_id:
        span_args["ray.worker_id"] = worker_id.hex()

    return span_args


def _function_span_producer_name(func: Callable[..., Any]) -> str:
    """Returns the function span name that has span kind of producer."""
    args = _function_hydrate_span_args(func)
    name = args["ray.function"]

    return f"{name} ray.remote"


def _function_span_consumer_name(func: Callable[..., Any]) -> str:
    """Returns the function span name that has span kind of consumer."""
    args = _function_hydrate_span_args(func)
    name = args["ray.function"]

    return f"{name} ray.remote_worker"


def _actor_hydrate_span_args(class_: _nameable, method: _nameable):
    """Get the Attributes of the actor that will be reported as attributes
    in the trace."""
    if callable(class_):
        class_ = class_.__name__
    if callable(method):
        method = method.__name__

    runtime_context = get_runtime_context().get()

    span_args = {
        "ray.remote": "actor",
        "ray.actor_class": class_,
        "ray.actor_method": method,
        "ray.function": f"{class_}.{method}",
        "ray.pid": str(os.getpid()),
        "ray.job_id": runtime_context["job_id"].hex(),
        "ray.node_id": runtime_context["node_id"].hex(),
    }

    # We only get actor ID for workers
    if ray.worker.global_worker.mode == ray.worker.WORKER_MODE:
        actor_id = (runtime_context["actor_id"].hex()
                    if runtime_context["actor_id"] else None)

        if actor_id:
            span_args["ray.actor_id"] = actor_id

    worker_id = getattr(ray.worker.global_worker, "worker_id", None)
    if worker_id:
        span_args["ray.worker_id"] = worker_id.hex()

    return span_args


def _actor_span_producer_name(class_: _nameable, method: _nameable) -> str:
    """Returns the actor span name that has span kind of producer."""
    args = _actor_hydrate_span_args(class_, method)
    assert args is not None
    name = args["ray.function"]

    return f"{name} ray.remote"


def _actor_span_consumer_name(class_: _nameable, method: _nameable) -> str:
    """Returns the actor span name that has span kind of consumer."""
    args = _actor_hydrate_span_args(class_, method)
    assert args is not None
    name = args["ray.function"]

    return f"{name} ray.remote_worker"


def _tracing_task_invocation(method):
    """Trace the execution of a remote task. Inject
    the current span context into kwargs for propagation."""

    @wraps(method)
    def _invocation_remote_span(
            self,
            args: Any = None,  # from tracing
            kwargs: MutableMapping[Any, Any] = None,  # from tracing
            *_args: Any,  # from Ray
            **_kwargs: Any,  # from Ray
    ) -> Any:
        # If tracing feature flag is not on, perform a no-op
        if not is_tracing_enabled():
            return method(self, args, kwargs, *_args, **_kwargs)
        assert "_ray_trace_ctx" not in kwargs

        tracer = _opentelemetry.trace.get_tracer(__name__)
        with tracer.start_as_current_span(
                _function_span_producer_name(self._function_name),
                kind=_opentelemetry.trace.SpanKind.PRODUCER,
                attributes=_function_hydrate_span_args(self._function_name),
        ):
            # Inject a _ray_trace_ctx as a dictionary
            kwargs["_ray_trace_ctx"] = DictPropagator.inject_current_context()
            return method(self, args, kwargs, *_args, **_kwargs)

    return _invocation_remote_span


def _inject_tracing_into_function(function):
    """Wrap the function argument passed to RemoteFunction's __init__ so that
    future execution of that function will include tracing.
    Use the provided trace context from kwargs.
    """
    # Add _ray_trace_ctx to function signature
    setattr(
        function, "__signature__",
        add_param_to_signature(
            function,
            inspect.Parameter(
                "_ray_trace_ctx", inspect.Parameter.KEYWORD_ONLY,
                default=None)))

    @wraps(function)
    def _function_with_tracing(
            *args: Any,
            _ray_trace_ctx: Optional[Dict[str, Any]] = None,
            **kwargs: Any,
    ) -> Any:
        # If tracing feature flag is not on, perform a no-op
        if not is_tracing_enabled():
            return function(*args, **kwargs)

        tracer = _opentelemetry.trace.get_tracer(__name__)

        assert _ray_trace_ctx is not None, (
            f"Missing ray_trace_ctx!: {args}, {kwargs}")

        function_name = function.__module__ + "." + function.__name__

        # Retrieves the context from the _ray_trace_ctx dictionary we injected
        with use_context(DictPropagator.extract(
                _ray_trace_ctx)), tracer.start_as_current_span(
                    _function_span_consumer_name(function_name),
                    kind=_opentelemetry.trace.SpanKind.CONSUMER,
                    attributes=_function_hydrate_span_args(function_name),
                ):
            return function(*args, **kwargs)

    return _function_with_tracing


def _tracing_actor_creation(method):
    """Trace the creation of an actor. Inject
    the current span context into kwargs for propagation."""

    @wraps(method)
    def _invocation_actor_class_remote_span(
            self,
            args: Any = tuple(),  # from tracing
            kwargs: MutableMapping[Any, Any] = {},  # from tracing
            *_args: Any,  # from Ray
            **_kwargs: Any,  # from Ray
    ):
        if kwargs is None:
            kwargs = {}
        # If tracing feature flag is not on, perform a no-op
        if not is_tracing_enabled():
            return method(self, args, kwargs, *_args, **_kwargs)

        class_name = self.__ray_metadata__.class_name
        method_name = "__init__"
        assert "_ray_trace_ctx" not in _kwargs
        tracer = _opentelemetry.trace.get_tracer(__name__)
        with tracer.start_as_current_span(
                name=_actor_span_producer_name(class_name, method_name),
                kind=_opentelemetry.trace.SpanKind.PRODUCER,
                attributes=_actor_hydrate_span_args(class_name, method_name),
        ) as span:
            # Inject a _ray_trace_ctx as a dictionary
            kwargs["_ray_trace_ctx"] = DictPropagator.inject_current_context()

            result = method(self, args, kwargs, *_args, **_kwargs)

            span.set_attribute("ray.actor_id", result._ray_actor_id.hex())

            return result

    return _invocation_actor_class_remote_span


def _tracing_actor_method_invocation(method):
    """Trace the invocation of an actor method."""

    @wraps(method)
    def _start_span(
            self,
            args: Sequence[Any] = None,
            kwargs: MutableMapping[Any, Any] = None,
            *_args: Any,
            **_kwargs: Any,
    ) -> Any:
        # If tracing feature flag is not on, perform a no-op
        if not is_tracing_enabled():
            return method(self, args, kwargs, *_args, **_kwargs)

        class_name = (self._actor_ref()
                      ._ray_actor_creation_function_descriptor.class_name)
        method_name = self._method_name
        assert "_ray_trace_ctx" not in _kwargs

        tracer = _opentelemetry.trace.get_tracer(__name__)
        with tracer.start_as_current_span(
                name=_actor_span_producer_name(class_name, method_name),
                kind=_opentelemetry.trace.SpanKind.PRODUCER,
                attributes=_actor_hydrate_span_args(class_name, method_name),
        ) as span:
            # Inject a _ray_trace_ctx as a dictionary
            kwargs["_ray_trace_ctx"] = DictPropagator.inject_current_context()

            span.set_attribute("ray.actor_id",
                               self._actor_ref()._ray_actor_id.hex())

            return method(self, args, kwargs, *_args, **_kwargs)

    return _start_span


def _inject_tracing_into_class(_cls):
    """Given a class that will be made into an actor,
    inject tracing into all of the methods."""

    def span_wrapper(method: Callable[..., Any]) -> Any:
        def _resume_span(
                self: Any,
                *_args: Any,
                _ray_trace_ctx: Optional[Dict[str, Any]] = None,
                **_kwargs: Any,
        ) -> Any:
            """
            Wrap the user's function with a function that
            will extract the trace context
            """
            # If tracing feature flag is not on, perform a no-op
            if not is_tracing_enabled():
                return method(self, *_args, **_kwargs)

            tracer: _opentelemetry.trace.Tracer = _opentelemetry.trace.\
                get_tracer(__name__)

            # Retrieves the context from the _ray_trace_ctx dictionary we
            # injected, or starts a new context
            if _ray_trace_ctx:
                with use_context(DictPropagator.extract(
                        _ray_trace_ctx)), tracer.start_as_current_span(
                            _actor_span_consumer_name(self.__class__.__name__,
                                                      method),
                            kind=_opentelemetry.trace.SpanKind.CONSUMER,
                            attributes=_actor_hydrate_span_args(
                                self.__class__.__name__, method),
                        ):
                    return method(self, *_args, **_kwargs)
            else:
                with tracer.start_as_current_span(
                        _actor_span_consumer_name(self.__class__.__name__,
                                                  method),
                        kind=_opentelemetry.trace.SpanKind.CONSUMER,
                        attributes=_actor_hydrate_span_args(
                            self.__class__.__name__, method),
                ):
                    return method(self, *_args, **_kwargs)

        return _resume_span

    def async_span_wrapper(method: Callable[..., Any]) -> Any:
        async def _resume_span(
                self: Any,
                *_args: Any,
                _ray_trace_ctx: Optional[Dict[str, Any]] = None,
                **_kwargs: Any,
        ) -> Any:
            """
            Wrap the user's function with a function that
            will extract the trace context
            """
            # If tracing feature flag is not on, perform a no-op
            if not is_tracing_enabled():
                return await method(self, *_args, **_kwargs)

            tracer = _opentelemetry.trace.get_tracer(__name__)

            # Retrieves the context from the _ray_trace_ctx dictionary we
            # injected, or starts a new context
            if _ray_trace_ctx:
                with use_context(DictPropagator.extract(
                        _ray_trace_ctx)), tracer.start_as_current_span(
                            _actor_span_consumer_name(self.__class__.__name__,
                                                      method.__name__),
                            kind=_opentelemetry.trace.SpanKind.CONSUMER,
                            attributes=_actor_hydrate_span_args(
                                self.__class__.__name__, method.__name__),
                        ):
                    return await method(self, *_args, **_kwargs)
            else:
                with tracer.start_as_current_span(
                        _actor_span_consumer_name(self.__class__.__name__,
                                                  method.__name__),
                        kind=_opentelemetry.trace.SpanKind.CONSUMER,
                        attributes=_actor_hydrate_span_args(
                            self.__class__.__name__, method.__name__),
                ):
                    return await method(self, *_args, **_kwargs)

        return _resume_span

    methods = inspect.getmembers(_cls, is_function_or_method)
    for name, method in methods:
        # Skip tracing for staticmethod or classmethod, because these method
        # might not be called directly by remote calls. Additionally, they are
        # tricky to get wrapped and unwrapped.
        if (is_static_method(_cls, name) or is_class_method(method)
                or not is_tracing_enabled()):
            continue

        # Add _ray_trace_ctx to method signature
        setattr(
            method, "__signature__",
            add_param_to_signature(
                method,
                inspect.Parameter(
                    "_ray_trace_ctx",
                    inspect.Parameter.KEYWORD_ONLY,
                    default=None)))

        if inspect.iscoroutinefunction(method):
            # If the method was async, swap out sync wrapper into async
            wrapped_method = wraps(method)(async_span_wrapper(method))
        else:
            wrapped_method = wraps(method)(span_wrapper(method))

        setattr(_cls, name, wrapped_method)

    return _cls
