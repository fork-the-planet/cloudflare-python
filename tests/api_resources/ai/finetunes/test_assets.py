# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai.finetunes import AssetCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        asset = client.ai.finetunes.assets.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        asset = client.ai.finetunes.assets.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            file_name="file_name",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai.finetunes.assets.with_raw_response.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai.finetunes.assets.with_streaming_response.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.finetunes.assets.with_raw_response.create(
                finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finetune_id` but received ''"):
            client.ai.finetunes.assets.with_raw_response.create(
                finetune_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.ai.finetunes.assets.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.ai.finetunes.assets.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            file_name="file_name",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.finetunes.assets.with_raw_response.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.finetunes.assets.with_streaming_response.create(
            finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.finetunes.assets.with_raw_response.create(
                finetune_id="bc451aef-f723-4b26-a6b2-901afd2e7a8a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finetune_id` but received ''"):
            await async_client.ai.finetunes.assets.with_raw_response.create(
                finetune_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
