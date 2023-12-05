"""Test high level API."""
from __future__ import annotations

import dataclasses
from http import HTTPStatus
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
from dacite import from_dict
from httpx import AsyncClient, ConnectTimeout, ReadError, ReadTimeout, TransportError

from ssllabs import Ssllabs
from ssllabs.api import Endpoint
from ssllabs.api._api import SSLLABS_URL
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData

from . import load_fixture

if TYPE_CHECKING:
    from pytest_httpx import HTTPXMock


@pytest.mark.asyncio()
async def test_availabile(httpx_mock: HTTPXMock) -> None:
    """Test API being available."""
    httpx_mock.add_response(json=load_fixture("info"))
    ssllabs = Ssllabs()
    assert await ssllabs.availability()


@pytest.mark.asyncio()
@pytest.mark.parametrize("exception", [ReadError, ReadTimeout, ConnectTimeout])
async def test_unavailable(exception: type[TransportError], httpx_mock: HTTPXMock) -> None:
    """Test API being unavailable."""
    httpx_mock.add_exception(exception(message="test"))
    ssllabs = Ssllabs()
    assert not await ssllabs.availability()


@pytest.mark.asyncio()
async def test_unavailable_status_error(httpx_mock: HTTPXMock) -> None:
    """Test API responding with an error."""
    httpx_mock.add_response(status_code=HTTPStatus.SERVICE_UNAVAILABLE)
    ssllabs = Ssllabs()
    assert not await ssllabs.availability()


@pytest.mark.asyncio()
async def test_analyze(httpx_mock: HTTPXMock) -> None:
    """Test analyzing a host."""
    httpx_mock.add_response(json=load_fixture("info"), url=f"{SSLLABS_URL}info")
    host = "ssllabs.com"
    publish = "off"

    start_new = "on"
    from_cache = "off"
    httpx_mock.add_response(
        json=load_fixture("analyze"),
        url=f"{SSLLABS_URL}analyze?host={host}&startNew={start_new}&fromCache={from_cache}&publish={publish}&ignoreMismatch=off&maxAge=",
    )
    ssllabs = Ssllabs()
    analyze = await ssllabs.analyze(host=host)
    assert dataclasses.asdict(analyze) == load_fixture("analyze")

    start_new = "off"
    from_cache = "on"
    max_age = 1
    httpx_mock.add_response(
        json=load_fixture("analyze"),
        url=f"{SSLLABS_URL}analyze?host={host}&startNew={start_new}&fromCache={from_cache}&publish={publish}&ignoreMismatch=off&maxAge={max_age}",
    )
    analyze = await ssllabs.analyze(host=host, from_cache=True, max_age=max_age)
    assert dataclasses.asdict(analyze) == load_fixture("analyze")


@pytest.mark.asyncio()
async def test_analyze_not_ready_yet(httpx_mock: HTTPXMock) -> None:
    """Test analysis is ongoing."""
    host = "ssllabs.com"
    publish = "off"
    start_new = "on"
    from_cache = "off"
    max_age = ""

    httpx_mock.add_response(json=load_fixture("info"), url=f"{SSLLABS_URL}info")
    httpx_mock.add_response(
        json=load_fixture("analyze_running"),
        url=f"{SSLLABS_URL}analyze?host={host}&startNew={start_new}&fromCache={from_cache}&publish={publish}&ignoreMismatch=off&maxAge={max_age}",
    )
    httpx_mock.add_response(json=load_fixture("analyze"), url=f"{SSLLABS_URL}analyze?host={host}&all=done")

    with patch("asyncio.sleep"):
        ssllabs = Ssllabs()
        await ssllabs.analyze(host=host)


@pytest.mark.asyncio()
async def test_analyze_max_assessments() -> None:
    """Test maximum assessments reached."""
    with patch("asyncio.sleep") as sleep, patch(
        "ssllabs.api.analyze.Analyze.get",
        return_value=from_dict(data_class=HostData, data=load_fixture("analyze")),
    ), patch(
        "ssllabs.api.info.Info.get",
        side_effect=[
            from_dict(data_class=InfoData, data=load_fixture("info_max_assessments")),
            from_dict(data_class=InfoData, data=load_fixture("info")),
        ],
    ):
        ssllabs = Ssllabs()
        await ssllabs.analyze(host="ssllabs.com")
        sleep.assert_awaited_once()


@pytest.mark.asyncio()
async def test_analyze_running_assessments() -> None:
    """Test cool down if assessment is running."""
    with patch("asyncio.sleep") as sleep, patch(
        "ssllabs.api.analyze.Analyze.get",
        return_value=from_dict(data_class=HostData, data=load_fixture("analyze")),
    ), patch(
        "ssllabs.api.info.Info.get",
        return_value=from_dict(data_class=InfoData, data=load_fixture("info_running_assessments")),
    ):
        ssllabs = Ssllabs()
        await ssllabs.analyze(host="ssllabs.com")
        sleep.assert_awaited_once()


@pytest.mark.asyncio()
async def test_info(httpx_mock: HTTPXMock) -> None:
    """Test getting information from SSL Labs."""
    httpx_mock.add_response(json=load_fixture("info"))
    ssllabs = Ssllabs()
    info = await ssllabs.info()
    assert dataclasses.asdict(info) == load_fixture("info")


@pytest.mark.asyncio()
async def test_info_with_client(httpx_mock: HTTPXMock) -> None:
    """Test getting information from SSL Labs using an own client."""
    httpx_mock.add_response(json=load_fixture("info"))
    async with AsyncClient() as client:
        ssllabs = Ssllabs(client=client)
        info = await ssllabs.info()
    assert dataclasses.asdict(info) == load_fixture("info")


@pytest.mark.asyncio()
async def test_root_certs(httpx_mock: HTTPXMock) -> None:
    """Test getting root certificates."""
    httpx_mock.add_response(text=load_fixture("root_certs")["rootCerts"])
    ssllabs = Ssllabs()
    root_certs = await ssllabs.root_certs()
    assert root_certs == load_fixture("root_certs")["rootCerts"]


@pytest.mark.asyncio()
async def test_status_codes(httpx_mock: HTTPXMock) -> None:
    """Test getting status codes."""
    httpx_mock.add_response(json=load_fixture("status_codes"))
    ssllabs = Ssllabs()
    status_codes = await ssllabs.status_codes()
    assert dataclasses.asdict(status_codes) == load_fixture("status_codes")


@pytest.mark.asyncio()
async def test_endpoint(httpx_mock: HTTPXMock) -> None:
    """Test endpoint details."""
    httpx_mock.add_response(json=load_fixture("endpoint"))
    endpoint = Endpoint()
    endpoint_data = await endpoint.get("ssllabs.com", "164.41.200.100")
    assert dataclasses.asdict(endpoint_data) == load_fixture("endpoint")
