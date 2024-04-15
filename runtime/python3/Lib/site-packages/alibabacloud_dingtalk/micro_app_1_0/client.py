# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
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

    def add_app_roles_to_member(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppRolesToMemberRequest,
    ) -> dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddAppRolesToMemberHeaders()
        return self.add_app_roles_to_member_with_options(agent_id, request, headers, runtime)

    async def add_app_roles_to_member_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppRolesToMemberRequest,
    ) -> dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddAppRolesToMemberHeaders()
        return await self.add_app_roles_to_member_with_options_async(agent_id, request, headers, runtime)

    def add_app_roles_to_member_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppRolesToMemberRequest,
        headers: dingtalkmicro_app__1__0_models.AddAppRolesToMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.member_id):
            body['memberId'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role_list):
            body['roleList'] = request.role_list
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
            dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse(),
            self.do_roarequest('AddAppRolesToMember', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}/members/roles', 'json', req, runtime)
        )

    async def add_app_roles_to_member_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppRolesToMemberRequest,
        headers: dingtalkmicro_app__1__0_models.AddAppRolesToMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.member_id):
            body['memberId'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role_list):
            body['roleList'] = request.role_list
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
            dingtalkmicro_app__1__0_models.AddAppRolesToMemberResponse(),
            await self.do_roarequest_async('AddAppRolesToMember', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}/members/roles', 'json', req, runtime)
        )

    def add_app_to_work_bench_group(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupRequest,
    ) -> dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupHeaders()
        return self.add_app_to_work_bench_group_with_options(agent_id, request, headers, runtime)

    async def add_app_to_work_bench_group_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupRequest,
    ) -> dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupHeaders()
        return await self.add_app_to_work_bench_group_with_options_async(agent_id, request, headers, runtime)

    def add_app_to_work_bench_group_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupRequest,
        headers: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.component_id):
            body['componentId'] = request.component_id
        if not UtilClient.is_unset(request.ecological_corp_id):
            body['ecologicalCorpId'] = request.ecological_corp_id
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse(),
            self.do_roarequest('AddAppToWorkBenchGroup', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/addToWorkBenchGroup', 'json', req, runtime)
        )

    async def add_app_to_work_bench_group_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupRequest,
        headers: dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.component_id):
            body['componentId'] = request.component_id
        if not UtilClient.is_unset(request.ecological_corp_id):
            body['ecologicalCorpId'] = request.ecological_corp_id
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.AddAppToWorkBenchGroupResponse(),
            await self.do_roarequest_async('AddAppToWorkBenchGroup', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/addToWorkBenchGroup', 'json', req, runtime)
        )

    def add_member_to_app_role(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.AddMemberToAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddMemberToAppRoleHeaders()
        return self.add_member_to_app_role_with_options(agent_id, role_id, request, headers, runtime)

    async def add_member_to_app_role_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.AddMemberToAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.AddMemberToAppRoleHeaders()
        return await self.add_member_to_app_role_with_options_async(agent_id, role_id, request, headers, runtime)

    def add_member_to_app_role_with_options(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.AddMemberToAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.AddMemberToAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse(),
            self.do_roarequest('AddMemberToAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/members', 'json', req, runtime)
        )

    async def add_member_to_app_role_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.AddMemberToAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.AddMemberToAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.AddMemberToAppRoleResponse(),
            await self.do_roarequest_async('AddMemberToAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/members', 'json', req, runtime)
        )

    def create_apaas_app(
        self,
        request: dingtalkmicro_app__1__0_models.CreateApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.CreateApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.CreateApaasAppHeaders()
        return self.create_apaas_app_with_options(request, headers, runtime)

    async def create_apaas_app_async(
        self,
        request: dingtalkmicro_app__1__0_models.CreateApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.CreateApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.CreateApaasAppHeaders()
        return await self.create_apaas_app_with_options_async(request, headers, runtime)

    def create_apaas_app_with_options(
        self,
        request: dingtalkmicro_app__1__0_models.CreateApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.CreateApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.CreateApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_desc):
            body['appDesc'] = request.app_desc
        if not UtilClient.is_unset(request.app_icon):
            body['appIcon'] = request.app_icon
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.homepage_edit_link):
            body['homepageEditLink'] = request.homepage_edit_link
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.is_short_cut):
            body['isShortCut'] = request.is_short_cut
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.pc_homepage_edit_link):
            body['pcHomepageEditLink'] = request.pc_homepage_edit_link
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
        if not UtilClient.is_unset(request.template_key):
            body['templateKey'] = request.template_key
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
            dingtalkmicro_app__1__0_models.CreateApaasAppResponse(),
            self.do_roarequest('CreateApaasApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apaasApps', 'json', req, runtime)
        )

    async def create_apaas_app_with_options_async(
        self,
        request: dingtalkmicro_app__1__0_models.CreateApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.CreateApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.CreateApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_desc):
            body['appDesc'] = request.app_desc
        if not UtilClient.is_unset(request.app_icon):
            body['appIcon'] = request.app_icon
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.homepage_edit_link):
            body['homepageEditLink'] = request.homepage_edit_link
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.is_short_cut):
            body['isShortCut'] = request.is_short_cut
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.pc_homepage_edit_link):
            body['pcHomepageEditLink'] = request.pc_homepage_edit_link
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
        if not UtilClient.is_unset(request.template_key):
            body['templateKey'] = request.template_key
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
            dingtalkmicro_app__1__0_models.CreateApaasAppResponse(),
            await self.do_roarequest_async('CreateApaasApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apaasApps', 'json', req, runtime)
        )

    def create_inner_app(
        self,
        request: dingtalkmicro_app__1__0_models.CreateInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.CreateInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.CreateInnerAppHeaders()
        return self.create_inner_app_with_options(request, headers, runtime)

    async def create_inner_app_async(
        self,
        request: dingtalkmicro_app__1__0_models.CreateInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.CreateInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.CreateInnerAppHeaders()
        return await self.create_inner_app_with_options_async(request, headers, runtime)

    def create_inner_app_with_options(
        self,
        request: dingtalkmicro_app__1__0_models.CreateInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.CreateInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.CreateInnerAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.ip_white_list):
            body['ipWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
        if not UtilClient.is_unset(request.scope_type):
            body['scopeType'] = request.scope_type
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
            dingtalkmicro_app__1__0_models.CreateInnerAppResponse(),
            self.do_roarequest('CreateInnerApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps', 'json', req, runtime)
        )

    async def create_inner_app_with_options_async(
        self,
        request: dingtalkmicro_app__1__0_models.CreateInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.CreateInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.CreateInnerAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.ip_white_list):
            body['ipWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
        if not UtilClient.is_unset(request.scope_type):
            body['scopeType'] = request.scope_type
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
            dingtalkmicro_app__1__0_models.CreateInnerAppResponse(),
            await self.do_roarequest_async('CreateInnerApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps', 'json', req, runtime)
        )

    def delete_app_role(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.DeleteAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.DeleteAppRoleHeaders()
        return self.delete_app_role_with_options(agent_id, role_id, request, headers, runtime)

    async def delete_app_role_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.DeleteAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.DeleteAppRoleHeaders()
        return await self.delete_app_role_with_options_async(agent_id, role_id, request, headers, runtime)

    def delete_app_role_with_options(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.DeleteAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.DeleteAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.DeleteAppRoleResponse(),
            self.do_roarequest('DeleteAppRole', 'microApp_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}', 'json', req, runtime)
        )

    async def delete_app_role_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.DeleteAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.DeleteAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        query = {}
        if not UtilClient.is_unset(request.op_user_id):
            query['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.DeleteAppRoleResponse(),
            await self.do_roarequest_async('DeleteAppRole', 'microApp_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}', 'json', req, runtime)
        )

    def delete_inner_app(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.DeleteInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders()
        return self.delete_inner_app_with_options(agent_id, request, headers, runtime)

    async def delete_inner_app_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.DeleteInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders()
        return await self.delete_inner_app_with_options_async(agent_id, request, headers, runtime)

    def delete_inner_app_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.DeleteInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.op_union_id):
            query['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.DeleteInnerAppResponse(),
            self.do_roarequest('DeleteInnerApp', 'microApp_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )

    async def delete_inner_app_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.DeleteInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.DeleteInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.op_union_id):
            query['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.DeleteInnerAppResponse(),
            await self.do_roarequest_async('DeleteInnerApp', 'microApp_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )

    def get_apaas_app(
        self,
        biz_app_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetApaasAppHeaders()
        return self.get_apaas_app_with_options(biz_app_id, headers, runtime)

    async def get_apaas_app_async(
        self,
        biz_app_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetApaasAppHeaders()
        return await self.get_apaas_app_with_options_async(biz_app_id, headers, runtime)

    def get_apaas_app_with_options(
        self,
        biz_app_id: str,
        headers: dingtalkmicro_app__1__0_models.GetApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetApaasAppResponse:
        biz_app_id = OpenApiUtilClient.get_encode_param(biz_app_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetApaasAppResponse(),
            self.do_roarequest('GetApaasApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apaasApps/{biz_app_id}', 'json', req, runtime)
        )

    async def get_apaas_app_with_options_async(
        self,
        biz_app_id: str,
        headers: dingtalkmicro_app__1__0_models.GetApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetApaasAppResponse:
        biz_app_id = OpenApiUtilClient.get_encode_param(biz_app_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetApaasAppResponse(),
            await self.do_roarequest_async('GetApaasApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apaasApps/{biz_app_id}', 'json', req, runtime)
        )

    def get_app_role_scope_by_role_id(
        self,
        agent_id: str,
        role_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdHeaders()
        return self.get_app_role_scope_by_role_id_with_options(agent_id, role_id, headers, runtime)

    async def get_app_role_scope_by_role_id_async(
        self,
        agent_id: str,
        role_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdHeaders()
        return await self.get_app_role_scope_by_role_id_with_options_async(agent_id, role_id, headers, runtime)

    def get_app_role_scope_by_role_id_with_options(
        self,
        agent_id: str,
        role_id: str,
        headers: dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse(),
            self.do_roarequest('GetAppRoleScopeByRoleId', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/scopes', 'json', req, runtime)
        )

    async def get_app_role_scope_by_role_id_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        headers: dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetAppRoleScopeByRoleIdResponse(),
            await self.do_roarequest_async('GetAppRoleScopeByRoleId', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/scopes', 'json', req, runtime)
        )

    def get_inner_app(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.GetInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.GetInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetInnerAppHeaders()
        return self.get_inner_app_with_options(agent_id, request, headers, runtime)

    async def get_inner_app_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.GetInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.GetInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetInnerAppHeaders()
        return await self.get_inner_app_with_options_async(agent_id, request, headers, runtime)

    def get_inner_app_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.GetInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.GetInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.ecological_corp_id):
            query['ecologicalCorpId'] = request.ecological_corp_id
        if not UtilClient.is_unset(request.op_union_id):
            query['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.GetInnerAppResponse(),
            self.do_roarequest('GetInnerApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )

    async def get_inner_app_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.GetInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.GetInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.ecological_corp_id):
            query['ecologicalCorpId'] = request.ecological_corp_id
        if not UtilClient.is_unset(request.op_union_id):
            query['opUnionId'] = request.op_union_id
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
            dingtalkmicro_app__1__0_models.GetInnerAppResponse(),
            await self.do_roarequest_async('GetInnerApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )

    def get_micro_app_scope(
        self,
        agent_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetMicroAppScopeHeaders()
        return self.get_micro_app_scope_with_options(agent_id, headers, runtime)

    async def get_micro_app_scope_async(
        self,
        agent_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetMicroAppScopeHeaders()
        return await self.get_micro_app_scope_with_options_async(agent_id, headers, runtime)

    def get_micro_app_scope_with_options(
        self,
        agent_id: str,
        headers: dingtalkmicro_app__1__0_models.GetMicroAppScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse(),
            self.do_roarequest('GetMicroAppScope', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/scopes', 'json', req, runtime)
        )

    async def get_micro_app_scope_with_options_async(
        self,
        agent_id: str,
        headers: dingtalkmicro_app__1__0_models.GetMicroAppScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.GetMicroAppScopeResponse(),
            await self.do_roarequest_async('GetMicroAppScope', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/scopes', 'json', req, runtime)
        )

    def get_micro_app_user_access(
        self,
        agent_id: str,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders()
        return self.get_micro_app_user_access_with_options(agent_id, user_id, headers, runtime)

    async def get_micro_app_user_access_async(
        self,
        agent_id: str,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders()
        return await self.get_micro_app_user_access_with_options_async(agent_id, user_id, headers, runtime)

    def get_micro_app_user_access_with_options(
        self,
        agent_id: str,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
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
            dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse(),
            self.do_roarequest('GetMicroAppUserAccess', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/users/{user_id}/adminAccess', 'json', req, runtime)
        )

    async def get_micro_app_user_access_with_options_async(
        self,
        agent_id: str,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
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
            dingtalkmicro_app__1__0_models.GetMicroAppUserAccessResponse(),
            await self.do_roarequest_async('GetMicroAppUserAccess', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/users/{user_id}/adminAccess', 'json', req, runtime)
        )

    def list_all_app(self) -> dingtalkmicro_app__1__0_models.ListAllAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListAllAppHeaders()
        return self.list_all_app_with_options(headers, runtime)

    async def list_all_app_async(self) -> dingtalkmicro_app__1__0_models.ListAllAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListAllAppHeaders()
        return await self.list_all_app_with_options_async(headers, runtime)

    def list_all_app_with_options(
        self,
        headers: dingtalkmicro_app__1__0_models.ListAllAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListAllAppResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.ListAllAppResponse(),
            self.do_roarequest('ListAllApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/allApps', 'json', req, runtime)
        )

    async def list_all_app_with_options_async(
        self,
        headers: dingtalkmicro_app__1__0_models.ListAllAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListAllAppResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkmicro_app__1__0_models.ListAllAppResponse(),
            await self.do_roarequest_async('ListAllApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/allApps', 'json', req, runtime)
        )

    def list_app_role_scopes(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.ListAppRoleScopesRequest,
    ) -> dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListAppRoleScopesHeaders()
        return self.list_app_role_scopes_with_options(agent_id, request, headers, runtime)

    async def list_app_role_scopes_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.ListAppRoleScopesRequest,
    ) -> dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListAppRoleScopesHeaders()
        return await self.list_app_role_scopes_with_options_async(agent_id, request, headers, runtime)

    def list_app_role_scopes_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.ListAppRoleScopesRequest,
        headers: dingtalkmicro_app__1__0_models.ListAppRoleScopesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
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
            dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse(),
            self.do_roarequest('ListAppRoleScopes', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles', 'json', req, runtime)
        )

    async def list_app_role_scopes_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.ListAppRoleScopesRequest,
        headers: dingtalkmicro_app__1__0_models.ListAppRoleScopesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
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
            dingtalkmicro_app__1__0_models.ListAppRoleScopesResponse(),
            await self.do_roarequest_async('ListAppRoleScopes', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles', 'json', req, runtime)
        )

    def list_inner_app(
        self,
        request: dingtalkmicro_app__1__0_models.ListInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.ListInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListInnerAppHeaders()
        return self.list_inner_app_with_options(request, headers, runtime)

    async def list_inner_app_async(
        self,
        request: dingtalkmicro_app__1__0_models.ListInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.ListInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListInnerAppHeaders()
        return await self.list_inner_app_with_options_async(request, headers, runtime)

    def list_inner_app_with_options(
        self,
        request: dingtalkmicro_app__1__0_models.ListInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.ListInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListInnerAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecological_corp_id):
            query['ecologicalCorpId'] = request.ecological_corp_id
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
            dingtalkmicro_app__1__0_models.ListInnerAppResponse(),
            self.do_roarequest('ListInnerApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps', 'json', req, runtime)
        )

    async def list_inner_app_with_options_async(
        self,
        request: dingtalkmicro_app__1__0_models.ListInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.ListInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListInnerAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecological_corp_id):
            query['ecologicalCorpId'] = request.ecological_corp_id
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
            dingtalkmicro_app__1__0_models.ListInnerAppResponse(),
            await self.do_roarequest_async('ListInnerApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps', 'json', req, runtime)
        )

    def list_role_info_by_user(
        self,
        agent_id: str,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListRoleInfoByUserHeaders()
        return self.list_role_info_by_user_with_options(agent_id, user_id, headers, runtime)

    async def list_role_info_by_user_async(
        self,
        agent_id: str,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListRoleInfoByUserHeaders()
        return await self.list_role_info_by_user_with_options_async(agent_id, user_id, headers, runtime)

    def list_role_info_by_user_with_options(
        self,
        agent_id: str,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.ListRoleInfoByUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
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
            dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse(),
            self.do_roarequest('ListRoleInfoByUser', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/users/{user_id}/roles', 'json', req, runtime)
        )

    async def list_role_info_by_user_with_options_async(
        self,
        agent_id: str,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.ListRoleInfoByUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse:
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
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
            dingtalkmicro_app__1__0_models.ListRoleInfoByUserResponse(),
            await self.do_roarequest_async('ListRoleInfoByUser', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/apps/{agent_id}/users/{user_id}/roles', 'json', req, runtime)
        )

    def list_user_vileble_app(
        self,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders()
        return self.list_user_vileble_app_with_options(user_id, headers, runtime)

    async def list_user_vileble_app_async(
        self,
        user_id: str,
    ) -> dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders()
        return await self.list_user_vileble_app_with_options_async(user_id, headers, runtime)

    def list_user_vileble_app_with_options(
        self,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse:
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
            dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse(),
            self.do_roarequest('ListUserVilebleApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/users/{user_id}/apps', 'json', req, runtime)
        )

    async def list_user_vileble_app_with_options_async(
        self,
        user_id: str,
        headers: dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse:
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
            dingtalkmicro_app__1__0_models.ListUserVilebleAppResponse(),
            await self.do_roarequest_async('ListUserVilebleApp', 'microApp_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/microApp/users/{user_id}/apps', 'json', req, runtime)
        )

    def rebuild_role_scope_for_app_role(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleHeaders()
        return self.rebuild_role_scope_for_app_role_with_options(agent_id, role_id, request, headers, runtime)

    async def rebuild_role_scope_for_app_role_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleHeaders()
        return await self.rebuild_role_scope_for_app_role_with_options_async(agent_id, role_id, request, headers, runtime)

    def rebuild_role_scope_for_app_role_with_options(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_type):
            body['scopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse(),
            self.do_roarequest('RebuildRoleScopeForAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/scopes/rebuild', 'json', req, runtime)
        )

    async def rebuild_role_scope_for_app_role_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_type):
            body['scopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.RebuildRoleScopeForAppRoleResponse(),
            await self.do_roarequest_async('RebuildRoleScopeForAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/scopes/rebuild', 'json', req, runtime)
        )

    def register_custom_app_role(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RegisterCustomAppRoleHeaders()
        return self.register_custom_app_role_with_options(agent_id, request, headers, runtime)

    async def register_custom_app_role_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RegisterCustomAppRoleHeaders()
        return await self.register_custom_app_role_with_options_async(agent_id, request, headers, runtime)

    def register_custom_app_role_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.can_manage_role):
            body['canManageRole'] = request.can_manage_role
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
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
            dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse(),
            self.do_roarequest('RegisterCustomAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles', 'json', req, runtime)
        )

    async def register_custom_app_role_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RegisterCustomAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.can_manage_role):
            body['canManageRole'] = request.can_manage_role
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
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
            dingtalkmicro_app__1__0_models.RegisterCustomAppRoleResponse(),
            await self.do_roarequest_async('RegisterCustomAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles', 'json', req, runtime)
        )

    def remove_apaas_app(
        self,
        request: dingtalkmicro_app__1__0_models.RemoveApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.RemoveApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RemoveApaasAppHeaders()
        return self.remove_apaas_app_with_options(request, headers, runtime)

    async def remove_apaas_app_async(
        self,
        request: dingtalkmicro_app__1__0_models.RemoveApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.RemoveApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RemoveApaasAppHeaders()
        return await self.remove_apaas_app_with_options_async(request, headers, runtime)

    def remove_apaas_app_with_options(
        self,
        request: dingtalkmicro_app__1__0_models.RemoveApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.RemoveApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RemoveApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.RemoveApaasAppResponse(),
            self.do_roarequest('RemoveApaasApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apaasApps/remove', 'json', req, runtime)
        )

    async def remove_apaas_app_with_options_async(
        self,
        request: dingtalkmicro_app__1__0_models.RemoveApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.RemoveApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RemoveApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.RemoveApaasAppResponse(),
            await self.do_roarequest_async('RemoveApaasApp', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apaasApps/remove', 'json', req, runtime)
        )

    def remove_member_for_app_role(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleHeaders()
        return self.remove_member_for_app_role_with_options(agent_id, role_id, request, headers, runtime)

    async def remove_member_for_app_role_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleRequest,
    ) -> dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleHeaders()
        return await self.remove_member_for_app_role_with_options_async(agent_id, role_id, request, headers, runtime)

    def remove_member_for_app_role_with_options(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse(),
            self.do_roarequest('RemoveMemberForAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/members/batchRemove', 'json', req, runtime)
        )

    async def remove_member_for_app_role_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleRequest,
        headers: dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.dept_id_list):
            body['deptIdList'] = request.dept_id_list
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.scope_version):
            body['scopeVersion'] = request.scope_version
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
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
            dingtalkmicro_app__1__0_models.RemoveMemberForAppRoleResponse(),
            await self.do_roarequest_async('RemoveMemberForAppRole', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}/members/batchRemove', 'json', req, runtime)
        )

    def set_micro_app_scope(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest,
    ) -> dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders()
        return self.set_micro_app_scope_with_options(agent_id, request, headers, runtime)

    async def set_micro_app_scope_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest,
    ) -> dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders()
        return await self.set_micro_app_scope_with_options_async(agent_id, request, headers, runtime)

    def set_micro_app_scope_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest,
        headers: dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.add_dept_ids):
            body['addDeptIds'] = request.add_dept_ids
        if not UtilClient.is_unset(request.add_role_ids):
            body['addRoleIds'] = request.add_role_ids
        if not UtilClient.is_unset(request.add_user_ids):
            body['addUserIds'] = request.add_user_ids
        if not UtilClient.is_unset(request.del_dept_ids):
            body['delDeptIds'] = request.del_dept_ids
        if not UtilClient.is_unset(request.del_role_ids):
            body['delRoleIds'] = request.del_role_ids
        if not UtilClient.is_unset(request.del_user_ids):
            body['delUserIds'] = request.del_user_ids
        if not UtilClient.is_unset(request.only_admin_visible):
            body['onlyAdminVisible'] = request.only_admin_visible
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
            dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse(),
            self.do_roarequest('SetMicroAppScope', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/scopes', 'json', req, runtime)
        )

    async def set_micro_app_scope_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest,
        headers: dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.add_dept_ids):
            body['addDeptIds'] = request.add_dept_ids
        if not UtilClient.is_unset(request.add_role_ids):
            body['addRoleIds'] = request.add_role_ids
        if not UtilClient.is_unset(request.add_user_ids):
            body['addUserIds'] = request.add_user_ids
        if not UtilClient.is_unset(request.del_dept_ids):
            body['delDeptIds'] = request.del_dept_ids
        if not UtilClient.is_unset(request.del_role_ids):
            body['delRoleIds'] = request.del_role_ids
        if not UtilClient.is_unset(request.del_user_ids):
            body['delUserIds'] = request.del_user_ids
        if not UtilClient.is_unset(request.only_admin_visible):
            body['onlyAdminVisible'] = request.only_admin_visible
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
            dingtalkmicro_app__1__0_models.SetMicroAppScopeResponse(),
            await self.do_roarequest_async('SetMicroAppScope', 'microApp_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/microApp/apps/{agent_id}/scopes', 'json', req, runtime)
        )

    def update_apaas_app(
        self,
        request: dingtalkmicro_app__1__0_models.UpdateApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateApaasAppHeaders()
        return self.update_apaas_app_with_options(request, headers, runtime)

    async def update_apaas_app_async(
        self,
        request: dingtalkmicro_app__1__0_models.UpdateApaasAppRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateApaasAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateApaasAppHeaders()
        return await self.update_apaas_app_with_options_async(request, headers, runtime)

    def update_apaas_app_with_options(
        self,
        request: dingtalkmicro_app__1__0_models.UpdateApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_icon):
            body['appIcon'] = request.app_icon
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            body['appStatus'] = request.app_status
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.UpdateApaasAppResponse(),
            self.do_roarequest('UpdateApaasApp', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apaasApps', 'json', req, runtime)
        )

    async def update_apaas_app_with_options_async(
        self,
        request: dingtalkmicro_app__1__0_models.UpdateApaasAppRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateApaasAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateApaasAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_icon):
            body['appIcon'] = request.app_icon
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            body['appStatus'] = request.app_status
        if not UtilClient.is_unset(request.biz_app_id):
            body['bizAppId'] = request.biz_app_id
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.UpdateApaasAppResponse(),
            await self.do_roarequest_async('UpdateApaasApp', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apaasApps', 'json', req, runtime)
        )

    def update_app_role_info(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateAppRoleInfoHeaders()
        return self.update_app_role_info_with_options(agent_id, role_id, request, headers, runtime)

    async def update_app_role_info_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateAppRoleInfoHeaders()
        return await self.update_app_role_info_with_options_async(agent_id, role_id, request, headers, runtime)

    def update_app_role_info_with_options(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.can_manage_role):
            body['canManageRole'] = request.can_manage_role
        if not UtilClient.is_unset(request.new_role_name):
            body['newRoleName'] = request.new_role_name
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse(),
            self.do_roarequest('UpdateAppRoleInfo', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}', 'json', req, runtime)
        )

    async def update_app_role_info_with_options_async(
        self,
        agent_id: str,
        role_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateAppRoleInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        role_id = OpenApiUtilClient.get_encode_param(role_id)
        body = {}
        if not UtilClient.is_unset(request.can_manage_role):
            body['canManageRole'] = request.can_manage_role
        if not UtilClient.is_unset(request.new_role_name):
            body['newRoleName'] = request.new_role_name
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
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
            dingtalkmicro_app__1__0_models.UpdateAppRoleInfoResponse(),
            await self.do_roarequest_async('UpdateAppRoleInfo', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}/roles/{role_id}', 'json', req, runtime)
        )

    def update_inner_app(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders()
        return self.update_inner_app_with_options(agent_id, request, headers, runtime)

    async def update_inner_app_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateInnerAppRequest,
    ) -> dingtalkmicro_app__1__0_models.UpdateInnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders()
        return await self.update_inner_app_with_options_async(agent_id, request, headers, runtime)

    def update_inner_app_with_options(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.ip_white_list):
            body['ipWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
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
            dingtalkmicro_app__1__0_models.UpdateInnerAppResponse(),
            self.do_roarequest('UpdateInnerApp', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )

    async def update_inner_app_with_options_async(
        self,
        agent_id: str,
        request: dingtalkmicro_app__1__0_models.UpdateInnerAppRequest,
        headers: dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkmicro_app__1__0_models.UpdateInnerAppResponse:
        UtilClient.validate_model(request)
        agent_id = OpenApiUtilClient.get_encode_param(agent_id)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.homepage_link):
            body['homepageLink'] = request.homepage_link
        if not UtilClient.is_unset(request.icon):
            body['icon'] = request.icon
        if not UtilClient.is_unset(request.ip_white_list):
            body['ipWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.omp_link):
            body['ompLink'] = request.omp_link
        if not UtilClient.is_unset(request.op_union_id):
            body['opUnionId'] = request.op_union_id
        if not UtilClient.is_unset(request.pc_homepage_link):
            body['pcHomepageLink'] = request.pc_homepage_link
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
            dingtalkmicro_app__1__0_models.UpdateInnerAppResponse(),
            await self.do_roarequest_async('UpdateInnerApp', 'microApp_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/microApp/apps/{agent_id}', 'json', req, runtime)
        )
