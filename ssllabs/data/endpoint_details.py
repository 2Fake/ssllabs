"""Endpoint Details."""
from __future__ import annotations

from dataclasses import dataclass

from .certificate_chain import CertificateChainData
from .drown_hosts import DrownHostsData
from .hpkp_policy import HpkpPolicyData
from .hsts_policy import HstsPolicyData
from .hsts_preload import HstsPreloadData
from .http_transaction import HttpTransactionData
from .named_groups import NamedGroupsData
from .protocol import ProtocolData
from .protocol_suites import ProtocolSuitesData
from .sim_details import SimDetailsData
from .static_pkp_policy import StaticPkpPolicyData


@dataclass
class EndpointDetailsData:
    """
    Dataclass for endpoint detail objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#endpointdetails
    """

    hostStartTime: int
    """
    Endpoint assessment starting time, in milliseconds since 1970. This field is useful when test results are retrieved in
    several HTTP invocations. Then, you should check that the hostStartTime value matches the startTime value of the host.
    """

    certChains: list[CertificateChainData]
    """Server Certificate chains"""

    protocols: list[ProtocolData]
    """Supported protocols"""

    suites: list[ProtocolSuitesData] | None
    """Supported cipher suites per protocol"""

    noSniSuites: ProtocolSuitesData | None
    """Cipher suites observed only with client that does not support Server Name Indication (SNI)."""

    namedGroups: NamedGroupsData | None
    """Instance of NamedGroups object."""

    serverSignature: str | None
    """
    Contents of the HTTP Server response header when known. This field could be absent for one of two reasons: 1) the HTTP
    request failed (check httpStatusCode) or 2) there was no Server response header returned.
    """

    prefixDelegation: bool
    """True if this endpoint is reachable via a hostname with the www prefix"""

    nonPrefixDelegation: bool
    """True if this endpoint is reachable via a hostname without the www prefix"""

    vulnBeast: bool | None
    """True if the endpoint is vulnerable to the BEAST attack"""

    renegSupport: int | None
    """This is an integer value that describes the endpoint support for renegotiation."""

    sessionResumption: int | None
    """This is an integer value that describes endpoint support for session resumption."""

    compressionMethods: int | None
    """Integer value that describes supported compression methods"""

    supportsNpn: bool | None
    """True if the server supports NPN"""

    npnProtocols: str | None
    """Space separated list of supported NPN protocols"""

    supportsAlpn: bool | None
    """True if the server supports ALPN"""

    alpnProtocols: str | None
    """Space separated list of supported ALPN protocols"""

    sessionTickets: int | None
    """Indicates support for Session Tickets"""

    ocspStapling: bool | None
    """True if OCSP stapling is deployed on the server"""

    staplingRevocationStatus: int | None
    """Same as Cert.revocationStatus, but for the stapled OCSP response."""

    staplingRevocationErrorMessage: str | None
    """Description of the problem with the stapled OCSP response, if any."""

    sniRequired: bool | None
    """If SNI support is required to access the web site."""

    httpStatusCode: int | None
    """
    Status code of the final HTTP response seen. When submitting HTTP requests, redirections are followed, but only if they
    lead to the same hostname. If this field is not available, that means the HTTP request failed.
    """

    httpForwarding: str | None
    """Available on a server that responded with a redirection to some other hostname."""

    supportsRc4: bool | None
    """True if the server supports at least one RC4 suite."""

    rc4WithModern: bool | None
    """True if RC4 is used with modern clients."""

    rc4Only: bool | None
    """True if only RC4 suites are supported."""

    forwardSecrecy: int | None
    """Indicates support for Forward Secrecy"""

    supportsAead: bool | None
    """True if the server supports at least one AEAD suite."""

    supportsCBC: bool | None
    """True if the server supports at least one CBC suite."""

    protocolIntolerance: int | None
    """Indicates protocol version intolerance issues"""

    miscIntolerance: int | None
    """Indicates various other types of intolerance"""

    sims: SimDetailsData | None
    """Instance of SimDetails."""

    heartbleed: bool | None
    """True if the server is vulnerable to the Heartbleed attack."""

    heartbeat: bool | None
    """True if the server supports the Heartbeat extension."""

    openSslCcs: int | None
    """Results of the CVE-2014-0224 test"""

    openSSLLuckyMinus20: int | None
    """Results of the CVE-2016-2107 test"""

    ticketbleed: int | None
    """Results of the ticketbleed CVE-2016-9244 test"""

    bleichenbacher: int | None
    """Results of the Return Of Bleichenbacher's Oracle Threat (ROBOT) test"""

    zombiePoodle: int | None
    """Results of the Zombie POODLE test"""

    goldenDoodle: int | None
    """Results of the GOLDENDOODLE test"""

    zeroLengthPaddingOracle: int | None
    """Results of the 0-Length Padding Oracle (CVE-2019-1559) test"""

    sleepingPoodle: int | None
    """Results of the Sleeping POODLE test"""

    poodle: bool | None
    """True if the endpoint is vulnerable to POODLE"""

    poodleTls: int | None
    """Results of the POODLE TLS test"""

    fallbackScsv: bool | None
    """
    True if the server supports TLS_FALLBACK_SCSV, false if it doesn't. This field will not be available if the server's
    support for TLS_FALLBACK_SCSV can't be tested because it supports only one protocol version (e.g., only TLS 1.2).
    """

    freak: bool | None
    """True if the server is vulnerable to the FREAK attack, meaning it supports 512-bit key exchange."""

    hasSct: int | None
    """Information about the availability of certificate transparency information (embedded SCTs)"""

    dhPrimes: list[str] | None
    """List of hex-encoded DH primes used by the server. Not present if the server doesn't support the DH key exchange."""

    dhUsesKnownPrimes: int | None
    """Whether the server uses known DH primes. Not present if the server doesn't support the DH key exchange."""

    dhYsReuse: bool | None
    """True if the DH ephemeral server value is reused. Not present if the server doesn't support the DH key exchange."""

    ecdhParameterReuse: bool | None
    """True if the server reuses its ECDHE values"""

    logjam: bool | None
    """True if the server uses DH parameters weaker than 1024 bits."""

    chaCha20Preference: bool | None
    """
    True if the server takes into account client preferences when deciding if to use ChaCha20 suites. Will be deprecated in
    new version.
    """

    hstsPolicy: HstsPolicyData | None
    """Server's HSTS policy. Experimental."""

    hstsPreloads: list[HstsPreloadData] | None
    """Information about preloaded HSTS policies."""

    hpkpPolicy: HpkpPolicyData | None
    """Server's HPKP policy."""

    hpkpRoPolicy: HpkpPolicyData | None
    """Server's HPKP-RO policy."""

    staticPkpPolicy: StaticPkpPolicyData | None
    """Server's SPKP policy."""

    httpTransactions: list[HttpTransactionData] | None
    """An array of HttpTransaction objects."""

    drownHosts: list[DrownHostsData] | None
    """List of DROWN hosts."""

    drownErrors: bool | None
    """True if error occurred in the DROWN test."""

    drownVulnerable: bool | None
    """True if server vulnerable to the DROWN attack."""

    implementsTLS13MandatoryCS: bool | None
    """True if server supports mandatory TLS 1.3 cipher suite (TLS_AES_128_GCM_SHA256), null if TLS 1.3 not supported."""

    zeroRTTEnabled: int | None
    """Results of the 0-RTT test. This test will only be performed if TLS 1.3 is enabled."""
