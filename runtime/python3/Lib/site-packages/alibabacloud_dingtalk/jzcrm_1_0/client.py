# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.jzcrm_1_0 import models as dingtalkjzcrm__1__0_models
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

    def edit_contact(
        self,
        request: dingtalkjzcrm__1__0_models.EditContactRequest,
    ) -> dingtalkjzcrm__1__0_models.EditContactResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditContactHeaders()
        return self.edit_contact_with_options(request, headers, runtime)

    async def edit_contact_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditContactRequest,
    ) -> dingtalkjzcrm__1__0_models.EditContactResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditContactHeaders()
        return await self.edit_contact_with_options_async(request, headers, runtime)

    def edit_contact_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditContactRequest,
        headers: dingtalkjzcrm__1__0_models.EditContactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditContactResponse(),
            self.do_roarequest('EditContact', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/contacts', 'json', req, runtime)
        )

    async def edit_contact_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditContactRequest,
        headers: dingtalkjzcrm__1__0_models.EditContactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditContactResponse(),
            await self.do_roarequest_async('EditContact', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/contacts', 'json', req, runtime)
        )

    def edit_customer(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerRequest,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditCustomerHeaders()
        return self.edit_customer_with_options(request, headers, runtime)

    async def edit_customer_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerRequest,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditCustomerHeaders()
        return await self.edit_customer_with_options_async(request, headers, runtime)

    def edit_customer_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerRequest,
        headers: dingtalkjzcrm__1__0_models.EditCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditCustomerResponse(),
            self.do_roarequest('EditCustomer', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/customers', 'json', req, runtime)
        )

    async def edit_customer_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerRequest,
        headers: dingtalkjzcrm__1__0_models.EditCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditCustomerResponse(),
            await self.do_roarequest_async('EditCustomer', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/customers', 'json', req, runtime)
        )

    def edit_customer_pool(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerPoolRequest,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerPoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders()
        return self.edit_customer_pool_with_options(request, headers, runtime)

    async def edit_customer_pool_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerPoolRequest,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerPoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders()
        return await self.edit_customer_pool_with_options_async(request, headers, runtime)

    def edit_customer_pool_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerPoolRequest,
        headers: dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerPoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditCustomerPoolResponse(),
            self.do_roarequest('EditCustomerPool', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/customerPools', 'json', req, runtime)
        )

    async def edit_customer_pool_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditCustomerPoolRequest,
        headers: dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditCustomerPoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditCustomerPoolResponse(),
            await self.do_roarequest_async('EditCustomerPool', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/customerPools', 'json', req, runtime)
        )

    def edit_exchange(
        self,
        request: dingtalkjzcrm__1__0_models.EditExchangeRequest,
    ) -> dingtalkjzcrm__1__0_models.EditExchangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditExchangeHeaders()
        return self.edit_exchange_with_options(request, headers, runtime)

    async def edit_exchange_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditExchangeRequest,
    ) -> dingtalkjzcrm__1__0_models.EditExchangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditExchangeHeaders()
        return await self.edit_exchange_with_options_async(request, headers, runtime)

    def edit_exchange_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditExchangeRequest,
        headers: dingtalkjzcrm__1__0_models.EditExchangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditExchangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditExchangeResponse(),
            self.do_roarequest('EditExchange', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/exchanges', 'json', req, runtime)
        )

    async def edit_exchange_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditExchangeRequest,
        headers: dingtalkjzcrm__1__0_models.EditExchangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditExchangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditExchangeResponse(),
            await self.do_roarequest_async('EditExchange', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/exchanges', 'json', req, runtime)
        )

    def edit_goods(
        self,
        request: dingtalkjzcrm__1__0_models.EditGoodsRequest,
    ) -> dingtalkjzcrm__1__0_models.EditGoodsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditGoodsHeaders()
        return self.edit_goods_with_options(request, headers, runtime)

    async def edit_goods_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditGoodsRequest,
    ) -> dingtalkjzcrm__1__0_models.EditGoodsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditGoodsHeaders()
        return await self.edit_goods_with_options_async(request, headers, runtime)

    def edit_goods_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditGoodsRequest,
        headers: dingtalkjzcrm__1__0_models.EditGoodsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditGoodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditGoodsResponse(),
            self.do_roarequest('EditGoods', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/goods', 'json', req, runtime)
        )

    async def edit_goods_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditGoodsRequest,
        headers: dingtalkjzcrm__1__0_models.EditGoodsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditGoodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditGoodsResponse(),
            await self.do_roarequest_async('EditGoods', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/goods', 'json', req, runtime)
        )

    def edit_intostock(
        self,
        request: dingtalkjzcrm__1__0_models.EditIntostockRequest,
    ) -> dingtalkjzcrm__1__0_models.EditIntostockResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditIntostockHeaders()
        return self.edit_intostock_with_options(request, headers, runtime)

    async def edit_intostock_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditIntostockRequest,
    ) -> dingtalkjzcrm__1__0_models.EditIntostockResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditIntostockHeaders()
        return await self.edit_intostock_with_options_async(request, headers, runtime)

    def edit_intostock_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditIntostockRequest,
        headers: dingtalkjzcrm__1__0_models.EditIntostockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditIntostockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditIntostockResponse(),
            self.do_roarequest('EditIntostock', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/intostocks', 'json', req, runtime)
        )

    async def edit_intostock_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditIntostockRequest,
        headers: dingtalkjzcrm__1__0_models.EditIntostockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditIntostockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditIntostockResponse(),
            await self.do_roarequest_async('EditIntostock', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/intostocks', 'json', req, runtime)
        )

    def edit_invoice(
        self,
        request: dingtalkjzcrm__1__0_models.EditInvoiceRequest,
    ) -> dingtalkjzcrm__1__0_models.EditInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditInvoiceHeaders()
        return self.edit_invoice_with_options(request, headers, runtime)

    async def edit_invoice_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditInvoiceRequest,
    ) -> dingtalkjzcrm__1__0_models.EditInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditInvoiceHeaders()
        return await self.edit_invoice_with_options_async(request, headers, runtime)

    def edit_invoice_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditInvoiceRequest,
        headers: dingtalkjzcrm__1__0_models.EditInvoiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditInvoiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditInvoiceResponse(),
            self.do_roarequest('EditInvoice', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/invoices', 'json', req, runtime)
        )

    async def edit_invoice_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditInvoiceRequest,
        headers: dingtalkjzcrm__1__0_models.EditInvoiceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditInvoiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditInvoiceResponse(),
            await self.do_roarequest_async('EditInvoice', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/invoices', 'json', req, runtime)
        )

    def edit_order(
        self,
        request: dingtalkjzcrm__1__0_models.EditOrderRequest,
    ) -> dingtalkjzcrm__1__0_models.EditOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditOrderHeaders()
        return self.edit_order_with_options(request, headers, runtime)

    async def edit_order_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditOrderRequest,
    ) -> dingtalkjzcrm__1__0_models.EditOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditOrderHeaders()
        return await self.edit_order_with_options_async(request, headers, runtime)

    def edit_order_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditOrderRequest,
        headers: dingtalkjzcrm__1__0_models.EditOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditOrderResponse(),
            self.do_roarequest('EditOrder', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/orders', 'json', req, runtime)
        )

    async def edit_order_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditOrderRequest,
        headers: dingtalkjzcrm__1__0_models.EditOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditOrderResponse(),
            await self.do_roarequest_async('EditOrder', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/orders', 'json', req, runtime)
        )

    def edit_outstock(
        self,
        request: dingtalkjzcrm__1__0_models.EditOutstockRequest,
    ) -> dingtalkjzcrm__1__0_models.EditOutstockResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditOutstockHeaders()
        return self.edit_outstock_with_options(request, headers, runtime)

    async def edit_outstock_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditOutstockRequest,
    ) -> dingtalkjzcrm__1__0_models.EditOutstockResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditOutstockHeaders()
        return await self.edit_outstock_with_options_async(request, headers, runtime)

    def edit_outstock_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditOutstockRequest,
        headers: dingtalkjzcrm__1__0_models.EditOutstockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditOutstockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditOutstockResponse(),
            self.do_roarequest('EditOutstock', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/outstocks', 'json', req, runtime)
        )

    async def edit_outstock_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditOutstockRequest,
        headers: dingtalkjzcrm__1__0_models.EditOutstockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditOutstockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditOutstockResponse(),
            await self.do_roarequest_async('EditOutstock', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/outstocks', 'json', req, runtime)
        )

    def edit_production(
        self,
        request: dingtalkjzcrm__1__0_models.EditProductionRequest,
    ) -> dingtalkjzcrm__1__0_models.EditProductionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditProductionHeaders()
        return self.edit_production_with_options(request, headers, runtime)

    async def edit_production_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditProductionRequest,
    ) -> dingtalkjzcrm__1__0_models.EditProductionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditProductionHeaders()
        return await self.edit_production_with_options_async(request, headers, runtime)

    def edit_production_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditProductionRequest,
        headers: dingtalkjzcrm__1__0_models.EditProductionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditProductionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditProductionResponse(),
            self.do_roarequest('EditProduction', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/productions', 'json', req, runtime)
        )

    async def edit_production_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditProductionRequest,
        headers: dingtalkjzcrm__1__0_models.EditProductionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditProductionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditProductionResponse(),
            await self.do_roarequest_async('EditProduction', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/productions', 'json', req, runtime)
        )

    def edit_purchase(
        self,
        request: dingtalkjzcrm__1__0_models.EditPurchaseRequest,
    ) -> dingtalkjzcrm__1__0_models.EditPurchaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditPurchaseHeaders()
        return self.edit_purchase_with_options(request, headers, runtime)

    async def edit_purchase_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditPurchaseRequest,
    ) -> dingtalkjzcrm__1__0_models.EditPurchaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditPurchaseHeaders()
        return await self.edit_purchase_with_options_async(request, headers, runtime)

    def edit_purchase_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditPurchaseRequest,
        headers: dingtalkjzcrm__1__0_models.EditPurchaseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditPurchaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditPurchaseResponse(),
            self.do_roarequest('EditPurchase', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/purchases', 'json', req, runtime)
        )

    async def edit_purchase_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditPurchaseRequest,
        headers: dingtalkjzcrm__1__0_models.EditPurchaseHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditPurchaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditPurchaseResponse(),
            await self.do_roarequest_async('EditPurchase', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/purchases', 'json', req, runtime)
        )

    def edit_quotation_record(
        self,
        request: dingtalkjzcrm__1__0_models.EditQuotationRecordRequest,
    ) -> dingtalkjzcrm__1__0_models.EditQuotationRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders()
        return self.edit_quotation_record_with_options(request, headers, runtime)

    async def edit_quotation_record_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditQuotationRecordRequest,
    ) -> dingtalkjzcrm__1__0_models.EditQuotationRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders()
        return await self.edit_quotation_record_with_options_async(request, headers, runtime)

    def edit_quotation_record_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditQuotationRecordRequest,
        headers: dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditQuotationRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditQuotationRecordResponse(),
            self.do_roarequest('EditQuotationRecord', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/quotationRecords', 'json', req, runtime)
        )

    async def edit_quotation_record_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditQuotationRecordRequest,
        headers: dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditQuotationRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditQuotationRecordResponse(),
            await self.do_roarequest_async('EditQuotationRecord', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/quotationRecords', 'json', req, runtime)
        )

    def edit_sales(
        self,
        request: dingtalkjzcrm__1__0_models.EditSalesRequest,
    ) -> dingtalkjzcrm__1__0_models.EditSalesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditSalesHeaders()
        return self.edit_sales_with_options(request, headers, runtime)

    async def edit_sales_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditSalesRequest,
    ) -> dingtalkjzcrm__1__0_models.EditSalesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.EditSalesHeaders()
        return await self.edit_sales_with_options_async(request, headers, runtime)

    def edit_sales_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.EditSalesRequest,
        headers: dingtalkjzcrm__1__0_models.EditSalesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditSalesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditSalesResponse(),
            self.do_roarequest('EditSales', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/sales', 'json', req, runtime)
        )

    async def edit_sales_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.EditSalesRequest,
        headers: dingtalkjzcrm__1__0_models.EditSalesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.EditSalesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.datatype):
            body['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            body['msgid'] = request.msgid
        if not UtilClient.is_unset(request.stamp):
            body['stamp'] = request.stamp
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
            dingtalkjzcrm__1__0_models.EditSalesResponse(),
            await self.do_roarequest_async('EditSales', 'jzcrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/jzcrm/sales', 'json', req, runtime)
        )

    def get_data_list(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataListRequest,
    ) -> dingtalkjzcrm__1__0_models.GetDataListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.GetDataListHeaders()
        return self.get_data_list_with_options(request, headers, runtime)

    async def get_data_list_async(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataListRequest,
    ) -> dingtalkjzcrm__1__0_models.GetDataListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.GetDataListHeaders()
        return await self.get_data_list_with_options_async(request, headers, runtime)

    def get_data_list_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataListRequest,
        headers: dingtalkjzcrm__1__0_models.GetDataListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.GetDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datatype):
            query['datatype'] = request.datatype
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.pagesize):
            query['pagesize'] = request.pagesize
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
            dingtalkjzcrm__1__0_models.GetDataListResponse(),
            self.do_roarequest('GetDataList', 'jzcrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/jzcrm/data', 'json', req, runtime)
        )

    async def get_data_list_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataListRequest,
        headers: dingtalkjzcrm__1__0_models.GetDataListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.GetDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datatype):
            query['datatype'] = request.datatype
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.pagesize):
            query['pagesize'] = request.pagesize
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
            dingtalkjzcrm__1__0_models.GetDataListResponse(),
            await self.do_roarequest_async('GetDataList', 'jzcrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/jzcrm/data', 'json', req, runtime)
        )

    def get_data_view(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataViewRequest,
    ) -> dingtalkjzcrm__1__0_models.GetDataViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.GetDataViewHeaders()
        return self.get_data_view_with_options(request, headers, runtime)

    async def get_data_view_async(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataViewRequest,
    ) -> dingtalkjzcrm__1__0_models.GetDataViewResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkjzcrm__1__0_models.GetDataViewHeaders()
        return await self.get_data_view_with_options_async(request, headers, runtime)

    def get_data_view_with_options(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataViewRequest,
        headers: dingtalkjzcrm__1__0_models.GetDataViewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.GetDataViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datatype):
            query['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            query['msgid'] = request.msgid
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
            dingtalkjzcrm__1__0_models.GetDataViewResponse(),
            self.do_roarequest('GetDataView', 'jzcrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/jzcrm/dataView', 'json', req, runtime)
        )

    async def get_data_view_with_options_async(
        self,
        request: dingtalkjzcrm__1__0_models.GetDataViewRequest,
        headers: dingtalkjzcrm__1__0_models.GetDataViewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkjzcrm__1__0_models.GetDataViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datatype):
            query['datatype'] = request.datatype
        if not UtilClient.is_unset(request.msgid):
            query['msgid'] = request.msgid
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
            dingtalkjzcrm__1__0_models.GetDataViewResponse(),
            await self.do_roarequest_async('GetDataView', 'jzcrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/jzcrm/dataView', 'json', req, runtime)
        )
