# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.badge_1_0 import models as dingtalkbadge__1__0_models
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

    def create_badge_code_user_instance(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest,
    ) -> dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders()
        return self.create_badge_code_user_instance_with_options(request, headers, runtime)

    async def create_badge_code_user_instance_async(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest,
    ) -> dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders()
        return await self.create_badge_code_user_instance_with_options_async(request, headers, runtime)

    def create_badge_code_user_instance_with_options(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest,
        headers: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.available_times):
            body['availableTimes'] = request.available_times
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.code_value):
            body['codeValue'] = request.code_value
        if not UtilClient.is_unset(request.code_value_type):
            body['codeValueType'] = request.code_value_type
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_expired):
            body['gmtExpired'] = request.gmt_expired
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
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
            dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse(),
            self.do_roarequest('CreateBadgeCodeUserInstance', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/userInstances', 'json', req, runtime)
        )

    async def create_badge_code_user_instance_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest,
        headers: dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.available_times):
            body['availableTimes'] = request.available_times
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.code_value):
            body['codeValue'] = request.code_value
        if not UtilClient.is_unset(request.code_value_type):
            body['codeValueType'] = request.code_value_type
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_expired):
            body['gmtExpired'] = request.gmt_expired
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
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
            dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceResponse(),
            await self.do_roarequest_async('CreateBadgeCodeUserInstance', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/userInstances', 'json', req, runtime)
        )

    def create_badge_notify(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeNotifyRequest,
    ) -> dingtalkbadge__1__0_models.CreateBadgeNotifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders()
        return self.create_badge_notify_with_options(request, headers, runtime)

    async def create_badge_notify_async(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeNotifyRequest,
    ) -> dingtalkbadge__1__0_models.CreateBadgeNotifyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders()
        return await self.create_badge_notify_with_options_async(request, headers, runtime)

    def create_badge_notify_with_options(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeNotifyRequest,
        headers: dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.CreateBadgeNotifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.msg_id):
            body['msgId'] = request.msg_id
        if not UtilClient.is_unset(request.msg_type):
            body['msgType'] = request.msg_type
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
            dingtalkbadge__1__0_models.CreateBadgeNotifyResponse(),
            self.do_roarequest('CreateBadgeNotify', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/notices', 'json', req, runtime)
        )

    async def create_badge_notify_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.CreateBadgeNotifyRequest,
        headers: dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.CreateBadgeNotifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.msg_id):
            body['msgId'] = request.msg_id
        if not UtilClient.is_unset(request.msg_type):
            body['msgType'] = request.msg_type
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
            dingtalkbadge__1__0_models.CreateBadgeNotifyResponse(),
            await self.do_roarequest_async('CreateBadgeNotify', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/notices', 'json', req, runtime)
        )

    def decode_badge_code(
        self,
        request: dingtalkbadge__1__0_models.DecodeBadgeCodeRequest,
    ) -> dingtalkbadge__1__0_models.DecodeBadgeCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders()
        return self.decode_badge_code_with_options(request, headers, runtime)

    async def decode_badge_code_async(
        self,
        request: dingtalkbadge__1__0_models.DecodeBadgeCodeRequest,
    ) -> dingtalkbadge__1__0_models.DecodeBadgeCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders()
        return await self.decode_badge_code_with_options_async(request, headers, runtime)

    def decode_badge_code_with_options(
        self,
        request: dingtalkbadge__1__0_models.DecodeBadgeCodeRequest,
        headers: dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.DecodeBadgeCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
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
            dingtalkbadge__1__0_models.DecodeBadgeCodeResponse(),
            self.do_roarequest('DecodeBadgeCode', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/decode', 'json', req, runtime)
        )

    async def decode_badge_code_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.DecodeBadgeCodeRequest,
        headers: dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.DecodeBadgeCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
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
            dingtalkbadge__1__0_models.DecodeBadgeCodeResponse(),
            await self.do_roarequest_async('DecodeBadgeCode', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/decode', 'json', req, runtime)
        )

    def notify_badge_code_pay_result(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodePayResultHeaders()
        return self.notify_badge_code_pay_result_with_options(request, headers, runtime)

    async def notify_badge_code_pay_result_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodePayResultHeaders()
        return await self.notify_badge_code_pay_result_with_options_async(request, headers, runtime)

    def notify_badge_code_pay_result_with_options(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.charge_amount):
            body['chargeAmount'] = request.charge_amount
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_trade_create):
            body['gmtTradeCreate'] = request.gmt_trade_create
        if not UtilClient.is_unset(request.gmt_trade_finish):
            body['gmtTradeFinish'] = request.gmt_trade_finish
        if not UtilClient.is_unset(request.merchant_name):
            body['merchantName'] = request.merchant_name
        if not UtilClient.is_unset(request.pay_channel_detail_list):
            body['payChannelDetailList'] = request.pay_channel_detail_list
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.promotion_amount):
            body['promotionAmount'] = request.promotion_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.trade_error_code):
            body['tradeErrorCode'] = request.trade_error_code
        if not UtilClient.is_unset(request.trade_error_msg):
            body['tradeErrorMsg'] = request.trade_error_msg
        if not UtilClient.is_unset(request.trade_no):
            body['tradeNo'] = request.trade_no
        if not UtilClient.is_unset(request.trade_status):
            body['tradeStatus'] = request.trade_status
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
            dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse(),
            self.do_roarequest('NotifyBadgeCodePayResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/payResults', 'json', req, runtime)
        )

    async def notify_badge_code_pay_result_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodePayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.charge_amount):
            body['chargeAmount'] = request.charge_amount
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_trade_create):
            body['gmtTradeCreate'] = request.gmt_trade_create
        if not UtilClient.is_unset(request.gmt_trade_finish):
            body['gmtTradeFinish'] = request.gmt_trade_finish
        if not UtilClient.is_unset(request.merchant_name):
            body['merchantName'] = request.merchant_name
        if not UtilClient.is_unset(request.pay_channel_detail_list):
            body['payChannelDetailList'] = request.pay_channel_detail_list
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.promotion_amount):
            body['promotionAmount'] = request.promotion_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.trade_error_code):
            body['tradeErrorCode'] = request.trade_error_code
        if not UtilClient.is_unset(request.trade_error_msg):
            body['tradeErrorMsg'] = request.trade_error_msg
        if not UtilClient.is_unset(request.trade_no):
            body['tradeNo'] = request.trade_no
        if not UtilClient.is_unset(request.trade_status):
            body['tradeStatus'] = request.trade_status
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
            dingtalkbadge__1__0_models.NotifyBadgeCodePayResultResponse(),
            await self.do_roarequest_async('NotifyBadgeCodePayResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/payResults', 'json', req, runtime)
        )

    def notify_badge_code_refund_result(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders()
        return self.notify_badge_code_refund_result_with_options(request, headers, runtime)

    async def notify_badge_code_refund_result_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders()
        return await self.notify_badge_code_refund_result_with_options_async(request, headers, runtime)

    def notify_badge_code_refund_result_with_options(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.gmt_refund):
            body['gmtRefund'] = request.gmt_refund
        if not UtilClient.is_unset(request.pay_channel_detail_list):
            body['payChannelDetailList'] = request.pay_channel_detail_list
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.refund_amount):
            body['refundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.refund_order_no):
            body['refundOrderNo'] = request.refund_order_no
        if not UtilClient.is_unset(request.refund_promotion_amount):
            body['refundPromotionAmount'] = request.refund_promotion_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
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
            dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse(),
            self.do_roarequest('NotifyBadgeCodeRefundResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/refundResults', 'json', req, runtime)
        )

    async def notify_badge_code_refund_result_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.gmt_refund):
            body['gmtRefund'] = request.gmt_refund
        if not UtilClient.is_unset(request.pay_channel_detail_list):
            body['payChannelDetailList'] = request.pay_channel_detail_list
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.refund_amount):
            body['refundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.refund_order_no):
            body['refundOrderNo'] = request.refund_order_no
        if not UtilClient.is_unset(request.refund_promotion_amount):
            body['refundPromotionAmount'] = request.refund_promotion_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
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
            dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultResponse(),
            await self.do_roarequest_async('NotifyBadgeCodeRefundResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/refundResults', 'json', req, runtime)
        )

    def notify_badge_code_verify_result(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders()
        return self.notify_badge_code_verify_result_with_options(request, headers, runtime)

    async def notify_badge_code_verify_result_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders()
        return await self.notify_badge_code_verify_result_with_options_async(request, headers, runtime)

    def notify_badge_code_verify_result_with_options(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
        if not UtilClient.is_unset(request.verify_event):
            body['verifyEvent'] = request.verify_event
        if not UtilClient.is_unset(request.verify_location):
            body['verifyLocation'] = request.verify_location
        if not UtilClient.is_unset(request.verify_no):
            body['verifyNo'] = request.verify_no
        if not UtilClient.is_unset(request.verify_result):
            body['verifyResult'] = request.verify_result
        if not UtilClient.is_unset(request.verify_time):
            body['verifyTime'] = request.verify_time
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
            dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse(),
            self.do_roarequest('NotifyBadgeCodeVerifyResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/verifyResults', 'json', req, runtime)
        )

    async def notify_badge_code_verify_result_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest,
        headers: dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.pay_code):
            body['payCode'] = request.pay_code
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
        if not UtilClient.is_unset(request.verify_event):
            body['verifyEvent'] = request.verify_event
        if not UtilClient.is_unset(request.verify_location):
            body['verifyLocation'] = request.verify_location
        if not UtilClient.is_unset(request.verify_no):
            body['verifyNo'] = request.verify_no
        if not UtilClient.is_unset(request.verify_result):
            body['verifyResult'] = request.verify_result
        if not UtilClient.is_unset(request.verify_time):
            body['verifyTime'] = request.verify_time
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
            dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultResponse(),
            await self.do_roarequest_async('NotifyBadgeCodeVerifyResult', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/verifyResults', 'json', req, runtime)
        )

    def save_badge_code_corp_instance(
        self,
        request: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceRequest,
    ) -> dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceHeaders()
        return self.save_badge_code_corp_instance_with_options(request, headers, runtime)

    async def save_badge_code_corp_instance_async(
        self,
        request: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceRequest,
    ) -> dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceHeaders()
        return await self.save_badge_code_corp_instance_with_options_async(request, headers, runtime)

    def save_badge_code_corp_instance_with_options(
        self,
        request: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceRequest,
        headers: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
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
            dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse(),
            self.do_roarequest('SaveBadgeCodeCorpInstance', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/corpInstances', 'json', req, runtime)
        )

    async def save_badge_code_corp_instance_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceRequest,
        headers: dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
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
            dingtalkbadge__1__0_models.SaveBadgeCodeCorpInstanceResponse(),
            await self.do_roarequest_async('SaveBadgeCodeCorpInstance', 'badge_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/badge/codes/corpInstances', 'json', req, runtime)
        )

    def update_badge_code_user_instance(
        self,
        request: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceRequest,
    ) -> dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceHeaders()
        return self.update_badge_code_user_instance_with_options(request, headers, runtime)

    async def update_badge_code_user_instance_async(
        self,
        request: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceRequest,
    ) -> dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceHeaders()
        return await self.update_badge_code_user_instance_with_options_async(request, headers, runtime)

    def update_badge_code_user_instance_with_options(
        self,
        request: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceRequest,
        headers: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.available_times):
            body['availableTimes'] = request.available_times
        if not UtilClient.is_unset(request.code_id):
            body['codeId'] = request.code_id
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.code_value):
            body['codeValue'] = request.code_value
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_expired):
            body['gmtExpired'] = request.gmt_expired
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
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
            dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse(),
            self.do_roarequest('UpdateBadgeCodeUserInstance', 'badge_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/badge/codes/userInstances', 'json', req, runtime)
        )

    async def update_badge_code_user_instance_with_options_async(
        self,
        request: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceRequest,
        headers: dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.available_times):
            body['availableTimes'] = request.available_times
        if not UtilClient.is_unset(request.code_id):
            body['codeId'] = request.code_id
        if not UtilClient.is_unset(request.code_identity):
            body['codeIdentity'] = request.code_identity
        if not UtilClient.is_unset(request.code_value):
            body['codeValue'] = request.code_value
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.ext_info):
            body['extInfo'] = request.ext_info
        if not UtilClient.is_unset(request.gmt_expired):
            body['gmtExpired'] = request.gmt_expired
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_corp_relation_type):
            body['userCorpRelationType'] = request.user_corp_relation_type
        if not UtilClient.is_unset(request.user_identity):
            body['userIdentity'] = request.user_identity
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
            dingtalkbadge__1__0_models.UpdateBadgeCodeUserInstanceResponse(),
            await self.do_roarequest_async('UpdateBadgeCodeUserInstance', 'badge_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/badge/codes/userInstances', 'json', req, runtime)
        )
