# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.schema_validation import setting_edit_params, setting_update_params
from ....types.schema_validation.setting_get_response import SettingGetResponse
from ....types.schema_validation.setting_edit_response import SettingEditResponse
from ....types.schema_validation.setting_update_response import SettingUpdateResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingUpdateResponse:
        """
        Update global schema validation settings

        Args:
          zone_id: Identifier.

          validation_default_mitigation_action:
              The default mitigation action used Mitigation actions are as follows:

              - `"log"` - log request when request does not conform to schema
              - `"block"` - deny access to the site when request does not conform to schema
              - `"none"` - skip running schema validation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `"none"` - skip running schema validation entirely for the request
              - `null` - clears any existing override

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/schema_validation/settings",
            body=maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingUpdateResponse], ResultWrapper[SettingUpdateResponse]),
        )

    def edit(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"] | NotGiven = NOT_GIVEN,
        validation_override_mitigation_action: Optional[Literal["none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingEditResponse:
        """
        Edit global schema validation settings

        Args:
          zone_id: Identifier.

          validation_default_mitigation_action:
              The default mitigation action used Mitigation actions are as follows:

              - `"log"` - log request when request does not conform to schema
              - `"block"` - deny access to the site when request does not conform to schema
              - `"none"` - skip running schema validation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `"none"` - skip running schema validation entirely for the request
              - `null` - clears any existing override

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/schema_validation/settings",
            body=maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingEditResponse], ResultWrapper[SettingEditResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetResponse:
        """
        Get global schema validation settings

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/schema_validation/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingGetResponse], ResultWrapper[SettingGetResponse]),
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingUpdateResponse:
        """
        Update global schema validation settings

        Args:
          zone_id: Identifier.

          validation_default_mitigation_action:
              The default mitigation action used Mitigation actions are as follows:

              - `"log"` - log request when request does not conform to schema
              - `"block"` - deny access to the site when request does not conform to schema
              - `"none"` - skip running schema validation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `"none"` - skip running schema validation entirely for the request
              - `null` - clears any existing override

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/schema_validation/settings",
            body=await async_maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingUpdateResponse], ResultWrapper[SettingUpdateResponse]),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"] | NotGiven = NOT_GIVEN,
        validation_override_mitigation_action: Optional[Literal["none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingEditResponse:
        """
        Edit global schema validation settings

        Args:
          zone_id: Identifier.

          validation_default_mitigation_action:
              The default mitigation action used Mitigation actions are as follows:

              - `"log"` - log request when request does not conform to schema
              - `"block"` - deny access to the site when request does not conform to schema
              - `"none"` - skip running schema validation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `"none"` - skip running schema validation entirely for the request
              - `null` - clears any existing override

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/schema_validation/settings",
            body=await async_maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingEditResponse], ResultWrapper[SettingEditResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetResponse:
        """
        Get global schema validation settings

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/schema_validation/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SettingGetResponse], ResultWrapper[SettingGetResponse]),
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.edit = to_raw_response_wrapper(
            settings.edit,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._settings.operations)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.edit = async_to_raw_response_wrapper(
            settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._settings.operations)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.edit = to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._settings.operations)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.edit = async_to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._settings.operations)
