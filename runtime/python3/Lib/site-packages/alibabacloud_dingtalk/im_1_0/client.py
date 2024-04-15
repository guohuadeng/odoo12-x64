# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
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

    def batch_query_group_member(
        self,
        request: dingtalkim__1__0_models.BatchQueryGroupMemberRequest,
    ) -> dingtalkim__1__0_models.BatchQueryGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.BatchQueryGroupMemberHeaders()
        return self.batch_query_group_member_with_options(request, headers, runtime)

    async def batch_query_group_member_async(
        self,
        request: dingtalkim__1__0_models.BatchQueryGroupMemberRequest,
    ) -> dingtalkim__1__0_models.BatchQueryGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.BatchQueryGroupMemberHeaders()
        return await self.batch_query_group_member_with_options_async(request, headers, runtime)

    def batch_query_group_member_with_options(
        self,
        request: dingtalkim__1__0_models.BatchQueryGroupMemberRequest,
        headers: dingtalkim__1__0_models.BatchQueryGroupMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.BatchQueryGroupMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
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
            dingtalkim__1__0_models.BatchQueryGroupMemberResponse(),
            self.do_roarequest('BatchQueryGroupMember', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/members/batchQuery', 'json', req, runtime)
        )

    async def batch_query_group_member_with_options_async(
        self,
        request: dingtalkim__1__0_models.BatchQueryGroupMemberRequest,
        headers: dingtalkim__1__0_models.BatchQueryGroupMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.BatchQueryGroupMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
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
            dingtalkim__1__0_models.BatchQueryGroupMemberResponse(),
            await self.do_roarequest_async('BatchQueryGroupMember', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/members/batchQuery', 'json', req, runtime)
        )

    def card_template_build_action(
        self,
        request: dingtalkim__1__0_models.CardTemplateBuildActionRequest,
    ) -> dingtalkim__1__0_models.CardTemplateBuildActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.CardTemplateBuildActionHeaders()
        return self.card_template_build_action_with_options(request, headers, runtime)

    async def card_template_build_action_async(
        self,
        request: dingtalkim__1__0_models.CardTemplateBuildActionRequest,
    ) -> dingtalkim__1__0_models.CardTemplateBuildActionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.CardTemplateBuildActionHeaders()
        return await self.card_template_build_action_with_options_async(request, headers, runtime)

    def card_template_build_action_with_options(
        self,
        request: dingtalkim__1__0_models.CardTemplateBuildActionRequest,
        headers: dingtalkim__1__0_models.CardTemplateBuildActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.CardTemplateBuildActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.card_template_json):
            body['cardTemplateJson'] = request.card_template_json
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
            dingtalkim__1__0_models.CardTemplateBuildActionResponse(),
            self.do_roarequest('CardTemplateBuildAction', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/templates/buildAction', 'json', req, runtime)
        )

    async def card_template_build_action_with_options_async(
        self,
        request: dingtalkim__1__0_models.CardTemplateBuildActionRequest,
        headers: dingtalkim__1__0_models.CardTemplateBuildActionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.CardTemplateBuildActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.card_template_json):
            body['cardTemplateJson'] = request.card_template_json
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
            dingtalkim__1__0_models.CardTemplateBuildActionResponse(),
            await self.do_roarequest_async('CardTemplateBuildAction', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/templates/buildAction', 'json', req, runtime)
        )

    def chat_id_to_open_conversation_id(
        self,
        chat_id: str,
    ) -> dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders()
        return self.chat_id_to_open_conversation_id_with_options(chat_id, headers, runtime)

    async def chat_id_to_open_conversation_id_async(
        self,
        chat_id: str,
    ) -> dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders()
        return await self.chat_id_to_open_conversation_id_with_options_async(chat_id, headers, runtime)

    def chat_id_to_open_conversation_id_with_options(
        self,
        chat_id: str,
        headers: dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse:
        chat_id = OpenApiUtilClient.get_encode_param(chat_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse(),
            self.do_roarequest('ChatIdToOpenConversationId', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/chat/{chat_id}/convertToOpenConversationId', 'json', req, runtime)
        )

    async def chat_id_to_open_conversation_id_with_options_async(
        self,
        chat_id: str,
        headers: dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse:
        chat_id = OpenApiUtilClient.get_encode_param(chat_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkim__1__0_models.ChatIdToOpenConversationIdResponse(),
            await self.do_roarequest_async('ChatIdToOpenConversationId', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/chat/{chat_id}/convertToOpenConversationId', 'json', req, runtime)
        )

    def get_interconnection_url(
        self,
        request: dingtalkim__1__0_models.GetInterconnectionUrlRequest,
    ) -> dingtalkim__1__0_models.GetInterconnectionUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetInterconnectionUrlHeaders()
        return self.get_interconnection_url_with_options(request, headers, runtime)

    async def get_interconnection_url_async(
        self,
        request: dingtalkim__1__0_models.GetInterconnectionUrlRequest,
    ) -> dingtalkim__1__0_models.GetInterconnectionUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetInterconnectionUrlHeaders()
        return await self.get_interconnection_url_with_options_async(request, headers, runtime)

    def get_interconnection_url_with_options(
        self,
        request: dingtalkim__1__0_models.GetInterconnectionUrlRequest,
        headers: dingtalkim__1__0_models.GetInterconnectionUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetInterconnectionUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_user_avatar):
            body['appUserAvatar'] = request.app_user_avatar
        if not UtilClient.is_unset(request.app_user_avatar_type):
            body['appUserAvatarType'] = request.app_user_avatar_type
        if not UtilClient.is_unset(request.app_user_id):
            body['appUserId'] = request.app_user_id
        if not UtilClient.is_unset(request.app_user_mobile_number):
            body['appUserMobileNumber'] = request.app_user_mobile_number
        if not UtilClient.is_unset(request.app_user_name):
            body['appUserName'] = request.app_user_name
        if not UtilClient.is_unset(request.msg_page_type):
            body['msgPageType'] = request.msg_page_type
        if not UtilClient.is_unset(request.qr_code):
            body['qrCode'] = request.qr_code
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.source_code):
            body['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
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
            dingtalkim__1__0_models.GetInterconnectionUrlResponse(),
            self.do_roarequest('GetInterconnectionUrl', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interconnections/sessions/urls', 'json', req, runtime)
        )

    async def get_interconnection_url_with_options_async(
        self,
        request: dingtalkim__1__0_models.GetInterconnectionUrlRequest,
        headers: dingtalkim__1__0_models.GetInterconnectionUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetInterconnectionUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_user_avatar):
            body['appUserAvatar'] = request.app_user_avatar
        if not UtilClient.is_unset(request.app_user_avatar_type):
            body['appUserAvatarType'] = request.app_user_avatar_type
        if not UtilClient.is_unset(request.app_user_id):
            body['appUserId'] = request.app_user_id
        if not UtilClient.is_unset(request.app_user_mobile_number):
            body['appUserMobileNumber'] = request.app_user_mobile_number
        if not UtilClient.is_unset(request.app_user_name):
            body['appUserName'] = request.app_user_name
        if not UtilClient.is_unset(request.msg_page_type):
            body['msgPageType'] = request.msg_page_type
        if not UtilClient.is_unset(request.qr_code):
            body['qrCode'] = request.qr_code
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.source_code):
            body['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
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
            dingtalkim__1__0_models.GetInterconnectionUrlResponse(),
            await self.do_roarequest_async('GetInterconnectionUrl', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interconnections/sessions/urls', 'json', req, runtime)
        )

    def get_scene_group_info(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupInfoRequest,
    ) -> dingtalkim__1__0_models.GetSceneGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetSceneGroupInfoHeaders()
        return self.get_scene_group_info_with_options(request, headers, runtime)

    async def get_scene_group_info_async(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupInfoRequest,
    ) -> dingtalkim__1__0_models.GetSceneGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetSceneGroupInfoHeaders()
        return await self.get_scene_group_info_with_options_async(request, headers, runtime)

    def get_scene_group_info_with_options(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupInfoRequest,
        headers: dingtalkim__1__0_models.GetSceneGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetSceneGroupInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
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
            dingtalkim__1__0_models.GetSceneGroupInfoResponse(),
            self.do_roarequest('GetSceneGroupInfo', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/query', 'json', req, runtime)
        )

    async def get_scene_group_info_with_options_async(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupInfoRequest,
        headers: dingtalkim__1__0_models.GetSceneGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetSceneGroupInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
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
            dingtalkim__1__0_models.GetSceneGroupInfoResponse(),
            await self.do_roarequest_async('GetSceneGroupInfo', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/query', 'json', req, runtime)
        )

    def get_scene_group_members(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupMembersRequest,
    ) -> dingtalkim__1__0_models.GetSceneGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetSceneGroupMembersHeaders()
        return self.get_scene_group_members_with_options(request, headers, runtime)

    async def get_scene_group_members_async(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupMembersRequest,
    ) -> dingtalkim__1__0_models.GetSceneGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.GetSceneGroupMembersHeaders()
        return await self.get_scene_group_members_with_options_async(request, headers, runtime)

    def get_scene_group_members_with_options(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupMembersRequest,
        headers: dingtalkim__1__0_models.GetSceneGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetSceneGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
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
            dingtalkim__1__0_models.GetSceneGroupMembersResponse(),
            self.do_roarequest('GetSceneGroupMembers', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/members/query', 'json', req, runtime)
        )

    async def get_scene_group_members_with_options_async(
        self,
        request: dingtalkim__1__0_models.GetSceneGroupMembersRequest,
        headers: dingtalkim__1__0_models.GetSceneGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.GetSceneGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
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
            dingtalkim__1__0_models.GetSceneGroupMembersResponse(),
            await self.do_roarequest_async('GetSceneGroupMembers', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/members/query', 'json', req, runtime)
        )

    def interactive_card_create_instance(
        self,
        request: dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest,
    ) -> dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders()
        return self.interactive_card_create_instance_with_options(request, headers, runtime)

    async def interactive_card_create_instance_async(
        self,
        request: dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest,
    ) -> dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders()
        return await self.interactive_card_create_instance_with_options_async(request, headers, runtime)

    def interactive_card_create_instance_with_options(
        self,
        request: dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest,
        headers: dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_route_key):
            body['callbackRouteKey'] = request.callback_route_key
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.chat_bot_id):
            body['chatBotId'] = request.chat_bot_id
        if not UtilClient.is_unset(request.conversation_type):
            body['conversationType'] = request.conversation_type
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse(),
            self.do_roarequest('InteractiveCardCreateInstance', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/instances', 'json', req, runtime)
        )

    async def interactive_card_create_instance_with_options_async(
        self,
        request: dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest,
        headers: dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_route_key):
            body['callbackRouteKey'] = request.callback_route_key
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.chat_bot_id):
            body['chatBotId'] = request.chat_bot_id
        if not UtilClient.is_unset(request.conversation_type):
            body['conversationType'] = request.conversation_type
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.InteractiveCardCreateInstanceResponse(),
            await self.do_roarequest_async('InteractiveCardCreateInstance', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/instances', 'json', req, runtime)
        )

    def query_group_mute_status(
        self,
        request: dingtalkim__1__0_models.QueryGroupMuteStatusRequest,
    ) -> dingtalkim__1__0_models.QueryGroupMuteStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.QueryGroupMuteStatusHeaders()
        return self.query_group_mute_status_with_options(request, headers, runtime)

    async def query_group_mute_status_async(
        self,
        request: dingtalkim__1__0_models.QueryGroupMuteStatusRequest,
    ) -> dingtalkim__1__0_models.QueryGroupMuteStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.QueryGroupMuteStatusHeaders()
        return await self.query_group_mute_status_with_options_async(request, headers, runtime)

    def query_group_mute_status_with_options(
        self,
        request: dingtalkim__1__0_models.QueryGroupMuteStatusRequest,
        headers: dingtalkim__1__0_models.QueryGroupMuteStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.QueryGroupMuteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            query['openConversationId'] = request.open_conversation_id
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
            dingtalkim__1__0_models.QueryGroupMuteStatusResponse(),
            self.do_roarequest('QueryGroupMuteStatus', 'im_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/im/sceneGroups/muteSettings', 'json', req, runtime)
        )

    async def query_group_mute_status_with_options_async(
        self,
        request: dingtalkim__1__0_models.QueryGroupMuteStatusRequest,
        headers: dingtalkim__1__0_models.QueryGroupMuteStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.QueryGroupMuteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            query['openConversationId'] = request.open_conversation_id
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
            dingtalkim__1__0_models.QueryGroupMuteStatusResponse(),
            await self.do_roarequest_async('QueryGroupMuteStatus', 'im_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/im/sceneGroups/muteSettings', 'json', req, runtime)
        )

    def query_members_of_group_role(
        self,
        request: dingtalkim__1__0_models.QueryMembersOfGroupRoleRequest,
    ) -> dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.QueryMembersOfGroupRoleHeaders()
        return self.query_members_of_group_role_with_options(request, headers, runtime)

    async def query_members_of_group_role_async(
        self,
        request: dingtalkim__1__0_models.QueryMembersOfGroupRoleRequest,
    ) -> dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.QueryMembersOfGroupRoleHeaders()
        return await self.query_members_of_group_role_with_options_async(request, headers, runtime)

    def query_members_of_group_role_with_options(
        self,
        request: dingtalkim__1__0_models.QueryMembersOfGroupRoleRequest,
        headers: dingtalkim__1__0_models.QueryMembersOfGroupRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.open_role_id):
            body['openRoleId'] = request.open_role_id
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse(),
            self.do_roarequest('QueryMembersOfGroupRole', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/roles/members/query', 'json', req, runtime)
        )

    async def query_members_of_group_role_with_options_async(
        self,
        request: dingtalkim__1__0_models.QueryMembersOfGroupRoleRequest,
        headers: dingtalkim__1__0_models.QueryMembersOfGroupRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.open_role_id):
            body['openRoleId'] = request.open_role_id
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkim__1__0_models.QueryMembersOfGroupRoleResponse(),
            await self.do_roarequest_async('QueryMembersOfGroupRole', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/roles/members/query', 'json', req, runtime)
        )

    def send_interactive_card(
        self,
        request: dingtalkim__1__0_models.SendInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendInteractiveCardHeaders()
        return self.send_interactive_card_with_options(request, headers, runtime)

    async def send_interactive_card_async(
        self,
        request: dingtalkim__1__0_models.SendInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendInteractiveCardHeaders()
        return await self.send_interactive_card_with_options_async(request, headers, runtime)

    def send_interactive_card_with_options(
        self,
        request: dingtalkim__1__0_models.SendInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.at_open_ids):
            body['atOpenIds'] = request.at_open_ids
        if not UtilClient.is_unset(request.callback_route_key):
            body['callbackRouteKey'] = request.callback_route_key
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_options):
            body['cardOptions'] = request.card_options
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.chat_bot_id):
            body['chatBotId'] = request.chat_bot_id
        if not UtilClient.is_unset(request.conversation_type):
            body['conversationType'] = request.conversation_type
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.SendInteractiveCardResponse(),
            self.do_roarequest('SendInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/send', 'json', req, runtime)
        )

    async def send_interactive_card_with_options_async(
        self,
        request: dingtalkim__1__0_models.SendInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.at_open_ids):
            body['atOpenIds'] = request.at_open_ids
        if not UtilClient.is_unset(request.callback_route_key):
            body['callbackRouteKey'] = request.callback_route_key
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_options):
            body['cardOptions'] = request.card_options
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.chat_bot_id):
            body['chatBotId'] = request.chat_bot_id
        if not UtilClient.is_unset(request.conversation_type):
            body['conversationType'] = request.conversation_type
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.SendInteractiveCardResponse(),
            await self.do_roarequest_async('SendInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/send', 'json', req, runtime)
        )

    def send_robot_interactive_card(
        self,
        request: dingtalkim__1__0_models.SendRobotInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendRobotInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendRobotInteractiveCardHeaders()
        return self.send_robot_interactive_card_with_options(request, headers, runtime)

    async def send_robot_interactive_card_async(
        self,
        request: dingtalkim__1__0_models.SendRobotInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendRobotInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendRobotInteractiveCardHeaders()
        return await self.send_robot_interactive_card_with_options_async(request, headers, runtime)

    def send_robot_interactive_card_with_options(
        self,
        request: dingtalkim__1__0_models.SendRobotInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendRobotInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendRobotInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_biz_id):
            body['cardBizId'] = request.card_biz_id
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.send_options):
            body['sendOptions'] = request.send_options
        if not UtilClient.is_unset(request.single_chat_receiver):
            body['singleChatReceiver'] = request.single_chat_receiver
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
            dingtalkim__1__0_models.SendRobotInteractiveCardResponse(),
            self.do_roarequest('SendRobotInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/v1.0/robot/interactiveCards/send', 'json', req, runtime)
        )

    async def send_robot_interactive_card_with_options_async(
        self,
        request: dingtalkim__1__0_models.SendRobotInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendRobotInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendRobotInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_biz_id):
            body['cardBizId'] = request.card_biz_id
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.send_options):
            body['sendOptions'] = request.send_options
        if not UtilClient.is_unset(request.single_chat_receiver):
            body['singleChatReceiver'] = request.single_chat_receiver
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
            dingtalkim__1__0_models.SendRobotInteractiveCardResponse(),
            await self.do_roarequest_async('SendRobotInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/v1.0/robot/interactiveCards/send', 'json', req, runtime)
        )

    def send_template_interactive_card(
        self,
        request: dingtalkim__1__0_models.SendTemplateInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendTemplateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders()
        return self.send_template_interactive_card_with_options(request, headers, runtime)

    async def send_template_interactive_card_async(
        self,
        request: dingtalkim__1__0_models.SendTemplateInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.SendTemplateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders()
        return await self.send_template_interactive_card_with_options_async(request, headers, runtime)

    def send_template_interactive_card_with_options(
        self,
        request: dingtalkim__1__0_models.SendTemplateInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendTemplateInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['callbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.send_options):
            body['sendOptions'] = request.send_options
        if not UtilClient.is_unset(request.single_chat_receiver):
            body['singleChatReceiver'] = request.single_chat_receiver
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
            dingtalkim__1__0_models.SendTemplateInteractiveCardResponse(),
            self.do_roarequest('SendTemplateInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/templates/send', 'json', req, runtime)
        )

    async def send_template_interactive_card_with_options_async(
        self,
        request: dingtalkim__1__0_models.SendTemplateInteractiveCardRequest,
        headers: dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.SendTemplateInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['callbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_template_id):
            body['cardTemplateId'] = request.card_template_id
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.robot_code):
            body['robotCode'] = request.robot_code
        if not UtilClient.is_unset(request.send_options):
            body['sendOptions'] = request.send_options
        if not UtilClient.is_unset(request.single_chat_receiver):
            body['singleChatReceiver'] = request.single_chat_receiver
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
            dingtalkim__1__0_models.SendTemplateInteractiveCardResponse(),
            await self.do_roarequest_async('SendTemplateInteractiveCard', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/interactiveCards/templates/send', 'json', req, runtime)
        )

    def topbox_close(
        self,
        request: dingtalkim__1__0_models.TopboxCloseRequest,
    ) -> dingtalkim__1__0_models.TopboxCloseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.TopboxCloseHeaders()
        return self.topbox_close_with_options(request, headers, runtime)

    async def topbox_close_async(
        self,
        request: dingtalkim__1__0_models.TopboxCloseRequest,
    ) -> dingtalkim__1__0_models.TopboxCloseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.TopboxCloseHeaders()
        return await self.topbox_close_with_options_async(request, headers, runtime)

    def topbox_close_with_options(
        self,
        request: dingtalkim__1__0_models.TopboxCloseRequest,
        headers: dingtalkim__1__0_models.TopboxCloseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.TopboxCloseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
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
            dingtalkim__1__0_models.TopboxCloseResponse(),
            self.do_roarequest('TopboxClose', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/topBoxes/close', 'none', req, runtime)
        )

    async def topbox_close_with_options_async(
        self,
        request: dingtalkim__1__0_models.TopboxCloseRequest,
        headers: dingtalkim__1__0_models.TopboxCloseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.TopboxCloseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
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
            dingtalkim__1__0_models.TopboxCloseResponse(),
            await self.do_roarequest_async('TopboxClose', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/topBoxes/close', 'none', req, runtime)
        )

    def topbox_open(
        self,
        request: dingtalkim__1__0_models.TopboxOpenRequest,
    ) -> dingtalkim__1__0_models.TopboxOpenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.TopboxOpenHeaders()
        return self.topbox_open_with_options(request, headers, runtime)

    async def topbox_open_async(
        self,
        request: dingtalkim__1__0_models.TopboxOpenRequest,
    ) -> dingtalkim__1__0_models.TopboxOpenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.TopboxOpenHeaders()
        return await self.topbox_open_with_options_async(request, headers, runtime)

    def topbox_open_with_options(
        self,
        request: dingtalkim__1__0_models.TopboxOpenRequest,
        headers: dingtalkim__1__0_models.TopboxOpenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.TopboxOpenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.expired_time):
            body['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.platforms):
            body['platforms'] = request.platforms
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
            dingtalkim__1__0_models.TopboxOpenResponse(),
            self.do_roarequest('TopboxOpen', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/topBoxes/open', 'none', req, runtime)
        )

    async def topbox_open_with_options_async(
        self,
        request: dingtalkim__1__0_models.TopboxOpenRequest,
        headers: dingtalkim__1__0_models.TopboxOpenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.TopboxOpenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_app_code):
            body['coolAppCode'] = request.cool_app_code
        if not UtilClient.is_unset(request.expired_time):
            body['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.platforms):
            body['platforms'] = request.platforms
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
            dingtalkim__1__0_models.TopboxOpenResponse(),
            await self.do_roarequest_async('TopboxOpen', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/topBoxes/open', 'none', req, runtime)
        )

    def update_group_permission(
        self,
        request: dingtalkim__1__0_models.UpdateGroupPermissionRequest,
    ) -> dingtalkim__1__0_models.UpdateGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateGroupPermissionHeaders()
        return self.update_group_permission_with_options(request, headers, runtime)

    async def update_group_permission_async(
        self,
        request: dingtalkim__1__0_models.UpdateGroupPermissionRequest,
    ) -> dingtalkim__1__0_models.UpdateGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateGroupPermissionHeaders()
        return await self.update_group_permission_with_options_async(request, headers, runtime)

    def update_group_permission_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateGroupPermissionRequest,
        headers: dingtalkim__1__0_models.UpdateGroupPermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateGroupPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.permission_group):
            body['permissionGroup'] = request.permission_group
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
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
            dingtalkim__1__0_models.UpdateGroupPermissionResponse(),
            self.do_roarequest('UpdateGroupPermission', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/permissions', 'json', req, runtime)
        )

    async def update_group_permission_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateGroupPermissionRequest,
        headers: dingtalkim__1__0_models.UpdateGroupPermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateGroupPermissionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.permission_group):
            body['permissionGroup'] = request.permission_group
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
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
            dingtalkim__1__0_models.UpdateGroupPermissionResponse(),
            await self.do_roarequest_async('UpdateGroupPermission', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/permissions', 'json', req, runtime)
        )

    def update_group_sub_admin(
        self,
        request: dingtalkim__1__0_models.UpdateGroupSubAdminRequest,
    ) -> dingtalkim__1__0_models.UpdateGroupSubAdminResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateGroupSubAdminHeaders()
        return self.update_group_sub_admin_with_options(request, headers, runtime)

    async def update_group_sub_admin_async(
        self,
        request: dingtalkim__1__0_models.UpdateGroupSubAdminRequest,
    ) -> dingtalkim__1__0_models.UpdateGroupSubAdminResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateGroupSubAdminHeaders()
        return await self.update_group_sub_admin_with_options_async(request, headers, runtime)

    def update_group_sub_admin_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateGroupSubAdminRequest,
        headers: dingtalkim__1__0_models.UpdateGroupSubAdminHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateGroupSubAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
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
            dingtalkim__1__0_models.UpdateGroupSubAdminResponse(),
            self.do_roarequest('UpdateGroupSubAdmin', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/subAdmins', 'json', req, runtime)
        )

    async def update_group_sub_admin_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateGroupSubAdminRequest,
        headers: dingtalkim__1__0_models.UpdateGroupSubAdminHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateGroupSubAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
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
            dingtalkim__1__0_models.UpdateGroupSubAdminResponse(),
            await self.do_roarequest_async('UpdateGroupSubAdmin', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/subAdmins', 'json', req, runtime)
        )

    def update_interactive_card(
        self,
        request: dingtalkim__1__0_models.UpdateInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.UpdateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateInteractiveCardHeaders()
        return self.update_interactive_card_with_options(request, headers, runtime)

    async def update_interactive_card_async(
        self,
        request: dingtalkim__1__0_models.UpdateInteractiveCardRequest,
    ) -> dingtalkim__1__0_models.UpdateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateInteractiveCardHeaders()
        return await self.update_interactive_card_with_options_async(request, headers, runtime)

    def update_interactive_card_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateInteractiveCardRequest,
        headers: dingtalkim__1__0_models.UpdateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_options):
            body['cardOptions'] = request.card_options
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.UpdateInteractiveCardResponse(),
            self.do_roarequest('UpdateInteractiveCard', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/interactiveCards', 'json', req, runtime)
        )

    async def update_interactive_card_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateInteractiveCardRequest,
        headers: dingtalkim__1__0_models.UpdateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateInteractiveCardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_data):
            body['cardData'] = request.card_data
        if not UtilClient.is_unset(request.card_options):
            body['cardOptions'] = request.card_options
        if not UtilClient.is_unset(request.out_track_id):
            body['outTrackId'] = request.out_track_id
        if not UtilClient.is_unset(request.private_data):
            body['privateData'] = request.private_data
        if not UtilClient.is_unset(request.user_id_type):
            body['userIdType'] = request.user_id_type
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
            dingtalkim__1__0_models.UpdateInteractiveCardResponse(),
            await self.do_roarequest_async('UpdateInteractiveCard', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/interactiveCards', 'json', req, runtime)
        )

    def update_member_ban_words(
        self,
        request: dingtalkim__1__0_models.UpdateMemberBanWordsRequest,
    ) -> dingtalkim__1__0_models.UpdateMemberBanWordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateMemberBanWordsHeaders()
        return self.update_member_ban_words_with_options(request, headers, runtime)

    async def update_member_ban_words_async(
        self,
        request: dingtalkim__1__0_models.UpdateMemberBanWordsRequest,
    ) -> dingtalkim__1__0_models.UpdateMemberBanWordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateMemberBanWordsHeaders()
        return await self.update_member_ban_words_with_options_async(request, headers, runtime)

    def update_member_ban_words_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateMemberBanWordsRequest,
        headers: dingtalkim__1__0_models.UpdateMemberBanWordsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateMemberBanWordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mute_duration):
            body['muteDuration'] = request.mute_duration
        if not UtilClient.is_unset(request.mute_status):
            body['muteStatus'] = request.mute_status
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkim__1__0_models.UpdateMemberBanWordsResponse(),
            self.do_roarequest('UpdateMemberBanWords', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/muteMembers/set', 'none', req, runtime)
        )

    async def update_member_ban_words_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateMemberBanWordsRequest,
        headers: dingtalkim__1__0_models.UpdateMemberBanWordsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateMemberBanWordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mute_duration):
            body['muteDuration'] = request.mute_duration
        if not UtilClient.is_unset(request.mute_status):
            body['muteStatus'] = request.mute_status
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkim__1__0_models.UpdateMemberBanWordsResponse(),
            await self.do_roarequest_async('UpdateMemberBanWords', 'im_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/im/sceneGroups/muteMembers/set', 'none', req, runtime)
        )

    def update_member_group_nick(
        self,
        request: dingtalkim__1__0_models.UpdateMemberGroupNickRequest,
    ) -> dingtalkim__1__0_models.UpdateMemberGroupNickResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateMemberGroupNickHeaders()
        return self.update_member_group_nick_with_options(request, headers, runtime)

    async def update_member_group_nick_async(
        self,
        request: dingtalkim__1__0_models.UpdateMemberGroupNickRequest,
    ) -> dingtalkim__1__0_models.UpdateMemberGroupNickResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateMemberGroupNickHeaders()
        return await self.update_member_group_nick_with_options_async(request, headers, runtime)

    def update_member_group_nick_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateMemberGroupNickRequest,
        headers: dingtalkim__1__0_models.UpdateMemberGroupNickHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateMemberGroupNickResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_nick):
            body['groupNick'] = request.group_nick
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkim__1__0_models.UpdateMemberGroupNickResponse(),
            self.do_roarequest('UpdateMemberGroupNick', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/members/groupNicks', 'json', req, runtime)
        )

    async def update_member_group_nick_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateMemberGroupNickRequest,
        headers: dingtalkim__1__0_models.UpdateMemberGroupNickHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateMemberGroupNickResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_nick):
            body['groupNick'] = request.group_nick
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
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
            dingtalkim__1__0_models.UpdateMemberGroupNickResponse(),
            await self.do_roarequest_async('UpdateMemberGroupNick', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/members/groupNicks', 'json', req, runtime)
        )

    def update_the_group_roles_of_group_member(
        self,
        request: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberRequest,
    ) -> dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberHeaders()
        return self.update_the_group_roles_of_group_member_with_options(request, headers, runtime)

    async def update_the_group_roles_of_group_member_async(
        self,
        request: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberRequest,
    ) -> dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberHeaders()
        return await self.update_the_group_roles_of_group_member_with_options_async(request, headers, runtime)

    def update_the_group_roles_of_group_member_with_options(
        self,
        request: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberRequest,
        headers: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.open_role_ids):
            body['openRoleIds'] = request.open_role_ids
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
            dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse(),
            self.do_roarequest('UpdateTheGroupRolesOfGroupMember', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/members/groupRoles', 'json', req, runtime)
        )

    async def update_the_group_roles_of_group_member_with_options_async(
        self,
        request: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberRequest,
        headers: dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['openConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.open_role_ids):
            body['openRoleIds'] = request.open_role_ids
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
            dingtalkim__1__0_models.UpdateTheGroupRolesOfGroupMemberResponse(),
            await self.do_roarequest_async('UpdateTheGroupRolesOfGroupMember', 'im_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/im/sceneGroups/members/groupRoles', 'json', req, runtime)
        )
