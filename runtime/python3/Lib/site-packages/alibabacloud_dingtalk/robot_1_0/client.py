# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
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

    def batch_otoquery(
        self,
        request: dingtalkrobot__1__0_models.BatchOTOQueryRequest,
    ) -> dingtalkrobot__1__0_models.BatchOTOQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchOTOQueryHeaders()
        return self.batch_otoquery_with_options(request, headers, runtime)

    async def batch_otoquery_async(
        self,
        request: dingtalkrobot__1__0_models.BatchOTOQueryRequest,
    ) -> dingtalkrobot__1__0_models.BatchOTOQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchOTOQueryHeaders()
        return await self.batch_otoquery_with_options_async(request, headers, runtime)

    def batch_otoquery_with_options(
        self,
        request: dingtalkrobot__1__0_models.BatchOTOQueryRequest,
        headers: dingtalkrobot__1__0_models.BatchOTOQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchOTOQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.process_query_key):
            query['processQueryKey'] = request.process_query_key
        if not UtilClient.is_unset(request.robot_code):
            query['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.BatchOTOQueryResponse(),
            self.do_roarequest('BatchOTOQuery', 'robot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/robot/oToMessages/readStatus', 'json', req, runtime)
        )

    async def batch_otoquery_with_options_async(
        self,
        request: dingtalkrobot__1__0_models.BatchOTOQueryRequest,
        headers: dingtalkrobot__1__0_models.BatchOTOQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchOTOQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.process_query_key):
            query['processQueryKey'] = request.process_query_key
        if not UtilClient.is_unset(request.robot_code):
            query['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.BatchOTOQueryResponse(),
            await self.do_roarequest_async('BatchOTOQuery', 'robot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/robot/oToMessages/readStatus', 'json', req, runtime)
        )

    def batch_recall_group(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallGroupRequest,
    ) -> dingtalkrobot__1__0_models.BatchRecallGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchRecallGroupHeaders()
        return self.batch_recall_group_with_options(request, headers, runtime)

    async def batch_recall_group_async(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallGroupRequest,
    ) -> dingtalkrobot__1__0_models.BatchRecallGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchRecallGroupHeaders()
        return await self.batch_recall_group_with_options_async(request, headers, runtime)

    def batch_recall_group_with_options(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallGroupRequest,
        headers: dingtalkrobot__1__0_models.BatchRecallGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchRecallGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.process_query_keys):
            body['processQueryKeys'] = request.process_query_keys
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
            dingtalkrobot__1__0_models.BatchRecallGroupResponse(),
            self.do_roarequest('BatchRecallGroup', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/groupMessages/batchRecall', 'json', req, runtime)
        )

    async def batch_recall_group_with_options_async(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallGroupRequest,
        headers: dingtalkrobot__1__0_models.BatchRecallGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchRecallGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chatbot_id):
            body['chatbotId'] = request.chatbot_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.process_query_keys):
            body['processQueryKeys'] = request.process_query_keys
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
            dingtalkrobot__1__0_models.BatchRecallGroupResponse(),
            await self.do_roarequest_async('BatchRecallGroup', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/groupMessages/batchRecall', 'json', req, runtime)
        )

    def batch_recall_oto(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallOTORequest,
    ) -> dingtalkrobot__1__0_models.BatchRecallOTOResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchRecallOTOHeaders()
        return self.batch_recall_otowith_options(request, headers, runtime)

    async def batch_recall_oto_async(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallOTORequest,
    ) -> dingtalkrobot__1__0_models.BatchRecallOTOResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchRecallOTOHeaders()
        return await self.batch_recall_otowith_options_async(request, headers, runtime)

    def batch_recall_otowith_options(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallOTORequest,
        headers: dingtalkrobot__1__0_models.BatchRecallOTOHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchRecallOTOResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.process_query_keys):
            body['processQueryKeys'] = request.process_query_keys
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.BatchRecallOTOResponse(),
            self.do_roarequest('BatchRecallOTO', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/otoMessages/batchRecall', 'json', req, runtime)
        )

    async def batch_recall_otowith_options_async(
        self,
        request: dingtalkrobot__1__0_models.BatchRecallOTORequest,
        headers: dingtalkrobot__1__0_models.BatchRecallOTOHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchRecallOTOResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.process_query_keys):
            body['processQueryKeys'] = request.process_query_keys
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.BatchRecallOTOResponse(),
            await self.do_roarequest_async('BatchRecallOTO', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/otoMessages/batchRecall', 'json', req, runtime)
        )

    def batch_send_oto(
        self,
        request: dingtalkrobot__1__0_models.BatchSendOTORequest,
    ) -> dingtalkrobot__1__0_models.BatchSendOTOResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        return self.batch_send_otowith_options(request, headers, runtime)

    async def batch_send_oto_async(
        self,
        request: dingtalkrobot__1__0_models.BatchSendOTORequest,
    ) -> dingtalkrobot__1__0_models.BatchSendOTOResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        return await self.batch_send_otowith_options_async(request, headers, runtime)

    def batch_send_otowith_options(
        self,
        request: dingtalkrobot__1__0_models.BatchSendOTORequest,
        headers: dingtalkrobot__1__0_models.BatchSendOTOHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchSendOTOResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
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
            dingtalkrobot__1__0_models.BatchSendOTOResponse(),
            self.do_roarequest('BatchSendOTO', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/oToMessages/batchSend', 'json', req, runtime)
        )

    async def batch_send_otowith_options_async(
        self,
        request: dingtalkrobot__1__0_models.BatchSendOTORequest,
        headers: dingtalkrobot__1__0_models.BatchSendOTOHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.BatchSendOTOResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
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
            dingtalkrobot__1__0_models.BatchSendOTOResponse(),
            await self.do_roarequest_async('BatchSendOTO', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/oToMessages/batchSend', 'json', req, runtime)
        )

    def org_group_send(
        self,
        request: dingtalkrobot__1__0_models.OrgGroupSendRequest,
    ) -> dingtalkrobot__1__0_models.OrgGroupSendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        return self.org_group_send_with_options(request, headers, runtime)

    async def org_group_send_async(
        self,
        request: dingtalkrobot__1__0_models.OrgGroupSendRequest,
    ) -> dingtalkrobot__1__0_models.OrgGroupSendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        return await self.org_group_send_with_options_async(request, headers, runtime)

    def org_group_send_with_options(
        self,
        request: dingtalkrobot__1__0_models.OrgGroupSendRequest,
        headers: dingtalkrobot__1__0_models.OrgGroupSendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.OrgGroupSendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
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
            dingtalkrobot__1__0_models.OrgGroupSendResponse(),
            self.do_roarequest('OrgGroupSend', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/groupMessages/send', 'json', req, runtime)
        )

    async def org_group_send_with_options_async(
        self,
        request: dingtalkrobot__1__0_models.OrgGroupSendRequest,
        headers: dingtalkrobot__1__0_models.OrgGroupSendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.OrgGroupSendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.msg_key):
            body['msgKey'] = request.msg_key
        if not UtilClient.is_unset(request.msg_param):
            body['msgParam'] = request.msg_param
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
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
            dingtalkrobot__1__0_models.OrgGroupSendResponse(),
            await self.do_roarequest_async('OrgGroupSend', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/groupMessages/send', 'json', req, runtime)
        )

    def query_robot_dingtalk_id(
        self,
        request: dingtalkrobot__1__0_models.QueryRobotDingtalkIdRequest,
    ) -> dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.QueryRobotDingtalkIdHeaders()
        return self.query_robot_dingtalk_id_with_options(request, headers, runtime)

    async def query_robot_dingtalk_id_async(
        self,
        request: dingtalkrobot__1__0_models.QueryRobotDingtalkIdRequest,
    ) -> dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.QueryRobotDingtalkIdHeaders()
        return await self.query_robot_dingtalk_id_with_options_async(request, headers, runtime)

    def query_robot_dingtalk_id_with_options(
        self,
        request: dingtalkrobot__1__0_models.QueryRobotDingtalkIdRequest,
        headers: dingtalkrobot__1__0_models.QueryRobotDingtalkIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_code):
            query['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse(),
            self.do_roarequest('QueryRobotDingtalkId', 'robot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/robot/dingtalkId', 'json', req, runtime)
        )

    async def query_robot_dingtalk_id_with_options_async(
        self,
        request: dingtalkrobot__1__0_models.QueryRobotDingtalkIdRequest,
        headers: dingtalkrobot__1__0_models.QueryRobotDingtalkIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_code):
            query['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.QueryRobotDingtalkIdResponse(),
            await self.do_roarequest_async('QueryRobotDingtalkId', 'robot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/robot/dingtalkId', 'json', req, runtime)
        )

    def send_robot_ding_message(
        self,
        request: dingtalkrobot__1__0_models.SendRobotDingMessageRequest,
    ) -> dingtalkrobot__1__0_models.SendRobotDingMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.SendRobotDingMessageHeaders()
        return self.send_robot_ding_message_with_options(request, headers, runtime)

    async def send_robot_ding_message_async(
        self,
        request: dingtalkrobot__1__0_models.SendRobotDingMessageRequest,
    ) -> dingtalkrobot__1__0_models.SendRobotDingMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkrobot__1__0_models.SendRobotDingMessageHeaders()
        return await self.send_robot_ding_message_with_options_async(request, headers, runtime)

    def send_robot_ding_message_with_options(
        self,
        request: dingtalkrobot__1__0_models.SendRobotDingMessageRequest,
        headers: dingtalkrobot__1__0_models.SendRobotDingMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.SendRobotDingMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_params):
            body['contentParams'] = request.content_params
        if not UtilClient.is_unset(request.ding_template_id):
            body['dingTemplateId'] = request.ding_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.SendRobotDingMessageResponse(),
            self.do_roarequest('SendRobotDingMessage', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/dingMessages/send', 'json', req, runtime)
        )

    async def send_robot_ding_message_with_options_async(
        self,
        request: dingtalkrobot__1__0_models.SendRobotDingMessageRequest,
        headers: dingtalkrobot__1__0_models.SendRobotDingMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkrobot__1__0_models.SendRobotDingMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_params):
            body['contentParams'] = request.content_params
        if not UtilClient.is_unset(request.ding_template_id):
            body['dingTemplateId'] = request.ding_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
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
            dingtalkrobot__1__0_models.SendRobotDingMessageResponse(),
            await self.do_roarequest_async('SendRobotDingMessage', 'robot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/robot/dingMessages/send', 'json', req, runtime)
        )
