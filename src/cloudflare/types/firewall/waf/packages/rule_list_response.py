# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from .waf_rule_group import WAFRuleGroup
from .allowed_modes_anomaly import AllowedModesAnomaly

__all__ = [
    "RuleListResponse",
    "WAFManagedRulesAnomalyRule",
    "WAFManagedRulesTraditionalDenyRule",
    "WAFManagedRulesTraditionalAllowRule",
]


class WAFManagedRulesAnomalyRule(BaseModel):
    id: str
    """Defines the unique identifier of the WAF rule."""

    allowed_modes: List[AllowedModesAnomaly]
    """Defines the available modes for the current WAF rule.

    Applies to anomaly detection WAF rules.
    """

    description: str
    """Defines the public description of the WAF rule."""

    group: WAFRuleGroup
    """Defines the rule group to which the current WAF rule belongs."""

    mode: AllowedModesAnomaly
    """Defines the mode anomaly.

    When set to `on`, the current WAF rule will be used when evaluating the request.
    Applies to anomaly detection WAF rules.
    """

    package_id: str
    """Defines the unique identifier of a WAF package."""

    priority: str
    """
    Defines the order in which the individual WAF rule is executed within its rule
    group.
    """


class WAFManagedRulesTraditionalDenyRule(BaseModel):
    id: str
    """Defines the unique identifier of the WAF rule."""

    allowed_modes: List[Literal["default", "disable", "simulate", "block", "challenge"]]
    """Defines the list of possible actions of the WAF rule when it is triggered."""

    default_mode: Literal["disable", "simulate", "block", "challenge"]
    """Defines the default action/mode of a rule."""

    description: str
    """Defines the public description of the WAF rule."""

    group: WAFRuleGroup
    """Defines the rule group to which the current WAF rule belongs."""

    mode: Literal["default", "disable", "simulate", "block", "challenge"]
    """Defines the action that the current WAF rule will perform when triggered.

    Applies to traditional (deny) WAF rules.
    """

    package_id: str
    """Defines the unique identifier of a WAF package."""

    priority: str
    """
    Defines the order in which the individual WAF rule is executed within its rule
    group.
    """


class WAFManagedRulesTraditionalAllowRule(BaseModel):
    id: str
    """Defines the unique identifier of the WAF rule."""

    allowed_modes: List[Literal["on", "off"]]
    """Defines the available modes for the current WAF rule."""

    description: str
    """Defines the public description of the WAF rule."""

    group: WAFRuleGroup
    """Defines the rule group to which the current WAF rule belongs."""

    mode: Literal["on", "off"]
    """When set to `on`, the current rule will be used when evaluating the request.

    Applies to traditional (allow) WAF rules.
    """

    package_id: str
    """Defines the unique identifier of a WAF package."""

    priority: str
    """
    Defines the order in which the individual WAF rule is executed within its rule
    group.
    """


RuleListResponse: TypeAlias = Union[
    WAFManagedRulesAnomalyRule, WAFManagedRulesTraditionalDenyRule, WAFManagedRulesTraditionalAllowRule
]
