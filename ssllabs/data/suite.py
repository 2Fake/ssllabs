"""Suite."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SuiteData:
    """
    Dataclass for suite objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#suite
    """

    id: int
    """Suite RFC ID"""

    name: str
    """Suite name (e.g., TLS_RSA_WITH_RC4_128_SHA)"""

    cipherStrength: int
    """Suite strength (e.g., 128)"""

    kxType: str | None
    """Key exchange type (e.g., ECDH)"""

    kxStrength: int | None
    """Key exchange strength, in RSA-equivalent bits"""

    dhP: int | None
    """DH params, p component"""

    dhG: int | None
    """DH params, g component"""

    dhYs: int | None
    """DH params, Ys component"""

    namedGroupBits: int | None
    """EC bits"""

    namedGroupId: int | None
    """EC curve ID"""

    namedGroupName: str | None
    """EC curve name"""

    q: int | None
    """Flag for suite insecure or weak. Not present if suite is strong or good"""
