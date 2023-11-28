"""SPKP Policy."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StaticPkpPolicyData:
    """
    Dataclass for SPKP Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#staticpkppolicy
    """

    status: str
    """SPKP status"""

    error: str | None
    """Error message, when the policy is invalid"""

    includeSubDomains: bool | None
    """True if the includeSubDomains directive is set else false"""

    reportUri: str | None
    """The report-uri value from the policy"""

    pins: list[dict]
    """List of all pins used by the policy"""

    matchedPins: list[dict]
    """List of pins that match the current configuration"""

    forbiddenPins: list[dict]
    """List of all forbidden pins used by policy"""

    matchedForbiddenPins: list[dict]
    """List of forbidden pins that match the current configuration"""
