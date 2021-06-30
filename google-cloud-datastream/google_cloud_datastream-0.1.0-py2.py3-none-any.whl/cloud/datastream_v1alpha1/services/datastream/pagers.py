# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.datastream_v1alpha1.types import datastream
from google.cloud.datastream_v1alpha1.types import datastream_resources


class ListConnectionProfilesPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListConnectionProfilesResponse],
        request: datastream.ListConnectionProfilesRequest,
        response: datastream.ListConnectionProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListConnectionProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[datastream.ListConnectionProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[datastream_resources.ConnectionProfile]:
        for page in self.pages:
            yield from page.connection_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionProfilesAsyncPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListConnectionProfilesResponse]],
        request: datastream.ListConnectionProfilesRequest,
        response: datastream.ListConnectionProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListConnectionProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[datastream.ListConnectionProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[datastream_resources.ConnectionProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connection_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamsPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListStreamsResponse],
        request: datastream.ListStreamsRequest,
        response: datastream.ListStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListStreamsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[datastream.ListStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[datastream_resources.Stream]:
        for page in self.pages:
            yield from page.streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamsAsyncPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListStreamsResponse]],
        request: datastream.ListStreamsRequest,
        response: datastream.ListStreamsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListStreamsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[datastream.ListStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[datastream_resources.Stream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.FetchStaticIpsResponse],
        request: datastream.FetchStaticIpsRequest,
        response: datastream.FetchStaticIpsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.FetchStaticIpsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[datastream.FetchStaticIpsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[str]:
        for page in self.pages:
            yield from page.static_ips

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsAsyncPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.FetchStaticIpsResponse]],
        request: datastream.FetchStaticIpsRequest,
        response: datastream.FetchStaticIpsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.FetchStaticIpsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[datastream.FetchStaticIpsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.static_ips:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListPrivateConnectionsResponse],
        request: datastream.ListPrivateConnectionsRequest,
        response: datastream.ListPrivateConnectionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListPrivateConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[datastream.ListPrivateConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[datastream_resources.PrivateConnection]:
        for page in self.pages:
            yield from page.private_connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsAsyncPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListPrivateConnectionsResponse]],
        request: datastream.ListPrivateConnectionsRequest,
        response: datastream.ListPrivateConnectionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListPrivateConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[datastream.ListPrivateConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[datastream_resources.PrivateConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.private_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListRoutesResponse],
        request: datastream.ListRoutesRequest,
        response: datastream.ListRoutesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListRoutesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListRoutesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[datastream.ListRoutesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[datastream_resources.Route]:
        for page in self.pages:
            yield from page.routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesAsyncPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1alpha1.types.ListRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1alpha1.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListRoutesResponse]],
        request: datastream.ListRoutesRequest,
        response: datastream.ListRoutesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1alpha1.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.datastream_v1alpha1.types.ListRoutesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = datastream.ListRoutesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[datastream.ListRoutesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[datastream_resources.Route]:
        async def async_generator():
            async for page in self.pages:
                for response in page.routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
