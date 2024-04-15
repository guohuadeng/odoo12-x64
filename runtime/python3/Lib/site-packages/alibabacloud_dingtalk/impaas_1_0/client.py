# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.impaas_1_0 import models as dingtalkimpaas__1__0_models
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

    def add_group_members(
        self,
        request: dingtalkimpaas__1__0_models.AddGroupMembersRequest,
    ) -> dingtalkimpaas__1__0_models.AddGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.AddGroupMembersHeaders()
        return self.add_group_members_with_options(request, headers, runtime)

    async def add_group_members_async(
        self,
        request: dingtalkimpaas__1__0_models.AddGroupMembersRequest,
    ) -> dingtalkimpaas__1__0_models.AddGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.AddGroupMembersHeaders()
        return await self.add_group_members_with_options_async(request, headers, runtime)

    def add_group_members_with_options(
        self,
        request: dingtalkimpaas__1__0_models.AddGroupMembersRequest,
        headers: dingtalkimpaas__1__0_models.AddGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.AddGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.AddGroupMembersResponse(),
            self.do_roarequest('AddGroupMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/members/batchAdd', 'json', req, runtime)
        )

    async def add_group_members_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.AddGroupMembersRequest,
        headers: dingtalkimpaas__1__0_models.AddGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.AddGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.AddGroupMembersResponse(),
            await self.do_roarequest_async('AddGroupMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/members/batchAdd', 'json', req, runtime)
        )

    def add_profile(
        self,
        request: dingtalkimpaas__1__0_models.AddProfileRequest,
    ) -> dingtalkimpaas__1__0_models.AddProfileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.AddProfileHeaders()
        return self.add_profile_with_options(request, headers, runtime)

    async def add_profile_async(
        self,
        request: dingtalkimpaas__1__0_models.AddProfileRequest,
    ) -> dingtalkimpaas__1__0_models.AddProfileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.AddProfileHeaders()
        return await self.add_profile_with_options_async(request, headers, runtime)

    def add_profile_with_options(
        self,
        request: dingtalkimpaas__1__0_models.AddProfileRequest,
        headers: dingtalkimpaas__1__0_models.AddProfileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.AddProfileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uid):
            body['appUid'] = request.app_uid
        if not UtilClient.is_unset(request.avatar_media_id):
            body['avatarMediaId'] = request.avatar_media_id
        if not UtilClient.is_unset(request.mobile_number):
            body['mobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.nick):
            body['nick'] = request.nick
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
            dingtalkimpaas__1__0_models.AddProfileResponse(),
            self.do_roarequest('AddProfile', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/users/profiles', 'none', req, runtime)
        )

    async def add_profile_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.AddProfileRequest,
        headers: dingtalkimpaas__1__0_models.AddProfileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.AddProfileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uid):
            body['appUid'] = request.app_uid
        if not UtilClient.is_unset(request.avatar_media_id):
            body['avatarMediaId'] = request.avatar_media_id
        if not UtilClient.is_unset(request.mobile_number):
            body['mobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.nick):
            body['nick'] = request.nick
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
            dingtalkimpaas__1__0_models.AddProfileResponse(),
            await self.do_roarequest_async('AddProfile', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/users/profiles', 'none', req, runtime)
        )

    def batch_send(
        self,
        request: dingtalkimpaas__1__0_models.BatchSendRequest,
    ) -> dingtalkimpaas__1__0_models.BatchSendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.BatchSendHeaders()
        return self.batch_send_with_options(request, headers, runtime)

    async def batch_send_async(
        self,
        request: dingtalkimpaas__1__0_models.BatchSendRequest,
    ) -> dingtalkimpaas__1__0_models.BatchSendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.BatchSendHeaders()
        return await self.batch_send_with_options_async(request, headers, runtime)

    def batch_send_with_options(
        self,
        request: dingtalkimpaas__1__0_models.BatchSendRequest,
        headers: dingtalkimpaas__1__0_models.BatchSendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.BatchSendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uids):
            body['appUids'] = request.app_uids
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.conversation_ids):
            body['conversationIds'] = request.conversation_ids
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
            dingtalkimpaas__1__0_models.BatchSendResponse(),
            self.do_roarequest('BatchSend', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/batchSend', 'json', req, runtime)
        )

    async def batch_send_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.BatchSendRequest,
        headers: dingtalkimpaas__1__0_models.BatchSendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.BatchSendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uids):
            body['appUids'] = request.app_uids
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.conversation_ids):
            body['conversationIds'] = request.conversation_ids
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
            dingtalkimpaas__1__0_models.BatchSendResponse(),
            await self.do_roarequest_async('BatchSend', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/batchSend', 'json', req, runtime)
        )

    def create_group(
        self,
        request: dingtalkimpaas__1__0_models.CreateGroupRequest,
    ) -> dingtalkimpaas__1__0_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.CreateGroupHeaders()
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: dingtalkimpaas__1__0_models.CreateGroupRequest,
    ) -> dingtalkimpaas__1__0_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.CreateGroupHeaders()
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: dingtalkimpaas__1__0_models.CreateGroupRequest,
        headers: dingtalkimpaas__1__0_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.creator_uid):
            body['creatorUid'] = request.creator_uid
        if not UtilClient.is_unset(request.icon_media_id):
            body['iconMediaId'] = request.icon_media_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.CreateGroupResponse(),
            self.do_roarequest('CreateGroup', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.CreateGroupRequest,
        headers: dingtalkimpaas__1__0_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.creator_uid):
            body['creatorUid'] = request.creator_uid
        if not UtilClient.is_unset(request.icon_media_id):
            body['iconMediaId'] = request.icon_media_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.CreateGroupResponse(),
            await self.do_roarequest_async('CreateGroup', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups', 'json', req, runtime)
        )

    def dismiss_group(
        self,
        request: dingtalkimpaas__1__0_models.DismissGroupRequest,
    ) -> dingtalkimpaas__1__0_models.DismissGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.DismissGroupHeaders()
        return self.dismiss_group_with_options(request, headers, runtime)

    async def dismiss_group_async(
        self,
        request: dingtalkimpaas__1__0_models.DismissGroupRequest,
    ) -> dingtalkimpaas__1__0_models.DismissGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.DismissGroupHeaders()
        return await self.dismiss_group_with_options_async(request, headers, runtime)

    def dismiss_group_with_options(
        self,
        request: dingtalkimpaas__1__0_models.DismissGroupRequest,
        headers: dingtalkimpaas__1__0_models.DismissGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.DismissGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.DismissGroupResponse(),
            self.do_roarequest('DismissGroup', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/dismiss', 'none', req, runtime)
        )

    async def dismiss_group_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.DismissGroupRequest,
        headers: dingtalkimpaas__1__0_models.DismissGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.DismissGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.DismissGroupResponse(),
            await self.do_roarequest_async('DismissGroup', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/dismiss', 'none', req, runtime)
        )

    def get_conversation_id(
        self,
        request: dingtalkimpaas__1__0_models.GetConversationIdRequest,
    ) -> dingtalkimpaas__1__0_models.GetConversationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.GetConversationIdHeaders()
        return self.get_conversation_id_with_options(request, headers, runtime)

    async def get_conversation_id_async(
        self,
        request: dingtalkimpaas__1__0_models.GetConversationIdRequest,
    ) -> dingtalkimpaas__1__0_models.GetConversationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.GetConversationIdHeaders()
        return await self.get_conversation_id_with_options_async(request, headers, runtime)

    def get_conversation_id_with_options(
        self,
        request: dingtalkimpaas__1__0_models.GetConversationIdRequest,
        headers: dingtalkimpaas__1__0_models.GetConversationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.GetConversationIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uid):
            body['appUid'] = request.app_uid
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
            dingtalkimpaas__1__0_models.GetConversationIdResponse(),
            self.do_roarequest('GetConversationId', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/conversations', 'json', req, runtime)
        )

    async def get_conversation_id_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.GetConversationIdRequest,
        headers: dingtalkimpaas__1__0_models.GetConversationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.GetConversationIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_uid):
            body['appUid'] = request.app_uid
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
            dingtalkimpaas__1__0_models.GetConversationIdResponse(),
            await self.do_roarequest_async('GetConversationId', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/conversations', 'json', req, runtime)
        )

    def get_media_url(
        self,
        request: dingtalkimpaas__1__0_models.GetMediaUrlRequest,
    ) -> dingtalkimpaas__1__0_models.GetMediaUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.GetMediaUrlHeaders()
        return self.get_media_url_with_options(request, headers, runtime)

    async def get_media_url_async(
        self,
        request: dingtalkimpaas__1__0_models.GetMediaUrlRequest,
    ) -> dingtalkimpaas__1__0_models.GetMediaUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.GetMediaUrlHeaders()
        return await self.get_media_url_with_options_async(request, headers, runtime)

    def get_media_url_with_options(
        self,
        request: dingtalkimpaas__1__0_models.GetMediaUrlRequest,
        headers: dingtalkimpaas__1__0_models.GetMediaUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.GetMediaUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.media_id):
            body['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.url_expire_time):
            body['urlExpireTime'] = request.url_expire_time
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
            dingtalkimpaas__1__0_models.GetMediaUrlResponse(),
            self.do_roarequest('GetMediaUrl', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/medium/urls', 'json', req, runtime)
        )

    async def get_media_url_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.GetMediaUrlRequest,
        headers: dingtalkimpaas__1__0_models.GetMediaUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.GetMediaUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.media_id):
            body['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.url_expire_time):
            body['urlExpireTime'] = request.url_expire_time
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
            dingtalkimpaas__1__0_models.GetMediaUrlResponse(),
            await self.do_roarequest_async('GetMediaUrl', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/medium/urls', 'json', req, runtime)
        )

    def list_group_staff_members(
        self,
        request: dingtalkimpaas__1__0_models.ListGroupStaffMembersRequest,
    ) -> dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.ListGroupStaffMembersHeaders()
        return self.list_group_staff_members_with_options(request, headers, runtime)

    async def list_group_staff_members_async(
        self,
        request: dingtalkimpaas__1__0_models.ListGroupStaffMembersRequest,
    ) -> dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.ListGroupStaffMembersHeaders()
        return await self.list_group_staff_members_with_options_async(request, headers, runtime)

    def list_group_staff_members_with_options(
        self,
        request: dingtalkimpaas__1__0_models.ListGroupStaffMembersRequest,
        headers: dingtalkimpaas__1__0_models.ListGroupStaffMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
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
            dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse(),
            self.do_roarequest('ListGroupStaffMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/staffMemers/query', 'json', req, runtime)
        )

    async def list_group_staff_members_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.ListGroupStaffMembersRequest,
        headers: dingtalkimpaas__1__0_models.ListGroupStaffMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
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
            dingtalkimpaas__1__0_models.ListGroupStaffMembersResponse(),
            await self.do_roarequest_async('ListGroupStaffMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/staffMemers/query', 'json', req, runtime)
        )

    def query_batch_send_result(
        self,
        request: dingtalkimpaas__1__0_models.QueryBatchSendResultRequest,
    ) -> dingtalkimpaas__1__0_models.QueryBatchSendResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.QueryBatchSendResultHeaders()
        return self.query_batch_send_result_with_options(request, headers, runtime)

    async def query_batch_send_result_async(
        self,
        request: dingtalkimpaas__1__0_models.QueryBatchSendResultRequest,
    ) -> dingtalkimpaas__1__0_models.QueryBatchSendResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.QueryBatchSendResultHeaders()
        return await self.query_batch_send_result_with_options_async(request, headers, runtime)

    def query_batch_send_result_with_options(
        self,
        request: dingtalkimpaas__1__0_models.QueryBatchSendResultRequest,
        headers: dingtalkimpaas__1__0_models.QueryBatchSendResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.QueryBatchSendResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sender_user_id):
            query['senderUserId'] = request.sender_user_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
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
            dingtalkimpaas__1__0_models.QueryBatchSendResultResponse(),
            self.do_roarequest('QueryBatchSendResult', 'impaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/impaas/interconnections/messages/batchSendResults', 'json', req, runtime)
        )

    async def query_batch_send_result_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.QueryBatchSendResultRequest,
        headers: dingtalkimpaas__1__0_models.QueryBatchSendResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.QueryBatchSendResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sender_user_id):
            query['senderUserId'] = request.sender_user_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
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
            dingtalkimpaas__1__0_models.QueryBatchSendResultResponse(),
            await self.do_roarequest_async('QueryBatchSendResult', 'impaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/impaas/interconnections/messages/batchSendResults', 'json', req, runtime)
        )

    def read_message(
        self,
        request: dingtalkimpaas__1__0_models.ReadMessageRequest,
    ) -> dingtalkimpaas__1__0_models.ReadMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.ReadMessageHeaders()
        return self.read_message_with_options(request, headers, runtime)

    async def read_message_async(
        self,
        request: dingtalkimpaas__1__0_models.ReadMessageRequest,
    ) -> dingtalkimpaas__1__0_models.ReadMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.ReadMessageHeaders()
        return await self.read_message_with_options_async(request, headers, runtime)

    def read_message_with_options(
        self,
        request: dingtalkimpaas__1__0_models.ReadMessageRequest,
        headers: dingtalkimpaas__1__0_models.ReadMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.ReadMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_id):
            body['messageId'] = request.message_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.ReadMessageResponse(),
            self.do_roarequest('ReadMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/read', 'none', req, runtime)
        )

    async def read_message_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.ReadMessageRequest,
        headers: dingtalkimpaas__1__0_models.ReadMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.ReadMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_id):
            body['messageId'] = request.message_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.ReadMessageResponse(),
            await self.do_roarequest_async('ReadMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/read', 'none', req, runtime)
        )

    def recall_message(
        self,
        request: dingtalkimpaas__1__0_models.RecallMessageRequest,
    ) -> dingtalkimpaas__1__0_models.RecallMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.RecallMessageHeaders()
        return self.recall_message_with_options(request, headers, runtime)

    async def recall_message_async(
        self,
        request: dingtalkimpaas__1__0_models.RecallMessageRequest,
    ) -> dingtalkimpaas__1__0_models.RecallMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.RecallMessageHeaders()
        return await self.recall_message_with_options_async(request, headers, runtime)

    def recall_message_with_options(
        self,
        request: dingtalkimpaas__1__0_models.RecallMessageRequest,
        headers: dingtalkimpaas__1__0_models.RecallMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.RecallMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_id):
            body['messageId'] = request.message_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.RecallMessageResponse(),
            self.do_roarequest('RecallMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/recall', 'none', req, runtime)
        )

    async def recall_message_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.RecallMessageRequest,
        headers: dingtalkimpaas__1__0_models.RecallMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.RecallMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_id):
            body['messageId'] = request.message_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.RecallMessageResponse(),
            await self.do_roarequest_async('RecallMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/recall', 'none', req, runtime)
        )

    def remove_group_members(
        self,
        request: dingtalkimpaas__1__0_models.RemoveGroupMembersRequest,
    ) -> dingtalkimpaas__1__0_models.RemoveGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.RemoveGroupMembersHeaders()
        return self.remove_group_members_with_options(request, headers, runtime)

    async def remove_group_members_async(
        self,
        request: dingtalkimpaas__1__0_models.RemoveGroupMembersRequest,
    ) -> dingtalkimpaas__1__0_models.RemoveGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.RemoveGroupMembersHeaders()
        return await self.remove_group_members_with_options_async(request, headers, runtime)

    def remove_group_members_with_options(
        self,
        request: dingtalkimpaas__1__0_models.RemoveGroupMembersRequest,
        headers: dingtalkimpaas__1__0_models.RemoveGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.RemoveGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.member_uids):
            body['memberUids'] = request.member_uids
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.RemoveGroupMembersResponse(),
            self.do_roarequest('RemoveGroupMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/members/batchRemove', 'none', req, runtime)
        )

    async def remove_group_members_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.RemoveGroupMembersRequest,
        headers: dingtalkimpaas__1__0_models.RemoveGroupMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.RemoveGroupMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.member_uids):
            body['memberUids'] = request.member_uids
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.RemoveGroupMembersResponse(),
            await self.do_roarequest_async('RemoveGroupMembers', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/groups/members/batchRemove', 'none', req, runtime)
        )

    def send_message(
        self,
        request: dingtalkimpaas__1__0_models.SendMessageRequest,
    ) -> dingtalkimpaas__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.SendMessageHeaders()
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: dingtalkimpaas__1__0_models.SendMessageRequest,
    ) -> dingtalkimpaas__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.SendMessageHeaders()
        return await self.send_message_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        request: dingtalkimpaas__1__0_models.SendMessageRequest,
        headers: dingtalkimpaas__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.receiver_uid):
            body['receiverUid'] = request.receiver_uid
        if not UtilClient.is_unset(request.sender_uid):
            body['senderUid'] = request.sender_uid
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.SendMessageResponse(),
            self.do_roarequest('SendMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/send', 'json', req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.SendMessageRequest,
        headers: dingtalkimpaas__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.receiver_uid):
            body['receiverUid'] = request.receiver_uid
        if not UtilClient.is_unset(request.sender_uid):
            body['senderUid'] = request.sender_uid
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.SendMessageResponse(),
            await self.do_roarequest_async('SendMessage', 'impaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/impaas/interconnections/messages/send', 'json', req, runtime)
        )

    def update_group_name(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupNameRequest,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.UpdateGroupNameHeaders()
        return self.update_group_name_with_options(request, headers, runtime)

    async def update_group_name_async(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupNameRequest,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.UpdateGroupNameHeaders()
        return await self.update_group_name_with_options_async(request, headers, runtime)

    def update_group_name_with_options(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupNameRequest,
        headers: dingtalkimpaas__1__0_models.UpdateGroupNameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.UpdateGroupNameResponse(),
            self.do_roarequest('UpdateGroupName', 'impaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/impaas/interconnections/groups/names', 'none', req, runtime)
        )

    async def update_group_name_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupNameRequest,
        headers: dingtalkimpaas__1__0_models.UpdateGroupNameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.UpdateGroupNameResponse(),
            await self.do_roarequest_async('UpdateGroupName', 'impaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/impaas/interconnections/groups/names', 'none', req, runtime)
        )

    def update_group_owner(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupOwnerRequest,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.UpdateGroupOwnerHeaders()
        return self.update_group_owner_with_options(request, headers, runtime)

    async def update_group_owner_async(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupOwnerRequest,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkimpaas__1__0_models.UpdateGroupOwnerHeaders()
        return await self.update_group_owner_with_options_async(request, headers, runtime)

    def update_group_owner_with_options(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupOwnerRequest,
        headers: dingtalkimpaas__1__0_models.UpdateGroupOwnerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.owner_uid):
            body['ownerUid'] = request.owner_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse(),
            self.do_roarequest('UpdateGroupOwner', 'impaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/impaas/interconnections/groups/owners', 'none', req, runtime)
        )

    async def update_group_owner_with_options_async(
        self,
        request: dingtalkimpaas__1__0_models.UpdateGroupOwnerRequest,
        headers: dingtalkimpaas__1__0_models.UpdateGroupOwnerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conversation_id):
            body['conversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.operator_uid):
            body['operatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.owner_uid):
            body['ownerUid'] = request.owner_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.operation_source):
            real_headers['operationSource'] = UtilClient.to_jsonstring(headers.operation_source)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkimpaas__1__0_models.UpdateGroupOwnerResponse(),
            await self.do_roarequest_async('UpdateGroupOwner', 'impaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/impaas/interconnections/groups/owners', 'none', req, runtime)
        )
