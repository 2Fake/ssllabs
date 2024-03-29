"""High level implementation of the SSL Labs API."""

from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

from .api import Analyze, Info, RootCertsRaw, StatusCodes
from .exceptions import SsllabsUnavailableError
from .trust_store import TrustStore

if TYPE_CHECKING:
    from httpx import AsyncClient

    from .data.host import HostData
    from .data.info import InfoData
    from .data.status_codes import StatusCodesData


LOGGER = logging.getLogger(__name__)


class Ssllabs:
    """High level methods to interact with the SSL Labs Assessment APIs."""

    def __init__(self, client: AsyncClient | None = None) -> None:
        """Initialize SSL Labs."""
        self._client = client
        self._semaphore = asyncio.Semaphore(1)
        LOGGER.info(
            "You will be sending assessment requests to remote SSL Labs servers and information will be shared with them.",
        )
        LOGGER.info("Please subject to the terms and conditions: https://www.ssllabs.com/about/terms.html")

    async def availability(self) -> bool:
        """
        Check the availability of the SSL Labs servers.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#error-response-status-codes
        """
        i = Info(self._client)
        try:
            await i.get()
        except SsllabsUnavailableError as ex:
            LOGGER.error(ex)  # noqa: TRY400
            return False
        else:
            LOGGER.info("SSL Labs servers are up and running.")
            return True

    async def analyze(  # noqa: PLR0913
        self,
        host: str,
        *,
        publish: bool = False,
        ignore_mismatch: bool = False,
        from_cache: bool = False,
        max_age: int | None = None,
    ) -> HostData:
        """
        Test a particular host with respect to the cool off and the maximum number of assessments.

        :param host: Host to test
        :param publish: True if assessment results should be published on the public results boards
        :param ignore_mismatch: True if assessment shall proceed even when the server certificate doesn't match the hostname
        :param from_cache: True if cached results should be used instead of new assessments
        :param max_age: Maximum age cached data might have in hours

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage
        """
        await self._semaphore.acquire()
        LOGGER.info("Analyzing %s", host)
        i = Info(self._client)
        info = await i.get()
        for message in info.messages:
            LOGGER.info("%s", message)

        # Wait for a free slot, if all slots are in use
        while info.currentAssessments >= info.maxAssessments:
            LOGGER.warning("Already %i assessments running. Need to wait.", info.currentAssessments)
            await asyncio.sleep(1)
            info = await i.get()

        # If there is already an assessment running, wait the needed cool off until starting the next one
        if info.currentAssessments != 0:
            await asyncio.sleep(info.newAssessmentCoolOff / 1000)

        a = Analyze(self._client)
        host_object = await a.get(
            host=host,
            startNew="off" if from_cache else "on",
            fromCache="on" if from_cache else "off",
            publish="on" if publish else "off",
            ignoreMismatch="on" if ignore_mismatch else "off",
            maxAge=max_age,
        )
        self._semaphore.release()
        while host_object.status not in ["READY", "ERROR"]:
            LOGGER.debug("Assessment of %s not ready yet.", host)
            await asyncio.sleep(10)
            host_object = await a.get(host=host, all="done")
        return host_object

    async def info(self) -> InfoData:
        """
        Retrieve the engine and criteria version, and initialize the maximum number of concurrent assessments.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
        """
        i = Info(self._client)
        return await i.get()

    async def root_certs(self, trust_store: TrustStore = TrustStore.MOZILLA) -> str:
        """
        Retrieve root certificates.

        :param trust_store: Trust store to return (Mozilla, MacOS, Android, Java or Windows)

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
        """
        rcr = RootCertsRaw(self._client)
        return await rcr.get(trustStore=trust_store)

    async def status_codes(self) -> StatusCodesData:
        """
        Retrieve known status codes.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
        """
        sc = StatusCodes(self._client)
        return await sc.get()
