# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.app_market_1_0 import models as dingtalkapp_market__1__0_models
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

    def create_app_goods_service_conversation(
        self,
        request: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationRequest,
    ) -> dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationHeaders()
        return self.create_app_goods_service_conversation_with_options(request, headers, runtime)

    async def create_app_goods_service_conversation_async(
        self,
        request: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationRequest,
    ) -> dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationHeaders()
        return await self.create_app_goods_service_conversation_with_options_async(request, headers, runtime)

    def create_app_goods_service_conversation_with_options(
        self,
        request: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationRequest,
        headers: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.isv_user_id):
            body['isvUserId'] = request.isv_user_id
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
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
            dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse(),
            self.do_roarequest('CreateAppGoodsServiceConversation', 'appMarket_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/appMarket/orders/serviceGroups', 'json', req, runtime)
        )

    async def create_app_goods_service_conversation_with_options_async(
        self,
        request: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationRequest,
        headers: dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.isv_user_id):
            body['isvUserId'] = request.isv_user_id
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
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
            dingtalkapp_market__1__0_models.CreateAppGoodsServiceConversationResponse(),
            await self.do_roarequest_async('CreateAppGoodsServiceConversation', 'appMarket_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/appMarket/orders/serviceGroups', 'json', req, runtime)
        )

    def get_personal_experience_info(
        self,
        request: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoRequest,
    ) -> dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.GetPersonalExperienceInfoHeaders()
        return self.get_personal_experience_info_with_options(request, headers, runtime)

    async def get_personal_experience_info_async(
        self,
        request: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoRequest,
    ) -> dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.GetPersonalExperienceInfoHeaders()
        return await self.get_personal_experience_info_with_options_async(request, headers, runtime)

    def get_personal_experience_info_with_options(
        self,
        request: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoRequest,
        headers: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse(),
            self.do_roarequest('GetPersonalExperienceInfo', 'appMarket_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/appMarket/personalExperiences', 'json', req, runtime)
        )

    async def get_personal_experience_info_with_options_async(
        self,
        request: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoRequest,
        headers: dingtalkapp_market__1__0_models.GetPersonalExperienceInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkapp_market__1__0_models.GetPersonalExperienceInfoResponse(),
            await self.do_roarequest_async('GetPersonalExperienceInfo', 'appMarket_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/appMarket/personalExperiences', 'json', req, runtime)
        )

    def query_market_order(
        self,
        order_id: str,
    ) -> dingtalkapp_market__1__0_models.QueryMarketOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.QueryMarketOrderHeaders()
        return self.query_market_order_with_options(order_id, headers, runtime)

    async def query_market_order_async(
        self,
        order_id: str,
    ) -> dingtalkapp_market__1__0_models.QueryMarketOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.QueryMarketOrderHeaders()
        return await self.query_market_order_with_options_async(order_id, headers, runtime)

    def query_market_order_with_options(
        self,
        order_id: str,
        headers: dingtalkapp_market__1__0_models.QueryMarketOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.QueryMarketOrderResponse:
        order_id = OpenApiUtilClient.get_encode_param(order_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapp_market__1__0_models.QueryMarketOrderResponse(),
            self.do_roarequest('QueryMarketOrder', 'appMarket_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/appMarket/orders/{order_id}', 'json', req, runtime)
        )

    async def query_market_order_with_options_async(
        self,
        order_id: str,
        headers: dingtalkapp_market__1__0_models.QueryMarketOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.QueryMarketOrderResponse:
        order_id = OpenApiUtilClient.get_encode_param(order_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapp_market__1__0_models.QueryMarketOrderResponse(),
            await self.do_roarequest_async('QueryMarketOrder', 'appMarket_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/appMarket/orders/{order_id}', 'json', req, runtime)
        )

    def user_task_report(
        self,
        request: dingtalkapp_market__1__0_models.UserTaskReportRequest,
    ) -> dingtalkapp_market__1__0_models.UserTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.UserTaskReportHeaders()
        return self.user_task_report_with_options(request, headers, runtime)

    async def user_task_report_async(
        self,
        request: dingtalkapp_market__1__0_models.UserTaskReportRequest,
    ) -> dingtalkapp_market__1__0_models.UserTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapp_market__1__0_models.UserTaskReportHeaders()
        return await self.user_task_report_with_options_async(request, headers, runtime)

    def user_task_report_with_options(
        self,
        request: dingtalkapp_market__1__0_models.UserTaskReportRequest,
        headers: dingtalkapp_market__1__0_models.UserTaskReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.UserTaskReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_no):
            body['bizNo'] = request.biz_no
        if not UtilClient.is_unset(request.operate_date):
            body['operateDate'] = request.operate_date
        if not UtilClient.is_unset(request.task_tag):
            body['taskTag'] = request.task_tag
        if not UtilClient.is_unset(request.userid):
            body['userid'] = request.userid
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
            dingtalkapp_market__1__0_models.UserTaskReportResponse(),
            self.do_roarequest('UserTaskReport', 'appMarket_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/appMarket/tasks', 'boolean', req, runtime)
        )

    async def user_task_report_with_options_async(
        self,
        request: dingtalkapp_market__1__0_models.UserTaskReportRequest,
        headers: dingtalkapp_market__1__0_models.UserTaskReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapp_market__1__0_models.UserTaskReportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_no):
            body['bizNo'] = request.biz_no
        if not UtilClient.is_unset(request.operate_date):
            body['operateDate'] = request.operate_date
        if not UtilClient.is_unset(request.task_tag):
            body['taskTag'] = request.task_tag
        if not UtilClient.is_unset(request.userid):
            body['userid'] = request.userid
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
            dingtalkapp_market__1__0_models.UserTaskReportResponse(),
            await self.do_roarequest_async('UserTaskReport', 'appMarket_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/appMarket/tasks', 'boolean', req, runtime)
        )
