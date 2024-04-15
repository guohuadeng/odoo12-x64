# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.search_1_0 import models as dingtalksearch__1__0_models
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

    def batch_insert_search_item(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.BatchInsertSearchItemRequest,
    ) -> dingtalksearch__1__0_models.BatchInsertSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.BatchInsertSearchItemHeaders()
        return self.batch_insert_search_item_with_options(tab_id, request, headers, runtime)

    async def batch_insert_search_item_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.BatchInsertSearchItemRequest,
    ) -> dingtalksearch__1__0_models.BatchInsertSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.BatchInsertSearchItemHeaders()
        return await self.batch_insert_search_item_with_options_async(tab_id, request, headers, runtime)

    def batch_insert_search_item_with_options(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.BatchInsertSearchItemRequest,
        headers: dingtalksearch__1__0_models.BatchInsertSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.BatchInsertSearchItemResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.search_item_models):
            body['searchItemModels'] = request.search_item_models
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
            dingtalksearch__1__0_models.BatchInsertSearchItemResponse(),
            self.do_roarequest('BatchInsertSearchItem', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs/{tab_id}/items/batch', 'none', req, runtime)
        )

    async def batch_insert_search_item_with_options_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.BatchInsertSearchItemRequest,
        headers: dingtalksearch__1__0_models.BatchInsertSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.BatchInsertSearchItemResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.search_item_models):
            body['searchItemModels'] = request.search_item_models
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
            dingtalksearch__1__0_models.BatchInsertSearchItemResponse(),
            await self.do_roarequest_async('BatchInsertSearchItem', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs/{tab_id}/items/batch', 'none', req, runtime)
        )

    def create_search_tab(
        self,
        request: dingtalksearch__1__0_models.CreateSearchTabRequest,
    ) -> dingtalksearch__1__0_models.CreateSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.CreateSearchTabHeaders()
        return self.create_search_tab_with_options(request, headers, runtime)

    async def create_search_tab_async(
        self,
        request: dingtalksearch__1__0_models.CreateSearchTabRequest,
    ) -> dingtalksearch__1__0_models.CreateSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.CreateSearchTabHeaders()
        return await self.create_search_tab_with_options_async(request, headers, runtime)

    def create_search_tab_with_options(
        self,
        request: dingtalksearch__1__0_models.CreateSearchTabRequest,
        headers: dingtalksearch__1__0_models.CreateSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.CreateSearchTabResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
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
            dingtalksearch__1__0_models.CreateSearchTabResponse(),
            self.do_roarequest('CreateSearchTab', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs', 'json', req, runtime)
        )

    async def create_search_tab_with_options_async(
        self,
        request: dingtalksearch__1__0_models.CreateSearchTabRequest,
        headers: dingtalksearch__1__0_models.CreateSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.CreateSearchTabResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
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
            dingtalksearch__1__0_models.CreateSearchTabResponse(),
            await self.do_roarequest_async('CreateSearchTab', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs', 'json', req, runtime)
        )

    def delete_search_item(
        self,
        tab_id: str,
        item_id: str,
    ) -> dingtalksearch__1__0_models.DeleteSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.DeleteSearchItemHeaders()
        return self.delete_search_item_with_options(tab_id, item_id, headers, runtime)

    async def delete_search_item_async(
        self,
        tab_id: str,
        item_id: str,
    ) -> dingtalksearch__1__0_models.DeleteSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.DeleteSearchItemHeaders()
        return await self.delete_search_item_with_options_async(tab_id, item_id, headers, runtime)

    def delete_search_item_with_options(
        self,
        tab_id: str,
        item_id: str,
        headers: dingtalksearch__1__0_models.DeleteSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.DeleteSearchItemResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.DeleteSearchItemResponse(),
            self.do_roarequest('DeleteSearchItem', 'search_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/search/tabs/{tab_id}/items/{item_id}', 'none', req, runtime)
        )

    async def delete_search_item_with_options_async(
        self,
        tab_id: str,
        item_id: str,
        headers: dingtalksearch__1__0_models.DeleteSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.DeleteSearchItemResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.DeleteSearchItemResponse(),
            await self.do_roarequest_async('DeleteSearchItem', 'search_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/search/tabs/{tab_id}/items/{item_id}', 'none', req, runtime)
        )

    def delete_search_tab(
        self,
        tab_id: str,
    ) -> dingtalksearch__1__0_models.DeleteSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.DeleteSearchTabHeaders()
        return self.delete_search_tab_with_options(tab_id, headers, runtime)

    async def delete_search_tab_async(
        self,
        tab_id: str,
    ) -> dingtalksearch__1__0_models.DeleteSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.DeleteSearchTabHeaders()
        return await self.delete_search_tab_with_options_async(tab_id, headers, runtime)

    def delete_search_tab_with_options(
        self,
        tab_id: str,
        headers: dingtalksearch__1__0_models.DeleteSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.DeleteSearchTabResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.DeleteSearchTabResponse(),
            self.do_roarequest('DeleteSearchTab', 'search_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/search/tabs/{tab_id}', 'none', req, runtime)
        )

    async def delete_search_tab_with_options_async(
        self,
        tab_id: str,
        headers: dingtalksearch__1__0_models.DeleteSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.DeleteSearchTabResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.DeleteSearchTabResponse(),
            await self.do_roarequest_async('DeleteSearchTab', 'search_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/search/tabs/{tab_id}', 'none', req, runtime)
        )

    def get_search_item(
        self,
        tab_id: str,
        item_id: str,
    ) -> dingtalksearch__1__0_models.GetSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchItemHeaders()
        return self.get_search_item_with_options(tab_id, item_id, headers, runtime)

    async def get_search_item_async(
        self,
        tab_id: str,
        item_id: str,
    ) -> dingtalksearch__1__0_models.GetSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchItemHeaders()
        return await self.get_search_item_with_options_async(tab_id, item_id, headers, runtime)

    def get_search_item_with_options(
        self,
        tab_id: str,
        item_id: str,
        headers: dingtalksearch__1__0_models.GetSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchItemResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.GetSearchItemResponse(),
            self.do_roarequest('GetSearchItem', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}/items/{item_id}', 'json', req, runtime)
        )

    async def get_search_item_with_options_async(
        self,
        tab_id: str,
        item_id: str,
        headers: dingtalksearch__1__0_models.GetSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchItemResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.GetSearchItemResponse(),
            await self.do_roarequest_async('GetSearchItem', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}/items/{item_id}', 'json', req, runtime)
        )

    def get_search_items_by_key_word(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.GetSearchItemsByKeyWordRequest,
    ) -> dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchItemsByKeyWordHeaders()
        return self.get_search_items_by_key_word_with_options(tab_id, request, headers, runtime)

    async def get_search_items_by_key_word_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.GetSearchItemsByKeyWordRequest,
    ) -> dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchItemsByKeyWordHeaders()
        return await self.get_search_items_by_key_word_with_options_async(tab_id, request, headers, runtime)

    def get_search_items_by_key_word_with_options(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.GetSearchItemsByKeyWordRequest,
        headers: dingtalksearch__1__0_models.GetSearchItemsByKeyWordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['keyWord'] = request.key_word
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
            dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse(),
            self.do_roarequest('GetSearchItemsByKeyWord', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}/items', 'json', req, runtime)
        )

    async def get_search_items_by_key_word_with_options_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.GetSearchItemsByKeyWordRequest,
        headers: dingtalksearch__1__0_models.GetSearchItemsByKeyWordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['keyWord'] = request.key_word
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
            dingtalksearch__1__0_models.GetSearchItemsByKeyWordResponse(),
            await self.do_roarequest_async('GetSearchItemsByKeyWord', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}/items', 'json', req, runtime)
        )

    def get_search_tab(
        self,
        tab_id: str,
    ) -> dingtalksearch__1__0_models.GetSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchTabHeaders()
        return self.get_search_tab_with_options(tab_id, headers, runtime)

    async def get_search_tab_async(
        self,
        tab_id: str,
    ) -> dingtalksearch__1__0_models.GetSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.GetSearchTabHeaders()
        return await self.get_search_tab_with_options_async(tab_id, headers, runtime)

    def get_search_tab_with_options(
        self,
        tab_id: str,
        headers: dingtalksearch__1__0_models.GetSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchTabResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.GetSearchTabResponse(),
            self.do_roarequest('GetSearchTab', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}', 'json', req, runtime)
        )

    async def get_search_tab_with_options_async(
        self,
        tab_id: str,
        headers: dingtalksearch__1__0_models.GetSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.GetSearchTabResponse:
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.GetSearchTabResponse(),
            await self.do_roarequest_async('GetSearchTab', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs/{tab_id}', 'json', req, runtime)
        )

    def insert_search_item(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.InsertSearchItemRequest,
    ) -> dingtalksearch__1__0_models.InsertSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.InsertSearchItemHeaders()
        return self.insert_search_item_with_options(tab_id, request, headers, runtime)

    async def insert_search_item_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.InsertSearchItemRequest,
    ) -> dingtalksearch__1__0_models.InsertSearchItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.InsertSearchItemHeaders()
        return await self.insert_search_item_with_options_async(tab_id, request, headers, runtime)

    def insert_search_item_with_options(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.InsertSearchItemRequest,
        headers: dingtalksearch__1__0_models.InsertSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.InsertSearchItemResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.footer):
            body['footer'] = request.footer
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.item_id):
            body['itemId'] = request.item_id
        if not UtilClient.is_unset(request.mobile_url):
            body['mobileUrl'] = request.mobile_url
        if not UtilClient.is_unset(request.pc_url):
            body['pcUrl'] = request.pc_url
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
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
            dingtalksearch__1__0_models.InsertSearchItemResponse(),
            self.do_roarequest('InsertSearchItem', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs/{tab_id}/items', 'none', req, runtime)
        )

    async def insert_search_item_with_options_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.InsertSearchItemRequest,
        headers: dingtalksearch__1__0_models.InsertSearchItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.InsertSearchItemResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.footer):
            body['footer'] = request.footer
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.item_id):
            body['itemId'] = request.item_id
        if not UtilClient.is_unset(request.mobile_url):
            body['mobileUrl'] = request.mobile_url
        if not UtilClient.is_unset(request.pc_url):
            body['pcUrl'] = request.pc_url
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
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
            dingtalksearch__1__0_models.InsertSearchItemResponse(),
            await self.do_roarequest_async('InsertSearchItem', 'search_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/search/tabs/{tab_id}/items', 'none', req, runtime)
        )

    def list_search_tabs_by_org_id(self) -> dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.ListSearchTabsByOrgIdHeaders()
        return self.list_search_tabs_by_org_id_with_options(headers, runtime)

    async def list_search_tabs_by_org_id_async(self) -> dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.ListSearchTabsByOrgIdHeaders()
        return await self.list_search_tabs_by_org_id_with_options_async(headers, runtime)

    def list_search_tabs_by_org_id_with_options(
        self,
        headers: dingtalksearch__1__0_models.ListSearchTabsByOrgIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse(),
            self.do_roarequest('ListSearchTabsByOrgId', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs', 'json', req, runtime)
        )

    async def list_search_tabs_by_org_id_with_options_async(
        self,
        headers: dingtalksearch__1__0_models.ListSearchTabsByOrgIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalksearch__1__0_models.ListSearchTabsByOrgIdResponse(),
            await self.do_roarequest_async('ListSearchTabsByOrgId', 'search_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/search/tabs', 'json', req, runtime)
        )

    def update_search_tab(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.UpdateSearchTabRequest,
    ) -> dingtalksearch__1__0_models.UpdateSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.UpdateSearchTabHeaders()
        return self.update_search_tab_with_options(tab_id, request, headers, runtime)

    async def update_search_tab_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.UpdateSearchTabRequest,
    ) -> dingtalksearch__1__0_models.UpdateSearchTabResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalksearch__1__0_models.UpdateSearchTabHeaders()
        return await self.update_search_tab_with_options_async(tab_id, request, headers, runtime)

    def update_search_tab_with_options(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.UpdateSearchTabRequest,
        headers: dingtalksearch__1__0_models.UpdateSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.UpdateSearchTabResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
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
            dingtalksearch__1__0_models.UpdateSearchTabResponse(),
            self.do_roarequest('UpdateSearchTab', 'search_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/search/tabs/{tab_id}', 'none', req, runtime)
        )

    async def update_search_tab_with_options_async(
        self,
        tab_id: str,
        request: dingtalksearch__1__0_models.UpdateSearchTabRequest,
        headers: dingtalksearch__1__0_models.UpdateSearchTabHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalksearch__1__0_models.UpdateSearchTabResponse:
        UtilClient.validate_model(request)
        tab_id = OpenApiUtilClient.get_encode_param(tab_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
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
            dingtalksearch__1__0_models.UpdateSearchTabResponse(),
            await self.do_roarequest_async('UpdateSearchTab', 'search_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/search/tabs/{tab_id}', 'none', req, runtime)
        )
