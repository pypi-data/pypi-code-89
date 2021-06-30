from __future__ import absolute_import

import os.path
import sys
import threading
from typing import Optional
from typing import Tuple

import attr
from six.moves import _thread

from ddtrace.internal import compat
from ddtrace.profiling import collector
from ddtrace.profiling import event
from ddtrace.profiling.collector import _traceback
from ddtrace.utils import attr as attr_utils
from ddtrace.vendor import wrapt


@event.event_class
class LockEventBase(event.StackBasedEvent):
    """Base Lock event."""

    lock_name = attr.ib(default=None)
    sampling_pct = attr.ib(default=None)


@event.event_class
class LockAcquireEvent(LockEventBase):
    """A lock has been acquired."""

    wait_time_ns = attr.ib(default=None)


@event.event_class
class LockReleaseEvent(LockEventBase):
    """A lock has been released."""

    locked_for_ns = attr.ib(default=None)


def _current_thread():
    # This is a custom version of `threading.current_thread`
    # that does not try # to create a `DummyThread` on `KeyError`.
    ident = _thread.get_ident()
    try:
        thread = threading._active[ident]
    except KeyError:
        name = None
    else:
        name = thread.name
    return ident, name


# We need to know if wrapt is compiled in C or not. If it's not using the C module, then the wrappers function will
# appear in the stack trace and we need to hide it.
if os.environ.get("WRAPT_DISABLE_EXTENSIONS"):
    WRAPT_C_EXT = False
else:
    try:
        import ddtrace.vendor.wrapt._wrappers as _w  # type: ignore[import] # noqa: F401
    except ImportError:
        WRAPT_C_EXT = False
    else:
        WRAPT_C_EXT = True
        del _w


class _ProfiledLock(wrapt.ObjectProxy):
    def __init__(self, wrapped, recorder, tracer, max_nframes, capture_sampler):
        wrapt.ObjectProxy.__init__(self, wrapped)
        self._self_recorder = recorder
        self._self_tracer = tracer
        self._self_max_nframes = max_nframes
        self._self_capture_sampler = capture_sampler
        frame = sys._getframe(2 if WRAPT_C_EXT else 3)
        code = frame.f_code
        self._self_name = "%s:%d" % (os.path.basename(code.co_filename), frame.f_lineno)

    def _get_trace_and_span_info(self):
        # type: (...) -> Tuple[Optional[int], Optional[int], Optional[str], Optional[str]]
        """Return current trace id, span id and trace resource and type."""
        if self._self_tracer is None:
            return (None, None, None, None)

        ctxt = self._self_tracer.current_trace_context()
        if ctxt is None:
            return (None, None, None, None)

        root = self._self_tracer.current_root_span()
        if root is None:
            resource = None
            span_type = None
        else:
            resource = root.resource
            span_type = root.span_type

        return (ctxt.trace_id, ctxt.span_id, resource, span_type)

    def acquire(self, *args, **kwargs):
        if not self._self_capture_sampler.capture():
            return self.__wrapped__.acquire(*args, **kwargs)

        start = compat.monotonic_ns()
        try:
            return self.__wrapped__.acquire(*args, **kwargs)
        finally:
            try:
                end = self._self_acquired_at = compat.monotonic_ns()
                thread_id, thread_name = _current_thread()
                frames, nframes = _traceback.pyframe_to_frames(sys._getframe(1), self._self_max_nframes)
                trace_id, span_id, trace_resource, trace_type = self._get_trace_and_span_info()
                self._self_recorder.push_event(
                    LockAcquireEvent(
                        lock_name=self._self_name,
                        frames=frames,
                        nframes=nframes,
                        thread_id=thread_id,
                        thread_name=thread_name,
                        trace_id=trace_id,
                        span_id=span_id,
                        trace_resource=trace_resource,
                        trace_type=trace_type,
                        wait_time_ns=end - start,
                        sampling_pct=self._self_capture_sampler.capture_pct,
                    )
                )
            except Exception:
                pass

    def release(self, *args, **kwargs):
        try:
            return self.__wrapped__.release(*args, **kwargs)
        finally:
            try:
                if hasattr(self, "_self_acquired_at"):
                    try:
                        end = compat.monotonic_ns()
                        frames, nframes = _traceback.pyframe_to_frames(sys._getframe(1), self._self_max_nframes)
                        thread_id, thread_name = _current_thread()
                        trace_id, span_id, trace_resource, trace_type = self._get_trace_and_span_info()
                        self._self_recorder.push_event(
                            LockReleaseEvent(
                                lock_name=self._self_name,
                                frames=frames,
                                nframes=nframes,
                                thread_id=thread_id,
                                thread_name=thread_name,
                                trace_id=trace_id,
                                span_id=span_id,
                                trace_resource=trace_resource,
                                trace_type=trace_type,
                                locked_for_ns=end - self._self_acquired_at,
                                sampling_pct=self._self_capture_sampler.capture_pct,
                            )
                        )
                    finally:
                        del self._self_acquired_at
            except Exception:
                pass

    acquire_lock = acquire


class FunctionWrapper(wrapt.FunctionWrapper):
    # Override the __get__ method: whatever happens, _allocate_lock is always considered by Python like a "static"
    # method, even when used as a class attribute. Python never tried to "bind" it to a method, because it sees it is a
    # builtin function. Override default wrapt behavior here that tries to detect bound method.
    def __get__(self, instance, owner=None):
        return self


@attr.s
class LockCollector(collector.CaptureSamplerCollector):
    """Record lock usage."""

    nframes = attr.ib(factory=attr_utils.from_env("DD_PROFILING_MAX_FRAMES", 64, int))
    tracer = attr.ib(default=None)

    def _start_service(self):  # type: ignore[override]
        # type: (...) -> None
        """Start collecting `threading.Lock` usage."""
        self.patch()
        super(LockCollector, self)._start_service()

    def _stop_service(self):  # type: ignore[override]
        # type: (...) -> None
        """Stop collecting `threading.Lock` usage."""
        super(LockCollector, self)._stop_service()
        self.unpatch()

    def patch(self):
        # type: (...) -> None
        """Patch the threading module for tracking lock allocation."""
        # We only patch the lock from the `threading` module.
        # Nobody should use locks from `_thread`; if they do so, then it's deliberate and we don't profile.
        self.original = threading.Lock

        def _allocate_lock(wrapped, instance, args, kwargs):
            lock = wrapped(*args, **kwargs)
            return _ProfiledLock(lock, self.recorder, self.tracer, self.nframes, self._capture_sampler)

        threading.Lock = FunctionWrapper(self.original, _allocate_lock)  # type: ignore[misc]

    def unpatch(self):
        # type: (...) -> None
        """Unpatch the threading module for tracking lock allocation."""
        threading.Lock = self.original  # type: ignore[misc]
