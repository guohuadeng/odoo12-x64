# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.connector_1_0 import models as dingtalkconnector__1__0_models
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

    def create_action(
        self,
        request: dingtalkconnector__1__0_models.CreateActionRequest,
    ) -> dingtalkconnector__1__0_models.CreateActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateActionHeaders()
        return self.create_action_with_options(request, headers, runtime)

    async def create_action_async(
        self,
        request: dingtalkconnector__1__0_models.CreateActionRequest,
    ) -> dingtalkconnector__1__0_models.CreateActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateActionHeaders()
        return await self.create_action_with_options_async(request, headers, runtime)

    def create_action_with_options(
        self,
        request: dingtalkconnector__1__0_models.CreateActionRequest,
        headers: dingtalkconnector__1__0_models.CreateActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_info):
            body['actionInfo'] = request.action_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.CreateActionResponse(),
            self.do_roarequest('CreateAction', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/actions', 'json', req, runtime)
        )

    async def create_action_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.CreateActionRequest,
        headers: dingtalkconnector__1__0_models.CreateActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_info):
            body['actionInfo'] = request.action_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.CreateActionResponse(),
            await self.do_roarequest_async('CreateAction', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/actions', 'json', req, runtime)
        )

    def create_connector(
        self,
        request: dingtalkconnector__1__0_models.CreateConnectorRequest,
    ) -> dingtalkconnector__1__0_models.CreateConnectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateConnectorHeaders()
        return self.create_connector_with_options(request, headers, runtime)

    async def create_connector_async(
        self,
        request: dingtalkconnector__1__0_models.CreateConnectorRequest,
    ) -> dingtalkconnector__1__0_models.CreateConnectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateConnectorHeaders()
        return await self.create_connector_with_options_async(request, headers, runtime)

    def create_connector_with_options(
        self,
        request: dingtalkconnector__1__0_models.CreateConnectorRequest,
        headers: dingtalkconnector__1__0_models.CreateConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateConnectorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connector_info):
            body['connectorInfo'] = request.connector_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.CreateConnectorResponse(),
            self.do_roarequest('CreateConnector', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/connectors', 'json', req, runtime)
        )

    async def create_connector_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.CreateConnectorRequest,
        headers: dingtalkconnector__1__0_models.CreateConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateConnectorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connector_info):
            body['connectorInfo'] = request.connector_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.CreateConnectorResponse(),
            await self.do_roarequest_async('CreateConnector', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/connectors', 'json', req, runtime)
        )

    def create_trigger(
        self,
        request: dingtalkconnector__1__0_models.CreateTriggerRequest,
    ) -> dingtalkconnector__1__0_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateTriggerHeaders()
        return self.create_trigger_with_options(request, headers, runtime)

    async def create_trigger_async(
        self,
        request: dingtalkconnector__1__0_models.CreateTriggerRequest,
    ) -> dingtalkconnector__1__0_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.CreateTriggerHeaders()
        return await self.create_trigger_with_options_async(request, headers, runtime)

    def create_trigger_with_options(
        self,
        request: dingtalkconnector__1__0_models.CreateTriggerRequest,
        headers: dingtalkconnector__1__0_models.CreateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
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
            dingtalkconnector__1__0_models.CreateTriggerResponse(),
            self.do_roarequest('CreateTrigger', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/triggers', 'json', req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.CreateTriggerRequest,
        headers: dingtalkconnector__1__0_models.CreateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
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
            dingtalkconnector__1__0_models.CreateTriggerResponse(),
            await self.do_roarequest_async('CreateTrigger', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/triggers', 'json', req, runtime)
        )

    def pull_data_by_page(
        self,
        request: dingtalkconnector__1__0_models.PullDataByPageRequest,
    ) -> dingtalkconnector__1__0_models.PullDataByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.PullDataByPageHeaders()
        return self.pull_data_by_page_with_options(request, headers, runtime)

    async def pull_data_by_page_async(
        self,
        request: dingtalkconnector__1__0_models.PullDataByPageRequest,
    ) -> dingtalkconnector__1__0_models.PullDataByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.PullDataByPageHeaders()
        return await self.pull_data_by_page_with_options_async(request, headers, runtime)

    def pull_data_by_page_with_options(
        self,
        request: dingtalkconnector__1__0_models.PullDataByPageRequest,
        headers: dingtalkconnector__1__0_models.PullDataByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.PullDataByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.data_model_id):
            query['dataModelId'] = request.data_model_id
        if not UtilClient.is_unset(request.datetime_filter_field):
            query['datetimeFilterField'] = request.datetime_filter_field
        if not UtilClient.is_unset(request.max_datetime):
            query['maxDatetime'] = request.max_datetime
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_datetime):
            query['minDatetime'] = request.min_datetime
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
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
            dingtalkconnector__1__0_models.PullDataByPageResponse(),
            self.do_roarequest('PullDataByPage', 'connector_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/connector/data', 'json', req, runtime)
        )

    async def pull_data_by_page_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.PullDataByPageRequest,
        headers: dingtalkconnector__1__0_models.PullDataByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.PullDataByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.data_model_id):
            query['dataModelId'] = request.data_model_id
        if not UtilClient.is_unset(request.datetime_filter_field):
            query['datetimeFilterField'] = request.datetime_filter_field
        if not UtilClient.is_unset(request.max_datetime):
            query['maxDatetime'] = request.max_datetime
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_datetime):
            query['minDatetime'] = request.min_datetime
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
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
            dingtalkconnector__1__0_models.PullDataByPageResponse(),
            await self.do_roarequest_async('PullDataByPage', 'connector_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/connector/data', 'json', req, runtime)
        )

    def pull_data_by_pk(
        self,
        data_model_id: str,
        request: dingtalkconnector__1__0_models.PullDataByPkRequest,
    ) -> dingtalkconnector__1__0_models.PullDataByPkResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.PullDataByPkHeaders()
        return self.pull_data_by_pk_with_options(data_model_id, request, headers, runtime)

    async def pull_data_by_pk_async(
        self,
        data_model_id: str,
        request: dingtalkconnector__1__0_models.PullDataByPkRequest,
    ) -> dingtalkconnector__1__0_models.PullDataByPkResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.PullDataByPkHeaders()
        return await self.pull_data_by_pk_with_options_async(data_model_id, request, headers, runtime)

    def pull_data_by_pk_with_options(
        self,
        data_model_id: str,
        request: dingtalkconnector__1__0_models.PullDataByPkRequest,
        headers: dingtalkconnector__1__0_models.PullDataByPkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.PullDataByPkResponse:
        UtilClient.validate_model(request)
        data_model_id = OpenApiUtilClient.get_encode_param(data_model_id)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.primary_key):
            query['primaryKey'] = request.primary_key
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
            dingtalkconnector__1__0_models.PullDataByPkResponse(),
            self.do_roarequest('PullDataByPk', 'connector_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/connector/data/{data_model_id}', 'json', req, runtime)
        )

    async def pull_data_by_pk_with_options_async(
        self,
        data_model_id: str,
        request: dingtalkconnector__1__0_models.PullDataByPkRequest,
        headers: dingtalkconnector__1__0_models.PullDataByPkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.PullDataByPkResponse:
        UtilClient.validate_model(request)
        data_model_id = OpenApiUtilClient.get_encode_param(data_model_id)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.primary_key):
            query['primaryKey'] = request.primary_key
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
            dingtalkconnector__1__0_models.PullDataByPkResponse(),
            await self.do_roarequest_async('PullDataByPk', 'connector_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/connector/data/{data_model_id}', 'json', req, runtime)
        )

    def sync_data(
        self,
        request: dingtalkconnector__1__0_models.SyncDataRequest,
    ) -> dingtalkconnector__1__0_models.SyncDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.SyncDataHeaders()
        return self.sync_data_with_options(request, headers, runtime)

    async def sync_data_async(
        self,
        request: dingtalkconnector__1__0_models.SyncDataRequest,
    ) -> dingtalkconnector__1__0_models.SyncDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.SyncDataHeaders()
        return await self.sync_data_with_options_async(request, headers, runtime)

    def sync_data_with_options(
        self,
        request: dingtalkconnector__1__0_models.SyncDataRequest,
        headers: dingtalkconnector__1__0_models.SyncDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.SyncDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.trigger_data_list):
            body['triggerDataList'] = request.trigger_data_list
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
            dingtalkconnector__1__0_models.SyncDataResponse(),
            self.do_roarequest('SyncData', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/triggers/data/sync', 'json', req, runtime)
        )

    async def sync_data_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.SyncDataRequest,
        headers: dingtalkconnector__1__0_models.SyncDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.SyncDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.trigger_data_list):
            body['triggerDataList'] = request.trigger_data_list
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
            dingtalkconnector__1__0_models.SyncDataResponse(),
            await self.do_roarequest_async('SyncData', 'connector_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/connector/triggers/data/sync', 'json', req, runtime)
        )

    def update_action(
        self,
        request: dingtalkconnector__1__0_models.UpdateActionRequest,
    ) -> dingtalkconnector__1__0_models.UpdateActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateActionHeaders()
        return self.update_action_with_options(request, headers, runtime)

    async def update_action_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateActionRequest,
    ) -> dingtalkconnector__1__0_models.UpdateActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateActionHeaders()
        return await self.update_action_with_options_async(request, headers, runtime)

    def update_action_with_options(
        self,
        request: dingtalkconnector__1__0_models.UpdateActionRequest,
        headers: dingtalkconnector__1__0_models.UpdateActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_info):
            body['actionInfo'] = request.action_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.UpdateActionResponse(),
            self.do_roarequest('UpdateAction', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/actions', 'json', req, runtime)
        )

    async def update_action_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateActionRequest,
        headers: dingtalkconnector__1__0_models.UpdateActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_info):
            body['actionInfo'] = request.action_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.UpdateActionResponse(),
            await self.do_roarequest_async('UpdateAction', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/actions', 'json', req, runtime)
        )

    def update_connector(
        self,
        request: dingtalkconnector__1__0_models.UpdateConnectorRequest,
    ) -> dingtalkconnector__1__0_models.UpdateConnectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateConnectorHeaders()
        return self.update_connector_with_options(request, headers, runtime)

    async def update_connector_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateConnectorRequest,
    ) -> dingtalkconnector__1__0_models.UpdateConnectorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateConnectorHeaders()
        return await self.update_connector_with_options_async(request, headers, runtime)

    def update_connector_with_options(
        self,
        request: dingtalkconnector__1__0_models.UpdateConnectorRequest,
        headers: dingtalkconnector__1__0_models.UpdateConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateConnectorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connector_info):
            body['connectorInfo'] = request.connector_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.UpdateConnectorResponse(),
            self.do_roarequest('UpdateConnector', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/connectors', 'json', req, runtime)
        )

    async def update_connector_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateConnectorRequest,
        headers: dingtalkconnector__1__0_models.UpdateConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateConnectorResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connector_info):
            body['connectorInfo'] = request.connector_info
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
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
            dingtalkconnector__1__0_models.UpdateConnectorResponse(),
            await self.do_roarequest_async('UpdateConnector', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/connectors', 'json', req, runtime)
        )

    def update_trigger(
        self,
        request: dingtalkconnector__1__0_models.UpdateTriggerRequest,
    ) -> dingtalkconnector__1__0_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateTriggerHeaders()
        return self.update_trigger_with_options(request, headers, runtime)

    async def update_trigger_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateTriggerRequest,
    ) -> dingtalkconnector__1__0_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconnector__1__0_models.UpdateTriggerHeaders()
        return await self.update_trigger_with_options_async(request, headers, runtime)

    def update_trigger_with_options(
        self,
        request: dingtalkconnector__1__0_models.UpdateTriggerRequest,
        headers: dingtalkconnector__1__0_models.UpdateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
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
            dingtalkconnector__1__0_models.UpdateTriggerResponse(),
            self.do_roarequest('UpdateTrigger', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/triggers', 'json', req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        request: dingtalkconnector__1__0_models.UpdateTriggerRequest,
        headers: dingtalkconnector__1__0_models.UpdateTriggerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconnector__1__0_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integrator_flag):
            body['integratorFlag'] = request.integrator_flag
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
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
            dingtalkconnector__1__0_models.UpdateTriggerResponse(),
            await self.do_roarequest_async('UpdateTrigger', 'connector_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/connector/triggers', 'json', req, runtime)
        )
