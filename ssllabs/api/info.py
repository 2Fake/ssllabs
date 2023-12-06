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

        :raises SsllabsUnavailableError: The SSL Labs service is not available.
        :raises SsllabsOverloadedError: The SSL Labs service is overloaded. You should reduce your usage or wait a bit.
        :raises HTTPStatusError: Something unexpected happened. Please file us a bug.
        :raises MissingValueError: Something unexpected happened. Please file us a bug.
        """
        r = await self._call("info")
        return from_dict(data_class=InfoData, data=r.json())
