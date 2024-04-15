# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.live_1_0 import models as dingtalklive__1__0_models
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

    def add_share_cid_list(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.AddShareCidListRequest,
    ) -> dingtalklive__1__0_models.AddShareCidListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.AddShareCidListHeaders()
        return self.add_share_cid_list_with_options(feed_id, request, headers, runtime)

    async def add_share_cid_list_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.AddShareCidListRequest,
    ) -> dingtalklive__1__0_models.AddShareCidListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.AddShareCidListHeaders()
        return await self.add_share_cid_list_with_options_async(feed_id, request, headers, runtime)

    def add_share_cid_list_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.AddShareCidListRequest,
        headers: dingtalklive__1__0_models.AddShareCidListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.AddShareCidListResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
        if not UtilClient.is_unset(request.group_id_type):
            body['groupIdType'] = request.group_id_type
        if not UtilClient.is_unset(request.group_ids):
            body['groupIds'] = request.group_ids
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
            dingtalklive__1__0_models.AddShareCidListResponse(),
            self.do_roarequest('AddShareCidList', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/share', 'json', req, runtime)
        )

    async def add_share_cid_list_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.AddShareCidListRequest,
        headers: dingtalklive__1__0_models.AddShareCidListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.AddShareCidListResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
        if not UtilClient.is_unset(request.group_id_type):
            body['groupIdType'] = request.group_id_type
        if not UtilClient.is_unset(request.group_ids):
            body['groupIds'] = request.group_ids
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
            dingtalklive__1__0_models.AddShareCidListResponse(),
            await self.do_roarequest_async('AddShareCidList', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/share', 'json', req, runtime)
        )

    def create_cloud_feed(
        self,
        request: dingtalklive__1__0_models.CreateCloudFeedRequest,
    ) -> dingtalklive__1__0_models.CreateCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.CreateCloudFeedHeaders()
        return self.create_cloud_feed_with_options(request, headers, runtime)

    async def create_cloud_feed_async(
        self,
        request: dingtalklive__1__0_models.CreateCloudFeedRequest,
    ) -> dingtalklive__1__0_models.CreateCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.CreateCloudFeedHeaders()
        return await self.create_cloud_feed_with_options_async(request, headers, runtime)

    def create_cloud_feed_with_options(
        self,
        request: dingtalklive__1__0_models.CreateCloudFeedRequest,
        headers: dingtalklive__1__0_models.CreateCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.CreateCloudFeedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.intro):
            body['intro'] = request.intro
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
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
            dingtalklive__1__0_models.CreateCloudFeedResponse(),
            self.do_roarequest('CreateCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds', 'json', req, runtime)
        )

    async def create_cloud_feed_with_options_async(
        self,
        request: dingtalklive__1__0_models.CreateCloudFeedRequest,
        headers: dingtalklive__1__0_models.CreateCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.CreateCloudFeedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.intro):
            body['intro'] = request.intro
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.video_url):
            body['videoUrl'] = request.video_url
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
            dingtalklive__1__0_models.CreateCloudFeedResponse(),
            await self.do_roarequest_async('CreateCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds', 'json', req, runtime)
        )

    def delete_live_feed(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.DeleteLiveFeedRequest,
    ) -> dingtalklive__1__0_models.DeleteLiveFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.DeleteLiveFeedHeaders()
        return self.delete_live_feed_with_options(feed_id, request, headers, runtime)

    async def delete_live_feed_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.DeleteLiveFeedRequest,
    ) -> dingtalklive__1__0_models.DeleteLiveFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.DeleteLiveFeedHeaders()
        return await self.delete_live_feed_with_options_async(feed_id, request, headers, runtime)

    def delete_live_feed_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.DeleteLiveFeedRequest,
        headers: dingtalklive__1__0_models.DeleteLiveFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.DeleteLiveFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
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
            dingtalklive__1__0_models.DeleteLiveFeedResponse(),
            self.do_roarequest('DeleteLiveFeed', 'live_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/live/openFeeds/{feed_id}', 'json', req, runtime)
        )

    async def delete_live_feed_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.DeleteLiveFeedRequest,
        headers: dingtalklive__1__0_models.DeleteLiveFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.DeleteLiveFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
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
            dingtalklive__1__0_models.DeleteLiveFeedResponse(),
            await self.do_roarequest_async('DeleteLiveFeed', 'live_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/live/openFeeds/{feed_id}', 'json', req, runtime)
        )

    def edit_feed_replay(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.EditFeedReplayRequest,
    ) -> dingtalklive__1__0_models.EditFeedReplayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.EditFeedReplayHeaders()
        return self.edit_feed_replay_with_options(feed_id, request, headers, runtime)

    async def edit_feed_replay_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.EditFeedReplayRequest,
    ) -> dingtalklive__1__0_models.EditFeedReplayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.EditFeedReplayHeaders()
        return await self.edit_feed_replay_with_options_async(feed_id, request, headers, runtime)

    def edit_feed_replay_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.EditFeedReplayRequest,
        headers: dingtalklive__1__0_models.EditFeedReplayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.EditFeedReplayResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
        if not UtilClient.is_unset(request.edit_end_time):
            body['editEndTime'] = request.edit_end_time
        if not UtilClient.is_unset(request.edit_start_time):
            body['editStartTime'] = request.edit_start_time
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
            dingtalklive__1__0_models.EditFeedReplayResponse(),
            self.do_roarequest('EditFeedReplay', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}/cutReplay', 'json', req, runtime)
        )

    async def edit_feed_replay_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.EditFeedReplayRequest,
        headers: dingtalklive__1__0_models.EditFeedReplayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.EditFeedReplayResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
        if not UtilClient.is_unset(request.edit_end_time):
            body['editEndTime'] = request.edit_end_time
        if not UtilClient.is_unset(request.edit_start_time):
            body['editStartTime'] = request.edit_start_time
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
            dingtalklive__1__0_models.EditFeedReplayResponse(),
            await self.do_roarequest_async('EditFeedReplay', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}/cutReplay', 'json', req, runtime)
        )

    def modify_feed_white_list(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.ModifyFeedWhiteListRequest,
    ) -> dingtalklive__1__0_models.ModifyFeedWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.ModifyFeedWhiteListHeaders()
        return self.modify_feed_white_list_with_options(feed_id, request, headers, runtime)

    async def modify_feed_white_list_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.ModifyFeedWhiteListRequest,
    ) -> dingtalklive__1__0_models.ModifyFeedWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.ModifyFeedWhiteListHeaders()
        return await self.modify_feed_white_list_with_options_async(feed_id, request, headers, runtime)

    def modify_feed_white_list_with_options(
        self,
        feed_id: str,
        tmp_req: dingtalklive__1__0_models.ModifyFeedWhiteListRequest,
        headers: dingtalklive__1__0_models.ModifyFeedWhiteListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.ModifyFeedWhiteListResponse:
        UtilClient.validate_model(tmp_req)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        request = dingtalklive__1__0_models.ModifyFeedWhiteListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_user_list):
            request.modify_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.modify_user_list, 'modifyUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.modify_user_list_shrink):
            query['modifyUserList'] = request.modify_user_list_shrink
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
            dingtalklive__1__0_models.ModifyFeedWhiteListResponse(),
            self.do_roarequest('ModifyFeedWhiteList', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}/whiteList', 'json', req, runtime)
        )

    async def modify_feed_white_list_with_options_async(
        self,
        feed_id: str,
        tmp_req: dingtalklive__1__0_models.ModifyFeedWhiteListRequest,
        headers: dingtalklive__1__0_models.ModifyFeedWhiteListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.ModifyFeedWhiteListResponse:
        UtilClient.validate_model(tmp_req)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        request = dingtalklive__1__0_models.ModifyFeedWhiteListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_user_list):
            request.modify_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.modify_user_list, 'modifyUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.modify_user_list_shrink):
            query['modifyUserList'] = request.modify_user_list_shrink
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
            dingtalklive__1__0_models.ModifyFeedWhiteListResponse(),
            await self.do_roarequest_async('ModifyFeedWhiteList', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}/whiteList', 'json', req, runtime)
        )

    def query_feed_white_list(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.QueryFeedWhiteListRequest,
    ) -> dingtalklive__1__0_models.QueryFeedWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.QueryFeedWhiteListHeaders()
        return self.query_feed_white_list_with_options(feed_id, request, headers, runtime)

    async def query_feed_white_list_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.QueryFeedWhiteListRequest,
    ) -> dingtalklive__1__0_models.QueryFeedWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.QueryFeedWhiteListHeaders()
        return await self.query_feed_white_list_with_options_async(feed_id, request, headers, runtime)

    def query_feed_white_list_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.QueryFeedWhiteListRequest,
        headers: dingtalklive__1__0_models.QueryFeedWhiteListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.QueryFeedWhiteListResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
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
            dingtalklive__1__0_models.QueryFeedWhiteListResponse(),
            self.do_roarequest('QueryFeedWhiteList', 'live_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/live/openFeeds/{feed_id}/whiteList', 'json', req, runtime)
        )

    async def query_feed_white_list_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.QueryFeedWhiteListRequest,
        headers: dingtalklive__1__0_models.QueryFeedWhiteListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.QueryFeedWhiteListResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
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
            dingtalklive__1__0_models.QueryFeedWhiteListResponse(),
            await self.do_roarequest_async('QueryFeedWhiteList', 'live_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/live/openFeeds/{feed_id}/whiteList', 'json', req, runtime)
        )

    def start_cloud_feed(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StartCloudFeedRequest,
    ) -> dingtalklive__1__0_models.StartCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.StartCloudFeedHeaders()
        return self.start_cloud_feed_with_options(feed_id, request, headers, runtime)

    async def start_cloud_feed_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StartCloudFeedRequest,
    ) -> dingtalklive__1__0_models.StartCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.StartCloudFeedHeaders()
        return await self.start_cloud_feed_with_options_async(feed_id, request, headers, runtime)

    def start_cloud_feed_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StartCloudFeedRequest,
        headers: dingtalklive__1__0_models.StartCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.StartCloudFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
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
            dingtalklive__1__0_models.StartCloudFeedResponse(),
            self.do_roarequest('StartCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/start', 'json', req, runtime)
        )

    async def start_cloud_feed_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StartCloudFeedRequest,
        headers: dingtalklive__1__0_models.StartCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.StartCloudFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
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
            dingtalklive__1__0_models.StartCloudFeedResponse(),
            await self.do_roarequest_async('StartCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/start', 'json', req, runtime)
        )

    def stop_cloud_feed(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StopCloudFeedRequest,
    ) -> dingtalklive__1__0_models.StopCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.StopCloudFeedHeaders()
        return self.stop_cloud_feed_with_options(feed_id, request, headers, runtime)

    async def stop_cloud_feed_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StopCloudFeedRequest,
    ) -> dingtalklive__1__0_models.StopCloudFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.StopCloudFeedHeaders()
        return await self.stop_cloud_feed_with_options_async(feed_id, request, headers, runtime)

    def stop_cloud_feed_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StopCloudFeedRequest,
        headers: dingtalklive__1__0_models.StopCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.StopCloudFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
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
            dingtalklive__1__0_models.StopCloudFeedResponse(),
            self.do_roarequest('StopCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/stop', 'json', req, runtime)
        )

    async def stop_cloud_feed_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.StopCloudFeedRequest,
        headers: dingtalklive__1__0_models.StopCloudFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.StopCloudFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        body = {}
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
            dingtalklive__1__0_models.StopCloudFeedResponse(),
            await self.do_roarequest_async('StopCloudFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/cloudFeeds/{feed_id}/stop', 'json', req, runtime)
        )

    def update_live_feed(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.UpdateLiveFeedRequest,
    ) -> dingtalklive__1__0_models.UpdateLiveFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.UpdateLiveFeedHeaders()
        return self.update_live_feed_with_options(feed_id, request, headers, runtime)

    async def update_live_feed_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.UpdateLiveFeedRequest,
    ) -> dingtalklive__1__0_models.UpdateLiveFeedResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalklive__1__0_models.UpdateLiveFeedHeaders()
        return await self.update_live_feed_with_options_async(feed_id, request, headers, runtime)

    def update_live_feed_with_options(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.UpdateLiveFeedRequest,
        headers: dingtalklive__1__0_models.UpdateLiveFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.UpdateLiveFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            query['introduction'] = request.introduction
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
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
            dingtalklive__1__0_models.UpdateLiveFeedResponse(),
            self.do_roarequest('UpdateLiveFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}', 'json', req, runtime)
        )

    async def update_live_feed_with_options_async(
        self,
        feed_id: str,
        request: dingtalklive__1__0_models.UpdateLiveFeedRequest,
        headers: dingtalklive__1__0_models.UpdateLiveFeedHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalklive__1__0_models.UpdateLiveFeedResponse:
        UtilClient.validate_model(request)
        feed_id = OpenApiUtilClient.get_encode_param(feed_id)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            query['introduction'] = request.introduction
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
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
            dingtalklive__1__0_models.UpdateLiveFeedResponse(),
            await self.do_roarequest_async('UpdateLiveFeed', 'live_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/live/openFeeds/{feed_id}', 'json', req, runtime)
        )
