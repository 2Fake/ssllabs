"""Simulation Objects."""
from __future__ import annotations

from dataclasses import dataclass

from .simulation import SimulationData


@dataclass
class SimDetailsData:
    """
    Dataclass for Simulation object lists.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simdetails
    """

    results: list[SimulationData]
    """Instances of Simulation."""
