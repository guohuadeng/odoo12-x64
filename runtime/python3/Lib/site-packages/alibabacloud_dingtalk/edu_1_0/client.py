# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
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

    def add_device(
        self,
        request: dingtalkedu__1__0_models.AddDeviceRequest,
    ) -> dingtalkedu__1__0_models.AddDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.AddDeviceHeaders()
        return self.add_device_with_options(request, headers, runtime)

    async def add_device_async(
        self,
        request: dingtalkedu__1__0_models.AddDeviceRequest,
    ) -> dingtalkedu__1__0_models.AddDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.AddDeviceHeaders()
        return await self.add_device_with_options_async(request, headers, runtime)

    def add_device_with_options(
        self,
        request: dingtalkedu__1__0_models.AddDeviceRequest,
        headers: dingtalkedu__1__0_models.AddDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.AddDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.AddDeviceResponse(),
            self.do_roarequest('AddDevice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/devices', 'json', req, runtime)
        )

    async def add_device_with_options_async(
        self,
        request: dingtalkedu__1__0_models.AddDeviceRequest,
        headers: dingtalkedu__1__0_models.AddDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.AddDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.AddDeviceResponse(),
            await self.do_roarequest_async('AddDevice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/devices', 'json', req, runtime)
        )

    def batch_create(
        self,
        request: dingtalkedu__1__0_models.BatchCreateRequest,
    ) -> dingtalkedu__1__0_models.BatchCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.BatchCreateHeaders()
        return self.batch_create_with_options(request, headers, runtime)

    async def batch_create_async(
        self,
        request: dingtalkedu__1__0_models.BatchCreateRequest,
    ) -> dingtalkedu__1__0_models.BatchCreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.BatchCreateHeaders()
        return await self.batch_create_with_options_async(request, headers, runtime)

    def batch_create_with_options(
        self,
        request: dingtalkedu__1__0_models.BatchCreateRequest,
        headers: dingtalkedu__1__0_models.BatchCreateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.BatchCreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_biz_code):
            body['cardBizCode'] = request.card_biz_code
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.js_version):
            body['jsVersion'] = request.js_version
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.userid):
            body['userid'] = request.userid
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
            dingtalkedu__1__0_models.BatchCreateResponse(),
            self.do_roarequest('BatchCreate', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/cards', 'json', req, runtime)
        )

    async def batch_create_with_options_async(
        self,
        request: dingtalkedu__1__0_models.BatchCreateRequest,
        headers: dingtalkedu__1__0_models.BatchCreateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.BatchCreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_biz_code):
            body['cardBizCode'] = request.card_biz_code
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.js_version):
            body['jsVersion'] = request.js_version
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.userid):
            body['userid'] = request.userid
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
            dingtalkedu__1__0_models.BatchCreateResponse(),
            await self.do_roarequest_async('BatchCreate', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/cards', 'json', req, runtime)
        )

    def batch_org_create_hw(
        self,
        request: dingtalkedu__1__0_models.BatchOrgCreateHWRequest,
    ) -> dingtalkedu__1__0_models.BatchOrgCreateHWResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.BatchOrgCreateHWHeaders()
        return self.batch_org_create_hwwith_options(request, headers, runtime)

    async def batch_org_create_hw_async(
        self,
        request: dingtalkedu__1__0_models.BatchOrgCreateHWRequest,
    ) -> dingtalkedu__1__0_models.BatchOrgCreateHWResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.BatchOrgCreateHWHeaders()
        return await self.batch_org_create_hwwith_options_async(request, headers, runtime)

    def batch_org_create_hwwith_options(
        self,
        request: dingtalkedu__1__0_models.BatchOrgCreateHWRequest,
        headers: dingtalkedu__1__0_models.BatchOrgCreateHWHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.BatchOrgCreateHWResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.hw_content):
            body['hwContent'] = request.hw_content
        if not UtilClient.is_unset(request.hw_deadline):
            body['hwDeadline'] = request.hw_deadline
        if not UtilClient.is_unset(request.hw_deadline_open):
            body['hwDeadlineOpen'] = request.hw_deadline_open
        if not UtilClient.is_unset(request.hw_media):
            body['hwMedia'] = request.hw_media
        if not UtilClient.is_unset(request.hw_photo):
            body['hwPhoto'] = request.hw_photo
        if not UtilClient.is_unset(request.hw_title):
            body['hwTitle'] = request.hw_title
        if not UtilClient.is_unset(request.hw_type):
            body['hwType'] = request.hw_type
        if not UtilClient.is_unset(request.hw_video):
            body['hwVideo'] = request.hw_video
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.open_select_item_list):
            body['openSelectItemList'] = request.open_select_item_list
        if not UtilClient.is_unset(request.scheduled_release):
            body['scheduledRelease'] = request.scheduled_release
        if not UtilClient.is_unset(request.scheduled_time):
            body['scheduledTime'] = request.scheduled_time
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.target_role):
            body['targetRole'] = request.target_role
        if not UtilClient.is_unset(request.teacher_name):
            body['teacherName'] = request.teacher_name
        if not UtilClient.is_unset(request.teacher_user_id):
            body['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.BatchOrgCreateHWResponse(),
            self.do_roarequest('BatchOrgCreateHW', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/homeworks', 'json', req, runtime)
        )

    async def batch_org_create_hwwith_options_async(
        self,
        request: dingtalkedu__1__0_models.BatchOrgCreateHWRequest,
        headers: dingtalkedu__1__0_models.BatchOrgCreateHWHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.BatchOrgCreateHWResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attributes):
            body['attributes'] = request.attributes
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.hw_content):
            body['hwContent'] = request.hw_content
        if not UtilClient.is_unset(request.hw_deadline):
            body['hwDeadline'] = request.hw_deadline
        if not UtilClient.is_unset(request.hw_deadline_open):
            body['hwDeadlineOpen'] = request.hw_deadline_open
        if not UtilClient.is_unset(request.hw_media):
            body['hwMedia'] = request.hw_media
        if not UtilClient.is_unset(request.hw_photo):
            body['hwPhoto'] = request.hw_photo
        if not UtilClient.is_unset(request.hw_title):
            body['hwTitle'] = request.hw_title
        if not UtilClient.is_unset(request.hw_type):
            body['hwType'] = request.hw_type
        if not UtilClient.is_unset(request.hw_video):
            body['hwVideo'] = request.hw_video
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.open_select_item_list):
            body['openSelectItemList'] = request.open_select_item_list
        if not UtilClient.is_unset(request.scheduled_release):
            body['scheduledRelease'] = request.scheduled_release
        if not UtilClient.is_unset(request.scheduled_time):
            body['scheduledTime'] = request.scheduled_time
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.target_role):
            body['targetRole'] = request.target_role
        if not UtilClient.is_unset(request.teacher_name):
            body['teacherName'] = request.teacher_name
        if not UtilClient.is_unset(request.teacher_user_id):
            body['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.BatchOrgCreateHWResponse(),
            await self.do_roarequest_async('BatchOrgCreateHW', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/homeworks', 'json', req, runtime)
        )

    def cancel_order(
        self,
        request: dingtalkedu__1__0_models.CancelOrderRequest,
    ) -> dingtalkedu__1__0_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CancelOrderHeaders()
        return self.cancel_order_with_options(request, headers, runtime)

    async def cancel_order_async(
        self,
        request: dingtalkedu__1__0_models.CancelOrderRequest,
    ) -> dingtalkedu__1__0_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CancelOrderHeaders()
        return await self.cancel_order_with_options_async(request, headers, runtime)

    def cancel_order_with_options(
        self,
        request: dingtalkedu__1__0_models.CancelOrderRequest,
        headers: dingtalkedu__1__0_models.CancelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkedu__1__0_models.CancelOrderResponse(),
            self.do_roarequest('CancelOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/cancel', 'json', req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CancelOrderRequest,
        headers: dingtalkedu__1__0_models.CancelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkedu__1__0_models.CancelOrderResponse(),
            await self.do_roarequest_async('CancelOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/cancel', 'json', req, runtime)
        )

    def check_restriction(
        self,
        request: dingtalkedu__1__0_models.CheckRestrictionRequest,
    ) -> dingtalkedu__1__0_models.CheckRestrictionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CheckRestrictionHeaders()
        return self.check_restriction_with_options(request, headers, runtime)

    async def check_restriction_async(
        self,
        request: dingtalkedu__1__0_models.CheckRestrictionRequest,
    ) -> dingtalkedu__1__0_models.CheckRestrictionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CheckRestrictionHeaders()
        return await self.check_restriction_with_options_async(request, headers, runtime)

    def check_restriction_with_options(
        self,
        request: dingtalkedu__1__0_models.CheckRestrictionRequest,
        headers: dingtalkedu__1__0_models.CheckRestrictionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CheckRestrictionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.CheckRestrictionResponse(),
            self.do_roarequest('CheckRestriction', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/restrictions/check', 'json', req, runtime)
        )

    async def check_restriction_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CheckRestrictionRequest,
        headers: dingtalkedu__1__0_models.CheckRestrictionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CheckRestrictionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.CheckRestrictionResponse(),
            await self.do_roarequest_async('CheckRestriction', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/restrictions/check', 'json', req, runtime)
        )

    def course_scheduling_compliment_notice(
        self,
        request: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeRequest,
    ) -> dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeHeaders()
        return self.course_scheduling_compliment_notice_with_options(request, headers, runtime)

    async def course_scheduling_compliment_notice_async(
        self,
        request: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeRequest,
    ) -> dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeHeaders()
        return await self.course_scheduling_compliment_notice_with_options_async(request, headers, runtime)

    def course_scheduling_compliment_notice_with_options(
        self,
        request: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeRequest,
        headers: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse(),
            self.do_roarequest('CourseSchedulingComplimentNotice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/schedules/finishNotify', 'json', req, runtime)
        )

    async def course_scheduling_compliment_notice_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeRequest,
        headers: dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.CourseSchedulingComplimentNoticeResponse(),
            await self.do_roarequest_async('CourseSchedulingComplimentNotice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/schedules/finishNotify', 'json', req, runtime)
        )

    def create_custom_class(
        self,
        request: dingtalkedu__1__0_models.CreateCustomClassRequest,
    ) -> dingtalkedu__1__0_models.CreateCustomClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateCustomClassHeaders()
        return self.create_custom_class_with_options(request, headers, runtime)

    async def create_custom_class_async(
        self,
        request: dingtalkedu__1__0_models.CreateCustomClassRequest,
    ) -> dingtalkedu__1__0_models.CreateCustomClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateCustomClassHeaders()
        return await self.create_custom_class_with_options_async(request, headers, runtime)

    def create_custom_class_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateCustomClassRequest,
        headers: dingtalkedu__1__0_models.CreateCustomClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateCustomClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_class):
            body['customClass'] = request.custom_class
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.super_id):
            body['superId'] = request.super_id
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
            dingtalkedu__1__0_models.CreateCustomClassResponse(),
            self.do_roarequest('CreateCustomClass', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/customClasses', 'json', req, runtime)
        )

    async def create_custom_class_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateCustomClassRequest,
        headers: dingtalkedu__1__0_models.CreateCustomClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateCustomClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_class):
            body['customClass'] = request.custom_class
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.super_id):
            body['superId'] = request.super_id
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
            dingtalkedu__1__0_models.CreateCustomClassResponse(),
            await self.do_roarequest_async('CreateCustomClass', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/customClasses', 'json', req, runtime)
        )

    def create_custom_dept(
        self,
        request: dingtalkedu__1__0_models.CreateCustomDeptRequest,
    ) -> dingtalkedu__1__0_models.CreateCustomDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateCustomDeptHeaders()
        return self.create_custom_dept_with_options(request, headers, runtime)

    async def create_custom_dept_async(
        self,
        request: dingtalkedu__1__0_models.CreateCustomDeptRequest,
    ) -> dingtalkedu__1__0_models.CreateCustomDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateCustomDeptHeaders()
        return await self.create_custom_dept_with_options_async(request, headers, runtime)

    def create_custom_dept_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateCustomDeptRequest,
        headers: dingtalkedu__1__0_models.CreateCustomDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateCustomDeptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_dept):
            body['customDept'] = request.custom_dept
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.super_id):
            body['superId'] = request.super_id
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
            dingtalkedu__1__0_models.CreateCustomDeptResponse(),
            self.do_roarequest('CreateCustomDept', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/customDepts', 'json', req, runtime)
        )

    async def create_custom_dept_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateCustomDeptRequest,
        headers: dingtalkedu__1__0_models.CreateCustomDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateCustomDeptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_dept):
            body['customDept'] = request.custom_dept
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.super_id):
            body['superId'] = request.super_id
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
            dingtalkedu__1__0_models.CreateCustomDeptResponse(),
            await self.do_roarequest_async('CreateCustomDept', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/customDepts', 'json', req, runtime)
        )

    def create_edu_asset_space(
        self,
        request: dingtalkedu__1__0_models.CreateEduAssetSpaceRequest,
    ) -> dingtalkedu__1__0_models.CreateEduAssetSpaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateEduAssetSpaceHeaders()
        return self.create_edu_asset_space_with_options(request, headers, runtime)

    async def create_edu_asset_space_async(
        self,
        request: dingtalkedu__1__0_models.CreateEduAssetSpaceRequest,
    ) -> dingtalkedu__1__0_models.CreateEduAssetSpaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateEduAssetSpaceHeaders()
        return await self.create_edu_asset_space_with_options_async(request, headers, runtime)

    def create_edu_asset_space_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateEduAssetSpaceRequest,
        headers: dingtalkedu__1__0_models.CreateEduAssetSpaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateEduAssetSpaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.space_desc):
            body['spaceDesc'] = request.space_desc
        if not UtilClient.is_unset(request.space_icon):
            body['spaceIcon'] = request.space_icon
        if not UtilClient.is_unset(request.space_name):
            body['spaceName'] = request.space_name
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
            dingtalkedu__1__0_models.CreateEduAssetSpaceResponse(),
            self.do_roarequest('CreateEduAssetSpace', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/assets/spaces', 'json', req, runtime)
        )

    async def create_edu_asset_space_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateEduAssetSpaceRequest,
        headers: dingtalkedu__1__0_models.CreateEduAssetSpaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateEduAssetSpaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.space_desc):
            body['spaceDesc'] = request.space_desc
        if not UtilClient.is_unset(request.space_icon):
            body['spaceIcon'] = request.space_icon
        if not UtilClient.is_unset(request.space_name):
            body['spaceName'] = request.space_name
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
            dingtalkedu__1__0_models.CreateEduAssetSpaceResponse(),
            await self.do_roarequest_async('CreateEduAssetSpace', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/assets/spaces', 'json', req, runtime)
        )

    def create_fulfil_record(
        self,
        request: dingtalkedu__1__0_models.CreateFulfilRecordRequest,
    ) -> dingtalkedu__1__0_models.CreateFulfilRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateFulfilRecordHeaders()
        return self.create_fulfil_record_with_options(request, headers, runtime)

    async def create_fulfil_record_async(
        self,
        request: dingtalkedu__1__0_models.CreateFulfilRecordRequest,
    ) -> dingtalkedu__1__0_models.CreateFulfilRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateFulfilRecordHeaders()
        return await self.create_fulfil_record_with_options_async(request, headers, runtime)

    def create_fulfil_record_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateFulfilRecordRequest,
        headers: dingtalkedu__1__0_models.CreateFulfilRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateFulfilRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_time):
            body['bizTime'] = request.biz_time
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.CreateFulfilRecordResponse(),
            self.do_roarequest('CreateFulfilRecord', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/fulfilRecords', 'json', req, runtime)
        )

    async def create_fulfil_record_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateFulfilRecordRequest,
        headers: dingtalkedu__1__0_models.CreateFulfilRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateFulfilRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_time):
            body['bizTime'] = request.biz_time
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.CreateFulfilRecordResponse(),
            await self.do_roarequest_async('CreateFulfilRecord', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/fulfilRecords', 'json', req, runtime)
        )

    def create_invite_url(
        self,
        request: dingtalkedu__1__0_models.CreateInviteUrlRequest,
    ) -> dingtalkedu__1__0_models.CreateInviteUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateInviteUrlHeaders()
        return self.create_invite_url_with_options(request, headers, runtime)

    async def create_invite_url_async(
        self,
        request: dingtalkedu__1__0_models.CreateInviteUrlRequest,
    ) -> dingtalkedu__1__0_models.CreateInviteUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateInviteUrlHeaders()
        return await self.create_invite_url_with_options_async(request, headers, runtime)

    def create_invite_url_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateInviteUrlRequest,
        headers: dingtalkedu__1__0_models.CreateInviteUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateInviteUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.target_operator):
            body['targetOperator'] = request.target_operator
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
            dingtalkedu__1__0_models.CreateInviteUrlResponse(),
            self.do_roarequest('CreateInviteUrl', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/remoteClasses/orgRelations/inviteUrls', 'json', req, runtime)
        )

    async def create_invite_url_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateInviteUrlRequest,
        headers: dingtalkedu__1__0_models.CreateInviteUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateInviteUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.target_operator):
            body['targetOperator'] = request.target_operator
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
            dingtalkedu__1__0_models.CreateInviteUrlResponse(),
            await self.do_roarequest_async('CreateInviteUrl', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/remoteClasses/orgRelations/inviteUrls', 'json', req, runtime)
        )

    def create_item(
        self,
        request: dingtalkedu__1__0_models.CreateItemRequest,
    ) -> dingtalkedu__1__0_models.CreateItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateItemHeaders()
        return self.create_item_with_options(request, headers, runtime)

    async def create_item_async(
        self,
        request: dingtalkedu__1__0_models.CreateItemRequest,
    ) -> dingtalkedu__1__0_models.CreateItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateItemHeaders()
        return await self.create_item_with_options_async(request, headers, runtime)

    def create_item_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateItemRequest,
        headers: dingtalkedu__1__0_models.CreateItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.effect_type):
            body['effectType'] = request.effect_type
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.opt_user):
            body['optUser'] = request.opt_user
        if not UtilClient.is_unset(request.period_type):
            body['periodType'] = request.period_type
        if not UtilClient.is_unset(request.price):
            body['price'] = request.price
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.CreateItemResponse(),
            self.do_roarequest('CreateItem', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/items', 'json', req, runtime)
        )

    async def create_item_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateItemRequest,
        headers: dingtalkedu__1__0_models.CreateItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.effect_type):
            body['effectType'] = request.effect_type
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.opt_user):
            body['optUser'] = request.opt_user
        if not UtilClient.is_unset(request.period_type):
            body['periodType'] = request.period_type
        if not UtilClient.is_unset(request.price):
            body['price'] = request.price
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.CreateItemResponse(),
            await self.do_roarequest_async('CreateItem', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/items', 'json', req, runtime)
        )

    def create_order(
        self,
        request: dingtalkedu__1__0_models.CreateOrderRequest,
    ) -> dingtalkedu__1__0_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateOrderHeaders()
        return self.create_order_with_options(request, headers, runtime)

    async def create_order_async(
        self,
        request: dingtalkedu__1__0_models.CreateOrderRequest,
    ) -> dingtalkedu__1__0_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateOrderHeaders()
        return await self.create_order_with_options_async(request, headers, runtime)

    def create_order_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateOrderRequest,
        headers: dingtalkedu__1__0_models.CreateOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.detail_list):
            body['detailList'] = request.detail_list
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.ftoken):
            body['ftoken'] = request.ftoken
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.terminal_params):
            body['terminalParams'] = request.terminal_params
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.CreateOrderResponse(),
            self.do_roarequest('CreateOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders', 'json', req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateOrderRequest,
        headers: dingtalkedu__1__0_models.CreateOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.detail_list):
            body['detailList'] = request.detail_list
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.ftoken):
            body['ftoken'] = request.ftoken
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.terminal_params):
            body['terminalParams'] = request.terminal_params
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.CreateOrderResponse(),
            await self.do_roarequest_async('CreateOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders', 'json', req, runtime)
        )

    def create_order_flow(
        self,
        request: dingtalkedu__1__0_models.CreateOrderFlowRequest,
    ) -> dingtalkedu__1__0_models.CreateOrderFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateOrderFlowHeaders()
        return self.create_order_flow_with_options(request, headers, runtime)

    async def create_order_flow_async(
        self,
        request: dingtalkedu__1__0_models.CreateOrderFlowRequest,
    ) -> dingtalkedu__1__0_models.CreateOrderFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateOrderFlowHeaders()
        return await self.create_order_flow_with_options_async(request, headers, runtime)

    def create_order_flow_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateOrderFlowRequest,
        headers: dingtalkedu__1__0_models.CreateOrderFlowHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateOrderFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.alipay_uid):
            body['alipayUid'] = request.alipay_uid
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.detail_list):
            body['detailList'] = request.detail_list
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
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
            dingtalkedu__1__0_models.CreateOrderFlowResponse(),
            self.do_roarequest('CreateOrderFlow', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/flows', 'json', req, runtime)
        )

    async def create_order_flow_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateOrderFlowRequest,
        headers: dingtalkedu__1__0_models.CreateOrderFlowHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateOrderFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_amount):
            body['actualAmount'] = request.actual_amount
        if not UtilClient.is_unset(request.alipay_uid):
            body['alipayUid'] = request.alipay_uid
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.detail_list):
            body['detailList'] = request.detail_list
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
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
            dingtalkedu__1__0_models.CreateOrderFlowResponse(),
            await self.do_roarequest_async('CreateOrderFlow', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/flows', 'json', req, runtime)
        )

    def create_physical_classroom(
        self,
        request: dingtalkedu__1__0_models.CreatePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.CreatePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreatePhysicalClassroomHeaders()
        return self.create_physical_classroom_with_options(request, headers, runtime)

    async def create_physical_classroom_async(
        self,
        request: dingtalkedu__1__0_models.CreatePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.CreatePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreatePhysicalClassroomHeaders()
        return await self.create_physical_classroom_with_options_async(request, headers, runtime)

    def create_physical_classroom_with_options(
        self,
        request: dingtalkedu__1__0_models.CreatePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.CreatePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreatePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.classroom_building):
            body['classroomBuilding'] = request.classroom_building
        if not UtilClient.is_unset(request.classroom_campus):
            body['classroomCampus'] = request.classroom_campus
        if not UtilClient.is_unset(request.classroom_floor):
            body['classroomFloor'] = request.classroom_floor
        if not UtilClient.is_unset(request.classroom_name):
            body['classroomName'] = request.classroom_name
        if not UtilClient.is_unset(request.classroom_number):
            body['classroomNumber'] = request.classroom_number
        if not UtilClient.is_unset(request.direct_broadcast):
            body['directBroadcast'] = request.direct_broadcast
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.CreatePhysicalClassroomResponse(),
            self.do_roarequest('CreatePhysicalClassroom', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    async def create_physical_classroom_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreatePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.CreatePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreatePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.classroom_building):
            body['classroomBuilding'] = request.classroom_building
        if not UtilClient.is_unset(request.classroom_campus):
            body['classroomCampus'] = request.classroom_campus
        if not UtilClient.is_unset(request.classroom_floor):
            body['classroomFloor'] = request.classroom_floor
        if not UtilClient.is_unset(request.classroom_name):
            body['classroomName'] = request.classroom_name
        if not UtilClient.is_unset(request.classroom_number):
            body['classroomNumber'] = request.classroom_number
        if not UtilClient.is_unset(request.direct_broadcast):
            body['directBroadcast'] = request.direct_broadcast
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.CreatePhysicalClassroomResponse(),
            await self.do_roarequest_async('CreatePhysicalClassroom', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    def create_refund_flow(
        self,
        request: dingtalkedu__1__0_models.CreateRefundFlowRequest,
    ) -> dingtalkedu__1__0_models.CreateRefundFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateRefundFlowHeaders()
        return self.create_refund_flow_with_options(request, headers, runtime)

    async def create_refund_flow_async(
        self,
        request: dingtalkedu__1__0_models.CreateRefundFlowRequest,
    ) -> dingtalkedu__1__0_models.CreateRefundFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateRefundFlowHeaders()
        return await self.create_refund_flow_with_options_async(request, headers, runtime)

    def create_refund_flow_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateRefundFlowRequest,
        headers: dingtalkedu__1__0_models.CreateRefundFlowHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateRefundFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_name):
            body['operatorName'] = request.operator_name
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkedu__1__0_models.CreateRefundFlowResponse(),
            self.do_roarequest('CreateRefundFlow', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/refunds/flows', 'json', req, runtime)
        )

    async def create_refund_flow_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateRefundFlowRequest,
        headers: dingtalkedu__1__0_models.CreateRefundFlowHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateRefundFlowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_name):
            body['operatorName'] = request.operator_name
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
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
            dingtalkedu__1__0_models.CreateRefundFlowResponse(),
            await self.do_roarequest_async('CreateRefundFlow', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/refunds/flows', 'json', req, runtime)
        )

    def create_remote_class_course(
        self,
        request: dingtalkedu__1__0_models.CreateRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.CreateRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateRemoteClassCourseHeaders()
        return self.create_remote_class_course_with_options(request, headers, runtime)

    async def create_remote_class_course_async(
        self,
        request: dingtalkedu__1__0_models.CreateRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.CreateRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateRemoteClassCourseHeaders()
        return await self.create_remote_class_course_with_options_async(request, headers, runtime)

    def create_remote_class_course_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.CreateRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attend_participants):
            body['attendParticipants'] = request.attend_participants
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.teaching_participant):
            body['teachingParticipant'] = request.teaching_participant
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
            dingtalkedu__1__0_models.CreateRemoteClassCourseResponse(),
            self.do_roarequest('CreateRemoteClassCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    async def create_remote_class_course_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.CreateRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attend_participants):
            body['attendParticipants'] = request.attend_participants
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.teaching_participant):
            body['teachingParticipant'] = request.teaching_participant
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
            dingtalkedu__1__0_models.CreateRemoteClassCourseResponse(),
            await self.do_roarequest_async('CreateRemoteClassCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    def create_section_config(
        self,
        request: dingtalkedu__1__0_models.CreateSectionConfigRequest,
    ) -> dingtalkedu__1__0_models.CreateSectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateSectionConfigHeaders()
        return self.create_section_config_with_options(request, headers, runtime)

    async def create_section_config_async(
        self,
        request: dingtalkedu__1__0_models.CreateSectionConfigRequest,
    ) -> dingtalkedu__1__0_models.CreateSectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateSectionConfigHeaders()
        return await self.create_section_config_with_options_async(request, headers, runtime)

    def create_section_config_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateSectionConfigRequest,
        headers: dingtalkedu__1__0_models.CreateSectionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateSectionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.section_configs):
            body['sectionConfigs'] = request.section_configs
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
            dingtalkedu__1__0_models.CreateSectionConfigResponse(),
            self.do_roarequest('CreateSectionConfig', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/sectionConfigs', 'json', req, runtime)
        )

    async def create_section_config_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateSectionConfigRequest,
        headers: dingtalkedu__1__0_models.CreateSectionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateSectionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.section_configs):
            body['sectionConfigs'] = request.section_configs
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
            dingtalkedu__1__0_models.CreateSectionConfigResponse(),
            await self.do_roarequest_async('CreateSectionConfig', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/sectionConfigs', 'json', req, runtime)
        )

    def create_token(
        self,
        request: dingtalkedu__1__0_models.CreateTokenRequest,
    ) -> dingtalkedu__1__0_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateTokenHeaders()
        return self.create_token_with_options(request, headers, runtime)

    async def create_token_async(
        self,
        request: dingtalkedu__1__0_models.CreateTokenRequest,
    ) -> dingtalkedu__1__0_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateTokenHeaders()
        return await self.create_token_with_options_async(request, headers, runtime)

    def create_token_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateTokenRequest,
        headers: dingtalkedu__1__0_models.CreateTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.CreateTokenResponse(),
            self.do_roarequest('CreateToken', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/tokens', 'json', req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateTokenRequest,
        headers: dingtalkedu__1__0_models.CreateTokenHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.CreateTokenResponse(),
            await self.do_roarequest_async('CreateToken', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/tokens', 'json', req, runtime)
        )

    def create_university_course_group(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityCourseGroupHeaders()
        return self.create_university_course_group_with_options(request, headers, runtime)

    async def create_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityCourseGroupHeaders()
        return await self.create_university_course_group_with_options_async(request, headers, runtime)

    def create_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_introduce):
            body['courseGroupIntroduce'] = request.course_group_introduce
        if not UtilClient.is_unset(request.course_group_name):
            body['courseGroupName'] = request.course_group_name
        if not UtilClient.is_unset(request.courser_group_item_models):
            body['courserGroupItemModels'] = request.courser_group_item_models
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_course_group_code):
            body['isvCourseGroupCode'] = request.isv_course_group_code
        if not UtilClient.is_unset(request.period_code):
            body['periodCode'] = request.period_code
        if not UtilClient.is_unset(request.school_year):
            body['schoolYear'] = request.school_year
        if not UtilClient.is_unset(request.semester):
            body['semester'] = request.semester
        if not UtilClient.is_unset(request.subject_name):
            body['subjectName'] = request.subject_name
        if not UtilClient.is_unset(request.teacher_infos):
            body['teacherInfos'] = request.teacher_infos
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
            dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse(),
            self.do_roarequest('CreateUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    async def create_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_introduce):
            body['courseGroupIntroduce'] = request.course_group_introduce
        if not UtilClient.is_unset(request.course_group_name):
            body['courseGroupName'] = request.course_group_name
        if not UtilClient.is_unset(request.courser_group_item_models):
            body['courserGroupItemModels'] = request.courser_group_item_models
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_course_group_code):
            body['isvCourseGroupCode'] = request.isv_course_group_code
        if not UtilClient.is_unset(request.period_code):
            body['periodCode'] = request.period_code
        if not UtilClient.is_unset(request.school_year):
            body['schoolYear'] = request.school_year
        if not UtilClient.is_unset(request.semester):
            body['semester'] = request.semester
        if not UtilClient.is_unset(request.subject_name):
            body['subjectName'] = request.subject_name
        if not UtilClient.is_unset(request.teacher_infos):
            body['teacherInfos'] = request.teacher_infos
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
            dingtalkedu__1__0_models.CreateUniversityCourseGroupResponse(),
            await self.do_roarequest_async('CreateUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    def create_university_student(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityStudentRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityStudentHeaders()
        return self.create_university_student_with_options(request, headers, runtime)

    async def create_university_student_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityStudentRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityStudentHeaders()
        return await self.create_university_student_with_options_async(request, headers, runtime)

    def create_university_student_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityStudentRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityStudentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.class_id):
            body['classId'] = request.class_id
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.identity_number):
            body['identityNumber'] = request.identity_number
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.student_number):
            body['studentNumber'] = request.student_number
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
            dingtalkedu__1__0_models.CreateUniversityStudentResponse(),
            self.do_roarequest('CreateUniversityStudent', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/students', 'json', req, runtime)
        )

    async def create_university_student_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityStudentRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityStudentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.class_id):
            body['classId'] = request.class_id
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.identity_number):
            body['identityNumber'] = request.identity_number
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.student_number):
            body['studentNumber'] = request.student_number
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
            dingtalkedu__1__0_models.CreateUniversityStudentResponse(),
            await self.do_roarequest_async('CreateUniversityStudent', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/students', 'json', req, runtime)
        )

    def create_university_teacher(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityTeacherRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityTeacherHeaders()
        return self.create_university_teacher_with_options(request, headers, runtime)

    async def create_university_teacher_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityTeacherRequest,
    ) -> dingtalkedu__1__0_models.CreateUniversityTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.CreateUniversityTeacherHeaders()
        return await self.create_university_teacher_with_options_async(request, headers, runtime)

    def create_university_teacher_with_options(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityTeacherRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityTeacherResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_id):
            body['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.teacher_user_id):
            body['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.CreateUniversityTeacherResponse(),
            self.do_roarequest('CreateUniversityTeacher', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/teachers', 'json', req, runtime)
        )

    async def create_university_teacher_with_options_async(
        self,
        request: dingtalkedu__1__0_models.CreateUniversityTeacherRequest,
        headers: dingtalkedu__1__0_models.CreateUniversityTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.CreateUniversityTeacherResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.class_id):
            body['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.teacher_user_id):
            body['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.CreateUniversityTeacherResponse(),
            await self.do_roarequest_async('CreateUniversityTeacher', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/teachers', 'json', req, runtime)
        )

    def delete_dept(
        self,
        dept_id: str,
        request: dingtalkedu__1__0_models.DeleteDeptRequest,
    ) -> dingtalkedu__1__0_models.DeleteDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteDeptHeaders()
        return self.delete_dept_with_options(dept_id, request, headers, runtime)

    async def delete_dept_async(
        self,
        dept_id: str,
        request: dingtalkedu__1__0_models.DeleteDeptRequest,
    ) -> dingtalkedu__1__0_models.DeleteDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteDeptHeaders()
        return await self.delete_dept_with_options_async(dept_id, request, headers, runtime)

    def delete_dept_with_options(
        self,
        dept_id: str,
        request: dingtalkedu__1__0_models.DeleteDeptRequest,
        headers: dingtalkedu__1__0_models.DeleteDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteDeptResponse(),
            self.do_roarequest('DeleteDept', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/depts/{dept_id}', 'json', req, runtime)
        )

    async def delete_dept_with_options_async(
        self,
        dept_id: str,
        request: dingtalkedu__1__0_models.DeleteDeptRequest,
        headers: dingtalkedu__1__0_models.DeleteDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteDeptResponse(),
            await self.do_roarequest_async('DeleteDept', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/depts/{dept_id}', 'json', req, runtime)
        )

    def delete_device_org(
        self,
        request: dingtalkedu__1__0_models.DeleteDeviceOrgRequest,
    ) -> dingtalkedu__1__0_models.DeleteDeviceOrgResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteDeviceOrgHeaders()
        return self.delete_device_org_with_options(request, headers, runtime)

    async def delete_device_org_async(
        self,
        request: dingtalkedu__1__0_models.DeleteDeviceOrgRequest,
    ) -> dingtalkedu__1__0_models.DeleteDeviceOrgResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteDeviceOrgHeaders()
        return await self.delete_device_org_with_options_async(request, headers, runtime)

    def delete_device_org_with_options(
        self,
        request: dingtalkedu__1__0_models.DeleteDeviceOrgRequest,
        headers: dingtalkedu__1__0_models.DeleteDeviceOrgHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteDeviceOrgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
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
            dingtalkedu__1__0_models.DeleteDeviceOrgResponse(),
            self.do_roarequest('DeleteDeviceOrg', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/deviceOrgs', 'json', req, runtime)
        )

    async def delete_device_org_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeleteDeviceOrgRequest,
        headers: dingtalkedu__1__0_models.DeleteDeviceOrgHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteDeviceOrgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
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
            dingtalkedu__1__0_models.DeleteDeviceOrgResponse(),
            await self.do_roarequest_async('DeleteDeviceOrg', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/deviceOrgs', 'json', req, runtime)
        )

    def delete_guardian(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteGuardianRequest,
    ) -> dingtalkedu__1__0_models.DeleteGuardianResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteGuardianHeaders()
        return self.delete_guardian_with_options(class_id, user_id, request, headers, runtime)

    async def delete_guardian_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteGuardianRequest,
    ) -> dingtalkedu__1__0_models.DeleteGuardianResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteGuardianHeaders()
        return await self.delete_guardian_with_options_async(class_id, user_id, request, headers, runtime)

    def delete_guardian_with_options(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteGuardianRequest,
        headers: dingtalkedu__1__0_models.DeleteGuardianHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteGuardianResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.stu_id):
            query['stuId'] = request.stu_id
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
            dingtalkedu__1__0_models.DeleteGuardianResponse(),
            self.do_roarequest('DeleteGuardian', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/guardians/{user_id}', 'json', req, runtime)
        )

    async def delete_guardian_with_options_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteGuardianRequest,
        headers: dingtalkedu__1__0_models.DeleteGuardianHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteGuardianResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.stu_id):
            query['stuId'] = request.stu_id
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
            dingtalkedu__1__0_models.DeleteGuardianResponse(),
            await self.do_roarequest_async('DeleteGuardian', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/guardians/{user_id}', 'json', req, runtime)
        )

    def delete_org_relation(
        self,
        request: dingtalkedu__1__0_models.DeleteOrgRelationRequest,
    ) -> dingtalkedu__1__0_models.DeleteOrgRelationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteOrgRelationHeaders()
        return self.delete_org_relation_with_options(request, headers, runtime)

    async def delete_org_relation_async(
        self,
        request: dingtalkedu__1__0_models.DeleteOrgRelationRequest,
    ) -> dingtalkedu__1__0_models.DeleteOrgRelationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteOrgRelationHeaders()
        return await self.delete_org_relation_with_options_async(request, headers, runtime)

    def delete_org_relation_with_options(
        self,
        request: dingtalkedu__1__0_models.DeleteOrgRelationRequest,
        headers: dingtalkedu__1__0_models.DeleteOrgRelationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteOrgRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
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
            dingtalkedu__1__0_models.DeleteOrgRelationResponse(),
            self.do_roarequest('DeleteOrgRelation', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/orgRelations', 'json', req, runtime)
        )

    async def delete_org_relation_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeleteOrgRelationRequest,
        headers: dingtalkedu__1__0_models.DeleteOrgRelationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteOrgRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
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
            dingtalkedu__1__0_models.DeleteOrgRelationResponse(),
            await self.do_roarequest_async('DeleteOrgRelation', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/orgRelations', 'json', req, runtime)
        )

    def delete_physical_classroom(
        self,
        request: dingtalkedu__1__0_models.DeletePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.DeletePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeletePhysicalClassroomHeaders()
        return self.delete_physical_classroom_with_options(request, headers, runtime)

    async def delete_physical_classroom_async(
        self,
        request: dingtalkedu__1__0_models.DeletePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.DeletePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeletePhysicalClassroomHeaders()
        return await self.delete_physical_classroom_with_options_async(request, headers, runtime)

    def delete_physical_classroom_with_options(
        self,
        request: dingtalkedu__1__0_models.DeletePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.DeletePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeletePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classroom_id):
            query['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.DeletePhysicalClassroomResponse(),
            self.do_roarequest('DeletePhysicalClassroom', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    async def delete_physical_classroom_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeletePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.DeletePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeletePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classroom_id):
            query['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.DeletePhysicalClassroomResponse(),
            await self.do_roarequest_async('DeletePhysicalClassroom', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    def delete_remote_class_course(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.DeleteRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteRemoteClassCourseHeaders()
        return self.delete_remote_class_course_with_options(course_code, request, headers, runtime)

    async def delete_remote_class_course_async(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.DeleteRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteRemoteClassCourseHeaders()
        return await self.delete_remote_class_course_with_options_async(course_code, request, headers, runtime)

    def delete_remote_class_course_with_options(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.DeleteRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.DeleteRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        course_code = OpenApiUtilClient.get_encode_param(course_code)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
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
            dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse(),
            self.do_roarequest('DeleteRemoteClassCourse', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/courses/{course_code}', 'json', req, runtime)
        )

    async def delete_remote_class_course_with_options_async(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.DeleteRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.DeleteRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        course_code = OpenApiUtilClient.get_encode_param(course_code)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
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
            dingtalkedu__1__0_models.DeleteRemoteClassCourseResponse(),
            await self.do_roarequest_async('DeleteRemoteClassCourse', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/remoteClasses/courses/{course_code}', 'json', req, runtime)
        )

    def delete_student(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteStudentRequest,
    ) -> dingtalkedu__1__0_models.DeleteStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteStudentHeaders()
        return self.delete_student_with_options(class_id, user_id, request, headers, runtime)

    async def delete_student_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteStudentRequest,
    ) -> dingtalkedu__1__0_models.DeleteStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteStudentHeaders()
        return await self.delete_student_with_options_async(class_id, user_id, request, headers, runtime)

    def delete_student_with_options(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteStudentRequest,
        headers: dingtalkedu__1__0_models.DeleteStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteStudentResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteStudentResponse(),
            self.do_roarequest('DeleteStudent', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/students/{user_id}', 'json', req, runtime)
        )

    async def delete_student_with_options_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteStudentRequest,
        headers: dingtalkedu__1__0_models.DeleteStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteStudentResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteStudentResponse(),
            await self.do_roarequest_async('DeleteStudent', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/students/{user_id}', 'json', req, runtime)
        )

    def delete_teacher(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteTeacherRequest,
    ) -> dingtalkedu__1__0_models.DeleteTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteTeacherHeaders()
        return self.delete_teacher_with_options(class_id, user_id, request, headers, runtime)

    async def delete_teacher_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteTeacherRequest,
    ) -> dingtalkedu__1__0_models.DeleteTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteTeacherHeaders()
        return await self.delete_teacher_with_options_async(class_id, user_id, request, headers, runtime)

    def delete_teacher_with_options(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteTeacherRequest,
        headers: dingtalkedu__1__0_models.DeleteTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteTeacherResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.adviser):
            query['adviser'] = request.adviser
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteTeacherResponse(),
            self.do_roarequest('DeleteTeacher', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/teachers/{user_id}', 'json', req, runtime)
        )

    async def delete_teacher_with_options_async(
        self,
        class_id: str,
        user_id: str,
        request: dingtalkedu__1__0_models.DeleteTeacherRequest,
        headers: dingtalkedu__1__0_models.DeleteTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteTeacherResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.adviser):
            query['adviser'] = request.adviser
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.DeleteTeacherResponse(),
            await self.do_roarequest_async('DeleteTeacher', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/classes/{class_id}/teachers/{user_id}', 'json', req, runtime)
        )

    def delete_university_course_group(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityCourseGroupHeaders()
        return self.delete_university_course_group_with_options(request, headers, runtime)

    async def delete_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityCourseGroupHeaders()
        return await self.delete_university_course_group_with_options_async(request, headers, runtime)

    def delete_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_group_code):
            query['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse(),
            self.do_roarequest('DeleteUniversityCourseGroup', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    async def delete_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_group_code):
            query['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityCourseGroupResponse(),
            await self.do_roarequest_async('DeleteUniversityCourseGroup', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    def delete_university_student(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityStudentRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityStudentHeaders()
        return self.delete_university_student_with_options(request, headers, runtime)

    async def delete_university_student_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityStudentRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityStudentHeaders()
        return await self.delete_university_student_with_options_async(request, headers, runtime)

    def delete_university_student_with_options(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityStudentRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityStudentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_id):
            query['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.student_user_id):
            query['studentUserId'] = request.student_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityStudentResponse(),
            self.do_roarequest('DeleteUniversityStudent', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/students', 'json', req, runtime)
        )

    async def delete_university_student_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityStudentRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityStudentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_id):
            query['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.student_user_id):
            query['studentUserId'] = request.student_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityStudentResponse(),
            await self.do_roarequest_async('DeleteUniversityStudent', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/students', 'json', req, runtime)
        )

    def delete_university_teacher(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityTeacherRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityTeacherHeaders()
        return self.delete_university_teacher_with_options(request, headers, runtime)

    async def delete_university_teacher_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityTeacherRequest,
    ) -> dingtalkedu__1__0_models.DeleteUniversityTeacherResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeleteUniversityTeacherHeaders()
        return await self.delete_university_teacher_with_options_async(request, headers, runtime)

    def delete_university_teacher_with_options(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityTeacherRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityTeacherResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_id):
            query['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role):
            query['role'] = request.role
        if not UtilClient.is_unset(request.teacher_user_id):
            query['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityTeacherResponse(),
            self.do_roarequest('DeleteUniversityTeacher', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/teachers', 'json', req, runtime)
        )

    async def delete_university_teacher_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeleteUniversityTeacherRequest,
        headers: dingtalkedu__1__0_models.DeleteUniversityTeacherHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeleteUniversityTeacherResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_id):
            query['classId'] = request.class_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role):
            query['role'] = request.role
        if not UtilClient.is_unset(request.teacher_user_id):
            query['teacherUserId'] = request.teacher_user_id
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
            dingtalkedu__1__0_models.DeleteUniversityTeacherResponse(),
            await self.do_roarequest_async('DeleteUniversityTeacher', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/universities/teachers', 'json', req, runtime)
        )

    def device_heartbeat(
        self,
        request: dingtalkedu__1__0_models.DeviceHeartbeatRequest,
    ) -> dingtalkedu__1__0_models.DeviceHeartbeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeviceHeartbeatHeaders()
        return self.device_heartbeat_with_options(request, headers, runtime)

    async def device_heartbeat_async(
        self,
        request: dingtalkedu__1__0_models.DeviceHeartbeatRequest,
    ) -> dingtalkedu__1__0_models.DeviceHeartbeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.DeviceHeartbeatHeaders()
        return await self.device_heartbeat_with_options_async(request, headers, runtime)

    def device_heartbeat_with_options(
        self,
        request: dingtalkedu__1__0_models.DeviceHeartbeatRequest,
        headers: dingtalkedu__1__0_models.DeviceHeartbeatHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeviceHeartbeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.DeviceHeartbeatResponse(),
            self.do_roarequest('DeviceHeartbeat', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/heartbeats/report', 'json', req, runtime)
        )

    async def device_heartbeat_with_options_async(
        self,
        request: dingtalkedu__1__0_models.DeviceHeartbeatRequest,
        headers: dingtalkedu__1__0_models.DeviceHeartbeatHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.DeviceHeartbeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.DeviceHeartbeatResponse(),
            await self.do_roarequest_async('DeviceHeartbeat', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/heartbeats/report', 'json', req, runtime)
        )

    def edu_teacher_list(
        self,
        request: dingtalkedu__1__0_models.EduTeacherListRequest,
    ) -> dingtalkedu__1__0_models.EduTeacherListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.EduTeacherListHeaders()
        return self.edu_teacher_list_with_options(request, headers, runtime)

    async def edu_teacher_list_async(
        self,
        request: dingtalkedu__1__0_models.EduTeacherListRequest,
    ) -> dingtalkedu__1__0_models.EduTeacherListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.EduTeacherListHeaders()
        return await self.edu_teacher_list_with_options_async(request, headers, runtime)

    def edu_teacher_list_with_options(
        self,
        request: dingtalkedu__1__0_models.EduTeacherListRequest,
        headers: dingtalkedu__1__0_models.EduTeacherListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.EduTeacherListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.EduTeacherListResponse(),
            self.do_roarequest('EduTeacherList', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/teachers', 'json', req, runtime)
        )

    async def edu_teacher_list_with_options_async(
        self,
        request: dingtalkedu__1__0_models.EduTeacherListRequest,
        headers: dingtalkedu__1__0_models.EduTeacherListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.EduTeacherListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.EduTeacherListResponse(),
            await self.do_roarequest_async('EduTeacherList', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/teachers', 'json', req, runtime)
        )

    def end_course(
        self,
        request: dingtalkedu__1__0_models.EndCourseRequest,
    ) -> dingtalkedu__1__0_models.EndCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.EndCourseHeaders()
        return self.end_course_with_options(request, headers, runtime)

    async def end_course_async(
        self,
        request: dingtalkedu__1__0_models.EndCourseRequest,
    ) -> dingtalkedu__1__0_models.EndCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.EndCourseHeaders()
        return await self.end_course_with_options_async(request, headers, runtime)

    def end_course_with_options(
        self,
        request: dingtalkedu__1__0_models.EndCourseRequest,
        headers: dingtalkedu__1__0_models.EndCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.EndCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_play_info_list):
            body['livePlayInfoList'] = request.live_play_info_list
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
            dingtalkedu__1__0_models.EndCourseResponse(),
            self.do_roarequest('EndCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/end', 'json', req, runtime)
        )

    async def end_course_with_options_async(
        self,
        request: dingtalkedu__1__0_models.EndCourseRequest,
        headers: dingtalkedu__1__0_models.EndCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.EndCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_play_info_list):
            body['livePlayInfoList'] = request.live_play_info_list
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
            dingtalkedu__1__0_models.EndCourseResponse(),
            await self.do_roarequest_async('EndCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/end', 'json', req, runtime)
        )

    def get_default_child(self) -> dingtalkedu__1__0_models.GetDefaultChildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetDefaultChildHeaders()
        return self.get_default_child_with_options(headers, runtime)

    async def get_default_child_async(self) -> dingtalkedu__1__0_models.GetDefaultChildResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetDefaultChildHeaders()
        return await self.get_default_child_with_options_async(headers, runtime)

    def get_default_child_with_options(
        self,
        headers: dingtalkedu__1__0_models.GetDefaultChildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetDefaultChildResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetDefaultChildResponse(),
            self.do_roarequest('GetDefaultChild', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/defaultChildren', 'json', req, runtime)
        )

    async def get_default_child_with_options_async(
        self,
        headers: dingtalkedu__1__0_models.GetDefaultChildHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetDefaultChildResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetDefaultChildResponse(),
            await self.do_roarequest_async('GetDefaultChild', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/defaultChildren', 'json', req, runtime)
        )

    def get_open_course_detail(
        self,
        course_id: str,
    ) -> dingtalkedu__1__0_models.GetOpenCourseDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetOpenCourseDetailHeaders()
        return self.get_open_course_detail_with_options(course_id, headers, runtime)

    async def get_open_course_detail_async(
        self,
        course_id: str,
    ) -> dingtalkedu__1__0_models.GetOpenCourseDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetOpenCourseDetailHeaders()
        return await self.get_open_course_detail_with_options_async(course_id, headers, runtime)

    def get_open_course_detail_with_options(
        self,
        course_id: str,
        headers: dingtalkedu__1__0_models.GetOpenCourseDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetOpenCourseDetailResponse:
        course_id = OpenApiUtilClient.get_encode_param(course_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetOpenCourseDetailResponse(),
            self.do_roarequest('GetOpenCourseDetail', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/openCourse/{course_id}', 'json', req, runtime)
        )

    async def get_open_course_detail_with_options_async(
        self,
        course_id: str,
        headers: dingtalkedu__1__0_models.GetOpenCourseDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetOpenCourseDetailResponse:
        course_id = OpenApiUtilClient.get_encode_param(course_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetOpenCourseDetailResponse(),
            await self.do_roarequest_async('GetOpenCourseDetail', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/openCourse/{course_id}', 'json', req, runtime)
        )

    def get_open_courses(
        self,
        request: dingtalkedu__1__0_models.GetOpenCoursesRequest,
    ) -> dingtalkedu__1__0_models.GetOpenCoursesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetOpenCoursesHeaders()
        return self.get_open_courses_with_options(request, headers, runtime)

    async def get_open_courses_async(
        self,
        request: dingtalkedu__1__0_models.GetOpenCoursesRequest,
    ) -> dingtalkedu__1__0_models.GetOpenCoursesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetOpenCoursesHeaders()
        return await self.get_open_courses_with_options_async(request, headers, runtime)

    def get_open_courses_with_options(
        self,
        request: dingtalkedu__1__0_models.GetOpenCoursesRequest,
        headers: dingtalkedu__1__0_models.GetOpenCoursesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetOpenCoursesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.GetOpenCoursesResponse(),
            self.do_roarequest('GetOpenCourses', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/openCourses', 'json', req, runtime)
        )

    async def get_open_courses_with_options_async(
        self,
        request: dingtalkedu__1__0_models.GetOpenCoursesRequest,
        headers: dingtalkedu__1__0_models.GetOpenCoursesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetOpenCoursesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.GetOpenCoursesResponse(),
            await self.do_roarequest_async('GetOpenCourses', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/openCourses', 'json', req, runtime)
        )

    def get_remote_class_course(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.GetRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.GetRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetRemoteClassCourseHeaders()
        return self.get_remote_class_course_with_options(course_code, request, headers, runtime)

    async def get_remote_class_course_async(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.GetRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.GetRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetRemoteClassCourseHeaders()
        return await self.get_remote_class_course_with_options_async(course_code, request, headers, runtime)

    def get_remote_class_course_with_options(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.GetRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.GetRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        course_code = OpenApiUtilClient.get_encode_param(course_code)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.GetRemoteClassCourseResponse(),
            self.do_roarequest('GetRemoteClassCourse', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/courses/{course_code}', 'json', req, runtime)
        )

    async def get_remote_class_course_with_options_async(
        self,
        course_code: str,
        request: dingtalkedu__1__0_models.GetRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.GetRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        course_code = OpenApiUtilClient.get_encode_param(course_code)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.GetRemoteClassCourseResponse(),
            await self.do_roarequest_async('GetRemoteClassCourse', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/courses/{course_code}', 'json', req, runtime)
        )

    def get_share_role_members(
        self,
        share_role_code: str,
    ) -> dingtalkedu__1__0_models.GetShareRoleMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetShareRoleMembersHeaders()
        return self.get_share_role_members_with_options(share_role_code, headers, runtime)

    async def get_share_role_members_async(
        self,
        share_role_code: str,
    ) -> dingtalkedu__1__0_models.GetShareRoleMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetShareRoleMembersHeaders()
        return await self.get_share_role_members_with_options_async(share_role_code, headers, runtime)

    def get_share_role_members_with_options(
        self,
        share_role_code: str,
        headers: dingtalkedu__1__0_models.GetShareRoleMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetShareRoleMembersResponse:
        share_role_code = OpenApiUtilClient.get_encode_param(share_role_code)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetShareRoleMembersResponse(),
            self.do_roarequest('GetShareRoleMembers', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/shareRoles/{share_role_code}/members', 'json', req, runtime)
        )

    async def get_share_role_members_with_options_async(
        self,
        share_role_code: str,
        headers: dingtalkedu__1__0_models.GetShareRoleMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetShareRoleMembersResponse:
        share_role_code = OpenApiUtilClient.get_encode_param(share_role_code)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetShareRoleMembersResponse(),
            await self.do_roarequest_async('GetShareRoleMembers', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/shareRoles/{share_role_code}/members', 'json', req, runtime)
        )

    def get_share_roles(self) -> dingtalkedu__1__0_models.GetShareRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetShareRolesHeaders()
        return self.get_share_roles_with_options(headers, runtime)

    async def get_share_roles_async(self) -> dingtalkedu__1__0_models.GetShareRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.GetShareRolesHeaders()
        return await self.get_share_roles_with_options_async(headers, runtime)

    def get_share_roles_with_options(
        self,
        headers: dingtalkedu__1__0_models.GetShareRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetShareRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetShareRolesResponse(),
            self.do_roarequest('GetShareRoles', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/shareRoles', 'json', req, runtime)
        )

    async def get_share_roles_with_options_async(
        self,
        headers: dingtalkedu__1__0_models.GetShareRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.GetShareRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.GetShareRolesResponse(),
            await self.do_roarequest_async('GetShareRoles', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/shareRoles', 'json', req, runtime)
        )

    def init_courses_of_class(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.InitCoursesOfClassRequest,
    ) -> dingtalkedu__1__0_models.InitCoursesOfClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InitCoursesOfClassHeaders()
        return self.init_courses_of_class_with_options(class_id, request, headers, runtime)

    async def init_courses_of_class_async(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.InitCoursesOfClassRequest,
    ) -> dingtalkedu__1__0_models.InitCoursesOfClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InitCoursesOfClassHeaders()
        return await self.init_courses_of_class_with_options_async(class_id, request, headers, runtime)

    def init_courses_of_class_with_options(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.InitCoursesOfClassRequest,
        headers: dingtalkedu__1__0_models.InitCoursesOfClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InitCoursesOfClassResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.courses):
            body['courses'] = request.courses
        if not UtilClient.is_unset(request.section_config):
            body['sectionConfig'] = request.section_config
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
            dingtalkedu__1__0_models.InitCoursesOfClassResponse(),
            self.do_roarequest('InitCoursesOfClass', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/{class_id}/courses/init', 'json', req, runtime)
        )

    async def init_courses_of_class_with_options_async(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.InitCoursesOfClassRequest,
        headers: dingtalkedu__1__0_models.InitCoursesOfClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InitCoursesOfClassResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.courses):
            body['courses'] = request.courses
        if not UtilClient.is_unset(request.section_config):
            body['sectionConfig'] = request.section_config
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
            dingtalkedu__1__0_models.InitCoursesOfClassResponse(),
            await self.do_roarequest_async('InitCoursesOfClass', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/{class_id}/courses/init', 'json', req, runtime)
        )

    def init_device(
        self,
        request: dingtalkedu__1__0_models.InitDeviceRequest,
    ) -> dingtalkedu__1__0_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InitDeviceHeaders()
        return self.init_device_with_options(request, headers, runtime)

    async def init_device_async(
        self,
        request: dingtalkedu__1__0_models.InitDeviceRequest,
    ) -> dingtalkedu__1__0_models.InitDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InitDeviceHeaders()
        return await self.init_device_with_options_async(request, headers, runtime)

    def init_device_with_options(
        self,
        request: dingtalkedu__1__0_models.InitDeviceRequest,
        headers: dingtalkedu__1__0_models.InitDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encrypt_pub_key):
            body['encryptPubKey'] = request.encrypt_pub_key
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.InitDeviceResponse(),
            self.do_roarequest('InitDevice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/devices/init', 'json', req, runtime)
        )

    async def init_device_with_options_async(
        self,
        request: dingtalkedu__1__0_models.InitDeviceRequest,
        headers: dingtalkedu__1__0_models.InitDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InitDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encrypt_pub_key):
            body['encryptPubKey'] = request.encrypt_pub_key
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.InitDeviceResponse(),
            await self.do_roarequest_async('InitDevice', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/devices/init', 'json', req, runtime)
        )

    def insert_section_config(
        self,
        request: dingtalkedu__1__0_models.InsertSectionConfigRequest,
    ) -> dingtalkedu__1__0_models.InsertSectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InsertSectionConfigHeaders()
        return self.insert_section_config_with_options(request, headers, runtime)

    async def insert_section_config_async(
        self,
        request: dingtalkedu__1__0_models.InsertSectionConfigRequest,
    ) -> dingtalkedu__1__0_models.InsertSectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.InsertSectionConfigHeaders()
        return await self.insert_section_config_with_options_async(request, headers, runtime)

    def insert_section_config_with_options(
        self,
        request: dingtalkedu__1__0_models.InsertSectionConfigRequest,
        headers: dingtalkedu__1__0_models.InsertSectionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InsertSectionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.schedule_name):
            body['scheduleName'] = request.schedule_name
        if not UtilClient.is_unset(request.section_models):
            body['sectionModels'] = request.section_models
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
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
            dingtalkedu__1__0_models.InsertSectionConfigResponse(),
            self.do_roarequest('InsertSectionConfig', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/schedules/configs', 'json', req, runtime)
        )

    async def insert_section_config_with_options_async(
        self,
        request: dingtalkedu__1__0_models.InsertSectionConfigRequest,
        headers: dingtalkedu__1__0_models.InsertSectionConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.InsertSectionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.schedule_name):
            body['scheduleName'] = request.schedule_name
        if not UtilClient.is_unset(request.section_models):
            body['sectionModels'] = request.section_models
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
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
            dingtalkedu__1__0_models.InsertSectionConfigResponse(),
            await self.do_roarequest_async('InsertSectionConfig', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/schedules/configs', 'json', req, runtime)
        )

    def list_order(
        self,
        request: dingtalkedu__1__0_models.ListOrderRequest,
    ) -> dingtalkedu__1__0_models.ListOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ListOrderHeaders()
        return self.list_order_with_options(request, headers, runtime)

    async def list_order_async(
        self,
        request: dingtalkedu__1__0_models.ListOrderRequest,
    ) -> dingtalkedu__1__0_models.ListOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ListOrderHeaders()
        return await self.list_order_with_options_async(request, headers, runtime)

    def list_order_with_options(
        self,
        request: dingtalkedu__1__0_models.ListOrderRequest,
        headers: dingtalkedu__1__0_models.ListOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ListOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['createTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['createTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.trade_no):
            body['tradeNo'] = request.trade_no
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
            dingtalkedu__1__0_models.ListOrderResponse(),
            self.do_roarequest('ListOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/query', 'json', req, runtime)
        )

    async def list_order_with_options_async(
        self,
        request: dingtalkedu__1__0_models.ListOrderRequest,
        headers: dingtalkedu__1__0_models.ListOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ListOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['createTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['createTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.merchant_id):
            body['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.trade_no):
            body['tradeNo'] = request.trade_no
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
            dingtalkedu__1__0_models.ListOrderResponse(),
            await self.do_roarequest_async('ListOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/query', 'json', req, runtime)
        )

    def move_student(
        self,
        request: dingtalkedu__1__0_models.MoveStudentRequest,
    ) -> dingtalkedu__1__0_models.MoveStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.MoveStudentHeaders()
        return self.move_student_with_options(request, headers, runtime)

    async def move_student_async(
        self,
        request: dingtalkedu__1__0_models.MoveStudentRequest,
    ) -> dingtalkedu__1__0_models.MoveStudentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.MoveStudentHeaders()
        return await self.move_student_with_options_async(request, headers, runtime)

    def move_student_with_options(
        self,
        request: dingtalkedu__1__0_models.MoveStudentRequest,
        headers: dingtalkedu__1__0_models.MoveStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.MoveStudentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.origin_class_id):
            body['originClassId'] = request.origin_class_id
        if not UtilClient.is_unset(request.target_class_id):
            body['targetClassId'] = request.target_class_id
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
            dingtalkedu__1__0_models.MoveStudentResponse(),
            self.do_roarequest('MoveStudent', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/students/move', 'json', req, runtime)
        )

    async def move_student_with_options_async(
        self,
        request: dingtalkedu__1__0_models.MoveStudentRequest,
        headers: dingtalkedu__1__0_models.MoveStudentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.MoveStudentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator):
            body['operator'] = request.operator
        if not UtilClient.is_unset(request.origin_class_id):
            body['originClassId'] = request.origin_class_id
        if not UtilClient.is_unset(request.target_class_id):
            body['targetClassId'] = request.target_class_id
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
            dingtalkedu__1__0_models.MoveStudentResponse(),
            await self.do_roarequest_async('MoveStudent', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/students/move', 'json', req, runtime)
        )

    def pay_order(
        self,
        request: dingtalkedu__1__0_models.PayOrderRequest,
    ) -> dingtalkedu__1__0_models.PayOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.PayOrderHeaders()
        return self.pay_order_with_options(request, headers, runtime)

    async def pay_order_async(
        self,
        request: dingtalkedu__1__0_models.PayOrderRequest,
    ) -> dingtalkedu__1__0_models.PayOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.PayOrderHeaders()
        return await self.pay_order_with_options_async(request, headers, runtime)

    def pay_order_with_options(
        self,
        request: dingtalkedu__1__0_models.PayOrderRequest,
        headers: dingtalkedu__1__0_models.PayOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.PayOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.PayOrderResponse(),
            self.do_roarequest('PayOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/pay', 'json', req, runtime)
        )

    async def pay_order_with_options_async(
        self,
        request: dingtalkedu__1__0_models.PayOrderRequest,
        headers: dingtalkedu__1__0_models.PayOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.PayOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.PayOrderResponse(),
            await self.do_roarequest_async('PayOrder', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/orders/pay', 'json', req, runtime)
        )

    def polling_confirm_status(
        self,
        request: dingtalkedu__1__0_models.PollingConfirmStatusRequest,
    ) -> dingtalkedu__1__0_models.PollingConfirmStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.PollingConfirmStatusHeaders()
        return self.polling_confirm_status_with_options(request, headers, runtime)

    async def polling_confirm_status_async(
        self,
        request: dingtalkedu__1__0_models.PollingConfirmStatusRequest,
    ) -> dingtalkedu__1__0_models.PollingConfirmStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.PollingConfirmStatusHeaders()
        return await self.polling_confirm_status_with_options_async(request, headers, runtime)

    def polling_confirm_status_with_options(
        self,
        request: dingtalkedu__1__0_models.PollingConfirmStatusRequest,
        headers: dingtalkedu__1__0_models.PollingConfirmStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.PollingConfirmStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_code):
            query['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            query['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            query['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.PollingConfirmStatusResponse(),
            self.do_roarequest('PollingConfirmStatus', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/courses/pollingConfirmStatus', 'json', req, runtime)
        )

    async def polling_confirm_status_with_options_async(
        self,
        request: dingtalkedu__1__0_models.PollingConfirmStatusRequest,
        headers: dingtalkedu__1__0_models.PollingConfirmStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.PollingConfirmStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_code):
            query['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            query['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            query['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.PollingConfirmStatusResponse(),
            await self.do_roarequest_async('PollingConfirmStatus', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/courses/pollingConfirmStatus', 'json', req, runtime)
        )

    def query_all_subjects_from_class_schedule(
        self,
        request: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleRequest,
    ) -> dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleHeaders()
        return self.query_all_subjects_from_class_schedule_with_options(request, headers, runtime)

    async def query_all_subjects_from_class_schedule_async(
        self,
        request: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleRequest,
    ) -> dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleHeaders()
        return await self.query_all_subjects_from_class_schedule_with_options_async(request, headers, runtime)

    def query_all_subjects_from_class_schedule_with_options(
        self,
        tmp_req: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleRequest,
        headers: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.class_ids):
            request.class_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.class_ids, 'classIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.class_ids_shrink):
            query['classIds'] = request.class_ids_shrink
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.period_code):
            query['periodCode'] = request.period_code
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
            dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse(),
            self.do_roarequest('QueryAllSubjectsFromClassSchedule', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/subjects/instances', 'json', req, runtime)
        )

    async def query_all_subjects_from_class_schedule_with_options_async(
        self,
        tmp_req: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleRequest,
        headers: dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.class_ids):
            request.class_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.class_ids, 'classIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.class_ids_shrink):
            query['classIds'] = request.class_ids_shrink
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.period_code):
            query['periodCode'] = request.period_code
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
            dingtalkedu__1__0_models.QueryAllSubjectsFromClassScheduleResponse(),
            await self.do_roarequest_async('QueryAllSubjectsFromClassSchedule', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/subjects/instances', 'json', req, runtime)
        )

    def query_class_schedule(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleHeaders()
        return self.query_class_schedule_with_options(request, headers, runtime)

    async def query_class_schedule_async(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleHeaders()
        return await self.query_class_schedule_with_options_async(request, headers, runtime)

    def query_class_schedule_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscriber_type):
            query['subscriberType'] = request.subscriber_type
        body = {}
        if not UtilClient.is_unset(request.section_index_list):
            body['sectionIndexList'] = request.section_index_list
        if not UtilClient.is_unset(request.subscriber_ids):
            body['subscriberIds'] = request.subscriber_ids
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
            dingtalkedu__1__0_models.QueryClassScheduleResponse(),
            self.do_roarequest('QueryClassSchedule', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/schedules/query', 'json', req, runtime)
        )

    async def query_class_schedule_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscriber_type):
            query['subscriberType'] = request.subscriber_type
        body = {}
        if not UtilClient.is_unset(request.section_index_list):
            body['sectionIndexList'] = request.section_index_list
        if not UtilClient.is_unset(request.subscriber_ids):
            body['subscriberIds'] = request.subscriber_ids
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
            dingtalkedu__1__0_models.QueryClassScheduleResponse(),
            await self.do_roarequest_async('QueryClassSchedule', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/schedules/query', 'json', req, runtime)
        )

    def query_class_schedule_by_time_school(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolHeaders()
        return self.query_class_schedule_by_time_school_with_options(request, headers, runtime)

    async def query_class_schedule_by_time_school_async(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolHeaders()
        return await self.query_class_schedule_by_time_school_with_options_async(request, headers, runtime)

    def query_class_schedule_by_time_school_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse(),
            self.do_roarequest('QueryClassScheduleByTimeSchool', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schools/classes/courses ', 'json', req, runtime)
        )

    async def query_class_schedule_by_time_school_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            dingtalkedu__1__0_models.QueryClassScheduleByTimeSchoolResponse(),
            await self.do_roarequest_async('QueryClassScheduleByTimeSchool', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schools/classes/courses ', 'json', req, runtime)
        )

    def query_class_schedule_config(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleConfigRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleConfigHeaders()
        return self.query_class_schedule_config_with_options(request, headers, runtime)

    async def query_class_schedule_config_async(
        self,
        request: dingtalkedu__1__0_models.QueryClassScheduleConfigRequest,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryClassScheduleConfigHeaders()
        return await self.query_class_schedule_config_with_options_async(request, headers, runtime)

    def query_class_schedule_config_with_options(
        self,
        tmp_req: dingtalkedu__1__0_models.QueryClassScheduleConfigRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkedu__1__0_models.QueryClassScheduleConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.class_ids):
            request.class_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.class_ids, 'classIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.class_ids_shrink):
            query['classIds'] = request.class_ids_shrink
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryClassScheduleConfigResponse(),
            self.do_roarequest('QueryClassScheduleConfig', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schedules/configs', 'json', req, runtime)
        )

    async def query_class_schedule_config_with_options_async(
        self,
        tmp_req: dingtalkedu__1__0_models.QueryClassScheduleConfigRequest,
        headers: dingtalkedu__1__0_models.QueryClassScheduleConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryClassScheduleConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkedu__1__0_models.QueryClassScheduleConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.class_ids):
            request.class_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.class_ids, 'classIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.class_ids_shrink):
            query['classIds'] = request.class_ids_shrink
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryClassScheduleConfigResponse(),
            await self.do_roarequest_async('QueryClassScheduleConfig', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schedules/configs', 'json', req, runtime)
        )

    def query_device_list_by_corp_id(
        self,
        request: dingtalkedu__1__0_models.QueryDeviceListByCorpIdRequest,
    ) -> dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryDeviceListByCorpIdHeaders()
        return self.query_device_list_by_corp_id_with_options(request, headers, runtime)

    async def query_device_list_by_corp_id_async(
        self,
        request: dingtalkedu__1__0_models.QueryDeviceListByCorpIdRequest,
    ) -> dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryDeviceListByCorpIdHeaders()
        return await self.query_device_list_by_corp_id_with_options_async(request, headers, runtime)

    def query_device_list_by_corp_id_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryDeviceListByCorpIdRequest,
        headers: dingtalkedu__1__0_models.QueryDeviceListByCorpIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse(),
            self.do_roarequest('QueryDeviceListByCorpId', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/devices', 'json', req, runtime)
        )

    async def query_device_list_by_corp_id_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryDeviceListByCorpIdRequest,
        headers: dingtalkedu__1__0_models.QueryDeviceListByCorpIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkedu__1__0_models.QueryDeviceListByCorpIdResponse(),
            await self.do_roarequest_async('QueryDeviceListByCorpId', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/devices', 'json', req, runtime)
        )

    def query_edu_asset_spaces(
        self,
        request: dingtalkedu__1__0_models.QueryEduAssetSpacesRequest,
    ) -> dingtalkedu__1__0_models.QueryEduAssetSpacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryEduAssetSpacesHeaders()
        return self.query_edu_asset_spaces_with_options(request, headers, runtime)

    async def query_edu_asset_spaces_async(
        self,
        request: dingtalkedu__1__0_models.QueryEduAssetSpacesRequest,
    ) -> dingtalkedu__1__0_models.QueryEduAssetSpacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryEduAssetSpacesHeaders()
        return await self.query_edu_asset_spaces_with_options_async(request, headers, runtime)

    def query_edu_asset_spaces_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryEduAssetSpacesRequest,
        headers: dingtalkedu__1__0_models.QueryEduAssetSpacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryEduAssetSpacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
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
            dingtalkedu__1__0_models.QueryEduAssetSpacesResponse(),
            self.do_roarequest('QueryEduAssetSpaces', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/assets/spaces', 'json', req, runtime)
        )

    async def query_edu_asset_spaces_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryEduAssetSpacesRequest,
        headers: dingtalkedu__1__0_models.QueryEduAssetSpacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryEduAssetSpacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
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
            dingtalkedu__1__0_models.QueryEduAssetSpacesResponse(),
            await self.do_roarequest_async('QueryEduAssetSpaces', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/assets/spaces', 'json', req, runtime)
        )

    def query_group_id(
        self,
        request: dingtalkedu__1__0_models.QueryGroupIdRequest,
    ) -> dingtalkedu__1__0_models.QueryGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryGroupIdHeaders()
        return self.query_group_id_with_options(request, headers, runtime)

    async def query_group_id_async(
        self,
        request: dingtalkedu__1__0_models.QueryGroupIdRequest,
    ) -> dingtalkedu__1__0_models.QueryGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryGroupIdHeaders()
        return await self.query_group_id_with_options_async(request, headers, runtime)

    def query_group_id_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryGroupIdRequest,
        headers: dingtalkedu__1__0_models.QueryGroupIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryGroupIdResponse(),
            self.do_roarequest('QueryGroupId', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/faces/groups', 'json', req, runtime)
        )

    async def query_group_id_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryGroupIdRequest,
        headers: dingtalkedu__1__0_models.QueryGroupIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryGroupIdResponse(),
            await self.do_roarequest_async('QueryGroupId', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/faces/groups', 'json', req, runtime)
        )

    def query_org_relation_list(
        self,
        request: dingtalkedu__1__0_models.QueryOrgRelationListRequest,
    ) -> dingtalkedu__1__0_models.QueryOrgRelationListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgRelationListHeaders()
        return self.query_org_relation_list_with_options(request, headers, runtime)

    async def query_org_relation_list_async(
        self,
        request: dingtalkedu__1__0_models.QueryOrgRelationListRequest,
    ) -> dingtalkedu__1__0_models.QueryOrgRelationListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgRelationListHeaders()
        return await self.query_org_relation_list_with_options_async(request, headers, runtime)

    def query_org_relation_list_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryOrgRelationListRequest,
        headers: dingtalkedu__1__0_models.QueryOrgRelationListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgRelationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.QueryOrgRelationListResponse(),
            self.do_roarequest('QueryOrgRelationList', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/orgRelations', 'json', req, runtime)
        )

    async def query_org_relation_list_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryOrgRelationListRequest,
        headers: dingtalkedu__1__0_models.QueryOrgRelationListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgRelationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
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
            dingtalkedu__1__0_models.QueryOrgRelationListResponse(),
            await self.do_roarequest_async('QueryOrgRelationList', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/orgRelations', 'json', req, runtime)
        )

    def query_org_secret_key(
        self,
        request: dingtalkedu__1__0_models.QueryOrgSecretKeyRequest,
    ) -> dingtalkedu__1__0_models.QueryOrgSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgSecretKeyHeaders()
        return self.query_org_secret_key_with_options(request, headers, runtime)

    async def query_org_secret_key_async(
        self,
        request: dingtalkedu__1__0_models.QueryOrgSecretKeyRequest,
    ) -> dingtalkedu__1__0_models.QueryOrgSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgSecretKeyHeaders()
        return await self.query_org_secret_key_with_options_async(request, headers, runtime)

    def query_org_secret_key_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryOrgSecretKeyRequest,
        headers: dingtalkedu__1__0_models.QueryOrgSecretKeyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isv_code):
            query['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryOrgSecretKeyResponse(),
            self.do_roarequest('QueryOrgSecretKey', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/secretKeys', 'json', req, runtime)
        )

    async def query_org_secret_key_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryOrgSecretKeyRequest,
        headers: dingtalkedu__1__0_models.QueryOrgSecretKeyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isv_code):
            query['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryOrgSecretKeyResponse(),
            await self.do_roarequest_async('QueryOrgSecretKey', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/secretKeys', 'json', req, runtime)
        )

    def query_org_type(self) -> dingtalkedu__1__0_models.QueryOrgTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgTypeHeaders()
        return self.query_org_type_with_options(headers, runtime)

    async def query_org_type_async(self) -> dingtalkedu__1__0_models.QueryOrgTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryOrgTypeHeaders()
        return await self.query_org_type_with_options_async(headers, runtime)

    def query_org_type_with_options(
        self,
        headers: dingtalkedu__1__0_models.QueryOrgTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgTypeResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.QueryOrgTypeResponse(),
            self.do_roarequest('QueryOrgType', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/orgTypes', 'json', req, runtime)
        )

    async def query_org_type_with_options_async(
        self,
        headers: dingtalkedu__1__0_models.QueryOrgTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryOrgTypeResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkedu__1__0_models.QueryOrgTypeResponse(),
            await self.do_roarequest_async('QueryOrgType', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/orgTypes', 'json', req, runtime)
        )

    def query_pay_result(
        self,
        request: dingtalkedu__1__0_models.QueryPayResultRequest,
    ) -> dingtalkedu__1__0_models.QueryPayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPayResultHeaders()
        return self.query_pay_result_with_options(request, headers, runtime)

    async def query_pay_result_async(
        self,
        request: dingtalkedu__1__0_models.QueryPayResultRequest,
    ) -> dingtalkedu__1__0_models.QueryPayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPayResultHeaders()
        return await self.query_pay_result_with_options_async(request, headers, runtime)

    def query_pay_result_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryPayResultRequest,
        headers: dingtalkedu__1__0_models.QueryPayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPayResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.QueryPayResultResponse(),
            self.do_roarequest('QueryPayResult', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/payResults/query', 'json', req, runtime)
        )

    async def query_pay_result_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryPayResultRequest,
        headers: dingtalkedu__1__0_models.QueryPayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPayResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.face_id):
            body['faceId'] = request.face_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
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
            dingtalkedu__1__0_models.QueryPayResultResponse(),
            await self.do_roarequest_async('QueryPayResult', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/payResults/query', 'json', req, runtime)
        )

    def query_physical_classroom(
        self,
        request: dingtalkedu__1__0_models.QueryPhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.QueryPhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPhysicalClassroomHeaders()
        return self.query_physical_classroom_with_options(request, headers, runtime)

    async def query_physical_classroom_async(
        self,
        request: dingtalkedu__1__0_models.QueryPhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.QueryPhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPhysicalClassroomHeaders()
        return await self.query_physical_classroom_with_options_async(request, headers, runtime)

    def query_physical_classroom_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryPhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.QueryPhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classroom_id):
            query['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryPhysicalClassroomResponse(),
            self.do_roarequest('QueryPhysicalClassroom', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    async def query_physical_classroom_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryPhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.QueryPhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classroom_id):
            query['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryPhysicalClassroomResponse(),
            await self.do_roarequest_async('QueryPhysicalClassroom', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    def query_purchase_info(
        self,
        request: dingtalkedu__1__0_models.QueryPurchaseInfoRequest,
    ) -> dingtalkedu__1__0_models.QueryPurchaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPurchaseInfoHeaders()
        return self.query_purchase_info_with_options(request, headers, runtime)

    async def query_purchase_info_async(
        self,
        request: dingtalkedu__1__0_models.QueryPurchaseInfoRequest,
    ) -> dingtalkedu__1__0_models.QueryPurchaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryPurchaseInfoHeaders()
        return await self.query_purchase_info_with_options_async(request, headers, runtime)

    def query_purchase_info_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryPurchaseInfoRequest,
        headers: dingtalkedu__1__0_models.QueryPurchaseInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPurchaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_id):
            query['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryPurchaseInfoResponse(),
            self.do_roarequest('QueryPurchaseInfo', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/users/purchases', 'json', req, runtime)
        )

    async def query_purchase_info_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryPurchaseInfoRequest,
        headers: dingtalkedu__1__0_models.QueryPurchaseInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryPurchaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_id):
            query['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryPurchaseInfoResponse(),
            await self.do_roarequest_async('QueryPurchaseInfo', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/users/purchases', 'json', req, runtime)
        )

    def query_remote_class_course(
        self,
        request: dingtalkedu__1__0_models.QueryRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.QueryRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryRemoteClassCourseHeaders()
        return self.query_remote_class_course_with_options(request, headers, runtime)

    async def query_remote_class_course_async(
        self,
        request: dingtalkedu__1__0_models.QueryRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.QueryRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryRemoteClassCourseHeaders()
        return await self.query_remote_class_course_with_options_async(request, headers, runtime)

    def query_remote_class_course_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.QueryRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            dingtalkedu__1__0_models.QueryRemoteClassCourseResponse(),
            self.do_roarequest('QueryRemoteClassCourse', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    async def query_remote_class_course_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.QueryRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            dingtalkedu__1__0_models.QueryRemoteClassCourseResponse(),
            await self.do_roarequest_async('QueryRemoteClassCourse', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    def query_school_user_face(
        self,
        request: dingtalkedu__1__0_models.QuerySchoolUserFaceRequest,
    ) -> dingtalkedu__1__0_models.QuerySchoolUserFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QuerySchoolUserFaceHeaders()
        return self.query_school_user_face_with_options(request, headers, runtime)

    async def query_school_user_face_async(
        self,
        request: dingtalkedu__1__0_models.QuerySchoolUserFaceRequest,
    ) -> dingtalkedu__1__0_models.QuerySchoolUserFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QuerySchoolUserFaceHeaders()
        return await self.query_school_user_face_with_options_async(request, headers, runtime)

    def query_school_user_face_with_options(
        self,
        request: dingtalkedu__1__0_models.QuerySchoolUserFaceRequest,
        headers: dingtalkedu__1__0_models.QuerySchoolUserFaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QuerySchoolUserFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QuerySchoolUserFaceResponse(),
            self.do_roarequest('QuerySchoolUserFace', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schools/faces', 'json', req, runtime)
        )

    async def query_school_user_face_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QuerySchoolUserFaceRequest,
        headers: dingtalkedu__1__0_models.QuerySchoolUserFaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QuerySchoolUserFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QuerySchoolUserFaceResponse(),
            await self.do_roarequest_async('QuerySchoolUserFace', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/schools/faces', 'json', req, runtime)
        )

    def query_statistics_data(
        self,
        request: dingtalkedu__1__0_models.QueryStatisticsDataRequest,
    ) -> dingtalkedu__1__0_models.QueryStatisticsDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryStatisticsDataHeaders()
        return self.query_statistics_data_with_options(request, headers, runtime)

    async def query_statistics_data_async(
        self,
        request: dingtalkedu__1__0_models.QueryStatisticsDataRequest,
    ) -> dingtalkedu__1__0_models.QueryStatisticsDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryStatisticsDataHeaders()
        return await self.query_statistics_data_with_options_async(request, headers, runtime)

    def query_statistics_data_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryStatisticsDataRequest,
        headers: dingtalkedu__1__0_models.QueryStatisticsDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryStatisticsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.section_index_list):
            body['sectionIndexList'] = request.section_index_list
        if not UtilClient.is_unset(request.teacher_user_ids):
            body['teacherUserIds'] = request.teacher_user_ids
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
            dingtalkedu__1__0_models.QueryStatisticsDataResponse(),
            self.do_roarequest('QueryStatisticsData', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/schedules/statisticData/query', 'json', req, runtime)
        )

    async def query_statistics_data_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryStatisticsDataRequest,
        headers: dingtalkedu__1__0_models.QueryStatisticsDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryStatisticsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.section_index_list):
            body['sectionIndexList'] = request.section_index_list
        if not UtilClient.is_unset(request.teacher_user_ids):
            body['teacherUserIds'] = request.teacher_user_ids
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
            dingtalkedu__1__0_models.QueryStatisticsDataResponse(),
            await self.do_roarequest_async('QueryStatisticsData', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/classes/schedules/statisticData/query', 'json', req, runtime)
        )

    def query_subject_teachers(
        self,
        request: dingtalkedu__1__0_models.QuerySubjectTeachersRequest,
    ) -> dingtalkedu__1__0_models.QuerySubjectTeachersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QuerySubjectTeachersHeaders()
        return self.query_subject_teachers_with_options(request, headers, runtime)

    async def query_subject_teachers_async(
        self,
        request: dingtalkedu__1__0_models.QuerySubjectTeachersRequest,
    ) -> dingtalkedu__1__0_models.QuerySubjectTeachersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QuerySubjectTeachersHeaders()
        return await self.query_subject_teachers_with_options_async(request, headers, runtime)

    def query_subject_teachers_with_options(
        self,
        request: dingtalkedu__1__0_models.QuerySubjectTeachersRequest,
        headers: dingtalkedu__1__0_models.QuerySubjectTeachersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QuerySubjectTeachersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_ids):
            query['classIds'] = request.class_ids
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.subject_code):
            query['subjectCode'] = request.subject_code
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
            dingtalkedu__1__0_models.QuerySubjectTeachersResponse(),
            self.do_roarequest('QuerySubjectTeachers', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/subjects/teachers', 'json', req, runtime)
        )

    async def query_subject_teachers_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QuerySubjectTeachersRequest,
        headers: dingtalkedu__1__0_models.QuerySubjectTeachersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QuerySubjectTeachersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_ids):
            query['classIds'] = request.class_ids
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.subject_code):
            query['subjectCode'] = request.subject_code
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
            dingtalkedu__1__0_models.QuerySubjectTeachersResponse(),
            await self.do_roarequest_async('QuerySubjectTeachers', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/subjects/teachers', 'json', req, runtime)
        )

    def query_teach_subjects(
        self,
        request: dingtalkedu__1__0_models.QueryTeachSubjectsRequest,
    ) -> dingtalkedu__1__0_models.QueryTeachSubjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryTeachSubjectsHeaders()
        return self.query_teach_subjects_with_options(request, headers, runtime)

    async def query_teach_subjects_async(
        self,
        request: dingtalkedu__1__0_models.QueryTeachSubjectsRequest,
    ) -> dingtalkedu__1__0_models.QueryTeachSubjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryTeachSubjectsHeaders()
        return await self.query_teach_subjects_with_options_async(request, headers, runtime)

    def query_teach_subjects_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryTeachSubjectsRequest,
        headers: dingtalkedu__1__0_models.QueryTeachSubjectsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryTeachSubjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_ids):
            query['classIds'] = request.class_ids
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryTeachSubjectsResponse(),
            self.do_roarequest('QueryTeachSubjects', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/teachers/subjects', 'json', req, runtime)
        )

    async def query_teach_subjects_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryTeachSubjectsRequest,
        headers: dingtalkedu__1__0_models.QueryTeachSubjectsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryTeachSubjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_ids):
            query['classIds'] = request.class_ids
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryTeachSubjectsResponse(),
            await self.do_roarequest_async('QueryTeachSubjects', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/teachers/subjects', 'json', req, runtime)
        )

    def query_university_course_group(
        self,
        request: dingtalkedu__1__0_models.QueryUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUniversityCourseGroupHeaders()
        return self.query_university_course_group_with_options(request, headers, runtime)

    async def query_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.QueryUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUniversityCourseGroupHeaders()
        return await self.query_university_course_group_with_options_async(request, headers, runtime)

    def query_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.QueryUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_group_code):
            query['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse(),
            self.do_roarequest('QueryUniversityCourseGroup', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    async def query_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.QueryUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.course_group_code):
            query['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkedu__1__0_models.QueryUniversityCourseGroupResponse(),
            await self.do_roarequest_async('QueryUniversityCourseGroup', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    def query_user_face(
        self,
        request: dingtalkedu__1__0_models.QueryUserFaceRequest,
    ) -> dingtalkedu__1__0_models.QueryUserFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUserFaceHeaders()
        return self.query_user_face_with_options(request, headers, runtime)

    async def query_user_face_async(
        self,
        request: dingtalkedu__1__0_models.QueryUserFaceRequest,
    ) -> dingtalkedu__1__0_models.QueryUserFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUserFaceHeaders()
        return await self.query_user_face_with_options_async(request, headers, runtime)

    def query_user_face_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryUserFaceRequest,
        headers: dingtalkedu__1__0_models.QueryUserFaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUserFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['faceId'] = request.face_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryUserFaceResponse(),
            self.do_roarequest('QueryUserFace', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/users/faces', 'json', req, runtime)
        )

    async def query_user_face_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryUserFaceRequest,
        headers: dingtalkedu__1__0_models.QueryUserFaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUserFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['faceId'] = request.face_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryUserFaceResponse(),
            await self.do_roarequest_async('QueryUserFace', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/users/faces', 'json', req, runtime)
        )

    def query_user_pay_info(
        self,
        request: dingtalkedu__1__0_models.QueryUserPayInfoRequest,
    ) -> dingtalkedu__1__0_models.QueryUserPayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUserPayInfoHeaders()
        return self.query_user_pay_info_with_options(request, headers, runtime)

    async def query_user_pay_info_async(
        self,
        request: dingtalkedu__1__0_models.QueryUserPayInfoRequest,
    ) -> dingtalkedu__1__0_models.QueryUserPayInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.QueryUserPayInfoHeaders()
        return await self.query_user_pay_info_with_options_async(request, headers, runtime)

    def query_user_pay_info_with_options(
        self,
        request: dingtalkedu__1__0_models.QueryUserPayInfoRequest,
        headers: dingtalkedu__1__0_models.QueryUserPayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUserPayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['faceId'] = request.face_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryUserPayInfoResponse(),
            self.do_roarequest('QueryUserPayInfo', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/orders/payInfos', 'json', req, runtime)
        )

    async def query_user_pay_info_with_options_async(
        self,
        request: dingtalkedu__1__0_models.QueryUserPayInfoRequest,
        headers: dingtalkedu__1__0_models.QueryUserPayInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.QueryUserPayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['faceId'] = request.face_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.QueryUserPayInfoResponse(),
            await self.do_roarequest_async('QueryUserPayInfo', 'edu_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/edu/orders/payInfos', 'json', req, runtime)
        )

    def remove_device(
        self,
        request: dingtalkedu__1__0_models.RemoveDeviceRequest,
    ) -> dingtalkedu__1__0_models.RemoveDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.RemoveDeviceHeaders()
        return self.remove_device_with_options(request, headers, runtime)

    async def remove_device_async(
        self,
        request: dingtalkedu__1__0_models.RemoveDeviceRequest,
    ) -> dingtalkedu__1__0_models.RemoveDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.RemoveDeviceHeaders()
        return await self.remove_device_with_options_async(request, headers, runtime)

    def remove_device_with_options(
        self,
        request: dingtalkedu__1__0_models.RemoveDeviceRequest,
        headers: dingtalkedu__1__0_models.RemoveDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.RemoveDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_id):
            query['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.RemoveDeviceResponse(),
            self.do_roarequest('RemoveDevice', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/devices', 'json', req, runtime)
        )

    async def remove_device_with_options_async(
        self,
        request: dingtalkedu__1__0_models.RemoveDeviceRequest,
        headers: dingtalkedu__1__0_models.RemoveDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.RemoveDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_id):
            query['merchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.RemoveDeviceResponse(),
            await self.do_roarequest_async('RemoveDevice', 'edu_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/edu/devices', 'json', req, runtime)
        )

    def report_device_log(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceLogRequest,
    ) -> dingtalkedu__1__0_models.ReportDeviceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ReportDeviceLogHeaders()
        return self.report_device_log_with_options(request, headers, runtime)

    async def report_device_log_async(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceLogRequest,
    ) -> dingtalkedu__1__0_models.ReportDeviceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ReportDeviceLogHeaders()
        return await self.report_device_log_with_options_async(request, headers, runtime)

    def report_device_log_with_options(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceLogRequest,
        headers: dingtalkedu__1__0_models.ReportDeviceLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ReportDeviceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.ReportDeviceLogResponse(),
            self.do_roarequest('ReportDeviceLog', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/deviceLogs/report', 'json', req, runtime)
        )

    async def report_device_log_with_options_async(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceLogRequest,
        headers: dingtalkedu__1__0_models.ReportDeviceLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ReportDeviceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['mediaId'] = request.media_id
        if not UtilClient.is_unset(request.sn):
            query['sn'] = request.sn
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
            dingtalkedu__1__0_models.ReportDeviceLogResponse(),
            await self.do_roarequest_async('ReportDeviceLog', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/deviceLogs/report', 'json', req, runtime)
        )

    def report_device_use_log(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceUseLogRequest,
    ) -> dingtalkedu__1__0_models.ReportDeviceUseLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ReportDeviceUseLogHeaders()
        return self.report_device_use_log_with_options(request, headers, runtime)

    async def report_device_use_log_async(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceUseLogRequest,
    ) -> dingtalkedu__1__0_models.ReportDeviceUseLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.ReportDeviceUseLogHeaders()
        return await self.report_device_use_log_with_options_async(request, headers, runtime)

    def report_device_use_log_with_options(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceUseLogRequest,
        headers: dingtalkedu__1__0_models.ReportDeviceUseLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ReportDeviceUseLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.ReportDeviceUseLogResponse(),
            self.do_roarequest('ReportDeviceUseLog', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/deviceUseLogs/report', 'json', req, runtime)
        )

    async def report_device_use_log_with_options_async(
        self,
        request: dingtalkedu__1__0_models.ReportDeviceUseLogRequest,
        headers: dingtalkedu__1__0_models.ReportDeviceUseLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.ReportDeviceUseLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
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
            dingtalkedu__1__0_models.ReportDeviceUseLogResponse(),
            await self.do_roarequest_async('ReportDeviceUseLog', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/deviceUseLogs/report', 'json', req, runtime)
        )

    def search_teachers(
        self,
        request: dingtalkedu__1__0_models.SearchTeachersRequest,
    ) -> dingtalkedu__1__0_models.SearchTeachersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SearchTeachersHeaders()
        return self.search_teachers_with_options(request, headers, runtime)

    async def search_teachers_async(
        self,
        request: dingtalkedu__1__0_models.SearchTeachersRequest,
    ) -> dingtalkedu__1__0_models.SearchTeachersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SearchTeachersHeaders()
        return await self.search_teachers_with_options_async(request, headers, runtime)

    def search_teachers_with_options(
        self,
        request: dingtalkedu__1__0_models.SearchTeachersRequest,
        headers: dingtalkedu__1__0_models.SearchTeachersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SearchTeachersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_keyword):
            query['nameKeyword'] = request.name_keyword
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
            dingtalkedu__1__0_models.SearchTeachersResponse(),
            self.do_roarequest('SearchTeachers', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/teachers/search', 'json', req, runtime)
        )

    async def search_teachers_with_options_async(
        self,
        request: dingtalkedu__1__0_models.SearchTeachersRequest,
        headers: dingtalkedu__1__0_models.SearchTeachersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SearchTeachersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_keyword):
            query['nameKeyword'] = request.name_keyword
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
            dingtalkedu__1__0_models.SearchTeachersResponse(),
            await self.do_roarequest_async('SearchTeachers', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/teachers/search', 'json', req, runtime)
        )

    def send_message(
        self,
        request: dingtalkedu__1__0_models.SendMessageRequest,
    ) -> dingtalkedu__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SendMessageHeaders()
        return self.send_message_with_options(request, headers, runtime)

    async def send_message_async(
        self,
        request: dingtalkedu__1__0_models.SendMessageRequest,
    ) -> dingtalkedu__1__0_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SendMessageHeaders()
        return await self.send_message_with_options_async(request, headers, runtime)

    def send_message_with_options(
        self,
        request: dingtalkedu__1__0_models.SendMessageRequest,
        headers: dingtalkedu__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.from_user_id):
            body['fromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.to_user_id_list):
            body['toUserIdList'] = request.to_user_id_list
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.SendMessageResponse(),
            self.do_roarequest('SendMessage', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/messages/send', 'json', req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: dingtalkedu__1__0_models.SendMessageRequest,
        headers: dingtalkedu__1__0_models.SendMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.from_user_id):
            body['fromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        if not UtilClient.is_unset(request.to_user_id_list):
            body['toUserIdList'] = request.to_user_id_list
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkedu__1__0_models.SendMessageResponse(),
            await self.do_roarequest_async('SendMessage', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/messages/send', 'json', req, runtime)
        )

    def start_course(
        self,
        request: dingtalkedu__1__0_models.StartCourseRequest,
    ) -> dingtalkedu__1__0_models.StartCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.StartCourseHeaders()
        return self.start_course_with_options(request, headers, runtime)

    async def start_course_async(
        self,
        request: dingtalkedu__1__0_models.StartCourseRequest,
    ) -> dingtalkedu__1__0_models.StartCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.StartCourseHeaders()
        return await self.start_course_with_options_async(request, headers, runtime)

    def start_course_with_options(
        self,
        request: dingtalkedu__1__0_models.StartCourseRequest,
        headers: dingtalkedu__1__0_models.StartCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.StartCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_play_info_list):
            body['livePlayInfoList'] = request.live_play_info_list
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
            dingtalkedu__1__0_models.StartCourseResponse(),
            self.do_roarequest('StartCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/start', 'json', req, runtime)
        )

    async def start_course_with_options_async(
        self,
        request: dingtalkedu__1__0_models.StartCourseRequest,
        headers: dingtalkedu__1__0_models.StartCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.StartCourseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_play_info_list):
            body['livePlayInfoList'] = request.live_play_info_list
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
            dingtalkedu__1__0_models.StartCourseResponse(),
            await self.do_roarequest_async('StartCourse', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/start', 'json', req, runtime)
        )

    def start_course_prepare(
        self,
        request: dingtalkedu__1__0_models.StartCoursePrepareRequest,
    ) -> dingtalkedu__1__0_models.StartCoursePrepareResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.StartCoursePrepareHeaders()
        return self.start_course_prepare_with_options(request, headers, runtime)

    async def start_course_prepare_async(
        self,
        request: dingtalkedu__1__0_models.StartCoursePrepareRequest,
    ) -> dingtalkedu__1__0_models.StartCoursePrepareResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.StartCoursePrepareHeaders()
        return await self.start_course_prepare_with_options_async(request, headers, runtime)

    def start_course_prepare_with_options(
        self,
        request: dingtalkedu__1__0_models.StartCoursePrepareRequest,
        headers: dingtalkedu__1__0_models.StartCoursePrepareHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.StartCoursePrepareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_date):
            body['courseDate'] = request.course_date
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_cover_image):
            body['liveCoverImage'] = request.live_cover_image
        if not UtilClient.is_unset(request.section_index):
            body['sectionIndex'] = request.section_index
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
            dingtalkedu__1__0_models.StartCoursePrepareResponse(),
            self.do_roarequest('StartCoursePrepare', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/prepare', 'json', req, runtime)
        )

    async def start_course_prepare_with_options_async(
        self,
        request: dingtalkedu__1__0_models.StartCoursePrepareRequest,
        headers: dingtalkedu__1__0_models.StartCoursePrepareHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.StartCoursePrepareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_date):
            body['courseDate'] = request.course_date
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
        if not UtilClient.is_unset(request.isv_code):
            body['isvCode'] = request.isv_code
        if not UtilClient.is_unset(request.live_cover_image):
            body['liveCoverImage'] = request.live_cover_image
        if not UtilClient.is_unset(request.section_index):
            body['sectionIndex'] = request.section_index
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
            dingtalkedu__1__0_models.StartCoursePrepareResponse(),
            await self.do_roarequest_async('StartCoursePrepare', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courses/prepare', 'json', req, runtime)
        )

    def subscribe_university_course_group(
        self,
        request: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SubscribeUniversityCourseGroupHeaders()
        return self.subscribe_university_course_group_with_options(request, headers, runtime)

    async def subscribe_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.SubscribeUniversityCourseGroupHeaders()
        return await self.subscribe_university_course_group_with_options_async(request, headers, runtime)

    def subscribe_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.student_user_ids):
            body['studentUserIds'] = request.student_user_ids
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
            dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse(),
            self.do_roarequest('SubscribeUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups/subscribe', 'json', req, runtime)
        )

    async def subscribe_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.SubscribeUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.student_user_ids):
            body['studentUserIds'] = request.student_user_ids
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
            dingtalkedu__1__0_models.SubscribeUniversityCourseGroupResponse(),
            await self.do_roarequest_async('SubscribeUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups/subscribe', 'json', req, runtime)
        )

    def unsubscribe_university_course_group(
        self,
        request: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupHeaders()
        return self.unsubscribe_university_course_group_with_options(request, headers, runtime)

    async def unsubscribe_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupHeaders()
        return await self.unsubscribe_university_course_group_with_options_async(request, headers, runtime)

    def unsubscribe_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.student_user_ids):
            body['studentUserIds'] = request.student_user_ids
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
            dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse(),
            self.do_roarequest('UnsubscribeUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups/unsubscribe', 'json', req, runtime)
        )

    async def unsubscribe_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.student_user_ids):
            body['studentUserIds'] = request.student_user_ids
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
            dingtalkedu__1__0_models.UnsubscribeUniversityCourseGroupResponse(),
            await self.do_roarequest_async('UnsubscribeUniversityCourseGroup', 'edu_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/edu/universities/courseGroups/unsubscribe', 'json', req, runtime)
        )

    def update_courses_of_class(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.UpdateCoursesOfClassRequest,
    ) -> dingtalkedu__1__0_models.UpdateCoursesOfClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateCoursesOfClassHeaders()
        return self.update_courses_of_class_with_options(class_id, request, headers, runtime)

    async def update_courses_of_class_async(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.UpdateCoursesOfClassRequest,
    ) -> dingtalkedu__1__0_models.UpdateCoursesOfClassResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateCoursesOfClassHeaders()
        return await self.update_courses_of_class_with_options_async(class_id, request, headers, runtime)

    def update_courses_of_class_with_options(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.UpdateCoursesOfClassRequest,
        headers: dingtalkedu__1__0_models.UpdateCoursesOfClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateCoursesOfClassResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.courses):
            body['courses'] = request.courses
        if not UtilClient.is_unset(request.section_config):
            body['sectionConfig'] = request.section_config
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
            dingtalkedu__1__0_models.UpdateCoursesOfClassResponse(),
            self.do_roarequest('UpdateCoursesOfClass', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/classes/{class_id}/courses/schedules', 'json', req, runtime)
        )

    async def update_courses_of_class_with_options_async(
        self,
        class_id: str,
        request: dingtalkedu__1__0_models.UpdateCoursesOfClassRequest,
        headers: dingtalkedu__1__0_models.UpdateCoursesOfClassHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateCoursesOfClassResponse:
        UtilClient.validate_model(request)
        class_id = OpenApiUtilClient.get_encode_param(class_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.courses):
            body['courses'] = request.courses
        if not UtilClient.is_unset(request.section_config):
            body['sectionConfig'] = request.section_config
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
            dingtalkedu__1__0_models.UpdateCoursesOfClassResponse(),
            await self.do_roarequest_async('UpdateCoursesOfClass', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/classes/{class_id}/courses/schedules', 'json', req, runtime)
        )

    def update_physical_classroom(
        self,
        request: dingtalkedu__1__0_models.UpdatePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdatePhysicalClassroomHeaders()
        return self.update_physical_classroom_with_options(request, headers, runtime)

    async def update_physical_classroom_async(
        self,
        request: dingtalkedu__1__0_models.UpdatePhysicalClassroomRequest,
    ) -> dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdatePhysicalClassroomHeaders()
        return await self.update_physical_classroom_with_options_async(request, headers, runtime)

    def update_physical_classroom_with_options(
        self,
        request: dingtalkedu__1__0_models.UpdatePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.UpdatePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.classroom_building):
            body['classroomBuilding'] = request.classroom_building
        if not UtilClient.is_unset(request.classroom_campus):
            body['classroomCampus'] = request.classroom_campus
        if not UtilClient.is_unset(request.classroom_floor):
            body['classroomFloor'] = request.classroom_floor
        if not UtilClient.is_unset(request.classroom_id):
            body['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.classroom_name):
            body['classroomName'] = request.classroom_name
        if not UtilClient.is_unset(request.classroom_number):
            body['classroomNumber'] = request.classroom_number
        if not UtilClient.is_unset(request.direct_broadcast):
            body['directBroadcast'] = request.direct_broadcast
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse(),
            self.do_roarequest('UpdatePhysicalClassroom', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    async def update_physical_classroom_with_options_async(
        self,
        request: dingtalkedu__1__0_models.UpdatePhysicalClassroomRequest,
        headers: dingtalkedu__1__0_models.UpdatePhysicalClassroomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.classroom_building):
            body['classroomBuilding'] = request.classroom_building
        if not UtilClient.is_unset(request.classroom_campus):
            body['classroomCampus'] = request.classroom_campus
        if not UtilClient.is_unset(request.classroom_floor):
            body['classroomFloor'] = request.classroom_floor
        if not UtilClient.is_unset(request.classroom_id):
            body['classroomId'] = request.classroom_id
        if not UtilClient.is_unset(request.classroom_name):
            body['classroomName'] = request.classroom_name
        if not UtilClient.is_unset(request.classroom_number):
            body['classroomNumber'] = request.classroom_number
        if not UtilClient.is_unset(request.direct_broadcast):
            body['directBroadcast'] = request.direct_broadcast
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.UpdatePhysicalClassroomResponse(),
            await self.do_roarequest_async('UpdatePhysicalClassroom', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/physicalClassrooms', 'json', req, runtime)
        )

    def update_remote_class_course(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateRemoteClassCourseHeaders()
        return self.update_remote_class_course_with_options(request, headers, runtime)

    async def update_remote_class_course_async(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassCourseRequest,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateRemoteClassCourseHeaders()
        return await self.update_remote_class_course_with_options_async(request, headers, runtime)

    def update_remote_class_course_with_options(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.UpdateRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attend_participants):
            body['attendParticipants'] = request.attend_participants
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.teaching_participant):
            body['teachingParticipant'] = request.teaching_participant
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
            dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse(),
            self.do_roarequest('UpdateRemoteClassCourse', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    async def update_remote_class_course_with_options_async(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassCourseRequest,
        headers: dingtalkedu__1__0_models.UpdateRemoteClassCourseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attend_participants):
            body['attendParticipants'] = request.attend_participants
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.course_code):
            body['courseCode'] = request.course_code
        if not UtilClient.is_unset(request.course_name):
            body['courseName'] = request.course_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.teaching_participant):
            body['teachingParticipant'] = request.teaching_participant
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
            dingtalkedu__1__0_models.UpdateRemoteClassCourseResponse(),
            await self.do_roarequest_async('UpdateRemoteClassCourse', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/remoteClasses/courses', 'json', req, runtime)
        )

    def update_remote_class_device(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassDeviceRequest,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateRemoteClassDeviceHeaders()
        return self.update_remote_class_device_with_options(request, headers, runtime)

    async def update_remote_class_device_async(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassDeviceRequest,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateRemoteClassDeviceHeaders()
        return await self.update_remote_class_device_with_options_async(request, headers, runtime)

    def update_remote_class_device_with_options(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassDeviceRequest,
        headers: dingtalkedu__1__0_models.UpdateRemoteClassDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_name):
            query['deviceName'] = request.device_name
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
            dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse(),
            self.do_roarequest('UpdateRemoteClassDevice', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/remoteClasses/deviceNames', 'json', req, runtime)
        )

    async def update_remote_class_device_with_options_async(
        self,
        request: dingtalkedu__1__0_models.UpdateRemoteClassDeviceRequest,
        headers: dingtalkedu__1__0_models.UpdateRemoteClassDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_name):
            query['deviceName'] = request.device_name
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
            dingtalkedu__1__0_models.UpdateRemoteClassDeviceResponse(),
            await self.do_roarequest_async('UpdateRemoteClassDevice', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/remoteClasses/deviceNames', 'json', req, runtime)
        )

    def update_university_course_group(
        self,
        request: dingtalkedu__1__0_models.UpdateUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateUniversityCourseGroupHeaders()
        return self.update_university_course_group_with_options(request, headers, runtime)

    async def update_university_course_group_async(
        self,
        request: dingtalkedu__1__0_models.UpdateUniversityCourseGroupRequest,
    ) -> dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkedu__1__0_models.UpdateUniversityCourseGroupHeaders()
        return await self.update_university_course_group_with_options_async(request, headers, runtime)

    def update_university_course_group_with_options(
        self,
        request: dingtalkedu__1__0_models.UpdateUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.UpdateUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.course_group_introduce):
            body['courseGroupIntroduce'] = request.course_group_introduce
        if not UtilClient.is_unset(request.course_group_name):
            body['courseGroupName'] = request.course_group_name
        if not UtilClient.is_unset(request.courser_group_item_models):
            body['courserGroupItemModels'] = request.courser_group_item_models
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse(),
            self.do_roarequest('UpdateUniversityCourseGroup', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )

    async def update_university_course_group_with_options_async(
        self,
        request: dingtalkedu__1__0_models.UpdateUniversityCourseGroupRequest,
        headers: dingtalkedu__1__0_models.UpdateUniversityCourseGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
        body = {}
        if not UtilClient.is_unset(request.course_group_code):
            body['courseGroupCode'] = request.course_group_code
        if not UtilClient.is_unset(request.course_group_introduce):
            body['courseGroupIntroduce'] = request.course_group_introduce
        if not UtilClient.is_unset(request.course_group_name):
            body['courseGroupName'] = request.course_group_name
        if not UtilClient.is_unset(request.courser_group_item_models):
            body['courserGroupItemModels'] = request.courser_group_item_models
        if not UtilClient.is_unset(request.ext):
            body['ext'] = request.ext
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
            dingtalkedu__1__0_models.UpdateUniversityCourseGroupResponse(),
            await self.do_roarequest_async('UpdateUniversityCourseGroup', 'edu_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/edu/universities/courseGroups', 'json', req, runtime)
        )
