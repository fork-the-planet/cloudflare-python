# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AppEditParams"]


class AppEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    hostnames: List[str]
    """FQDNs to associate with traffic decisions."""

    ip_subnets: List[str]
    """IPv4 CIDRs to associate with traffic decisions.

    (IPv6 CIDRs are currently unsupported)
    """

    name: str
    """Display name for the app."""

    type: str
    """Category of the app."""
