# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.apaas_1_0 import models as dingtalkapaas__1__0_models
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

    def batch_create_template(
        self,
        request: dingtalkapaas__1__0_models.BatchCreateTemplateRequest,
    ) -> dingtalkapaas__1__0_models.BatchCreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchCreateTemplateHeaders()
        return self.batch_create_template_with_options(request, headers, runtime)

    async def batch_create_template_async(
        self,
        request: dingtalkapaas__1__0_models.BatchCreateTemplateRequest,
    ) -> dingtalkapaas__1__0_models.BatchCreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchCreateTemplateHeaders()
        return await self.batch_create_template_with_options_async(request, headers, runtime)

    def batch_create_template_with_options(
        self,
        request: dingtalkapaas__1__0_models.BatchCreateTemplateRequest,
        headers: dingtalkapaas__1__0_models.BatchCreateTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchCreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_list):
            body['templateList'] = request.template_list
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
            dingtalkapaas__1__0_models.BatchCreateTemplateResponse(),
            self.do_roarequest('BatchCreateTemplate', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates', 'json', req, runtime)
        )

    async def batch_create_template_with_options_async(
        self,
        request: dingtalkapaas__1__0_models.BatchCreateTemplateRequest,
        headers: dingtalkapaas__1__0_models.BatchCreateTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchCreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_list):
            body['templateList'] = request.template_list
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
            dingtalkapaas__1__0_models.BatchCreateTemplateResponse(),
            await self.do_roarequest_async('BatchCreateTemplate', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates', 'json', req, runtime)
        )

    def batch_query_by_template_key(
        self,
        request: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyRequest,
    ) -> dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchQueryByTemplateKeyHeaders()
        return self.batch_query_by_template_key_with_options(request, headers, runtime)

    async def batch_query_by_template_key_async(
        self,
        request: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyRequest,
    ) -> dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchQueryByTemplateKeyHeaders()
        return await self.batch_query_by_template_key_with_options_async(request, headers, runtime)

    def batch_query_by_template_key_with_options(
        self,
        request: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyRequest,
        headers: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_keys):
            body['templateKeys'] = request.template_keys
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
            dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse(),
            self.do_roarequest('BatchQueryByTemplateKey', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates/query', 'json', req, runtime)
        )

    async def batch_query_by_template_key_with_options_async(
        self,
        request: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyRequest,
        headers: dingtalkapaas__1__0_models.BatchQueryByTemplateKeyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_keys):
            body['templateKeys'] = request.template_keys
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
            dingtalkapaas__1__0_models.BatchQueryByTemplateKeyResponse(),
            await self.do_roarequest_async('BatchQueryByTemplateKey', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates/query', 'json', req, runtime)
        )

    def batch_update_template(
        self,
        request: dingtalkapaas__1__0_models.BatchUpdateTemplateRequest,
    ) -> dingtalkapaas__1__0_models.BatchUpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchUpdateTemplateHeaders()
        return self.batch_update_template_with_options(request, headers, runtime)

    async def batch_update_template_async(
        self,
        request: dingtalkapaas__1__0_models.BatchUpdateTemplateRequest,
    ) -> dingtalkapaas__1__0_models.BatchUpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.BatchUpdateTemplateHeaders()
        return await self.batch_update_template_with_options_async(request, headers, runtime)

    def batch_update_template_with_options(
        self,
        request: dingtalkapaas__1__0_models.BatchUpdateTemplateRequest,
        headers: dingtalkapaas__1__0_models.BatchUpdateTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchUpdateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_list):
            body['templateList'] = request.template_list
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
            dingtalkapaas__1__0_models.BatchUpdateTemplateResponse(),
            self.do_roarequest('BatchUpdateTemplate', 'apaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/apaas/templates', 'json', req, runtime)
        )

    async def batch_update_template_with_options_async(
        self,
        request: dingtalkapaas__1__0_models.BatchUpdateTemplateRequest,
        headers: dingtalkapaas__1__0_models.BatchUpdateTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.BatchUpdateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_list):
            body['templateList'] = request.template_list
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
            dingtalkapaas__1__0_models.BatchUpdateTemplateResponse(),
            await self.do_roarequest_async('BatchUpdateTemplate', 'apaas_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/apaas/templates', 'json', req, runtime)
        )

    def query_industry_tag_list(self) -> dingtalkapaas__1__0_models.QueryIndustryTagListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryIndustryTagListHeaders()
        return self.query_industry_tag_list_with_options(headers, runtime)

    async def query_industry_tag_list_async(self) -> dingtalkapaas__1__0_models.QueryIndustryTagListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryIndustryTagListHeaders()
        return await self.query_industry_tag_list_with_options_async(headers, runtime)

    def query_industry_tag_list_with_options(
        self,
        headers: dingtalkapaas__1__0_models.QueryIndustryTagListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryIndustryTagListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryIndustryTagListResponse(),
            self.do_roarequest('QueryIndustryTagList', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/industries', 'json', req, runtime)
        )

    async def query_industry_tag_list_with_options_async(
        self,
        headers: dingtalkapaas__1__0_models.QueryIndustryTagListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryIndustryTagListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryIndustryTagListResponse(),
            await self.do_roarequest_async('QueryIndustryTagList', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/industries', 'json', req, runtime)
        )

    def query_role_tag_list(self) -> dingtalkapaas__1__0_models.QueryRoleTagListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryRoleTagListHeaders()
        return self.query_role_tag_list_with_options(headers, runtime)

    async def query_role_tag_list_async(self) -> dingtalkapaas__1__0_models.QueryRoleTagListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryRoleTagListHeaders()
        return await self.query_role_tag_list_with_options_async(headers, runtime)

    def query_role_tag_list_with_options(
        self,
        headers: dingtalkapaas__1__0_models.QueryRoleTagListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryRoleTagListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryRoleTagListResponse(),
            self.do_roarequest('QueryRoleTagList', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/roles', 'json', req, runtime)
        )

    async def query_role_tag_list_with_options_async(
        self,
        headers: dingtalkapaas__1__0_models.QueryRoleTagListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryRoleTagListResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryRoleTagListResponse(),
            await self.do_roarequest_async('QueryRoleTagList', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/roles', 'json', req, runtime)
        )

    def query_template_categorys(self) -> dingtalkapaas__1__0_models.QueryTemplateCategorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryTemplateCategorysHeaders()
        return self.query_template_categorys_with_options(headers, runtime)

    async def query_template_categorys_async(self) -> dingtalkapaas__1__0_models.QueryTemplateCategorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.QueryTemplateCategorysHeaders()
        return await self.query_template_categorys_with_options_async(headers, runtime)

    def query_template_categorys_with_options(
        self,
        headers: dingtalkapaas__1__0_models.QueryTemplateCategorysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryTemplateCategorysResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryTemplateCategorysResponse(),
            self.do_roarequest('QueryTemplateCategorys', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/categories', 'json', req, runtime)
        )

    async def query_template_categorys_with_options_async(
        self,
        headers: dingtalkapaas__1__0_models.QueryTemplateCategorysHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.QueryTemplateCategorysResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkapaas__1__0_models.QueryTemplateCategorysResponse(),
            await self.do_roarequest_async('QueryTemplateCategorys', 'apaas_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/apaas/templates/categories', 'json', req, runtime)
        )

    def recall_audit_template(
        self,
        request: dingtalkapaas__1__0_models.RecallAuditTemplateRequest,
    ) -> dingtalkapaas__1__0_models.RecallAuditTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.RecallAuditTemplateHeaders()
        return self.recall_audit_template_with_options(request, headers, runtime)

    async def recall_audit_template_async(
        self,
        request: dingtalkapaas__1__0_models.RecallAuditTemplateRequest,
    ) -> dingtalkapaas__1__0_models.RecallAuditTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkapaas__1__0_models.RecallAuditTemplateHeaders()
        return await self.recall_audit_template_with_options_async(request, headers, runtime)

    def recall_audit_template_with_options(
        self,
        request: dingtalkapaas__1__0_models.RecallAuditTemplateRequest,
        headers: dingtalkapaas__1__0_models.RecallAuditTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.RecallAuditTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_keys):
            body['templateKeys'] = request.template_keys
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
            dingtalkapaas__1__0_models.RecallAuditTemplateResponse(),
            self.do_roarequest('RecallAuditTemplate', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates/audits/recall', 'json', req, runtime)
        )

    async def recall_audit_template_with_options_async(
        self,
        request: dingtalkapaas__1__0_models.RecallAuditTemplateRequest,
        headers: dingtalkapaas__1__0_models.RecallAuditTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkapaas__1__0_models.RecallAuditTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_keys):
            body['templateKeys'] = request.template_keys
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
            dingtalkapaas__1__0_models.RecallAuditTemplateResponse(),
            await self.do_roarequest_async('RecallAuditTemplate', 'apaas_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/apaas/templates/audits/recall', 'json', req, runtime)
        )
