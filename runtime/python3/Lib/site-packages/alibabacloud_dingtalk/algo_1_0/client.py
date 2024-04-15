# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.algo_1_0 import models as dingtalkalgo__1__0_models
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

    def nlp_word_distinguish(
        self,
        request: dingtalkalgo__1__0_models.NlpWordDistinguishRequest,
    ) -> dingtalkalgo__1__0_models.NlpWordDistinguishResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalgo__1__0_models.NlpWordDistinguishHeaders()
        return self.nlp_word_distinguish_with_options(request, headers, runtime)

    async def nlp_word_distinguish_async(
        self,
        request: dingtalkalgo__1__0_models.NlpWordDistinguishRequest,
    ) -> dingtalkalgo__1__0_models.NlpWordDistinguishResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalgo__1__0_models.NlpWordDistinguishHeaders()
        return await self.nlp_word_distinguish_with_options_async(request, headers, runtime)

    def nlp_word_distinguish_with_options(
        self,
        request: dingtalkalgo__1__0_models.NlpWordDistinguishRequest,
        headers: dingtalkalgo__1__0_models.NlpWordDistinguishHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalgo__1__0_models.NlpWordDistinguishResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_extract_decision_info):
            body['attachExtractDecisionInfo'] = request.attach_extract_decision_info
        if not UtilClient.is_unset(request.isv_app_id):
            body['isvAppId'] = request.isv_app_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
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
            dingtalkalgo__1__0_models.NlpWordDistinguishResponse(),
            self.do_roarequest('NlpWordDistinguish', 'algo_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/algo/okrs/keywords/extract', 'json', req, runtime)
        )

    async def nlp_word_distinguish_with_options_async(
        self,
        request: dingtalkalgo__1__0_models.NlpWordDistinguishRequest,
        headers: dingtalkalgo__1__0_models.NlpWordDistinguishHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalgo__1__0_models.NlpWordDistinguishResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attach_extract_decision_info):
            body['attachExtractDecisionInfo'] = request.attach_extract_decision_info
        if not UtilClient.is_unset(request.isv_app_id):
            body['isvAppId'] = request.isv_app_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
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
            dingtalkalgo__1__0_models.NlpWordDistinguishResponse(),
            await self.do_roarequest_async('NlpWordDistinguish', 'algo_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/algo/okrs/keywords/extract', 'json', req, runtime)
        )

    def okr_open_recommend(
        self,
        request: dingtalkalgo__1__0_models.OkrOpenRecommendRequest,
    ) -> dingtalkalgo__1__0_models.OkrOpenRecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalgo__1__0_models.OkrOpenRecommendHeaders()
        return self.okr_open_recommend_with_options(request, headers, runtime)

    async def okr_open_recommend_async(
        self,
        request: dingtalkalgo__1__0_models.OkrOpenRecommendRequest,
    ) -> dingtalkalgo__1__0_models.OkrOpenRecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalgo__1__0_models.OkrOpenRecommendHeaders()
        return await self.okr_open_recommend_with_options_async(request, headers, runtime)

    def okr_open_recommend_with_options(
        self,
        request: dingtalkalgo__1__0_models.OkrOpenRecommendRequest,
        headers: dingtalkalgo__1__0_models.OkrOpenRecommendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalgo__1__0_models.OkrOpenRecommendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.candidate_okr_items):
            body['candidateOkrItems'] = request.candidate_okr_items
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.isv_app_id):
            body['isvAppId'] = request.isv_app_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.words):
            body['words'] = request.words
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
            dingtalkalgo__1__0_models.OkrOpenRecommendResponse(),
            self.do_roarequest('OkrOpenRecommend', 'algo_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/algo/okrs/recommend', 'json', req, runtime)
        )

    async def okr_open_recommend_with_options_async(
        self,
        request: dingtalkalgo__1__0_models.OkrOpenRecommendRequest,
        headers: dingtalkalgo__1__0_models.OkrOpenRecommendHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalgo__1__0_models.OkrOpenRecommendResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.candidate_okr_items):
            body['candidateOkrItems'] = request.candidate_okr_items
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.isv_app_id):
            body['isvAppId'] = request.isv_app_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.words):
            body['words'] = request.words
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
            dingtalkalgo__1__0_models.OkrOpenRecommendResponse(),
            await self.do_roarequest_async('OkrOpenRecommend', 'algo_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/algo/okrs/recommend', 'json', req, runtime)
        )
