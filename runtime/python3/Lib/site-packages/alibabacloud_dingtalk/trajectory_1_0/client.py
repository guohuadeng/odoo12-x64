# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.trajectory_1_0 import models as dingtalktrajectory__1__0_models
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

    def query_app_active_users(
        self,
        request: dingtalktrajectory__1__0_models.QueryAppActiveUsersRequest,
    ) -> dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryAppActiveUsersHeaders()
        return self.query_app_active_users_with_options(request, headers, runtime)

    async def query_app_active_users_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryAppActiveUsersRequest,
    ) -> dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryAppActiveUsersHeaders()
        return await self.query_app_active_users_with_options_async(request, headers, runtime)

    def query_app_active_users_with_options(
        self,
        request: dingtalktrajectory__1__0_models.QueryAppActiveUsersRequest,
        headers: dingtalktrajectory__1__0_models.QueryAppActiveUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.need_position_info):
            query['needPositionInfo'] = request.need_position_info
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
            dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse(),
            self.do_roarequest('QueryAppActiveUsers', 'trajectory_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/trajectory/activeUsers', 'json', req, runtime)
        )

    async def query_app_active_users_with_options_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryAppActiveUsersRequest,
        headers: dingtalktrajectory__1__0_models.QueryAppActiveUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.need_position_info):
            query['needPositionInfo'] = request.need_position_info
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
            dingtalktrajectory__1__0_models.QueryAppActiveUsersResponse(),
            await self.do_roarequest_async('QueryAppActiveUsers', 'trajectory_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/trajectory/activeUsers', 'json', req, runtime)
        )

    def query_collecting_trace_task(
        self,
        request: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskRequest,
    ) -> dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryCollectingTraceTaskHeaders()
        return self.query_collecting_trace_task_with_options(request, headers, runtime)

    async def query_collecting_trace_task_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskRequest,
    ) -> dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryCollectingTraceTaskHeaders()
        return await self.query_collecting_trace_task_with_options_async(request, headers, runtime)

    def query_collecting_trace_task_with_options(
        self,
        request: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskRequest,
        headers: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
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
            dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse(),
            self.do_roarequest('QueryCollectingTraceTask', 'trajectory_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/trajectory/currentTasks/queryByUserIds', 'json', req, runtime)
        )

    async def query_collecting_trace_task_with_options_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskRequest,
        headers: dingtalktrajectory__1__0_models.QueryCollectingTraceTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
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
            dingtalktrajectory__1__0_models.QueryCollectingTraceTaskResponse(),
            await self.do_roarequest_async('QueryCollectingTraceTask', 'trajectory_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/trajectory/currentTasks/queryByUserIds', 'json', req, runtime)
        )

    def query_page_trace_data(
        self,
        request: dingtalktrajectory__1__0_models.QueryPageTraceDataRequest,
    ) -> dingtalktrajectory__1__0_models.QueryPageTraceDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryPageTraceDataHeaders()
        return self.query_page_trace_data_with_options(request, headers, runtime)

    async def query_page_trace_data_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryPageTraceDataRequest,
    ) -> dingtalktrajectory__1__0_models.QueryPageTraceDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalktrajectory__1__0_models.QueryPageTraceDataHeaders()
        return await self.query_page_trace_data_with_options_async(request, headers, runtime)

    def query_page_trace_data_with_options(
        self,
        request: dingtalktrajectory__1__0_models.QueryPageTraceDataRequest,
        headers: dingtalktrajectory__1__0_models.QueryPageTraceDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryPageTraceDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.staff_id):
            query['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
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
            dingtalktrajectory__1__0_models.QueryPageTraceDataResponse(),
            self.do_roarequest('QueryPageTraceData', 'trajectory_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/trajectory/data', 'json', req, runtime)
        )

    async def query_page_trace_data_with_options_async(
        self,
        request: dingtalktrajectory__1__0_models.QueryPageTraceDataRequest,
        headers: dingtalktrajectory__1__0_models.QueryPageTraceDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalktrajectory__1__0_models.QueryPageTraceDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.staff_id):
            query['staffId'] = request.staff_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
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
            dingtalktrajectory__1__0_models.QueryPageTraceDataResponse(),
            await self.do_roarequest_async('QueryPageTraceData', 'trajectory_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/trajectory/data', 'json', req, runtime)
        )
