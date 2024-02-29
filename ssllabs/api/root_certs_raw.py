"""Retrieve root certificates."""

from typing import Any

from ._api import _Api


class RootCertsRaw(_Api):
    """
    Retrieve root certificates.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
    """

    async def get(self, **kwargs: Any) -> str:
        """
        Retrieve root certificates.

        :keyword trustStore: 1-Mozilla(default), 2-Apple MacOS, 3-Android, 4-Java, 5-Windows
        :type trustStore: TrustStore
        :raises SsllabsUnavailableError: The SSL Labs service is not available.
        :raises SsllabsOverloadedError: The SSL Labs service is overloaded. You should reduce your usage or wait a bit.
        :raises HTTPStatusError: Something unexpected happened. Please file us a bug.
        :raises MissingValueError: Something unexpected happened. Please file us a bug.
        """
        self._verify_kwargs(kwargs.keys(), ["trustStore"])
        r = await self._call("getRootCertsRaw", **kwargs)
        return r.text
