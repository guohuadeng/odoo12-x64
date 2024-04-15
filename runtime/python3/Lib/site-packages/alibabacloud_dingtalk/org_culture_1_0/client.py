# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.org_culture_1_0 import models as dingtalkorg_culture__1__0_models
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

    def grant_honor(
        self,
        honor_id: str,
        request: dingtalkorg_culture__1__0_models.GrantHonorRequest,
    ) -> dingtalkorg_culture__1__0_models.GrantHonorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.GrantHonorHeaders()
        return self.grant_honor_with_options(honor_id, request, headers, runtime)

    async def grant_honor_async(
        self,
        honor_id: str,
        request: dingtalkorg_culture__1__0_models.GrantHonorRequest,
    ) -> dingtalkorg_culture__1__0_models.GrantHonorResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.GrantHonorHeaders()
        return await self.grant_honor_with_options_async(honor_id, request, headers, runtime)

    def grant_honor_with_options(
        self,
        honor_id: str,
        request: dingtalkorg_culture__1__0_models.GrantHonorRequest,
        headers: dingtalkorg_culture__1__0_models.GrantHonorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.GrantHonorResponse:
        UtilClient.validate_model(request)
        honor_id = OpenApiUtilClient.get_encode_param(honor_id)
        body = {}
        if not UtilClient.is_unset(request.expiration_time):
            body['expirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.grant_reason):
            body['grantReason'] = request.grant_reason
        if not UtilClient.is_unset(request.granter_name):
            body['granterName'] = request.granter_name
        if not UtilClient.is_unset(request.notice_announcer):
            body['noticeAnnouncer'] = request.notice_announcer
        if not UtilClient.is_unset(request.notice_single):
            body['noticeSingle'] = request.notice_single
        if not UtilClient.is_unset(request.receiver_user_ids):
            body['receiverUserIds'] = request.receiver_user_ids
        if not UtilClient.is_unset(request.sender_user_id):
            body['senderUserId'] = request.sender_user_id
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
            dingtalkorg_culture__1__0_models.GrantHonorResponse(),
            self.do_roarequest('GrantHonor', 'orgCulture_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/orgCulture/honors/{honor_id}/grant', 'json', req, runtime)
        )

    async def grant_honor_with_options_async(
        self,
        honor_id: str,
        request: dingtalkorg_culture__1__0_models.GrantHonorRequest,
        headers: dingtalkorg_culture__1__0_models.GrantHonorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.GrantHonorResponse:
        UtilClient.validate_model(request)
        honor_id = OpenApiUtilClient.get_encode_param(honor_id)
        body = {}
        if not UtilClient.is_unset(request.expiration_time):
            body['expirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.grant_reason):
            body['grantReason'] = request.grant_reason
        if not UtilClient.is_unset(request.granter_name):
            body['granterName'] = request.granter_name
        if not UtilClient.is_unset(request.notice_announcer):
            body['noticeAnnouncer'] = request.notice_announcer
        if not UtilClient.is_unset(request.notice_single):
            body['noticeSingle'] = request.notice_single
        if not UtilClient.is_unset(request.receiver_user_ids):
            body['receiverUserIds'] = request.receiver_user_ids
        if not UtilClient.is_unset(request.sender_user_id):
            body['senderUserId'] = request.sender_user_id
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
            dingtalkorg_culture__1__0_models.GrantHonorResponse(),
            await self.do_roarequest_async('GrantHonor', 'orgCulture_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/orgCulture/honors/{honor_id}/grant', 'json', req, runtime)
        )

    def query_org_honors(
        self,
        request: dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest,
    ) -> dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders()
        return self.query_org_honors_with_options(request, headers, runtime)

    async def query_org_honors_async(
        self,
        request: dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest,
    ) -> dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders()
        return await self.query_org_honors_with_options_async(request, headers, runtime)

    def query_org_honors_with_options(
        self,
        request: dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest,
        headers: dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse(),
            self.do_roarequest('QueryOrgHonors', 'orgCulture_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/orgCulture/organizations/honors', 'json', req, runtime)
        )

    async def query_org_honors_with_options_async(
        self,
        request: dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest,
        headers: dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            dingtalkorg_culture__1__0_models.QueryOrgHonorsResponse(),
            await self.do_roarequest_async('QueryOrgHonors', 'orgCulture_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/orgCulture/organizations/honors', 'json', req, runtime)
        )

    def query_user_honors(
        self,
        user_id: str,
        request: dingtalkorg_culture__1__0_models.QueryUserHonorsRequest,
    ) -> dingtalkorg_culture__1__0_models.QueryUserHonorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders()
        return self.query_user_honors_with_options(user_id, request, headers, runtime)

    async def query_user_honors_async(
        self,
        user_id: str,
        request: dingtalkorg_culture__1__0_models.QueryUserHonorsRequest,
    ) -> dingtalkorg_culture__1__0_models.QueryUserHonorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders()
        return await self.query_user_honors_with_options_async(user_id, request, headers, runtime)

    def query_user_honors_with_options(
        self,
        user_id: str,
        request: dingtalkorg_culture__1__0_models.QueryUserHonorsRequest,
        headers: dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.QueryUserHonorsResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
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
            dingtalkorg_culture__1__0_models.QueryUserHonorsResponse(),
            self.do_roarequest('QueryUserHonors', 'orgCulture_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/orgCulture/honors/users/{user_id}', 'json', req, runtime)
        )

    async def query_user_honors_with_options_async(
        self,
        user_id: str,
        request: dingtalkorg_culture__1__0_models.QueryUserHonorsRequest,
        headers: dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkorg_culture__1__0_models.QueryUserHonorsResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
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
            dingtalkorg_culture__1__0_models.QueryUserHonorsResponse(),
            await self.do_roarequest_async('QueryUserHonors', 'orgCulture_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/orgCulture/honors/users/{user_id}', 'json', req, runtime)
        )
