"""Retrieve detailed endpoint information."""
from typing import Any

from dacite import from_dict

from ssllabs.data.endpoint import EndpointData

from ._api import _Api


class Endpoint(_Api):
    """
    Retrieve detailed endpoint information.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-detailed-endpoint-information
    """

    async def get(self, host: str, s: str, **kwargs: Any) -> EndpointData:
        """
        Retrieve detailed endpoint information.

        :param host: Hostname to analyze
        :type host: str
        :param s: Endpoint IP address
        :type s: str
        :keyword fromCache: Always deliver cached assessment reports if available; optional, defaults to "off". This parameter
                            is intended for API consumers that don't want to wait for assessment results. Can't be used at the
                            same time as the startNew parameter.
        :type fromCache: str
        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occurred.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        self._verify_kwargs(kwargs.keys(), ["fromCache"])
        r = await self._call("getEndpointData", host=host, s=s, **kwargs)
        return from_dict(data_class=EndpointData, data=r.json())
