# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.diot_1_0 import models as dingtalkdiot__1__0_models
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

    def batch_delete_device(
        self,
        request: dingtalkdiot__1__0_models.BatchDeleteDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchDeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchDeleteDeviceHeaders()
        return self.batch_delete_device_with_options(request, headers, runtime)

    async def batch_delete_device_async(
        self,
        request: dingtalkdiot__1__0_models.BatchDeleteDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchDeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchDeleteDeviceHeaders()
        return await self.batch_delete_device_with_options_async(request, headers, runtime)

    def batch_delete_device_with_options(
        self,
        request: dingtalkdiot__1__0_models.BatchDeleteDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchDeleteDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchDeleteDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_ids):
            body['deviceIds'] = request.device_ids
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
            dingtalkdiot__1__0_models.BatchDeleteDeviceResponse(),
            self.do_roarequest('BatchDeleteDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/remove', 'json', req, runtime)
        )

    async def batch_delete_device_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.BatchDeleteDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchDeleteDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchDeleteDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_ids):
            body['deviceIds'] = request.device_ids
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
            dingtalkdiot__1__0_models.BatchDeleteDeviceResponse(),
            await self.do_roarequest_async('BatchDeleteDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/remove', 'json', req, runtime)
        )

    def batch_register_device(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders()
        return self.batch_register_device_with_options(request, headers, runtime)

    async def batch_register_device_async(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders()
        return await self.batch_register_device_with_options_async(request, headers, runtime)

    def batch_register_device_with_options(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
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
            dingtalkdiot__1__0_models.BatchRegisterDeviceResponse(),
            self.do_roarequest('BatchRegisterDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/registrations/batch', 'json', req, runtime)
        )

    async def batch_register_device_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
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
            dingtalkdiot__1__0_models.BatchRegisterDeviceResponse(),
            await self.do_roarequest_async('BatchRegisterDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/registrations/batch', 'json', req, runtime)
        )

    def batch_register_event_type(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest,
    ) -> dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders()
        return self.batch_register_event_type_with_options(request, headers, runtime)

    async def batch_register_event_type_async(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest,
    ) -> dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders()
        return await self.batch_register_event_type_with_options_async(request, headers, runtime)

    def batch_register_event_type_with_options(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest,
        headers: dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.event_types):
            body['eventTypes'] = request.event_types
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
            dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse(),
            self.do_roarequest('BatchRegisterEventType', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/eventTypes/registrations/batch', 'json', req, runtime)
        )

    async def batch_register_event_type_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest,
        headers: dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.event_types):
            body['eventTypes'] = request.event_types
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
            dingtalkdiot__1__0_models.BatchRegisterEventTypeResponse(),
            await self.do_roarequest_async('BatchRegisterEventType', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/eventTypes/registrations/batch', 'json', req, runtime)
        )

    def batch_update_device(
        self,
        request: dingtalkdiot__1__0_models.BatchUpdateDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchUpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchUpdateDeviceHeaders()
        return self.batch_update_device_with_options(request, headers, runtime)

    async def batch_update_device_async(
        self,
        request: dingtalkdiot__1__0_models.BatchUpdateDeviceRequest,
    ) -> dingtalkdiot__1__0_models.BatchUpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BatchUpdateDeviceHeaders()
        return await self.batch_update_device_with_options_async(request, headers, runtime)

    def batch_update_device_with_options(
        self,
        request: dingtalkdiot__1__0_models.BatchUpdateDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchUpdateDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchUpdateDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
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
            dingtalkdiot__1__0_models.BatchUpdateDeviceResponse(),
            self.do_roarequest('BatchUpdateDevice', 'diot_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/diot/devices/batch', 'json', req, runtime)
        )

    async def batch_update_device_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.BatchUpdateDeviceRequest,
        headers: dingtalkdiot__1__0_models.BatchUpdateDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BatchUpdateDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
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
            dingtalkdiot__1__0_models.BatchUpdateDeviceResponse(),
            await self.do_roarequest_async('BatchUpdateDevice', 'diot_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/diot/devices/batch', 'json', req, runtime)
        )

    def bind_system(
        self,
        request: dingtalkdiot__1__0_models.BindSystemRequest,
    ) -> dingtalkdiot__1__0_models.BindSystemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BindSystemHeaders()
        return self.bind_system_with_options(request, headers, runtime)

    async def bind_system_async(
        self,
        request: dingtalkdiot__1__0_models.BindSystemRequest,
    ) -> dingtalkdiot__1__0_models.BindSystemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.BindSystemHeaders()
        return await self.bind_system_with_options_async(request, headers, runtime)

    def bind_system_with_options(
        self,
        request: dingtalkdiot__1__0_models.BindSystemRequest,
        headers: dingtalkdiot__1__0_models.BindSystemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BindSystemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_name):
            body['clientName'] = request.client_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.extra_data):
            body['extraData'] = request.extra_data
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
            dingtalkdiot__1__0_models.BindSystemResponse(),
            self.do_roarequest('BindSystem', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/systems/bind', 'json', req, runtime)
        )

    async def bind_system_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.BindSystemRequest,
        headers: dingtalkdiot__1__0_models.BindSystemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.BindSystemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_code):
            body['authCode'] = request.auth_code
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_name):
            body['clientName'] = request.client_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.extra_data):
            body['extraData'] = request.extra_data
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
            dingtalkdiot__1__0_models.BindSystemResponse(),
            await self.do_roarequest_async('BindSystem', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/systems/bind', 'json', req, runtime)
        )

    def device_conference(
        self,
        request: dingtalkdiot__1__0_models.DeviceConferenceRequest,
    ) -> dingtalkdiot__1__0_models.DeviceConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.DeviceConferenceHeaders()
        return self.device_conference_with_options(request, headers, runtime)

    async def device_conference_async(
        self,
        request: dingtalkdiot__1__0_models.DeviceConferenceRequest,
    ) -> dingtalkdiot__1__0_models.DeviceConferenceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.DeviceConferenceHeaders()
        return await self.device_conference_with_options_async(request, headers, runtime)

    def device_conference_with_options(
        self,
        request: dingtalkdiot__1__0_models.DeviceConferenceRequest,
        headers: dingtalkdiot__1__0_models.DeviceConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.DeviceConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['confTitle'] = request.conf_title
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.conference_password):
            body['conferencePassword'] = request.conference_password
        if not UtilClient.is_unset(request.device_ids):
            body['deviceIds'] = request.device_ids
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
            dingtalkdiot__1__0_models.DeviceConferenceResponse(),
            self.do_roarequest('DeviceConference', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/deviceConferences/initiate', 'json', req, runtime)
        )

    async def device_conference_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.DeviceConferenceRequest,
        headers: dingtalkdiot__1__0_models.DeviceConferenceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.DeviceConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['confTitle'] = request.conf_title
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.conference_password):
            body['conferencePassword'] = request.conference_password
        if not UtilClient.is_unset(request.device_ids):
            body['deviceIds'] = request.device_ids
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
            dingtalkdiot__1__0_models.DeviceConferenceResponse(),
            await self.do_roarequest_async('DeviceConference', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/deviceConferences/initiate', 'json', req, runtime)
        )

    def push_event(
        self,
        request: dingtalkdiot__1__0_models.PushEventRequest,
    ) -> dingtalkdiot__1__0_models.PushEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.PushEventHeaders()
        return self.push_event_with_options(request, headers, runtime)

    async def push_event_async(
        self,
        request: dingtalkdiot__1__0_models.PushEventRequest,
    ) -> dingtalkdiot__1__0_models.PushEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.PushEventHeaders()
        return await self.push_event_with_options_async(request, headers, runtime)

    def push_event_with_options(
        self,
        request: dingtalkdiot__1__0_models.PushEventRequest,
        headers: dingtalkdiot__1__0_models.PushEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.PushEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.event_id):
            body['eventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            body['eventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['eventType'] = request.event_type
        if not UtilClient.is_unset(request.extra_data):
            body['extraData'] = request.extra_data
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.msg):
            body['msg'] = request.msg
        if not UtilClient.is_unset(request.occurrence_time):
            body['occurrenceTime'] = request.occurrence_time
        if not UtilClient.is_unset(request.pic_urls):
            body['picUrls'] = request.pic_urls
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
            dingtalkdiot__1__0_models.PushEventResponse(),
            self.do_roarequest('PushEvent', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/events/push', 'json', req, runtime)
        )

    async def push_event_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.PushEventRequest,
        headers: dingtalkdiot__1__0_models.PushEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.PushEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.event_id):
            body['eventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            body['eventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['eventType'] = request.event_type
        if not UtilClient.is_unset(request.extra_data):
            body['extraData'] = request.extra_data
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.msg):
            body['msg'] = request.msg
        if not UtilClient.is_unset(request.occurrence_time):
            body['occurrenceTime'] = request.occurrence_time
        if not UtilClient.is_unset(request.pic_urls):
            body['picUrls'] = request.pic_urls
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
            dingtalkdiot__1__0_models.PushEventResponse(),
            await self.do_roarequest_async('PushEvent', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/events/push', 'json', req, runtime)
        )

    def query_device(
        self,
        request: dingtalkdiot__1__0_models.QueryDeviceRequest,
    ) -> dingtalkdiot__1__0_models.QueryDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.QueryDeviceHeaders()
        return self.query_device_with_options(request, headers, runtime)

    async def query_device_async(
        self,
        request: dingtalkdiot__1__0_models.QueryDeviceRequest,
    ) -> dingtalkdiot__1__0_models.QueryDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.QueryDeviceHeaders()
        return await self.query_device_with_options_async(request, headers, runtime)

    def query_device_with_options(
        self,
        request: dingtalkdiot__1__0_models.QueryDeviceRequest,
        headers: dingtalkdiot__1__0_models.QueryDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.QueryDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkdiot__1__0_models.QueryDeviceResponse(),
            self.do_roarequest('QueryDevice', 'diot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/diot/devices', 'json', req, runtime)
        )

    async def query_device_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.QueryDeviceRequest,
        headers: dingtalkdiot__1__0_models.QueryDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.QueryDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkdiot__1__0_models.QueryDeviceResponse(),
            await self.do_roarequest_async('QueryDevice', 'diot_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/diot/devices', 'json', req, runtime)
        )

    def register_device(
        self,
        request: dingtalkdiot__1__0_models.RegisterDeviceRequest,
    ) -> dingtalkdiot__1__0_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.RegisterDeviceHeaders()
        return self.register_device_with_options(request, headers, runtime)

    async def register_device_async(
        self,
        request: dingtalkdiot__1__0_models.RegisterDeviceRequest,
    ) -> dingtalkdiot__1__0_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdiot__1__0_models.RegisterDeviceHeaders()
        return await self.register_device_with_options_async(request, headers, runtime)

    def register_device_with_options(
        self,
        request: dingtalkdiot__1__0_models.RegisterDeviceRequest,
        headers: dingtalkdiot__1__0_models.RegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_status):
            body['deviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.device_type):
            body['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_type_name):
            body['deviceTypeName'] = request.device_type_name
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.live_urls):
            body['liveUrls'] = request.live_urls
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.nick_name):
            body['nickName'] = request.nick_name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
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
            dingtalkdiot__1__0_models.RegisterDeviceResponse(),
            self.do_roarequest('RegisterDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/register', 'json', req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: dingtalkdiot__1__0_models.RegisterDeviceRequest,
        headers: dingtalkdiot__1__0_models.RegisterDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdiot__1__0_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_name):
            body['deviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_status):
            body['deviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.device_type):
            body['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_type_name):
            body['deviceTypeName'] = request.device_type_name
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.live_urls):
            body['liveUrls'] = request.live_urls
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.nick_name):
            body['nickName'] = request.nick_name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
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
            dingtalkdiot__1__0_models.RegisterDeviceResponse(),
            await self.do_roarequest_async('RegisterDevice', 'diot_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/diot/devices/register', 'json', req, runtime)
        )
