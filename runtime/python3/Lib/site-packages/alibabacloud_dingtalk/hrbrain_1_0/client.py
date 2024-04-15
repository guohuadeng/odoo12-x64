# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
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

    def sync_data(
        self,
        request: dingtalkhrbrain__1__0_models.SyncDataRequest,
    ) -> dingtalkhrbrain__1__0_models.SyncDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrbrain__1__0_models.SyncDataHeaders()
        return self.sync_data_with_options(request, headers, runtime)

    async def sync_data_async(
        self,
        request: dingtalkhrbrain__1__0_models.SyncDataRequest,
    ) -> dingtalkhrbrain__1__0_models.SyncDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrbrain__1__0_models.SyncDataHeaders()
        return await self.sync_data_with_options_async(request, headers, runtime)

    def sync_data_with_options(
        self,
        request: dingtalkhrbrain__1__0_models.SyncDataRequest,
        headers: dingtalkhrbrain__1__0_models.SyncDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrbrain__1__0_models.SyncDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['dataId'] = request.data_id
        if not UtilClient.is_unset(request.etl_time):
            body['etlTime'] = request.etl_time
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.schema_id):
            body['schemaId'] = request.schema_id
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
            dingtalkhrbrain__1__0_models.SyncDataResponse(),
            self.do_roarequest('SyncData', 'hrbrain_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrbrain/datas', 'json', req, runtime)
        )

    async def sync_data_with_options_async(
        self,
        request: dingtalkhrbrain__1__0_models.SyncDataRequest,
        headers: dingtalkhrbrain__1__0_models.SyncDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrbrain__1__0_models.SyncDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            body['dataId'] = request.data_id
        if not UtilClient.is_unset(request.etl_time):
            body['etlTime'] = request.etl_time
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.schema_id):
            body['schemaId'] = request.schema_id
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
            dingtalkhrbrain__1__0_models.SyncDataResponse(),
            await self.do_roarequest_async('SyncData', 'hrbrain_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrbrain/datas', 'json', req, runtime)
        )
