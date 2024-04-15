# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.occupationauth_1_0 import models as dingtalkoccupationauth__1__0_models
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

    def check_user_task_status(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusRequest,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoccupationauth__1__0_models.CheckUserTaskStatusHeaders()
        return self.check_user_task_status_with_options(request, headers, runtime)

    async def check_user_task_status_async(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusRequest,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoccupationauth__1__0_models.CheckUserTaskStatusHeaders()
        return await self.check_user_task_status_with_options_async(request, headers, runtime)

    def check_user_task_status_with_options(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusRequest,
        headers: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.province_code):
            body['provinceCode'] = request.province_code
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
            dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse(),
            self.do_roarequest('CheckUserTaskStatus', 'occupationauth_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/occupationauth/auths/userTasks', 'json', req, runtime)
        )

    async def check_user_task_status_with_options_async(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusRequest,
        headers: dingtalkoccupationauth__1__0_models.CheckUserTaskStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.province_code):
            body['provinceCode'] = request.province_code
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
            dingtalkoccupationauth__1__0_models.CheckUserTaskStatusResponse(),
            await self.do_roarequest_async('CheckUserTaskStatus', 'occupationauth_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/occupationauth/auths/userTasks', 'json', req, runtime)
        )

    def check_user_tasks_status(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders()
        return self.check_user_tasks_status_with_options(request, headers, runtime)

    async def check_user_tasks_status_async(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders()
        return await self.check_user_tasks_status_with_options_async(request, headers, runtime)

    def check_user_tasks_status_with_options(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest,
        headers: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.province_code):
            query['provinceCode'] = request.province_code
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
            dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse(),
            self.do_roarequest('CheckUserTasksStatus', 'occupationauth_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/occupationauth/userTasks/check', 'json', req, runtime)
        )

    async def check_user_tasks_status_with_options_async(
        self,
        request: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest,
        headers: dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.province_code):
            query['provinceCode'] = request.province_code
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
            dingtalkoccupationauth__1__0_models.CheckUserTasksStatusResponse(),
            await self.do_roarequest_async('CheckUserTasksStatus', 'occupationauth_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/occupationauth/userTasks/check', 'json', req, runtime)
        )
