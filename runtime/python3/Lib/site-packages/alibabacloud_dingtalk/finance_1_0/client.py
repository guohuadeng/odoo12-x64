# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.finance_1_0 import models as dingtalkfinance__1__0_models
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

    def apply_batch_pay(
        self,
        request: dingtalkfinance__1__0_models.ApplyBatchPayRequest,
    ) -> dingtalkfinance__1__0_models.ApplyBatchPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ApplyBatchPayHeaders()
        return self.apply_batch_pay_with_options(request, headers, runtime)

    async def apply_batch_pay_async(
        self,
        request: dingtalkfinance__1__0_models.ApplyBatchPayRequest,
    ) -> dingtalkfinance__1__0_models.ApplyBatchPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ApplyBatchPayHeaders()
        return await self.apply_batch_pay_with_options_async(request, headers, runtime)

    def apply_batch_pay_with_options(
        self,
        request: dingtalkfinance__1__0_models.ApplyBatchPayRequest,
        headers: dingtalkfinance__1__0_models.ApplyBatchPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ApplyBatchPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.pass_back_params):
            body['passBackParams'] = request.pass_back_params
        if not UtilClient.is_unset(request.pay_terminal):
            body['payTerminal'] = request.pay_terminal
        if not UtilClient.is_unset(request.return_url):
            body['returnUrl'] = request.return_url
        if not UtilClient.is_unset(request.staff_id):
            body['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.trans_amount):
            body['transAmount'] = request.trans_amount
        if not UtilClient.is_unset(request.trans_expire_time):
            body['transExpireTime'] = request.trans_expire_time
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
            dingtalkfinance__1__0_models.ApplyBatchPayResponse(),
            self.do_roarequest('ApplyBatchPay', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders/pay', 'json', req, runtime)
        )

    async def apply_batch_pay_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.ApplyBatchPayRequest,
        headers: dingtalkfinance__1__0_models.ApplyBatchPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ApplyBatchPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.pass_back_params):
            body['passBackParams'] = request.pass_back_params
        if not UtilClient.is_unset(request.pay_terminal):
            body['payTerminal'] = request.pay_terminal
        if not UtilClient.is_unset(request.return_url):
            body['returnUrl'] = request.return_url
        if not UtilClient.is_unset(request.staff_id):
            body['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.trans_amount):
            body['transAmount'] = request.trans_amount
        if not UtilClient.is_unset(request.trans_expire_time):
            body['transExpireTime'] = request.trans_expire_time
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
            dingtalkfinance__1__0_models.ApplyBatchPayResponse(),
            await self.do_roarequest_async('ApplyBatchPay', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders/pay', 'json', req, runtime)
        )

    def consult_create_sub_institution(
        self,
        request: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ConsultCreateSubInstitutionHeaders()
        return self.consult_create_sub_institution_with_options(request, headers, runtime)

    async def consult_create_sub_institution_async(
        self,
        request: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ConsultCreateSubInstitutionHeaders()
        return await self.consult_create_sub_institution_with_options_async(request, headers, runtime)

    def consult_create_sub_institution_with_options(
        self,
        request: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.solution):
            body['solution'] = request.solution
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse(),
            self.do_roarequest('ConsultCreateSubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions/consult', 'json', req, runtime)
        )

    async def consult_create_sub_institution_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.ConsultCreateSubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.solution):
            body['solution'] = request.solution
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.ConsultCreateSubInstitutionResponse(),
            await self.do_roarequest_async('ConsultCreateSubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions/consult', 'json', req, runtime)
        )

    def creat_withholding_order_and_pay(
        self,
        request: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayRequest,
    ) -> dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayHeaders()
        return self.creat_withholding_order_and_pay_with_options(request, headers, runtime)

    async def creat_withholding_order_and_pay_async(
        self,
        request: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayRequest,
    ) -> dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayHeaders()
        return await self.creat_withholding_order_and_pay_with_options_async(request, headers, runtime)

    def creat_withholding_order_and_pay_with_options(
        self,
        request: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayRequest,
        headers: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.other_pay_channel_detail_info_list):
            body['otherPayChannelDetailInfoList'] = request.other_pay_channel_detail_info_list
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.payer_user_id):
            body['payerUserId'] = request.payer_user_id
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.time_out_express):
            body['timeOutExpress'] = request.time_out_express
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
            dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse(),
            self.do_roarequest('CreatWithholdingOrderAndPay', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/withholdingOrders', 'json', req, runtime)
        )

    async def creat_withholding_order_and_pay_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayRequest,
        headers: dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.other_pay_channel_detail_info_list):
            body['otherPayChannelDetailInfoList'] = request.other_pay_channel_detail_info_list
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.payer_user_id):
            body['payerUserId'] = request.payer_user_id
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.time_out_express):
            body['timeOutExpress'] = request.time_out_express
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
            dingtalkfinance__1__0_models.CreatWithholdingOrderAndPayResponse(),
            await self.do_roarequest_async('CreatWithholdingOrderAndPay', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/withholdingOrders', 'json', req, runtime)
        )

    def create_acquire_refund_order(
        self,
        request: dingtalkfinance__1__0_models.CreateAcquireRefundOrderRequest,
    ) -> dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateAcquireRefundOrderHeaders()
        return self.create_acquire_refund_order_with_options(request, headers, runtime)

    async def create_acquire_refund_order_async(
        self,
        request: dingtalkfinance__1__0_models.CreateAcquireRefundOrderRequest,
    ) -> dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateAcquireRefundOrderHeaders()
        return await self.create_acquire_refund_order_with_options_async(request, headers, runtime)

    def create_acquire_refund_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.CreateAcquireRefundOrderRequest,
        headers: dingtalkfinance__1__0_models.CreateAcquireRefundOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.origin_out_trade_no):
            body['originOutTradeNo'] = request.origin_out_trade_no
        if not UtilClient.is_unset(request.other_pay_channel_detail_info_list):
            body['otherPayChannelDetailInfoList'] = request.other_pay_channel_detail_info_list
        if not UtilClient.is_unset(request.out_refund_no):
            body['outRefundNo'] = request.out_refund_no
        if not UtilClient.is_unset(request.refund_amount):
            body['refundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse(),
            self.do_roarequest('CreateAcquireRefundOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/acquireOrders/refund', 'json', req, runtime)
        )

    async def create_acquire_refund_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.CreateAcquireRefundOrderRequest,
        headers: dingtalkfinance__1__0_models.CreateAcquireRefundOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.origin_out_trade_no):
            body['originOutTradeNo'] = request.origin_out_trade_no
        if not UtilClient.is_unset(request.other_pay_channel_detail_info_list):
            body['otherPayChannelDetailInfoList'] = request.other_pay_channel_detail_info_list
        if not UtilClient.is_unset(request.out_refund_no):
            body['outRefundNo'] = request.out_refund_no
        if not UtilClient.is_unset(request.refund_amount):
            body['refundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.CreateAcquireRefundOrderResponse(),
            await self.do_roarequest_async('CreateAcquireRefundOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/acquireOrders/refund', 'json', req, runtime)
        )

    def create_batch_trade_order(
        self,
        request: dingtalkfinance__1__0_models.CreateBatchTradeOrderRequest,
    ) -> dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateBatchTradeOrderHeaders()
        return self.create_batch_trade_order_with_options(request, headers, runtime)

    async def create_batch_trade_order_async(
        self,
        request: dingtalkfinance__1__0_models.CreateBatchTradeOrderRequest,
    ) -> dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateBatchTradeOrderHeaders()
        return await self.create_batch_trade_order_with_options_async(request, headers, runtime)

    def create_batch_trade_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.CreateBatchTradeOrderRequest,
        headers: dingtalkfinance__1__0_models.CreateBatchTradeOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.account_no):
            body['accountNo'] = request.account_no
        if not UtilClient.is_unset(request.batch_remark):
            body['batchRemark'] = request.batch_remark
        if not UtilClient.is_unset(request.batch_trade_details):
            body['batchTradeDetails'] = request.batch_trade_details
        if not UtilClient.is_unset(request.out_batch_no):
            body['outBatchNo'] = request.out_batch_no
        if not UtilClient.is_unset(request.staff_id):
            body['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.total_count):
            body['totalCount'] = request.total_count
        if not UtilClient.is_unset(request.trade_title):
            body['tradeTitle'] = request.trade_title
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
            dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse(),
            self.do_roarequest('CreateBatchTradeOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders', 'json', req, runtime)
        )

    async def create_batch_trade_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.CreateBatchTradeOrderRequest,
        headers: dingtalkfinance__1__0_models.CreateBatchTradeOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.account_no):
            body['accountNo'] = request.account_no
        if not UtilClient.is_unset(request.batch_remark):
            body['batchRemark'] = request.batch_remark
        if not UtilClient.is_unset(request.batch_trade_details):
            body['batchTradeDetails'] = request.batch_trade_details
        if not UtilClient.is_unset(request.out_batch_no):
            body['outBatchNo'] = request.out_batch_no
        if not UtilClient.is_unset(request.staff_id):
            body['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.total_amount):
            body['totalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.total_count):
            body['totalCount'] = request.total_count
        if not UtilClient.is_unset(request.trade_title):
            body['tradeTitle'] = request.trade_title
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
            dingtalkfinance__1__0_models.CreateBatchTradeOrderResponse(),
            await self.do_roarequest_async('CreateBatchTradeOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders', 'json', req, runtime)
        )

    def create_sub_institution(
        self,
        request: dingtalkfinance__1__0_models.CreateSubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.CreateSubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateSubInstitutionHeaders()
        return self.create_sub_institution_with_options(request, headers, runtime)

    async def create_sub_institution_async(
        self,
        request: dingtalkfinance__1__0_models.CreateSubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.CreateSubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateSubInstitutionHeaders()
        return await self.create_sub_institution_with_options_async(request, headers, runtime)

    def create_sub_institution_with_options(
        self,
        request: dingtalkfinance__1__0_models.CreateSubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.CreateSubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateSubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.solution):
            body['solution'] = request.solution
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.CreateSubInstitutionResponse(),
            self.do_roarequest('CreateSubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions', 'json', req, runtime)
        )

    async def create_sub_institution_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.CreateSubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.CreateSubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateSubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.solution):
            body['solution'] = request.solution
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.CreateSubInstitutionResponse(),
            await self.do_roarequest_async('CreateSubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions', 'json', req, runtime)
        )

    def create_user_code_instance(
        self,
        request: dingtalkfinance__1__0_models.CreateUserCodeInstanceRequest,
    ) -> dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateUserCodeInstanceHeaders()
        return self.create_user_code_instance_with_options(request, headers, runtime)

    async def create_user_code_instance_async(
        self,
        request: dingtalkfinance__1__0_models.CreateUserCodeInstanceRequest,
    ) -> dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.CreateUserCodeInstanceHeaders()
        return await self.create_user_code_instance_with_options_async(request, headers, runtime)

    def create_user_code_instance_with_options(
        self,
        request: dingtalkfinance__1__0_models.CreateUserCodeInstanceRequest,
        headers: dingtalkfinance__1__0_models.CreateUserCodeInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse:
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
            dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse(),
            self.do_roarequest('CreateUserCodeInstance', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/userInstances', 'json', req, runtime)
        )

    async def create_user_code_instance_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.CreateUserCodeInstanceRequest,
        headers: dingtalkfinance__1__0_models.CreateUserCodeInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse:
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
            dingtalkfinance__1__0_models.CreateUserCodeInstanceResponse(),
            await self.do_roarequest_async('CreateUserCodeInstance', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/userInstances', 'json', req, runtime)
        )

    def decode_pay_code(
        self,
        request: dingtalkfinance__1__0_models.DecodePayCodeRequest,
    ) -> dingtalkfinance__1__0_models.DecodePayCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.DecodePayCodeHeaders()
        return self.decode_pay_code_with_options(request, headers, runtime)

    async def decode_pay_code_async(
        self,
        request: dingtalkfinance__1__0_models.DecodePayCodeRequest,
    ) -> dingtalkfinance__1__0_models.DecodePayCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.DecodePayCodeHeaders()
        return await self.decode_pay_code_with_options_async(request, headers, runtime)

    def decode_pay_code_with_options(
        self,
        request: dingtalkfinance__1__0_models.DecodePayCodeRequest,
        headers: dingtalkfinance__1__0_models.DecodePayCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.DecodePayCodeResponse:
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
            dingtalkfinance__1__0_models.DecodePayCodeResponse(),
            self.do_roarequest('DecodePayCode', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/decode', 'json', req, runtime)
        )

    async def decode_pay_code_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.DecodePayCodeRequest,
        headers: dingtalkfinance__1__0_models.DecodePayCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.DecodePayCodeResponse:
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
            dingtalkfinance__1__0_models.DecodePayCodeResponse(),
            await self.do_roarequest_async('DecodePayCode', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/decode', 'json', req, runtime)
        )

    def modify_sub_institution(
        self,
        request: dingtalkfinance__1__0_models.ModifySubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.ModifySubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ModifySubInstitutionHeaders()
        return self.modify_sub_institution_with_options(request, headers, runtime)

    async def modify_sub_institution_async(
        self,
        request: dingtalkfinance__1__0_models.ModifySubInstitutionRequest,
    ) -> dingtalkfinance__1__0_models.ModifySubInstitutionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.ModifySubInstitutionHeaders()
        return await self.modify_sub_institution_with_options_async(request, headers, runtime)

    def modify_sub_institution_with_options(
        self,
        request: dingtalkfinance__1__0_models.ModifySubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.ModifySubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ModifySubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.ModifySubInstitutionResponse(),
            self.do_roarequest('ModifySubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions/modify', 'json', req, runtime)
        )

    async def modify_sub_institution_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.ModifySubInstitutionRequest,
        headers: dingtalkfinance__1__0_models.ModifySubInstitutionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.ModifySubInstitutionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_alipay_logon_id):
            body['bindingAlipayLogonId'] = request.binding_alipay_logon_id
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.legal_person_cert_info):
            body['legalPersonCertInfo'] = request.legal_person_cert_info
        if not UtilClient.is_unset(request.out_trade_no):
            body['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.qualification_infos):
            body['qualificationInfos'] = request.qualification_infos
        if not UtilClient.is_unset(request.services):
            body['services'] = request.services
        if not UtilClient.is_unset(request.settle_info):
            body['settleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.sub_inst_address_info):
            body['subInstAddressInfo'] = request.sub_inst_address_info
        if not UtilClient.is_unset(request.sub_inst_auth_info):
            body['subInstAuthInfo'] = request.sub_inst_auth_info
        if not UtilClient.is_unset(request.sub_inst_basic_info):
            body['subInstBasicInfo'] = request.sub_inst_basic_info
        if not UtilClient.is_unset(request.sub_inst_certify_info):
            body['subInstCertifyInfo'] = request.sub_inst_certify_info
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_inst_invoice_info):
            body['subInstInvoiceInfo'] = request.sub_inst_invoice_info
        if not UtilClient.is_unset(request.sub_inst_shop_info):
            body['subInstShopInfo'] = request.sub_inst_shop_info
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
            dingtalkfinance__1__0_models.ModifySubInstitutionResponse(),
            await self.do_roarequest_async('ModifySubInstitution', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/subInstitutions/modify', 'json', req, runtime)
        )

    def notify_pay_code_pay_result(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders()
        return self.notify_pay_code_pay_result_with_options(request, headers, runtime)

    async def notify_pay_code_pay_result_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders()
        return await self.notify_pay_code_pay_result_with_options_async(request, headers, runtime)

    def notify_pay_code_pay_result_with_options(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse:
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
            dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse(),
            self.do_roarequest('NotifyPayCodePayResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/payResults/notify', 'json', req, runtime)
        )

    async def notify_pay_code_pay_result_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse:
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
            dingtalkfinance__1__0_models.NotifyPayCodePayResultResponse(),
            await self.do_roarequest_async('NotifyPayCodePayResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/payResults/notify', 'json', req, runtime)
        )

    def notify_pay_code_refund_result(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders()
        return self.notify_pay_code_refund_result_with_options(request, headers, runtime)

    async def notify_pay_code_refund_result_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders()
        return await self.notify_pay_code_refund_result_with_options_async(request, headers, runtime)

    def notify_pay_code_refund_result_with_options(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse:
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
            dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse(),
            self.do_roarequest('NotifyPayCodeRefundResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/refundResults/notify', 'json', req, runtime)
        )

    async def notify_pay_code_refund_result_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse:
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
            dingtalkfinance__1__0_models.NotifyPayCodeRefundResultResponse(),
            await self.do_roarequest_async('NotifyPayCodeRefundResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/refundResults/notify', 'json', req, runtime)
        )

    def notify_verify_result(
        self,
        request: dingtalkfinance__1__0_models.NotifyVerifyResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyVerifyResultHeaders()
        return self.notify_verify_result_with_options(request, headers, runtime)

    async def notify_verify_result_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyVerifyResultRequest,
    ) -> dingtalkfinance__1__0_models.NotifyVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.NotifyVerifyResultHeaders()
        return await self.notify_verify_result_with_options_async(request, headers, runtime)

    def notify_verify_result_with_options(
        self,
        request: dingtalkfinance__1__0_models.NotifyVerifyResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyVerifyResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyVerifyResultResponse:
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
            dingtalkfinance__1__0_models.NotifyVerifyResultResponse(),
            self.do_roarequest('NotifyVerifyResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/verifyResults/notify', 'json', req, runtime)
        )

    async def notify_verify_result_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.NotifyVerifyResultRequest,
        headers: dingtalkfinance__1__0_models.NotifyVerifyResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.NotifyVerifyResultResponse:
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
            dingtalkfinance__1__0_models.NotifyVerifyResultResponse(),
            await self.do_roarequest_async('NotifyVerifyResult', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/verifyResults/notify', 'json', req, runtime)
        )

    def query_acquire_refund_order(
        self,
        request: dingtalkfinance__1__0_models.QueryAcquireRefundOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryAcquireRefundOrderHeaders()
        return self.query_acquire_refund_order_with_options(request, headers, runtime)

    async def query_acquire_refund_order_async(
        self,
        request: dingtalkfinance__1__0_models.QueryAcquireRefundOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryAcquireRefundOrderHeaders()
        return await self.query_acquire_refund_order_with_options_async(request, headers, runtime)

    def query_acquire_refund_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryAcquireRefundOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryAcquireRefundOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_refund_no):
            query['outRefundNo'] = request.out_refund_no
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
            dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse(),
            self.do_roarequest('QueryAcquireRefundOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/acquireOrders/refunds', 'json', req, runtime)
        )

    async def query_acquire_refund_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryAcquireRefundOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryAcquireRefundOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_refund_no):
            query['outRefundNo'] = request.out_refund_no
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
            dingtalkfinance__1__0_models.QueryAcquireRefundOrderResponse(),
            await self.do_roarequest_async('QueryAcquireRefundOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/acquireOrders/refunds', 'json', req, runtime)
        )

    def query_batch_trade_detail_list(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeDetailListRequest,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryBatchTradeDetailListHeaders()
        return self.query_batch_trade_detail_list_with_options(request, headers, runtime)

    async def query_batch_trade_detail_list_async(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeDetailListRequest,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryBatchTradeDetailListHeaders()
        return await self.query_batch_trade_detail_list_with_options_async(request, headers, runtime)

    def query_batch_trade_detail_list_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeDetailListRequest,
        headers: dingtalkfinance__1__0_models.QueryBatchTradeDetailListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_batch_no):
            query['outBatchNo'] = request.out_batch_no
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
            dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse(),
            self.do_roarequest('QueryBatchTradeDetailList', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/batchTrades/details', 'json', req, runtime)
        )

    async def query_batch_trade_detail_list_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeDetailListRequest,
        headers: dingtalkfinance__1__0_models.QueryBatchTradeDetailListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_batch_no):
            query['outBatchNo'] = request.out_batch_no
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
            dingtalkfinance__1__0_models.QueryBatchTradeDetailListResponse(),
            await self.do_roarequest_async('QueryBatchTradeDetailList', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/batchTrades/details', 'json', req, runtime)
        )

    def query_batch_trade_order(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryBatchTradeOrderHeaders()
        return self.query_batch_trade_order_with_options(request, headers, runtime)

    async def query_batch_trade_order_async(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryBatchTradeOrderHeaders()
        return await self.query_batch_trade_order_with_options_async(request, headers, runtime)

    def query_batch_trade_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryBatchTradeOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_batch_nos):
            body['outBatchNos'] = request.out_batch_nos
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
            dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse(),
            self.do_roarequest('QueryBatchTradeOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders/query', 'json', req, runtime)
        )

    async def query_batch_trade_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryBatchTradeOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryBatchTradeOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_batch_nos):
            body['outBatchNos'] = request.out_batch_nos
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
            dingtalkfinance__1__0_models.QueryBatchTradeOrderResponse(),
            await self.do_roarequest_async('QueryBatchTradeOrder', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/batchTrades/orders/query', 'json', req, runtime)
        )

    def query_pay_account_list(self) -> dingtalkfinance__1__0_models.QueryPayAccountListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryPayAccountListHeaders()
        return self.query_pay_account_list_with_options(headers, runtime)

    async def query_pay_account_list_async(self) -> dingtalkfinance__1__0_models.QueryPayAccountListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryPayAccountListHeaders()
        return await self.query_pay_account_list_with_options_async(headers, runtime)

    def query_pay_account_list_with_options(
        self,
        headers: dingtalkfinance__1__0_models.QueryPayAccountListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryPayAccountListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkfinance__1__0_models.QueryPayAccountListResponse(),
            self.do_roarequest('QueryPayAccountList', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/payAccounts', 'json', req, runtime)
        )

    async def query_pay_account_list_with_options_async(
        self,
        headers: dingtalkfinance__1__0_models.QueryPayAccountListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryPayAccountListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkfinance__1__0_models.QueryPayAccountListResponse(),
            await self.do_roarequest_async('QueryPayAccountList', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/payAccounts', 'json', req, runtime)
        )

    def query_register_order(
        self,
        request: dingtalkfinance__1__0_models.QueryRegisterOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryRegisterOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryRegisterOrderHeaders()
        return self.query_register_order_with_options(request, headers, runtime)

    async def query_register_order_async(
        self,
        request: dingtalkfinance__1__0_models.QueryRegisterOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryRegisterOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryRegisterOrderHeaders()
        return await self.query_register_order_with_options_async(request, headers, runtime)

    def query_register_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryRegisterOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryRegisterOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryRegisterOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inst_id):
            query['instId'] = request.inst_id
        if not UtilClient.is_unset(request.order_id):
            query['orderId'] = request.order_id
        if not UtilClient.is_unset(request.out_trade_no):
            query['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.sub_inst_id):
            query['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.QueryRegisterOrderResponse(),
            self.do_roarequest('QueryRegisterOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/institutions/subInstitutions/orders', 'json', req, runtime)
        )

    async def query_register_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryRegisterOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryRegisterOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryRegisterOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inst_id):
            query['instId'] = request.inst_id
        if not UtilClient.is_unset(request.order_id):
            query['orderId'] = request.order_id
        if not UtilClient.is_unset(request.out_trade_no):
            query['outTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.sub_inst_id):
            query['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.QueryRegisterOrderResponse(),
            await self.do_roarequest_async('QueryRegisterOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/institutions/subInstitutions/orders', 'json', req, runtime)
        )

    def query_user_agreement(
        self,
        request: dingtalkfinance__1__0_models.QueryUserAgreementRequest,
    ) -> dingtalkfinance__1__0_models.QueryUserAgreementResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryUserAgreementHeaders()
        return self.query_user_agreement_with_options(request, headers, runtime)

    async def query_user_agreement_async(
        self,
        request: dingtalkfinance__1__0_models.QueryUserAgreementRequest,
    ) -> dingtalkfinance__1__0_models.QueryUserAgreementResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryUserAgreementHeaders()
        return await self.query_user_agreement_with_options_async(request, headers, runtime)

    def query_user_agreement_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryUserAgreementRequest,
        headers: dingtalkfinance__1__0_models.QueryUserAgreementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryUserAgreementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            query['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            query['instId'] = request.inst_id
        if not UtilClient.is_unset(request.sub_inst_id):
            query['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.QueryUserAgreementResponse(),
            self.do_roarequest('QueryUserAgreement', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/userAgreements', 'json', req, runtime)
        )

    async def query_user_agreement_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryUserAgreementRequest,
        headers: dingtalkfinance__1__0_models.QueryUserAgreementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryUserAgreementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            query['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            query['instId'] = request.inst_id
        if not UtilClient.is_unset(request.sub_inst_id):
            query['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.QueryUserAgreementResponse(),
            await self.do_roarequest_async('QueryUserAgreement', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/userAgreements', 'json', req, runtime)
        )

    def query_user_alipay_account(self) -> dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryUserAlipayAccountHeaders()
        return self.query_user_alipay_account_with_options(headers, runtime)

    async def query_user_alipay_account_async(self) -> dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryUserAlipayAccountHeaders()
        return await self.query_user_alipay_account_with_options_async(headers, runtime)

    def query_user_alipay_account_with_options(
        self,
        headers: dingtalkfinance__1__0_models.QueryUserAlipayAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse(),
            self.do_roarequest('QueryUserAlipayAccount', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/userAlipayAccounts', 'json', req, runtime)
        )

    async def query_user_alipay_account_with_options_async(
        self,
        headers: dingtalkfinance__1__0_models.QueryUserAlipayAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkfinance__1__0_models.QueryUserAlipayAccountResponse(),
            await self.do_roarequest_async('QueryUserAlipayAccount', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/userAlipayAccounts', 'json', req, runtime)
        )

    def query_withholding_order(
        self,
        request: dingtalkfinance__1__0_models.QueryWithholdingOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryWithholdingOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryWithholdingOrderHeaders()
        return self.query_withholding_order_with_options(request, headers, runtime)

    async def query_withholding_order_async(
        self,
        request: dingtalkfinance__1__0_models.QueryWithholdingOrderRequest,
    ) -> dingtalkfinance__1__0_models.QueryWithholdingOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.QueryWithholdingOrderHeaders()
        return await self.query_withholding_order_with_options_async(request, headers, runtime)

    def query_withholding_order_with_options(
        self,
        request: dingtalkfinance__1__0_models.QueryWithholdingOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryWithholdingOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryWithholdingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_trade_no):
            query['outTradeNo'] = request.out_trade_no
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
            dingtalkfinance__1__0_models.QueryWithholdingOrderResponse(),
            self.do_roarequest('QueryWithholdingOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/withholdingOrders', 'json', req, runtime)
        )

    async def query_withholding_order_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.QueryWithholdingOrderRequest,
        headers: dingtalkfinance__1__0_models.QueryWithholdingOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.QueryWithholdingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_trade_no):
            query['outTradeNo'] = request.out_trade_no
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
            dingtalkfinance__1__0_models.QueryWithholdingOrderResponse(),
            await self.do_roarequest_async('QueryWithholdingOrder', 'finance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/finance/withholdingOrders', 'json', req, runtime)
        )

    def save_corp_pay_code(
        self,
        request: dingtalkfinance__1__0_models.SaveCorpPayCodeRequest,
    ) -> dingtalkfinance__1__0_models.SaveCorpPayCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders()
        return self.save_corp_pay_code_with_options(request, headers, runtime)

    async def save_corp_pay_code_async(
        self,
        request: dingtalkfinance__1__0_models.SaveCorpPayCodeRequest,
    ) -> dingtalkfinance__1__0_models.SaveCorpPayCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders()
        return await self.save_corp_pay_code_with_options_async(request, headers, runtime)

    def save_corp_pay_code_with_options(
        self,
        request: dingtalkfinance__1__0_models.SaveCorpPayCodeRequest,
        headers: dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.SaveCorpPayCodeResponse:
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
            dingtalkfinance__1__0_models.SaveCorpPayCodeResponse(),
            self.do_roarequest('SaveCorpPayCode', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/corpSettings', 'json', req, runtime)
        )

    async def save_corp_pay_code_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.SaveCorpPayCodeRequest,
        headers: dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.SaveCorpPayCodeResponse:
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
            dingtalkfinance__1__0_models.SaveCorpPayCodeResponse(),
            await self.do_roarequest_async('SaveCorpPayCode', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/payCodes/corpSettings', 'json', req, runtime)
        )

    def unsign_user_agreement(
        self,
        request: dingtalkfinance__1__0_models.UnsignUserAgreementRequest,
    ) -> dingtalkfinance__1__0_models.UnsignUserAgreementResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UnsignUserAgreementHeaders()
        return self.unsign_user_agreement_with_options(request, headers, runtime)

    async def unsign_user_agreement_async(
        self,
        request: dingtalkfinance__1__0_models.UnsignUserAgreementRequest,
    ) -> dingtalkfinance__1__0_models.UnsignUserAgreementResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UnsignUserAgreementHeaders()
        return await self.unsign_user_agreement_with_options_async(request, headers, runtime)

    def unsign_user_agreement_with_options(
        self,
        request: dingtalkfinance__1__0_models.UnsignUserAgreementRequest,
        headers: dingtalkfinance__1__0_models.UnsignUserAgreementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UnsignUserAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['agreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            body['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.UnsignUserAgreementResponse(),
            self.do_roarequest('UnsignUserAgreement', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/userAgreements/unsign', 'none', req, runtime)
        )

    async def unsign_user_agreement_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UnsignUserAgreementRequest,
        headers: dingtalkfinance__1__0_models.UnsignUserAgreementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UnsignUserAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['agreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            body['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
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
            dingtalkfinance__1__0_models.UnsignUserAgreementResponse(),
            await self.do_roarequest_async('UnsignUserAgreement', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/userAgreements/unsign', 'none', req, runtime)
        )

    def upate_user_code_instance(
        self,
        request: dingtalkfinance__1__0_models.UpateUserCodeInstanceRequest,
    ) -> dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UpateUserCodeInstanceHeaders()
        return self.upate_user_code_instance_with_options(request, headers, runtime)

    async def upate_user_code_instance_async(
        self,
        request: dingtalkfinance__1__0_models.UpateUserCodeInstanceRequest,
    ) -> dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UpateUserCodeInstanceHeaders()
        return await self.upate_user_code_instance_with_options_async(request, headers, runtime)

    def upate_user_code_instance_with_options(
        self,
        request: dingtalkfinance__1__0_models.UpateUserCodeInstanceRequest,
        headers: dingtalkfinance__1__0_models.UpateUserCodeInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse:
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
            dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse(),
            self.do_roarequest('UpateUserCodeInstance', 'finance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/finance/payCodes/userInstances', 'json', req, runtime)
        )

    async def upate_user_code_instance_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UpateUserCodeInstanceRequest,
        headers: dingtalkfinance__1__0_models.UpateUserCodeInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse:
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
            dingtalkfinance__1__0_models.UpateUserCodeInstanceResponse(),
            await self.do_roarequest_async('UpateUserCodeInstance', 'finance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/finance/payCodes/userInstances', 'json', req, runtime)
        )

    def update_invoice_verify_status(
        self,
        request: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusRequest,
    ) -> dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusHeaders()
        return self.update_invoice_verify_status_with_options(request, headers, runtime)

    async def update_invoice_verify_status_async(
        self,
        request: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusRequest,
    ) -> dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusHeaders()
        return await self.update_invoice_verify_status_with_options_async(request, headers, runtime)

    def update_invoice_verify_status_with_options(
        self,
        request: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusRequest,
        headers: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.checking_result):
            body['checkingResult'] = request.checking_result
        if not UtilClient.is_unset(request.checking_status):
            body['checkingStatus'] = request.checking_status
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.invoice_code):
            body['invoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_no):
            body['invoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.invoice_status):
            body['invoiceStatus'] = request.invoice_status
        if not UtilClient.is_unset(request.invoice_verify_id):
            body['invoiceVerifyId'] = request.invoice_verify_id
        if not UtilClient.is_unset(request.msg):
            body['msg'] = request.msg
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
            dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse(),
            self.do_roarequest('UpdateInvoiceVerifyStatus', 'finance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/finance/invoices/verifyStatus', 'json', req, runtime)
        )

    async def update_invoice_verify_status_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusRequest,
        headers: dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.checking_result):
            body['checkingResult'] = request.checking_result
        if not UtilClient.is_unset(request.checking_status):
            body['checkingStatus'] = request.checking_status
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.invoice_code):
            body['invoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_no):
            body['invoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.invoice_status):
            body['invoiceStatus'] = request.invoice_status
        if not UtilClient.is_unset(request.invoice_verify_id):
            body['invoiceVerifyId'] = request.invoice_verify_id
        if not UtilClient.is_unset(request.msg):
            body['msg'] = request.msg
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
            dingtalkfinance__1__0_models.UpdateInvoiceVerifyStatusResponse(),
            await self.do_roarequest_async('UpdateInvoiceVerifyStatus', 'finance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/finance/invoices/verifyStatus', 'json', req, runtime)
        )

    def upload_invoice_by_auth(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByAuthRequest,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadInvoiceByAuthHeaders()
        return self.upload_invoice_by_auth_with_options(request, headers, runtime)

    async def upload_invoice_by_auth_async(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByAuthRequest,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadInvoiceByAuthHeaders()
        return await self.upload_invoice_by_auth_with_options_async(request, headers, runtime)

    def upload_invoice_by_auth_with_options(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByAuthRequest,
        headers: dingtalkfinance__1__0_models.UploadInvoiceByAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoices):
            body['invoices'] = request.invoices
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
            dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse(),
            self.do_roarequest('UploadInvoiceByAuth', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/invoices/authorizations/upload', 'json', req, runtime)
        )

    async def upload_invoice_by_auth_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByAuthRequest,
        headers: dingtalkfinance__1__0_models.UploadInvoiceByAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoices):
            body['invoices'] = request.invoices
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
            dingtalkfinance__1__0_models.UploadInvoiceByAuthResponse(),
            await self.do_roarequest_async('UploadInvoiceByAuth', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/invoices/authorizations/upload', 'json', req, runtime)
        )

    def upload_invoice_by_mobile(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByMobileRequest,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadInvoiceByMobileHeaders()
        return self.upload_invoice_by_mobile_with_options(request, headers, runtime)

    async def upload_invoice_by_mobile_async(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByMobileRequest,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadInvoiceByMobileHeaders()
        return await self.upload_invoice_by_mobile_with_options_async(request, headers, runtime)

    def upload_invoice_by_mobile_with_options(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByMobileRequest,
        headers: dingtalkfinance__1__0_models.UploadInvoiceByMobileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoices):
            body['invoices'] = request.invoices
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_state_code):
            body['mobileStateCode'] = request.mobile_state_code
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
            dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse(),
            self.do_roarequest('UploadInvoiceByMobile', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/invoices/mobiles/upload', 'json', req, runtime)
        )

    async def upload_invoice_by_mobile_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UploadInvoiceByMobileRequest,
        headers: dingtalkfinance__1__0_models.UploadInvoiceByMobileHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoices):
            body['invoices'] = request.invoices
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_state_code):
            body['mobileStateCode'] = request.mobile_state_code
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
            dingtalkfinance__1__0_models.UploadInvoiceByMobileResponse(),
            await self.do_roarequest_async('UploadInvoiceByMobile', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/invoices/mobiles/upload', 'json', req, runtime)
        )

    def upload_register_image(
        self,
        request: dingtalkfinance__1__0_models.UploadRegisterImageRequest,
    ) -> dingtalkfinance__1__0_models.UploadRegisterImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadRegisterImageHeaders()
        return self.upload_register_image_with_options(request, headers, runtime)

    async def upload_register_image_async(
        self,
        request: dingtalkfinance__1__0_models.UploadRegisterImageRequest,
    ) -> dingtalkfinance__1__0_models.UploadRegisterImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UploadRegisterImageHeaders()
        return await self.upload_register_image_with_options_async(request, headers, runtime)

    def upload_register_image_with_options(
        self,
        request: dingtalkfinance__1__0_models.UploadRegisterImageRequest,
        headers: dingtalkfinance__1__0_models.UploadRegisterImageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadRegisterImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_content):
            body['imageContent'] = request.image_content
        if not UtilClient.is_unset(request.image_name):
            body['imageName'] = request.image_name
        if not UtilClient.is_unset(request.image_type):
            body['imageType'] = request.image_type
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
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
            dingtalkfinance__1__0_models.UploadRegisterImageResponse(),
            self.do_roarequest('UploadRegisterImage', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/images', 'json', req, runtime)
        )

    async def upload_register_image_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UploadRegisterImageRequest,
        headers: dingtalkfinance__1__0_models.UploadRegisterImageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UploadRegisterImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_content):
            body['imageContent'] = request.image_content
        if not UtilClient.is_unset(request.image_name):
            body['imageName'] = request.image_name
        if not UtilClient.is_unset(request.image_type):
            body['imageType'] = request.image_type
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
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
            dingtalkfinance__1__0_models.UploadRegisterImageResponse(),
            await self.do_roarequest_async('UploadRegisterImage', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/institutions/images', 'json', req, runtime)
        )

    def user_agreement_page_sign(
        self,
        request: dingtalkfinance__1__0_models.UserAgreementPageSignRequest,
    ) -> dingtalkfinance__1__0_models.UserAgreementPageSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UserAgreementPageSignHeaders()
        return self.user_agreement_page_sign_with_options(request, headers, runtime)

    async def user_agreement_page_sign_async(
        self,
        request: dingtalkfinance__1__0_models.UserAgreementPageSignRequest,
    ) -> dingtalkfinance__1__0_models.UserAgreementPageSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkfinance__1__0_models.UserAgreementPageSignHeaders()
        return await self.user_agreement_page_sign_with_options_async(request, headers, runtime)

    def user_agreement_page_sign_with_options(
        self,
        request: dingtalkfinance__1__0_models.UserAgreementPageSignRequest,
        headers: dingtalkfinance__1__0_models.UserAgreementPageSignHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UserAgreementPageSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            body['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.return_url):
            body['returnUrl'] = request.return_url
        if not UtilClient.is_unset(request.sign_scene):
            body['signScene'] = request.sign_scene
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_merchant_name):
            body['subMerchantName'] = request.sub_merchant_name
        if not UtilClient.is_unset(request.sub_merchant_service_desc):
            body['subMerchantServiceDesc'] = request.sub_merchant_service_desc
        if not UtilClient.is_unset(request.sub_merchant_service_name):
            body['subMerchantServiceName'] = request.sub_merchant_service_name
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
            dingtalkfinance__1__0_models.UserAgreementPageSignResponse(),
            self.do_roarequest('UserAgreementPageSign', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/userAgreements', 'json', req, runtime)
        )

    async def user_agreement_page_sign_with_options_async(
        self,
        request: dingtalkfinance__1__0_models.UserAgreementPageSignRequest,
        headers: dingtalkfinance__1__0_models.UserAgreementPageSignHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkfinance__1__0_models.UserAgreementPageSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['bizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_scene):
            body['bizScene'] = request.biz_scene
        if not UtilClient.is_unset(request.inst_id):
            body['instId'] = request.inst_id
        if not UtilClient.is_unset(request.pay_channel):
            body['payChannel'] = request.pay_channel
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.return_url):
            body['returnUrl'] = request.return_url
        if not UtilClient.is_unset(request.sign_scene):
            body['signScene'] = request.sign_scene
        if not UtilClient.is_unset(request.sub_inst_id):
            body['subInstId'] = request.sub_inst_id
        if not UtilClient.is_unset(request.sub_merchant_name):
            body['subMerchantName'] = request.sub_merchant_name
        if not UtilClient.is_unset(request.sub_merchant_service_desc):
            body['subMerchantServiceDesc'] = request.sub_merchant_service_desc
        if not UtilClient.is_unset(request.sub_merchant_service_name):
            body['subMerchantServiceName'] = request.sub_merchant_service_name
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
            dingtalkfinance__1__0_models.UserAgreementPageSignResponse(),
            await self.do_roarequest_async('UserAgreementPageSign', 'finance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/finance/userAgreements', 'json', req, runtime)
        )
