# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.workrecord_1_0 import models as dingtalkworkrecord__1__0_models
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

    def count_work_record(
        self,
        request: dingtalkworkrecord__1__0_models.CountWorkRecordRequest,
    ) -> dingtalkworkrecord__1__0_models.CountWorkRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkworkrecord__1__0_models.CountWorkRecordHeaders()
        return self.count_work_record_with_options(request, headers, runtime)

    async def count_work_record_async(
        self,
        request: dingtalkworkrecord__1__0_models.CountWorkRecordRequest,
    ) -> dingtalkworkrecord__1__0_models.CountWorkRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkworkrecord__1__0_models.CountWorkRecordHeaders()
        return await self.count_work_record_with_options_async(request, headers, runtime)

    def count_work_record_with_options(
        self,
        request: dingtalkworkrecord__1__0_models.CountWorkRecordRequest,
        headers: dingtalkworkrecord__1__0_models.CountWorkRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkworkrecord__1__0_models.CountWorkRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkworkrecord__1__0_models.CountWorkRecordResponse(),
            self.do_roarequest('CountWorkRecord', 'workrecord_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/workrecord/counts', 'json', req, runtime)
        )

    async def count_work_record_with_options_async(
        self,
        request: dingtalkworkrecord__1__0_models.CountWorkRecordRequest,
        headers: dingtalkworkrecord__1__0_models.CountWorkRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkworkrecord__1__0_models.CountWorkRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkworkrecord__1__0_models.CountWorkRecordResponse(),
            await self.do_roarequest_async('CountWorkRecord', 'workrecord_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/workrecord/counts', 'json', req, runtime)
        )
