# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.load_balancers.pools import health_create_params
from ....types.load_balancers.pools.health_get_response import HealthGetResponse
from ....types.load_balancers.pools.health_create_response import HealthCreateResponse

__all__ = ["HealthResource", "AsyncHealthResource"]


class HealthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HealthResourceWithStreamingResponse(self)

    def create(
        self,
        pool_id: str,
        *,
        account_id: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        expected_codes: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        load_balancer_monitor_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCreateResponse:
        """Preview pool health using provided monitor details.

        The returned preview_id can
        be used in the preview endpoint to retrieve the results.

        Args:
          account_id: Identifier

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          load_balancer_monitor_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._post(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/preview",
            body=maybe_transform(
                {
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "expected_codes": expected_codes,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "load_balancer_monitor_timeout": load_balancer_monitor_timeout,
                    "type": type,
                },
                health_create_params.HealthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthCreateResponse], ResultWrapper[HealthCreateResponse]),
        )

    def get(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthGetResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthGetResponse], ResultWrapper[HealthGetResponse]),
        )


class AsyncHealthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHealthResourceWithStreamingResponse(self)

    async def create(
        self,
        pool_id: str,
        *,
        account_id: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        expected_codes: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        load_balancer_monitor_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCreateResponse:
        """Preview pool health using provided monitor details.

        The returned preview_id can
        be used in the preview endpoint to retrieve the results.

        Args:
          account_id: Identifier

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          load_balancer_monitor_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._post(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/preview",
            body=await async_maybe_transform(
                {
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "expected_codes": expected_codes,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "load_balancer_monitor_timeout": load_balancer_monitor_timeout,
                    "type": type,
                },
                health_create_params.HealthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthCreateResponse], ResultWrapper[HealthCreateResponse]),
        )

    async def get(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthGetResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthGetResponse], ResultWrapper[HealthGetResponse]),
        )


class HealthResourceWithRawResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.create = to_raw_response_wrapper(
            health.create,
        )
        self.get = to_raw_response_wrapper(
            health.get,
        )


class AsyncHealthResourceWithRawResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.create = async_to_raw_response_wrapper(
            health.create,
        )
        self.get = async_to_raw_response_wrapper(
            health.get,
        )


class HealthResourceWithStreamingResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.create = to_streamed_response_wrapper(
            health.create,
        )
        self.get = to_streamed_response_wrapper(
            health.get,
        )


class AsyncHealthResourceWithStreamingResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.create = async_to_streamed_response_wrapper(
            health.create,
        )
        self.get = async_to_streamed_response_wrapper(
            health.get,
        )
