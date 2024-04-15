# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BatchApproveUnionApplyHeaders(TeaModel):
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


class BatchApproveUnionApplyRequestBody(TeaModel):
    def __init__(
        self,
        branch_corp_id: str = None,
        link_dept_id: int = None,
        union_root_name: str = None,
    ):
        # branchCorpId
        self.branch_corp_id = branch_corp_id
        # linkDeptId
        self.link_dept_id = link_dept_id
        # unionRootName
        self.union_root_name = union_root_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_corp_id is not None:
            result['branchCorpId'] = self.branch_corp_id
        if self.link_dept_id is not None:
            result['linkDeptId'] = self.link_dept_id
        if self.union_root_name is not None:
            result['unionRootName'] = self.union_root_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branchCorpId') is not None:
            self.branch_corp_id = m.get('branchCorpId')
        if m.get('linkDeptId') is not None:
            self.link_dept_id = m.get('linkDeptId')
        if m.get('unionRootName') is not None:
            self.union_root_name = m.get('unionRootName')
        return self


class BatchApproveUnionApplyRequest(TeaModel):
    def __init__(
        self,
        body: List[BatchApproveUnionApplyRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = BatchApproveUnionApplyRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class BatchApproveUnionApplyResponse(TeaModel):
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


class ChangeMainAdminHeaders(TeaModel):
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


class ChangeMainAdminRequest(TeaModel):
    def __init__(
        self,
        effect_corp_id: str = None,
        source_user_id: str = None,
        target_user_id: str = None,
    ):
        # effectCorpId
        self.effect_corp_id = effect_corp_id
        # sourceUserId
        self.source_user_id = source_user_id
        # targetUserId
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_corp_id is not None:
            result['effectCorpId'] = self.effect_corp_id
        if self.source_user_id is not None:
            result['sourceUserId'] = self.source_user_id
        if self.target_user_id is not None:
            result['targetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectCorpId') is not None:
            self.effect_corp_id = m.get('effectCorpId')
        if m.get('sourceUserId') is not None:
            self.source_user_id = m.get('sourceUserId')
        if m.get('targetUserId') is not None:
            self.target_user_id = m.get('targetUserId')
        return self


class ChangeMainAdminResponse(TeaModel):
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


class CreateCooperateOrgHeaders(TeaModel):
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


class CreateCooperateOrgRequest(TeaModel):
    def __init__(
        self,
        industry_code: int = None,
        logo_media_id: str = None,
        org_name: str = None,
    ):
        # 行业code
        self.industry_code = industry_code
        # 合作空间的logo
        self.logo_media_id = logo_media_id
        # 合作空间组织名称
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry_code is not None:
            result['industryCode'] = self.industry_code
        if self.logo_media_id is not None:
            result['logoMediaId'] = self.logo_media_id
        if self.org_name is not None:
            result['orgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industryCode') is not None:
            self.industry_code = m.get('industryCode')
        if m.get('logoMediaId') is not None:
            self.logo_media_id = m.get('logoMediaId')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        return self


class CreateCooperateOrgResponseBody(TeaModel):
    def __init__(
        self,
        cooperate_corp_id: str = None,
    ):
        # result
        self.cooperate_corp_id = cooperate_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cooperate_corp_id is not None:
            result['cooperateCorpId'] = self.cooperate_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cooperateCorpId') is not None:
            self.cooperate_corp_id = m.get('cooperateCorpId')
        return self


class CreateCooperateOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCooperateOrgResponseBody = None,
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
            temp_model = CreateCooperateOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateManagementGroupHeaders(TeaModel):
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


class CreateManagementGroupRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class CreateManagementGroupRequestScope(TeaModel):
    def __init__(
        self,
        dept_ids: List[int] = None,
        scope_type: int = None,
    ):
        # 部门列表，只在scopeType=3 生效
        self.dept_ids = dept_ids
        # 范围类型
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        return self


class CreateManagementGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        members: List[CreateManagementGroupRequestMembers] = None,
        resource_ids: List[str] = None,
        scope: CreateManagementGroupRequestScope = None,
    ):
        self.group_name = group_name
        # 管理组成员
        self.members = members
        # 资源列表
        self.resource_ids = resource_ids
        # 管理范围
        self.scope = scope

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = CreateManagementGroupRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('scope') is not None:
            temp_model = CreateManagementGroupRequestScope()
            self.scope = temp_model.from_map(m['scope'])
        return self


class CreateManagementGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # 返回管理组groupId
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        return self


class CreateManagementGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateManagementGroupResponseBody = None,
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
            temp_model = CreateManagementGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactHideSettingHeaders(TeaModel):
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


class DeleteContactHideSettingResponse(TeaModel):
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


class DeleteEmpAttributeVisibilityHeaders(TeaModel):
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


class DeleteEmpAttributeVisibilityResponse(TeaModel):
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


class DeleteManagementGroupHeaders(TeaModel):
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


class DeleteManagementGroupResponse(TeaModel):
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


class GetApplyInviteInfoHeaders(TeaModel):
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


class GetApplyInviteInfoRequest(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
        inviter_user_id: str = None,
    ):
        # 获取部门邀请链接的部门ID
        self.dept_id = dept_id
        # 邀请者userId
        self.inviter_user_id = inviter_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.inviter_user_id is not None:
            result['inviterUserId'] = self.inviter_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('inviterUserId') is not None:
            self.inviter_user_id = m.get('inviterUserId')
        return self


class GetApplyInviteInfoResponseBody(TeaModel):
    def __init__(
        self,
        audit_type: int = None,
        emp_apply_join_dept: bool = None,
        invite_switch: bool = None,
        invite_url: str = None,
        link_invite: bool = None,
        org_apply_code_invite: bool = None,
        search_name_invite: bool = None,
    ):
        # 仅部门邀请有效： 0-无需审核 1-有权限的子管理员
        self.audit_type = audit_type
        # 是否允许员工扫码加入部门，仅在无需审核的时候有效（已经在组织内的成员通过扫描部门二维码加入某个部门）
        self.emp_apply_join_dept = emp_apply_join_dept
        # 是否开启邀请
        self.invite_switch = invite_switch
        # 邀请链接
        self.invite_url = invite_url
        # 是否开启通过链接邀请加入
        self.link_invite = link_invite
        # 是否开启通过团队号申请加入
        self.org_apply_code_invite = org_apply_code_invite
        # 是否开启通过企业名称搜索申请
        self.search_name_invite = search_name_invite

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_type is not None:
            result['auditType'] = self.audit_type
        if self.emp_apply_join_dept is not None:
            result['empApplyJoinDept'] = self.emp_apply_join_dept
        if self.invite_switch is not None:
            result['inviteSwitch'] = self.invite_switch
        if self.invite_url is not None:
            result['inviteUrl'] = self.invite_url
        if self.link_invite is not None:
            result['linkInvite'] = self.link_invite
        if self.org_apply_code_invite is not None:
            result['orgApplyCodeInvite'] = self.org_apply_code_invite
        if self.search_name_invite is not None:
            result['searchNameInvite'] = self.search_name_invite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditType') is not None:
            self.audit_type = m.get('auditType')
        if m.get('empApplyJoinDept') is not None:
            self.emp_apply_join_dept = m.get('empApplyJoinDept')
        if m.get('inviteSwitch') is not None:
            self.invite_switch = m.get('inviteSwitch')
        if m.get('inviteUrl') is not None:
            self.invite_url = m.get('inviteUrl')
        if m.get('linkInvite') is not None:
            self.link_invite = m.get('linkInvite')
        if m.get('orgApplyCodeInvite') is not None:
            self.org_apply_code_invite = m.get('orgApplyCodeInvite')
        if m.get('searchNameInvite') is not None:
            self.search_name_invite = m.get('searchNameInvite')
        return self


class GetApplyInviteInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApplyInviteInfoResponseBody = None,
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
            temp_model = GetApplyInviteInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBranchAuthDataHeaders(TeaModel):
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


class GetBranchAuthDataRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, str] = None,
        branch_corp_id: str = None,
        code: str = None,
    ):
        # 查询条件
        self.body = body
        # 分支组织corpId
        self.branch_corp_id = branch_corp_id
        # 数据编码
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.branch_corp_id is not None:
            result['branchCorpId'] = self.branch_corp_id
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('branchCorpId') is not None:
            self.branch_corp_id = m.get('branchCorpId')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetBranchAuthDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        field_value: str = None,
    ):
        # 字段code
        self.field_code = field_code
        # 字段名称
        self.field_name = field_name
        # 字段值
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['fieldCode'] = self.field_code
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.field_value is not None:
            result['fieldValue'] = self.field_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')
        return self


class GetBranchAuthDataResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetBranchAuthDataResponseBodyResult] = None,
    ):
        # result
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetBranchAuthDataResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetBranchAuthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBranchAuthDataResponseBody = None,
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
            temp_model = GetBranchAuthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardInUserHolderHeaders(TeaModel):
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


class GetCardInUserHolderResponseBody(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        card_id: str = None,
        extension: Dict[str, Any] = None,
        industry_name: str = None,
        introduce: str = None,
        name: str = None,
        org_name: str = None,
        template_id: str = None,
        title: str = None,
    ):
        # 头像
        self.avatar_url = avatar_url
        # 名片ID
        self.card_id = card_id
        # 扩展信息
        self.extension = extension
        # 行业
        self.industry_name = industry_name
        # 简介
        self.introduce = introduce
        # 名字
        self.name = name
        # 组织名称
        self.org_name = org_name
        # 模板ID
        self.template_id = template_id
        # 职位
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.card_id is not None:
            result['cardId'] = self.card_id
        if self.extension is not None:
            result['extension'] = self.extension
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('cardId') is not None:
            self.card_id = m.get('cardId')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetCardInUserHolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCardInUserHolderResponseBody = None,
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
            temp_model = GetCardInUserHolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardInfoHeaders(TeaModel):
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


class GetCardInfoResponseBodyExtensionCardContactInfoAddressArea(TeaModel):
    def __init__(
        self,
        region: str = None,
        region_full_name: str = None,
    ):
        # 地区
        self.region = region
        # 地区详细数据
        self.region_full_name = region_full_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.region_full_name is not None:
            result['regionFullName'] = self.region_full_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionFullName') is not None:
            self.region_full_name = m.get('regionFullName')
        return self


class GetCardInfoResponseBodyExtensionCardContactInfoAddress(TeaModel):
    def __init__(
        self,
        area: GetCardInfoResponseBodyExtensionCardContactInfoAddressArea = None,
        detail: str = None,
    ):
        # 区域
        self.area = area
        # 详细地址
        self.detail = detail

    def validate(self):
        if self.area:
            self.area.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['area'] = self.area.to_map()
        if self.detail is not None:
            result['detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            temp_model = GetCardInfoResponseBodyExtensionCardContactInfoAddressArea()
            self.area = temp_model.from_map(m['area'])
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        return self


class GetCardInfoResponseBodyExtensionCardContactInfoEmail(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetCardInfoResponseBodyExtensionCardContactInfoTelephone(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetCardInfoResponseBodyExtensionCardContactInfoWechat(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetCardInfoResponseBodyExtensionCardContactInfo(TeaModel):
    def __init__(
        self,
        address: List[GetCardInfoResponseBodyExtensionCardContactInfoAddress] = None,
        email: List[GetCardInfoResponseBodyExtensionCardContactInfoEmail] = None,
        telephone: List[GetCardInfoResponseBodyExtensionCardContactInfoTelephone] = None,
        wechat: List[GetCardInfoResponseBodyExtensionCardContactInfoWechat] = None,
    ):
        # 地址
        self.address = address
        # 邮箱
        self.email = email
        # 电话
        self.telephone = telephone
        # 微信
        self.wechat = wechat

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()
        if self.email:
            for k in self.email:
                if k:
                    k.validate()
        if self.telephone:
            for k in self.telephone:
                if k:
                    k.validate()
        if self.wechat:
            for k in self.wechat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['address'] = []
        if self.address is not None:
            for k in self.address:
                result['address'].append(k.to_map() if k else None)
        result['email'] = []
        if self.email is not None:
            for k in self.email:
                result['email'].append(k.to_map() if k else None)
        result['telephone'] = []
        if self.telephone is not None:
            for k in self.telephone:
                result['telephone'].append(k.to_map() if k else None)
        result['wechat'] = []
        if self.wechat is not None:
            for k in self.wechat:
                result['wechat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('address') is not None:
            for k in m.get('address'):
                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoAddress()
                self.address.append(temp_model.from_map(k))
        self.email = []
        if m.get('email') is not None:
            for k in m.get('email'):
                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoEmail()
                self.email.append(temp_model.from_map(k))
        self.telephone = []
        if m.get('telephone') is not None:
            for k in m.get('telephone'):
                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoTelephone()
                self.telephone.append(temp_model.from_map(k))
        self.wechat = []
        if m.get('wechat') is not None:
            for k in m.get('wechat'):
                temp_model = GetCardInfoResponseBodyExtensionCardContactInfoWechat()
                self.wechat.append(temp_model.from_map(k))
        return self


class GetCardInfoResponseBodyExtension(TeaModel):
    def __init__(
        self,
        card_contact_info: GetCardInfoResponseBodyExtensionCardContactInfo = None,
        corp_id: str = None,
        department: str = None,
        org_auth_level: int = None,
        org_authed: bool = None,
        org_logo: str = None,
        origin_card_url: str = None,
        share_content: str = None,
        thumbnail_url: str = None,
        video_file_name: str = None,
        video_title: str = None,
        video_url: str = None,
    ):
        # 联系信息
        self.card_contact_info = card_contact_info
        # 企业corpId
        self.corp_id = corp_id
        # 拍名片部门
        self.department = department
        # 企业认证等级
        self.org_auth_level = org_auth_level
        # 企业是否认证
        self.org_authed = org_authed
        # 企业LOGO
        self.org_logo = org_logo
        # 拍名片图片链接
        self.origin_card_url = origin_card_url
        # 分享文案
        self.share_content = share_content
        # 视频缩略图
        self.thumbnail_url = thumbnail_url
        # 视频文件名称
        self.video_file_name = video_file_name
        # 视频标题
        self.video_title = video_title
        # 视频链接
        self.video_url = video_url

    def validate(self):
        if self.card_contact_info:
            self.card_contact_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_contact_info is not None:
            result['cardContactInfo'] = self.card_contact_info.to_map()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.department is not None:
            result['department'] = self.department
        if self.org_auth_level is not None:
            result['orgAuthLevel'] = self.org_auth_level
        if self.org_authed is not None:
            result['orgAuthed'] = self.org_authed
        if self.org_logo is not None:
            result['orgLogo'] = self.org_logo
        if self.origin_card_url is not None:
            result['originCardUrl'] = self.origin_card_url
        if self.share_content is not None:
            result['shareContent'] = self.share_content
        if self.thumbnail_url is not None:
            result['thumbnailUrl'] = self.thumbnail_url
        if self.video_file_name is not None:
            result['videoFileName'] = self.video_file_name
        if self.video_title is not None:
            result['videoTitle'] = self.video_title
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardContactInfo') is not None:
            temp_model = GetCardInfoResponseBodyExtensionCardContactInfo()
            self.card_contact_info = temp_model.from_map(m['cardContactInfo'])
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('orgAuthLevel') is not None:
            self.org_auth_level = m.get('orgAuthLevel')
        if m.get('orgAuthed') is not None:
            self.org_authed = m.get('orgAuthed')
        if m.get('orgLogo') is not None:
            self.org_logo = m.get('orgLogo')
        if m.get('originCardUrl') is not None:
            self.origin_card_url = m.get('originCardUrl')
        if m.get('shareContent') is not None:
            self.share_content = m.get('shareContent')
        if m.get('thumbnailUrl') is not None:
            self.thumbnail_url = m.get('thumbnailUrl')
        if m.get('videoFileName') is not None:
            self.video_file_name = m.get('videoFileName')
        if m.get('videoTitle') is not None:
            self.video_title = m.get('videoTitle')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class GetCardInfoResponseBody(TeaModel):
    def __init__(
        self,
        admin_role: int = None,
        avatar_url: str = None,
        card_id: str = None,
        extension: GetCardInfoResponseBodyExtension = None,
        industry_name: str = None,
        introduce: Dict[str, Any] = None,
        name: str = None,
        org_name: str = None,
        settings: Dict[str, Any] = None,
        template_id: str = None,
        title: str = None,
    ):
        # 用户角色
        self.admin_role = admin_role
        # 头像
        self.avatar_url = avatar_url
        # 名片ID
        self.card_id = card_id
        # 扩展信息
        self.extension = extension
        # 行业
        self.industry_name = industry_name
        # 个人介绍
        self.introduce = introduce
        # 名字
        self.name = name
        # 组织名称
        self.org_name = org_name
        # 用户名片信息设置
        self.settings = settings
        # 模板ID
        self.template_id = template_id
        # 职位
        self.title = title

    def validate(self):
        if self.extension:
            self.extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_role is not None:
            result['adminRole'] = self.admin_role
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.card_id is not None:
            result['cardId'] = self.card_id
        if self.extension is not None:
            result['extension'] = self.extension.to_map()
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.settings is not None:
            result['settings'] = self.settings
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adminRole') is not None:
            self.admin_role = m.get('adminRole')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('cardId') is not None:
            self.card_id = m.get('cardId')
        if m.get('extension') is not None:
            temp_model = GetCardInfoResponseBodyExtension()
            self.extension = temp_model.from_map(m['extension'])
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetCardInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCardInfoResponseBody = None,
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
            temp_model = GetCardInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCooperateOrgInviteInfoHeaders(TeaModel):
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


class GetCooperateOrgInviteInfoResponseBody(TeaModel):
    def __init__(
        self,
        invite_url: str = None,
    ):
        self.invite_url = invite_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_url is not None:
            result['inviteUrl'] = self.invite_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inviteUrl') is not None:
            self.invite_url = m.get('inviteUrl')
        return self


class GetCooperateOrgInviteInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCooperateOrgInviteInfoResponseBody = None,
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
            temp_model = GetCooperateOrgInviteInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpCardStyleListHeaders(TeaModel):
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


class GetCorpCardStyleListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[Dict[str, Any]] = None,
    ):
        # Id of the request
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetCorpCardStyleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpCardStyleListResponseBody = None,
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
            temp_model = GetCorpCardStyleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDingIdByMigrationDingIdHeaders(TeaModel):
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


class GetDingIdByMigrationDingIdRequest(TeaModel):
    def __init__(
        self,
        migration_ding_id: str = None,
    ):
        # migrationDingId
        self.migration_ding_id = migration_ding_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_ding_id is not None:
            result['migrationDingId'] = self.migration_ding_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationDingId') is not None:
            self.migration_ding_id = m.get('migrationDingId')
        return self


class GetDingIdByMigrationDingIdResponseBody(TeaModel):
    def __init__(
        self,
        ding_id: str = None,
    ):
        # dingId
        self.ding_id = ding_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_id is not None:
            result['dingId'] = self.ding_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingId') is not None:
            self.ding_id = m.get('dingId')
        return self


class GetDingIdByMigrationDingIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDingIdByMigrationDingIdResponseBody = None,
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
            temp_model = GetDingIdByMigrationDingIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestDingIndexHeaders(TeaModel):
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


class GetLatestDingIndexResponseBody(TeaModel):
    def __init__(
        self,
        idx_carbon: float = None,
        idx_efficiency: float = None,
        idx_monthly_avg: float = None,
        idx_total: float = None,
        stat_date: str = None,
    ):
        # 绿色指数
        self.idx_carbon = idx_carbon
        # 效率指数
        self.idx_efficiency = idx_efficiency
        # 钉钉指数月均分
        self.idx_monthly_avg = idx_monthly_avg
        # 钉钉指数
        self.idx_total = idx_total
        # 日期
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idx_carbon is not None:
            result['idxCarbon'] = self.idx_carbon
        if self.idx_efficiency is not None:
            result['idxEfficiency'] = self.idx_efficiency
        if self.idx_monthly_avg is not None:
            result['idxMonthlyAvg'] = self.idx_monthly_avg
        if self.idx_total is not None:
            result['idxTotal'] = self.idx_total
        if self.stat_date is not None:
            result['statDate'] = self.stat_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idxCarbon') is not None:
            self.idx_carbon = m.get('idxCarbon')
        if m.get('idxEfficiency') is not None:
            self.idx_efficiency = m.get('idxEfficiency')
        if m.get('idxMonthlyAvg') is not None:
            self.idx_monthly_avg = m.get('idxMonthlyAvg')
        if m.get('idxTotal') is not None:
            self.idx_total = m.get('idxTotal')
        if m.get('statDate') is not None:
            self.stat_date = m.get('statDate')
        return self


class GetLatestDingIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLatestDingIndexResponseBody = None,
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
            temp_model = GetLatestDingIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMigrationDingIdByDingIdHeaders(TeaModel):
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


class GetMigrationDingIdByDingIdRequest(TeaModel):
    def __init__(
        self,
        ding_id: str = None,
    ):
        # dingId
        self.ding_id = ding_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_id is not None:
            result['dingId'] = self.ding_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingId') is not None:
            self.ding_id = m.get('dingId')
        return self


class GetMigrationDingIdByDingIdResponseBody(TeaModel):
    def __init__(
        self,
        migration_ding_id_list: Dict[str, Any] = None,
    ):
        # migrationDingIdList
        self.migration_ding_id_list = migration_ding_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_ding_id_list is not None:
            result['migrationDingIdList'] = self.migration_ding_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationDingIdList') is not None:
            self.migration_ding_id_list = m.get('migrationDingIdList')
        return self


class GetMigrationDingIdByDingIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMigrationDingIdByDingIdResponseBody = None,
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
            temp_model = GetMigrationDingIdByDingIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMigrationUnionIdByUnionIdHeaders(TeaModel):
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


class GetMigrationUnionIdByUnionIdRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # unionId
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetMigrationUnionIdByUnionIdResponseBody(TeaModel):
    def __init__(
        self,
        migration_union_id_list: Dict[str, Any] = None,
    ):
        # migrationUnionIdList
        self.migration_union_id_list = migration_union_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_union_id_list is not None:
            result['migrationUnionIdList'] = self.migration_union_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationUnionIdList') is not None:
            self.migration_union_id_list = m.get('migrationUnionIdList')
        return self


class GetMigrationUnionIdByUnionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMigrationUnionIdByUnionIdResponseBody = None,
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
            temp_model = GetMigrationUnionIdByUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgAuthInfoHeaders(TeaModel):
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


class GetOrgAuthInfoRequest(TeaModel):
    def __init__(
        self,
        target_corp_id: str = None,
    ):
        # 需要获取的企业认证信息的企业corpId
        self.target_corp_id = target_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_corp_id is not None:
            result['targetCorpId'] = self.target_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCorpId') is not None:
            self.target_corp_id = m.get('targetCorpId')
        return self


class GetOrgAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        auth_level: int = None,
        legal_person: str = None,
        license_org_name: str = None,
        license_url: str = None,
        org_name: str = None,
        organization_code: str = None,
        registration_num: str = None,
        unified_social_credit: str = None,
    ):
        # 认证等级 1高级认证 2中级认证
        self.auth_level = auth_level
        # 法人
        self.legal_person = legal_person
        # 提交企业认证时营业执照上面的企业名称
        self.license_org_name = license_org_name
        # 营业执照url
        self.license_url = license_url
        # 企业在钉钉通讯录的名称
        self.org_name = org_name
        # 组织机构代码证号（格式11111111-1）
        self.organization_code = organization_code
        # 营业执照注册号（一般15位）
        self.registration_num = registration_num
        # 社会统一信用代码（固定18位）
        self.unified_social_credit = unified_social_credit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_level is not None:
            result['authLevel'] = self.auth_level
        if self.legal_person is not None:
            result['legalPerson'] = self.legal_person
        if self.license_org_name is not None:
            result['licenseOrgName'] = self.license_org_name
        if self.license_url is not None:
            result['licenseUrl'] = self.license_url
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.organization_code is not None:
            result['organizationCode'] = self.organization_code
        if self.registration_num is not None:
            result['registrationNum'] = self.registration_num
        if self.unified_social_credit is not None:
            result['unifiedSocialCredit'] = self.unified_social_credit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authLevel') is not None:
            self.auth_level = m.get('authLevel')
        if m.get('legalPerson') is not None:
            self.legal_person = m.get('legalPerson')
        if m.get('licenseOrgName') is not None:
            self.license_org_name = m.get('licenseOrgName')
        if m.get('licenseUrl') is not None:
            self.license_url = m.get('licenseUrl')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('organizationCode') is not None:
            self.organization_code = m.get('organizationCode')
        if m.get('registrationNum') is not None:
            self.registration_num = m.get('registrationNum')
        if m.get('unifiedSocialCredit') is not None:
            self.unified_social_credit = m.get('unifiedSocialCredit')
        return self


class GetOrgAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrgAuthInfoResponseBody = None,
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
            temp_model = GetOrgAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranslateFileJobResultHeaders(TeaModel):
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


class GetTranslateFileJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 异步转译任务id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self


class GetTranslateFileJobResultResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        url: str = None,
    ):
        # 0 任务进行中 1 任务处理成功 2 任务处理失败
        self.status = status
        # 文件内容转译成功后的url，需要用户通过oauth2授权登录在用户侧打开
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetTranslateFileJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTranslateFileJobResultResponseBody = None,
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
            temp_model = GetTranslateFileJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnionIdByMigrationUnionIdHeaders(TeaModel):
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


class GetUnionIdByMigrationUnionIdRequest(TeaModel):
    def __init__(
        self,
        migration_union_id: str = None,
    ):
        # migrationUnionId
        self.migration_union_id = migration_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_union_id is not None:
            result['migrationUnionId'] = self.migration_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationUnionId') is not None:
            self.migration_union_id = m.get('migrationUnionId')
        return self


class GetUnionIdByMigrationUnionIdResponseBody(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # unionId
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetUnionIdByMigrationUnionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUnionIdByMigrationUnionIdResponseBody = None,
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
            temp_model = GetUnionIdByMigrationUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserHeaders(TeaModel):
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


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        email: str = None,
        mobile: str = None,
        nick: str = None,
        open_id: str = None,
        state_code: str = None,
        union_id: str = None,
    ):
        # 头像url
        self.avatar_url = avatar_url
        # 个人邮箱
        self.email = email
        # 手机号
        self.mobile = mobile
        # 昵称
        self.nick = nick
        # openId
        self.open_id = open_id
        # 手机号对应的国家号
        self.state_code = state_code
        # unionId
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.email is not None:
            result['email'] = self.email
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.nick is not None:
            result['nick'] = self.nick
        if self.open_id is not None:
            result['openId'] = self.open_id
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('nick') is not None:
            self.nick = m.get('nick')
        if m.get('openId') is not None:
            self.open_id = m.get('openId')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserCardHolderListHeaders(TeaModel):
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


class GetUserCardHolderListRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
    ):
        # 每页返回个数
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class GetUserCardHolderListResponseBodyList(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        card_id: str = None,
        extension: Dict[str, Any] = None,
        industry_name: str = None,
        introduce: str = None,
        name: str = None,
        org_name: str = None,
        template_id: str = None,
        title: str = None,
    ):
        # 头像
        self.avatar_url = avatar_url
        # 名片ID
        self.card_id = card_id
        # 扩展信息
        self.extension = extension
        # 行业名称
        self.industry_name = industry_name
        # 个人介绍
        self.introduce = introduce
        # 名字
        self.name = name
        # 组织名称
        self.org_name = org_name
        # 模板ID
        self.template_id = template_id
        # 职位
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.card_id is not None:
            result['cardId'] = self.card_id
        if self.extension is not None:
            result['extension'] = self.extension
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('cardId') is not None:
            self.card_id = m.get('cardId')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetUserCardHolderListResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[GetUserCardHolderListResponseBodyList] = None,
        next_token: int = None,
        total_count: int = None,
    ):
        # 是否还有数据
        self.has_more = has_more
        # 名片夹列表
        self.list = list
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetUserCardHolderListResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetUserCardHolderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserCardHolderListResponseBody = None,
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
            temp_model = GetUserCardHolderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvCardEventPushHeaders(TeaModel):
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


class IsvCardEventPushRequest(TeaModel):
    def __init__(
        self,
        event_params: Dict[str, Any] = None,
        event_type: str = None,
        isv_card_id: str = None,
        isv_token: str = None,
        isv_uid: str = None,
    ):
        # 事件参数
        self.event_params = event_params
        # 事件类型
        self.event_type = event_type
        # ISV名片ID
        self.isv_card_id = isv_card_id
        # ISV用户TOKEN
        self.isv_token = isv_token
        # ISV用户iD
        self.isv_uid = isv_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_params is not None:
            result['eventParams'] = self.event_params
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.isv_card_id is not None:
            result['isvCardId'] = self.isv_card_id
        if self.isv_token is not None:
            result['isvToken'] = self.isv_token
        if self.isv_uid is not None:
            result['isvUid'] = self.isv_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventParams') is not None:
            self.event_params = m.get('eventParams')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('isvCardId') is not None:
            self.isv_card_id = m.get('isvCardId')
        if m.get('isvToken') is not None:
            self.isv_token = m.get('isvToken')
        if m.get('isvUid') is not None:
            self.isv_uid = m.get('isvUid')
        return self


class IsvCardEventPushResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 执行结果
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class IsvCardEventPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IsvCardEventPushResponseBody = None,
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
            temp_model = IsvCardEventPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContactHideSettingsHeaders(TeaModel):
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


class ListContactHideSettingsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListContactHideSettingsResponseBodyList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        exclude_dept_ids: List[int] = None,
        exclude_staff_ids: List[str] = None,
        exclude_tag_ids: List[int] = None,
        id: int = None,
        name: str = None,
        object_dept_ids: List[int] = None,
        object_staff_ids: List[str] = None,
        object_tag_ids: List[int] = None,
    ):
        # 规则是否生效
        self.active = active
        # 设置描述
        self.description = description
        # 白名单部门列表
        self.exclude_dept_ids = exclude_dept_ids
        # 白名单用户列表
        self.exclude_staff_ids = exclude_staff_ids
        # 白名单角色列表
        self.exclude_tag_ids = exclude_tag_ids
        # settingId
        self.id = id
        # 设置名称
        self.name = name
        # 要隐藏的部门列表
        self.object_dept_ids = object_dept_ids
        # 要隐藏的员工列表
        self.object_staff_ids = object_staff_ids
        # 要影藏的角色列表
        self.object_tag_ids = object_tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.exclude_dept_ids is not None:
            result['excludeDeptIds'] = self.exclude_dept_ids
        if self.exclude_staff_ids is not None:
            result['excludeStaffIds'] = self.exclude_staff_ids
        if self.exclude_tag_ids is not None:
            result['excludeTagIds'] = self.exclude_tag_ids
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.object_dept_ids is not None:
            result['objectDeptIds'] = self.object_dept_ids
        if self.object_staff_ids is not None:
            result['objectStaffIds'] = self.object_staff_ids
        if self.object_tag_ids is not None:
            result['objectTagIds'] = self.object_tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('excludeDeptIds') is not None:
            self.exclude_dept_ids = m.get('excludeDeptIds')
        if m.get('excludeStaffIds') is not None:
            self.exclude_staff_ids = m.get('excludeStaffIds')
        if m.get('excludeTagIds') is not None:
            self.exclude_tag_ids = m.get('excludeTagIds')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectDeptIds') is not None:
            self.object_dept_ids = m.get('objectDeptIds')
        if m.get('objectStaffIds') is not None:
            self.object_staff_ids = m.get('objectStaffIds')
        if m.get('objectTagIds') is not None:
            self.object_tag_ids = m.get('objectTagIds')
        return self


class ListContactHideSettingsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[ListContactHideSettingsResponseBodyList] = None,
        next_token: int = None,
    ):
        # 是否还有数据
        self.has_more = has_more
        # 设置列表
        self.list = list
        # 下一次拉取数据时的offset
        self.next_token = next_token

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListContactHideSettingsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListContactHideSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListContactHideSettingsResponseBody = None,
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
            temp_model = ListContactHideSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmpAttributeVisibilityHeaders(TeaModel):
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


class ListEmpAttributeVisibilityRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListEmpAttributeVisibilityResponseBodyList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        exclude_dept_ids: List[int] = None,
        exclude_staff_ids: List[str] = None,
        exclude_tag_ids: List[int] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hide_fields: List[str] = None,
        id: int = None,
        name: str = None,
        object_dept_ids: List[int] = None,
        object_staff_ids: List[str] = None,
        object_tag_ids: List[int] = None,
    ):
        # 是否生效
        self.active = active
        # 设置描述
        self.description = description
        # 白名单部门id列表
        self.exclude_dept_ids = exclude_dept_ids
        # 白名单用户id列表
        self.exclude_staff_ids = exclude_staff_ids
        # 白名单角色id列表
        self.exclude_tag_ids = exclude_tag_ids
        # 设置时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 隐藏的字段id列表
        self.hide_fields = hide_fields
        # id
        self.id = id
        # 名称
        self.name = name
        # 被查看的部门id列表
        self.object_dept_ids = object_dept_ids
        # 被查看的用户id列表
        self.object_staff_ids = object_staff_ids
        # 被查看的角色id列表
        self.object_tag_ids = object_tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.exclude_dept_ids is not None:
            result['excludeDeptIds'] = self.exclude_dept_ids
        if self.exclude_staff_ids is not None:
            result['excludeStaffIds'] = self.exclude_staff_ids
        if self.exclude_tag_ids is not None:
            result['excludeTagIds'] = self.exclude_tag_ids
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hide_fields is not None:
            result['hideFields'] = self.hide_fields
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.object_dept_ids is not None:
            result['objectDeptIds'] = self.object_dept_ids
        if self.object_staff_ids is not None:
            result['objectStaffIds'] = self.object_staff_ids
        if self.object_tag_ids is not None:
            result['objectTagIds'] = self.object_tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('excludeDeptIds') is not None:
            self.exclude_dept_ids = m.get('excludeDeptIds')
        if m.get('excludeStaffIds') is not None:
            self.exclude_staff_ids = m.get('excludeStaffIds')
        if m.get('excludeTagIds') is not None:
            self.exclude_tag_ids = m.get('excludeTagIds')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hideFields') is not None:
            self.hide_fields = m.get('hideFields')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectDeptIds') is not None:
            self.object_dept_ids = m.get('objectDeptIds')
        if m.get('objectStaffIds') is not None:
            self.object_staff_ids = m.get('objectStaffIds')
        if m.get('objectTagIds') is not None:
            self.object_tag_ids = m.get('objectTagIds')
        return self


class ListEmpAttributeVisibilityResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[ListEmpAttributeVisibilityResponseBodyList] = None,
        next_cursor: int = None,
    ):
        # 是否还有数据
        self.has_more = has_more
        # 设置列表
        self.list = list
        # 下一次拉取时的offset
        self.next_cursor = next_cursor

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEmpAttributeVisibilityResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        return self


class ListEmpAttributeVisibilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEmpAttributeVisibilityResponseBody = None,
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
            temp_model = ListEmpAttributeVisibilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmpLeaveRecordsHeaders(TeaModel):
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


class ListEmpLeaveRecordsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        start_time: str = None,
    ):
        # 结束时间，YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339)
        self.end_time = end_time
        # 分页大小
        self.max_results = max_results
        # 分页token
        self.next_token = next_token
        # 开始时间，YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339)
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListEmpLeaveRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        leave_reason: str = None,
        leave_time: str = None,
        mobile: str = None,
        name: str = None,
        state_code: str = None,
        user_id: str = None,
    ):
        # 离职原因(oapi-开放平台删除，cancel-注销，leave-主动离职，unknown-未知原因，delete-管理员删除）
        self.leave_reason = leave_reason
        # 离职时间
        self.leave_time = leave_time
        # 手机号码
        self.mobile = mobile
        # 员工名称
        self.name = name
        # 国际电话区号
        self.state_code = state_code
        # 员工userid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.leave_reason is not None:
            result['leaveReason'] = self.leave_reason
        if self.leave_time is not None:
            result['leaveTime'] = self.leave_time
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('leaveReason') is not None:
            self.leave_reason = m.get('leaveReason')
        if m.get('leaveTime') is not None:
            self.leave_time = m.get('leaveTime')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListEmpLeaveRecordsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        records: List[ListEmpLeaveRecordsResponseBodyRecords] = None,
    ):
        # 分页token
        self.next_token = next_token
        # 离职记录列表
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ListEmpLeaveRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListEmpLeaveRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEmpLeaveRecordsResponseBody = None,
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
            temp_model = ListEmpLeaveRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManagementGroupsHeaders(TeaModel):
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


class ListManagementGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 开始读取的位置
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListManagementGroupsResponseBodyGroupsMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class ListManagementGroupsResponseBodyGroupsScope(TeaModel):
    def __init__(
        self,
        dept_ids: List[int] = None,
        scope_type: int = None,
    ):
        # 部门列表，只在scopeType=3 生效
        self.dept_ids = dept_ids
        # 1
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        return self


class ListManagementGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        members: List[ListManagementGroupsResponseBodyGroupsMembers] = None,
        resource_ids: List[str] = None,
        scope: ListManagementGroupsResponseBodyGroupsScope = None,
    ):
        # 管理组id
        self.group_id = group_id
        # 管理组名
        self.group_name = group_name
        # 成员
        self.members = members
        # 资源列表
        self.resource_ids = resource_ids
        # 管理范围
        self.scope = scope

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = ListManagementGroupsResponseBodyGroupsMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('scope') is not None:
            temp_model = ListManagementGroupsResponseBodyGroupsScope()
            self.scope = temp_model.from_map(m['scope'])
        return self


class ListManagementGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[ListManagementGroupsResponseBodyGroups] = None,
        has_more: bool = None,
        next_token: int = None,
    ):
        # 管理组列表
        self.groups = groups
        # 是否有下一页
        self.has_more = has_more
        # 下一次读取的位置
        self.next_token = next_token

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = ListManagementGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListManagementGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListManagementGroupsResponseBody = None,
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
            temp_model = ListManagementGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOwnedOrgByStaffIdHeaders(TeaModel):
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


class ListOwnedOrgByStaffIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListOwnedOrgByStaffIdResponseBodyOrgList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
    ):
        # corpId
        self.corp_id = corp_id
        # corpName
        self.corp_name = corp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.corp_name is not None:
            result['corpName'] = self.corp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        return self


class ListOwnedOrgByStaffIdResponseBody(TeaModel):
    def __init__(
        self,
        org_list: List[ListOwnedOrgByStaffIdResponseBodyOrgList] = None,
    ):
        # 组织列表
        self.org_list = org_list

    def validate(self):
        if self.org_list:
            for k in self.org_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['orgList'] = []
        if self.org_list is not None:
            for k in self.org_list:
                result['orgList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.org_list = []
        if m.get('orgList') is not None:
            for k in m.get('orgList'):
                temp_model = ListOwnedOrgByStaffIdResponseBodyOrgList()
                self.org_list.append(temp_model.from_map(k))
        return self


class ListOwnedOrgByStaffIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOwnedOrgByStaffIdResponseBody = None,
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
            temp_model = ListOwnedOrgByStaffIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSeniorSettingsHeaders(TeaModel):
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


class ListSeniorSettingsRequest(TeaModel):
    def __init__(
        self,
        senior_staff_id: str = None,
    ):
        self.senior_staff_id = senior_staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.senior_staff_id is not None:
            result['seniorStaffId'] = self.senior_staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('seniorStaffId') is not None:
            self.senior_staff_id = m.get('seniorStaffId')
        return self


class ListSeniorSettingsResponseBodySeniorWhiteList(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSeniorSettingsResponseBody(TeaModel):
    def __init__(
        self,
        protect_scenes: List[str] = None,
        senior_staff_id: str = None,
        senior_white_list: List[ListSeniorSettingsResponseBodySeniorWhiteList] = None,
    ):
        self.protect_scenes = protect_scenes
        # Id of the request
        self.senior_staff_id = senior_staff_id
        self.senior_white_list = senior_white_list

    def validate(self):
        if self.senior_white_list:
            for k in self.senior_white_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_scenes is not None:
            result['protectScenes'] = self.protect_scenes
        if self.senior_staff_id is not None:
            result['seniorStaffId'] = self.senior_staff_id
        result['seniorWhiteList'] = []
        if self.senior_white_list is not None:
            for k in self.senior_white_list:
                result['seniorWhiteList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protectScenes') is not None:
            self.protect_scenes = m.get('protectScenes')
        if m.get('seniorStaffId') is not None:
            self.senior_staff_id = m.get('seniorStaffId')
        self.senior_white_list = []
        if m.get('seniorWhiteList') is not None:
            for k in m.get('seniorWhiteList'):
                temp_model = ListSeniorSettingsResponseBodySeniorWhiteList()
                self.senior_white_list.append(temp_model.from_map(k))
        return self


class ListSeniorSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSeniorSettingsResponseBody = None,
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
            temp_model = ListSeniorSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MultiOrgPermissionGrantHeaders(TeaModel):
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


class MultiOrgPermissionGrantRequest(TeaModel):
    def __init__(
        self,
        grant_dept_id_list: List[int] = None,
        join_corp_id: str = None,
    ):
        # 被授权的部门，如果不填则默认全组织
        self.grant_dept_id_list = grant_dept_id_list
        # 授权加入的组织corpId
        self.join_corp_id = join_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_dept_id_list is not None:
            result['grantDeptIdList'] = self.grant_dept_id_list
        if self.join_corp_id is not None:
            result['joinCorpId'] = self.join_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grantDeptIdList') is not None:
            self.grant_dept_id_list = m.get('grantDeptIdList')
        if m.get('joinCorpId') is not None:
            self.join_corp_id = m.get('joinCorpId')
        return self


class MultiOrgPermissionGrantResponse(TeaModel):
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


class QueryResourceManagementMembersHeaders(TeaModel):
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


class QueryResourceManagementMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class QueryResourceManagementMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[QueryResourceManagementMembersResponseBodyMembers] = None,
    ):
        # 可管理资源的成员
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = QueryResourceManagementMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        return self


class QueryResourceManagementMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryResourceManagementMembersResponseBody = None,
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
            temp_model = QueryResourceManagementMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatusHeaders(TeaModel):
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


class QueryStatusRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryStatusResponseBody(TeaModel):
    def __init__(
        self,
        disable: bool = None,
    ):
        # disable
        self.disable = disable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable is not None:
            result['disable'] = self.disable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        return self


class QueryStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryStatusResponseBody = None,
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
            temp_model = QueryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserManagementResourcesHeaders(TeaModel):
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


class QueryUserManagementResourcesResponseBody(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
    ):
        # 资源列表
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        return self


class QueryUserManagementResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUserManagementResourcesResponseBody = None,
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
            temp_model = QueryUserManagementResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDepartmentHeaders(TeaModel):
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


class SearchDepartmentRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        query_word: str = None,
        size: int = None,
    ):
        # 分页查询锚点
        self.offset = offset
        # 部门名称或者部门名称拼音
        self.query_word = query_word
        # 分页长度
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.query_word is not None:
            result['queryWord'] = self.query_word
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('queryWord') is not None:
            self.query_word = m.get('queryWord')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class SearchDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[int] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.list = list
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.list is not None:
            result['list'] = self.list
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('list') is not None:
            self.list = m.get('list')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class SearchDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchDepartmentResponseBody = None,
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
            temp_model = SearchDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchUserHeaders(TeaModel):
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


class SearchUserRequest(TeaModel):
    def __init__(
        self,
        full_match_field: int = None,
        offset: int = None,
        query_word: str = None,
        size: int = None,
    ):
        # 精确匹配的字段。1：匹配用户名称。不填则为模糊匹配
        self.full_match_field = full_match_field
        # 分页查询锚点
        self.offset = offset
        # 用户名称、名称拼音或英文名称
        self.query_word = query_word
        # 分页长度
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_match_field is not None:
            result['fullMatchField'] = self.full_match_field
        if self.offset is not None:
            result['offset'] = self.offset
        if self.query_word is not None:
            result['queryWord'] = self.query_word
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fullMatchField') is not None:
            self.full_match_field = m.get('fullMatchField')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('queryWord') is not None:
            self.query_word = m.get('queryWord')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class SearchUserResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[str] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.has_more = has_more
        self.list = list
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.list is not None:
            result['list'] = self.list
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('list') is not None:
            self.list = m.get('list')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class SearchUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchUserResponseBody = None,
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
            temp_model = SearchUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SeparateBranchOrgHeaders(TeaModel):
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


class SeparateBranchOrgRequest(TeaModel):
    def __init__(
        self,
        attach_dept_id: int = None,
    ):
        self.attach_dept_id = attach_dept_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_dept_id is not None:
            result['attachDeptId'] = self.attach_dept_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachDeptId') is not None:
            self.attach_dept_id = m.get('attachDeptId')
        return self


class SeparateBranchOrgResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 处理结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class SeparateBranchOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SeparateBranchOrgResponseBody = None,
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
            temp_model = SeparateBranchOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDisableHeaders(TeaModel):
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


class SetDisableRequest(TeaModel):
    def __init__(
        self,
        reason: str = None,
        user_id: str = None,
    ):
        # reason
        self.reason = reason
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['reason'] = self.reason
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SetDisableResponse(TeaModel):
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


class SetEnableHeaders(TeaModel):
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


class SetEnableRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SetEnableResponse(TeaModel):
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


class SignOutHeaders(TeaModel):
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


class SignOutRequest(TeaModel):
    def __init__(
        self,
        reason: str = None,
        user_id: str = None,
    ):
        self.reason = reason
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['reason'] = self.reason
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SignOutResponse(TeaModel):
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


class SortUserHeaders(TeaModel):
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


class SortUserRequest(TeaModel):
    def __init__(
        self,
        sort_type: int = None,
        user_id_list: List[str] = None,
    ):
        # 0 根据姓名拼音升序排列 1 根据姓名拼音降序排列
        self.sort_type = sort_type
        # 用户id列表
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_type is not None:
            result['sortType'] = self.sort_type
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sortType') is not None:
            self.sort_type = m.get('sortType')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        return self


class SortUserResponseBody(TeaModel):
    def __init__(
        self,
        user_id_list: List[str] = None,
    ):
        # userIdList
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        return self


class SortUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SortUserResponseBody = None,
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
            temp_model = SortUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformToExclusiveAccountHeaders(TeaModel):
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


class TransformToExclusiveAccountRequest(TeaModel):
    def __init__(
        self,
        idp_ding_talk: bool = None,
        init_password: str = None,
        login_id: str = None,
        transform_type: str = None,
        user_id: str = None,
    ):
        # idpDingTalk
        self.idp_ding_talk = idp_ding_talk
        # initPassword
        self.init_password = init_password
        # loginId
        self.login_id = login_id
        # transformType
        self.transform_type = transform_type
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_ding_talk is not None:
            result['idpDingTalk'] = self.idp_ding_talk
        if self.init_password is not None:
            result['initPassword'] = self.init_password
        if self.login_id is not None:
            result['loginId'] = self.login_id
        if self.transform_type is not None:
            result['transformType'] = self.transform_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idpDingTalk') is not None:
            self.idp_ding_talk = m.get('idpDingTalk')
        if m.get('initPassword') is not None:
            self.init_password = m.get('initPassword')
        if m.get('loginId') is not None:
            self.login_id = m.get('loginId')
        if m.get('transformType') is not None:
            self.transform_type = m.get('transformType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class TransformToExclusiveAccountResponse(TeaModel):
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


class TranslateFileHeaders(TeaModel):
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


class TranslateFileRequest(TeaModel):
    def __init__(
        self,
        medias: Dict[str, str] = None,
        output_file_name: str = None,
        union_id: str = None,
    ):
        # key为钉盘文件mediaId，#号开头。只支持xlsx，xls，csv，txt文件。 value为文件名，包含文件扩展名。 不超过20个文件，可以调用单步文件上传接口获取。
        self.medias = medias
        # 若medias中文件个数大于1，则该字段必填。 转译完打包的文件名，不需带后缀。钉钉后台会打包成zip压缩文件，并自动拼接上.zip后缀。
        self.output_file_name = output_file_name
        # unionId
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medias is not None:
            result['medias'] = self.medias
        if self.output_file_name is not None:
            result['outputFileName'] = self.output_file_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('medias') is not None:
            self.medias = m.get('medias')
        if m.get('outputFileName') is not None:
            self.output_file_name = m.get('outputFileName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class TranslateFileResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 异步转译任务id，最大长度为64字符
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self


class TranslateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TranslateFileResponseBody = None,
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
            temp_model = TranslateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBranchAttributesInCooperateHeaders(TeaModel):
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


class UpdateBranchAttributesInCooperateRequestBody(TeaModel):
    def __init__(
        self,
        branch_corp_id: str = None,
        link_dept_id: int = None,
        union_root_name: str = None,
    ):
        # 分支的企业ID
        self.branch_corp_id = branch_corp_id
        # 挂载节点部门ID
        self.link_dept_id = link_dept_id
        # （分支/合作伙伴）在（集团/合作空间）的别名
        self.union_root_name = union_root_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_corp_id is not None:
            result['branchCorpId'] = self.branch_corp_id
        if self.link_dept_id is not None:
            result['linkDeptId'] = self.link_dept_id
        if self.union_root_name is not None:
            result['unionRootName'] = self.union_root_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branchCorpId') is not None:
            self.branch_corp_id = m.get('branchCorpId')
        if m.get('linkDeptId') is not None:
            self.link_dept_id = m.get('linkDeptId')
        if m.get('unionRootName') is not None:
            self.union_root_name = m.get('unionRootName')
        return self


class UpdateBranchAttributesInCooperateRequest(TeaModel):
    def __init__(
        self,
        body: List[UpdateBranchAttributesInCooperateRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateBranchAttributesInCooperateRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class UpdateBranchAttributesInCooperateResponse(TeaModel):
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


class UpdateBranchVisibleSettingInCooperateHeaders(TeaModel):
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


class UpdateBranchVisibleSettingInCooperateRequestBody(TeaModel):
    def __init__(
        self,
        branch_corp_id: str = None,
        open: bool = None,
        type: int = None,
        visible_branch_corp_ids: List[str] = None,
        visible_dept_ids: List[int] = None,
    ):
        # 分支的企业ID
        self.branch_corp_id = branch_corp_id
        # 是否开启 true：开启，false：关闭
        self.open = open
        # 设置可见性类型 0 ：在主干通讯录隐藏分支(其它分支包含主组织都看不到,额外设置可以看到) 1 ： 仅可见分支所在部门(只能看到自己企业加入的成员，额外设置可以看到其它成员)
        self.type = type
        # 设置例外的加入合作空间/关联组织的分支企业CorpId列表
        self.visible_branch_corp_ids = visible_branch_corp_ids
        # 设置例外的部门ID列表
        self.visible_dept_ids = visible_dept_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_corp_id is not None:
            result['branchCorpId'] = self.branch_corp_id
        if self.open is not None:
            result['open'] = self.open
        if self.type is not None:
            result['type'] = self.type
        if self.visible_branch_corp_ids is not None:
            result['visibleBranchCorpIds'] = self.visible_branch_corp_ids
        if self.visible_dept_ids is not None:
            result['visibleDeptIds'] = self.visible_dept_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branchCorpId') is not None:
            self.branch_corp_id = m.get('branchCorpId')
        if m.get('open') is not None:
            self.open = m.get('open')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('visibleBranchCorpIds') is not None:
            self.visible_branch_corp_ids = m.get('visibleBranchCorpIds')
        if m.get('visibleDeptIds') is not None:
            self.visible_dept_ids = m.get('visibleDeptIds')
        return self


class UpdateBranchVisibleSettingInCooperateRequest(TeaModel):
    def __init__(
        self,
        body: List[UpdateBranchVisibleSettingInCooperateRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateBranchVisibleSettingInCooperateRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class UpdateBranchVisibleSettingInCooperateResponse(TeaModel):
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


class UpdateContactHideSettingHeaders(TeaModel):
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


class UpdateContactHideSettingRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        exclude_dept_ids: List[int] = None,
        exclude_staff_ids: List[str] = None,
        exclude_tag_ids: List[int] = None,
        id: int = None,
        name: str = None,
        object_dept_ids: List[int] = None,
        object_staff_ids: List[str] = None,
        object_tag_ids: List[int] = None,
    ):
        # 是否激活
        self.active = active
        # 设置描述信息
        self.description = description
        # 白名单部门列表
        self.exclude_dept_ids = exclude_dept_ids
        # 白名单员工列表
        self.exclude_staff_ids = exclude_staff_ids
        # 白名单角色列表
        self.exclude_tag_ids = exclude_tag_ids
        # settingId
        self.id = id
        # 设置名称
        self.name = name
        # 影藏部门列表
        self.object_dept_ids = object_dept_ids
        # 隐藏员工列表
        self.object_staff_ids = object_staff_ids
        # 影藏角色列表
        self.object_tag_ids = object_tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.exclude_dept_ids is not None:
            result['excludeDeptIds'] = self.exclude_dept_ids
        if self.exclude_staff_ids is not None:
            result['excludeStaffIds'] = self.exclude_staff_ids
        if self.exclude_tag_ids is not None:
            result['excludeTagIds'] = self.exclude_tag_ids
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.object_dept_ids is not None:
            result['objectDeptIds'] = self.object_dept_ids
        if self.object_staff_ids is not None:
            result['objectStaffIds'] = self.object_staff_ids
        if self.object_tag_ids is not None:
            result['objectTagIds'] = self.object_tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('excludeDeptIds') is not None:
            self.exclude_dept_ids = m.get('excludeDeptIds')
        if m.get('excludeStaffIds') is not None:
            self.exclude_staff_ids = m.get('excludeStaffIds')
        if m.get('excludeTagIds') is not None:
            self.exclude_tag_ids = m.get('excludeTagIds')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectDeptIds') is not None:
            self.object_dept_ids = m.get('objectDeptIds')
        if m.get('objectStaffIds') is not None:
            self.object_staff_ids = m.get('objectStaffIds')
        if m.get('objectTagIds') is not None:
            self.object_tag_ids = m.get('objectTagIds')
        return self


class UpdateContactHideSettingResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # settingId
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateContactHideSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateContactHideSettingResponseBody = None,
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
            temp_model = UpdateContactHideSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeptSettngTailFirstHeaders(TeaModel):
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


class UpdateDeptSettngTailFirstRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateDeptSettngTailFirstResponse(TeaModel):
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


class UpdateEmpAttrbuteVisibilitySettingHeaders(TeaModel):
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


class UpdateEmpAttrbuteVisibilitySettingRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        exclude_dept_ids: List[int] = None,
        exclude_staff_ids: List[str] = None,
        exclude_tag_ids: List[int] = None,
        hide_fields: List[str] = None,
        id: int = None,
        name: str = None,
        object_dept_ids: List[int] = None,
        object_staff_ids: List[str] = None,
        object_tag_ids: List[int] = None,
    ):
        # 是否生效
        self.active = active
        # 描述信息
        self.description = description
        # 例外部门id列表
        self.exclude_dept_ids = exclude_dept_ids
        # 例外员工id列表
        self.exclude_staff_ids = exclude_staff_ids
        # 例外角色id列表
        self.exclude_tag_ids = exclude_tag_ids
        # 隐藏字段id列表
        self.hide_fields = hide_fields
        # id
        self.id = id
        # 名称
        self.name = name
        # object部门id列表
        self.object_dept_ids = object_dept_ids
        # object员工id列表
        self.object_staff_ids = object_staff_ids
        # object角色id列表
        self.object_tag_ids = object_tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.exclude_dept_ids is not None:
            result['excludeDeptIds'] = self.exclude_dept_ids
        if self.exclude_staff_ids is not None:
            result['excludeStaffIds'] = self.exclude_staff_ids
        if self.exclude_tag_ids is not None:
            result['excludeTagIds'] = self.exclude_tag_ids
        if self.hide_fields is not None:
            result['hideFields'] = self.hide_fields
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.object_dept_ids is not None:
            result['objectDeptIds'] = self.object_dept_ids
        if self.object_staff_ids is not None:
            result['objectStaffIds'] = self.object_staff_ids
        if self.object_tag_ids is not None:
            result['objectTagIds'] = self.object_tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('excludeDeptIds') is not None:
            self.exclude_dept_ids = m.get('excludeDeptIds')
        if m.get('excludeStaffIds') is not None:
            self.exclude_staff_ids = m.get('excludeStaffIds')
        if m.get('excludeTagIds') is not None:
            self.exclude_tag_ids = m.get('excludeTagIds')
        if m.get('hideFields') is not None:
            self.hide_fields = m.get('hideFields')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectDeptIds') is not None:
            self.object_dept_ids = m.get('objectDeptIds')
        if m.get('objectStaffIds') is not None:
            self.object_staff_ids = m.get('objectStaffIds')
        if m.get('objectTagIds') is not None:
            self.object_tag_ids = m.get('objectTagIds')
        return self


class UpdateEmpAttrbuteVisibilitySettingResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # settingId
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateEmpAttrbuteVisibilitySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEmpAttrbuteVisibilitySettingResponseBody = None,
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
            temp_model = UpdateEmpAttrbuteVisibilitySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateManagementGroupHeaders(TeaModel):
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


class UpdateManagementGroupRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class UpdateManagementGroupRequestScope(TeaModel):
    def __init__(
        self,
        dept_ids: List[int] = None,
        scope_type: int = None,
    ):
        # 部门列表，只在scopeType=3 生效
        self.dept_ids = dept_ids
        # 范围类型
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        return self


class UpdateManagementGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        members: List[UpdateManagementGroupRequestMembers] = None,
        resource_ids: List[str] = None,
        scope: UpdateManagementGroupRequestScope = None,
    ):
        # 管理组名称
        self.group_name = group_name
        # 管理组成员
        self.members = members
        # 资源列表
        self.resource_ids = resource_ids
        self.scope = scope

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = UpdateManagementGroupRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('scope') is not None:
            temp_model = UpdateManagementGroupRequestScope()
            self.scope = temp_model.from_map(m['scope'])
        return self


class UpdateManagementGroupResponse(TeaModel):
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


class UpdateSeniorSettingHeaders(TeaModel):
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


class UpdateSeniorSettingRequest(TeaModel):
    def __init__(
        self,
        open: bool = None,
        permit_dept_ids: List[int] = None,
        permit_staff_ids: List[str] = None,
        permit_tag_ids: List[int] = None,
        protect_scenes: List[str] = None,
        senior_staff_id: str = None,
    ):
        self.open = open
        self.permit_dept_ids = permit_dept_ids
        self.permit_staff_ids = permit_staff_ids
        self.permit_tag_ids = permit_tag_ids
        self.protect_scenes = protect_scenes
        self.senior_staff_id = senior_staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open is not None:
            result['open'] = self.open
        if self.permit_dept_ids is not None:
            result['permitDeptIds'] = self.permit_dept_ids
        if self.permit_staff_ids is not None:
            result['permitStaffIds'] = self.permit_staff_ids
        if self.permit_tag_ids is not None:
            result['permitTagIds'] = self.permit_tag_ids
        if self.protect_scenes is not None:
            result['protectScenes'] = self.protect_scenes
        if self.senior_staff_id is not None:
            result['seniorStaffId'] = self.senior_staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('open') is not None:
            self.open = m.get('open')
        if m.get('permitDeptIds') is not None:
            self.permit_dept_ids = m.get('permitDeptIds')
        if m.get('permitStaffIds') is not None:
            self.permit_staff_ids = m.get('permitStaffIds')
        if m.get('permitTagIds') is not None:
            self.permit_tag_ids = m.get('permitTagIds')
        if m.get('protectScenes') is not None:
            self.protect_scenes = m.get('protectScenes')
        if m.get('seniorStaffId') is not None:
            self.senior_staff_id = m.get('seniorStaffId')
        return self


class UpdateSeniorSettingResponse(TeaModel):
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


class UpdateUserOwnnessHeaders(TeaModel):
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


class UpdateUserOwnnessRequest(TeaModel):
    def __init__(
        self,
        deleted_flag: int = None,
        end_time: int = None,
        id: int = None,
        ownenss_type: int = None,
        start_time: int = None,
    ):
        # 删除标记
        self.deleted_flag = deleted_flag
        # 结束时间戳（毫秒）
        self.end_time = end_time
        # 业务标志id
        self.id = id
        # 状态类型
        self.ownenss_type = ownenss_type
        # 开始时间戳（毫秒）
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_flag is not None:
            result['deletedFlag'] = self.deleted_flag
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.ownenss_type is not None:
            result['ownenssType'] = self.ownenss_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletedFlag') is not None:
            self.deleted_flag = m.get('deletedFlag')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ownenssType') is not None:
            self.ownenss_type = m.get('ownenssType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class UpdateUserOwnnessResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 业务标识id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateUserOwnnessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserOwnnessResponseBody = None,
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
            temp_model = UpdateUserOwnnessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


