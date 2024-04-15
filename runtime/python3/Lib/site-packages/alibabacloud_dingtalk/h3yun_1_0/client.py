# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
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

    def batch_insert_biz_object(
        self,
        request: dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders()
        return self.batch_insert_biz_object_with_options(request, headers, runtime)

    async def batch_insert_biz_object_async(
        self,
        request: dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders()
        return await self.batch_insert_biz_object_with_options_async(request, headers, runtime)

    def batch_insert_biz_object_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_json_array):
            body['bizObjectJsonArray'] = request.biz_object_json_array
        if not UtilClient.is_unset(request.is_draft):
            body['isDraft'] = request.is_draft
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse(),
            self.do_roarequest('BatchInsertBizObject', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances/batch', 'json', req, runtime)
        )

    async def batch_insert_biz_object_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_json_array):
            body['bizObjectJsonArray'] = request.biz_object_json_array
        if not UtilClient.is_unset(request.is_draft):
            body['isDraft'] = request.is_draft
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.BatchInsertBizObjectResponse(),
            await self.do_roarequest_async('BatchInsertBizObject', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances/batch', 'json', req, runtime)
        )

    def cancel_process_instance(
        self,
        request: dingtalkh_3yun__1__0_models.CancelProcessInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CancelProcessInstanceHeaders()
        return self.cancel_process_instance_with_options(request, headers, runtime)

    async def cancel_process_instance_async(
        self,
        request: dingtalkh_3yun__1__0_models.CancelProcessInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CancelProcessInstanceHeaders()
        return await self.cancel_process_instance_with_options_async(request, headers, runtime)

    def cancel_process_instance_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.CancelProcessInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.CancelProcessInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.process_instance_id):
            body['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse(),
            self.do_roarequest('CancelProcessInstance', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/processes/instances/cancel', 'json', req, runtime)
        )

    async def cancel_process_instance_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.CancelProcessInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.CancelProcessInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.process_instance_id):
            body['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.CancelProcessInstanceResponse(),
            await self.do_roarequest_async('CancelProcessInstance', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/processes/instances/cancel', 'json', req, runtime)
        )

    def create_biz_object(
        self,
        request: dingtalkh_3yun__1__0_models.CreateBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.CreateBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CreateBizObjectHeaders()
        return self.create_biz_object_with_options(request, headers, runtime)

    async def create_biz_object_async(
        self,
        request: dingtalkh_3yun__1__0_models.CreateBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.CreateBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CreateBizObjectHeaders()
        return await self.create_biz_object_with_options_async(request, headers, runtime)

    def create_biz_object_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.CreateBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.CreateBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CreateBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_json):
            body['bizObjectJson'] = request.biz_object_json
        if not UtilClient.is_unset(request.is_draft):
            body['isDraft'] = request.is_draft
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.CreateBizObjectResponse(),
            self.do_roarequest('CreateBizObject', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )

    async def create_biz_object_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.CreateBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.CreateBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CreateBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_json):
            body['bizObjectJson'] = request.biz_object_json
        if not UtilClient.is_unset(request.is_draft):
            body['isDraft'] = request.is_draft
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.CreateBizObjectResponse(),
            await self.do_roarequest_async('CreateBizObject', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )

    def create_processes_instance(
        self,
        request: dingtalkh_3yun__1__0_models.CreateProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CreateProcessesInstanceHeaders()
        return self.create_processes_instance_with_options(request, headers, runtime)

    async def create_processes_instance_async(
        self,
        request: dingtalkh_3yun__1__0_models.CreateProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.CreateProcessesInstanceHeaders()
        return await self.create_processes_instance_with_options_async(request, headers, runtime)

    def create_processes_instance_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.CreateProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.CreateProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_id):
            body['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse(),
            self.do_roarequest('CreateProcessesInstance', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    async def create_processes_instance_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.CreateProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.CreateProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_id):
            body['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.CreateProcessesInstanceResponse(),
            await self.do_roarequest_async('CreateProcessesInstance', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    def delete_biz_object(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.DeleteBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.DeleteBizObjectHeaders()
        return self.delete_biz_object_with_options(request, headers, runtime)

    async def delete_biz_object_async(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.DeleteBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.DeleteBizObjectHeaders()
        return await self.delete_biz_object_with_options_async(request, headers, runtime)

    def delete_biz_object_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.DeleteBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.DeleteBizObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.DeleteBizObjectResponse(),
            self.do_roarequest('DeleteBizObject', 'h3yun_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )

    async def delete_biz_object_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.DeleteBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.DeleteBizObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.DeleteBizObjectResponse(),
            await self.do_roarequest_async('DeleteBizObject', 'h3yun_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )

    def delete_processes_instance(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.DeleteProcessesInstanceHeaders()
        return self.delete_processes_instance_with_options(request, headers, runtime)

    async def delete_processes_instance_async(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.DeleteProcessesInstanceHeaders()
        return await self.delete_processes_instance_with_options_async(request, headers, runtime)

    def delete_processes_instance_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_auto_update_biz_object):
            query['isAutoUpdateBizObject'] = request.is_auto_update_biz_object
        if not UtilClient.is_unset(request.process_instance_id):
            query['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse(),
            self.do_roarequest('DeleteProcessesInstance', 'h3yun_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    async def delete_processes_instance_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.DeleteProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_auto_update_biz_object):
            query['isAutoUpdateBizObject'] = request.is_auto_update_biz_object
        if not UtilClient.is_unset(request.process_instance_id):
            query['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.DeleteProcessesInstanceResponse(),
            await self.do_roarequest_async('DeleteProcessesInstance', 'h3yun_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    def get_apps(
        self,
        request: dingtalkh_3yun__1__0_models.GetAppsRequest,
    ) -> dingtalkh_3yun__1__0_models.GetAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetAppsHeaders()
        return self.get_apps_with_options(request, headers, runtime)

    async def get_apps_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetAppsRequest,
    ) -> dingtalkh_3yun__1__0_models.GetAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetAppsHeaders()
        return await self.get_apps_with_options_async(request, headers, runtime)

    def get_apps_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetAppsRequest,
        headers: dingtalkh_3yun__1__0_models.GetAppsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
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
            dingtalkh_3yun__1__0_models.GetAppsResponse(),
            self.do_roarequest('GetApps', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/apps/search', 'json', req, runtime)
        )

    async def get_apps_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetAppsRequest,
        headers: dingtalkh_3yun__1__0_models.GetAppsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
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
            dingtalkh_3yun__1__0_models.GetAppsResponse(),
            await self.do_roarequest_async('GetApps', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/apps/search', 'json', req, runtime)
        )

    def get_attachment_temporary_url(
        self,
        request: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlRequest,
    ) -> dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlHeaders()
        return self.get_attachment_temporary_url_with_options(request, headers, runtime)

    async def get_attachment_temporary_url_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlRequest,
    ) -> dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlHeaders()
        return await self.get_attachment_temporary_url_with_options_async(request, headers, runtime)

    def get_attachment_temporary_url_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlRequest,
        headers: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attachment_id):
            query['attachmentId'] = request.attachment_id
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
            dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse(),
            self.do_roarequest('GetAttachmentTemporaryUrl', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/attachments/temporaryUrls', 'json', req, runtime)
        )

    async def get_attachment_temporary_url_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlRequest,
        headers: dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attachment_id):
            query['attachmentId'] = request.attachment_id
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
            dingtalkh_3yun__1__0_models.GetAttachmentTemporaryUrlResponse(),
            await self.do_roarequest_async('GetAttachmentTemporaryUrl', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/attachments/temporaryUrls', 'json', req, runtime)
        )

    def get_organizations(
        self,
        request: dingtalkh_3yun__1__0_models.GetOrganizationsRequest,
    ) -> dingtalkh_3yun__1__0_models.GetOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetOrganizationsHeaders()
        return self.get_organizations_with_options(request, headers, runtime)

    async def get_organizations_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetOrganizationsRequest,
    ) -> dingtalkh_3yun__1__0_models.GetOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetOrganizationsHeaders()
        return await self.get_organizations_with_options_async(request, headers, runtime)

    def get_organizations_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetOrganizationsRequest,
        headers: dingtalkh_3yun__1__0_models.GetOrganizationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['departmentId'] = request.department_id
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
            dingtalkh_3yun__1__0_models.GetOrganizationsResponse(),
            self.do_roarequest('GetOrganizations', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/departments', 'json', req, runtime)
        )

    async def get_organizations_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetOrganizationsRequest,
        headers: dingtalkh_3yun__1__0_models.GetOrganizationsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['departmentId'] = request.department_id
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
            dingtalkh_3yun__1__0_models.GetOrganizationsResponse(),
            await self.do_roarequest_async('GetOrganizations', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/departments', 'json', req, runtime)
        )

    def get_role_users(
        self,
        request: dingtalkh_3yun__1__0_models.GetRoleUsersRequest,
    ) -> dingtalkh_3yun__1__0_models.GetRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetRoleUsersHeaders()
        return self.get_role_users_with_options(request, headers, runtime)

    async def get_role_users_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetRoleUsersRequest,
    ) -> dingtalkh_3yun__1__0_models.GetRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetRoleUsersHeaders()
        return await self.get_role_users_with_options_async(request, headers, runtime)

    def get_role_users_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetRoleUsersRequest,
        headers: dingtalkh_3yun__1__0_models.GetRoleUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetRoleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['roleId'] = request.role_id
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
            dingtalkh_3yun__1__0_models.GetRoleUsersResponse(),
            self.do_roarequest('GetRoleUsers', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/roles/roleUsers', 'json', req, runtime)
        )

    async def get_role_users_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetRoleUsersRequest,
        headers: dingtalkh_3yun__1__0_models.GetRoleUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetRoleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['roleId'] = request.role_id
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
            dingtalkh_3yun__1__0_models.GetRoleUsersResponse(),
            await self.do_roarequest_async('GetRoleUsers', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/roles/roleUsers', 'json', req, runtime)
        )

    def get_roles(self) -> dingtalkh_3yun__1__0_models.GetRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetRolesHeaders()
        return self.get_roles_with_options(headers, runtime)

    async def get_roles_async(self) -> dingtalkh_3yun__1__0_models.GetRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetRolesHeaders()
        return await self.get_roles_with_options_async(headers, runtime)

    def get_roles_with_options(
        self,
        headers: dingtalkh_3yun__1__0_models.GetRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkh_3yun__1__0_models.GetRolesResponse(),
            self.do_roarequest('GetRoles', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/roles', 'json', req, runtime)
        )

    async def get_roles_with_options_async(
        self,
        headers: dingtalkh_3yun__1__0_models.GetRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkh_3yun__1__0_models.GetRolesResponse(),
            await self.do_roarequest_async('GetRoles', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/roles', 'json', req, runtime)
        )

    def get_upload_url(
        self,
        request: dingtalkh_3yun__1__0_models.GetUploadUrlRequest,
    ) -> dingtalkh_3yun__1__0_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetUploadUrlHeaders()
        return self.get_upload_url_with_options(request, headers, runtime)

    async def get_upload_url_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetUploadUrlRequest,
    ) -> dingtalkh_3yun__1__0_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetUploadUrlHeaders()
        return await self.get_upload_url_with_options_async(request, headers, runtime)

    def get_upload_url_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetUploadUrlRequest,
        headers: dingtalkh_3yun__1__0_models.GetUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetUploadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.is_overwrite):
            query['isOverwrite'] = request.is_overwrite
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.GetUploadUrlResponse(),
            self.do_roarequest('GetUploadUrl', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/attachments/uploadUrls', 'json', req, runtime)
        )

    async def get_upload_url_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetUploadUrlRequest,
        headers: dingtalkh_3yun__1__0_models.GetUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetUploadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.is_overwrite):
            query['isOverwrite'] = request.is_overwrite
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.GetUploadUrlResponse(),
            await self.do_roarequest_async('GetUploadUrl', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/attachments/uploadUrls', 'json', req, runtime)
        )

    def get_users(
        self,
        request: dingtalkh_3yun__1__0_models.GetUsersRequest,
    ) -> dingtalkh_3yun__1__0_models.GetUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetUsersHeaders()
        return self.get_users_with_options(request, headers, runtime)

    async def get_users_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetUsersRequest,
    ) -> dingtalkh_3yun__1__0_models.GetUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.GetUsersHeaders()
        return await self.get_users_with_options_async(request, headers, runtime)

    def get_users_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.GetUsersRequest,
        headers: dingtalkh_3yun__1__0_models.GetUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['departmentId'] = request.department_id
        if not UtilClient.is_unset(request.is_recursive):
            query['isRecursive'] = request.is_recursive
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
            dingtalkh_3yun__1__0_models.GetUsersResponse(),
            self.do_roarequest('GetUsers', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/users', 'json', req, runtime)
        )

    async def get_users_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.GetUsersRequest,
        headers: dingtalkh_3yun__1__0_models.GetUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.GetUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['departmentId'] = request.department_id
        if not UtilClient.is_unset(request.is_recursive):
            query['isRecursive'] = request.is_recursive
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
            dingtalkh_3yun__1__0_models.GetUsersResponse(),
            await self.do_roarequest_async('GetUsers', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/users', 'json', req, runtime)
        )

    def load_biz_fields(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizFieldsRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders()
        return self.load_biz_fields_with_options(request, headers, runtime)

    async def load_biz_fields_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizFieldsRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders()
        return await self.load_biz_fields_with_options_async(request, headers, runtime)

    def load_biz_fields_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizFieldsRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.LoadBizFieldsResponse(),
            self.do_roarequest('LoadBizFields', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/forms/loadBizFields', 'json', req, runtime)
        )

    async def load_biz_fields_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizFieldsRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.LoadBizFieldsResponse(),
            await self.do_roarequest_async('LoadBizFields', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/forms/loadBizFields', 'json', req, runtime)
        )

    def load_biz_object(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizObjectHeaders()
        return self.load_biz_object_with_options(request, headers, runtime)

    async def load_biz_object_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizObjectHeaders()
        return await self.load_biz_object_with_options_async(request, headers, runtime)

    def load_biz_object_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.LoadBizObjectResponse(),
            self.do_roarequest('LoadBizObject', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/forms/instances/loadInstances', 'json', req, runtime)
        )

    async def load_biz_object_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.LoadBizObjectResponse(),
            await self.do_roarequest_async('LoadBizObject', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/forms/instances/loadInstances', 'json', req, runtime)
        )

    def load_biz_objects(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectsRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders()
        return self.load_biz_objects_with_options(request, headers, runtime)

    async def load_biz_objects_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectsRequest,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders()
        return await self.load_biz_objects_with_options_async(request, headers, runtime)

    def load_biz_objects_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectsRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.matcher_json):
            body['matcherJson'] = request.matcher_json
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_fields):
            body['returnFields'] = request.return_fields
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
        if not UtilClient.is_unset(request.sort_by_fields):
            body['sortByFields'] = request.sort_by_fields
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
            dingtalkh_3yun__1__0_models.LoadBizObjectsResponse(),
            self.do_roarequest('LoadBizObjects', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances/search', 'json', req, runtime)
        )

    async def load_biz_objects_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.LoadBizObjectsRequest,
        headers: dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.LoadBizObjectsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.matcher_json):
            body['matcherJson'] = request.matcher_json
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_fields):
            body['returnFields'] = request.return_fields
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
        if not UtilClient.is_unset(request.sort_by_fields):
            body['sortByFields'] = request.sort_by_fields
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
            dingtalkh_3yun__1__0_models.LoadBizObjectsResponse(),
            await self.do_roarequest_async('LoadBizObjects', 'h3yun_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/h3yun/forms/instances/search', 'json', req, runtime)
        )

    def query_app_function_nodes(
        self,
        request: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryAppFunctionNodesHeaders()
        return self.query_app_function_nodes_with_options(request, headers, runtime)

    async def query_app_function_nodes_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryAppFunctionNodesHeaders()
        return await self.query_app_function_nodes_with_options_async(request, headers, runtime)

    def query_app_function_nodes_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesRequest,
        headers: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
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
            dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse(),
            self.do_roarequest('QueryAppFunctionNodes', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/apps/functionNodes', 'json', req, runtime)
        )

    async def query_app_function_nodes_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesRequest,
        headers: dingtalkh_3yun__1__0_models.QueryAppFunctionNodesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
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
            dingtalkh_3yun__1__0_models.QueryAppFunctionNodesResponse(),
            await self.do_roarequest_async('QueryAppFunctionNodes', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/apps/functionNodes', 'json', req, runtime)
        )

    def query_processes_instance(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryProcessesInstanceHeaders()
        return self.query_processes_instance_with_options(request, headers, runtime)

    async def query_processes_instance_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesInstanceRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryProcessesInstanceHeaders()
        return await self.query_processes_instance_with_options_async(request, headers, runtime)

    def query_processes_instance_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.QueryProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse(),
            self.do_roarequest('QueryProcessesInstance', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    async def query_processes_instance_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesInstanceRequest,
        headers: dingtalkh_3yun__1__0_models.QueryProcessesInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_object_id):
            query['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.schema_code):
            query['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.QueryProcessesInstanceResponse(),
            await self.do_roarequest_async('QueryProcessesInstance', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/processes/instances', 'json', req, runtime)
        )

    def query_processes_work_items(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders()
        return self.query_processes_work_items_with_options(request, headers, runtime)

    async def query_processes_work_items_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders()
        return await self.query_processes_work_items_with_options_async(request, headers, runtime)

    def query_processes_work_items_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest,
        headers: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.process_instance_id):
            query['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse(),
            self.do_roarequest('QueryProcessesWorkItems', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/processes/workItems', 'json', req, runtime)
        )

    async def query_processes_work_items_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest,
        headers: dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.process_instance_id):
            query['processInstanceId'] = request.process_instance_id
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
            dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsResponse(),
            await self.do_roarequest_async('QueryProcessesWorkItems', 'h3yun_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/h3yun/processes/workItems', 'json', req, runtime)
        )

    def update_biz_object(
        self,
        request: dingtalkh_3yun__1__0_models.UpdateBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.UpdateBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.UpdateBizObjectHeaders()
        return self.update_biz_object_with_options(request, headers, runtime)

    async def update_biz_object_async(
        self,
        request: dingtalkh_3yun__1__0_models.UpdateBizObjectRequest,
    ) -> dingtalkh_3yun__1__0_models.UpdateBizObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkh_3yun__1__0_models.UpdateBizObjectHeaders()
        return await self.update_biz_object_with_options_async(request, headers, runtime)

    def update_biz_object_with_options(
        self,
        request: dingtalkh_3yun__1__0_models.UpdateBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.UpdateBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.UpdateBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_id):
            body['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.biz_object_json):
            body['bizObjectJson'] = request.biz_object_json
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.UpdateBizObjectResponse(),
            self.do_roarequest('UpdateBizObject', 'h3yun_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )

    async def update_biz_object_with_options_async(
        self,
        request: dingtalkh_3yun__1__0_models.UpdateBizObjectRequest,
        headers: dingtalkh_3yun__1__0_models.UpdateBizObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkh_3yun__1__0_models.UpdateBizObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_object_id):
            body['bizObjectId'] = request.biz_object_id
        if not UtilClient.is_unset(request.biz_object_json):
            body['bizObjectJson'] = request.biz_object_json
        if not UtilClient.is_unset(request.schema_code):
            body['schemaCode'] = request.schema_code
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
            dingtalkh_3yun__1__0_models.UpdateBizObjectResponse(),
            await self.do_roarequest_async('UpdateBizObject', 'h3yun_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/h3yun/forms/instances', 'json', req, runtime)
        )
