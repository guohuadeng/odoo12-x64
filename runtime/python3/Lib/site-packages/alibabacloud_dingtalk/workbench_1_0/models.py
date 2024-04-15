# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetDingPortalDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetDingPortalDetailResponseBodyPages(TeaModel):
    def __init__(
        self,
        all_visible: bool = None,
        dept_ids: List[int] = None,
        page_name: str = None,
        page_uuid: str = None,
        role_ids: List[int] = None,
        userids: List[str] = None,
    ):
        # 是否全公司可见
        self.all_visible = all_visible
        # 可见部门 ID 铺
        self.dept_ids = dept_ids
        # 页面名称
        self.page_name = page_name
        # 页面ID
        self.page_uuid = page_uuid
        # 可见角色列表
        self.role_ids = role_ids
        # 可见员工 ID 列表
        self.userids = userids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_visible is not None:
            result['allVisible'] = self.all_visible
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.page_name is not None:
            result['pageName'] = self.page_name
        if self.page_uuid is not None:
            result['pageUuid'] = self.page_uuid
        if self.role_ids is not None:
            result['roleIds'] = self.role_ids
        if self.userids is not None:
            result['userids'] = self.userids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allVisible') is not None:
            self.all_visible = m.get('allVisible')
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('pageName') is not None:
            self.page_name = m.get('pageName')
        if m.get('pageUuid') is not None:
            self.page_uuid = m.get('pageUuid')
        if m.get('roleIds') is not None:
            self.role_ids = m.get('roleIds')
        if m.get('userids') is not None:
            self.userids = m.get('userids')
        return self


class GetDingPortalDetailResponseBody(TeaModel):
    def __init__(
        self,
        app_uuid: str = None,
        ding_portal_name: str = None,
        pages: List[GetDingPortalDetailResponseBodyPages] = None,
    ):
        # 工作台ID
        self.app_uuid = app_uuid
        # 工作台名称
        self.ding_portal_name = ding_portal_name
        # 工作台页面信息
        self.pages = pages

    def validate(self):
        if self.pages:
            for k in self.pages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uuid is not None:
            result['appUuid'] = self.app_uuid
        if self.ding_portal_name is not None:
            result['dingPortalName'] = self.ding_portal_name
        result['pages'] = []
        if self.pages is not None:
            for k in self.pages:
                result['pages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appUuid') is not None:
            self.app_uuid = m.get('appUuid')
        if m.get('dingPortalName') is not None:
            self.ding_portal_name = m.get('dingPortalName')
        self.pages = []
        if m.get('pages') is not None:
            for k in m.get('pages'):
                temp_model = GetDingPortalDetailResponseBodyPages()
                self.pages.append(temp_model.from_map(k))
        return self


class GetDingPortalDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDingPortalDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDingPortalDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPluginPermissionPointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetPluginPermissionPointRequest(TeaModel):
    def __init__(
        self,
        mini_app_id: str = None,
    ):
        # 插件id
        self.mini_app_id = mini_app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_app_id is not None:
            result['miniAppId'] = self.mini_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('miniAppId') is not None:
            self.mini_app_id = m.get('miniAppId')
        return self


class GetPluginPermissionPointResponseBody(TeaModel):
    def __init__(
        self,
        permission_point_list: List[str] = None,
    ):
        # 插件权限点列表
        self.permission_point_list = permission_point_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_point_list is not None:
            result['permissionPointList'] = self.permission_point_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permissionPointList') is not None:
            self.permission_point_list = m.get('permissionPointList')
        return self


class GetPluginPermissionPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPluginPermissionPointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPluginPermissionPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPluginRuleCheckInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetPluginRuleCheckInfoRequest(TeaModel):
    def __init__(
        self,
        mini_app_id: str = None,
    ):
        self.mini_app_id = mini_app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_app_id is not None:
            result['miniAppId'] = self.mini_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('miniAppId') is not None:
            self.mini_app_id = m.get('miniAppId')
        return self


class GetPluginRuleCheckInfoResponseBody(TeaModel):
    def __init__(
        self,
        pack_code: str = None,
        plugin_rule_check_detail: str = None,
    ):
        # 权限包code
        self.pack_code = pack_code
        # 校验规则
        self.plugin_rule_check_detail = plugin_rule_check_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pack_code is not None:
            result['packCode'] = self.pack_code
        if self.plugin_rule_check_detail is not None:
            result['pluginRuleCheckDetail'] = self.plugin_rule_check_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packCode') is not None:
            self.pack_code = m.get('packCode')
        if m.get('pluginRuleCheckDetail') is not None:
            self.plugin_rule_check_detail = m.get('pluginRuleCheckDetail')
        return self


class GetPluginRuleCheckInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPluginRuleCheckInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPluginRuleCheckInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkBenchGroupHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ListWorkBenchGroupRequest(TeaModel):
    def __init__(
        self,
        ecological_corp_id: str = None,
        group_type: str = None,
        op_union_id: str = None,
    ):
        # 合作空间corpId
        self.ecological_corp_id = ecological_corp_id
        # WORK_ALL
        self.group_type = group_type
        # 操作人unionId
        self.op_union_id = op_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecological_corp_id is not None:
            result['ecologicalCorpId'] = self.ecological_corp_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.op_union_id is not None:
            result['opUnionId'] = self.op_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ecologicalCorpId') is not None:
            self.ecological_corp_id = m.get('ecologicalCorpId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('opUnionId') is not None:
            self.op_union_id = m.get('opUnionId')
        return self


class ListWorkBenchGroupResponseBodyGroupList(TeaModel):
    def __init__(
        self,
        component_id: str = None,
        name: str = None,
    ):
        # 分组id
        self.component_id = component_id
        # 分组名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['componentId'] = self.component_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListWorkBenchGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_list: List[ListWorkBenchGroupResponseBodyGroupList] = None,
    ):
        # 应用列表
        self.group_list = group_list

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['groupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['groupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_list = []
        if m.get('groupList') is not None:
            for k in m.get('groupList'):
                temp_model = ListWorkBenchGroupResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k))
        return self


class ListWorkBenchGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWorkBenchGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListWorkBenchGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryComponentScopesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryComponentScopesResponseBody(TeaModel):
    def __init__(
        self,
        dept_visible_scopes: List[int] = None,
        user_visible_scopes: List[str] = None,
    ):
        self.dept_visible_scopes = dept_visible_scopes
        # scopes
        self.user_visible_scopes = user_visible_scopes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_visible_scopes is not None:
            result['deptVisibleScopes'] = self.dept_visible_scopes
        if self.user_visible_scopes is not None:
            result['userVisibleScopes'] = self.user_visible_scopes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptVisibleScopes') is not None:
            self.dept_visible_scopes = m.get('deptVisibleScopes')
        if m.get('userVisibleScopes') is not None:
            self.user_visible_scopes = m.get('userVisibleScopes')
        return self


class QueryComponentScopesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryComponentScopesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryComponentScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShortcutScopesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class QueryShortcutScopesResponseBody(TeaModel):
    def __init__(
        self,
        dept_visible_scopes: List[int] = None,
        user_visible_scopes: List[str] = None,
    ):
        self.dept_visible_scopes = dept_visible_scopes
        # errorMsg
        self.user_visible_scopes = user_visible_scopes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_visible_scopes is not None:
            result['deptVisibleScopes'] = self.dept_visible_scopes
        if self.user_visible_scopes is not None:
            result['userVisibleScopes'] = self.user_visible_scopes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptVisibleScopes') is not None:
            self.dept_visible_scopes = m.get('deptVisibleScopes')
        if m.get('userVisibleScopes') is not None:
            self.user_visible_scopes = m.get('userVisibleScopes')
        return self


class QueryShortcutScopesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryShortcutScopesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryShortcutScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDingPortalPageScopeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_dingtalk_access_token = x_acs_dingtalk_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class UpdateDingPortalPageScopeRequest(TeaModel):
    def __init__(
        self,
        all_visible: bool = None,
        dept_ids: List[int] = None,
        role_ids: List[int] = None,
        userids: List[str] = None,
    ):
        # 是否全员可见
        self.all_visible = all_visible
        # 可见部门列表
        self.dept_ids = dept_ids
        # 可见角色列表
        self.role_ids = role_ids
        # 可见用户列表
        self.userids = userids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_visible is not None:
            result['allVisible'] = self.all_visible
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.role_ids is not None:
            result['roleIds'] = self.role_ids
        if self.userids is not None:
            result['userids'] = self.userids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allVisible') is not None:
            self.all_visible = m.get('allVisible')
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('roleIds') is not None:
            self.role_ids = m.get('roleIds')
        if m.get('userids') is not None:
            self.userids = m.get('userids')
        return self


class UpdateDingPortalPageScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


