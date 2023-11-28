"""HPKP Policy."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HpkpPolicyData:
    """
    Dataclass for HPKP Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hpkppolicy
    """

    header: str | None
    """The contents of the HPKP response header, if present"""

    status: str
    """HPKP status"""

    error: str | None
    """Error message, when the policy is invalid"""

    maxAge: int | None
    """The max-age value from the policy"""

    includeSubDomains: bool | None
    """True if the includeSubDomains directive is set; null otherwise"""

    reportUri: str | None
    """The report-uri value from the policy"""

    pins: list[dict]
    """List of all pins used by the policy"""

    matchedPins: list[dict]
    """List of pins that match the current configuration"""

    directives: list[dict]
    """List of raw policy directives (name-value pairs)"""
