# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.flashmeeting_1_0 import models as dingtalkflashmeeting__1__0_models
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

    def create_flash_meeting(
        self,
        request: dingtalkflashmeeting__1__0_models.CreateFlashMeetingRequest,
    ) -> dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkflashmeeting__1__0_models.CreateFlashMeetingHeaders()
        return self.create_flash_meeting_with_options(request, headers, runtime)

    async def create_flash_meeting_async(
        self,
        request: dingtalkflashmeeting__1__0_models.CreateFlashMeetingRequest,
    ) -> dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkflashmeeting__1__0_models.CreateFlashMeetingHeaders()
        return await self.create_flash_meeting_with_options_async(request, headers, runtime)

    def create_flash_meeting_with_options(
        self,
        request: dingtalkflashmeeting__1__0_models.CreateFlashMeetingRequest,
        headers: dingtalkflashmeeting__1__0_models.CreateFlashMeetingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.event_id):
            body['eventId'] = request.event_id
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
            dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse(),
            self.do_roarequest('CreateFlashMeeting', 'flashmeeting_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/flashmeeting/meetings', 'json', req, runtime)
        )

    async def create_flash_meeting_with_options_async(
        self,
        request: dingtalkflashmeeting__1__0_models.CreateFlashMeetingRequest,
        headers: dingtalkflashmeeting__1__0_models.CreateFlashMeetingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.event_id):
            body['eventId'] = request.event_id
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
            dingtalkflashmeeting__1__0_models.CreateFlashMeetingResponse(),
            await self.do_roarequest_async('CreateFlashMeeting', 'flashmeeting_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/flashmeeting/meetings', 'json', req, runtime)
        )
