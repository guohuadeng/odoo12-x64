# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.customer_service_1_0 import models as dingtalkcustomer_service__1__0_models
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

    def create_ticket(
        self,
        request: dingtalkcustomer_service__1__0_models.CreateTicketRequest,
    ) -> dingtalkcustomer_service__1__0_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.CreateTicketHeaders()
        return self.create_ticket_with_options(request, headers, runtime)

    async def create_ticket_async(
        self,
        request: dingtalkcustomer_service__1__0_models.CreateTicketRequest,
    ) -> dingtalkcustomer_service__1__0_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.CreateTicketHeaders()
        return await self.create_ticket_with_options_async(request, headers, runtime)

    def create_ticket_with_options(
        self,
        request: dingtalkcustomer_service__1__0_models.CreateTicketRequest,
        headers: dingtalkcustomer_service__1__0_models.CreateTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.foreign_name):
            body['foreignName'] = request.foreign_name
        if not UtilClient.is_unset(request.open_instance_id):
            body['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            body['productionType'] = request.production_type
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
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
            dingtalkcustomer_service__1__0_models.CreateTicketResponse(),
            self.do_roarequest('CreateTicket', 'customerService_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/customerService/tickets', 'json', req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: dingtalkcustomer_service__1__0_models.CreateTicketRequest,
        headers: dingtalkcustomer_service__1__0_models.CreateTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.foreign_name):
            body['foreignName'] = request.foreign_name
        if not UtilClient.is_unset(request.open_instance_id):
            body['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            body['productionType'] = request.production_type
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
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
            dingtalkcustomer_service__1__0_models.CreateTicketResponse(),
            await self.do_roarequest_async('CreateTicket', 'customerService_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/customerService/tickets', 'json', req, runtime)
        )

    def execute_activity(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.ExecuteActivityRequest,
    ) -> dingtalkcustomer_service__1__0_models.ExecuteActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.ExecuteActivityHeaders()
        return self.execute_activity_with_options(ticket_id, request, headers, runtime)

    async def execute_activity_async(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.ExecuteActivityRequest,
    ) -> dingtalkcustomer_service__1__0_models.ExecuteActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.ExecuteActivityHeaders()
        return await self.execute_activity_with_options_async(ticket_id, request, headers, runtime)

    def execute_activity_with_options(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.ExecuteActivityRequest,
        headers: dingtalkcustomer_service__1__0_models.ExecuteActivityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.ExecuteActivityResponse:
        UtilClient.validate_model(request)
        ticket_id = OpenApiUtilClient.get_encode_param(ticket_id)
        body = {}
        if not UtilClient.is_unset(request.activity_code):
            body['activityCode'] = request.activity_code
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.foreign_name):
            body['foreignName'] = request.foreign_name
        if not UtilClient.is_unset(request.open_instance_id):
            body['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            body['productionType'] = request.production_type
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
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
            dingtalkcustomer_service__1__0_models.ExecuteActivityResponse(),
            self.do_roarequest('ExecuteActivity', 'customerService_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/customerService/tickets/{ticket_id}', 'json', req, runtime)
        )

    async def execute_activity_with_options_async(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.ExecuteActivityRequest,
        headers: dingtalkcustomer_service__1__0_models.ExecuteActivityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.ExecuteActivityResponse:
        UtilClient.validate_model(request)
        ticket_id = OpenApiUtilClient.get_encode_param(ticket_id)
        body = {}
        if not UtilClient.is_unset(request.activity_code):
            body['activityCode'] = request.activity_code
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.foreign_name):
            body['foreignName'] = request.foreign_name
        if not UtilClient.is_unset(request.open_instance_id):
            body['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            body['productionType'] = request.production_type
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
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
            dingtalkcustomer_service__1__0_models.ExecuteActivityResponse(),
            await self.do_roarequest_async('ExecuteActivity', 'customerService_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/customerService/tickets/{ticket_id}', 'json', req, runtime)
        )

    def get_user_source_list(
        self,
        request: dingtalkcustomer_service__1__0_models.GetUserSourceListRequest,
    ) -> dingtalkcustomer_service__1__0_models.GetUserSourceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.GetUserSourceListHeaders()
        return self.get_user_source_list_with_options(request, headers, runtime)

    async def get_user_source_list_async(
        self,
        request: dingtalkcustomer_service__1__0_models.GetUserSourceListRequest,
    ) -> dingtalkcustomer_service__1__0_models.GetUserSourceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.GetUserSourceListHeaders()
        return await self.get_user_source_list_with_options_async(request, headers, runtime)

    def get_user_source_list_with_options(
        self,
        request: dingtalkcustomer_service__1__0_models.GetUserSourceListRequest,
        headers: dingtalkcustomer_service__1__0_models.GetUserSourceListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.GetUserSourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.org_id):
            query['orgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            query['orgName'] = request.org_name
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.GetUserSourceListResponse(),
            self.do_roarequest('GetUserSourceList', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/customers/sources', 'json', req, runtime)
        )

    async def get_user_source_list_with_options_async(
        self,
        request: dingtalkcustomer_service__1__0_models.GetUserSourceListRequest,
        headers: dingtalkcustomer_service__1__0_models.GetUserSourceListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.GetUserSourceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.org_id):
            query['orgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            query['orgName'] = request.org_name
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.GetUserSourceListResponse(),
            await self.do_roarequest_async('GetUserSourceList', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/customers/sources', 'json', req, runtime)
        )

    def page_list_action(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.PageListActionRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListActionHeaders()
        return self.page_list_action_with_options(ticket_id, request, headers, runtime)

    async def page_list_action_async(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.PageListActionRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListActionHeaders()
        return await self.page_list_action_with_options_async(ticket_id, request, headers, runtime)

    def page_list_action_with_options(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.PageListActionRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListActionResponse:
        UtilClient.validate_model(request)
        ticket_id = OpenApiUtilClient.get_encode_param(ticket_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.PageListActionResponse(),
            self.do_roarequest('PageListAction', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/tickets/{ticket_id}/actions', 'json', req, runtime)
        )

    async def page_list_action_with_options_async(
        self,
        ticket_id: str,
        request: dingtalkcustomer_service__1__0_models.PageListActionRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListActionResponse:
        UtilClient.validate_model(request)
        ticket_id = OpenApiUtilClient.get_encode_param(ticket_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.PageListActionResponse(),
            await self.do_roarequest_async('PageListAction', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/tickets/{ticket_id}/actions', 'json', req, runtime)
        )

    def page_list_robot(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListRobotRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListRobotHeaders()
        return self.page_list_robot_with_options(request, headers, runtime)

    async def page_list_robot_async(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListRobotRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListRobotHeaders()
        return await self.page_list_robot_with_options_async(request, headers, runtime)

    def page_list_robot_with_options(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListRobotRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListRobotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.PageListRobotResponse(),
            self.do_roarequest('PageListRobot', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/robots', 'json', req, runtime)
        )

    async def page_list_robot_with_options_async(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListRobotRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListRobotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
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
            dingtalkcustomer_service__1__0_models.PageListRobotResponse(),
            await self.do_roarequest_async('PageListRobot', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/robots', 'json', req, runtime)
        )

    def page_list_ticket(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListTicketRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListTicketHeaders()
        return self.page_list_ticket_with_options(request, headers, runtime)

    async def page_list_ticket_async(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListTicketRequest,
    ) -> dingtalkcustomer_service__1__0_models.PageListTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcustomer_service__1__0_models.PageListTicketHeaders()
        return await self.page_list_ticket_with_options_async(request, headers, runtime)

    def page_list_ticket_with_options(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListTicketRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.foreign_id):
            query['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
        if not UtilClient.is_unset(request.source_id):
            query['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.ticket_id):
            query['ticketId'] = request.ticket_id
        if not UtilClient.is_unset(request.ticket_status):
            query['ticketStatus'] = request.ticket_status
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
            dingtalkcustomer_service__1__0_models.PageListTicketResponse(),
            self.do_roarequest('PageListTicket', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/tickets', 'json', req, runtime)
        )

    async def page_list_ticket_with_options_async(
        self,
        request: dingtalkcustomer_service__1__0_models.PageListTicketRequest,
        headers: dingtalkcustomer_service__1__0_models.PageListTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcustomer_service__1__0_models.PageListTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.foreign_id):
            query['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.open_instance_id):
            query['openInstanceId'] = request.open_instance_id
        if not UtilClient.is_unset(request.production_type):
            query['productionType'] = request.production_type
        if not UtilClient.is_unset(request.source_id):
            query['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.ticket_id):
            query['ticketId'] = request.ticket_id
        if not UtilClient.is_unset(request.ticket_status):
            query['ticketStatus'] = request.ticket_status
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
            dingtalkcustomer_service__1__0_models.PageListTicketResponse(),
            await self.do_roarequest_async('PageListTicket', 'customerService_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/customerService/tickets', 'json', req, runtime)
        )
