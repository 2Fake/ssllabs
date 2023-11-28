"""HTTP Transaction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HttpTransactionData:
    """
    Dataclass for HTTP Transaction objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#httptransaction
    """

    requestUrl: str
    """Request URL"""

    statusCode: int | None
    """Response status code"""

    requestLine: str | None
    """The entire request line as a single field"""

    requestHeaders: list[str]
    """An array of request HTTP headers, each with name and value"""

    responseLine: str | None
    """The entire response line as a single field"""

    responseHeadersRaw: list[str]
    """All response headers as a single field (useful if the headers are malformed)"""

    responseHeaders: list[dict]
    """An array of response HTTP headers, each with name and value"""

    fragileServer: bool
    """True if the server crashes when inspected by SSL Labs (in which case the full test is refused)"""
