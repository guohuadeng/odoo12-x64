# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
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

    def add_hrm_preentry(
        self,
        request: dingtalkhrm__1__0_models.AddHrmPreentryRequest,
    ) -> dingtalkhrm__1__0_models.AddHrmPreentryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.AddHrmPreentryHeaders()
        return self.add_hrm_preentry_with_options(request, headers, runtime)

    async def add_hrm_preentry_async(
        self,
        request: dingtalkhrm__1__0_models.AddHrmPreentryRequest,
    ) -> dingtalkhrm__1__0_models.AddHrmPreentryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.AddHrmPreentryHeaders()
        return await self.add_hrm_preentry_with_options_async(request, headers, runtime)

    def add_hrm_preentry_with_options(
        self,
        request: dingtalkhrm__1__0_models.AddHrmPreentryRequest,
        headers: dingtalkhrm__1__0_models.AddHrmPreentryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.AddHrmPreentryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.groups):
            body['groups'] = request.groups
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pre_entry_time):
            body['preEntryTime'] = request.pre_entry_time
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
            dingtalkhrm__1__0_models.AddHrmPreentryResponse(),
            self.do_roarequest('AddHrmPreentry', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/preentries', 'json', req, runtime)
        )

    async def add_hrm_preentry_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.AddHrmPreentryRequest,
        headers: dingtalkhrm__1__0_models.AddHrmPreentryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.AddHrmPreentryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.groups):
            body['groups'] = request.groups
        if not UtilClient.is_unset(request.mobile):
            body['mobile'] = request.mobile
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pre_entry_time):
            body['preEntryTime'] = request.pre_entry_time
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
            dingtalkhrm__1__0_models.AddHrmPreentryResponse(),
            await self.do_roarequest_async('AddHrmPreentry', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/preentries', 'json', req, runtime)
        )

    def e_cert_query(
        self,
        request: dingtalkhrm__1__0_models.ECertQueryRequest,
    ) -> dingtalkhrm__1__0_models.ECertQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.ECertQueryHeaders()
        return self.e_cert_query_with_options(request, headers, runtime)

    async def e_cert_query_async(
        self,
        request: dingtalkhrm__1__0_models.ECertQueryRequest,
    ) -> dingtalkhrm__1__0_models.ECertQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.ECertQueryHeaders()
        return await self.e_cert_query_with_options_async(request, headers, runtime)

    def e_cert_query_with_options(
        self,
        request: dingtalkhrm__1__0_models.ECertQueryRequest,
        headers: dingtalkhrm__1__0_models.ECertQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.ECertQueryResponse:
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
            dingtalkhrm__1__0_models.ECertQueryResponse(),
            self.do_roarequest('ECertQuery', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/eCerts', 'json', req, runtime)
        )

    async def e_cert_query_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.ECertQueryRequest,
        headers: dingtalkhrm__1__0_models.ECertQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.ECertQueryResponse:
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
            dingtalkhrm__1__0_models.ECertQueryResponse(),
            await self.do_roarequest_async('ECertQuery', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/eCerts', 'json', req, runtime)
        )

    def master_data_query(
        self,
        request: dingtalkhrm__1__0_models.MasterDataQueryRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataQueryHeaders()
        return self.master_data_query_with_options(request, headers, runtime)

    async def master_data_query_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataQueryRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataQueryHeaders()
        return await self.master_data_query_with_options_async(request, headers, runtime)

    def master_data_query_with_options(
        self,
        request: dingtalkhrm__1__0_models.MasterDataQueryRequest,
        headers: dingtalkhrm__1__0_models.MasterDataQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_uk):
            body['bizUK'] = request.biz_uk
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.opt_user_id):
            body['optUserId'] = request.opt_user_id
        if not UtilClient.is_unset(request.query_params):
            body['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.relation_ids):
            body['relationIds'] = request.relation_ids
        if not UtilClient.is_unset(request.scope_code):
            body['scopeCode'] = request.scope_code
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.view_entity_code):
            body['viewEntityCode'] = request.view_entity_code
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
            dingtalkhrm__1__0_models.MasterDataQueryResponse(),
            self.do_roarequest('MasterDataQuery', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/masters/datas/query', 'json', req, runtime)
        )

    async def master_data_query_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataQueryRequest,
        headers: dingtalkhrm__1__0_models.MasterDataQueryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_uk):
            body['bizUK'] = request.biz_uk
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.opt_user_id):
            body['optUserId'] = request.opt_user_id
        if not UtilClient.is_unset(request.query_params):
            body['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.relation_ids):
            body['relationIds'] = request.relation_ids
        if not UtilClient.is_unset(request.scope_code):
            body['scopeCode'] = request.scope_code
        if not UtilClient.is_unset(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.view_entity_code):
            body['viewEntityCode'] = request.view_entity_code
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
            dingtalkhrm__1__0_models.MasterDataQueryResponse(),
            await self.do_roarequest_async('MasterDataQuery', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/masters/datas/query', 'json', req, runtime)
        )

    def master_data_save(
        self,
        request: dingtalkhrm__1__0_models.MasterDataSaveRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataSaveHeaders()
        return self.master_data_save_with_options(request, headers, runtime)

    async def master_data_save_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataSaveRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataSaveResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataSaveHeaders()
        return await self.master_data_save_with_options_async(request, headers, runtime)

    def master_data_save_with_options(
        self,
        request: dingtalkhrm__1__0_models.MasterDataSaveRequest,
        headers: dingtalkhrm__1__0_models.MasterDataSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataSaveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            dingtalkhrm__1__0_models.MasterDataSaveResponse(),
            self.do_roarequest('MasterDataSave', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/masters/datas/save', 'json', req, runtime)
        )

    async def master_data_save_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataSaveRequest,
        headers: dingtalkhrm__1__0_models.MasterDataSaveHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataSaveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            dingtalkhrm__1__0_models.MasterDataSaveResponse(),
            await self.do_roarequest_async('MasterDataSave', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/masters/datas/save', 'json', req, runtime)
        )

    def master_data_tenant_quey(
        self,
        request: dingtalkhrm__1__0_models.MasterDataTenantQueyRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataTenantQueyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataTenantQueyHeaders()
        return self.master_data_tenant_quey_with_options(request, headers, runtime)

    async def master_data_tenant_quey_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataTenantQueyRequest,
    ) -> dingtalkhrm__1__0_models.MasterDataTenantQueyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.MasterDataTenantQueyHeaders()
        return await self.master_data_tenant_quey_with_options_async(request, headers, runtime)

    def master_data_tenant_quey_with_options(
        self,
        request: dingtalkhrm__1__0_models.MasterDataTenantQueyRequest,
        headers: dingtalkhrm__1__0_models.MasterDataTenantQueyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataTenantQueyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_code):
            query['entityCode'] = request.entity_code
        if not UtilClient.is_unset(request.scope_code):
            query['scopeCode'] = request.scope_code
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
            dingtalkhrm__1__0_models.MasterDataTenantQueyResponse(),
            self.do_roarequest('MasterDataTenantQuey', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/masters/tenants', 'json', req, runtime)
        )

    async def master_data_tenant_quey_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.MasterDataTenantQueyRequest,
        headers: dingtalkhrm__1__0_models.MasterDataTenantQueyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.MasterDataTenantQueyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_code):
            query['entityCode'] = request.entity_code
        if not UtilClient.is_unset(request.scope_code):
            query['scopeCode'] = request.scope_code
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
            dingtalkhrm__1__0_models.MasterDataTenantQueyResponse(),
            await self.do_roarequest_async('MasterDataTenantQuey', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/masters/tenants', 'json', req, runtime)
        )

    def query_custom_entry_processes(
        self,
        request: dingtalkhrm__1__0_models.QueryCustomEntryProcessesRequest,
    ) -> dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryCustomEntryProcessesHeaders()
        return self.query_custom_entry_processes_with_options(request, headers, runtime)

    async def query_custom_entry_processes_async(
        self,
        request: dingtalkhrm__1__0_models.QueryCustomEntryProcessesRequest,
    ) -> dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryCustomEntryProcessesHeaders()
        return await self.query_custom_entry_processes_with_options_async(request, headers, runtime)

    def query_custom_entry_processes_with_options(
        self,
        request: dingtalkhrm__1__0_models.QueryCustomEntryProcessesRequest,
        headers: dingtalkhrm__1__0_models.QueryCustomEntryProcessesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operate_user_id):
            query['operateUserId'] = request.operate_user_id
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
            dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse(),
            self.do_roarequest('QueryCustomEntryProcesses', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/customEntryProcesses', 'json', req, runtime)
        )

    async def query_custom_entry_processes_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.QueryCustomEntryProcessesRequest,
        headers: dingtalkhrm__1__0_models.QueryCustomEntryProcessesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operate_user_id):
            query['operateUserId'] = request.operate_user_id
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
            dingtalkhrm__1__0_models.QueryCustomEntryProcessesResponse(),
            await self.do_roarequest_async('QueryCustomEntryProcesses', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/customEntryProcesses', 'json', req, runtime)
        )

    def query_hrm_employee_dismission_info(
        self,
        request: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest,
    ) -> dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders()
        return self.query_hrm_employee_dismission_info_with_options(request, headers, runtime)

    async def query_hrm_employee_dismission_info_async(
        self,
        request: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest,
    ) -> dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders()
        return await self.query_hrm_employee_dismission_info_with_options_async(request, headers, runtime)

    def query_hrm_employee_dismission_info_with_options(
        self,
        tmp_req: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest,
        headers: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_id_list):
            request.user_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_id_list, 'userIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_id_list_shrink):
            query['userIdList'] = request.user_id_list_shrink
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
            dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse(),
            self.do_roarequest('QueryHrmEmployeeDismissionInfo', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/employees/dimissionInfos', 'json', req, runtime)
        )

    async def query_hrm_employee_dismission_info_with_options_async(
        self,
        tmp_req: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest,
        headers: dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_id_list):
            request.user_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_id_list, 'userIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_id_list_shrink):
            query['userIdList'] = request.user_id_list_shrink
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
            dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoResponse(),
            await self.do_roarequest_async('QueryHrmEmployeeDismissionInfo', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/employees/dimissionInfos', 'json', req, runtime)
        )

    def query_job_ranks(
        self,
        request: dingtalkhrm__1__0_models.QueryJobRanksRequest,
    ) -> dingtalkhrm__1__0_models.QueryJobRanksResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryJobRanksHeaders()
        return self.query_job_ranks_with_options(request, headers, runtime)

    async def query_job_ranks_async(
        self,
        request: dingtalkhrm__1__0_models.QueryJobRanksRequest,
    ) -> dingtalkhrm__1__0_models.QueryJobRanksResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryJobRanksHeaders()
        return await self.query_job_ranks_with_options_async(request, headers, runtime)

    def query_job_ranks_with_options(
        self,
        request: dingtalkhrm__1__0_models.QueryJobRanksRequest,
        headers: dingtalkhrm__1__0_models.QueryJobRanksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryJobRanksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.rank_category_id):
            query['rankCategoryId'] = request.rank_category_id
        if not UtilClient.is_unset(request.rank_code):
            query['rankCode'] = request.rank_code
        if not UtilClient.is_unset(request.rank_name):
            query['rankName'] = request.rank_name
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
            dingtalkhrm__1__0_models.QueryJobRanksResponse(),
            self.do_roarequest('QueryJobRanks', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/jobRanks', 'json', req, runtime)
        )

    async def query_job_ranks_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.QueryJobRanksRequest,
        headers: dingtalkhrm__1__0_models.QueryJobRanksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryJobRanksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.rank_category_id):
            query['rankCategoryId'] = request.rank_category_id
        if not UtilClient.is_unset(request.rank_code):
            query['rankCode'] = request.rank_code
        if not UtilClient.is_unset(request.rank_name):
            query['rankName'] = request.rank_name
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
            dingtalkhrm__1__0_models.QueryJobRanksResponse(),
            await self.do_roarequest_async('QueryJobRanks', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/jobRanks', 'json', req, runtime)
        )

    def query_jobs(
        self,
        request: dingtalkhrm__1__0_models.QueryJobsRequest,
    ) -> dingtalkhrm__1__0_models.QueryJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryJobsHeaders()
        return self.query_jobs_with_options(request, headers, runtime)

    async def query_jobs_async(
        self,
        request: dingtalkhrm__1__0_models.QueryJobsRequest,
    ) -> dingtalkhrm__1__0_models.QueryJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryJobsHeaders()
        return await self.query_jobs_with_options_async(request, headers, runtime)

    def query_jobs_with_options(
        self,
        request: dingtalkhrm__1__0_models.QueryJobsRequest,
        headers: dingtalkhrm__1__0_models.QueryJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_name):
            query['jobName'] = request.job_name
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
            dingtalkhrm__1__0_models.QueryJobsResponse(),
            self.do_roarequest('QueryJobs', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/jobs', 'json', req, runtime)
        )

    async def query_jobs_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.QueryJobsRequest,
        headers: dingtalkhrm__1__0_models.QueryJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_name):
            query['jobName'] = request.job_name
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
            dingtalkhrm__1__0_models.QueryJobsResponse(),
            await self.do_roarequest_async('QueryJobs', 'hrm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/hrm/jobs', 'json', req, runtime)
        )

    def query_positions(
        self,
        request: dingtalkhrm__1__0_models.QueryPositionsRequest,
    ) -> dingtalkhrm__1__0_models.QueryPositionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryPositionsHeaders()
        return self.query_positions_with_options(request, headers, runtime)

    async def query_positions_async(
        self,
        request: dingtalkhrm__1__0_models.QueryPositionsRequest,
    ) -> dingtalkhrm__1__0_models.QueryPositionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkhrm__1__0_models.QueryPositionsHeaders()
        return await self.query_positions_with_options_async(request, headers, runtime)

    def query_positions_with_options(
        self,
        request: dingtalkhrm__1__0_models.QueryPositionsRequest,
        headers: dingtalkhrm__1__0_models.QueryPositionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryPositionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.in_category_ids):
            body['inCategoryIds'] = request.in_category_ids
        if not UtilClient.is_unset(request.in_position_ids):
            body['inPositionIds'] = request.in_position_ids
        if not UtilClient.is_unset(request.position_name):
            body['positionName'] = request.position_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkhrm__1__0_models.QueryPositionsResponse(),
            self.do_roarequest('QueryPositions', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/positions/query', 'json', req, runtime)
        )

    async def query_positions_with_options_async(
        self,
        request: dingtalkhrm__1__0_models.QueryPositionsRequest,
        headers: dingtalkhrm__1__0_models.QueryPositionsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkhrm__1__0_models.QueryPositionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.in_category_ids):
            body['inCategoryIds'] = request.in_category_ids
        if not UtilClient.is_unset(request.in_position_ids):
            body['inPositionIds'] = request.in_position_ids
        if not UtilClient.is_unset(request.position_name):
            body['positionName'] = request.position_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkhrm__1__0_models.QueryPositionsResponse(),
            await self.do_roarequest_async('QueryPositions', 'hrm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/hrm/positions/query', 'json', req, runtime)
        )
