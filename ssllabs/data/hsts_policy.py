"""HSTS Policy."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HstsPolicyData:
    """
    Dataclass for HSTS Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hstspolicy
    """

    LONG_MAX_AGE: int
    """This constant contains what SSL Labs considers to be sufficiently large max-age value"""

    header: str | None
    """The contents of the HSTS response header, if present"""

    status: str
    """HSTS status"""

    error: str | None
    """Error message when error is encountered, null otherwise"""

    maxAge: int | None
    """The max-age value specified in the policy; null if policy is missing or invalid or on parsing error"""

    includeSubDomains: bool | None
    """True if the includeSubDomains directive is set; null otherwise"""

    preload: bool | None
    """True if the preload directive is set; null otherwise"""

    directives: dict | None
    """List of raw policy directives"""
