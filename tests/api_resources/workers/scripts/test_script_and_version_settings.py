# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.scripts import (
    ScriptAndVersionSettingGetResponse,
    ScriptAndVersionSettingEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScriptAndVersionSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        script_and_version_setting = client.workers.scripts.script_and_version_settings.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        script_and_version_setting = client.workers.scripts.script_and_version_settings.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings={
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "compatibility_date": "2021-01-01",
                "compatibility_flags": ["nodejs_compat"],
                "limits": {"cpu_ms": 50},
                "logpush": False,
                "migrations": {
                    "deleted_classes": ["string"],
                    "new_classes": ["string"],
                    "new_sqlite_classes": ["string"],
                    "new_tag": "v2",
                    "old_tag": "v1",
                    "renamed_classes": [
                        {
                            "from": "from",
                            "to": "to",
                        }
                    ],
                    "transferred_classes": [
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        }
                    ],
                },
                "observability": {
                    "enabled": True,
                    "head_sampling_rate": 0.1,
                    "logs": {
                        "enabled": True,
                        "invocation_logs": True,
                        "head_sampling_rate": 0.1,
                    },
                },
                "placement": {"mode": "smart"},
                "tags": ["my-tag"],
                "tail_consumers": [
                    {
                        "service": "my-log-consumer",
                        "environment": "production",
                        "namespace": "my-namespace",
                    }
                ],
                "usage_model": "standard",
            },
        )
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.workers.scripts.script_and_version_settings.with_raw_response.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script_and_version_setting = response.parse()
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.workers.scripts.script_and_version_settings.with_streaming_response.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script_and_version_setting = response.parse()
            assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.script_and_version_settings.with_raw_response.edit(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.script_and_version_settings.with_raw_response.edit(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        script_and_version_setting = client.workers.scripts.script_and_version_settings.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.script_and_version_settings.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script_and_version_setting = response.parse()
        assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.script_and_version_settings.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script_and_version_setting = response.parse()
            assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.script_and_version_settings.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.script_and_version_settings.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncScriptAndVersionSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        script_and_version_setting = await async_client.workers.scripts.script_and_version_settings.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        script_and_version_setting = await async_client.workers.scripts.script_and_version_settings.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings={
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "compatibility_date": "2021-01-01",
                "compatibility_flags": ["nodejs_compat"],
                "limits": {"cpu_ms": 50},
                "logpush": False,
                "migrations": {
                    "deleted_classes": ["string"],
                    "new_classes": ["string"],
                    "new_sqlite_classes": ["string"],
                    "new_tag": "v2",
                    "old_tag": "v1",
                    "renamed_classes": [
                        {
                            "from": "from",
                            "to": "to",
                        }
                    ],
                    "transferred_classes": [
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        }
                    ],
                },
                "observability": {
                    "enabled": True,
                    "head_sampling_rate": 0.1,
                    "logs": {
                        "enabled": True,
                        "invocation_logs": True,
                        "head_sampling_rate": 0.1,
                    },
                },
                "placement": {"mode": "smart"},
                "tags": ["my-tag"],
                "tail_consumers": [
                    {
                        "service": "my-log-consumer",
                        "environment": "production",
                        "namespace": "my-namespace",
                    }
                ],
                "usage_model": "standard",
            },
        )
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.script_and_version_settings.with_raw_response.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script_and_version_setting = await response.parse()
        assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.script_and_version_settings.with_streaming_response.edit(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script_and_version_setting = await response.parse()
            assert_matches_type(ScriptAndVersionSettingEditResponse, script_and_version_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.script_and_version_settings.with_raw_response.edit(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.script_and_version_settings.with_raw_response.edit(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        script_and_version_setting = await async_client.workers.scripts.script_and_version_settings.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.script_and_version_settings.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script_and_version_setting = await response.parse()
        assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.script_and_version_settings.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script_and_version_setting = await response.parse()
            assert_matches_type(ScriptAndVersionSettingGetResponse, script_and_version_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.script_and_version_settings.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.script_and_version_settings.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
