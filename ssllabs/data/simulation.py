"""Simulation."""
from __future__ import annotations

from dataclasses import dataclass

from .sim_client import SimClientData


@dataclass
class SimulationData:
    """
    Dataclass for Simulation objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simulation
    """

    client: SimClientData
    """Instance of SimClient."""

    errorCode: int
    """Zero if handshake was successful, 1 if it was not."""

    errorMessage: str | None
    """Error message if simulation has failed."""

    attempts: int
    """Always 1 with the current implementation."""

    certChainId: str | None
    """ID of the certificate chain."""

    protocolId: int | None
    """Negotiated protocol ID."""

    suiteId: int | None
    """Negotiated suite ID."""

    suiteName: str | None
    """Negotiated suite Name."""

    kxType: str | None
    """Negotiated key exchange, for example 'ECDH'."""

    kxStrength: int | None
    """Negotiated key exchange strength, in RSA-equivalent bits."""

    dhBits: int | None
    """Strength of DH params (e.g., 1024)"""

    dhP: int | None
    """DH params, p component"""

    dhG: int | None
    """DH params, g component"""

    dhYs: int | None
    """DH params, Ys component"""

    namedGroupBits: int | None
    """When ECDHE is negotiated, length of EC parameters."""

    namedGroupId: int | None
    """When ECDHE is negotiated, EC curve ID."""

    namedGroupName: str | None
    """When ECDHE is negotiated, EC curve nanme (e.g., 'secp256r1')."""

    keyAlg: str | None
    """Connection certificate key algorithsm (e.g., 'RSA')."""

    keySize: int | None
    """Connection certificate key size (e.g., 2048)."""

    sigAlg: str | None
    """Connection certificate signature algorithm (e.g, 'SHA256withRSA')."""
