# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.industry_1_0 import models as dingtalkindustry__1__0_models
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

    def industry_manufacture_cost_record_list_get(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetHeaders()
        return self.industry_manufacture_cost_record_list_get_with_options(request, headers, runtime)

    async def industry_manufacture_cost_record_list_get_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetHeaders()
        return await self.industry_manufacture_cost_record_list_get_with_options_async(request, headers, runtime)

    def industry_manufacture_cost_record_list_get_with_options(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.production_task_no):
            body['productionTaskNo'] = request.production_task_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse(),
            self.do_roarequest('IndustryManufactureCostRecordListGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/materialCostRecords/query', 'json', req, runtime)
        )

    async def industry_manufacture_cost_record_list_get_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.order_no):
            body['orderNo'] = request.order_no
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.production_task_no):
            body['productionTaskNo'] = request.production_task_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureCostRecordListGetResponse(),
            await self.do_roarequest_async('IndustryManufactureCostRecordListGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/materialCostRecords/query', 'json', req, runtime)
        )

    def industry_manufacture_fee_list_get(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureFeeListGetHeaders()
        return self.industry_manufacture_fee_list_get_with_options(request, headers, runtime)

    async def industry_manufacture_fee_list_get_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureFeeListGetHeaders()
        return await self.industry_manufacture_fee_list_get_with_options_async(request, headers, runtime)

    def industry_manufacture_fee_list_get_with_options(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.production_task_no):
            body['productionTaskNo'] = request.production_task_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse(),
            self.do_roarequest('IndustryManufactureFeeListGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/fees/query', 'json', req, runtime)
        )

    async def industry_manufacture_fee_list_get_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureFeeListGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.production_task_no):
            body['productionTaskNo'] = request.production_task_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
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
            dingtalkindustry__1__0_models.IndustryManufactureFeeListGetResponse(),
            await self.do_roarequest_async('IndustryManufactureFeeListGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/fees/query', 'json', req, runtime)
        )

    def industry_manufacture_labour_cost(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureLabourCostRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureLabourCostHeaders()
        return self.industry_manufacture_labour_cost_with_options(request, headers, runtime)

    async def industry_manufacture_labour_cost_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureLabourCostRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureLabourCostHeaders()
        return await self.industry_manufacture_labour_cost_with_options_async(request, headers, runtime)

    def industry_manufacture_labour_cost_with_options(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureLabourCostRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureLabourCostHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_no):
            body['processNo'] = request.process_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse(),
            self.do_roarequest('IndustryManufactureLabourCost', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/labourCosts/query', 'json', req, runtime)
        )

    async def industry_manufacture_labour_cost_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureLabourCostRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureLabourCostHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_no):
            body['processNo'] = request.process_no
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureLabourCostResponse(),
            await self.do_roarequest_async('IndustryManufactureLabourCost', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/labourCosts/query', 'json', req, runtime)
        )

    def industry_manufacture_material_list(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureMaterialListRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureMaterialListHeaders()
        return self.industry_manufacture_material_list_with_options(request, headers, runtime)

    async def industry_manufacture_material_list_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureMaterialListRequest,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryManufactureMaterialListHeaders()
        return await self.industry_manufacture_material_list_with_options_async(request, headers, runtime)

    def industry_manufacture_material_list_with_options(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureMaterialListRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureMaterialListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse(),
            self.do_roarequest('IndustryManufactureMaterialList', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/materials/query', 'json', req, runtime)
        )

    async def industry_manufacture_material_list_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryManufactureMaterialListRequest,
        headers: dingtalkindustry__1__0_models.IndustryManufactureMaterialListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryManufactureMaterialListResponse(),
            await self.do_roarequest_async('IndustryManufactureMaterialList', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/materials/query', 'json', req, runtime)
        )

    def industry_mmanufacture_material_cost_get(
        self,
        request: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetHeaders()
        return self.industry_mmanufacture_material_cost_get_with_options(request, headers, runtime)

    async def industry_mmanufacture_material_cost_get_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetRequest,
    ) -> dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetHeaders()
        return await self.industry_mmanufacture_material_cost_get_with_options_async(request, headers, runtime)

    def industry_mmanufacture_material_cost_get_with_options(
        self,
        request: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse(),
            self.do_roarequest('IndustryMmanufactureMaterialCostGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/base/materialCosts/query', 'json', req, runtime)
        )

    async def industry_mmanufacture_material_cost_get_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetRequest,
        headers: dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.app_ids):
            body['appIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isv_org_id):
            body['isvOrgId'] = request.isv_org_id
        if not UtilClient.is_unset(request.material_no):
            body['materialNo'] = request.material_no
        if not UtilClient.is_unset(request.microapp_agent_id):
            body['microappAgentId'] = request.microapp_agent_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.suite_key):
            body['suiteKey'] = request.suite_key
        if not UtilClient.is_unset(request.token_grant_type):
            body['tokenGrantType'] = request.token_grant_type
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
            dingtalkindustry__1__0_models.IndustryMmanufactureMaterialCostGetResponse(),
            await self.do_roarequest_async('IndustryMmanufactureMaterialCostGet', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/manufactures/base/materialCosts/query', 'json', req, runtime)
        )

    def query_all_department(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDepartmentRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllDepartmentHeaders()
        return self.query_all_department_with_options(request, headers, runtime)

    async def query_all_department_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDepartmentRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllDepartmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllDepartmentHeaders()
        return await self.query_all_department_with_options_async(request, headers, runtime)

    def query_all_department_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDepartmentRequest,
        headers: dingtalkindustry__1__0_models.QueryAllDepartmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllDepartmentResponse:
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
            dingtalkindustry__1__0_models.QueryAllDepartmentResponse(),
            self.do_roarequest('QueryAllDepartment', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments', 'json', req, runtime)
        )

    async def query_all_department_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDepartmentRequest,
        headers: dingtalkindustry__1__0_models.QueryAllDepartmentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllDepartmentResponse:
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
            dingtalkindustry__1__0_models.QueryAllDepartmentResponse(),
            await self.do_roarequest_async('QueryAllDepartment', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments', 'json', req, runtime)
        )

    def query_all_doctors(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDoctorsRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllDoctorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllDoctorsHeaders()
        return self.query_all_doctors_with_options(request, headers, runtime)

    async def query_all_doctors_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDoctorsRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllDoctorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllDoctorsHeaders()
        return await self.query_all_doctors_with_options_async(request, headers, runtime)

    def query_all_doctors_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDoctorsRequest,
        headers: dingtalkindustry__1__0_models.QueryAllDoctorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllDoctorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
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
            dingtalkindustry__1__0_models.QueryAllDoctorsResponse(),
            self.do_roarequest('QueryAllDoctors', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/doctors', 'json', req, runtime)
        )

    async def query_all_doctors_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllDoctorsRequest,
        headers: dingtalkindustry__1__0_models.QueryAllDoctorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllDoctorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
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
            dingtalkindustry__1__0_models.QueryAllDoctorsResponse(),
            await self.do_roarequest_async('QueryAllDoctors', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/doctors', 'json', req, runtime)
        )

    def query_all_group(
        self,
        request: dingtalkindustry__1__0_models.QueryAllGroupRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllGroupHeaders()
        return self.query_all_group_with_options(request, headers, runtime)

    async def query_all_group_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllGroupRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllGroupHeaders()
        return await self.query_all_group_with_options_async(request, headers, runtime)

    def query_all_group_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryAllGroupRequest,
        headers: dingtalkindustry__1__0_models.QueryAllGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupResponse:
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
            dingtalkindustry__1__0_models.QueryAllGroupResponse(),
            self.do_roarequest('QueryAllGroup', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups', 'json', req, runtime)
        )

    async def query_all_group_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryAllGroupRequest,
        headers: dingtalkindustry__1__0_models.QueryAllGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupResponse:
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
            dingtalkindustry__1__0_models.QueryAllGroupResponse(),
            await self.do_roarequest_async('QueryAllGroup', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups', 'json', req, runtime)
        )

    def query_all_groups_in_dept(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllGroupsInDeptRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllGroupsInDeptHeaders()
        return self.query_all_groups_in_dept_with_options(dept_id, request, headers, runtime)

    async def query_all_groups_in_dept_async(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllGroupsInDeptRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllGroupsInDeptHeaders()
        return await self.query_all_groups_in_dept_with_options_async(dept_id, request, headers, runtime)

    def query_all_groups_in_dept_with_options(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllGroupsInDeptRequest,
        headers: dingtalkindustry__1__0_models.QueryAllGroupsInDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
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
            dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse(),
            self.do_roarequest('QueryAllGroupsInDept', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}/groups', 'json', req, runtime)
        )

    async def query_all_groups_in_dept_with_options_async(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllGroupsInDeptRequest,
        headers: dingtalkindustry__1__0_models.QueryAllGroupsInDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
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
            dingtalkindustry__1__0_models.QueryAllGroupsInDeptResponse(),
            await self.do_roarequest_async('QueryAllGroupsInDept', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}/groups', 'json', req, runtime)
        )

    def query_all_member_by_dept(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByDeptRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllMemberByDeptHeaders()
        return self.query_all_member_by_dept_with_options(dept_id, request, headers, runtime)

    async def query_all_member_by_dept_async(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByDeptRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllMemberByDeptHeaders()
        return await self.query_all_member_by_dept_with_options_async(dept_id, request, headers, runtime)

    def query_all_member_by_dept_with_options(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByDeptRequest,
        headers: dingtalkindustry__1__0_models.QueryAllMemberByDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
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
            dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse(),
            self.do_roarequest('QueryAllMemberByDept', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}/members', 'json', req, runtime)
        )

    async def query_all_member_by_dept_with_options_async(
        self,
        dept_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByDeptRequest,
        headers: dingtalkindustry__1__0_models.QueryAllMemberByDeptHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse:
        UtilClient.validate_model(request)
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
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
            dingtalkindustry__1__0_models.QueryAllMemberByDeptResponse(),
            await self.do_roarequest_async('QueryAllMemberByDept', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}/members', 'json', req, runtime)
        )

    def query_all_member_by_group(
        self,
        group_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByGroupRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllMemberByGroupHeaders()
        return self.query_all_member_by_group_with_options(group_id, request, headers, runtime)

    async def query_all_member_by_group_async(
        self,
        group_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByGroupRequest,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryAllMemberByGroupHeaders()
        return await self.query_all_member_by_group_with_options_async(group_id, request, headers, runtime)

    def query_all_member_by_group_with_options(
        self,
        group_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByGroupRequest,
        headers: dingtalkindustry__1__0_models.QueryAllMemberByGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse:
        UtilClient.validate_model(request)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
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
            dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse(),
            self.do_roarequest('QueryAllMemberByGroup', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups/{group_id}/members', 'json', req, runtime)
        )

    async def query_all_member_by_group_with_options_async(
        self,
        group_id: str,
        request: dingtalkindustry__1__0_models.QueryAllMemberByGroupRequest,
        headers: dingtalkindustry__1__0_models.QueryAllMemberByGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse:
        UtilClient.validate_model(request)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
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
            dingtalkindustry__1__0_models.QueryAllMemberByGroupResponse(),
            await self.do_roarequest_async('QueryAllMemberByGroup', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups/{group_id}/members', 'json', req, runtime)
        )

    def query_biz_opt_log(
        self,
        request: dingtalkindustry__1__0_models.QueryBizOptLogRequest,
    ) -> dingtalkindustry__1__0_models.QueryBizOptLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryBizOptLogHeaders()
        return self.query_biz_opt_log_with_options(request, headers, runtime)

    async def query_biz_opt_log_async(
        self,
        request: dingtalkindustry__1__0_models.QueryBizOptLogRequest,
    ) -> dingtalkindustry__1__0_models.QueryBizOptLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryBizOptLogHeaders()
        return await self.query_biz_opt_log_with_options_async(request, headers, runtime)

    def query_biz_opt_log_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryBizOptLogRequest,
        headers: dingtalkindustry__1__0_models.QueryBizOptLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryBizOptLogResponse:
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
            dingtalkindustry__1__0_models.QueryBizOptLogResponse(),
            self.do_roarequest('QueryBizOptLog', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/bizOptLogs', 'json', req, runtime)
        )

    async def query_biz_opt_log_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryBizOptLogRequest,
        headers: dingtalkindustry__1__0_models.QueryBizOptLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryBizOptLogResponse:
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
            dingtalkindustry__1__0_models.QueryBizOptLogResponse(),
            await self.do_roarequest_async('QueryBizOptLog', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/bizOptLogs', 'json', req, runtime)
        )

    def query_department_info(
        self,
        dept_id: str,
    ) -> dingtalkindustry__1__0_models.QueryDepartmentInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryDepartmentInfoHeaders()
        return self.query_department_info_with_options(dept_id, headers, runtime)

    async def query_department_info_async(
        self,
        dept_id: str,
    ) -> dingtalkindustry__1__0_models.QueryDepartmentInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryDepartmentInfoHeaders()
        return await self.query_department_info_with_options_async(dept_id, headers, runtime)

    def query_department_info_with_options(
        self,
        dept_id: str,
        headers: dingtalkindustry__1__0_models.QueryDepartmentInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryDepartmentInfoResponse:
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryDepartmentInfoResponse(),
            self.do_roarequest('QueryDepartmentInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}', 'json', req, runtime)
        )

    async def query_department_info_with_options_async(
        self,
        dept_id: str,
        headers: dingtalkindustry__1__0_models.QueryDepartmentInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryDepartmentInfoResponse:
        dept_id = OpenApiUtilClient.get_encode_param(dept_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryDepartmentInfoResponse(),
            await self.do_roarequest_async('QueryDepartmentInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/departments/{dept_id}', 'json', req, runtime)
        )

    def query_group_info(
        self,
        group_id: str,
    ) -> dingtalkindustry__1__0_models.QueryGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryGroupInfoHeaders()
        return self.query_group_info_with_options(group_id, headers, runtime)

    async def query_group_info_async(
        self,
        group_id: str,
    ) -> dingtalkindustry__1__0_models.QueryGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryGroupInfoHeaders()
        return await self.query_group_info_with_options_async(group_id, headers, runtime)

    def query_group_info_with_options(
        self,
        group_id: str,
        headers: dingtalkindustry__1__0_models.QueryGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryGroupInfoResponse:
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryGroupInfoResponse(),
            self.do_roarequest('QueryGroupInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups/{group_id}', 'json', req, runtime)
        )

    async def query_group_info_with_options_async(
        self,
        group_id: str,
        headers: dingtalkindustry__1__0_models.QueryGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryGroupInfoResponse:
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryGroupInfoResponse(),
            await self.do_roarequest_async('QueryGroupInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/groups/{group_id}', 'json', req, runtime)
        )

    def query_hospital_district_info(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoRequest,
    ) -> dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalDistrictInfoHeaders()
        return self.query_hospital_district_info_with_options(request, headers, runtime)

    async def query_hospital_district_info_async(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoRequest,
    ) -> dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalDistrictInfoHeaders()
        return await self.query_hospital_district_info_with_options_async(request, headers, runtime)

    def query_hospital_district_info_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoRequest,
        headers: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse:
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
            dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse(),
            self.do_roarequest('QueryHospitalDistrictInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/districts', 'json', req, runtime)
        )

    async def query_hospital_district_info_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoRequest,
        headers: dingtalkindustry__1__0_models.QueryHospitalDistrictInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse:
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
            dingtalkindustry__1__0_models.QueryHospitalDistrictInfoResponse(),
            await self.do_roarequest_async('QueryHospitalDistrictInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/districts', 'json', req, runtime)
        )

    def query_hospital_role_user_info(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoRequest,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoHeaders()
        return self.query_hospital_role_user_info_with_options(request, headers, runtime)

    async def query_hospital_role_user_info_async(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoRequest,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoHeaders()
        return await self.query_hospital_role_user_info_with_options_async(request, headers, runtime)

    def query_hospital_role_user_info_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoRequest,
        headers: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse:
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
            dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse(),
            self.do_roarequest('QueryHospitalRoleUserInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/roles/userInfos', 'json', req, runtime)
        )

    async def query_hospital_role_user_info_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoRequest,
        headers: dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse:
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
            dingtalkindustry__1__0_models.QueryHospitalRoleUserInfoResponse(),
            await self.do_roarequest_async('QueryHospitalRoleUserInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/roles/userInfos', 'json', req, runtime)
        )

    def query_hospital_roles(self) -> dingtalkindustry__1__0_models.QueryHospitalRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalRolesHeaders()
        return self.query_hospital_roles_with_options(headers, runtime)

    async def query_hospital_roles_async(self) -> dingtalkindustry__1__0_models.QueryHospitalRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryHospitalRolesHeaders()
        return await self.query_hospital_roles_with_options_async(headers, runtime)

    def query_hospital_roles_with_options(
        self,
        headers: dingtalkindustry__1__0_models.QueryHospitalRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryHospitalRolesResponse(),
            self.do_roarequest('QueryHospitalRoles', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/roles', 'json', req, runtime)
        )

    async def query_hospital_roles_with_options_async(
        self,
        headers: dingtalkindustry__1__0_models.QueryHospitalRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryHospitalRolesResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryHospitalRolesResponse(),
            await self.do_roarequest_async('QueryHospitalRoles', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/roles', 'json', req, runtime)
        )

    def query_job_code_dictionary(self) -> dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryJobCodeDictionaryHeaders()
        return self.query_job_code_dictionary_with_options(headers, runtime)

    async def query_job_code_dictionary_async(self) -> dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryJobCodeDictionaryHeaders()
        return await self.query_job_code_dictionary_with_options_async(headers, runtime)

    def query_job_code_dictionary_with_options(
        self,
        headers: dingtalkindustry__1__0_models.QueryJobCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse(),
            self.do_roarequest('QueryJobCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/jobCodes', 'json', req, runtime)
        )

    async def query_job_code_dictionary_with_options_async(
        self,
        headers: dingtalkindustry__1__0_models.QueryJobCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryJobCodeDictionaryResponse(),
            await self.do_roarequest_async('QueryJobCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/jobCodes', 'json', req, runtime)
        )

    def query_job_status_code_dictionary(self) -> dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryHeaders()
        return self.query_job_status_code_dictionary_with_options(headers, runtime)

    async def query_job_status_code_dictionary_async(self) -> dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryHeaders()
        return await self.query_job_status_code_dictionary_with_options_async(headers, runtime)

    def query_job_status_code_dictionary_with_options(
        self,
        headers: dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse(),
            self.do_roarequest('QueryJobStatusCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/jobStatusCodes', 'json', req, runtime)
        )

    async def query_job_status_code_dictionary_with_options_async(
        self,
        headers: dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryJobStatusCodeDictionaryResponse(),
            await self.do_roarequest_async('QueryJobStatusCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/jobStatusCodes', 'json', req, runtime)
        )

    def query_medical_events(self) -> dingtalkindustry__1__0_models.QueryMedicalEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryMedicalEventsHeaders()
        return self.query_medical_events_with_options(headers, runtime)

    async def query_medical_events_async(self) -> dingtalkindustry__1__0_models.QueryMedicalEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryMedicalEventsHeaders()
        return await self.query_medical_events_with_options_async(headers, runtime)

    def query_medical_events_with_options(
        self,
        headers: dingtalkindustry__1__0_models.QueryMedicalEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryMedicalEventsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryMedicalEventsResponse(),
            self.do_roarequest('QueryMedicalEvents', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/events', 'json', req, runtime)
        )

    async def query_medical_events_with_options_async(
        self,
        headers: dingtalkindustry__1__0_models.QueryMedicalEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryMedicalEventsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryMedicalEventsResponse(),
            await self.do_roarequest_async('QueryMedicalEvents', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/events', 'json', req, runtime)
        )

    def query_user_ext_info(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserExtInfoHeaders()
        return self.query_user_ext_info_with_options(user_id, headers, runtime)

    async def query_user_ext_info_async(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserExtInfoHeaders()
        return await self.query_user_ext_info_with_options_async(user_id, headers, runtime)

    def query_user_ext_info_with_options(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserExtInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserExtInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserExtInfoResponse(),
            self.do_roarequest('QueryUserExtInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extInfos', 'json', req, runtime)
        )

    async def query_user_ext_info_with_options_async(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserExtInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserExtInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserExtInfoResponse(),
            await self.do_roarequest_async('QueryUserExtInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extInfos', 'json', req, runtime)
        )

    def query_user_extend_values(
        self,
        request: dingtalkindustry__1__0_models.QueryUserExtendValuesRequest,
    ) -> dingtalkindustry__1__0_models.QueryUserExtendValuesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserExtendValuesHeaders()
        return self.query_user_extend_values_with_options(request, headers, runtime)

    async def query_user_extend_values_async(
        self,
        request: dingtalkindustry__1__0_models.QueryUserExtendValuesRequest,
    ) -> dingtalkindustry__1__0_models.QueryUserExtendValuesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserExtendValuesHeaders()
        return await self.query_user_extend_values_with_options_async(request, headers, runtime)

    def query_user_extend_values_with_options(
        self,
        request: dingtalkindustry__1__0_models.QueryUserExtendValuesRequest,
        headers: dingtalkindustry__1__0_models.QueryUserExtendValuesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserExtendValuesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_extend_key):
            body['userExtendKey'] = request.user_extend_key
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
            dingtalkindustry__1__0_models.QueryUserExtendValuesResponse(),
            self.do_roarequest('QueryUserExtendValues', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/medicals/users/extends/query', 'json', req, runtime)
        )

    async def query_user_extend_values_with_options_async(
        self,
        request: dingtalkindustry__1__0_models.QueryUserExtendValuesRequest,
        headers: dingtalkindustry__1__0_models.QueryUserExtendValuesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserExtendValuesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_extend_key):
            body['userExtendKey'] = request.user_extend_key
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
            dingtalkindustry__1__0_models.QueryUserExtendValuesResponse(),
            await self.do_roarequest_async('QueryUserExtendValues', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/medicals/users/extends/query', 'json', req, runtime)
        )

    def query_user_info(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserInfoHeaders()
        return self.query_user_info_with_options(user_id, headers, runtime)

    async def query_user_info_async(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserInfoHeaders()
        return await self.query_user_info_with_options_async(user_id, headers, runtime)

    def query_user_info_with_options(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserInfoResponse(),
            self.do_roarequest('QueryUserInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}', 'json', req, runtime)
        )

    async def query_user_info_with_options_async(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserInfoResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserInfoResponse(),
            await self.do_roarequest_async('QueryUserInfo', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}', 'json', req, runtime)
        )

    def query_user_prob_code_dictionary(self) -> dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryHeaders()
        return self.query_user_prob_code_dictionary_with_options(headers, runtime)

    async def query_user_prob_code_dictionary_async(self) -> dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryHeaders()
        return await self.query_user_prob_code_dictionary_with_options_async(headers, runtime)

    def query_user_prob_code_dictionary_with_options(
        self,
        headers: dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse(),
            self.do_roarequest('QueryUserProbCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/userProbCodes', 'json', req, runtime)
        )

    async def query_user_prob_code_dictionary_with_options_async(
        self,
        headers: dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserProbCodeDictionaryResponse(),
            await self.do_roarequest_async('QueryUserProbCodeDictionary', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/userProbCodes', 'json', req, runtime)
        )

    def query_user_roles(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserRolesHeaders()
        return self.query_user_roles_with_options(user_id, headers, runtime)

    async def query_user_roles_async(
        self,
        user_id: str,
    ) -> dingtalkindustry__1__0_models.QueryUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.QueryUserRolesHeaders()
        return await self.query_user_roles_with_options_async(user_id, headers, runtime)

    def query_user_roles_with_options(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserRolesResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserRolesResponse(),
            self.do_roarequest('QueryUserRoles', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}/roles', 'json', req, runtime)
        )

    async def query_user_roles_with_options_async(
        self,
        user_id: str,
        headers: dingtalkindustry__1__0_models.QueryUserRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.QueryUserRolesResponse:
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkindustry__1__0_models.QueryUserRolesResponse(),
            await self.do_roarequest_async('QueryUserRoles', 'industry_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/industry/medicals/users/{user_id}/roles', 'json', req, runtime)
        )

    def save_user_extend_values(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.SaveUserExtendValuesRequest,
    ) -> dingtalkindustry__1__0_models.SaveUserExtendValuesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders()
        return self.save_user_extend_values_with_options(user_id, request, headers, runtime)

    async def save_user_extend_values_async(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.SaveUserExtendValuesRequest,
    ) -> dingtalkindustry__1__0_models.SaveUserExtendValuesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders()
        return await self.save_user_extend_values_with_options_async(user_id, request, headers, runtime)

    def save_user_extend_values_with_options(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.SaveUserExtendValuesRequest,
        headers: dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.SaveUserExtendValuesResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.user_display_name):
            query['userDisplayName'] = request.user_display_name
        if not UtilClient.is_unset(request.user_extend_key):
            query['userExtendKey'] = request.user_extend_key
        if not UtilClient.is_unset(request.user_extend_value):
            query['userExtendValue'] = request.user_extend_value
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
            dingtalkindustry__1__0_models.SaveUserExtendValuesResponse(),
            self.do_roarequest('SaveUserExtendValues', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extends', 'json', req, runtime)
        )

    async def save_user_extend_values_with_options_async(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.SaveUserExtendValuesRequest,
        headers: dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.SaveUserExtendValuesResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        query = {}
        if not UtilClient.is_unset(request.user_display_name):
            query['userDisplayName'] = request.user_display_name
        if not UtilClient.is_unset(request.user_extend_key):
            query['userExtendKey'] = request.user_extend_key
        if not UtilClient.is_unset(request.user_extend_value):
            query['userExtendValue'] = request.user_extend_value
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
            dingtalkindustry__1__0_models.SaveUserExtendValuesResponse(),
            await self.do_roarequest_async('SaveUserExtendValues', 'industry_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extends', 'json', req, runtime)
        )

    def update_user_extend_info(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.UpdateUserExtendInfoRequest,
    ) -> dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.UpdateUserExtendInfoHeaders()
        return self.update_user_extend_info_with_options(user_id, request, headers, runtime)

    async def update_user_extend_info_async(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.UpdateUserExtendInfoRequest,
    ) -> dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkindustry__1__0_models.UpdateUserExtendInfoHeaders()
        return await self.update_user_extend_info_with_options_async(user_id, request, headers, runtime)

    def update_user_extend_info_with_options(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.UpdateUserExtendInfoRequest,
        headers: dingtalkindustry__1__0_models.UpdateUserExtendInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        body = {}
        if not UtilClient.is_unset(request.comments):
            body['comments'] = request.comments
        if not UtilClient.is_unset(request.job_code):
            body['jobCode'] = request.job_code
        if not UtilClient.is_unset(request.job_status_code):
            body['jobStatusCode'] = request.job_status_code
        if not UtilClient.is_unset(request.user_prob_code):
            body['userProbCode'] = request.user_prob_code
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
            dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse(),
            self.do_roarequest('UpdateUserExtendInfo', 'industry_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extInfos', 'none', req, runtime)
        )

    async def update_user_extend_info_with_options_async(
        self,
        user_id: str,
        request: dingtalkindustry__1__0_models.UpdateUserExtendInfoRequest,
        headers: dingtalkindustry__1__0_models.UpdateUserExtendInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse:
        UtilClient.validate_model(request)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        body = {}
        if not UtilClient.is_unset(request.comments):
            body['comments'] = request.comments
        if not UtilClient.is_unset(request.job_code):
            body['jobCode'] = request.job_code
        if not UtilClient.is_unset(request.job_status_code):
            body['jobStatusCode'] = request.job_status_code
        if not UtilClient.is_unset(request.user_prob_code):
            body['userProbCode'] = request.user_prob_code
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
            dingtalkindustry__1__0_models.UpdateUserExtendInfoResponse(),
            await self.do_roarequest_async('UpdateUserExtendInfo', 'industry_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/industry/medicals/users/{user_id}/extInfos', 'none', req, runtime)
        )
