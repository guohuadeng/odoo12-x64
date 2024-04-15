# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
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

    def approval_list(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.ApprovalListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ApprovalListHeaders()
        return self.approval_list_with_options(task_id, headers, runtime)

    async def approval_list_async(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.ApprovalListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ApprovalListHeaders()
        return await self.approval_list_with_options_async(task_id, headers, runtime)

    def approval_list_with_options(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.ApprovalListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ApprovalListResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ApprovalListResponse(),
            self.do_roarequest('ApprovalList', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/approvals/{task_id}', 'json', req, runtime)
        )

    async def approval_list_with_options_async(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.ApprovalListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ApprovalListResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ApprovalListResponse(),
            await self.do_roarequest_async('ApprovalList', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/approvals/{task_id}', 'json', req, runtime)
        )

    def cancel_corp_auth(
        self,
        request: dingtalkesign__2__0_models.CancelCorpAuthRequest,
    ) -> dingtalkesign__2__0_models.CancelCorpAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CancelCorpAuthHeaders()
        return self.cancel_corp_auth_with_options(request, headers, runtime)

    async def cancel_corp_auth_async(
        self,
        request: dingtalkesign__2__0_models.CancelCorpAuthRequest,
    ) -> dingtalkesign__2__0_models.CancelCorpAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CancelCorpAuthHeaders()
        return await self.cancel_corp_auth_with_options_async(request, headers, runtime)

    def cancel_corp_auth_with_options(
        self,
        request: dingtalkesign__2__0_models.CancelCorpAuthRequest,
        headers: dingtalkesign__2__0_models.CancelCorpAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CancelCorpAuthResponse:
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CancelCorpAuthResponse(),
            self.do_roarequest('CancelCorpAuth', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/auths/cancel', 'json', req, runtime)
        )

    async def cancel_corp_auth_with_options_async(
        self,
        request: dingtalkesign__2__0_models.CancelCorpAuthRequest,
        headers: dingtalkesign__2__0_models.CancelCorpAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CancelCorpAuthResponse:
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CancelCorpAuthResponse(),
            await self.do_roarequest_async('CancelCorpAuth', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/auths/cancel', 'json', req, runtime)
        )

    def channel_orders(
        self,
        request: dingtalkesign__2__0_models.ChannelOrdersRequest,
    ) -> dingtalkesign__2__0_models.ChannelOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ChannelOrdersHeaders()
        return self.channel_orders_with_options(request, headers, runtime)

    async def channel_orders_async(
        self,
        request: dingtalkesign__2__0_models.ChannelOrdersRequest,
    ) -> dingtalkesign__2__0_models.ChannelOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ChannelOrdersHeaders()
        return await self.channel_orders_with_options_async(request, headers, runtime)

    def channel_orders_with_options(
        self,
        request: dingtalkesign__2__0_models.ChannelOrdersRequest,
        headers: dingtalkesign__2__0_models.ChannelOrdersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ChannelOrdersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_code):
            body['itemCode'] = request.item_code
        if not UtilClient.is_unset(request.item_name):
            body['itemName'] = request.item_name
        if not UtilClient.is_unset(request.order_create_time):
            body['orderCreateTime'] = request.order_create_time
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.pay_fee):
            body['payFee'] = request.pay_fee
        if not UtilClient.is_unset(request.quantity):
            body['quantity'] = request.quantity
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ChannelOrdersResponse(),
            self.do_roarequest('ChannelOrders', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/orders/channel', 'json', req, runtime)
        )

    async def channel_orders_with_options_async(
        self,
        request: dingtalkesign__2__0_models.ChannelOrdersRequest,
        headers: dingtalkesign__2__0_models.ChannelOrdersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ChannelOrdersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_code):
            body['itemCode'] = request.item_code
        if not UtilClient.is_unset(request.item_name):
            body['itemName'] = request.item_name
        if not UtilClient.is_unset(request.order_create_time):
            body['orderCreateTime'] = request.order_create_time
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.pay_fee):
            body['payFee'] = request.pay_fee
        if not UtilClient.is_unset(request.quantity):
            body['quantity'] = request.quantity
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ChannelOrdersResponse(),
            await self.do_roarequest_async('ChannelOrders', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/orders/channel', 'json', req, runtime)
        )

    def corp_realname(
        self,
        request: dingtalkesign__2__0_models.CorpRealnameRequest,
    ) -> dingtalkesign__2__0_models.CorpRealnameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CorpRealnameHeaders()
        return self.corp_realname_with_options(request, headers, runtime)

    async def corp_realname_async(
        self,
        request: dingtalkesign__2__0_models.CorpRealnameRequest,
    ) -> dingtalkesign__2__0_models.CorpRealnameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CorpRealnameHeaders()
        return await self.corp_realname_with_options_async(request, headers, runtime)

    def corp_realname_with_options(
        self,
        request: dingtalkesign__2__0_models.CorpRealnameRequest,
        headers: dingtalkesign__2__0_models.CorpRealnameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CorpRealnameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CorpRealnameResponse(),
            self.do_roarequest('CorpRealname', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/corps/realnames', 'json', req, runtime)
        )

    async def corp_realname_with_options_async(
        self,
        request: dingtalkesign__2__0_models.CorpRealnameRequest,
        headers: dingtalkesign__2__0_models.CorpRealnameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CorpRealnameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CorpRealnameResponse(),
            await self.do_roarequest_async('CorpRealname', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/corps/realnames', 'json', req, runtime)
        )

    def create_developers(
        self,
        request: dingtalkesign__2__0_models.CreateDevelopersRequest,
    ) -> dingtalkesign__2__0_models.CreateDevelopersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CreateDevelopersHeaders()
        return self.create_developers_with_options(request, headers, runtime)

    async def create_developers_async(
        self,
        request: dingtalkesign__2__0_models.CreateDevelopersRequest,
    ) -> dingtalkesign__2__0_models.CreateDevelopersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CreateDevelopersHeaders()
        return await self.create_developers_with_options_async(request, headers, runtime)

    def create_developers_with_options(
        self,
        request: dingtalkesign__2__0_models.CreateDevelopersRequest,
        headers: dingtalkesign__2__0_models.CreateDevelopersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CreateDevelopersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notice_url):
            body['noticeUrl'] = request.notice_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CreateDevelopersResponse(),
            self.do_roarequest('CreateDevelopers', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/developers', 'json', req, runtime)
        )

    async def create_developers_with_options_async(
        self,
        request: dingtalkesign__2__0_models.CreateDevelopersRequest,
        headers: dingtalkesign__2__0_models.CreateDevelopersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CreateDevelopersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notice_url):
            body['noticeUrl'] = request.notice_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.CreateDevelopersResponse(),
            await self.do_roarequest_async('CreateDevelopers', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/developers', 'json', req, runtime)
        )

    def create_process(
        self,
        request: dingtalkesign__2__0_models.CreateProcessRequest,
    ) -> dingtalkesign__2__0_models.CreateProcessResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CreateProcessHeaders()
        return self.create_process_with_options(request, headers, runtime)

    async def create_process_async(
        self,
        request: dingtalkesign__2__0_models.CreateProcessRequest,
    ) -> dingtalkesign__2__0_models.CreateProcessResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.CreateProcessHeaders()
        return await self.create_process_with_options_async(request, headers, runtime)

    def create_process_with_options(
        self,
        request: dingtalkesign__2__0_models.CreateProcessRequest,
        headers: dingtalkesign__2__0_models.CreateProcessHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CreateProcessResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ccs):
            body['ccs'] = request.ccs
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.initiator_user_id):
            body['initiatorUserId'] = request.initiator_user_id
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.sign_end_time):
            body['signEndTime'] = request.sign_end_time
        if not UtilClient.is_unset(request.source_info):
            body['sourceInfo'] = request.source_info
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
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
            dingtalkesign__2__0_models.CreateProcessResponse(),
            self.do_roarequest('CreateProcess', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/process/startAtOnce', 'json', req, runtime)
        )

    async def create_process_with_options_async(
        self,
        request: dingtalkesign__2__0_models.CreateProcessRequest,
        headers: dingtalkesign__2__0_models.CreateProcessHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.CreateProcessResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ccs):
            body['ccs'] = request.ccs
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.initiator_user_id):
            body['initiatorUserId'] = request.initiator_user_id
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.sign_end_time):
            body['signEndTime'] = request.sign_end_time
        if not UtilClient.is_unset(request.source_info):
            body['sourceInfo'] = request.source_info
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
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
            dingtalkesign__2__0_models.CreateProcessResponse(),
            await self.do_roarequest_async('CreateProcess', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/process/startAtOnce', 'json', req, runtime)
        )

    def get_attachs_approval(
        self,
        instance_id: str,
    ) -> dingtalkesign__2__0_models.GetAttachsApprovalResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetAttachsApprovalHeaders()
        return self.get_attachs_approval_with_options(instance_id, headers, runtime)

    async def get_attachs_approval_async(
        self,
        instance_id: str,
    ) -> dingtalkesign__2__0_models.GetAttachsApprovalResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetAttachsApprovalHeaders()
        return await self.get_attachs_approval_with_options_async(instance_id, headers, runtime)

    def get_attachs_approval_with_options(
        self,
        instance_id: str,
        headers: dingtalkesign__2__0_models.GetAttachsApprovalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetAttachsApprovalResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.tsign_open_app_id):
            real_headers['tsignOpenAppId'] = UtilClient.to_jsonstring(headers.tsign_open_app_id)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetAttachsApprovalResponse(),
            self.do_roarequest('GetAttachsApproval', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/dingInstances/{instance_id}/attachments', 'json', req, runtime)
        )

    async def get_attachs_approval_with_options_async(
        self,
        instance_id: str,
        headers: dingtalkesign__2__0_models.GetAttachsApprovalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetAttachsApprovalResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.tsign_open_app_id):
            real_headers['tsignOpenAppId'] = UtilClient.to_jsonstring(headers.tsign_open_app_id)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetAttachsApprovalResponse(),
            await self.do_roarequest_async('GetAttachsApproval', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/dingInstances/{instance_id}/attachments', 'json', req, runtime)
        )

    def get_auth_url(
        self,
        request: dingtalkesign__2__0_models.GetAuthUrlRequest,
    ) -> dingtalkesign__2__0_models.GetAuthUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetAuthUrlHeaders()
        return self.get_auth_url_with_options(request, headers, runtime)

    async def get_auth_url_async(
        self,
        request: dingtalkesign__2__0_models.GetAuthUrlRequest,
    ) -> dingtalkesign__2__0_models.GetAuthUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetAuthUrlHeaders()
        return await self.get_auth_url_with_options_async(request, headers, runtime)

    def get_auth_url_with_options(
        self,
        request: dingtalkesign__2__0_models.GetAuthUrlRequest,
        headers: dingtalkesign__2__0_models.GetAuthUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetAuthUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetAuthUrlResponse(),
            self.do_roarequest('GetAuthUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/auths/urls', 'json', req, runtime)
        )

    async def get_auth_url_with_options_async(
        self,
        request: dingtalkesign__2__0_models.GetAuthUrlRequest,
        headers: dingtalkesign__2__0_models.GetAuthUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetAuthUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetAuthUrlResponse(),
            await self.do_roarequest_async('GetAuthUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/auths/urls', 'json', req, runtime)
        )

    def get_contract_margin(self) -> dingtalkesign__2__0_models.GetContractMarginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetContractMarginHeaders()
        return self.get_contract_margin_with_options(headers, runtime)

    async def get_contract_margin_async(self) -> dingtalkesign__2__0_models.GetContractMarginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetContractMarginHeaders()
        return await self.get_contract_margin_with_options_async(headers, runtime)

    def get_contract_margin_with_options(
        self,
        headers: dingtalkesign__2__0_models.GetContractMarginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetContractMarginResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetContractMarginResponse(),
            self.do_roarequest('GetContractMargin', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/margins', 'json', req, runtime)
        )

    async def get_contract_margin_with_options_async(
        self,
        headers: dingtalkesign__2__0_models.GetContractMarginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetContractMarginResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetContractMarginResponse(),
            await self.do_roarequest_async('GetContractMargin', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/margins', 'json', req, runtime)
        )

    def get_corp_console(self) -> dingtalkesign__2__0_models.GetCorpConsoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetCorpConsoleHeaders()
        return self.get_corp_console_with_options(headers, runtime)

    async def get_corp_console_async(self) -> dingtalkesign__2__0_models.GetCorpConsoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetCorpConsoleHeaders()
        return await self.get_corp_console_with_options_async(headers, runtime)

    def get_corp_console_with_options(
        self,
        headers: dingtalkesign__2__0_models.GetCorpConsoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetCorpConsoleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetCorpConsoleResponse(),
            self.do_roarequest('GetCorpConsole', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/consoles', 'json', req, runtime)
        )

    async def get_corp_console_with_options_async(
        self,
        headers: dingtalkesign__2__0_models.GetCorpConsoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetCorpConsoleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetCorpConsoleResponse(),
            await self.do_roarequest_async('GetCorpConsole', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/consoles', 'json', req, runtime)
        )

    def get_corp_info(self) -> dingtalkesign__2__0_models.GetCorpInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetCorpInfoHeaders()
        return self.get_corp_info_with_options(headers, runtime)

    async def get_corp_info_async(self) -> dingtalkesign__2__0_models.GetCorpInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetCorpInfoHeaders()
        return await self.get_corp_info_with_options_async(headers, runtime)

    def get_corp_info_with_options(
        self,
        headers: dingtalkesign__2__0_models.GetCorpInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetCorpInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetCorpInfoResponse(),
            self.do_roarequest('GetCorpInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/infos', 'json', req, runtime)
        )

    async def get_corp_info_with_options_async(
        self,
        headers: dingtalkesign__2__0_models.GetCorpInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetCorpInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetCorpInfoResponse(),
            await self.do_roarequest_async('GetCorpInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/infos', 'json', req, runtime)
        )

    def get_execute_url(
        self,
        request: dingtalkesign__2__0_models.GetExecuteUrlRequest,
    ) -> dingtalkesign__2__0_models.GetExecuteUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetExecuteUrlHeaders()
        return self.get_execute_url_with_options(request, headers, runtime)

    async def get_execute_url_async(
        self,
        request: dingtalkesign__2__0_models.GetExecuteUrlRequest,
    ) -> dingtalkesign__2__0_models.GetExecuteUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetExecuteUrlHeaders()
        return await self.get_execute_url_with_options_async(request, headers, runtime)

    def get_execute_url_with_options(
        self,
        request: dingtalkesign__2__0_models.GetExecuteUrlRequest,
        headers: dingtalkesign__2__0_models.GetExecuteUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetExecuteUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['account'] = request.account
        if not UtilClient.is_unset(request.sign_container):
            body['signContainer'] = request.sign_container
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetExecuteUrlResponse(),
            self.do_roarequest('GetExecuteUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/process/executeUrls', 'json', req, runtime)
        )

    async def get_execute_url_with_options_async(
        self,
        request: dingtalkesign__2__0_models.GetExecuteUrlRequest,
        headers: dingtalkesign__2__0_models.GetExecuteUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetExecuteUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['account'] = request.account
        if not UtilClient.is_unset(request.sign_container):
            body['signContainer'] = request.sign_container
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetExecuteUrlResponse(),
            await self.do_roarequest_async('GetExecuteUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/process/executeUrls', 'json', req, runtime)
        )

    def get_file_info(
        self,
        file_id: str,
    ) -> dingtalkesign__2__0_models.GetFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFileInfoHeaders()
        return self.get_file_info_with_options(file_id, headers, runtime)

    async def get_file_info_async(
        self,
        file_id: str,
    ) -> dingtalkesign__2__0_models.GetFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFileInfoHeaders()
        return await self.get_file_info_with_options_async(file_id, headers, runtime)

    def get_file_info_with_options(
        self,
        file_id: str,
        headers: dingtalkesign__2__0_models.GetFileInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFileInfoResponse:
        file_id = OpenApiUtilClient.get_encode_param(file_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFileInfoResponse(),
            self.do_roarequest('GetFileInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/files/{file_id}', 'json', req, runtime)
        )

    async def get_file_info_with_options_async(
        self,
        file_id: str,
        headers: dingtalkesign__2__0_models.GetFileInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFileInfoResponse:
        file_id = OpenApiUtilClient.get_encode_param(file_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFileInfoResponse(),
            await self.do_roarequest_async('GetFileInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/files/{file_id}', 'json', req, runtime)
        )

    def get_file_upload_url(
        self,
        request: dingtalkesign__2__0_models.GetFileUploadUrlRequest,
    ) -> dingtalkesign__2__0_models.GetFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFileUploadUrlHeaders()
        return self.get_file_upload_url_with_options(request, headers, runtime)

    async def get_file_upload_url_async(
        self,
        request: dingtalkesign__2__0_models.GetFileUploadUrlRequest,
    ) -> dingtalkesign__2__0_models.GetFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFileUploadUrlHeaders()
        return await self.get_file_upload_url_with_options_async(request, headers, runtime)

    def get_file_upload_url_with_options(
        self,
        request: dingtalkesign__2__0_models.GetFileUploadUrlRequest,
        headers: dingtalkesign__2__0_models.GetFileUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFileUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_md_5):
            body['contentMd5'] = request.content_md_5
        if not UtilClient.is_unset(request.content_type):
            body['contentType'] = request.content_type
        if not UtilClient.is_unset(request.convert_2pdf):
            body['convert2Pdf'] = request.convert_2pdf
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            body['fileSize'] = request.file_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFileUploadUrlResponse(),
            self.do_roarequest('GetFileUploadUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/files/uploadUrls', 'json', req, runtime)
        )

    async def get_file_upload_url_with_options_async(
        self,
        request: dingtalkesign__2__0_models.GetFileUploadUrlRequest,
        headers: dingtalkesign__2__0_models.GetFileUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFileUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_md_5):
            body['contentMd5'] = request.content_md_5
        if not UtilClient.is_unset(request.content_type):
            body['contentType'] = request.content_type
        if not UtilClient.is_unset(request.convert_2pdf):
            body['convert2Pdf'] = request.convert_2pdf
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            body['fileSize'] = request.file_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFileUploadUrlResponse(),
            await self.do_roarequest_async('GetFileUploadUrl', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/files/uploadUrls', 'json', req, runtime)
        )

    def get_flow_detail(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetFlowDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFlowDetailHeaders()
        return self.get_flow_detail_with_options(task_id, headers, runtime)

    async def get_flow_detail_async(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetFlowDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFlowDetailHeaders()
        return await self.get_flow_detail_with_options_async(task_id, headers, runtime)

    def get_flow_detail_with_options(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetFlowDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFlowDetailResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFlowDetailResponse(),
            self.do_roarequest('GetFlowDetail', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/flowTasks/{task_id}', 'json', req, runtime)
        )

    async def get_flow_detail_with_options_async(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetFlowDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFlowDetailResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFlowDetailResponse(),
            await self.do_roarequest_async('GetFlowDetail', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/flowTasks/{task_id}', 'json', req, runtime)
        )

    def get_flow_docs(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetFlowDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFlowDocsHeaders()
        return self.get_flow_docs_with_options(task_id, headers, runtime)

    async def get_flow_docs_async(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetFlowDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetFlowDocsHeaders()
        return await self.get_flow_docs_with_options_async(task_id, headers, runtime)

    def get_flow_docs_with_options(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetFlowDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFlowDocsResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFlowDocsResponse(),
            self.do_roarequest('GetFlowDocs', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/flowTasks/{task_id}/docs', 'json', req, runtime)
        )

    async def get_flow_docs_with_options_async(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetFlowDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetFlowDocsResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetFlowDocsResponse(),
            await self.do_roarequest_async('GetFlowDocs', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/flowTasks/{task_id}/docs', 'json', req, runtime)
        )

    def get_isv_status(self) -> dingtalkesign__2__0_models.GetIsvStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetIsvStatusHeaders()
        return self.get_isv_status_with_options(headers, runtime)

    async def get_isv_status_async(self) -> dingtalkesign__2__0_models.GetIsvStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetIsvStatusHeaders()
        return await self.get_isv_status_with_options_async(headers, runtime)

    def get_isv_status_with_options(
        self,
        headers: dingtalkesign__2__0_models.GetIsvStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetIsvStatusResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetIsvStatusResponse(),
            self.do_roarequest('GetIsvStatus', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/appStatus', 'json', req, runtime)
        )

    async def get_isv_status_with_options_async(
        self,
        headers: dingtalkesign__2__0_models.GetIsvStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetIsvStatusResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetIsvStatusResponse(),
            await self.do_roarequest_async('GetIsvStatus', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/corps/appStatus', 'json', req, runtime)
        )

    def get_sign_detail(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetSignDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetSignDetailHeaders()
        return self.get_sign_detail_with_options(task_id, headers, runtime)

    async def get_sign_detail_async(
        self,
        task_id: str,
    ) -> dingtalkesign__2__0_models.GetSignDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetSignDetailHeaders()
        return await self.get_sign_detail_with_options_async(task_id, headers, runtime)

    def get_sign_detail_with_options(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetSignDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetSignDetailResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetSignDetailResponse(),
            self.do_roarequest('GetSignDetail', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/signTasks/{task_id}', 'json', req, runtime)
        )

    async def get_sign_detail_with_options_async(
        self,
        task_id: str,
        headers: dingtalkesign__2__0_models.GetSignDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetSignDetailResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetSignDetailResponse(),
            await self.do_roarequest_async('GetSignDetail', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/signTasks/{task_id}', 'json', req, runtime)
        )

    def get_user_info(
        self,
        user_id: str,
    ) -> dingtalkesign__2__0_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetUserInfoHeaders()
        return self.get_user_info_with_options(user_id, headers, runtime)

    async def get_user_info_async(
        self,
        user_id: str,
    ) -> dingtalkesign__2__0_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.GetUserInfoHeaders()
        return await self.get_user_info_with_options_async(user_id, headers, runtime)

    def get_user_info_with_options(
        self,
        user_id: str,
        headers: dingtalkesign__2__0_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetUserInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetUserInfoResponse(),
            self.do_roarequest('GetUserInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/users/{user_id}', 'json', req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        user_id: str,
        headers: dingtalkesign__2__0_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.GetUserInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.GetUserInfoResponse(),
            await self.do_roarequest_async('GetUserInfo', 'esign_2.0', 'HTTP', 'GET', 'AK', f'/v2.0/esign/users/{user_id}', 'json', req, runtime)
        )

    def process_start(
        self,
        request: dingtalkesign__2__0_models.ProcessStartRequest,
    ) -> dingtalkesign__2__0_models.ProcessStartResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ProcessStartHeaders()
        return self.process_start_with_options(request, headers, runtime)

    async def process_start_async(
        self,
        request: dingtalkesign__2__0_models.ProcessStartRequest,
    ) -> dingtalkesign__2__0_models.ProcessStartResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ProcessStartHeaders()
        return await self.process_start_with_options_async(request, headers, runtime)

    def process_start_with_options(
        self,
        request: dingtalkesign__2__0_models.ProcessStartRequest,
        headers: dingtalkesign__2__0_models.ProcessStartHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ProcessStartResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_start):
            body['autoStart'] = request.auto_start
        if not UtilClient.is_unset(request.ccs):
            body['ccs'] = request.ccs
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.initiator_user_id):
            body['initiatorUserId'] = request.initiator_user_id
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.source_info):
            body['sourceInfo'] = request.source_info
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ProcessStartResponse(),
            self.do_roarequest('ProcessStart', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/processes/startUrls', 'json', req, runtime)
        )

    async def process_start_with_options_async(
        self,
        request: dingtalkesign__2__0_models.ProcessStartRequest,
        headers: dingtalkesign__2__0_models.ProcessStartHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ProcessStartResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_start):
            body['autoStart'] = request.auto_start
        if not UtilClient.is_unset(request.ccs):
            body['ccs'] = request.ccs
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.initiator_user_id):
            body['initiatorUserId'] = request.initiator_user_id
        if not UtilClient.is_unset(request.participants):
            body['participants'] = request.participants
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.source_info):
            body['sourceInfo'] = request.source_info
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ProcessStartResponse(),
            await self.do_roarequest_async('ProcessStart', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/processes/startUrls', 'json', req, runtime)
        )

    def resale_order(
        self,
        request: dingtalkesign__2__0_models.ResaleOrderRequest,
    ) -> dingtalkesign__2__0_models.ResaleOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ResaleOrderHeaders()
        return self.resale_order_with_options(request, headers, runtime)

    async def resale_order_async(
        self,
        request: dingtalkesign__2__0_models.ResaleOrderRequest,
    ) -> dingtalkesign__2__0_models.ResaleOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.ResaleOrderHeaders()
        return await self.resale_order_with_options_async(request, headers, runtime)

    def resale_order_with_options(
        self,
        request: dingtalkesign__2__0_models.ResaleOrderRequest,
        headers: dingtalkesign__2__0_models.ResaleOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ResaleOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_create_time):
            body['orderCreateTime'] = request.order_create_time
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.quantity):
            body['quantity'] = request.quantity
        if not UtilClient.is_unset(request.service_start_time):
            body['serviceStartTime'] = request.service_start_time
        if not UtilClient.is_unset(request.service_stop_time):
            body['serviceStopTime'] = request.service_stop_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ResaleOrderResponse(),
            self.do_roarequest('ResaleOrder', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/orders/resale', 'json', req, runtime)
        )

    async def resale_order_with_options_async(
        self,
        request: dingtalkesign__2__0_models.ResaleOrderRequest,
        headers: dingtalkesign__2__0_models.ResaleOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.ResaleOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_create_time):
            body['orderCreateTime'] = request.order_create_time
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.quantity):
            body['quantity'] = request.quantity
        if not UtilClient.is_unset(request.service_start_time):
            body['serviceStartTime'] = request.service_start_time
        if not UtilClient.is_unset(request.service_stop_time):
            body['serviceStopTime'] = request.service_stop_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.ResaleOrderResponse(),
            await self.do_roarequest_async('ResaleOrder', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/orders/resale', 'json', req, runtime)
        )

    def users_realname(
        self,
        request: dingtalkesign__2__0_models.UsersRealnameRequest,
    ) -> dingtalkesign__2__0_models.UsersRealnameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.UsersRealnameHeaders()
        return self.users_realname_with_options(request, headers, runtime)

    async def users_realname_async(
        self,
        request: dingtalkesign__2__0_models.UsersRealnameRequest,
    ) -> dingtalkesign__2__0_models.UsersRealnameResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__2__0_models.UsersRealnameHeaders()
        return await self.users_realname_with_options_async(request, headers, runtime)

    def users_realname_with_options(
        self,
        request: dingtalkesign__2__0_models.UsersRealnameRequest,
        headers: dingtalkesign__2__0_models.UsersRealnameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.UsersRealnameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.UsersRealnameResponse(),
            self.do_roarequest('UsersRealname', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/users/realnames', 'json', req, runtime)
        )

    async def users_realname_with_options_async(
        self,
        request: dingtalkesign__2__0_models.UsersRealnameRequest,
        headers: dingtalkesign__2__0_models.UsersRealnameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__2__0_models.UsersRealnameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.service_group):
            real_headers['serviceGroup'] = UtilClient.to_jsonstring(headers.service_group)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__2__0_models.UsersRealnameResponse(),
            await self.do_roarequest_async('UsersRealname', 'esign_2.0', 'HTTP', 'POST', 'AK', f'/v2.0/esign/users/realnames', 'json', req, runtime)
        )
