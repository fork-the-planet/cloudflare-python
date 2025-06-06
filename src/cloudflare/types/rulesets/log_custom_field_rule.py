# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .logging import Logging
from ..._models import BaseModel

__all__ = [
    "LogCustomFieldRule",
    "ActionParameters",
    "ActionParametersCookieField",
    "ActionParametersRawResponseField",
    "ActionParametersRequestField",
    "ActionParametersResponseField",
    "ActionParametersTransformedRequestField",
    "ExposedCredentialCheck",
    "Ratelimit",
]


class ActionParametersCookieField(BaseModel):
    name: str
    """The name of the field."""


class ActionParametersRawResponseField(BaseModel):
    name: str
    """The name of the field."""

    preserve_duplicates: Optional[bool] = None
    """Whether to log duplicate values of the same header."""


class ActionParametersRequestField(BaseModel):
    name: str
    """The name of the field."""


class ActionParametersResponseField(BaseModel):
    name: str
    """The name of the field."""

    preserve_duplicates: Optional[bool] = None
    """Whether to log duplicate values of the same header."""


class ActionParametersTransformedRequestField(BaseModel):
    name: str
    """The name of the field."""


class ActionParameters(BaseModel):
    cookie_fields: Optional[List[ActionParametersCookieField]] = None
    """The cookie fields to log."""

    raw_response_fields: Optional[List[ActionParametersRawResponseField]] = None
    """The raw response fields to log."""

    request_fields: Optional[List[ActionParametersRequestField]] = None
    """The raw request fields to log."""

    response_fields: Optional[List[ActionParametersResponseField]] = None
    """The transformed response fields to log."""

    transformed_request_fields: Optional[List[ActionParametersTransformedRequestField]] = None
    """The transformed request fields to log."""


class ExposedCredentialCheck(BaseModel):
    password_expression: str
    """Expression that selects the password used in the credentials check."""

    username_expression: str
    """Expression that selects the user ID used in the credentials check."""


class Ratelimit(BaseModel):
    characteristics: List[str]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class LogCustomFieldRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["log_custom_field"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[ExposedCredentialCheck] = None
    """Configure checks for exposed credentials."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[Ratelimit] = None
    """An object configuring the rule's ratelimit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
