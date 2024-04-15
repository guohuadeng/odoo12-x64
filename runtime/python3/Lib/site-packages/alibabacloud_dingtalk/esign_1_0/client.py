# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
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

    def auth_url(
        self,
        request: dingtalkesign__1__0_models.AuthUrlRequest,
    ) -> dingtalkesign__1__0_models.AuthUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.AuthUrlHeaders()
        return self.auth_url_with_options(request, headers, runtime)

    async def auth_url_async(
        self,
        request: dingtalkesign__1__0_models.AuthUrlRequest,
    ) -> dingtalkesign__1__0_models.AuthUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.AuthUrlHeaders()
        return await self.auth_url_with_options_async(request, headers, runtime)

    def auth_url_with_options(
        self,
        request: dingtalkesign__1__0_models.AuthUrlRequest,
        headers: dingtalkesign__1__0_models.AuthUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.AuthUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.AuthUrlResponse(),
            self.do_roarequest('AuthUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/auths/url', 'json', req, runtime)
        )

    async def auth_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.AuthUrlRequest,
        headers: dingtalkesign__1__0_models.AuthUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.AuthUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.AuthUrlResponse(),
            await self.do_roarequest_async('AuthUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/auths/url', 'json', req, runtime)
        )

    def cancel_corp_auth(self) -> dingtalkesign__1__0_models.CancelCorpAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CancelCorpAuthHeaders()
        return self.cancel_corp_auth_with_options(headers, runtime)

    async def cancel_corp_auth_async(self) -> dingtalkesign__1__0_models.CancelCorpAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CancelCorpAuthHeaders()
        return await self.cancel_corp_auth_with_options_async(headers, runtime)

    def cancel_corp_auth_with_options(
        self,
        headers: dingtalkesign__1__0_models.CancelCorpAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CancelCorpAuthResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CancelCorpAuthResponse(),
            self.do_roarequest('CancelCorpAuth', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/auth/cancel', 'json', req, runtime)
        )

    async def cancel_corp_auth_with_options_async(
        self,
        headers: dingtalkesign__1__0_models.CancelCorpAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CancelCorpAuthResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CancelCorpAuthResponse(),
            await self.do_roarequest_async('CancelCorpAuth', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/auth/cancel', 'json', req, runtime)
        )

    def channel_order(
        self,
        request: dingtalkesign__1__0_models.ChannelOrderRequest,
    ) -> dingtalkesign__1__0_models.ChannelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ChannelOrderHeaders()
        return self.channel_order_with_options(request, headers, runtime)

    async def channel_order_async(
        self,
        request: dingtalkesign__1__0_models.ChannelOrderRequest,
    ) -> dingtalkesign__1__0_models.ChannelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ChannelOrderHeaders()
        return await self.channel_order_with_options_async(request, headers, runtime)

    def channel_order_with_options(
        self,
        request: dingtalkesign__1__0_models.ChannelOrderRequest,
        headers: dingtalkesign__1__0_models.ChannelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ChannelOrderResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.ChannelOrderResponse(),
            self.do_roarequest('ChannelOrder', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/orders/channel', 'json', req, runtime)
        )

    async def channel_order_with_options_async(
        self,
        request: dingtalkesign__1__0_models.ChannelOrderRequest,
        headers: dingtalkesign__1__0_models.ChannelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ChannelOrderResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.ChannelOrderResponse(),
            await self.do_roarequest_async('ChannelOrder', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/orders/channel', 'json', req, runtime)
        )

    def contract_margin(self) -> dingtalkesign__1__0_models.ContractMarginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ContractMarginHeaders()
        return self.contract_margin_with_options(headers, runtime)

    async def contract_margin_async(self) -> dingtalkesign__1__0_models.ContractMarginResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ContractMarginHeaders()
        return await self.contract_margin_with_options_async(headers, runtime)

    def contract_margin_with_options(
        self,
        headers: dingtalkesign__1__0_models.ContractMarginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ContractMarginResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.ContractMarginResponse(),
            self.do_roarequest('ContractMargin', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/contracts/margin', 'json', req, runtime)
        )

    async def contract_margin_with_options_async(
        self,
        headers: dingtalkesign__1__0_models.ContractMarginHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ContractMarginResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.ContractMarginResponse(),
            await self.do_roarequest_async('ContractMargin', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/contracts/margin', 'json', req, runtime)
        )

    def corp_console(self) -> dingtalkesign__1__0_models.CorpConsoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CorpConsoleHeaders()
        return self.corp_console_with_options(headers, runtime)

    async def corp_console_async(self) -> dingtalkesign__1__0_models.CorpConsoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CorpConsoleHeaders()
        return await self.corp_console_with_options_async(headers, runtime)

    def corp_console_with_options(
        self,
        headers: dingtalkesign__1__0_models.CorpConsoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CorpConsoleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CorpConsoleResponse(),
            self.do_roarequest('CorpConsole', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/console', 'json', req, runtime)
        )

    async def corp_console_with_options_async(
        self,
        headers: dingtalkesign__1__0_models.CorpConsoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CorpConsoleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CorpConsoleResponse(),
            await self.do_roarequest_async('CorpConsole', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/console', 'json', req, runtime)
        )

    def corp_info(self) -> dingtalkesign__1__0_models.CorpInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CorpInfoHeaders()
        return self.corp_info_with_options(headers, runtime)

    async def corp_info_async(self) -> dingtalkesign__1__0_models.CorpInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CorpInfoHeaders()
        return await self.corp_info_with_options_async(headers, runtime)

    def corp_info_with_options(
        self,
        headers: dingtalkesign__1__0_models.CorpInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CorpInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CorpInfoResponse(),
            self.do_roarequest('CorpInfo', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/info', 'json', req, runtime)
        )

    async def corp_info_with_options_async(
        self,
        headers: dingtalkesign__1__0_models.CorpInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CorpInfoResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.CorpInfoResponse(),
            await self.do_roarequest_async('CorpInfo', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/info', 'json', req, runtime)
        )

    def create_developer(
        self,
        request: dingtalkesign__1__0_models.CreateDeveloperRequest,
    ) -> dingtalkesign__1__0_models.CreateDeveloperResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CreateDeveloperHeaders()
        return self.create_developer_with_options(request, headers, runtime)

    async def create_developer_async(
        self,
        request: dingtalkesign__1__0_models.CreateDeveloperRequest,
    ) -> dingtalkesign__1__0_models.CreateDeveloperResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.CreateDeveloperHeaders()
        return await self.create_developer_with_options_async(request, headers, runtime)

    def create_developer_with_options(
        self,
        request: dingtalkesign__1__0_models.CreateDeveloperRequest,
        headers: dingtalkesign__1__0_models.CreateDeveloperHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CreateDeveloperResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.CreateDeveloperResponse(),
            self.do_roarequest('CreateDeveloper', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/developers/create', 'json', req, runtime)
        )

    async def create_developer_with_options_async(
        self,
        request: dingtalkesign__1__0_models.CreateDeveloperRequest,
        headers: dingtalkesign__1__0_models.CreateDeveloperHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.CreateDeveloperResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.CreateDeveloperResponse(),
            await self.do_roarequest_async('CreateDeveloper', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/developers/create', 'json', req, runtime)
        )

    def get_corp_realname_url(
        self,
        request: dingtalkesign__1__0_models.GetCorpRealnameUrlRequest,
    ) -> dingtalkesign__1__0_models.GetCorpRealnameUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetCorpRealnameUrlHeaders()
        return self.get_corp_realname_url_with_options(request, headers, runtime)

    async def get_corp_realname_url_async(
        self,
        request: dingtalkesign__1__0_models.GetCorpRealnameUrlRequest,
    ) -> dingtalkesign__1__0_models.GetCorpRealnameUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetCorpRealnameUrlHeaders()
        return await self.get_corp_realname_url_with_options_async(request, headers, runtime)

    def get_corp_realname_url_with_options(
        self,
        request: dingtalkesign__1__0_models.GetCorpRealnameUrlRequest,
        headers: dingtalkesign__1__0_models.GetCorpRealnameUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetCorpRealnameUrlResponse:
        UtilClient.validate_model(request)
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
            dingtalkesign__1__0_models.GetCorpRealnameUrlResponse(),
            self.do_roarequest('GetCorpRealnameUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/corps/realname', 'json', req, runtime)
        )

    async def get_corp_realname_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetCorpRealnameUrlRequest,
        headers: dingtalkesign__1__0_models.GetCorpRealnameUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetCorpRealnameUrlResponse:
        UtilClient.validate_model(request)
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
            dingtalkesign__1__0_models.GetCorpRealnameUrlResponse(),
            await self.do_roarequest_async('GetCorpRealnameUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/corps/realname', 'json', req, runtime)
        )

    def get_crop_status(self) -> dingtalkesign__1__0_models.GetCropStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetCropStatusHeaders()
        return self.get_crop_status_with_options(headers, runtime)

    async def get_crop_status_async(self) -> dingtalkesign__1__0_models.GetCropStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetCropStatusHeaders()
        return await self.get_crop_status_with_options_async(headers, runtime)

    def get_crop_status_with_options(
        self,
        headers: dingtalkesign__1__0_models.GetCropStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetCropStatusResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetCropStatusResponse(),
            self.do_roarequest('GetCropStatus', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/statuses', 'json', req, runtime)
        )

    async def get_crop_status_with_options_async(
        self,
        headers: dingtalkesign__1__0_models.GetCropStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetCropStatusResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetCropStatusResponse(),
            await self.do_roarequest_async('GetCropStatus', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/corps/statuses', 'json', req, runtime)
        )

    def get_file(
        self,
        file_id: str,
    ) -> dingtalkesign__1__0_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFileHeaders()
        return self.get_file_with_options(file_id, headers, runtime)

    async def get_file_async(
        self,
        file_id: str,
    ) -> dingtalkesign__1__0_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFileHeaders()
        return await self.get_file_with_options_async(file_id, headers, runtime)

    def get_file_with_options(
        self,
        file_id: str,
        headers: dingtalkesign__1__0_models.GetFileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFileResponse:
        file_id = OpenApiUtilClient.get_encode_param(file_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetFileResponse(),
            self.do_roarequest('GetFile', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/files/{file_id}', 'json', req, runtime)
        )

    async def get_file_with_options_async(
        self,
        file_id: str,
        headers: dingtalkesign__1__0_models.GetFileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFileResponse:
        file_id = OpenApiUtilClient.get_encode_param(file_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetFileResponse(),
            await self.do_roarequest_async('GetFile', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/files/{file_id}', 'json', req, runtime)
        )

    def get_flow_detail(
        self,
        request: dingtalkesign__1__0_models.GetFlowDetailRequest,
    ) -> dingtalkesign__1__0_models.GetFlowDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFlowDetailHeaders()
        return self.get_flow_detail_with_options(request, headers, runtime)

    async def get_flow_detail_async(
        self,
        request: dingtalkesign__1__0_models.GetFlowDetailRequest,
    ) -> dingtalkesign__1__0_models.GetFlowDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFlowDetailHeaders()
        return await self.get_flow_detail_with_options_async(request, headers, runtime)

    def get_flow_detail_with_options(
        self,
        request: dingtalkesign__1__0_models.GetFlowDetailRequest,
        headers: dingtalkesign__1__0_models.GetFlowDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFlowDetailResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.GetFlowDetailResponse(),
            self.do_roarequest('GetFlowDetail', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/detail', 'json', req, runtime)
        )

    async def get_flow_detail_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetFlowDetailRequest,
        headers: dingtalkesign__1__0_models.GetFlowDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFlowDetailResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.GetFlowDetailResponse(),
            await self.do_roarequest_async('GetFlowDetail', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/detail', 'json', req, runtime)
        )

    def get_flow_sign_detail(
        self,
        request: dingtalkesign__1__0_models.GetFlowSignDetailRequest,
    ) -> dingtalkesign__1__0_models.GetFlowSignDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFlowSignDetailHeaders()
        return self.get_flow_sign_detail_with_options(request, headers, runtime)

    async def get_flow_sign_detail_async(
        self,
        request: dingtalkesign__1__0_models.GetFlowSignDetailRequest,
    ) -> dingtalkesign__1__0_models.GetFlowSignDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetFlowSignDetailHeaders()
        return await self.get_flow_sign_detail_with_options_async(request, headers, runtime)

    def get_flow_sign_detail_with_options(
        self,
        request: dingtalkesign__1__0_models.GetFlowSignDetailRequest,
        headers: dingtalkesign__1__0_models.GetFlowSignDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFlowSignDetailResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.GetFlowSignDetailResponse(),
            self.do_roarequest('GetFlowSignDetail', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/sign/detail', 'json', req, runtime)
        )

    async def get_flow_sign_detail_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetFlowSignDetailRequest,
        headers: dingtalkesign__1__0_models.GetFlowSignDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetFlowSignDetailResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.GetFlowSignDetailResponse(),
            await self.do_roarequest_async('GetFlowSignDetail', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/sign/detail', 'json', req, runtime)
        )

    def get_process_start_url(
        self,
        request: dingtalkesign__1__0_models.GetProcessStartUrlRequest,
    ) -> dingtalkesign__1__0_models.GetProcessStartUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetProcessStartUrlHeaders()
        return self.get_process_start_url_with_options(request, headers, runtime)

    async def get_process_start_url_async(
        self,
        request: dingtalkesign__1__0_models.GetProcessStartUrlRequest,
    ) -> dingtalkesign__1__0_models.GetProcessStartUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetProcessStartUrlHeaders()
        return await self.get_process_start_url_with_options_async(request, headers, runtime)

    def get_process_start_url_with_options(
        self,
        request: dingtalkesign__1__0_models.GetProcessStartUrlRequest,
        headers: dingtalkesign__1__0_models.GetProcessStartUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetProcessStartUrlResponse:
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
            dingtalkesign__1__0_models.GetProcessStartUrlResponse(),
            self.do_roarequest('GetProcessStartUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/process/start', 'json', req, runtime)
        )

    async def get_process_start_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetProcessStartUrlRequest,
        headers: dingtalkesign__1__0_models.GetProcessStartUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetProcessStartUrlResponse:
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
            dingtalkesign__1__0_models.GetProcessStartUrlResponse(),
            await self.do_roarequest_async('GetProcessStartUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/process/start', 'json', req, runtime)
        )

    def get_sign_notice_url(
        self,
        request: dingtalkesign__1__0_models.GetSignNoticeUrlRequest,
    ) -> dingtalkesign__1__0_models.GetSignNoticeUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetSignNoticeUrlHeaders()
        return self.get_sign_notice_url_with_options(request, headers, runtime)

    async def get_sign_notice_url_async(
        self,
        request: dingtalkesign__1__0_models.GetSignNoticeUrlRequest,
    ) -> dingtalkesign__1__0_models.GetSignNoticeUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetSignNoticeUrlHeaders()
        return await self.get_sign_notice_url_with_options_async(request, headers, runtime)

    def get_sign_notice_url_with_options(
        self,
        request: dingtalkesign__1__0_models.GetSignNoticeUrlRequest,
        headers: dingtalkesign__1__0_models.GetSignNoticeUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetSignNoticeUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
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
            dingtalkesign__1__0_models.GetSignNoticeUrlResponse(),
            self.do_roarequest('GetSignNoticeUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/signs/notice/url', 'json', req, runtime)
        )

    async def get_sign_notice_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetSignNoticeUrlRequest,
        headers: dingtalkesign__1__0_models.GetSignNoticeUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetSignNoticeUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
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
            dingtalkesign__1__0_models.GetSignNoticeUrlResponse(),
            await self.do_roarequest_async('GetSignNoticeUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/signs/notice/url', 'json', req, runtime)
        )

    def get_upload_url(
        self,
        request: dingtalkesign__1__0_models.GetUploadUrlRequest,
    ) -> dingtalkesign__1__0_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUploadUrlHeaders()
        return self.get_upload_url_with_options(request, headers, runtime)

    async def get_upload_url_async(
        self,
        request: dingtalkesign__1__0_models.GetUploadUrlRequest,
    ) -> dingtalkesign__1__0_models.GetUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUploadUrlHeaders()
        return await self.get_upload_url_with_options_async(request, headers, runtime)

    def get_upload_url_with_options(
        self,
        request: dingtalkesign__1__0_models.GetUploadUrlRequest,
        headers: dingtalkesign__1__0_models.GetUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUploadUrlResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetUploadUrlResponse(),
            self.do_roarequest('GetUploadUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/files/getUploadUrl', 'json', req, runtime)
        )

    async def get_upload_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetUploadUrlRequest,
        headers: dingtalkesign__1__0_models.GetUploadUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUploadUrlResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.GetUploadUrlResponse(),
            await self.do_roarequest_async('GetUploadUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/files/getUploadUrl', 'json', req, runtime)
        )

    def get_user_info(
        self,
        user_id: str,
    ) -> dingtalkesign__1__0_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUserInfoHeaders()
        return self.get_user_info_with_options(user_id, headers, runtime)

    async def get_user_info_async(
        self,
        user_id: str,
    ) -> dingtalkesign__1__0_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUserInfoHeaders()
        return await self.get_user_info_with_options_async(user_id, headers, runtime)

    def get_user_info_with_options(
        self,
        user_id: str,
        headers: dingtalkesign__1__0_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUserInfoResponse:
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
            dingtalkesign__1__0_models.GetUserInfoResponse(),
            self.do_roarequest('GetUserInfo', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/users/{user_id}', 'json', req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        user_id: str,
        headers: dingtalkesign__1__0_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUserInfoResponse:
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
            dingtalkesign__1__0_models.GetUserInfoResponse(),
            await self.do_roarequest_async('GetUserInfo', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/users/{user_id}', 'json', req, runtime)
        )

    def get_user_realname_url(
        self,
        request: dingtalkesign__1__0_models.GetUserRealnameUrlRequest,
    ) -> dingtalkesign__1__0_models.GetUserRealnameUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUserRealnameUrlHeaders()
        return self.get_user_realname_url_with_options(request, headers, runtime)

    async def get_user_realname_url_async(
        self,
        request: dingtalkesign__1__0_models.GetUserRealnameUrlRequest,
    ) -> dingtalkesign__1__0_models.GetUserRealnameUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.GetUserRealnameUrlHeaders()
        return await self.get_user_realname_url_with_options_async(request, headers, runtime)

    def get_user_realname_url_with_options(
        self,
        request: dingtalkesign__1__0_models.GetUserRealnameUrlRequest,
        headers: dingtalkesign__1__0_models.GetUserRealnameUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUserRealnameUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.GetUserRealnameUrlResponse(),
            self.do_roarequest('GetUserRealnameUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/users/realname', 'json', req, runtime)
        )

    async def get_user_realname_url_with_options_async(
        self,
        request: dingtalkesign__1__0_models.GetUserRealnameUrlRequest,
        headers: dingtalkesign__1__0_models.GetUserRealnameUrlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.GetUserRealnameUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.redirect_url):
            body['redirectUrl'] = request.redirect_url
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
            dingtalkesign__1__0_models.GetUserRealnameUrlResponse(),
            await self.do_roarequest_async('GetUserRealnameUrl', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/users/realname', 'json', req, runtime)
        )

    def list_flow_docs(
        self,
        request: dingtalkesign__1__0_models.ListFlowDocsRequest,
    ) -> dingtalkesign__1__0_models.ListFlowDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ListFlowDocsHeaders()
        return self.list_flow_docs_with_options(request, headers, runtime)

    async def list_flow_docs_async(
        self,
        request: dingtalkesign__1__0_models.ListFlowDocsRequest,
    ) -> dingtalkesign__1__0_models.ListFlowDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ListFlowDocsHeaders()
        return await self.list_flow_docs_with_options_async(request, headers, runtime)

    def list_flow_docs_with_options(
        self,
        request: dingtalkesign__1__0_models.ListFlowDocsRequest,
        headers: dingtalkesign__1__0_models.ListFlowDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ListFlowDocsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.ListFlowDocsResponse(),
            self.do_roarequest('ListFlowDocs', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/docs', 'json', req, runtime)
        )

    async def list_flow_docs_with_options_async(
        self,
        request: dingtalkesign__1__0_models.ListFlowDocsRequest,
        headers: dingtalkesign__1__0_models.ListFlowDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ListFlowDocsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.ListFlowDocsResponse(),
            await self.do_roarequest_async('ListFlowDocs', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/flows/docs', 'json', req, runtime)
        )

    def list_seal_approval(
        self,
        request: dingtalkesign__1__0_models.ListSealApprovalRequest,
    ) -> dingtalkesign__1__0_models.ListSealApprovalResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ListSealApprovalHeaders()
        return self.list_seal_approval_with_options(request, headers, runtime)

    async def list_seal_approval_async(
        self,
        request: dingtalkesign__1__0_models.ListSealApprovalRequest,
    ) -> dingtalkesign__1__0_models.ListSealApprovalResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.ListSealApprovalHeaders()
        return await self.list_seal_approval_with_options_async(request, headers, runtime)

    def list_seal_approval_with_options(
        self,
        request: dingtalkesign__1__0_models.ListSealApprovalRequest,
        headers: dingtalkesign__1__0_models.ListSealApprovalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ListSealApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.ListSealApprovalResponse(),
            self.do_roarequest('ListSealApproval', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/seals/approval/list', 'json', req, runtime)
        )

    async def list_seal_approval_with_options_async(
        self,
        request: dingtalkesign__1__0_models.ListSealApprovalRequest,
        headers: dingtalkesign__1__0_models.ListSealApprovalHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.ListSealApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkesign__1__0_models.ListSealApprovalResponse(),
            await self.do_roarequest_async('ListSealApproval', 'esign_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/esign/seals/approval/list', 'json', req, runtime)
        )

    def order_resale(
        self,
        request: dingtalkesign__1__0_models.OrderResaleRequest,
    ) -> dingtalkesign__1__0_models.OrderResaleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.OrderResaleHeaders()
        return self.order_resale_with_options(request, headers, runtime)

    async def order_resale_async(
        self,
        request: dingtalkesign__1__0_models.OrderResaleRequest,
    ) -> dingtalkesign__1__0_models.OrderResaleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkesign__1__0_models.OrderResaleHeaders()
        return await self.order_resale_with_options_async(request, headers, runtime)

    def order_resale_with_options(
        self,
        request: dingtalkesign__1__0_models.OrderResaleRequest,
        headers: dingtalkesign__1__0_models.OrderResaleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.OrderResaleResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.OrderResaleResponse(),
            self.do_roarequest('OrderResale', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/orders/resale', 'json', req, runtime)
        )

    async def order_resale_with_options_async(
        self,
        request: dingtalkesign__1__0_models.OrderResaleRequest,
        headers: dingtalkesign__1__0_models.OrderResaleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkesign__1__0_models.OrderResaleResponse:
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
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkesign__1__0_models.OrderResaleResponse(),
            await self.do_roarequest_async('OrderResale', 'esign_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/esign/orders/resale', 'json', req, runtime)
        )
