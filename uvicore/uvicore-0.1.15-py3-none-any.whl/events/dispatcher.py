import re
import uvicore
import inspect
import asyncio
from uvicore.typing import Dict, List, Any, Union, Callable, Tuple
from uvicore.support.dumper import dump, dd
from types import SimpleNamespace as obj
from collections import namedtuple
from uvicore.contracts import Dispatcher as DispatcherInterface
from uvicore.support import module
from uvicore.support.concurrency import run_in_threadpool

#from uvicore.contracts import Event as EventInterface
# from prettyprinter import pretty_call, register_pretty
# class EventInfo(EventInterface):
#     """Event Definition"""
#     # These class level properties for for type annotations only.
#     # They do not restrict of define valid properties like a dataclass would.
#     # This is still a fully dynamic SuperDict!
#     name: str
#     description: str
#     dynamic: bool
#     is_async: bool
#     options: Dict


# @register_pretty(EventInfo)
# def pretty_entity(value, ctx):
#     """Custom pretty printer for my SuperDict"""
#     # This printer removes the class name uvicore.types.Dict and makes it print
#     # with a regular {.  This really cleans up the output!

#     #return pretty_call(ctx, 'Dict', **value)
#     #return pretty_call(ctx, 'Dict', value.to_dict())  # Does show nested dicts as SuperDicts
#     return pretty_call(ctx, 'EventInfo', dict(**value))

@uvicore.service('uvicore.events.dispatcher.Dispatcher',
    aliases=['Dispatcher', 'dispatcher', 'Event', 'event'],
    singleton=True,
)
class Dispatcher(DispatcherInterface):
    """Event Dispatcher private class.

    Do not import from this location.
    Use the uvicore.events singleton global instead."""

    # @property
    # def events(self) -> Dict[str, EventInfo]:
    #     """Dictionary of all registered events in uvicore and all packages"""
    #     return self._events

    @property
    def listeners(self) -> Dict[str, List]:
        """Dictionary of all listeners for each event"""
        return self._listeners

    @property
    def wildcards(self) -> List:
        """List of all wildcard listeners"""
        return self._wildcards

    def __init__(self) -> None:
        self._events: Dict[str, EventInfo] = Dict()
        self._listeners: Dict[str, List] = Dict()
        self._wildcards: List = []

    # def event(self, event: Union[str, Callable]) -> EventInfo:
    #     """Get one known (pre-registered) EventInfo by str name or class"""
    #     if type(event) == str:
    #         # Get event by a string name
    #         name = event
    #     else:
    #         # Get event by a class, use the class name as the event string name
    #         #name = str(event.__class__).split("'")[1]
    #         name = event.name
    #     if name in self.events:
    #         return self.events.get(name)
    #     else:
    #         # This event is NOT registered, but we still want it to work
    #         # because of all the dynamic events like ORM makes
    #         # So create a fake event meta
    #         return Dict({
    #             'name': name
    #         })

    def event_listeners(self, event: str) -> List:
        """Get all listeners for an event including wildcard"""
        listeners = []
        if event in self.listeners:
            listeners += self.listeners[event]

        for wildcard in self.wildcards:
            regex = wildcard
            #regex = wildcard.replace('*', '.*')
            #dump(regex)
            if re.search(regex, event):
                listeners += self.listeners[wildcard]

        return listeners

    # def register(self, events: Dict[str, Dict] = None, *, name: str = None, description: str = None, dynamic: bool = False, is_async: bool = False, options: Dict = {}):
    #     """Register an event with the system.  Retrieve with .events property"""

    #     event = EventInfo({
    #         'name': name,
    #         'description': description,
    #         'is_async': is_async,
    #         'dynamic': dynamic,
    #         'options': options,
    #     })

    #     if events:
    #         # Register events as a dictionary
    #         for (key, value) in events.items():
    #             if 'name' not in value: value['name'] = key

    #             # Overwrite existing event, last one wins
    #             self._events[key] = EventInfo(value).defaults(event)
    #     else:
    #         # Register single event as method params
    #         self._events[name] = event

    def listen(self, events: Union[str, List], listener: Union[str, Callable] = None) -> None:
        """Decorator or method to append a listener (string or Callable) callback to one or more events."""
        def handle(events, listener):
            if type(events) != list: events = [events]

            # Do NOT check self.events for listener verification becuase self.events
            # is probably empty at this stage.  All registrations and listeners are
            # applied in service provider register() methods so cannot rely on
            # self.events being full and complete.  This means we cannot properly
            # match wildcard events to actual events.

            # Expand all wildcards
            for event in events:
                if type(event) != str: event = event.name
                if event not in self.listeners:
                    self._listeners[event] = []
                self._listeners[event].append(listener)
                if '*' in event:
                    self._wildcards.append(event)

        # Method access
        if listener: return handle(events, listener)

        # Decorator access
        def decorator(func):
            handle(events, func)
            return func
        return decorator

    def handle(self, events: Union[str, List], listener: Union[str, Callable] = None) -> None:
        """Decorator or method to append a listener (string or Callable) callback to one or more events.  Alias to listen()."""
        return self.listen(events, listener)

    def subscribe(self, listener: Union[str, Callable]) -> None:
        """Add a subscription class which handles both registration and listener callbacks"""
        try:
            if type(listener) == str:
                module.load(listener).object().subscribe(uvicore.events)
            else:
                listener.subscribe(uvicore.events)
        except ModuleNotFoundError:
            pass

    def dispatch(self, event: Union[str, Callable], payload: Dict = {}) -> None:
        """Fire off an event and run all listener callbacks"""

        # Get dispatcher method for this event
        dispatch, params = self._get_dispatcher(event, payload, is_async=False)

        # Dispatch this event
        dispatch(*params)

    async def dispatch_async(self, event: Union[str, Callable], payload: Dict = {}) -> None:
        """Async fire off an event and run all async listener callbacks"""

        # Get dispatcher method for this event
        dispatch, params = self._get_dispatcher(event, payload, is_async=True)

        # Dispatch this event
        await dispatch(*params)

    async def codispatch(self, event: Union[str, Callable], payload: Dict = {}) -> None:
        """Async fire off an event and run all async listener callbacks.  Alias for dispatch_async()."""
        return await self.dispatch_async(event, payload)

    def _dispatch(self, event: Union[str, Callable], payload: Dict = {}) -> None:
        """Dispatch an event by fireing off all listeners/handlers"""
        (event, handlers) = self._get_handlers(event, payload)
        for handler in handlers:
            handler(event)

    async def _dispatch_async(self, event: Union[str, Callable], payload: Dict = {}) -> None:
        """Dispatch an event by fireing off all listeners/handlers"""
        (payload, handlers) = self._get_handlers(event, payload)
        for handler in handlers:
            if asyncio.iscoroutinefunction(handler) or asyncio.iscoroutinefunction(handler.__call__):
                await handler(event)
            else:
                # Listener/handler is NOT async but was called from await, lets throw in thread pool
                await run_in_threadpool(handler, event)

    def _get_dispatcher(self, event: Union[str, Callable], payload: Dict = {}, is_async: bool = False) -> Tuple:
        """Get dispatcher method for this event"""
        # This function determines the proper dispatching method for this event.
        # If event is a string, we use self._dispatch
        # If event is a class we call that classes .dispatch method
        method = None
        params = [event, payload]
        if type(event) == str:
            if '-' in event or '{' in event:
                # String event (we know because classes can't have dashes or {.
                # This is how we name dynamic string based events like per model or table...
                method = self._dispatch_async if is_async else self.dispatch
            else:
                # See if string event has a matching class.  If so, import and dispatch it
                try:
                    event = module.load(event).object(**payload)
                    params = []
                    method = event.dispatch_async if is_async else event.dispatch
                except:
                    # No class found for this string.  This is OK because events can
                    # be strings without matching classes.  Dispatch it anyway
                    method = self._dispatch_async if is_async else self._dispatch
        else:
            # Event is an event class INSTANCE.  Call the actual classes dispatch method
            # in case the user overrode it, we still execute it
            params = []
            method = event.dispatch_async if is_async else event.dispatch

        # Return tuple of dispatcher method and params
        return (method, params)

    def _get_handlers(self, event: Union[str, Callable], payload: Dict = {}) -> Tuple:
        """Get all listener/handlers and fix up payload"""
        # Get event by string name or class inspection
        #event_meta = self.event(event)

        if type(event) == str:
            # String based event, merge payload with default event
            event = Dict(payload).merge({
                'name': event,
                'description': 'String based dynamic event.'
            })

        # Payload default is a SuperDict
        #payload = Dict(payload)

        # If event is a class, payload is the class instance
        #if type(event) != str: payload = event

        # Get listener methods (dynamic import if string)
        listeners = self.event_listeners(event.name)
        handlers = []
        for handler in listeners:
            if type(handler) == str:
                # handler is a string to a listener class with handle() method
                try:
                    #cls = module.load(listener).object(uvicore.app)
                    cls = module.load(handler).object()
                    handlers.append(cls)
                    #handlers.append(cls.handle)
                except ModuleNotFoundError:
                    # Bad handler, handler will never fire
                    continue
            else:
                # handler is a Class
                if inspect.isclass(handler): handler = handler()

                # Listener is a Callable (if was a class, NOW its callable)
                handlers.append(handler)

        # Return tuple of event and handlers
        #return (event_meta, payload, handlers)
        return (event, handlers)


# IoC Class Instance
# **Not meant to be imported from here**.  Use the uvicore.events singleton global instead.
# Only here because uvicore bootstrap needs to import it without a service provider.
# By using the default bind and make feature of the IoC we can swap the implimentation
# at a high bootstrap level using our app configs 'bindings' dictionary.
# The only two classes that do this are Application and the event Dispatcher.
#Dispatcher: _Dispatcher = uvicore.ioc.make('Dispatcher', _Dispatcher, singleton=True, aliases=['dispatcher', 'Event', 'event', 'Events', 'events'])
