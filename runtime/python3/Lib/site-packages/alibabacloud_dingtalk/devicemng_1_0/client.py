# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.devicemng_1_0 import models as dingtalkdevicemng__1__0_models
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

    def batch_register_device(
        self,
        request: dingtalkdevicemng__1__0_models.BatchRegisterDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.BatchRegisterDeviceHeaders()
        return self.batch_register_device_with_options(request, headers, runtime)

    async def batch_register_device_async(
        self,
        request: dingtalkdevicemng__1__0_models.BatchRegisterDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.BatchRegisterDeviceHeaders()
        return await self.batch_register_device_with_options_async(request, headers, runtime)

    def batch_register_device_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.BatchRegisterDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.BatchRegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_list):
            body['deviceList'] = request.device_list
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
            dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse(),
            self.do_roarequest('BatchRegisterDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/devices/batch', 'json', req, runtime)
        )

    async def batch_register_device_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.BatchRegisterDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.BatchRegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_list):
            body['deviceList'] = request.device_list
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
            dingtalkdevicemng__1__0_models.BatchRegisterDeviceResponse(),
            await self.do_roarequest_async('BatchRegisterDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/devices/batch', 'json', req, runtime)
        )

    def create_chat_room(
        self,
        request: dingtalkdevicemng__1__0_models.CreateChatRoomRequest,
    ) -> dingtalkdevicemng__1__0_models.CreateChatRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.CreateChatRoomHeaders()
        return self.create_chat_room_with_options(request, headers, runtime)

    async def create_chat_room_async(
        self,
        request: dingtalkdevicemng__1__0_models.CreateChatRoomRequest,
    ) -> dingtalkdevicemng__1__0_models.CreateChatRoomResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.CreateChatRoomHeaders()
        return await self.create_chat_room_with_options_async(request, headers, runtime)

    def create_chat_room_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.CreateChatRoomRequest,
        headers: dingtalkdevicemng__1__0_models.CreateChatRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.CreateChatRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chat_group_name):
            body['chatGroupName'] = request.chat_group_name
        if not UtilClient.is_unset(request.device_codes):
            body['deviceCodes'] = request.device_codes
        if not UtilClient.is_unset(request.device_type_id):
            body['deviceTypeId'] = request.device_type_id
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.role_list):
            body['roleList'] = request.role_list
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
            dingtalkdevicemng__1__0_models.CreateChatRoomResponse(),
            self.do_roarequest('CreateChatRoom', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/chatRoom', 'json', req, runtime)
        )

    async def create_chat_room_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.CreateChatRoomRequest,
        headers: dingtalkdevicemng__1__0_models.CreateChatRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.CreateChatRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chat_group_name):
            body['chatGroupName'] = request.chat_group_name
        if not UtilClient.is_unset(request.device_codes):
            body['deviceCodes'] = request.device_codes
        if not UtilClient.is_unset(request.device_type_id):
            body['deviceTypeId'] = request.device_type_id
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.role_list):
            body['roleList'] = request.role_list
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
            dingtalkdevicemng__1__0_models.CreateChatRoomResponse(),
            await self.do_roarequest_async('CreateChatRoom', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/chatRoom', 'json', req, runtime)
        )

    def create_department(
        self,
        request: dingtalkdevicemng__1__0_models.CreateDepartmentRequest,
    ) -> dingtalkdevicemng__1__0_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.CreateDepartmentHeaders()
        return self.create_department_with_options(request, headers, runtime)

    async def create_department_async(
        self,
        request: dingtalkdevicemng__1__0_models.CreateDepartmentRequest,
    ) -> dingtalkdevicemng__1__0_models.CreateDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.CreateDepartmentHeaders()
        return await self.create_department_with_options_async(request, headers, runtime)

    def create_department_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.CreateDepartmentRequest,
        headers: dingtalkdevicemng__1__0_models.CreateDepartmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_info):
            body['authInfo'] = request.auth_info
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.biz_ext):
            body['bizExt'] = request.biz_ext
        if not UtilClient.is_unset(request.department_name):
            body['departmentName'] = request.department_name
        if not UtilClient.is_unset(request.department_type):
            body['departmentType'] = request.department_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.system_url):
            body['systemUrl'] = request.system_url
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
            dingtalkdevicemng__1__0_models.CreateDepartmentResponse(),
            self.do_roarequest('CreateDepartment', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/departments', 'json', req, runtime)
        )

    async def create_department_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.CreateDepartmentRequest,
        headers: dingtalkdevicemng__1__0_models.CreateDepartmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.CreateDepartmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_info):
            body['authInfo'] = request.auth_info
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.biz_ext):
            body['bizExt'] = request.biz_ext
        if not UtilClient.is_unset(request.department_name):
            body['departmentName'] = request.department_name
        if not UtilClient.is_unset(request.department_type):
            body['departmentType'] = request.department_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.system_url):
            body['systemUrl'] = request.system_url
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
            dingtalkdevicemng__1__0_models.CreateDepartmentResponse(),
            await self.do_roarequest_async('CreateDepartment', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/departments', 'json', req, runtime)
        )

    def device_ding(
        self,
        request: dingtalkdevicemng__1__0_models.DeviceDingRequest,
    ) -> dingtalkdevicemng__1__0_models.DeviceDingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.DeviceDingHeaders()
        return self.device_ding_with_options(request, headers, runtime)

    async def device_ding_async(
        self,
        request: dingtalkdevicemng__1__0_models.DeviceDingRequest,
    ) -> dingtalkdevicemng__1__0_models.DeviceDingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.DeviceDingHeaders()
        return await self.device_ding_with_options_async(request, headers, runtime)

    def device_ding_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.DeviceDingRequest,
        headers: dingtalkdevicemng__1__0_models.DeviceDingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.DeviceDingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_key):
            body['deviceKey'] = request.device_key
        if not UtilClient.is_unset(request.params_json):
            body['paramsJson'] = request.params_json
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
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
            dingtalkdevicemng__1__0_models.DeviceDingResponse(),
            self.do_roarequest('DeviceDing', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/ding', 'json', req, runtime)
        )

    async def device_ding_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.DeviceDingRequest,
        headers: dingtalkdevicemng__1__0_models.DeviceDingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.DeviceDingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_key):
            body['deviceKey'] = request.device_key
        if not UtilClient.is_unset(request.params_json):
            body['paramsJson'] = request.params_json
        if not UtilClient.is_unset(request.receiver_user_id_list):
            body['receiverUserIdList'] = request.receiver_user_id_list
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
            dingtalkdevicemng__1__0_models.DeviceDingResponse(),
            await self.do_roarequest_async('DeviceDing', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/ding', 'json', req, runtime)
        )

    def list_activate_devices(
        self,
        request: dingtalkdevicemng__1__0_models.ListActivateDevicesRequest,
    ) -> dingtalkdevicemng__1__0_models.ListActivateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders()
        return self.list_activate_devices_with_options(request, headers, runtime)

    async def list_activate_devices_async(
        self,
        request: dingtalkdevicemng__1__0_models.ListActivateDevicesRequest,
    ) -> dingtalkdevicemng__1__0_models.ListActivateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders()
        return await self.list_activate_devices_with_options_async(request, headers, runtime)

    def list_activate_devices_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.ListActivateDevicesRequest,
        headers: dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.ListActivateDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_type_id):
            query['deviceTypeId'] = request.device_type_id
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
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
            dingtalkdevicemng__1__0_models.ListActivateDevicesResponse(),
            self.do_roarequest('ListActivateDevices', 'devicemng_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/devicemng/customers/devices/activations/infos', 'json', req, runtime)
        )

    async def list_activate_devices_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.ListActivateDevicesRequest,
        headers: dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.ListActivateDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_code):
            query['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_type_id):
            query['deviceTypeId'] = request.device_type_id
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
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
            dingtalkdevicemng__1__0_models.ListActivateDevicesResponse(),
            await self.do_roarequest_async('ListActivateDevices', 'devicemng_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/devicemng/customers/devices/activations/infos', 'json', req, runtime)
        )

    def register_and_activate_device(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders()
        return self.register_and_activate_device_with_options(request, headers, runtime)

    async def register_and_activate_device_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders()
        return await self.register_and_activate_device_with_options_async(request, headers, runtime)

    def register_and_activate_device_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_callback_url):
            body['deviceCallbackUrl'] = request.device_callback_url
        if not UtilClient.is_unset(request.device_code):
            body['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_detail_url):
            body['deviceDetailUrl'] = request.device_detail_url
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.introduction):
            body['introduction'] = request.introduction
        if not UtilClient.is_unset(request.role_uuid):
            body['roleUuid'] = request.role_uuid
        if not UtilClient.is_unset(request.type_uuid):
            body['typeUuid'] = request.type_uuid
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
            dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse(),
            self.do_roarequest('RegisterAndActivateDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/devices/registerAndActivate', 'json', req, runtime)
        )

    async def register_and_activate_device_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_callback_url):
            body['deviceCallbackUrl'] = request.device_callback_url
        if not UtilClient.is_unset(request.device_code):
            body['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_detail_url):
            body['deviceDetailUrl'] = request.device_detail_url
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.introduction):
            body['introduction'] = request.introduction
        if not UtilClient.is_unset(request.role_uuid):
            body['roleUuid'] = request.role_uuid
        if not UtilClient.is_unset(request.type_uuid):
            body['typeUuid'] = request.type_uuid
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
            dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceResponse(),
            await self.do_roarequest_async('RegisterAndActivateDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/devices/registerAndActivate', 'json', req, runtime)
        )

    def register_and_activate_device_batch(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders()
        return self.register_and_activate_device_batch_with_options(request, headers, runtime)

    async def register_and_activate_device_batch_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders()
        return await self.register_and_activate_device_batch_with_options_async(request, headers, runtime)

    def register_and_activate_device_batch_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.register_and_activate_vos):
            body['registerAndActivateVOS'] = request.register_and_activate_vos
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
            dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse(),
            self.do_roarequest('RegisterAndActivateDeviceBatch', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/devices/registrationActivations/batch', 'json', req, runtime)
        )

    async def register_and_activate_device_batch_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.register_and_activate_vos):
            body['registerAndActivateVOS'] = request.register_and_activate_vos
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
            dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchResponse(),
            await self.do_roarequest_async('RegisterAndActivateDeviceBatch', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/customers/devices/registrationActivations/batch', 'json', req, runtime)
        )

    def register_device(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterDeviceHeaders()
        return self.register_device_with_options(request, headers, runtime)

    async def register_device_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterDeviceRequest,
    ) -> dingtalkdevicemng__1__0_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.RegisterDeviceHeaders()
        return await self.register_device_with_options_async(request, headers, runtime)

    def register_device_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collaborators):
            body['collaborators'] = request.collaborators
        if not UtilClient.is_unset(request.department_id):
            body['departmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.device_key):
            body['deviceKey'] = request.device_key
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
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
            dingtalkdevicemng__1__0_models.RegisterDeviceResponse(),
            self.do_roarequest('RegisterDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/devices', 'json', req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.RegisterDeviceRequest,
        headers: dingtalkdevicemng__1__0_models.RegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.collaborators):
            body['collaborators'] = request.collaborators
        if not UtilClient.is_unset(request.department_id):
            body['departmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.device_key):
            body['deviceKey'] = request.device_key
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
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
            dingtalkdevicemng__1__0_models.RegisterDeviceResponse(),
            await self.do_roarequest_async('RegisterDevice', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/devices', 'json', req, runtime)
        )

    def upload_event(
        self,
        request: dingtalkdevicemng__1__0_models.UploadEventRequest,
    ) -> dingtalkdevicemng__1__0_models.UploadEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.UploadEventHeaders()
        return self.upload_event_with_options(request, headers, runtime)

    async def upload_event_async(
        self,
        request: dingtalkdevicemng__1__0_models.UploadEventRequest,
    ) -> dingtalkdevicemng__1__0_models.UploadEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdevicemng__1__0_models.UploadEventHeaders()
        return await self.upload_event_with_options_async(request, headers, runtime)

    def upload_event_with_options(
        self,
        request: dingtalkdevicemng__1__0_models.UploadEventRequest,
        headers: dingtalkdevicemng__1__0_models.UploadEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.UploadEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.device_code):
            body['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_uuid):
            body['deviceUuid'] = request.device_uuid
        if not UtilClient.is_unset(request.event_time):
            body['eventTime'] = request.event_time
        if not UtilClient.is_unset(request.event_type):
            body['eventType'] = request.event_type
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
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
            dingtalkdevicemng__1__0_models.UploadEventResponse(),
            self.do_roarequest('UploadEvent', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/suppliers/events/upload', 'json', req, runtime)
        )

    async def upload_event_with_options_async(
        self,
        request: dingtalkdevicemng__1__0_models.UploadEventRequest,
        headers: dingtalkdevicemng__1__0_models.UploadEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdevicemng__1__0_models.UploadEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.device_code):
            body['deviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_uuid):
            body['deviceUuid'] = request.device_uuid
        if not UtilClient.is_unset(request.event_time):
            body['eventTime'] = request.event_time
        if not UtilClient.is_unset(request.event_type):
            body['eventType'] = request.event_type
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
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
            dingtalkdevicemng__1__0_models.UploadEventResponse(),
            await self.do_roarequest_async('UploadEvent', 'devicemng_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/devicemng/suppliers/events/upload', 'json', req, runtime)
        )
