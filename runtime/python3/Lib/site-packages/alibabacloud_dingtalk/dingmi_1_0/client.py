# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.dingmi_1_0 import models as dingtalkdingmi__1__0_models
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

    def add_robot_instance_to_group(
        self,
        request: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupRequest,
    ) -> dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.AddRobotInstanceToGroupHeaders()
        return self.add_robot_instance_to_group_with_options(request, headers, runtime)

    async def add_robot_instance_to_group_async(
        self,
        request: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupRequest,
    ) -> dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.AddRobotInstanceToGroupHeaders()
        return await self.add_robot_instance_to_group_with_options_async(request, headers, runtime)

    def add_robot_instance_to_group_with_options(
        self,
        request: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupRequest,
        headers: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse(),
            self.do_roarequest('AddRobotInstanceToGroup', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/groups', 'json', req, runtime)
        )

    async def add_robot_instance_to_group_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupRequest,
        headers: dingtalkdingmi__1__0_models.AddRobotInstanceToGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkdingmi__1__0_models.AddRobotInstanceToGroupResponse(),
            await self.do_roarequest_async('AddRobotInstanceToGroup', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/groups', 'json', req, runtime)
        )

    def ask_robot(
        self,
        request: dingtalkdingmi__1__0_models.AskRobotRequest,
    ) -> dingtalkdingmi__1__0_models.AskRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.AskRobotHeaders()
        return self.ask_robot_with_options(request, headers, runtime)

    async def ask_robot_async(
        self,
        request: dingtalkdingmi__1__0_models.AskRobotRequest,
    ) -> dingtalkdingmi__1__0_models.AskRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.AskRobotHeaders()
        return await self.ask_robot_with_options_async(request, headers, runtime)

    def ask_robot_with_options(
        self,
        request: dingtalkdingmi__1__0_models.AskRobotRequest,
        headers: dingtalkdingmi__1__0_models.AskRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.AskRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ding_user_id):
            body['dingUserId'] = request.ding_user_id
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.robot_app_key):
            body['robotAppKey'] = request.robot_app_key
        if not UtilClient.is_unset(request.session_uuid):
            body['sessionUuid'] = request.session_uuid
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
            dingtalkdingmi__1__0_models.AskRobotResponse(),
            self.do_roarequest('AskRobot', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/ask', 'json', req, runtime)
        )

    async def ask_robot_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.AskRobotRequest,
        headers: dingtalkdingmi__1__0_models.AskRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.AskRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ding_user_id):
            body['dingUserId'] = request.ding_user_id
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.robot_app_key):
            body['robotAppKey'] = request.robot_app_key
        if not UtilClient.is_unset(request.session_uuid):
            body['sessionUuid'] = request.session_uuid
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
            dingtalkdingmi__1__0_models.AskRobotResponse(),
            await self.do_roarequest_async('AskRobot', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/ask', 'json', req, runtime)
        )

    def get_ding_me_base_data(
        self,
        request: dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest,
    ) -> dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders()
        return self.get_ding_me_base_data_with_options(request, headers, runtime)

    async def get_ding_me_base_data_async(
        self,
        request: dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest,
    ) -> dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders()
        return await self.get_ding_me_base_data_with_options_async(request, headers, runtime)

    def get_ding_me_base_data_with_options(
        self,
        request: dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest,
        headers: dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.by_day):
            query['byDay'] = request.by_day
        if not UtilClient.is_unset(request.end_day):
            query['endDay'] = request.end_day
        if not UtilClient.is_unset(request.start_day):
            query['startDay'] = request.start_day
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
            dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse(),
            self.do_roarequest('GetDingMeBaseData', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/robots/data', 'json', req, runtime)
        )

    async def get_ding_me_base_data_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest,
        headers: dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.by_day):
            query['byDay'] = request.by_day
        if not UtilClient.is_unset(request.end_day):
            query['endDay'] = request.end_day
        if not UtilClient.is_unset(request.start_day):
            query['startDay'] = request.start_day
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
            dingtalkdingmi__1__0_models.GetDingMeBaseDataResponse(),
            await self.do_roarequest_async('GetDingMeBaseData', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/robots/data', 'json', req, runtime)
        )

    def get_intelligent_robot_info(
        self,
        request: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetIntelligentRobotInfoHeaders()
        return self.get_intelligent_robot_info_with_options(request, headers, runtime)

    async def get_intelligent_robot_info_async(
        self,
        request: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetIntelligentRobotInfoHeaders()
        return await self.get_intelligent_robot_info_with_options_async(request, headers, runtime)

    def get_intelligent_robot_info_with_options(
        self,
        request: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_app_key):
            query['robotAppKey'] = request.robot_app_key
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
            dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse(),
            self.do_roarequest('GetIntelligentRobotInfo', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/intelligentRobots/infos', 'json', req, runtime)
        )

    async def get_intelligent_robot_info_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.GetIntelligentRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_app_key):
            query['robotAppKey'] = request.robot_app_key
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
            dingtalkdingmi__1__0_models.GetIntelligentRobotInfoResponse(),
            await self.do_roarequest_async('GetIntelligentRobotInfo', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/intelligentRobots/infos', 'json', req, runtime)
        )

    def get_official_account_robot_info(
        self,
        request: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoHeaders()
        return self.get_official_account_robot_info_with_options(request, headers, runtime)

    async def get_official_account_robot_info_async(
        self,
        request: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoHeaders()
        return await self.get_official_account_robot_info_with_options_async(request, headers, runtime)

    def get_official_account_robot_info_with_options(
        self,
        request: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
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
            dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse(),
            self.do_roarequest('GetOfficialAccountRobotInfo', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/officialAccounts/robots', 'json', req, runtime)
        )

    async def get_official_account_robot_info_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
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
            dingtalkdingmi__1__0_models.GetOfficialAccountRobotInfoResponse(),
            await self.do_roarequest_async('GetOfficialAccountRobotInfo', 'dingmi_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/dingmi/officialAccounts/robots', 'json', req, runtime)
        )

    def get_web_channel_user_token(
        self,
        request: dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest,
    ) -> dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders()
        return self.get_web_channel_user_token_with_options(request, headers, runtime)

    async def get_web_channel_user_token_async(
        self,
        request: dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest,
    ) -> dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders()
        return await self.get_web_channel_user_token_with_options_async(request, headers, runtime)

    def get_web_channel_user_token_with_options(
        self,
        request: dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest,
        headers: dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.nick):
            body['nick'] = request.nick
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
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
            dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse(),
            self.do_roarequest('GetWebChannelUserToken', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/webChannels/userTokens', 'json', req, runtime)
        )

    async def get_web_channel_user_token_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest,
        headers: dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.foreign_id):
            body['foreignId'] = request.foreign_id
        if not UtilClient.is_unset(request.nick):
            body['nick'] = request.nick
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
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
            dingtalkdingmi__1__0_models.GetWebChannelUserTokenResponse(),
            await self.do_roarequest_async('GetWebChannelUserToken', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/webChannels/userTokens', 'json', req, runtime)
        )

    def push_customer_group_message(
        self,
        request: dingtalkdingmi__1__0_models.PushCustomerGroupMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushCustomerGroupMessageHeaders()
        return self.push_customer_group_message_with_options(request, headers, runtime)

    async def push_customer_group_message_async(
        self,
        request: dingtalkdingmi__1__0_models.PushCustomerGroupMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushCustomerGroupMessageHeaders()
        return await self.push_customer_group_message_with_options_async(request, headers, runtime)

    def push_customer_group_message_with_options(
        self,
        request: dingtalkdingmi__1__0_models.PushCustomerGroupMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushCustomerGroupMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
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
            dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse(),
            self.do_roarequest('PushCustomerGroupMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/officialAccounts/robots/groupMessages/send', 'json', req, runtime)
        )

    async def push_customer_group_message_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.PushCustomerGroupMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushCustomerGroupMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
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
            dingtalkdingmi__1__0_models.PushCustomerGroupMessageResponse(),
            await self.do_roarequest_async('PushCustomerGroupMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/officialAccounts/robots/groupMessages/send', 'json', req, runtime)
        )

    def push_intelligent_robot_group_message(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageHeaders()
        return self.push_intelligent_robot_group_message_with_options(request, headers, runtime)

    async def push_intelligent_robot_group_message_async(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageHeaders()
        return await self.push_intelligent_robot_group_message_with_options_async(request, headers, runtime)

    def push_intelligent_robot_group_message_with_options(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse(),
            self.do_roarequest('PushIntelligentRobotGroupMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/groupMessages/send', 'json', req, runtime)
        )

    async def push_intelligent_robot_group_message_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkdingmi__1__0_models.PushIntelligentRobotGroupMessageResponse(),
            await self.do_roarequest_async('PushIntelligentRobotGroupMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/groupMessages/send', 'json', req, runtime)
        )

    def push_intelligent_robot_message(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushIntelligentRobotMessageHeaders()
        return self.push_intelligent_robot_message_with_options(request, headers, runtime)

    async def push_intelligent_robot_message_async(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushIntelligentRobotMessageHeaders()
        return await self.push_intelligent_robot_message_with_options_async(request, headers, runtime)

    def push_intelligent_robot_message_with_options(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse(),
            self.do_roarequest('PushIntelligentRobotMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/oToMessages/send', 'json', req, runtime)
        )

    async def push_intelligent_robot_message_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushIntelligentRobotMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushIntelligentRobotMessageResponse(),
            await self.do_roarequest_async('PushIntelligentRobotMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/intelligentRobots/oToMessages/send', 'json', req, runtime)
        )

    def push_official_account_message(
        self,
        request: dingtalkdingmi__1__0_models.PushOfficialAccountMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushOfficialAccountMessageHeaders()
        return self.push_official_account_message_with_options(request, headers, runtime)

    async def push_official_account_message_async(
        self,
        request: dingtalkdingmi__1__0_models.PushOfficialAccountMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushOfficialAccountMessageHeaders()
        return await self.push_official_account_message_with_options_async(request, headers, runtime)

    def push_official_account_message_with_options(
        self,
        request: dingtalkdingmi__1__0_models.PushOfficialAccountMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushOfficialAccountMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse(),
            self.do_roarequest('PushOfficialAccountMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/officialAccounts/robots/oToMessages/send', 'json', req, runtime)
        )

    async def push_official_account_message_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.PushOfficialAccountMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushOfficialAccountMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushOfficialAccountMessageResponse(),
            await self.do_roarequest_async('PushOfficialAccountMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/officialAccounts/robots/oToMessages/send', 'json', req, runtime)
        )

    def push_robot_message(
        self,
        request: dingtalkdingmi__1__0_models.PushRobotMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushRobotMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushRobotMessageHeaders()
        return self.push_robot_message_with_options(request, headers, runtime)

    async def push_robot_message_async(
        self,
        request: dingtalkdingmi__1__0_models.PushRobotMessageRequest,
    ) -> dingtalkdingmi__1__0_models.PushRobotMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.PushRobotMessageHeaders()
        return await self.push_robot_message_with_options_async(request, headers, runtime)

    def push_robot_message_with_options(
        self,
        request: dingtalkdingmi__1__0_models.PushRobotMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushRobotMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushRobotMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushRobotMessageResponse(),
            self.do_roarequest('PushRobotMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/oToMessages/send', 'json', req, runtime)
        )

    async def push_robot_message_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.PushRobotMessageRequest,
        headers: dingtalkdingmi__1__0_models.PushRobotMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.PushRobotMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkdingmi__1__0_models.PushRobotMessageResponse(),
            await self.do_roarequest_async('PushRobotMessage', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/oToMessages/send', 'json', req, runtime)
        )

    def reply_robot(
        self,
        request: dingtalkdingmi__1__0_models.ReplyRobotRequest,
    ) -> dingtalkdingmi__1__0_models.ReplyRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.ReplyRobotHeaders()
        return self.reply_robot_with_options(request, headers, runtime)

    async def reply_robot_async(
        self,
        request: dingtalkdingmi__1__0_models.ReplyRobotRequest,
    ) -> dingtalkdingmi__1__0_models.ReplyRobotResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.ReplyRobotHeaders()
        return await self.reply_robot_with_options_async(request, headers, runtime)

    def reply_robot_with_options(
        self,
        request: dingtalkdingmi__1__0_models.ReplyRobotRequest,
        headers: dingtalkdingmi__1__0_models.ReplyRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.ReplyRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.proxy_message_str):
            body['proxyMessageStr'] = request.proxy_message_str
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
            dingtalkdingmi__1__0_models.ReplyRobotResponse(),
            self.do_roarequest('ReplyRobot', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/reply', 'json', req, runtime)
        )

    async def reply_robot_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.ReplyRobotRequest,
        headers: dingtalkdingmi__1__0_models.ReplyRobotHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.ReplyRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.proxy_message_str):
            body['proxyMessageStr'] = request.proxy_message_str
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
            dingtalkdingmi__1__0_models.ReplyRobotResponse(),
            await self.do_roarequest_async('ReplyRobot', 'dingmi_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/dingmi/robots/reply', 'json', req, runtime)
        )

    def update_official_account_robot_info(
        self,
        request: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoHeaders()
        return self.update_official_account_robot_info_with_options(request, headers, runtime)

    async def update_official_account_robot_info_async(
        self,
        request: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoRequest,
    ) -> dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoHeaders()
        return await self.update_official_account_robot_info_with_options_async(request, headers, runtime)

    def update_official_account_robot_info_with_options(
        self,
        request: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.brief):
            body['brief'] = request.brief
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.preview_media_url):
            body['previewMediaUrl'] = request.preview_media_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse(),
            self.do_roarequest('UpdateOfficialAccountRobotInfo', 'dingmi_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/dingmi/officialAccounts/robots', 'json', req, runtime)
        )

    async def update_official_account_robot_info_with_options_async(
        self,
        request: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoRequest,
        headers: dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.brief):
            body['brief'] = request.brief
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.preview_media_url):
            body['previewMediaUrl'] = request.preview_media_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdingmi__1__0_models.UpdateOfficialAccountRobotInfoResponse(),
            await self.do_roarequest_async('UpdateOfficialAccountRobotInfo', 'dingmi_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/dingmi/officialAccounts/robots', 'json', req, runtime)
        )
