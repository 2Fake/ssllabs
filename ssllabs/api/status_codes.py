"""Retrieve known status codes."""
from dacite import from_dict

from ssllabs.data.status_codes import StatusCodesData

from ._api import _Api


class StatusCodes(_Api):
    """
    Retrieve known status codes.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
    """

    async def get(self) -> StatusCodesData:
        """
        Retrieve known status codes.

        :raises SsllabsUnavailableError: The SSL Labs service is not available.
        :raises SsllabsOverloadedError: The SSL Labs service is overloaded. You should reduce your usage or wait a bit.
        :raises HTTPStatusError: Something unexpected happened. Please file us a bug.
        :raises MissingValueError: Something unexpected happened. Please file us a bug.
        """
        r = await self._call("getStatusCodes")
        return from_dict(data_class=StatusCodesData, data=r.json())
