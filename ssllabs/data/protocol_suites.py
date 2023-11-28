"""Protocol suites."""
from __future__ import annotations

from dataclasses import dataclass

from .suite import SuiteData


@dataclass
class ProtocolSuitesData:
    """
    Dataclass for protocol suites objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocolsuites
    """

    protocol: int
    """Protocol version."""

    list: list[SuiteData]
    """List of Suite objects"""

    preference: bool | None
    """
    True if the server actively selects cipher suites; if null, we were not able to determine if the server has a preference
    """

    chaCha20Preference: bool | None
    """
    True if the server takes into account client preferences when deciding if to use ChaCha20 suites. null, we were not able
    to determine if the server has a chacha preference.
    """
