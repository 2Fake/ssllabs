from __future__ import annotations

import logging
from typing import Any, KeysView

from httpx import AsyncClient, Response

API_VERSION = 3
SSLLABS_URL = f"https://api.ssllabs.com/api/v{API_VERSION}/"


class _Api:
    """Base class to communicate with Qualys SSL Labs Assessment APIs."""

    def __init__(self, client: AsyncClient | None = None) -> None:
        self._logger = logging.getLogger(f"{self.__class__.__module__}.{self.__class__.__name__}")
        self._client = client

    async def _call(self, api_endpoint: str, **kwargs: Any) -> Response:
        """Invocate API."""
        if self._client:
            r = await self._client.get(f"{SSLLABS_URL}{api_endpoint}", params=kwargs)
        else:
            async with AsyncClient() as client:
                r = await client.get(f"{SSLLABS_URL}{api_endpoint}", params=kwargs, timeout=30.0)
        r.raise_for_status()
        return r

    def _verify_kwargs(self, given: KeysView[str], known: list[str]) -> None:
        """Log warning, if an argument is unknown."""
        for arg in given:
            if arg not in known:
                self._logger.warning(
                    "Argument '%s' is not known by the SSL Labs API. It will be send, but the results might be unexpected.",
                    arg,
                )
