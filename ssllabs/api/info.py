"""General information about the SSL Labs API."""
from dacite import from_dict

from ssllabs.data.info import InfoData

from ._api import _Api


class Info(_Api):
    """
    General information about the SSL Labs API.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#check-ssl-labs-availability
    """

    async def get(self) -> InfoData:
        """
        Get information.

        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        r = await self._call("info")
        return from_dict(data_class=InfoData, data=r.json())
