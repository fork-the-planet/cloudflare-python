# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rules import (
    ListGetResponse,
    ListListResponse,
    ListCreateResponse,
    ListDeleteResponse,
    ListUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
            description="This is a note",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.create(
                account_id="",
                kind="ip",
                name="list1",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is a note",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.update(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.update(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListListResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.delete(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.delete(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        list_ = client.rules.lists.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListGetResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.get(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.get(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
            description="This is a note",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.create(
                account_id="",
                kind="ip",
                name="list1",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is a note",
        )
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListUpdateResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListUpdateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.update(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.update(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListListResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.delete(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.delete(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        list_ = await async_client.rules.lists.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListGetResponse, list_, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.get(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListGetResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.get(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.get(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
