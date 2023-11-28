"""CAA Policy."""
from __future__ import annotations

from dataclasses import dataclass

from .caa_record import CaaRecordData


@dataclass
class CaaPolicyData:
    """
    Dataclass for CAA Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#caapolicy
    """

    policyHostname: str
    """hostname where policy is located"""

    caaRecords: list[CaaRecordData]
    """List of supported CAARecord"""
