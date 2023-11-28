"""Trust Path."""
from __future__ import annotations

from dataclasses import dataclass

from .trust import TrustData


@dataclass
class TrustPathData:
    """
    Dataclass for trust path objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#trustpath
    """

    certIds: list[str]
    """List of certificate ID from leaf to root."""

    trust: list[TrustData]
    """Trust object. This object shows info about the trusted certificate by using Mozilla trust store."""

    isPinned: bool | None
    """True if a key is pinned, else false"""

    matchedPins: int | None
    """Number of matched pins with HPKP policy"""

    unmatchedPins: int | None
    """Number of unmatched pins with HPKP policy"""
