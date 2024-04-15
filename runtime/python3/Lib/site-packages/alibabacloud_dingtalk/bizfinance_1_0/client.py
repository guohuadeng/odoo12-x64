# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.bizfinance_1_0 import models as dingtalkbizfinance__1__0_models
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

    def create_receipt(
        self,
        request: dingtalkbizfinance__1__0_models.CreateReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.CreateReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.CreateReceiptHeaders()
        return self.create_receipt_with_options(request, headers, runtime)

    async def create_receipt_async(
        self,
        request: dingtalkbizfinance__1__0_models.CreateReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.CreateReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.CreateReceiptHeaders()
        return await self.create_receipt_with_options_async(request, headers, runtime)

    def create_receipt_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.CreateReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.CreateReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.CreateReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.CreateReceiptResponse(),
            self.do_roarequest('CreateReceipt', 'bizfinance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )

    async def create_receipt_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.CreateReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.CreateReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.CreateReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.CreateReceiptResponse(),
            await self.do_roarequest_async('CreateReceipt', 'bizfinance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )

    def delete_receipt(
        self,
        request: dingtalkbizfinance__1__0_models.DeleteReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.DeleteReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.DeleteReceiptHeaders()
        return self.delete_receipt_with_options(request, headers, runtime)

    async def delete_receipt_async(
        self,
        request: dingtalkbizfinance__1__0_models.DeleteReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.DeleteReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.DeleteReceiptHeaders()
        return await self.delete_receipt_with_options_async(request, headers, runtime)

    def delete_receipt_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.DeleteReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.DeleteReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.DeleteReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.DeleteReceiptResponse(),
            self.do_roarequest('DeleteReceipt', 'bizfinance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/bizfinance/receipts/remove', 'json', req, runtime)
        )

    async def delete_receipt_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.DeleteReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.DeleteReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.DeleteReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.DeleteReceiptResponse(),
            await self.do_roarequest_async('DeleteReceipt', 'bizfinance_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/bizfinance/receipts/remove', 'json', req, runtime)
        )

    def get_bookkeeping_user_list(self) -> dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetBookkeepingUserListHeaders()
        return self.get_bookkeeping_user_list_with_options(headers, runtime)

    async def get_bookkeeping_user_list_async(self) -> dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetBookkeepingUserListHeaders()
        return await self.get_bookkeeping_user_list_with_options_async(headers, runtime)

    def get_bookkeeping_user_list_with_options(
        self,
        headers: dingtalkbizfinance__1__0_models.GetBookkeepingUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse(),
            self.do_roarequest('GetBookkeepingUserList', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/bookkeeping/users', 'json', req, runtime)
        )

    async def get_bookkeeping_user_list_with_options_async(
        self,
        headers: dingtalkbizfinance__1__0_models.GetBookkeepingUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkbizfinance__1__0_models.GetBookkeepingUserListResponse(),
            await self.do_roarequest_async('GetBookkeepingUserList', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/bookkeeping/users', 'json', req, runtime)
        )

    def get_category(
        self,
        request: dingtalkbizfinance__1__0_models.GetCategoryRequest,
    ) -> dingtalkbizfinance__1__0_models.GetCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetCategoryHeaders()
        return self.get_category_with_options(request, headers, runtime)

    async def get_category_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetCategoryRequest,
    ) -> dingtalkbizfinance__1__0_models.GetCategoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetCategoryHeaders()
        return await self.get_category_with_options_async(request, headers, runtime)

    def get_category_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetCategoryRequest,
        headers: dingtalkbizfinance__1__0_models.GetCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetCategoryResponse(),
            self.do_roarequest('GetCategory', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/categories/get', 'json', req, runtime)
        )

    async def get_category_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetCategoryRequest,
        headers: dingtalkbizfinance__1__0_models.GetCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetCategoryResponse(),
            await self.do_roarequest_async('GetCategory', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/categories/get', 'json', req, runtime)
        )

    def get_customer(
        self,
        request: dingtalkbizfinance__1__0_models.GetCustomerRequest,
    ) -> dingtalkbizfinance__1__0_models.GetCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetCustomerHeaders()
        return self.get_customer_with_options(request, headers, runtime)

    async def get_customer_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetCustomerRequest,
    ) -> dingtalkbizfinance__1__0_models.GetCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetCustomerHeaders()
        return await self.get_customer_with_options_async(request, headers, runtime)

    def get_customer_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetCustomerRequest,
        headers: dingtalkbizfinance__1__0_models.GetCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetCustomerResponse(),
            self.do_roarequest('GetCustomer', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/customers/details', 'json', req, runtime)
        )

    async def get_customer_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetCustomerRequest,
        headers: dingtalkbizfinance__1__0_models.GetCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetCustomerResponse(),
            await self.do_roarequest_async('GetCustomer', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/customers/details', 'json', req, runtime)
        )

    def get_finance_account(
        self,
        request: dingtalkbizfinance__1__0_models.GetFinanceAccountRequest,
    ) -> dingtalkbizfinance__1__0_models.GetFinanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetFinanceAccountHeaders()
        return self.get_finance_account_with_options(request, headers, runtime)

    async def get_finance_account_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetFinanceAccountRequest,
    ) -> dingtalkbizfinance__1__0_models.GetFinanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetFinanceAccountHeaders()
        return await self.get_finance_account_with_options_async(request, headers, runtime)

    def get_finance_account_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetFinanceAccountRequest,
        headers: dingtalkbizfinance__1__0_models.GetFinanceAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetFinanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_code):
            query['accountCode'] = request.account_code
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
            dingtalkbizfinance__1__0_models.GetFinanceAccountResponse(),
            self.do_roarequest('GetFinanceAccount', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/financeAccounts/get', 'json', req, runtime)
        )

    async def get_finance_account_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetFinanceAccountRequest,
        headers: dingtalkbizfinance__1__0_models.GetFinanceAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetFinanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_code):
            query['accountCode'] = request.account_code
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
            dingtalkbizfinance__1__0_models.GetFinanceAccountResponse(),
            await self.do_roarequest_async('GetFinanceAccount', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/financeAccounts/get', 'json', req, runtime)
        )

    def get_project(
        self,
        request: dingtalkbizfinance__1__0_models.GetProjectRequest,
    ) -> dingtalkbizfinance__1__0_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetProjectHeaders()
        return self.get_project_with_options(request, headers, runtime)

    async def get_project_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetProjectRequest,
    ) -> dingtalkbizfinance__1__0_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetProjectHeaders()
        return await self.get_project_with_options_async(request, headers, runtime)

    def get_project_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetProjectRequest,
        headers: dingtalkbizfinance__1__0_models.GetProjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetProjectResponse(),
            self.do_roarequest('GetProject', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/projects/get', 'json', req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetProjectRequest,
        headers: dingtalkbizfinance__1__0_models.GetProjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetProjectResponse(),
            await self.do_roarequest_async('GetProject', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/projects/get', 'json', req, runtime)
        )

    def get_receipt(
        self,
        request: dingtalkbizfinance__1__0_models.GetReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.GetReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetReceiptHeaders()
        return self.get_receipt_with_options(request, headers, runtime)

    async def get_receipt_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.GetReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetReceiptHeaders()
        return await self.get_receipt_with_options_async(request, headers, runtime)

    def get_receipt_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.GetReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetReceiptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
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
            dingtalkbizfinance__1__0_models.GetReceiptResponse(),
            self.do_roarequest('GetReceipt', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/receipts/details', 'json', req, runtime)
        )

    async def get_receipt_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.GetReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetReceiptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
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
            dingtalkbizfinance__1__0_models.GetReceiptResponse(),
            await self.do_roarequest_async('GetReceipt', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/receipts/details', 'json', req, runtime)
        )

    def get_supplier(
        self,
        request: dingtalkbizfinance__1__0_models.GetSupplierRequest,
    ) -> dingtalkbizfinance__1__0_models.GetSupplierResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetSupplierHeaders()
        return self.get_supplier_with_options(request, headers, runtime)

    async def get_supplier_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetSupplierRequest,
    ) -> dingtalkbizfinance__1__0_models.GetSupplierResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.GetSupplierHeaders()
        return await self.get_supplier_with_options_async(request, headers, runtime)

    def get_supplier_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.GetSupplierRequest,
        headers: dingtalkbizfinance__1__0_models.GetSupplierHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetSupplierResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetSupplierResponse(),
            self.do_roarequest('GetSupplier', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/suppliers/details', 'json', req, runtime)
        )

    async def get_supplier_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.GetSupplierRequest,
        headers: dingtalkbizfinance__1__0_models.GetSupplierHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.GetSupplierResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
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
            dingtalkbizfinance__1__0_models.GetSupplierResponse(),
            await self.do_roarequest_async('GetSupplier', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/suppliers/details', 'json', req, runtime)
        )

    def query_category_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCategoryByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryCategoryByPageHeaders()
        return self.query_category_by_page_with_options(request, headers, runtime)

    async def query_category_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCategoryByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryCategoryByPageHeaders()
        return await self.query_category_by_page_with_options_async(request, headers, runtime)

    def query_category_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCategoryByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryCategoryByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse(),
            self.do_roarequest('QueryCategoryByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/categories/list', 'json', req, runtime)
        )

    async def query_category_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCategoryByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryCategoryByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
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
            dingtalkbizfinance__1__0_models.QueryCategoryByPageResponse(),
            await self.do_roarequest_async('QueryCategoryByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/categories/list', 'json', req, runtime)
        )

    def query_customer_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCustomerByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryCustomerByPageHeaders()
        return self.query_customer_by_page_with_options(request, headers, runtime)

    async def query_customer_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCustomerByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryCustomerByPageHeaders()
        return await self.query_customer_by_page_with_options_async(request, headers, runtime)

    def query_customer_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCustomerByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryCustomerByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse(),
            self.do_roarequest('QueryCustomerByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/customers', 'json', req, runtime)
        )

    async def query_customer_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryCustomerByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryCustomerByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryCustomerByPageResponse(),
            await self.do_roarequest_async('QueryCustomerByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/customers', 'json', req, runtime)
        )

    def query_enterprise_account_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageHeaders()
        return self.query_enterprise_account_by_page_with_options(request, headers, runtime)

    async def query_enterprise_account_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageHeaders()
        return await self.query_enterprise_account_by_page_with_options_async(request, headers, runtime)

    def query_enterprise_account_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse(),
            self.do_roarequest('QueryEnterpriseAccountByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/financeAccounts/list', 'json', req, runtime)
        )

    async def query_enterprise_account_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryEnterpriseAccountByPageResponse(),
            await self.do_roarequest_async('QueryEnterpriseAccountByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/financeAccounts/list', 'json', req, runtime)
        )

    def query_project_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QueryProjectByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryProjectByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryProjectByPageHeaders()
        return self.query_project_by_page_with_options(request, headers, runtime)

    async def query_project_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryProjectByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryProjectByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryProjectByPageHeaders()
        return await self.query_project_by_page_with_options_async(request, headers, runtime)

    def query_project_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QueryProjectByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryProjectByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryProjectByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryProjectByPageResponse(),
            self.do_roarequest('QueryProjectByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/projects/list', 'json', req, runtime)
        )

    async def query_project_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryProjectByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryProjectByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryProjectByPageResponse:
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
            dingtalkbizfinance__1__0_models.QueryProjectByPageResponse(),
            await self.do_roarequest_async('QueryProjectByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/projects/list', 'json', req, runtime)
        )

    def query_receipts_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QueryReceiptsByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryReceiptsByPageHeaders()
        return self.query_receipts_by_page_with_options(request, headers, runtime)

    async def query_receipts_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryReceiptsByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QueryReceiptsByPageHeaders()
        return await self.query_receipts_by_page_with_options_async(request, headers, runtime)

    def query_receipts_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QueryReceiptsByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryReceiptsByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.time_filter_field):
            query['timeFilterField'] = request.time_filter_field
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
            dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse(),
            self.do_roarequest('QueryReceiptsByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )

    async def query_receipts_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QueryReceiptsByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QueryReceiptsByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.time_filter_field):
            query['timeFilterField'] = request.time_filter_field
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
            dingtalkbizfinance__1__0_models.QueryReceiptsByPageResponse(),
            await self.do_roarequest_async('QueryReceiptsByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )

    def query_supplier_by_page(
        self,
        request: dingtalkbizfinance__1__0_models.QuerySupplierByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QuerySupplierByPageHeaders()
        return self.query_supplier_by_page_with_options(request, headers, runtime)

    async def query_supplier_by_page_async(
        self,
        request: dingtalkbizfinance__1__0_models.QuerySupplierByPageRequest,
    ) -> dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.QuerySupplierByPageHeaders()
        return await self.query_supplier_by_page_with_options_async(request, headers, runtime)

    def query_supplier_by_page_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.QuerySupplierByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QuerySupplierByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse:
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
            dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse(),
            self.do_roarequest('QuerySupplierByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/suppliers', 'json', req, runtime)
        )

    async def query_supplier_by_page_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.QuerySupplierByPageRequest,
        headers: dingtalkbizfinance__1__0_models.QuerySupplierByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse:
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
            dingtalkbizfinance__1__0_models.QuerySupplierByPageResponse(),
            await self.do_roarequest_async('QuerySupplierByPage', 'bizfinance_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/bizfinance/suppliers', 'json', req, runtime)
        )

    def update_receipt(
        self,
        request: dingtalkbizfinance__1__0_models.UpdateReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.UpdateReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.UpdateReceiptHeaders()
        return self.update_receipt_with_options(request, headers, runtime)

    async def update_receipt_async(
        self,
        request: dingtalkbizfinance__1__0_models.UpdateReceiptRequest,
    ) -> dingtalkbizfinance__1__0_models.UpdateReceiptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkbizfinance__1__0_models.UpdateReceiptHeaders()
        return await self.update_receipt_with_options_async(request, headers, runtime)

    def update_receipt_with_options(
        self,
        request: dingtalkbizfinance__1__0_models.UpdateReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.UpdateReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.UpdateReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.UpdateReceiptResponse(),
            self.do_roarequest('UpdateReceipt', 'bizfinance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )

    async def update_receipt_with_options_async(
        self,
        request: dingtalkbizfinance__1__0_models.UpdateReceiptRequest,
        headers: dingtalkbizfinance__1__0_models.UpdateReceiptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkbizfinance__1__0_models.UpdateReceiptResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.receipts):
            body['receipts'] = request.receipts
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
            dingtalkbizfinance__1__0_models.UpdateReceiptResponse(),
            await self.do_roarequest_async('UpdateReceipt', 'bizfinance_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/bizfinance/receipts', 'json', req, runtime)
        )
