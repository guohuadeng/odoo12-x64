# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
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

    def create_jsapi_ticket(self) -> dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.CreateJsapiTicketHeaders()
        return self.create_jsapi_ticket_with_options(headers, runtime)

    async def create_jsapi_ticket_async(self) -> dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.CreateJsapiTicketHeaders()
        return await self.create_jsapi_ticket_with_options_async(headers, runtime)

    def create_jsapi_ticket_with_options(
        self,
        headers: dingtalkoauth_2__1__0_models.CreateJsapiTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse(),
            self.do_roarequest('CreateJsapiTicket', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/jsapiTickets', 'json', req, runtime)
        )

    async def create_jsapi_ticket_with_options_async(
        self,
        headers: dingtalkoauth_2__1__0_models.CreateJsapiTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.CreateJsapiTicketResponse(),
            await self.do_roarequest_async('CreateJsapiTicket', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/jsapiTickets', 'json', req, runtime)
        )

    def get_access_token(
        self,
        request: dingtalkoauth_2__1__0_models.GetAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_access_token_with_options(request, headers, runtime)

    async def get_access_token_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_access_token_with_options_async(request, headers, runtime)

    def get_access_token_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['appKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['appSecret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetAccessTokenResponse(),
            self.do_roarequest('GetAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/accessToken', 'json', req, runtime)
        )

    async def get_access_token_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['appKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['appSecret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetAccessTokenResponse(),
            await self.do_roarequest_async('GetAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/accessToken', 'json', req, runtime)
        )

    def get_auth_info(
        self,
        request: dingtalkoauth_2__1__0_models.GetAuthInfoRequest,
    ) -> dingtalkoauth_2__1__0_models.GetAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetAuthInfoHeaders()
        return self.get_auth_info_with_options(request, headers, runtime)

    async def get_auth_info_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetAuthInfoRequest,
    ) -> dingtalkoauth_2__1__0_models.GetAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetAuthInfoHeaders()
        return await self.get_auth_info_with_options_async(request, headers, runtime)

    def get_auth_info_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetAuthInfoRequest,
        headers: dingtalkoauth_2__1__0_models.GetAuthInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetAuthInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_corp_id):
            query['authCorpId'] = request.auth_corp_id
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
            dingtalkoauth_2__1__0_models.GetAuthInfoResponse(),
            self.do_roarequest('GetAuthInfo', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/apps/authInfo', 'json', req, runtime)
        )

    async def get_auth_info_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetAuthInfoRequest,
        headers: dingtalkoauth_2__1__0_models.GetAuthInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetAuthInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_corp_id):
            query['authCorpId'] = request.auth_corp_id
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
            dingtalkoauth_2__1__0_models.GetAuthInfoResponse(),
            await self.do_roarequest_async('GetAuthInfo', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/apps/authInfo', 'json', req, runtime)
        )

    def get_corp_access_token(
        self,
        request: dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_corp_access_token_with_options(request, headers, runtime)

    async def get_corp_access_token_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_corp_access_token_with_options_async(request, headers, runtime)

    def get_corp_access_token_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_corp_id):
            body['authCorpId'] = request.auth_corp_id
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.suite_secret):
            body['suiteSecret'] = request.suite_secret
        if not UtilClient.is_unset(request.suite_ticket):
            body['suiteTicket'] = request.suite_ticket
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse(),
            self.do_roarequest('GetCorpAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/corpAccessToken', 'json', req, runtime)
        )

    async def get_corp_access_token_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_corp_id):
            body['authCorpId'] = request.auth_corp_id
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.suite_secret):
            body['suiteSecret'] = request.suite_secret
        if not UtilClient.is_unset(request.suite_ticket):
            body['suiteTicket'] = request.suite_ticket
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetCorpAccessTokenResponse(),
            await self.do_roarequest_async('GetCorpAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/corpAccessToken', 'json', req, runtime)
        )

    def get_personal_auth_rule(self) -> dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders()
        return self.get_personal_auth_rule_with_options(headers, runtime)

    async def get_personal_auth_rule_async(self) -> dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders()
        return await self.get_personal_auth_rule_with_options_async(headers, runtime)

    def get_personal_auth_rule_with_options(
        self,
        headers: dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse(),
            self.do_roarequest('GetPersonalAuthRule', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/authRules/user', 'json', req, runtime)
        )

    async def get_personal_auth_rule_with_options_async(
        self,
        headers: dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetPersonalAuthRuleResponse(),
            await self.do_roarequest_async('GetPersonalAuthRule', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/authRules/user', 'json', req, runtime)
        )

    def get_sso_access_token(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sso_access_token_with_options(request, headers, runtime)

    async def get_sso_access_token_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sso_access_token_with_options_async(request, headers, runtime)

    def get_sso_access_token_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corpid):
            body['corpid'] = request.corpid
        if not UtilClient.is_unset(request.sso_secret):
            body['ssoSecret'] = request.sso_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse(),
            self.do_roarequest('GetSsoAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/ssoAccessToken', 'json', req, runtime)
        )

    async def get_sso_access_token_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corpid):
            body['corpid'] = request.corpid
        if not UtilClient.is_unset(request.sso_secret):
            body['ssoSecret'] = request.sso_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetSsoAccessTokenResponse(),
            await self.do_roarequest_async('GetSsoAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/ssoAccessToken', 'json', req, runtime)
        )

    def get_sso_user_info(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders()
        return self.get_sso_user_info_with_options(request, headers, runtime)

    async def get_sso_user_info_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders()
        return await self.get_sso_user_info_with_options_async(request, headers, runtime)

    def get_sso_user_info_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest,
        headers: dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse:
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
            dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse(),
            self.do_roarequest('GetSsoUserInfo', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/ssoUserInfo', 'json', req, runtime)
        )

    async def get_sso_user_info_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest,
        headers: dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse:
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
            dingtalkoauth_2__1__0_models.GetSsoUserInfoResponse(),
            await self.do_roarequest_async('GetSsoUserInfo', 'oauth2_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/oauth2/ssoUserInfo', 'json', req, runtime)
        )

    def get_suite_access_token(
        self,
        request: dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_suite_access_token_with_options(request, headers, runtime)

    async def get_suite_access_token_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_suite_access_token_with_options_async(request, headers, runtime)

    def get_suite_access_token_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.suite_secret):
            body['suiteSecret'] = request.suite_secret
        if not UtilClient.is_unset(request.suite_ticket):
            body['suiteTicket'] = request.suite_ticket
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse(),
            self.do_roarequest('GetSuiteAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/suiteAccessToken', 'json', req, runtime)
        )

    async def get_suite_access_token_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.suite_secret):
            body['suiteSecret'] = request.suite_secret
        if not UtilClient.is_unset(request.suite_ticket):
            body['suiteTicket'] = request.suite_ticket
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetSuiteAccessTokenResponse(),
            await self.do_roarequest_async('GetSuiteAccessToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/suiteAccessToken', 'json', req, runtime)
        )

    def get_user_token(
        self,
        request: dingtalkoauth_2__1__0_models.GetUserTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_token_with_options(request, headers, runtime)

    async def get_user_token_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetUserTokenRequest,
    ) -> dingtalkoauth_2__1__0_models.GetUserTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_token_with_options_async(request, headers, runtime)

    def get_user_token_with_options(
        self,
        request: dingtalkoauth_2__1__0_models.GetUserTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetUserTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.refresh_token):
            body['refreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetUserTokenResponse(),
            self.do_roarequest('GetUserToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/userAccessToken', 'json', req, runtime)
        )

    async def get_user_token_with_options_async(
        self,
        request: dingtalkoauth_2__1__0_models.GetUserTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkoauth_2__1__0_models.GetUserTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.refresh_token):
            body['refreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkoauth_2__1__0_models.GetUserTokenResponse(),
            await self.do_roarequest_async('GetUserToken', 'oauth2_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/oauth2/userAccessToken', 'json', req, runtime)
        )
