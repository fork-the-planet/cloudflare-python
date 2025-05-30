# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.radar.bgp.leaks import event_list_params
from .....types.radar.bgp.leaks.event_list_response import EventListResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        involved_asn: int | NotGiven = NOT_GIVEN,
        involved_country: str | NotGiven = NOT_GIVEN,
        leak_asn: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["ID", "LEAKS", "PEERS", "PREFIXES", "ORIGINS", "TIME"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[EventListResponse]:
        """
        Retrieves the BGP route leak events.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event.

          format: Format in which results will be returned.

          involved_asn: ASN that is causing or affected by a route leak event.

          involved_country: Country code of a involved ASN in a route leak event.

          leak_asn: The leaking AS of a route leak event.

          page: Current page number, starting from 1.

          per_page: Number of entries per page.

          sort_by: Sorts results by the specified field.

          sort_order: Sort order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/leaks/events",
            page=SyncV4PagePagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "event_id": event_id,
                        "format": format,
                        "involved_asn": involved_asn,
                        "involved_country": involved_country,
                        "leak_asn": leak_asn,
                        "page": page,
                        "per_page": per_page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        involved_asn: int | NotGiven = NOT_GIVEN,
        involved_country: str | NotGiven = NOT_GIVEN,
        leak_asn: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["ID", "LEAKS", "PEERS", "PREFIXES", "ORIGINS", "TIME"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventListResponse, AsyncV4PagePagination[EventListResponse]]:
        """
        Retrieves the BGP route leak events.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event.

          format: Format in which results will be returned.

          involved_asn: ASN that is causing or affected by a route leak event.

          involved_country: Country code of a involved ASN in a route leak event.

          leak_asn: The leaking AS of a route leak event.

          page: Current page number, starting from 1.

          per_page: Number of entries per page.

          sort_by: Sorts results by the specified field.

          sort_order: Sort order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/leaks/events",
            page=AsyncV4PagePagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "event_id": event_id,
                        "format": format,
                        "involved_asn": involved_asn,
                        "involved_country": involved_country,
                        "leak_asn": leak_asn,
                        "page": page,
                        "per_page": per_page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
