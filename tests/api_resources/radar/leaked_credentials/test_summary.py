# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.leaked_credentials import (
    SummaryBotClassResponse,
    SummaryCompromisedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bot_class(self, client: Cloudflare) -> None:
        summary = client.radar.leaked_credentials.summary.bot_class()
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    def test_method_bot_class_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.leaked_credentials.summary.bot_class(
            compromised=["CLEAN"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_bot_class(self, client: Cloudflare) -> None:
        response = client.radar.leaked_credentials.summary.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_bot_class(self, client: Cloudflare) -> None:
        with client.radar.leaked_credentials.summary.with_streaming_response.bot_class() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_compromised(self, client: Cloudflare) -> None:
        summary = client.radar.leaked_credentials.summary.compromised()
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    def test_method_compromised_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.leaked_credentials.summary.compromised(
            bot_class=["LIKELY_AUTOMATED"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_compromised(self, client: Cloudflare) -> None:
        response = client.radar.leaked_credentials.summary.with_raw_response.compromised()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_compromised(self, client: Cloudflare) -> None:
        with client.radar.leaked_credentials.summary.with_streaming_response.compromised() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_bot_class(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.leaked_credentials.summary.bot_class()
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    async def test_method_bot_class_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.leaked_credentials.summary.bot_class(
            compromised=["CLEAN"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_bot_class(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.leaked_credentials.summary.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_bot_class(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.leaked_credentials.summary.with_streaming_response.bot_class() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryBotClassResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_compromised(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.leaked_credentials.summary.compromised()
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    async def test_method_compromised_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.leaked_credentials.summary.compromised(
            bot_class=["LIKELY_AUTOMATED"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_compromised(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.leaked_credentials.summary.with_raw_response.compromised()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_compromised(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.leaked_credentials.summary.with_streaming_response.compromised() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryCompromisedResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
