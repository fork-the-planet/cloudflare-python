# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OutputCreateParams"]


class OutputCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    stream_key: Required[Annotated[str, PropertyInfo(alias="streamKey")]]
    """The streamKey used to authenticate against an output's target."""

    url: Required[str]
    """The URL an output uses to restream."""

    enabled: bool
    """
    When enabled, live video streamed to the associated live input will be sent to
    the output URL. When disabled, live video will not be sent to the output URL,
    even when streaming to the associated live input. Use this to control precisely
    when you start and stop simulcasting to specific destinations like YouTube and
    Twitch.
    """
