"""HSTS Preload."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HstsPreloadData:
    """
    Dataclass for HSTS Preload objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hstspreload
    """

    source: str
    """Source name"""

    hostname: str
    """Name of the host"""

    status: str
    """preload status"""

    error: str | None
    """Error message, when status is 'error'"""

    sourceTime: int | None
    """Time, as a Unix timestamp, when the preload database was retrieved"""
