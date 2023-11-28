"""Trust."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrustData:
    """
    Dataclass for trust objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#trust
    """

    rootStore: str
    """this field shows the Trust store being used (eg. 'Mozilla')"""

    isTrusted: bool | None
    """True if trusted against above rootStore"""

    trustErrorMessage: str | None
    """Shows the error message if any"""
