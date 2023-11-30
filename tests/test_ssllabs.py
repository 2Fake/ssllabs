import asyncio
import dataclasses
from unittest.mock import AsyncMock, patch

import pytest
from dacite import from_dict
from httpx import ConnectTimeout, HTTPStatusError, ReadError, ReadTimeout, TransportError

from ssllabs import Ssllabs
from ssllabs.api.analyze import Analyze
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData
from ssllabs.data.status_codes import StatusCodesData

from . import load_fixture


class TestSsllabs:
    API_CALLS: list = [("info.Info", InfoData, {}), ("status_codes.StatusCodes", StatusCodesData, {})]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("api, result, parameters", API_CALLS)
    async def test_ssllabs(self, api, result, parameters):
        call = api.split(".")[0]
        with patch(
            f"ssllabs.api.{api}.get", new=AsyncMock(return_value=from_dict(data_class=result, data=load_fixture(call)))
        ):
            ssllabs = Ssllabs()
            api_data = await getattr(ssllabs, call)(**parameters)
            assert dataclasses.asdict(api_data) == load_fixture(call)

    @pytest.mark.asyncio
    async def test_analyze(self) -> None:
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_value=from_dict(data_class=InfoData, data=load_fixture("info")))
        ), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=load_fixture("analyze"))),
        ) as get:
            ssllabs = Ssllabs()
            api_data = await ssllabs.analyze(host="devolo.de")
            assert dataclasses.asdict(api_data) == load_fixture("analyze")
            get.assert_called_with(
                host="devolo.de", ignoreMismatch="off", publish="off", startNew="on", fromCache="off", maxAge=None
            )
            api_data = await ssllabs.analyze(host="devolo.de", from_cache=True, max_age=1)
            assert dataclasses.asdict(api_data) == load_fixture("analyze")
            get.assert_called_with(
                host="devolo.de", ignoreMismatch="off", publish="off", startNew="off", fromCache="on", maxAge=1
            )

    @pytest.mark.asyncio
    async def test_analyze_not_ready_yet(self, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_value=from_dict(data_class=InfoData, data=load_fixture("info")))
        ), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(
                side_effect=[
                    from_dict(data_class=HostData, data=load_fixture("analyze_running")),
                    from_dict(data_class=HostData, data=load_fixture("analyze")),
                ]
            ),
        ):
            spy = mocker.spy(Analyze, "get")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 2

    @pytest.mark.asyncio
    async def test_analyze_max_assessments(self, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=load_fixture("analyze"))),
        ), patch(
            "ssllabs.api.info.Info.get",
            new=AsyncMock(
                side_effect=[
                    from_dict(data_class=InfoData, data=load_fixture("info_max_assessments")),
                    from_dict(data_class=InfoData, data=load_fixture("info")),
                ]
            ),
        ):
            spy = mocker.spy(asyncio, "sleep")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 1

    @pytest.mark.asyncio
    async def test_analyze_running_assessments(self, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=load_fixture("analyze"))),
        ), patch(
            "ssllabs.api.info.Info.get",
            new=AsyncMock(return_value=from_dict(data_class=InfoData, data=load_fixture("info_running_assessments"))),
        ):
            spy = mocker.spy(asyncio, "sleep")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 1

    @pytest.mark.asyncio
    async def test_root_certs(self):
        with patch(
            "ssllabs.api.root_certs_raw.RootCertsRaw.get", new=AsyncMock(return_value=load_fixture("root_certs")["rootCerts"])
        ):
            ssllabs = Ssllabs()
            root_certs = await ssllabs.root_certs()
            assert root_certs == load_fixture("root_certs")["rootCerts"]

    @pytest.mark.asyncio
    async def test_availabile(self):
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_Value=from_dict(data_class=InfoData, data=load_fixture("info")))
        ):
            ssllabs = Ssllabs()
            assert await ssllabs.availability()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("exception", [ReadError, ReadTimeout, ConnectTimeout])
    async def test_unavailabile_timeout(self, exception: TransportError) -> None:
        with patch("ssllabs.api.info.Info.get", new=AsyncMock(side_effect=exception(message="", request=""))):
            ssllabs = Ssllabs()
            assert not await ssllabs.availability()

    @pytest.mark.asyncio
    async def test_unavailabile_status_error(self):
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(side_effect=HTTPStatusError(message="", request="", response=""))
        ):
            ssllabs = Ssllabs()
            assert not await ssllabs.availability()
