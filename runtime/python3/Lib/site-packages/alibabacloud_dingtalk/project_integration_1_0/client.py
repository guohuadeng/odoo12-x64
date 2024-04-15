# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.project_integration_1_0 import models as dingtalkproject_integration__1__0_models
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

    def add_attendee_to_event_group(
        self,
        user_id: str,
        group_id: str,
    ) -> dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupHeaders()
        return self.add_attendee_to_event_group_with_options(user_id, group_id, headers, runtime)

    async def add_attendee_to_event_group_async(
        self,
        user_id: str,
        group_id: str,
    ) -> dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupHeaders()
        return await self.add_attendee_to_event_group_with_options_async(user_id, group_id, headers, runtime)

    def add_attendee_to_event_group_with_options(
        self,
        user_id: str,
        group_id: str,
        headers: dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse(),
            self.do_roarequest('AddAttendeeToEventGroup', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/eventGroups/{group_id}/members', 'json', req, runtime)
        )

    async def add_attendee_to_event_group_with_options_async(
        self,
        user_id: str,
        group_id: str,
        headers: dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.AddAttendeeToEventGroupResponse(),
            await self.do_roarequest_async('AddAttendeeToEventGroup', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/eventGroups/{group_id}/members', 'json', req, runtime)
        )

    def create_event_group(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.CreateEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.CreateEventGroupHeaders()
        return self.create_event_group_with_options(user_id, headers, runtime)

    async def create_event_group_async(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.CreateEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.CreateEventGroupHeaders()
        return await self.create_event_group_with_options_async(user_id, headers, runtime)

    def create_event_group_with_options(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.CreateEventGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.CreateEventGroupResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.CreateEventGroupResponse(),
            self.do_roarequest('CreateEventGroup', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/eventGroups', 'json', req, runtime)
        )

    async def create_event_group_with_options_async(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.CreateEventGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.CreateEventGroupResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.CreateEventGroupResponse(),
            await self.do_roarequest_async('CreateEventGroup', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/eventGroups', 'json', req, runtime)
        )

    def send_interactive_card(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.SendInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.SendInteractiveCardHeaders()
        return self.send_interactive_card_with_options(user_id, headers, runtime)

    async def send_interactive_card_async(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.SendInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.SendInteractiveCardHeaders()
        return await self.send_interactive_card_with_options_async(user_id, headers, runtime)

    def send_interactive_card_with_options(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.SendInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.SendInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.SendInteractiveCardResponse(),
            self.do_roarequest('SendInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/groupChatCardMessages', 'json', req, runtime)
        )

    async def send_interactive_card_with_options_async(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.SendInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.SendInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.SendInteractiveCardResponse(),
            await self.do_roarequest_async('SendInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/groupChatCardMessages', 'json', req, runtime)
        )

    def send_single_interactive_card(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.SendSingleInteractiveCardHeaders()
        return self.send_single_interactive_card_with_options(user_id, headers, runtime)

    async def send_single_interactive_card_async(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.SendSingleInteractiveCardHeaders()
        return await self.send_single_interactive_card_with_options_async(user_id, headers, runtime)

    def send_single_interactive_card_with_options(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.SendSingleInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse(),
            self.do_roarequest('SendSingleInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/singleChatCardMessages', 'json', req, runtime)
        )

    async def send_single_interactive_card_with_options_async(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.SendSingleInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.SendSingleInteractiveCardResponse(),
            await self.do_roarequest_async('SendSingleInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/projectIntegration/users/{user_id}/singleChatCardMessages', 'json', req, runtime)
        )

    def update_interactive_card(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.UpdateInteractiveCardHeaders()
        return self.update_interactive_card_with_options(user_id, headers, runtime)

    async def update_interactive_card_async(
        self,
        user_id: str,
    ) -> dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkproject_integration__1__0_models.UpdateInteractiveCardHeaders()
        return await self.update_interactive_card_with_options_async(user_id, headers, runtime)

    def update_interactive_card_with_options(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.UpdateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse(),
            self.do_roarequest('UpdateInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/projectIntegration/users/{user_id}/cardMessages', 'json', req, runtime)
        )

    async def update_interactive_card_with_options_async(
        self,
        user_id: str,
        headers: dingtalkproject_integration__1__0_models.UpdateInteractiveCardHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkproject_integration__1__0_models.UpdateInteractiveCardResponse(),
            await self.do_roarequest_async('UpdateInteractiveCard', 'projectIntegration_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/projectIntegration/users/{user_id}/cardMessages', 'json', req, runtime)
        )
