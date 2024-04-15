# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.miniapp_1_0 import models as dingtalkminiapp__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        if UtilClient.empty(self._endpoint):
            self._endpoint = 'api.dingtalk.com'

    def create_mini_app(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppRequest,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateMiniAppHeaders()
        return self.create_mini_app_with_options(request, headers, runtime)

    async def create_mini_app_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppRequest,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateMiniAppHeaders()
        return await self.create_mini_app_with_options_async(request, headers, runtime)

    def create_mini_app_with_options(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppRequest,
        headers: dingtalkminiapp__1__0_models.CreateMiniAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateMiniAppResponse(),
            self.do_roarequest('CreateMiniApp', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/apps', 'json', req, runtime)
        )

    async def create_mini_app_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppRequest,
        headers: dingtalkminiapp__1__0_models.CreateMiniAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateMiniAppResponse(),
            await self.do_roarequest_async('CreateMiniApp', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/apps', 'json', req, runtime)
        )

    def create_mini_app_plugin(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppPluginRequest,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateMiniAppPluginHeaders()
        return self.create_mini_app_plugin_with_options(request, headers, runtime)

    async def create_mini_app_plugin_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppPluginRequest,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateMiniAppPluginHeaders()
        return await self.create_mini_app_plugin_with_options_async(request, headers, runtime)

    def create_mini_app_plugin_with_options(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppPluginRequest,
        headers: dingtalkminiapp__1__0_models.CreateMiniAppPluginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse(),
            self.do_roarequest('CreateMiniAppPlugin', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/plugins', 'json', req, runtime)
        )

    async def create_mini_app_plugin_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateMiniAppPluginRequest,
        headers: dingtalkminiapp__1__0_models.CreateMiniAppPluginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateMiniAppPluginResponse(),
            await self.do_roarequest_async('CreateMiniAppPlugin', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/plugins', 'json', req, runtime)
        )

    def create_version_across_bundle(
        self,
        request: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleRequest,
    ) -> dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateVersionAcrossBundleHeaders()
        return self.create_version_across_bundle_with_options(request, headers, runtime)

    async def create_version_across_bundle_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleRequest,
    ) -> dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.CreateVersionAcrossBundleHeaders()
        return await self.create_version_across_bundle_with_options_async(request, headers, runtime)

    def create_version_across_bundle_with_options(
        self,
        request: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleRequest,
        headers: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.source_bundle_id):
            body['sourceBundleId'] = request.source_bundle_id
        if not UtilClient.is_unset(request.source_version):
            body['sourceVersion'] = request.source_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse(),
            self.do_roarequest('CreateVersionAcrossBundle', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/versions/createAcrossBundle', 'json', req, runtime)
        )

    async def create_version_across_bundle_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleRequest,
        headers: dingtalkminiapp__1__0_models.CreateVersionAcrossBundleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.source_bundle_id):
            body['sourceBundleId'] = request.source_bundle_id
        if not UtilClient.is_unset(request.source_version):
            body['sourceVersion'] = request.source_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.CreateVersionAcrossBundleResponse(),
            await self.do_roarequest_async('CreateVersionAcrossBundle', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/versions/createAcrossBundle', 'json', req, runtime)
        )

    def get_max_version(
        self,
        request: dingtalkminiapp__1__0_models.GetMaxVersionRequest,
    ) -> dingtalkminiapp__1__0_models.GetMaxVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.GetMaxVersionHeaders()
        return self.get_max_version_with_options(request, headers, runtime)

    async def get_max_version_async(
        self,
        request: dingtalkminiapp__1__0_models.GetMaxVersionRequest,
    ) -> dingtalkminiapp__1__0_models.GetMaxVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.GetMaxVersionHeaders()
        return await self.get_max_version_with_options_async(request, headers, runtime)

    def get_max_version_with_options(
        self,
        request: dingtalkminiapp__1__0_models.GetMaxVersionRequest,
        headers: dingtalkminiapp__1__0_models.GetMaxVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.GetMaxVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.GetMaxVersionResponse(),
            self.do_roarequest('GetMaxVersion', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/apps/maxVersions', 'json', req, runtime)
        )

    async def get_max_version_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.GetMaxVersionRequest,
        headers: dingtalkminiapp__1__0_models.GetMaxVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.GetMaxVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.GetMaxVersionResponse(),
            await self.do_roarequest_async('GetMaxVersion', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/apps/maxVersions', 'json', req, runtime)
        )

    def get_setting_by_mini_app_id(
        self,
        mini_app_id: str,
    ) -> dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.GetSettingByMiniAppIdHeaders()
        return self.get_setting_by_mini_app_id_with_options(mini_app_id, headers, runtime)

    async def get_setting_by_mini_app_id_async(
        self,
        mini_app_id: str,
    ) -> dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.GetSettingByMiniAppIdHeaders()
        return await self.get_setting_by_mini_app_id_with_options_async(mini_app_id, headers, runtime)

    def get_setting_by_mini_app_id_with_options(
        self,
        mini_app_id: str,
        headers: dingtalkminiapp__1__0_models.GetSettingByMiniAppIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse:
        mini_app_id = OpenApiUtilClient.get_encode_param(mini_app_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse(),
            self.do_roarequest('GetSettingByMiniAppId', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/apps/settings', 'json', req, runtime)
        )

    async def get_setting_by_mini_app_id_with_options_async(
        self,
        mini_app_id: str,
        headers: dingtalkminiapp__1__0_models.GetSettingByMiniAppIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse:
        mini_app_id = OpenApiUtilClient.get_encode_param(mini_app_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.GetSettingByMiniAppIdResponse(),
            await self.do_roarequest_async('GetSettingByMiniAppId', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/apps/settings', 'json', req, runtime)
        )

    def invoke_html_bundle_build(
        self,
        request: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildRequest,
    ) -> dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildHeaders()
        return self.invoke_html_bundle_build_with_options(request, headers, runtime)

    async def invoke_html_bundle_build_async(
        self,
        request: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildRequest,
    ) -> dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildHeaders()
        return await self.invoke_html_bundle_build_with_options_async(request, headers, runtime)

    def invoke_html_bundle_build_with_options(
        self,
        request: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildRequest,
        headers: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse(),
            self.do_roarequest('InvokeHtmlBundleBuild', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/h5Bundles/build', 'json', req, runtime)
        )

    async def invoke_html_bundle_build_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildRequest,
        headers: dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.InvokeHtmlBundleBuildResponse(),
            await self.do_roarequest_async('InvokeHtmlBundleBuild', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/h5Bundles/build', 'json', req, runtime)
        )

    def list_avaiable_version(
        self,
        request: dingtalkminiapp__1__0_models.ListAvaiableVersionRequest,
    ) -> dingtalkminiapp__1__0_models.ListAvaiableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.ListAvaiableVersionHeaders()
        return self.list_avaiable_version_with_options(request, headers, runtime)

    async def list_avaiable_version_async(
        self,
        request: dingtalkminiapp__1__0_models.ListAvaiableVersionRequest,
    ) -> dingtalkminiapp__1__0_models.ListAvaiableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.ListAvaiableVersionHeaders()
        return await self.list_avaiable_version_with_options_async(request, headers, runtime)

    def list_avaiable_version_with_options(
        self,
        request: dingtalkminiapp__1__0_models.ListAvaiableVersionRequest,
        headers: dingtalkminiapp__1__0_models.ListAvaiableVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.ListAvaiableVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_type_set):
            body['versionTypeSet'] = request.version_type_set
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.ListAvaiableVersionResponse(),
            self.do_roarequest('ListAvaiableVersion', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/apps/versions/query', 'json', req, runtime)
        )

    async def list_avaiable_version_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.ListAvaiableVersionRequest,
        headers: dingtalkminiapp__1__0_models.ListAvaiableVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.ListAvaiableVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_type_set):
            body['versionTypeSet'] = request.version_type_set
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.ListAvaiableVersionResponse(),
            await self.do_roarequest_async('ListAvaiableVersion', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/apps/versions/query', 'json', req, runtime)
        )

    def query_html_bundle_build(
        self,
        request: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildRequest,
    ) -> dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.QueryHtmlBundleBuildHeaders()
        return self.query_html_bundle_build_with_options(request, headers, runtime)

    async def query_html_bundle_build_async(
        self,
        request: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildRequest,
    ) -> dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.QueryHtmlBundleBuildHeaders()
        return await self.query_html_bundle_build_with_options_async(request, headers, runtime)

    def query_html_bundle_build_with_options(
        self,
        request: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildRequest,
        headers: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse(),
            self.do_roarequest('QueryHtmlBundleBuild', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/h5Bundles/buildResults', 'json', req, runtime)
        )

    async def query_html_bundle_build_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildRequest,
        headers: dingtalkminiapp__1__0_models.QueryHtmlBundleBuildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.QueryHtmlBundleBuildResponse(),
            await self.do_roarequest_async('QueryHtmlBundleBuild', 'miniapp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/miniapp/h5Bundles/buildResults', 'json', req, runtime)
        )

    def set_extend_setting(
        self,
        request: dingtalkminiapp__1__0_models.SetExtendSettingRequest,
    ) -> dingtalkminiapp__1__0_models.SetExtendSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.SetExtendSettingHeaders()
        return self.set_extend_setting_with_options(request, headers, runtime)

    async def set_extend_setting_async(
        self,
        request: dingtalkminiapp__1__0_models.SetExtendSettingRequest,
    ) -> dingtalkminiapp__1__0_models.SetExtendSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.SetExtendSettingHeaders()
        return await self.set_extend_setting_with_options_async(request, headers, runtime)

    def set_extend_setting_with_options(
        self,
        request: dingtalkminiapp__1__0_models.SetExtendSettingRequest,
        headers: dingtalkminiapp__1__0_models.SetExtendSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.SetExtendSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_h5bundle):
            body['buildH5Bundle'] = request.build_h5bundle
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.SetExtendSettingResponse(),
            self.do_roarequest('SetExtendSetting', 'miniapp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/miniapp/apps/settings', 'json', req, runtime)
        )

    async def set_extend_setting_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.SetExtendSettingRequest,
        headers: dingtalkminiapp__1__0_models.SetExtendSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.SetExtendSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_h5bundle):
            body['buildH5Bundle'] = request.build_h5bundle
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.SetExtendSettingResponse(),
            await self.do_roarequest_async('SetExtendSetting', 'miniapp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/miniapp/apps/settings', 'json', req, runtime)
        )

    def update_version_status(
        self,
        request: dingtalkminiapp__1__0_models.UpdateVersionStatusRequest,
    ) -> dingtalkminiapp__1__0_models.UpdateVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.UpdateVersionStatusHeaders()
        return self.update_version_status_with_options(request, headers, runtime)

    async def update_version_status_async(
        self,
        request: dingtalkminiapp__1__0_models.UpdateVersionStatusRequest,
    ) -> dingtalkminiapp__1__0_models.UpdateVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkminiapp__1__0_models.UpdateVersionStatusHeaders()
        return await self.update_version_status_with_options_async(request, headers, runtime)

    def update_version_status_with_options(
        self,
        request: dingtalkminiapp__1__0_models.UpdateVersionStatusRequest,
        headers: dingtalkminiapp__1__0_models.UpdateVersionStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.UpdateVersionStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.version_type):
            body['versionType'] = request.version_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.UpdateVersionStatusResponse(),
            self.do_roarequest('UpdateVersionStatus', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/versions/status', 'json', req, runtime)
        )

    async def update_version_status_with_options_async(
        self,
        request: dingtalkminiapp__1__0_models.UpdateVersionStatusRequest,
        headers: dingtalkminiapp__1__0_models.UpdateVersionStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkminiapp__1__0_models.UpdateVersionStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.version_type):
            body['versionType'] = request.version_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkminiapp__1__0_models.UpdateVersionStatusResponse(),
            await self.do_roarequest_async('UpdateVersionStatus', 'miniapp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/miniapp/versions/status', 'json', req, runtime)
        )
