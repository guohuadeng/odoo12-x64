# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
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

    def abandon_customer(
        self,
        request: dingtalkcrm__1__0_models.AbandonCustomerRequest,
    ) -> dingtalkcrm__1__0_models.AbandonCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AbandonCustomerHeaders()
        return self.abandon_customer_with_options(request, headers, runtime)

    async def abandon_customer_async(
        self,
        request: dingtalkcrm__1__0_models.AbandonCustomerRequest,
    ) -> dingtalkcrm__1__0_models.AbandonCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AbandonCustomerHeaders()
        return await self.abandon_customer_with_options_async(request, headers, runtime)

    def abandon_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.AbandonCustomerRequest,
        headers: dingtalkcrm__1__0_models.AbandonCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AbandonCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_track_desc):
            body['customTrackDesc'] = request.custom_track_desc
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.opt_type):
            body['optType'] = request.opt_type
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
            dingtalkcrm__1__0_models.AbandonCustomerResponse(),
            self.do_roarequest('AbandonCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customers/abandon', 'json', req, runtime)
        )

    async def abandon_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.AbandonCustomerRequest,
        headers: dingtalkcrm__1__0_models.AbandonCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AbandonCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_track_desc):
            body['customTrackDesc'] = request.custom_track_desc
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.opt_type):
            body['optType'] = request.opt_type
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
            dingtalkcrm__1__0_models.AbandonCustomerResponse(),
            await self.do_roarequest_async('AbandonCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customers/abandon', 'json', req, runtime)
        )

    def add_crm_personal_customer(
        self,
        request: dingtalkcrm__1__0_models.AddCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddCrmPersonalCustomerHeaders()
        return self.add_crm_personal_customer_with_options(request, headers, runtime)

    async def add_crm_personal_customer_async(
        self,
        request: dingtalkcrm__1__0_models.AddCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddCrmPersonalCustomerHeaders()
        return await self.add_crm_personal_customer_with_options_async(request, headers, runtime)

    def add_crm_personal_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.AddCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.AddCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.creator_nick):
            body['creatorNick'] = request.creator_nick
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse(),
            self.do_roarequest('AddCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    async def add_crm_personal_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.AddCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.AddCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.creator_nick):
            body['creatorNick'] = request.creator_nick
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.AddCrmPersonalCustomerResponse(),
            await self.do_roarequest_async('AddCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    def add_customer_track(
        self,
        request: dingtalkcrm__1__0_models.AddCustomerTrackRequest,
    ) -> dingtalkcrm__1__0_models.AddCustomerTrackResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddCustomerTrackHeaders()
        return self.add_customer_track_with_options(request, headers, runtime)

    async def add_customer_track_async(
        self,
        request: dingtalkcrm__1__0_models.AddCustomerTrackRequest,
    ) -> dingtalkcrm__1__0_models.AddCustomerTrackResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddCustomerTrackHeaders()
        return await self.add_customer_track_with_options_async(request, headers, runtime)

    def add_customer_track_with_options(
        self,
        request: dingtalkcrm__1__0_models.AddCustomerTrackRequest,
        headers: dingtalkcrm__1__0_models.AddCustomerTrackHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddCustomerTrackResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.customer_id):
            body['customerId'] = request.customer_id
        if not UtilClient.is_unset(request.extra_biz_info):
            body['extraBizInfo'] = request.extra_biz_info
        if not UtilClient.is_unset(request.idempotent_key):
            body['idempotentKey'] = request.idempotent_key
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
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
            dingtalkcrm__1__0_models.AddCustomerTrackResponse(),
            self.do_roarequest('AddCustomerTrack', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customerTracks', 'json', req, runtime)
        )

    async def add_customer_track_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.AddCustomerTrackRequest,
        headers: dingtalkcrm__1__0_models.AddCustomerTrackHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddCustomerTrackResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.customer_id):
            body['customerId'] = request.customer_id
        if not UtilClient.is_unset(request.extra_biz_info):
            body['extraBizInfo'] = request.extra_biz_info
        if not UtilClient.is_unset(request.idempotent_key):
            body['idempotentKey'] = request.idempotent_key
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
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
            dingtalkcrm__1__0_models.AddCustomerTrackResponse(),
            await self.do_roarequest_async('AddCustomerTrack', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customerTracks', 'json', req, runtime)
        )

    def add_relation_meta_field(
        self,
        request: dingtalkcrm__1__0_models.AddRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.AddRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddRelationMetaFieldHeaders()
        return self.add_relation_meta_field_with_options(request, headers, runtime)

    async def add_relation_meta_field_async(
        self,
        request: dingtalkcrm__1__0_models.AddRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.AddRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.AddRelationMetaFieldHeaders()
        return await self.add_relation_meta_field_with_options_async(request, headers, runtime)

    def add_relation_meta_field_with_options(
        self,
        request: dingtalkcrm__1__0_models.AddRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.AddRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_dtolist):
            body['fieldDTOList'] = request.field_dtolist
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.AddRelationMetaFieldResponse(),
            self.do_roarequest('AddRelationMetaField', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/fields', 'json', req, runtime)
        )

    async def add_relation_meta_field_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.AddRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.AddRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.AddRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_dtolist):
            body['fieldDTOList'] = request.field_dtolist
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.AddRelationMetaFieldResponse(),
            await self.do_roarequest_async('AddRelationMetaField', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/fields', 'json', req, runtime)
        )

    def batch_add_relation_datas(
        self,
        request: dingtalkcrm__1__0_models.BatchAddRelationDatasRequest,
    ) -> dingtalkcrm__1__0_models.BatchAddRelationDatasResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchAddRelationDatasHeaders()
        return self.batch_add_relation_datas_with_options(request, headers, runtime)

    async def batch_add_relation_datas_async(
        self,
        request: dingtalkcrm__1__0_models.BatchAddRelationDatasRequest,
    ) -> dingtalkcrm__1__0_models.BatchAddRelationDatasResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchAddRelationDatasHeaders()
        return await self.batch_add_relation_datas_with_options_async(request, headers, runtime)

    def batch_add_relation_datas_with_options(
        self,
        request: dingtalkcrm__1__0_models.BatchAddRelationDatasRequest,
        headers: dingtalkcrm__1__0_models.BatchAddRelationDatasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchAddRelationDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_list):
            body['relationList'] = request.relation_list
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.BatchAddRelationDatasResponse(),
            self.do_roarequest('BatchAddRelationDatas', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relationDatas/batch', 'json', req, runtime)
        )

    async def batch_add_relation_datas_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.BatchAddRelationDatasRequest,
        headers: dingtalkcrm__1__0_models.BatchAddRelationDatasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchAddRelationDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_list):
            body['relationList'] = request.relation_list
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.BatchAddRelationDatasResponse(),
            await self.do_roarequest_async('BatchAddRelationDatas', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relationDatas/batch', 'json', req, runtime)
        )

    def batch_send_official_account_otomessage(
        self,
        request: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders()
        return self.batch_send_official_account_otomessage_with_options(request, headers, runtime)

    async def batch_send_official_account_otomessage_async(
        self,
        request: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders()
        return await self.batch_send_official_account_otomessage_with_options_async(request, headers, runtime)

    def batch_send_official_account_otomessage_with_options(
        self,
        request: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse(),
            self.do_roarequest('BatchSendOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/batchSend', 'json', req, runtime)
        )

    async def batch_send_official_account_otomessage_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageResponse(),
            await self.do_roarequest_async('BatchSendOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/batchSend', 'json', req, runtime)
        )

    def batch_update_relation_datas(
        self,
        request: dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest,
    ) -> dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders()
        return self.batch_update_relation_datas_with_options(request, headers, runtime)

    async def batch_update_relation_datas_async(
        self,
        request: dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest,
    ) -> dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders()
        return await self.batch_update_relation_datas_with_options_async(request, headers, runtime)

    def batch_update_relation_datas_with_options(
        self,
        request: dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest,
        headers: dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_list):
            body['relationList'] = request.relation_list
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse(),
            self.do_roarequest('BatchUpdateRelationDatas', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/relationDatas/batch', 'json', req, runtime)
        )

    async def batch_update_relation_datas_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest,
        headers: dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_list):
            body['relationList'] = request.relation_list
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.BatchUpdateRelationDatasResponse(),
            await self.do_roarequest_async('BatchUpdateRelationDatas', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/relationDatas/batch', 'json', req, runtime)
        )

    def create_customer(
        self,
        request: dingtalkcrm__1__0_models.CreateCustomerRequest,
    ) -> dingtalkcrm__1__0_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateCustomerHeaders()
        return self.create_customer_with_options(request, headers, runtime)

    async def create_customer_async(
        self,
        request: dingtalkcrm__1__0_models.CreateCustomerRequest,
    ) -> dingtalkcrm__1__0_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateCustomerHeaders()
        return await self.create_customer_with_options_async(request, headers, runtime)

    def create_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.CreateCustomerRequest,
        headers: dingtalkcrm__1__0_models.CreateCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contacts):
            body['contacts'] = request.contacts
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.save_option):
            body['saveOption'] = request.save_option
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
            dingtalkcrm__1__0_models.CreateCustomerResponse(),
            self.do_roarequest('CreateCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customers', 'json', req, runtime)
        )

    async def create_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.CreateCustomerRequest,
        headers: dingtalkcrm__1__0_models.CreateCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contacts):
            body['contacts'] = request.contacts
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.save_option):
            body['saveOption'] = request.save_option
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
            dingtalkcrm__1__0_models.CreateCustomerResponse(),
            await self.do_roarequest_async('CreateCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customers', 'json', req, runtime)
        )

    def create_group(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupRequest,
    ) -> dingtalkcrm__1__0_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateGroupHeaders()
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupRequest,
    ) -> dingtalkcrm__1__0_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateGroupHeaders()
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupRequest,
        headers: dingtalkcrm__1__0_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.member_user_ids):
            body['memberUserIds'] = request.member_user_ids
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.CreateGroupResponse(),
            self.do_roarequest('CreateGroup', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groups', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupRequest,
        headers: dingtalkcrm__1__0_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.member_user_ids):
            body['memberUserIds'] = request.member_user_ids
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.CreateGroupResponse(),
            await self.do_roarequest_async('CreateGroup', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groups', 'json', req, runtime)
        )

    def create_group_set(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.CreateGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateGroupSetHeaders()
        return self.create_group_set_with_options(request, headers, runtime)

    async def create_group_set_async(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.CreateGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateGroupSetHeaders()
        return await self.create_group_set_with_options_async(request, headers, runtime)

    def create_group_set_with_options(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupSetRequest,
        headers: dingtalkcrm__1__0_models.CreateGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.manager_user_ids):
            body['managerUserIds'] = request.manager_user_ids
        if not UtilClient.is_unset(request.member_quota):
            body['memberQuota'] = request.member_quota
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notice):
            body['notice'] = request.notice
        if not UtilClient.is_unset(request.notice_toped):
            body['noticeToped'] = request.notice_toped
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
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
            dingtalkcrm__1__0_models.CreateGroupSetResponse(),
            self.do_roarequest('CreateGroupSet', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groupSets', 'json', req, runtime)
        )

    async def create_group_set_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.CreateGroupSetRequest,
        headers: dingtalkcrm__1__0_models.CreateGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator_user_id):
            body['creatorUserId'] = request.creator_user_id
        if not UtilClient.is_unset(request.manager_user_ids):
            body['managerUserIds'] = request.manager_user_ids
        if not UtilClient.is_unset(request.member_quota):
            body['memberQuota'] = request.member_quota
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notice):
            body['notice'] = request.notice
        if not UtilClient.is_unset(request.notice_toped):
            body['noticeToped'] = request.notice_toped
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
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
            dingtalkcrm__1__0_models.CreateGroupSetResponse(),
            await self.do_roarequest_async('CreateGroupSet', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groupSets', 'json', req, runtime)
        )

    def create_relation_meta(
        self,
        request: dingtalkcrm__1__0_models.CreateRelationMetaRequest,
    ) -> dingtalkcrm__1__0_models.CreateRelationMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateRelationMetaHeaders()
        return self.create_relation_meta_with_options(request, headers, runtime)

    async def create_relation_meta_async(
        self,
        request: dingtalkcrm__1__0_models.CreateRelationMetaRequest,
    ) -> dingtalkcrm__1__0_models.CreateRelationMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.CreateRelationMetaHeaders()
        return await self.create_relation_meta_with_options_async(request, headers, runtime)

    def create_relation_meta_with_options(
        self,
        request: dingtalkcrm__1__0_models.CreateRelationMetaRequest,
        headers: dingtalkcrm__1__0_models.CreateRelationMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateRelationMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_meta_dto):
            body['relationMetaDTO'] = request.relation_meta_dto
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.CreateRelationMetaResponse(),
            self.do_roarequest('CreateRelationMeta', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/create', 'json', req, runtime)
        )

    async def create_relation_meta_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.CreateRelationMetaRequest,
        headers: dingtalkcrm__1__0_models.CreateRelationMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.CreateRelationMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_meta_dto):
            body['relationMetaDTO'] = request.relation_meta_dto
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.CreateRelationMetaResponse(),
            await self.do_roarequest_async('CreateRelationMeta', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/create', 'json', req, runtime)
        )

    def delete_crm_form_instance(
        self,
        instance_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmFormInstanceRequest,
    ) -> dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteCrmFormInstanceHeaders()
        return self.delete_crm_form_instance_with_options(instance_id, request, headers, runtime)

    async def delete_crm_form_instance_async(
        self,
        instance_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmFormInstanceRequest,
    ) -> dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteCrmFormInstanceHeaders()
        return await self.delete_crm_form_instance_with_options_async(instance_id, request, headers, runtime)

    def delete_crm_form_instance_with_options(
        self,
        instance_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmFormInstanceRequest,
        headers: dingtalkcrm__1__0_models.DeleteCrmFormInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
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
            dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse(),
            self.do_roarequest('DeleteCrmFormInstance', 'crm_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/crm/formInstances/{instance_id}', 'json', req, runtime)
        )

    async def delete_crm_form_instance_with_options_async(
        self,
        instance_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmFormInstanceRequest,
        headers: dingtalkcrm__1__0_models.DeleteCrmFormInstanceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
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
            dingtalkcrm__1__0_models.DeleteCrmFormInstanceResponse(),
            await self.do_roarequest_async('DeleteCrmFormInstance', 'crm_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/crm/formInstances/{instance_id}', 'json', req, runtime)
        )

    def delete_crm_personal_customer(
        self,
        data_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerHeaders()
        return self.delete_crm_personal_customer_with_options(data_id, request, headers, runtime)

    async def delete_crm_personal_customer_async(
        self,
        data_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerHeaders()
        return await self.delete_crm_personal_customer_with_options_async(data_id, request, headers, runtime)

    def delete_crm_personal_customer_with_options(
        self,
        data_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
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
            dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse(),
            self.do_roarequest('DeleteCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/crm/personalCustomers/{data_id}', 'json', req, runtime)
        )

    async def delete_crm_personal_customer_with_options_async(
        self,
        data_id: str,
        request: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
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
            dingtalkcrm__1__0_models.DeleteCrmPersonalCustomerResponse(),
            await self.do_roarequest_async('DeleteCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/crm/personalCustomers/{data_id}', 'json', req, runtime)
        )

    def delete_relation_meta_field(
        self,
        request: dingtalkcrm__1__0_models.DeleteRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteRelationMetaFieldHeaders()
        return self.delete_relation_meta_field_with_options(request, headers, runtime)

    async def delete_relation_meta_field_async(
        self,
        request: dingtalkcrm__1__0_models.DeleteRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DeleteRelationMetaFieldHeaders()
        return await self.delete_relation_meta_field_with_options_async(request, headers, runtime)

    def delete_relation_meta_field_with_options(
        self,
        request: dingtalkcrm__1__0_models.DeleteRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.DeleteRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_id_list):
            body['fieldIdList'] = request.field_id_list
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse(),
            self.do_roarequest('DeleteRelationMetaField', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/fields/remove', 'json', req, runtime)
        )

    async def delete_relation_meta_field_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.DeleteRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.DeleteRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_id_list):
            body['fieldIdList'] = request.field_id_list
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.DeleteRelationMetaFieldResponse(),
            await self.do_roarequest_async('DeleteRelationMetaField', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/fields/remove', 'json', req, runtime)
        )

    def describe_crm_personal_customer_object_meta(self) -> dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders()
        return self.describe_crm_personal_customer_object_meta_with_options(headers, runtime)

    async def describe_crm_personal_customer_object_meta_async(self) -> dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders()
        return await self.describe_crm_personal_customer_object_meta_with_options_async(headers, runtime)

    def describe_crm_personal_customer_object_meta_with_options(
        self,
        headers: dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse(),
            self.do_roarequest('DescribeCrmPersonalCustomerObjectMeta', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/personalCustomers/objectMeta', 'json', req, runtime)
        )

    async def describe_crm_personal_customer_object_meta_with_options_async(
        self,
        headers: dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaResponse(),
            await self.do_roarequest_async('DescribeCrmPersonalCustomerObjectMeta', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/personalCustomers/objectMeta', 'json', req, runtime)
        )

    def describe_relation_meta(
        self,
        request: dingtalkcrm__1__0_models.DescribeRelationMetaRequest,
    ) -> dingtalkcrm__1__0_models.DescribeRelationMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DescribeRelationMetaHeaders()
        return self.describe_relation_meta_with_options(request, headers, runtime)

    async def describe_relation_meta_async(
        self,
        request: dingtalkcrm__1__0_models.DescribeRelationMetaRequest,
    ) -> dingtalkcrm__1__0_models.DescribeRelationMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.DescribeRelationMetaHeaders()
        return await self.describe_relation_meta_with_options_async(request, headers, runtime)

    def describe_relation_meta_with_options(
        self,
        request: dingtalkcrm__1__0_models.DescribeRelationMetaRequest,
        headers: dingtalkcrm__1__0_models.DescribeRelationMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DescribeRelationMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_types):
            body['relationTypes'] = request.relation_types
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.DescribeRelationMetaResponse(),
            self.do_roarequest('DescribeRelationMeta', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/query', 'json', req, runtime)
        )

    async def describe_relation_meta_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.DescribeRelationMetaRequest,
        headers: dingtalkcrm__1__0_models.DescribeRelationMetaHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.DescribeRelationMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_types):
            body['relationTypes'] = request.relation_types
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.DescribeRelationMetaResponse(),
            await self.do_roarequest_async('DescribeRelationMeta', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/relations/metas/query', 'json', req, runtime)
        )

    def get_crm_group_chat(
        self,
        open_conversation_id: str,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatHeaders()
        return self.get_crm_group_chat_with_options(open_conversation_id, headers, runtime)

    async def get_crm_group_chat_async(
        self,
        open_conversation_id: str,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatHeaders()
        return await self.get_crm_group_chat_with_options_async(open_conversation_id, headers, runtime)

    def get_crm_group_chat_with_options(
        self,
        open_conversation_id: str,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatResponse:
        open_conversation_id = OpenApiUtilClient.get_encode_param(open_conversation_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.GetCrmGroupChatResponse(),
            self.do_roarequest('GetCrmGroupChat', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/crmGroupChats/{open_conversation_id}', 'json', req, runtime)
        )

    async def get_crm_group_chat_with_options_async(
        self,
        open_conversation_id: str,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatResponse:
        open_conversation_id = OpenApiUtilClient.get_encode_param(open_conversation_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.GetCrmGroupChatResponse(),
            await self.do_roarequest_async('GetCrmGroupChat', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/crmGroupChats/{open_conversation_id}', 'json', req, runtime)
        )

    def get_crm_group_chat_multi(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatMultiRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatMultiHeaders()
        return self.get_crm_group_chat_multi_with_options(request, headers, runtime)

    async def get_crm_group_chat_multi_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatMultiRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatMultiHeaders()
        return await self.get_crm_group_chat_multi_with_options_async(request, headers, runtime)

    def get_crm_group_chat_multi_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatMultiRequest,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatMultiHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_ids):
            body['openConversationIds'] = request.open_conversation_ids
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
            dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse(),
            self.do_roarequest('GetCrmGroupChatMulti', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/crmGroupChats/batchQuery', 'json', req, runtime)
        )

    async def get_crm_group_chat_multi_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatMultiRequest,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatMultiHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_conversation_ids):
            body['openConversationIds'] = request.open_conversation_ids
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
            dingtalkcrm__1__0_models.GetCrmGroupChatMultiResponse(),
            await self.do_roarequest_async('GetCrmGroupChatMulti', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/crmGroupChats/batchQuery', 'json', req, runtime)
        )

    def get_crm_group_chat_single(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders()
        return self.get_crm_group_chat_single_with_options(request, headers, runtime)

    async def get_crm_group_chat_single_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders()
        return await self.get_crm_group_chat_single_with_options_async(request, headers, runtime)

    def get_crm_group_chat_single_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            query['openConversationId'] = request.open_conversation_id
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
            dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse(),
            self.do_roarequest('GetCrmGroupChatSingle', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/crmGroupChats/query', 'json', req, runtime)
        )

    async def get_crm_group_chat_single_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest,
        headers: dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            query['openConversationId'] = request.open_conversation_id
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
            dingtalkcrm__1__0_models.GetCrmGroupChatSingleResponse(),
            await self.do_roarequest_async('GetCrmGroupChatSingle', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/crmGroupChats/query', 'json', req, runtime)
        )

    def get_crm_role_permission(
        self,
        request: dingtalkcrm__1__0_models.GetCrmRolePermissionRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmRolePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmRolePermissionHeaders()
        return self.get_crm_role_permission_with_options(request, headers, runtime)

    async def get_crm_role_permission_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmRolePermissionRequest,
    ) -> dingtalkcrm__1__0_models.GetCrmRolePermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCrmRolePermissionHeaders()
        return await self.get_crm_role_permission_with_options_async(request, headers, runtime)

    def get_crm_role_permission_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetCrmRolePermissionRequest,
        headers: dingtalkcrm__1__0_models.GetCrmRolePermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmRolePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.form_code):
            query['formCode'] = request.form_code
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
            dingtalkcrm__1__0_models.GetCrmRolePermissionResponse(),
            self.do_roarequest('GetCrmRolePermission', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/permissions', 'json', req, runtime)
        )

    async def get_crm_role_permission_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetCrmRolePermissionRequest,
        headers: dingtalkcrm__1__0_models.GetCrmRolePermissionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCrmRolePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.form_code):
            query['formCode'] = request.form_code
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
            dingtalkcrm__1__0_models.GetCrmRolePermissionResponse(),
            await self.do_roarequest_async('GetCrmRolePermission', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/permissions', 'json', req, runtime)
        )

    def get_customer_tracks_by_relation_id(
        self,
        request: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdRequest,
    ) -> dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdHeaders()
        return self.get_customer_tracks_by_relation_id_with_options(request, headers, runtime)

    async def get_customer_tracks_by_relation_id_async(
        self,
        request: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdRequest,
    ) -> dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdHeaders()
        return await self.get_customer_tracks_by_relation_id_with_options_async(request, headers, runtime)

    def get_customer_tracks_by_relation_id_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdRequest,
        headers: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.relation_id):
            query['relationId'] = request.relation_id
        if not UtilClient.is_unset(request.type_group):
            query['typeGroup'] = request.type_group
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
            dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse(),
            self.do_roarequest('GetCustomerTracksByRelationId', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/customerTracks', 'json', req, runtime)
        )

    async def get_customer_tracks_by_relation_id_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdRequest,
        headers: dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.relation_id):
            query['relationId'] = request.relation_id
        if not UtilClient.is_unset(request.type_group):
            query['typeGroup'] = request.type_group
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
            dingtalkcrm__1__0_models.GetCustomerTracksByRelationIdResponse(),
            await self.do_roarequest_async('GetCustomerTracksByRelationId', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/customerTracks', 'json', req, runtime)
        )

    def get_group_set(
        self,
        request: dingtalkcrm__1__0_models.GetGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.GetGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetGroupSetHeaders()
        return self.get_group_set_with_options(request, headers, runtime)

    async def get_group_set_async(
        self,
        request: dingtalkcrm__1__0_models.GetGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.GetGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetGroupSetHeaders()
        return await self.get_group_set_with_options_async(request, headers, runtime)

    def get_group_set_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetGroupSetRequest,
        headers: dingtalkcrm__1__0_models.GetGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetGroupSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_set_id):
            query['openGroupSetId'] = request.open_group_set_id
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
            dingtalkcrm__1__0_models.GetGroupSetResponse(),
            self.do_roarequest('GetGroupSet', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/groupSets', 'json', req, runtime)
        )

    async def get_group_set_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetGroupSetRequest,
        headers: dingtalkcrm__1__0_models.GetGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetGroupSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_set_id):
            query['openGroupSetId'] = request.open_group_set_id
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
            dingtalkcrm__1__0_models.GetGroupSetResponse(),
            await self.do_roarequest_async('GetGroupSet', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/groupSets', 'json', req, runtime)
        )

    def get_official_account_contact_info(
        self,
        user_id: str,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders()
        return self.get_official_account_contact_info_with_options(user_id, headers, runtime)

    async def get_official_account_contact_info_async(
        self,
        user_id: str,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders()
        return await self.get_official_account_contact_info_with_options_async(user_id, headers, runtime)

    def get_official_account_contact_info_with_options(
        self,
        user_id: str,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse:
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
            dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse(),
            self.do_roarequest('GetOfficialAccountContactInfo', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/contacts/{user_id}', 'json', req, runtime)
        )

    async def get_official_account_contact_info_with_options_async(
        self,
        user_id: str,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse:
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
            dingtalkcrm__1__0_models.GetOfficialAccountContactInfoResponse(),
            await self.do_roarequest_async('GetOfficialAccountContactInfo', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/contacts/{user_id}', 'json', req, runtime)
        )

    def get_official_account_contacts(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders()
        return self.get_official_account_contacts_with_options(request, headers, runtime)

    async def get_official_account_contacts_async(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders()
        return await self.get_official_account_contacts_with_options_async(request, headers, runtime)

    def get_official_account_contacts_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse:
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
            dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse(),
            self.do_roarequest('GetOfficialAccountContacts', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/contacts', 'json', req, runtime)
        )

    async def get_official_account_contacts_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse:
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
            dingtalkcrm__1__0_models.GetOfficialAccountContactsResponse(),
            await self.do_roarequest_async('GetOfficialAccountContacts', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/contacts', 'json', req, runtime)
        )

    def get_official_account_otomessage_result(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultRequest,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultHeaders()
        return self.get_official_account_otomessage_result_with_options(request, headers, runtime)

    async def get_official_account_otomessage_result_async(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultRequest,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultHeaders()
        return await self.get_official_account_otomessage_result_with_options_async(request, headers, runtime)

    def get_official_account_otomessage_result_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultRequest,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.open_push_id):
            query['openPushId'] = request.open_push_id
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
            dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse(),
            self.do_roarequest('GetOfficialAccountOTOMessageResult', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/sendResults', 'json', req, runtime)
        )

    async def get_official_account_otomessage_result_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultRequest,
        headers: dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.open_push_id):
            query['openPushId'] = request.open_push_id
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
            dingtalkcrm__1__0_models.GetOfficialAccountOTOMessageResultResponse(),
            await self.do_roarequest_async('GetOfficialAccountOTOMessageResult', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/sendResults', 'json', req, runtime)
        )

    def get_relation_uk_setting(
        self,
        request: dingtalkcrm__1__0_models.GetRelationUkSettingRequest,
    ) -> dingtalkcrm__1__0_models.GetRelationUkSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetRelationUkSettingHeaders()
        return self.get_relation_uk_setting_with_options(request, headers, runtime)

    async def get_relation_uk_setting_async(
        self,
        request: dingtalkcrm__1__0_models.GetRelationUkSettingRequest,
    ) -> dingtalkcrm__1__0_models.GetRelationUkSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.GetRelationUkSettingHeaders()
        return await self.get_relation_uk_setting_with_options_async(request, headers, runtime)

    def get_relation_uk_setting_with_options(
        self,
        request: dingtalkcrm__1__0_models.GetRelationUkSettingRequest,
        headers: dingtalkcrm__1__0_models.GetRelationUkSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetRelationUkSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.GetRelationUkSettingResponse(),
            self.do_roarequest('GetRelationUkSetting', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/relationUkSettings', 'json', req, runtime)
        )

    async def get_relation_uk_setting_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.GetRelationUkSettingRequest,
        headers: dingtalkcrm__1__0_models.GetRelationUkSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.GetRelationUkSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.GetRelationUkSettingResponse(),
            await self.do_roarequest_async('GetRelationUkSetting', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/relationUkSettings', 'json', req, runtime)
        )

    def join_group_set(
        self,
        request: dingtalkcrm__1__0_models.JoinGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.JoinGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.JoinGroupSetHeaders()
        return self.join_group_set_with_options(request, headers, runtime)

    async def join_group_set_async(
        self,
        request: dingtalkcrm__1__0_models.JoinGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.JoinGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.JoinGroupSetHeaders()
        return await self.join_group_set_with_options_async(request, headers, runtime)

    def join_group_set_with_options(
        self,
        request: dingtalkcrm__1__0_models.JoinGroupSetRequest,
        headers: dingtalkcrm__1__0_models.JoinGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.JoinGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_data_list):
            body['bizDataList'] = request.biz_data_list
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.open_group_set_id):
            body['openGroupSetId'] = request.open_group_set_id
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkcrm__1__0_models.JoinGroupSetResponse(),
            self.do_roarequest('JoinGroupSet', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groupSets/join', 'json', req, runtime)
        )

    async def join_group_set_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.JoinGroupSetRequest,
        headers: dingtalkcrm__1__0_models.JoinGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.JoinGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_data_list):
            body['bizDataList'] = request.biz_data_list
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.open_group_set_id):
            body['openGroupSetId'] = request.open_group_set_id
        if not UtilClient.is_unset(request.union_id):
            body['unionId'] = request.union_id
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
            dingtalkcrm__1__0_models.JoinGroupSetResponse(),
            await self.do_roarequest_async('JoinGroupSet', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/groupSets/join', 'json', req, runtime)
        )

    def list_crm_personal_customers(
        self,
        request: dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest,
    ) -> dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders()
        return self.list_crm_personal_customers_with_options(request, headers, runtime)

    async def list_crm_personal_customers_async(
        self,
        request: dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest,
    ) -> dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders()
        return await self.list_crm_personal_customers_with_options_async(request, headers, runtime)

    def list_crm_personal_customers_with_options(
        self,
        request: dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest,
        headers: dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse(),
            self.do_roarequest('ListCrmPersonalCustomers', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/personalCustomers/batchQuery', 'json', req, runtime)
        )

    async def list_crm_personal_customers_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest,
        headers: dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            dingtalkcrm__1__0_models.ListCrmPersonalCustomersResponse(),
            await self.do_roarequest_async('ListCrmPersonalCustomers', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/personalCustomers/batchQuery', 'json', req, runtime)
        )

    def list_group_set(
        self,
        request: dingtalkcrm__1__0_models.ListGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.ListGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ListGroupSetHeaders()
        return self.list_group_set_with_options(request, headers, runtime)

    async def list_group_set_async(
        self,
        request: dingtalkcrm__1__0_models.ListGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.ListGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ListGroupSetHeaders()
        return await self.list_group_set_with_options_async(request, headers, runtime)

    def list_group_set_with_options(
        self,
        request: dingtalkcrm__1__0_models.ListGroupSetRequest,
        headers: dingtalkcrm__1__0_models.ListGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ListGroupSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.ListGroupSetResponse(),
            self.do_roarequest('ListGroupSet', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/groupSets/lists', 'json', req, runtime)
        )

    async def list_group_set_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.ListGroupSetRequest,
        headers: dingtalkcrm__1__0_models.ListGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ListGroupSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.ListGroupSetResponse(),
            await self.do_roarequest_async('ListGroupSet', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/groupSets/lists', 'json', req, runtime)
        )

    def query_all_customer(
        self,
        request: dingtalkcrm__1__0_models.QueryAllCustomerRequest,
    ) -> dingtalkcrm__1__0_models.QueryAllCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryAllCustomerHeaders()
        return self.query_all_customer_with_options(request, headers, runtime)

    async def query_all_customer_async(
        self,
        request: dingtalkcrm__1__0_models.QueryAllCustomerRequest,
    ) -> dingtalkcrm__1__0_models.QueryAllCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryAllCustomerHeaders()
        return await self.query_all_customer_with_options_async(request, headers, runtime)

    def query_all_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.QueryAllCustomerRequest,
        headers: dingtalkcrm__1__0_models.QueryAllCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryAllCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
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
            dingtalkcrm__1__0_models.QueryAllCustomerResponse(),
            self.do_roarequest('QueryAllCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customerInstances', 'json', req, runtime)
        )

    async def query_all_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.QueryAllCustomerRequest,
        headers: dingtalkcrm__1__0_models.QueryAllCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryAllCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
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
            dingtalkcrm__1__0_models.QueryAllCustomerResponse(),
            await self.do_roarequest_async('QueryAllCustomer', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/customerInstances', 'json', req, runtime)
        )

    def query_all_tracks(
        self,
        request: dingtalkcrm__1__0_models.QueryAllTracksRequest,
    ) -> dingtalkcrm__1__0_models.QueryAllTracksResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryAllTracksHeaders()
        return self.query_all_tracks_with_options(request, headers, runtime)

    async def query_all_tracks_async(
        self,
        request: dingtalkcrm__1__0_models.QueryAllTracksRequest,
    ) -> dingtalkcrm__1__0_models.QueryAllTracksResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryAllTracksHeaders()
        return await self.query_all_tracks_with_options_async(request, headers, runtime)

    def query_all_tracks_with_options(
        self,
        request: dingtalkcrm__1__0_models.QueryAllTracksRequest,
        headers: dingtalkcrm__1__0_models.QueryAllTracksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryAllTracksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['order'] = request.order
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
            dingtalkcrm__1__0_models.QueryAllTracksResponse(),
            self.do_roarequest('QueryAllTracks', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/customers/tracks', 'json', req, runtime)
        )

    async def query_all_tracks_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.QueryAllTracksRequest,
        headers: dingtalkcrm__1__0_models.QueryAllTracksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryAllTracksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['order'] = request.order
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
            dingtalkcrm__1__0_models.QueryAllTracksResponse(),
            await self.do_roarequest_async('QueryAllTracks', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/customers/tracks', 'json', req, runtime)
        )

    def query_crm_group_chats(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest,
    ) -> dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders()
        return self.query_crm_group_chats_with_options(request, headers, runtime)

    async def query_crm_group_chats_async(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest,
    ) -> dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders()
        return await self.query_crm_group_chats_with_options_async(request, headers, runtime)

    def query_crm_group_chats_with_options(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest,
        headers: dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse(),
            self.do_roarequest('QueryCrmGroupChats', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/crmGroupChats', 'json', req, runtime)
        )

    async def query_crm_group_chats_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest,
        headers: dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryCrmGroupChatsResponse(),
            await self.do_roarequest_async('QueryCrmGroupChats', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/crmGroupChats', 'json', req, runtime)
        )

    def query_crm_personal_customer(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders()
        return self.query_crm_personal_customer_with_options(request, headers, runtime)

    async def query_crm_personal_customer_async(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders()
        return await self.query_crm_personal_customer_with_options_async(request, headers, runtime)

    def query_crm_personal_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse(),
            self.do_roarequest('QueryCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    async def query_crm_personal_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_operator_user_id):
            query['currentOperatorUserId'] = request.current_operator_user_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_dsl):
            query['queryDsl'] = request.query_dsl
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryCrmPersonalCustomerResponse(),
            await self.do_roarequest_async('QueryCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    def query_official_account_user_basic_info(
        self,
        request: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest,
    ) -> dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders()
        return self.query_official_account_user_basic_info_with_options(request, headers, runtime)

    async def query_official_account_user_basic_info_async(
        self,
        request: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest,
    ) -> dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders()
        return await self.query_official_account_user_basic_info_with_options_async(request, headers, runtime)

    def query_official_account_user_basic_info_with_options(
        self,
        request: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest,
        headers: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_token):
            query['bindingToken'] = request.binding_token
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse(),
            self.do_roarequest('QueryOfficialAccountUserBasicInfo', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/basics/users', 'json', req, runtime)
        )

    async def query_official_account_user_basic_info_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest,
        headers: dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binding_token):
            query['bindingToken'] = request.binding_token
        if not UtilClient.is_unset(request.union_id):
            query['unionId'] = request.union_id
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
            dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoResponse(),
            await self.do_roarequest_async('QueryOfficialAccountUserBasicInfo', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/officialAccounts/basics/users', 'json', req, runtime)
        )

    def query_relation_datas_by_target_id(
        self,
        target_id: str,
        request: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest,
    ) -> dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders()
        return self.query_relation_datas_by_target_id_with_options(target_id, request, headers, runtime)

    async def query_relation_datas_by_target_id_async(
        self,
        target_id: str,
        request: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest,
    ) -> dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders()
        return await self.query_relation_datas_by_target_id_with_options_async(target_id, request, headers, runtime)

    def query_relation_datas_by_target_id_with_options(
        self,
        target_id: str,
        request: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest,
        headers: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse:
        UtilClient.validate_model(request)
        target_id = OpenApiUtilClient.get_encode_param(target_id)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse(),
            self.do_roarequest('QueryRelationDatasByTargetId', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/relations/datas/targets/{target_id}', 'json', req, runtime)
        )

    async def query_relation_datas_by_target_id_with_options_async(
        self,
        target_id: str,
        request: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest,
        headers: dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse:
        UtilClient.validate_model(request)
        target_id = OpenApiUtilClient.get_encode_param(target_id)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
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
            dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdResponse(),
            await self.do_roarequest_async('QueryRelationDatasByTargetId', 'crm_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/crm/relations/datas/targets/{target_id}', 'json', req, runtime)
        )

    def recall_official_account_otomessage(
        self,
        request: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageHeaders()
        return self.recall_official_account_otomessage_with_options(request, headers, runtime)

    async def recall_official_account_otomessage_async(
        self,
        request: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageHeaders()
        return await self.recall_official_account_otomessage_with_options_async(request, headers, runtime)

    def recall_official_account_otomessage_with_options(
        self,
        request: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.open_push_id):
            body['openPushId'] = request.open_push_id
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
            dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse(),
            self.do_roarequest('RecallOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/recall', 'json', req, runtime)
        )

    async def recall_official_account_otomessage_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.open_push_id):
            body['openPushId'] = request.open_push_id
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
            dingtalkcrm__1__0_models.RecallOfficialAccountOTOMessageResponse(),
            await self.do_roarequest_async('RecallOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/recall', 'json', req, runtime)
        )

    def send_official_account_otomessage(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders()
        return self.send_official_account_otomessage_with_options(request, headers, runtime)

    async def send_official_account_otomessage_async(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders()
        return await self.send_official_account_otomessage_with_options_async(request, headers, runtime)

    def send_official_account_otomessage_with_options(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse(),
            self.do_roarequest('SendOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/send', 'json', req, runtime)
        )

    async def send_official_account_otomessage_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest,
        headers: dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageResponse(),
            await self.do_roarequest_async('SendOfficialAccountOTOMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/oToMessages/send', 'json', req, runtime)
        )

    def send_official_account_snsmessage(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders()
        return self.send_official_account_snsmessage_with_options(request, headers, runtime)

    async def send_official_account_snsmessage_async(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders()
        return await self.send_official_account_snsmessage_with_options_async(request, headers, runtime)

    def send_official_account_snsmessage_with_options(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest,
        headers: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_token):
            body['bindingToken'] = request.binding_token
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse(),
            self.do_roarequest('SendOfficialAccountSNSMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/snsMessages/send', 'json', req, runtime)
        )

    async def send_official_account_snsmessage_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest,
        headers: dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_token):
            body['bindingToken'] = request.binding_token
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageResponse(),
            await self.do_roarequest_async('SendOfficialAccountSNSMessage', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/officialAccounts/snsMessages/send', 'json', req, runtime)
        )

    def service_window_message_batch_push(
        self,
        request: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushRequest,
    ) -> dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushHeaders()
        return self.service_window_message_batch_push_with_options(request, headers, runtime)

    async def service_window_message_batch_push_async(
        self,
        request: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushRequest,
    ) -> dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushHeaders()
        return await self.service_window_message_batch_push_with_options_async(request, headers, runtime)

    def service_window_message_batch_push_with_options(
        self,
        request: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushRequest,
        headers: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse(),
            self.do_roarequest('ServiceWindowMessageBatchPush', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/messages/batchSend', 'json', req, runtime)
        )

    async def service_window_message_batch_push_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushRequest,
        headers: dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['bizId'] = request.biz_id
        if not UtilClient.is_unset(request.detail):
            body['detail'] = request.detail
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
            dingtalkcrm__1__0_models.ServiceWindowMessageBatchPushResponse(),
            await self.do_roarequest_async('ServiceWindowMessageBatchPush', 'crm_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/crm/messages/batchSend', 'json', req, runtime)
        )

    def update_crm_personal_customer(
        self,
        request: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders()
        return self.update_crm_personal_customer_with_options(request, headers, runtime)

    async def update_crm_personal_customer_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest,
    ) -> dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders()
        return await self.update_crm_personal_customer_with_options_async(request, headers, runtime)

    def update_crm_personal_customer_with_options(
        self,
        request: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modifier_nick):
            body['modifierNick'] = request.modifier_nick
        if not UtilClient.is_unset(request.modifier_user_id):
            body['modifierUserId'] = request.modifier_user_id
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse(),
            self.do_roarequest('UpdateCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    async def update_crm_personal_customer_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest,
        headers: dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.extend_data):
            body['extendData'] = request.extend_data
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modifier_nick):
            body['modifierNick'] = request.modifier_nick
        if not UtilClient.is_unset(request.modifier_user_id):
            body['modifierUserId'] = request.modifier_user_id
        if not UtilClient.is_unset(request.permission):
            body['permission'] = request.permission
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.skip_duplicate_check):
            body['skipDuplicateCheck'] = request.skip_duplicate_check
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
            dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerResponse(),
            await self.do_roarequest_async('UpdateCrmPersonalCustomer', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/personalCustomers', 'json', req, runtime)
        )

    def update_group_set(
        self,
        request: dingtalkcrm__1__0_models.UpdateGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.UpdateGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateGroupSetHeaders()
        return self.update_group_set_with_options(request, headers, runtime)

    async def update_group_set_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateGroupSetRequest,
    ) -> dingtalkcrm__1__0_models.UpdateGroupSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateGroupSetHeaders()
        return await self.update_group_set_with_options_async(request, headers, runtime)

    def update_group_set_with_options(
        self,
        request: dingtalkcrm__1__0_models.UpdateGroupSetRequest,
        headers: dingtalkcrm__1__0_models.UpdateGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.manager_user_ids):
            body['managerUserIds'] = request.manager_user_ids
        if not UtilClient.is_unset(request.member_quota):
            body['memberQuota'] = request.member_quota
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notice):
            body['notice'] = request.notice
        if not UtilClient.is_unset(request.notice_toped):
            body['noticeToped'] = request.notice_toped
        if not UtilClient.is_unset(request.open_group_set_id):
            body['openGroupSetId'] = request.open_group_set_id
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
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
            dingtalkcrm__1__0_models.UpdateGroupSetResponse(),
            self.do_roarequest('UpdateGroupSet', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/groupSets/set', 'boolean', req, runtime)
        )

    async def update_group_set_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateGroupSetRequest,
        headers: dingtalkcrm__1__0_models.UpdateGroupSetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateGroupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.manager_user_ids):
            body['managerUserIds'] = request.manager_user_ids
        if not UtilClient.is_unset(request.member_quota):
            body['memberQuota'] = request.member_quota
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notice):
            body['notice'] = request.notice
        if not UtilClient.is_unset(request.notice_toped):
            body['noticeToped'] = request.notice_toped
        if not UtilClient.is_unset(request.open_group_set_id):
            body['openGroupSetId'] = request.open_group_set_id
        if not UtilClient.is_unset(request.owner_user_id):
            body['ownerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
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
            dingtalkcrm__1__0_models.UpdateGroupSetResponse(),
            await self.do_roarequest_async('UpdateGroupSet', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/groupSets/set', 'boolean', req, runtime)
        )

    def update_relation_meta_field(
        self,
        request: dingtalkcrm__1__0_models.UpdateRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateRelationMetaFieldHeaders()
        return self.update_relation_meta_field_with_options(request, headers, runtime)

    async def update_relation_meta_field_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateRelationMetaFieldRequest,
    ) -> dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcrm__1__0_models.UpdateRelationMetaFieldHeaders()
        return await self.update_relation_meta_field_with_options_async(request, headers, runtime)

    def update_relation_meta_field_with_options(
        self,
        request: dingtalkcrm__1__0_models.UpdateRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.UpdateRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_dtolist):
            body['fieldDTOList'] = request.field_dtolist
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse(),
            self.do_roarequest('UpdateRelationMetaField', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/relations/metas/fields', 'json', req, runtime)
        )

    async def update_relation_meta_field_with_options_async(
        self,
        request: dingtalkcrm__1__0_models.UpdateRelationMetaFieldRequest,
        headers: dingtalkcrm__1__0_models.UpdateRelationMetaFieldHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_dtolist):
            body['fieldDTOList'] = request.field_dtolist
        if not UtilClient.is_unset(request.operator_user_id):
            body['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.relation_type):
            body['relationType'] = request.relation_type
        if not UtilClient.is_unset(request.tenant):
            body['tenant'] = request.tenant
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
            dingtalkcrm__1__0_models.UpdateRelationMetaFieldResponse(),
            await self.do_roarequest_async('UpdateRelationMetaField', 'crm_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/crm/relations/metas/fields', 'json', req, runtime)
        )
