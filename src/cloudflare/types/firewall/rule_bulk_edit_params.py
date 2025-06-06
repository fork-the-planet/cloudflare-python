# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleBulkEditParams"]


class RuleBulkEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    body: Required[object]
