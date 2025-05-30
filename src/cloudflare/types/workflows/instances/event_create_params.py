# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    instance_id: Required[str]

    body: object
