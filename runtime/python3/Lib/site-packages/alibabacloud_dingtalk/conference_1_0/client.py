# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
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

    def close_video_conference(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.CloseVideoConferenceRequest,
    ) -> dingtalkconference__1__0_models.CloseVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.CloseVideoConferenceHeaders()
        return self.close_video_conference_with_options(conference_id, request, headers, runtime)

    async def close_video_conference_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.CloseVideoConferenceRequest,
    ) -> dingtalkconference__1__0_models.CloseVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.CloseVideoConferenceHeaders()
        return await self.close_video_conference_with_options_async(conference_id, request, headers, runtime)

    def close_video_conference_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.CloseVideoConferenceRequest,
        headers: dingtalkconference__1__0_models.CloseVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.CloseVideoConferenceResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.CloseVideoConferenceResponse(),
            self.do_roarequest('CloseVideoConference', 'conference_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/conference/videoConferences/{conference_id}', 'json', req, runtime)
        )

    async def close_video_conference_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.CloseVideoConferenceRequest,
        headers: dingtalkconference__1__0_models.CloseVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.CloseVideoConferenceResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.CloseVideoConferenceResponse(),
            await self.do_roarequest_async('CloseVideoConference', 'conference_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/conference/videoConferences/{conference_id}', 'json', req, runtime)
        )

    def create_video_conference(
        self,
        request: dingtalkconference__1__0_models.CreateVideoConferenceRequest,
    ) -> dingtalkconference__1__0_models.CreateVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.CreateVideoConferenceHeaders()
        return self.create_video_conference_with_options(request, headers, runtime)

    async def create_video_conference_async(
        self,
        request: dingtalkconference__1__0_models.CreateVideoConferenceRequest,
    ) -> dingtalkconference__1__0_models.CreateVideoConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.CreateVideoConferenceHeaders()
        return await self.create_video_conference_with_options_async(request, headers, runtime)

    def create_video_conference_with_options(
        self,
        request: dingtalkconference__1__0_models.CreateVideoConferenceRequest,
        headers: dingtalkconference__1__0_models.CreateVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.CreateVideoConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['confTitle'] = request.conf_title
        if not UtilClient.is_unset(request.invite_caller):
            body['inviteCaller'] = request.invite_caller
        if not UtilClient.is_unset(request.invite_user_ids):
            body['inviteUserIds'] = request.invite_user_ids
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
            dingtalkconference__1__0_models.CreateVideoConferenceResponse(),
            self.do_roarequest('CreateVideoConference', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences', 'json', req, runtime)
        )

    async def create_video_conference_with_options_async(
        self,
        request: dingtalkconference__1__0_models.CreateVideoConferenceRequest,
        headers: dingtalkconference__1__0_models.CreateVideoConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.CreateVideoConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['confTitle'] = request.conf_title
        if not UtilClient.is_unset(request.invite_caller):
            body['inviteCaller'] = request.invite_caller
        if not UtilClient.is_unset(request.invite_user_ids):
            body['inviteUserIds'] = request.invite_user_ids
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
            dingtalkconference__1__0_models.CreateVideoConferenceResponse(),
            await self.do_roarequest_async('CreateVideoConference', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences', 'json', req, runtime)
        )

    def query_cloud_record_text(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordTextRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordTextHeaders()
        return self.query_cloud_record_text_with_options(conference_id, request, headers, runtime)

    async def query_cloud_record_text_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordTextRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordTextHeaders()
        return await self.query_cloud_record_text_with_options_async(conference_id, request, headers, runtime)

    def query_cloud_record_text_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordTextRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordTextResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordTextResponse(),
            self.do_roarequest('QueryCloudRecordText', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/getTexts', 'json', req, runtime)
        )

    async def query_cloud_record_text_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordTextRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordTextResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordTextResponse(),
            await self.do_roarequest_async('QueryCloudRecordText', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/getTexts', 'json', req, runtime)
        )

    def query_cloud_record_video(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordVideoHeaders()
        return self.query_cloud_record_video_with_options(conference_id, request, headers, runtime)

    async def query_cloud_record_video_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordVideoHeaders()
        return await self.query_cloud_record_video_with_options_async(conference_id, request, headers, runtime)

    def query_cloud_record_video_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordVideoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordVideoResponse(),
            self.do_roarequest('QueryCloudRecordVideo', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/getVideos', 'json', req, runtime)
        )

    async def query_cloud_record_video_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordVideoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordVideoResponse(),
            await self.do_roarequest_async('QueryCloudRecordVideo', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/getVideos', 'json', req, runtime)
        )

    def query_cloud_record_video_play_info(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoHeaders()
        return self.query_cloud_record_video_play_info_with_options(conference_id, request, headers, runtime)

    async def query_cloud_record_video_play_info_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoRequest,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoHeaders()
        return await self.query_cloud_record_video_play_info_with_options_async(conference_id, request, headers, runtime)

    def query_cloud_record_video_play_info_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse(),
            self.do_roarequest('QueryCloudRecordVideoPlayInfo', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/videos/getPlayInfos', 'json', req, runtime)
        )

    async def query_cloud_record_video_play_info_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoRequest,
        headers: dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.QueryCloudRecordVideoPlayInfoResponse(),
            await self.do_roarequest_async('QueryCloudRecordVideoPlayInfo', 'conference_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/videos/getPlayInfos', 'json', req, runtime)
        )

    def query_conference_info_batch(
        self,
        request: dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest,
    ) -> dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders()
        return self.query_conference_info_batch_with_options(request, headers, runtime)

    async def query_conference_info_batch_async(
        self,
        request: dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest,
    ) -> dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders()
        return await self.query_conference_info_batch_with_options_async(request, headers, runtime)

    def query_conference_info_batch_with_options(
        self,
        request: dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest,
        headers: dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id_list):
            body['conferenceIdList'] = request.conference_id_list
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
            dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse(),
            self.do_roarequest('QueryConferenceInfoBatch', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/query', 'json', req, runtime)
        )

    async def query_conference_info_batch_with_options_async(
        self,
        request: dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest,
        headers: dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id_list):
            body['conferenceIdList'] = request.conference_id_list
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
            dingtalkconference__1__0_models.QueryConferenceInfoBatchResponse(),
            await self.do_roarequest_async('QueryConferenceInfoBatch', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/query', 'json', req, runtime)
        )

    def start_cloud_record(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartCloudRecordRequest,
    ) -> dingtalkconference__1__0_models.StartCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StartCloudRecordHeaders()
        return self.start_cloud_record_with_options(conference_id, request, headers, runtime)

    async def start_cloud_record_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartCloudRecordRequest,
    ) -> dingtalkconference__1__0_models.StartCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StartCloudRecordHeaders()
        return await self.start_cloud_record_with_options_async(conference_id, request, headers, runtime)

    def start_cloud_record_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartCloudRecordRequest,
        headers: dingtalkconference__1__0_models.StartCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StartCloudRecordResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.small_window_position):
            body['smallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StartCloudRecordResponse(),
            self.do_roarequest('StartCloudRecord', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/start', 'json', req, runtime)
        )

    async def start_cloud_record_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartCloudRecordRequest,
        headers: dingtalkconference__1__0_models.StartCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StartCloudRecordResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.small_window_position):
            body['smallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StartCloudRecordResponse(),
            await self.do_roarequest_async('StartCloudRecord', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/start', 'json', req, runtime)
        )

    def start_stream_out(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartStreamOutRequest,
    ) -> dingtalkconference__1__0_models.StartStreamOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StartStreamOutHeaders()
        return self.start_stream_out_with_options(conference_id, request, headers, runtime)

    async def start_stream_out_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartStreamOutRequest,
    ) -> dingtalkconference__1__0_models.StartStreamOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StartStreamOutHeaders()
        return await self.start_stream_out_with_options_async(conference_id, request, headers, runtime)

    def start_stream_out_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartStreamOutRequest,
        headers: dingtalkconference__1__0_models.StartStreamOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StartStreamOutResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.need_host_join):
            body['needHostJoin'] = request.need_host_join
        if not UtilClient.is_unset(request.small_window_position):
            body['smallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.stream_name):
            body['streamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_url_list):
            body['streamUrlList'] = request.stream_url_list
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StartStreamOutResponse(),
            self.do_roarequest('StartStreamOut', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/streamOuts/start', 'json', req, runtime)
        )

    async def start_stream_out_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StartStreamOutRequest,
        headers: dingtalkconference__1__0_models.StartStreamOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StartStreamOutResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.need_host_join):
            body['needHostJoin'] = request.need_host_join
        if not UtilClient.is_unset(request.small_window_position):
            body['smallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.stream_name):
            body['streamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_url_list):
            body['streamUrlList'] = request.stream_url_list
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StartStreamOutResponse(),
            await self.do_roarequest_async('StartStreamOut', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/streamOuts/start', 'json', req, runtime)
        )

    def stop_cloud_record(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopCloudRecordRequest,
    ) -> dingtalkconference__1__0_models.StopCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StopCloudRecordHeaders()
        return self.stop_cloud_record_with_options(conference_id, request, headers, runtime)

    async def stop_cloud_record_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopCloudRecordRequest,
    ) -> dingtalkconference__1__0_models.StopCloudRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StopCloudRecordHeaders()
        return await self.stop_cloud_record_with_options_async(conference_id, request, headers, runtime)

    def stop_cloud_record_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopCloudRecordRequest,
        headers: dingtalkconference__1__0_models.StopCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StopCloudRecordResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StopCloudRecordResponse(),
            self.do_roarequest('StopCloudRecord', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/stop', 'json', req, runtime)
        )

    async def stop_cloud_record_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopCloudRecordRequest,
        headers: dingtalkconference__1__0_models.StopCloudRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StopCloudRecordResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StopCloudRecordResponse(),
            await self.do_roarequest_async('StopCloudRecord', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/cloudRecords/stop', 'json', req, runtime)
        )

    def stop_stream_out(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopStreamOutRequest,
    ) -> dingtalkconference__1__0_models.StopStreamOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StopStreamOutHeaders()
        return self.stop_stream_out_with_options(conference_id, request, headers, runtime)

    async def stop_stream_out_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopStreamOutRequest,
    ) -> dingtalkconference__1__0_models.StopStreamOutResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.StopStreamOutHeaders()
        return await self.stop_stream_out_with_options_async(conference_id, request, headers, runtime)

    def stop_stream_out_with_options(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopStreamOutRequest,
        headers: dingtalkconference__1__0_models.StopStreamOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StopStreamOutResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.stop_all_stream):
            body['stopAllStream'] = request.stop_all_stream
        if not UtilClient.is_unset(request.stream_id):
            body['streamId'] = request.stream_id
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StopStreamOutResponse(),
            self.do_roarequest('StopStreamOut', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/streamOuts/stop', 'json', req, runtime)
        )

    async def stop_stream_out_with_options_async(
        self,
        conference_id: str,
        request: dingtalkconference__1__0_models.StopStreamOutRequest,
        headers: dingtalkconference__1__0_models.StopStreamOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.StopStreamOutResponse:
        UtilClient.validate_model(request)
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        body = {}
        if not UtilClient.is_unset(request.stop_all_stream):
            body['stopAllStream'] = request.stop_all_stream
        if not UtilClient.is_unset(request.stream_id):
            body['streamId'] = request.stream_id
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkconference__1__0_models.StopStreamOutResponse(),
            await self.do_roarequest_async('StopStreamOut', 'conference_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/streamOuts/stop', 'json', req, runtime)
        )

    def update_video_conference_ext_info(
        self,
        conference_id: str,
    ) -> dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoHeaders()
        return self.update_video_conference_ext_info_with_options(conference_id, headers, runtime)

    async def update_video_conference_ext_info_async(
        self,
        conference_id: str,
    ) -> dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoHeaders()
        return await self.update_video_conference_ext_info_with_options_async(conference_id, headers, runtime)

    def update_video_conference_ext_info_with_options(
        self,
        conference_id: str,
        headers: dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse:
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse(),
            self.do_roarequest('UpdateVideoConferenceExtInfo', 'conference_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/extInfo', 'json', req, runtime)
        )

    async def update_video_conference_ext_info_with_options_async(
        self,
        conference_id: str,
        headers: dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse:
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkconference__1__0_models.UpdateVideoConferenceExtInfoResponse(),
            await self.do_roarequest_async('UpdateVideoConferenceExtInfo', 'conference_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/conference/videoConferences/{conference_id}/extInfo', 'json', req, runtime)
        )
