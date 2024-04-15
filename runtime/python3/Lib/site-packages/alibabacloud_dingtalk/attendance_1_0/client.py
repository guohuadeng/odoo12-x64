# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
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

    def attendance_ble_devices_add(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesAddRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesAddHeaders()
        return self.attendance_ble_devices_add_with_options(request, headers, runtime)

    async def attendance_ble_devices_add_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesAddRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesAddHeaders()
        return await self.attendance_ble_devices_add_with_options_async(request, headers, runtime)

    def attendance_ble_devices_add_with_options(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesAddRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['deviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse(),
            self.do_roarequest('AttendanceBleDevicesAdd', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices', 'json', req, runtime)
        )

    async def attendance_ble_devices_add_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesAddRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesAddHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['deviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesAddResponse(),
            await self.do_roarequest_async('AttendanceBleDevicesAdd', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices', 'json', req, runtime)
        )

    def attendance_ble_devices_query(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesQueryHeaders()
        return self.attendance_ble_devices_query_with_options(request, headers, runtime)

    async def attendance_ble_devices_query_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesQueryHeaders()
        return await self.attendance_ble_devices_query_with_options_async(request, headers, runtime)

    def attendance_ble_devices_query_with_options(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse(),
            self.do_roarequest_with_form('AttendanceBleDevicesQuery', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices/query', 'json', req, runtime)
        )

    async def attendance_ble_devices_query_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesQueryResponse(),
            await self.do_roarequest_with_form_async('AttendanceBleDevicesQuery', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices/query', 'json', req, runtime)
        )

    def attendance_ble_devices_remove(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveHeaders()
        return self.attendance_ble_devices_remove_with_options(request, headers, runtime)

    async def attendance_ble_devices_remove_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveRequest,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveHeaders()
        return await self.attendance_ble_devices_remove_with_options_async(request, headers, runtime)

    def attendance_ble_devices_remove_with_options(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['deviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse(),
            self.do_roarequest('AttendanceBleDevicesRemove', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices/remove', 'json', req, runtime)
        )

    async def attendance_ble_devices_remove_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveRequest,
        headers: dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['deviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.group_key):
            body['groupKey'] = request.group_key
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkattendance__1__0_models.AttendanceBleDevicesRemoveResponse(),
            await self.do_roarequest_async('AttendanceBleDevicesRemove', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/group/bledevices/remove', 'json', req, runtime)
        )

    def check_closing_account(
        self,
        request: dingtalkattendance__1__0_models.CheckClosingAccountRequest,
    ) -> dingtalkattendance__1__0_models.CheckClosingAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CheckClosingAccountHeaders()
        return self.check_closing_account_with_options(request, headers, runtime)

    async def check_closing_account_async(
        self,
        request: dingtalkattendance__1__0_models.CheckClosingAccountRequest,
    ) -> dingtalkattendance__1__0_models.CheckClosingAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CheckClosingAccountHeaders()
        return await self.check_closing_account_with_options_async(request, headers, runtime)

    def check_closing_account_with_options(
        self,
        request: dingtalkattendance__1__0_models.CheckClosingAccountRequest,
        headers: dingtalkattendance__1__0_models.CheckClosingAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CheckClosingAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.user_time_range):
            body['userTimeRange'] = request.user_time_range
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
            dingtalkattendance__1__0_models.CheckClosingAccountResponse(),
            self.do_roarequest('CheckClosingAccount', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/closingAccounts/status/query', 'json', req, runtime)
        )

    async def check_closing_account_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.CheckClosingAccountRequest,
        headers: dingtalkattendance__1__0_models.CheckClosingAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CheckClosingAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.user_time_range):
            body['userTimeRange'] = request.user_time_range
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
            dingtalkattendance__1__0_models.CheckClosingAccountResponse(),
            await self.do_roarequest_async('CheckClosingAccount', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/closingAccounts/status/query', 'json', req, runtime)
        )

    def check_write_permission(
        self,
        request: dingtalkattendance__1__0_models.CheckWritePermissionRequest,
    ) -> dingtalkattendance__1__0_models.CheckWritePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CheckWritePermissionHeaders()
        return self.check_write_permission_with_options(request, headers, runtime)

    async def check_write_permission_async(
        self,
        request: dingtalkattendance__1__0_models.CheckWritePermissionRequest,
    ) -> dingtalkattendance__1__0_models.CheckWritePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CheckWritePermissionHeaders()
        return await self.check_write_permission_with_options_async(request, headers, runtime)

    def check_write_permission_with_options(
        self,
        request: dingtalkattendance__1__0_models.CheckWritePermissionRequest,
        headers: dingtalkattendance__1__0_models.CheckWritePermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CheckWritePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.entity_ids):
            body['entityIds'] = request.entity_ids
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.resource_key):
            body['resourceKey'] = request.resource_key
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
            dingtalkattendance__1__0_models.CheckWritePermissionResponse(),
            self.do_roarequest('CheckWritePermission', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/writePermissions/query', 'json', req, runtime)
        )

    async def check_write_permission_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.CheckWritePermissionRequest,
        headers: dingtalkattendance__1__0_models.CheckWritePermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CheckWritePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.entity_ids):
            body['entityIds'] = request.entity_ids
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.resource_key):
            body['resourceKey'] = request.resource_key
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
            dingtalkattendance__1__0_models.CheckWritePermissionResponse(),
            await self.do_roarequest_async('CheckWritePermission', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/writePermissions/query', 'json', req, runtime)
        )

    def create_approve(
        self,
        request: dingtalkattendance__1__0_models.CreateApproveRequest,
    ) -> dingtalkattendance__1__0_models.CreateApproveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CreateApproveHeaders()
        return self.create_approve_with_options(request, headers, runtime)

    async def create_approve_async(
        self,
        request: dingtalkattendance__1__0_models.CreateApproveRequest,
    ) -> dingtalkattendance__1__0_models.CreateApproveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.CreateApproveHeaders()
        return await self.create_approve_with_options_async(request, headers, runtime)

    def create_approve_with_options(
        self,
        request: dingtalkattendance__1__0_models.CreateApproveRequest,
        headers: dingtalkattendance__1__0_models.CreateApproveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CreateApproveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approve_id):
            body['approveId'] = request.approve_id
        if not UtilClient.is_unset(request.op_userid):
            body['opUserid'] = request.op_userid
        if not UtilClient.is_unset(request.punch_param):
            body['punchParam'] = request.punch_param
        if not UtilClient.is_unset(request.sub_type):
            body['subType'] = request.sub_type
        if not UtilClient.is_unset(request.tag_name):
            body['tagName'] = request.tag_name
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
            dingtalkattendance__1__0_models.CreateApproveResponse(),
            self.do_roarequest('CreateApprove', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/approves', 'json', req, runtime)
        )

    async def create_approve_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.CreateApproveRequest,
        headers: dingtalkattendance__1__0_models.CreateApproveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.CreateApproveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approve_id):
            body['approveId'] = request.approve_id
        if not UtilClient.is_unset(request.op_userid):
            body['opUserid'] = request.op_userid
        if not UtilClient.is_unset(request.punch_param):
            body['punchParam'] = request.punch_param
        if not UtilClient.is_unset(request.sub_type):
            body['subType'] = request.sub_type
        if not UtilClient.is_unset(request.tag_name):
            body['tagName'] = request.tag_name
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
            dingtalkattendance__1__0_models.CreateApproveResponse(),
            await self.do_roarequest_async('CreateApprove', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/approves', 'json', req, runtime)
        )

    def ding_talk_security_check(
        self,
        request: dingtalkattendance__1__0_models.DingTalkSecurityCheckRequest,
    ) -> dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.DingTalkSecurityCheckHeaders()
        return self.ding_talk_security_check_with_options(request, headers, runtime)

    async def ding_talk_security_check_async(
        self,
        request: dingtalkattendance__1__0_models.DingTalkSecurityCheckRequest,
    ) -> dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.DingTalkSecurityCheckHeaders()
        return await self.ding_talk_security_check_with_options_async(request, headers, runtime)

    def ding_talk_security_check_with_options(
        self,
        request: dingtalkattendance__1__0_models.DingTalkSecurityCheckRequest,
        headers: dingtalkattendance__1__0_models.DingTalkSecurityCheckHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ver):
            body['clientVer'] = request.client_ver
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.platform_ver):
            body['platformVer'] = request.platform_ver
        if not UtilClient.is_unset(request.sec):
            body['sec'] = request.sec
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
            dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse(),
            self.do_roarequest('DingTalkSecurityCheck', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/securities/check', 'json', req, runtime)
        )

    async def ding_talk_security_check_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.DingTalkSecurityCheckRequest,
        headers: dingtalkattendance__1__0_models.DingTalkSecurityCheckHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ver):
            body['clientVer'] = request.client_ver
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.platform_ver):
            body['platformVer'] = request.platform_ver
        if not UtilClient.is_unset(request.sec):
            body['sec'] = request.sec
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
            dingtalkattendance__1__0_models.DingTalkSecurityCheckResponse(),
            await self.do_roarequest_async('DingTalkSecurityCheck', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/securities/check', 'json', req, runtime)
        )

    def get_closing_accounts(
        self,
        request: dingtalkattendance__1__0_models.GetClosingAccountsRequest,
    ) -> dingtalkattendance__1__0_models.GetClosingAccountsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetClosingAccountsHeaders()
        return self.get_closing_accounts_with_options(request, headers, runtime)

    async def get_closing_accounts_async(
        self,
        request: dingtalkattendance__1__0_models.GetClosingAccountsRequest,
    ) -> dingtalkattendance__1__0_models.GetClosingAccountsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetClosingAccountsHeaders()
        return await self.get_closing_accounts_with_options_async(request, headers, runtime)

    def get_closing_accounts_with_options(
        self,
        request: dingtalkattendance__1__0_models.GetClosingAccountsRequest,
        headers: dingtalkattendance__1__0_models.GetClosingAccountsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetClosingAccountsResponse:
        UtilClient.validate_model(request)
        body = {}
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
            dingtalkattendance__1__0_models.GetClosingAccountsResponse(),
            self.do_roarequest('GetClosingAccounts', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/closingAccounts/rules/query', 'json', req, runtime)
        )

    async def get_closing_accounts_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.GetClosingAccountsRequest,
        headers: dingtalkattendance__1__0_models.GetClosingAccountsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetClosingAccountsResponse:
        UtilClient.validate_model(request)
        body = {}
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
            dingtalkattendance__1__0_models.GetClosingAccountsResponse(),
            await self.do_roarequest_async('GetClosingAccounts', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/closingAccounts/rules/query', 'json', req, runtime)
        )

    def get_machine(
        self,
        dev_id: str,
    ) -> dingtalkattendance__1__0_models.GetMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetMachineHeaders()
        return self.get_machine_with_options(dev_id, headers, runtime)

    async def get_machine_async(
        self,
        dev_id: str,
    ) -> dingtalkattendance__1__0_models.GetMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetMachineHeaders()
        return await self.get_machine_with_options_async(dev_id, headers, runtime)

    def get_machine_with_options(
        self,
        dev_id: str,
        headers: dingtalkattendance__1__0_models.GetMachineHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetMachineResponse:
        dev_id = OpenApiUtilClient.get_encode_param(dev_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkattendance__1__0_models.GetMachineResponse(),
            self.do_roarequest('GetMachine', 'attendance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/attendance/machines/{dev_id}', 'json', req, runtime)
        )

    async def get_machine_with_options_async(
        self,
        dev_id: str,
        headers: dingtalkattendance__1__0_models.GetMachineHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetMachineResponse:
        dev_id = OpenApiUtilClient.get_encode_param(dev_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkattendance__1__0_models.GetMachineResponse(),
            await self.do_roarequest_async('GetMachine', 'attendance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/attendance/machines/{dev_id}', 'json', req, runtime)
        )

    def get_machine_user(
        self,
        dev_id: str,
        request: dingtalkattendance__1__0_models.GetMachineUserRequest,
    ) -> dingtalkattendance__1__0_models.GetMachineUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetMachineUserHeaders()
        return self.get_machine_user_with_options(dev_id, request, headers, runtime)

    async def get_machine_user_async(
        self,
        dev_id: str,
        request: dingtalkattendance__1__0_models.GetMachineUserRequest,
    ) -> dingtalkattendance__1__0_models.GetMachineUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetMachineUserHeaders()
        return await self.get_machine_user_with_options_async(dev_id, request, headers, runtime)

    def get_machine_user_with_options(
        self,
        dev_id: str,
        request: dingtalkattendance__1__0_models.GetMachineUserRequest,
        headers: dingtalkattendance__1__0_models.GetMachineUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetMachineUserResponse:
        UtilClient.validate_model(request)
        dev_id = OpenApiUtilClient.get_encode_param(dev_id)
        query = {}
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
            dingtalkattendance__1__0_models.GetMachineUserResponse(),
            self.do_roarequest('GetMachineUser', 'attendance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/attendance/machines/getUser/{dev_id}', 'json', req, runtime)
        )

    async def get_machine_user_with_options_async(
        self,
        dev_id: str,
        request: dingtalkattendance__1__0_models.GetMachineUserRequest,
        headers: dingtalkattendance__1__0_models.GetMachineUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetMachineUserResponse:
        UtilClient.validate_model(request)
        dev_id = OpenApiUtilClient.get_encode_param(dev_id)
        query = {}
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
            dingtalkattendance__1__0_models.GetMachineUserResponse(),
            await self.do_roarequest_async('GetMachineUser', 'attendance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/attendance/machines/getUser/{dev_id}', 'json', req, runtime)
        )

    def get_overtime_setting(
        self,
        request: dingtalkattendance__1__0_models.GetOvertimeSettingRequest,
    ) -> dingtalkattendance__1__0_models.GetOvertimeSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetOvertimeSettingHeaders()
        return self.get_overtime_setting_with_options(request, headers, runtime)

    async def get_overtime_setting_async(
        self,
        request: dingtalkattendance__1__0_models.GetOvertimeSettingRequest,
    ) -> dingtalkattendance__1__0_models.GetOvertimeSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetOvertimeSettingHeaders()
        return await self.get_overtime_setting_with_options_async(request, headers, runtime)

    def get_overtime_setting_with_options(
        self,
        request: dingtalkattendance__1__0_models.GetOvertimeSettingRequest,
        headers: dingtalkattendance__1__0_models.GetOvertimeSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetOvertimeSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overtime_setting_ids):
            body['overtimeSettingIds'] = request.overtime_setting_ids
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
            dingtalkattendance__1__0_models.GetOvertimeSettingResponse(),
            self.do_roarequest('GetOvertimeSetting', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/overtimeSettings/query', 'json', req, runtime)
        )

    async def get_overtime_setting_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.GetOvertimeSettingRequest,
        headers: dingtalkattendance__1__0_models.GetOvertimeSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetOvertimeSettingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overtime_setting_ids):
            body['overtimeSettingIds'] = request.overtime_setting_ids
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
            dingtalkattendance__1__0_models.GetOvertimeSettingResponse(),
            await self.do_roarequest_async('GetOvertimeSetting', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/overtimeSettings/query', 'json', req, runtime)
        )

    def get_user_holidays(
        self,
        request: dingtalkattendance__1__0_models.GetUserHolidaysRequest,
    ) -> dingtalkattendance__1__0_models.GetUserHolidaysResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetUserHolidaysHeaders()
        return self.get_user_holidays_with_options(request, headers, runtime)

    async def get_user_holidays_async(
        self,
        request: dingtalkattendance__1__0_models.GetUserHolidaysRequest,
    ) -> dingtalkattendance__1__0_models.GetUserHolidaysResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.GetUserHolidaysHeaders()
        return await self.get_user_holidays_with_options_async(request, headers, runtime)

    def get_user_holidays_with_options(
        self,
        request: dingtalkattendance__1__0_models.GetUserHolidaysRequest,
        headers: dingtalkattendance__1__0_models.GetUserHolidaysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetUserHolidaysResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.work_date_from):
            body['workDateFrom'] = request.work_date_from
        if not UtilClient.is_unset(request.work_date_to):
            body['workDateTo'] = request.work_date_to
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
            dingtalkattendance__1__0_models.GetUserHolidaysResponse(),
            self.do_roarequest('GetUserHolidays', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/holidays', 'json', req, runtime)
        )

    async def get_user_holidays_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.GetUserHolidaysRequest,
        headers: dingtalkattendance__1__0_models.GetUserHolidaysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.GetUserHolidaysResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.work_date_from):
            body['workDateFrom'] = request.work_date_from
        if not UtilClient.is_unset(request.work_date_to):
            body['workDateTo'] = request.work_date_to
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
            dingtalkattendance__1__0_models.GetUserHolidaysResponse(),
            await self.do_roarequest_async('GetUserHolidays', 'attendance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/attendance/holidays', 'json', req, runtime)
        )

    def sync_schedule_info(
        self,
        request: dingtalkattendance__1__0_models.SyncScheduleInfoRequest,
    ) -> dingtalkattendance__1__0_models.SyncScheduleInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.SyncScheduleInfoHeaders()
        return self.sync_schedule_info_with_options(request, headers, runtime)

    async def sync_schedule_info_async(
        self,
        request: dingtalkattendance__1__0_models.SyncScheduleInfoRequest,
    ) -> dingtalkattendance__1__0_models.SyncScheduleInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkattendance__1__0_models.SyncScheduleInfoHeaders()
        return await self.sync_schedule_info_with_options_async(request, headers, runtime)

    def sync_schedule_info_with_options(
        self,
        request: dingtalkattendance__1__0_models.SyncScheduleInfoRequest,
        headers: dingtalkattendance__1__0_models.SyncScheduleInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.SyncScheduleInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schedule_infos):
            body['scheduleInfos'] = request.schedule_infos
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
            dingtalkattendance__1__0_models.SyncScheduleInfoResponse(),
            self.do_roarequest('SyncScheduleInfo', 'attendance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/attendance/schedules/additionalInfo', 'none', req, runtime)
        )

    async def sync_schedule_info_with_options_async(
        self,
        request: dingtalkattendance__1__0_models.SyncScheduleInfoRequest,
        headers: dingtalkattendance__1__0_models.SyncScheduleInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkattendance__1__0_models.SyncScheduleInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.schedule_infos):
            body['scheduleInfos'] = request.schedule_infos
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
            dingtalkattendance__1__0_models.SyncScheduleInfoResponse(),
            await self.do_roarequest_async('SyncScheduleInfo', 'attendance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/attendance/schedules/additionalInfo', 'none', req, runtime)
        )
