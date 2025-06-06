# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.addressing import (
    AddressMap,
    AddressMapGetResponse,
    AddressMapCreateResponse,
    AddressMapDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressMaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="My Ecommerce zones",
            enabled=True,
            ips=["192.0.2.1"],
            memberships=[
                {
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                }
            ],
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.with_raw_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.with_streaming_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.with_raw_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.with_streaming_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.with_raw_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.with_streaming_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.delete(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.delete(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.with_raw_response.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.with_streaming_response.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.edit(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.edit(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        address_map = client.addressing.address_maps.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.with_raw_response.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.with_streaming_response.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.get(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.get(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )


class TestAsyncAddressMaps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="My Ecommerce zones",
            enabled=True,
            ips=["192.0.2.1"],
            memberships=[
                {
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                }
            ],
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AddressMapDeleteResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.delete(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.delete(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.edit(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.edit(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.edit(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addressing.address_maps.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.get(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.get(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.get(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )
