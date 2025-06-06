# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ViewEditParams"]


class ViewEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    name: str
    """The name of the view."""

    zones: List[str]
    """The list of zones linked to this view."""
