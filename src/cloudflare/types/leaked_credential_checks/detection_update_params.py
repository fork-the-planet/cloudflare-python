# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DetectionUpdateParams"]


class DetectionUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    password: str
    """Defines ehe ruleset expression to use in matching the password in a request."""

    username: str
    """Defines the ruleset expression to use in matching the username in a request."""
