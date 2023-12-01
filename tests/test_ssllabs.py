"""Test high level API."""
import dataclasses
from unittest.mock import patch

import pytest
from dacite import from_dict
from httpx import ConnectTimeout, HTTPStatusError, ReadError, ReadTimeout, TransportError

from ssllabs import Ssllabs
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData
from ssllabs.data.status_codes import StatusCodesData

from . import load_fixture


@pytest.mark.asyncio()
async def test_availabile() -> None:
    """Test API being available."""
    with patch("ssllabs.api.info.Info.get", return_Value=from_dict(data_class=InfoData, data=load_fixture("info"))):
        ssllabs = Ssllabs()
        assert await ssllabs.availability()


@pytest.mark.asyncio()
@pytest.mark.parametrize("exception", [ReadError, ReadTimeout, ConnectTimeout])
async def test_unavailable(exception: TransportError) -> None:
    """Test API being unavailable."""
    with patch("ssllabs.api.info.Info.get", side_effect=exception(message="", request="")):
        ssllabs = Ssllabs()
        assert not await ssllabs.availability()


@pytest.mark.asyncio()
async def test_unavailable_status_error() -> None:
    """Test API responding with an error."""
    with patch("ssllabs.api.info.Info.get", side_effect=HTTPStatusError(message="", request="", response="")):
        ssllabs = Ssllabs()
        assert not await ssllabs.availability()


@pytest.mark.asyncio()
async def test_analyze() -> None:
    """Test analyzing a host."""
    with patch("ssllabs.api.info.Info.get", return_value=from_dict(data_class=InfoData, data=load_fixture("info"))), patch(
        "ssllabs.api.analyze.Analyze.get",
        return_value=from_dict(data_class=HostData, data=load_fixture("analyze")),
    ) as get:
        ssllabs = Ssllabs()
        analyze = await ssllabs.analyze(host="ssllabs.com")
        assert dataclasses.asdict(analyze) == load_fixture("analyze")
        get.assert_called_with(
            host="ssllabs.com",
            ignoreMismatch="off",
            publish="off",
            startNew="on",
            fromCache="off",
            maxAge=None,
        )
        analyze = await ssllabs.analyze(host="ssllabs.com", from_cache=True, max_age=1)
        assert dataclasses.asdict(analyze) == load_fixture("analyze")
        get.assert_called_with(
            host="ssllabs.com",
            ignoreMismatch="off",
            publish="off",
            startNew="off",
            fromCache="on",
            maxAge=1,
        )


@pytest.mark.asyncio()
async def test_analyze_not_ready_yet() -> None:
    """Test analysis is ongoing."""
    with patch("asyncio.sleep"), patch(
        "ssllabs.api.info.Info.get",
        return_value=from_dict(data_class=InfoData, data=load_fixture("info")),
    ), patch(
        "ssllabs.api.analyze.Analyze.get",
        side_effect=[
            from_dict(data_class=HostData, data=load_fixture("analyze_running")),
            from_dict(data_class=HostData, data=load_fixture("analyze")),
        ],
    ) as get:
        ssllabs = Ssllabs()
        await ssllabs.analyze(host="ssllabs.com")
        assert get.call_count == 2


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
async def test_info() -> None:
    """Test getting information from SSL Labs."""
    with patch("ssllabs.api.Info.get", return_value=from_dict(data_class=InfoData, data=load_fixture("info"))):
        ssllabs = Ssllabs()
        info = await ssllabs.info()
        assert dataclasses.asdict(info) == load_fixture("info")


@pytest.mark.asyncio()
async def test_root_certs() -> None:
    """Test getting root certificates."""
    with patch("ssllabs.api.RootCertsRaw.get", return_value=load_fixture("root_certs")["rootCerts"]):
        ssllabs = Ssllabs()
        root_certs = await ssllabs.root_certs()
        assert root_certs == load_fixture("root_certs")["rootCerts"]


@pytest.mark.asyncio()
async def test_status_codes() -> None:
    """Test gettint status codes."""
    with patch(
        "ssllabs.api.StatusCodes.get",
        return_value=from_dict(data_class=StatusCodesData, data=load_fixture("status_codes")),
    ):
        ssllabs = Ssllabs()
        status_codes = await ssllabs.status_codes()
        assert dataclasses.asdict(status_codes) == load_fixture("status_codes")
