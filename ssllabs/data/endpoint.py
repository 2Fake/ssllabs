"""Endpoint."""
from __future__ import annotations

from dataclasses import dataclass

from .endpoint_details import EndpointDetailsData


@dataclass
class EndpointData:
    """
    Dataclass for endpoint objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#endpoint
    """

    ipAddress: str
    """Endpoint IP address, in IPv4 or IPv6 format."""

    serverName: str | None
    """Server name retrieved via reverse DNS"""

    statusMessage: str
    """Assessment status message; this field will contain 'Ready' if the endpoint assessment was successful."""

    statusDetails: str | None
    """Code of the operation currently in progress"""

    statusDetailsMessage: str | None
    """Description of the operation currently in progress"""

    grade: str | None
    """Possible values: A+, A-, A-F, T (no trust) and M (certificate name mismatch)"""

    gradeTrustIgnored: str | None
    """Grade (as above), if trust issues are ignored"""

    futureGrade: str | None
    """Next grade because of upcoming grading criteria changes, Null if there is no impact on current grade."""

    hasWarnings: bool | None
    """If this endpoint has warnings that might affect the score (e.g., get A- instead of A)."""

    isExceptional: bool | None
    """
    This flag will be raised when an exceptional configuration is encountered. The SSL Labs test will give such sites an A+.
    """

    progress: int | None
    """Assessment progress, which is a value from 0 to 100, and -1 if the assessment has not yet started"""

    duration: int | None
    """Assessment duration, in milliseconds"""

    eta: int | None
    """Estimated time, in seconds, until the completion of the assessment"""

    delegation: int
    """Indicates domain name delegation with and without the www prefix"""

    details: EndpointDetailsData | None
    """
    This field contains an EndpointDetails object. It's not present by default, but can be enabled by using the "all"
    parameter to the analyze API call.
    """
