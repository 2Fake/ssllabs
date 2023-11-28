"""Cert."""
from __future__ import annotations

from dataclasses import dataclass

from .caa_policy import CaaPolicyData


@dataclass
class CertData:
    """
    Dataclass for Cert objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#cert
    """

    id: str
    """Certificate ID"""

    subject: str
    """Certificate subject"""

    serialNumber: str
    """Certificate serial number (hex-encoded)"""

    commonNames: list[str]
    """Common names extracted from the subject"""

    altNames: list[str] | None
    """Alternative names"""

    notBefore: int
    """Timestamp before which the certificate is not valid (Unix Timestamp)"""

    notAfter: int
    """Timestamp after which the certificate is not valid (Unix Timestamp)"""

    issuerSubject: str
    """Issuer subject"""

    sigAlg: str
    """Certificate signature algorithm"""

    revocationInfo: int
    """A number that represents revocation information present in the certificate"""

    crlURIs: list[str] | None
    """CRL URIs extracted from the certificate"""

    ocspURIs: list[str] | None
    """OCSP URIs extracted from the certificate"""

    revocationStatus: int
    """A number that describes the revocation status of the certificate"""

    crlRevocationStatus: int
    """Same as revocationStatus, but only for the CRL information (if any)."""

    ocspRevocationStatus: int
    """Same as revocationStatus, but only for the OCSP information (if any)."""

    dnsCaa: bool | None
    """True if CAA is supported else false."""

    caaPolicy: CaaPolicyData | None
    """CAA Policy, Null if CAA is not supported"""

    mustStaple: bool
    """True if stapling is supported else false"""

    sgc: int
    """Server Gated Cryptography support"""

    validationType: str | None
    """E for Extended Validation certificates"""

    issues: int | None
    """list of certificate issues, one bit per issue"""

    sct: bool
    """True if the certificate contains an embedded SCT; false otherwise."""

    sha1Hash: str
    """sha1 hash of the certificate"""

    sha256Hash: str
    """sha256 hash of the certificate"""

    pinSha256: str
    """sha256 hash of the public key"""

    keyAlg: str
    """Key algorithm."""

    keySize: int
    """Key size, in bits appropriate for the key algorithm."""

    keyStrength: int
    """Key strength, in equivalent RSA bits"""

    keyKnownDebianInsecure: bool | None
    """True if debian flaw is found, else false"""

    raw: str
    """PEM-encoded certificate"""
