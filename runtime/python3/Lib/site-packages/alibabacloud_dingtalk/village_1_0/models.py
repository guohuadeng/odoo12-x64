# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetDeptHeaders(TeaModel):
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


class GetDeptRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        sub_corp_id: str = None,
    ):
        # 通讯录语言(默认zh_CN另外支持en_US)
        self.language = language
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class GetDeptResponseBody(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        from_union_org: bool = None,
        order: int = None,
        parent_department_id: int = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 部门名称
        self.department_name = department_name
        # 部门是否来自关联组织
        self.from_union_org = from_union_org
        # 在父部门中的次序值
        self.order = order
        # 父部门id
        self.parent_department_id = parent_department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.from_union_org is not None:
            result['fromUnionOrg'] = self.from_union_org
        if self.order is not None:
            result['order'] = self.order
        if self.parent_department_id is not None:
            result['parentDepartmentId'] = self.parent_department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('fromUnionOrg') is not None:
            self.from_union_org = m.get('fromUnionOrg')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('parentDepartmentId') is not None:
            self.parent_department_id = m.get('parentDepartmentId')
        return self


class GetDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeptResponseBody = None,
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
            temp_model = GetDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResidentDeptHeaders(TeaModel):
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


class GetResidentDeptRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class GetResidentDeptResponseBody(TeaModel):
    def __init__(
        self,
        contact_type: str = None,
        department_id: int = None,
        department_name: str = None,
        dept_type: str = None,
        feature: str = None,
    ):
        # 通讯录架构类型
        self.contact_type = contact_type
        # 下属组织的部门ID
        self.department_id = department_id
        # 部门名称
        self.department_name = department_name
        # 部门类型
        self.dept_type = dept_type
        # 部门属性
        self.feature = feature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['contactType'] = self.contact_type
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.dept_type is not None:
            result['deptType'] = self.dept_type
        if self.feature is not None:
            result['feature'] = self.feature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactType') is not None:
            self.contact_type = m.get('contactType')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('deptType') is not None:
            self.dept_type = m.get('deptType')
        if m.get('feature') is not None:
            self.feature = m.get('feature')
        return self


class GetResidentDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResidentDeptResponseBody = None,
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
            temp_model = GetResidentDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResidentUserInfoHeaders(TeaModel):
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


class GetResidentUserInfoRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class GetResidentUserInfoResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        role_name: str = None,
        tag_code: str = None,
    ):
        # 标签id
        self.role_id = role_id
        # 标签名称
        self.role_name = role_name
        # 标签名称 tagCode
        self.tag_code = tag_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        return self


class GetResidentUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        feature: str = None,
        name: str = None,
        roles: List[GetResidentUserInfoResponseBodyRoles] = None,
        union_id: str = None,
        userid: str = None,
    ):
        # 员工特征
        self.feature = feature
        # 员工名字
        self.name = name
        # 标签列表
        self.roles = roles
        # 钉钉唯一标识
        self.union_id = union_id
        # 员工id
        self.userid = userid

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature is not None:
            result['feature'] = self.feature
        if self.name is not None:
            result['name'] = self.name
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feature') is not None:
            self.feature = m.get('feature')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = GetResidentUserInfoResponseBodyRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class GetResidentUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResidentUserInfoResponseBody = None,
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
            temp_model = GetResidentUserInfoResponseBody()
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


class GetUserRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        sub_corp_id: str = None,
    ):
        # 通讯录语言(默认zh_CN另外支持en_US)
        self.language = language
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class GetUserResponseBodyDepartmentOrderSet(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        order: int = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 员工在部门中的排序。
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class GetUserResponseBodyLeaderInDepartment(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        leader: bool = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 员工在对应的部门中是否领导
        self.leader = leader

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.leader is not None:
            result['leader'] = self.leader
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('leader') is not None:
            self.leader = m.get('leader')
        return self


class GetUserResponseBodyRoleList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # 角色组名称
        self.group_name = group_name
        # 角色id
        self.role_id = role_id
        # 角色名称
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class GetUserResponseBodyUnionEmpExtUnionEmpMapList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        staff_id: str = None,
    ):
        # 企业 id
        self.corp_id = corp_id
        # 员工 id
        self.staff_id = staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.staff_id is not None:
            result['staffId'] = self.staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')
        return self


class GetUserResponseBodyUnionEmpExt(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        staff_id: str = None,
        union_emp_map_list: List[GetUserResponseBodyUnionEmpExtUnionEmpMapList] = None,
    ):
        # 企业id
        self.corp_id = corp_id
        # 员工id
        self.staff_id = staff_id
        # 关联映射关系
        self.union_emp_map_list = union_emp_map_list

    def validate(self):
        if self.union_emp_map_list:
            for k in self.union_emp_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.staff_id is not None:
            result['staffId'] = self.staff_id
        result['unionEmpMapList'] = []
        if self.union_emp_map_list is not None:
            for k in self.union_emp_map_list:
                result['unionEmpMapList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')
        self.union_emp_map_list = []
        if m.get('unionEmpMapList') is not None:
            for k in m.get('unionEmpMapList'):
                temp_model = GetUserResponseBodyUnionEmpExtUnionEmpMapList()
                self.union_emp_map_list.append(temp_model.from_map(k))
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin: bool = None,
        boss: bool = None,
        department_id_list: List[int] = None,
        department_order_set: List[GetUserResponseBodyDepartmentOrderSet] = None,
        exclusive_account: bool = None,
        exclusive_account_type: str = None,
        extension: str = None,
        hired_date: int = None,
        job_number: str = None,
        leader_in_department: List[GetUserResponseBodyLeaderInDepartment] = None,
        manager_user_id: str = None,
        name: str = None,
        real_authed: bool = None,
        remark: str = None,
        role_list: List[GetUserResponseBodyRoleList] = None,
        senior: bool = None,
        title: str = None,
        union_emp_ext: GetUserResponseBodyUnionEmpExt = None,
        union_id: str = None,
        user_id: str = None,
        work_place: str = None,
    ):
        # 是否激活
        self.active = active
        # 是否管理员
        self.admin = admin
        # 是否老板
        self.boss = boss
        # 所属部门id列表
        self.department_id_list = department_id_list
        # 员工在对应的部门中的排序。
        self.department_order_set = department_order_set
        # 是否专属帐号
        self.exclusive_account = exclusive_account
        # 专属帐号类型：{sso: 企业自定义idp;dingtalk: 钉钉idp}
        self.exclusive_account_type = exclusive_account_type
        # 扩展属性，长度最大2000个字符。可以设置多种属性（手机上最多显示10个扩展属性，具体显示哪些属性，请到OA管理后台->设置->通讯录信息设置和OA管理后台->设置->手机端显示信息设置）。 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。示例： [工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)
        self.extension = extension
        # 入职时间，Unix时间戳，单位ms。
        self.hired_date = hired_date
        # 员工工号
        self.job_number = job_number
        # 员工在对应的部门中是否领导。
        self.leader_in_department = leader_in_department
        # 主管的ID，仅限企业内部开发调用
        self.manager_user_id = manager_user_id
        # 姓名
        self.name = name
        # 是否实名认证
        self.real_authed = real_authed
        # 备注
        self.remark = remark
        # 角色列表
        self.role_list = role_list
        # 是否高管
        self.senior = senior
        # 职位
        self.title = title
        # 关联信息
        self.union_emp_ext = union_emp_ext
        # 员工在当前开发者企业账号范围内的唯一标识
        self.union_id = union_id
        # 用户id
        self.user_id = user_id
        # 办公地点
        self.work_place = work_place

    def validate(self):
        if self.department_order_set:
            for k in self.department_order_set:
                if k:
                    k.validate()
        if self.leader_in_department:
            for k in self.leader_in_department:
                if k:
                    k.validate()
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()
        if self.union_emp_ext:
            self.union_emp_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.admin is not None:
            result['admin'] = self.admin
        if self.boss is not None:
            result['boss'] = self.boss
        if self.department_id_list is not None:
            result['departmentIdList'] = self.department_id_list
        result['departmentOrderSet'] = []
        if self.department_order_set is not None:
            for k in self.department_order_set:
                result['departmentOrderSet'].append(k.to_map() if k else None)
        if self.exclusive_account is not None:
            result['exclusiveAccount'] = self.exclusive_account
        if self.exclusive_account_type is not None:
            result['exclusiveAccountType'] = self.exclusive_account_type
        if self.extension is not None:
            result['extension'] = self.extension
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.job_number is not None:
            result['jobNumber'] = self.job_number
        result['leaderInDepartment'] = []
        if self.leader_in_department is not None:
            for k in self.leader_in_department:
                result['leaderInDepartment'].append(k.to_map() if k else None)
        if self.manager_user_id is not None:
            result['managerUserId'] = self.manager_user_id
        if self.name is not None:
            result['name'] = self.name
        if self.real_authed is not None:
            result['realAuthed'] = self.real_authed
        if self.remark is not None:
            result['remark'] = self.remark
        result['roleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['roleList'].append(k.to_map() if k else None)
        if self.senior is not None:
            result['senior'] = self.senior
        if self.title is not None:
            result['title'] = self.title
        if self.union_emp_ext is not None:
            result['unionEmpExt'] = self.union_emp_ext.to_map()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.work_place is not None:
            result['workPlace'] = self.work_place
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('admin') is not None:
            self.admin = m.get('admin')
        if m.get('boss') is not None:
            self.boss = m.get('boss')
        if m.get('departmentIdList') is not None:
            self.department_id_list = m.get('departmentIdList')
        self.department_order_set = []
        if m.get('departmentOrderSet') is not None:
            for k in m.get('departmentOrderSet'):
                temp_model = GetUserResponseBodyDepartmentOrderSet()
                self.department_order_set.append(temp_model.from_map(k))
        if m.get('exclusiveAccount') is not None:
            self.exclusive_account = m.get('exclusiveAccount')
        if m.get('exclusiveAccountType') is not None:
            self.exclusive_account_type = m.get('exclusiveAccountType')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')
        self.leader_in_department = []
        if m.get('leaderInDepartment') is not None:
            for k in m.get('leaderInDepartment'):
                temp_model = GetUserResponseBodyLeaderInDepartment()
                self.leader_in_department.append(temp_model.from_map(k))
        if m.get('managerUserId') is not None:
            self.manager_user_id = m.get('managerUserId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('realAuthed') is not None:
            self.real_authed = m.get('realAuthed')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        self.role_list = []
        if m.get('roleList') is not None:
            for k in m.get('roleList'):
                temp_model = GetUserResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('senior') is not None:
            self.senior = m.get('senior')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('unionEmpExt') is not None:
            temp_model = GetUserResponseBodyUnionEmpExt()
            self.union_emp_ext = temp_model.from_map(m['unionEmpExt'])
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workPlace') is not None:
            self.work_place = m.get('workPlace')
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


class GetUserByUnionIdHeaders(TeaModel):
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


class GetUserByUnionIdRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        sub_corp_id: str = None,
        union_id: str = None,
    ):
        # 通讯录语言(默认zh_CN另外支持en_US)
        self.language = language
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id
        # 人员 id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetUserByUnionIdResponseBody(TeaModel):
    def __init__(
        self,
        contact_type: int = None,
        user_id: str = None,
    ):
        # 联系类型，0表示企业内部员工，1表示企业外部联系人
        self.contact_type = contact_type
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['contactType'] = self.contact_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactType') is not None:
            self.contact_type = m.get('contactType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserByUnionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserByUnionIdResponseBody = None,
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
            temp_model = GetUserByUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVillageOrgInfoHeaders(TeaModel):
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


class GetVillageOrgInfoResponseBody(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_location: str = None,
        region_type: str = None,
    ):
        # 行政区ID
        self.region_id = region_id
        # 具体的企业区域位置信息
        self.region_location = region_location
        # 区域类型
        self.region_type = region_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.region_location is not None:
            result['regionLocation'] = self.region_location
        if self.region_type is not None:
            result['regionType'] = self.region_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regionLocation') is not None:
            self.region_location = m.get('regionLocation')
        if m.get('regionType') is not None:
            self.region_type = m.get('regionType')
        return self


class GetVillageOrgInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVillageOrgInfoResponseBody = None,
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
            temp_model = GetVillageOrgInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeptSimpleUsersHeaders(TeaModel):
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


class ListDeptSimpleUsersRequest(TeaModel):
    def __init__(
        self,
        contain_access_limit: bool = None,
        cursor: int = None,
        language: str = None,
        order_field: str = None,
        size: int = None,
        sub_corp_id: str = None,
    ):
        # containAccessLimit
        self.contain_access_limit = contain_access_limit
        # cursor
        self.cursor = cursor
        # language
        self.language = language
        # orderField
        self.order_field = order_field
        # size
        self.size = size
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_access_limit is not None:
            result['containAccessLimit'] = self.contain_access_limit
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.language is not None:
            result['language'] = self.language
        if self.order_field is not None:
            result['orderField'] = self.order_field
        if self.size is not None:
            result['size'] = self.size
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containAccessLimit') is not None:
            self.contain_access_limit = m.get('containAccessLimit')
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('orderField') is not None:
            self.order_field = m.get('orderField')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListDeptSimpleUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        # 用户姓名
        self.name = name
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListDeptSimpleUsersResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_cursor: int = None,
        total_count: int = None,
        user_list: List[ListDeptSimpleUsersResponseBodyUserList] = None,
    ):
        self.has_more = has_more
        self.next_cursor = next_cursor
        self.total_count = total_count
        # 用户列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = ListDeptSimpleUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListDeptSimpleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeptSimpleUsersResponseBody = None,
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
            temp_model = ListDeptSimpleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeptUserIdsHeaders(TeaModel):
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


class ListDeptUserIdsRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListDeptUserIdsResponseBody(TeaModel):
    def __init__(
        self,
        user_id_list: List[str] = None,
    ):
        # 用户ID列表
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


class ListDeptUserIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeptUserIdsResponseBody = None,
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
            temp_model = ListDeptUserIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeptUsersHeaders(TeaModel):
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


class ListDeptUsersRequest(TeaModel):
    def __init__(
        self,
        contain_access_limit: bool = None,
        cursor: int = None,
        language: str = None,
        order_field: str = None,
        size: int = None,
        sub_corp_id: str = None,
    ):
        # containAccessLimit
        self.contain_access_limit = contain_access_limit
        # cursor
        self.cursor = cursor
        # language
        self.language = language
        # orderField
        self.order_field = order_field
        # size
        self.size = size
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_access_limit is not None:
            result['containAccessLimit'] = self.contain_access_limit
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.language is not None:
            result['language'] = self.language
        if self.order_field is not None:
            result['orderField'] = self.order_field
        if self.size is not None:
            result['size'] = self.size
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containAccessLimit') is not None:
            self.contain_access_limit = m.get('containAccessLimit')
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('orderField') is not None:
            self.order_field = m.get('orderField')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListDeptUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        department_list: List[int] = None,
        job_number: str = None,
        name: str = None,
        union_id: str = None,
        user_id: str = None,
    ):
        self.active = active
        # 部门ID列表
        self.department_list = department_list
        self.job_number = job_number
        self.name = name
        # unionId
        self.union_id = union_id
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.department_list is not None:
            result['departmentList'] = self.department_list
        if self.job_number is not None:
            result['jobNumber'] = self.job_number
        if self.name is not None:
            result['name'] = self.name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('departmentList') is not None:
            self.department_list = m.get('departmentList')
        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListDeptUsersResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_cursor: int = None,
        user_list: List[ListDeptUsersResponseBodyUserList] = None,
    ):
        self.has_more = has_more
        self.next_cursor = next_cursor
        # 用户列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = ListDeptUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListDeptUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeptUsersResponseBody = None,
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
            temp_model = ListDeptUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParentByDeptHeaders(TeaModel):
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


class ListParentByDeptRequest(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        sub_corp_id: str = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListParentByDeptResponseBody(TeaModel):
    def __init__(
        self,
        department_id_list: List[int] = None,
    ):
        # 父部门ID列表
        self.department_id_list = department_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id_list is not None:
            result['departmentIdList'] = self.department_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIdList') is not None:
            self.department_id_list = m.get('departmentIdList')
        return self


class ListParentByDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListParentByDeptResponseBody = None,
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
            temp_model = ListParentByDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParentByUserHeaders(TeaModel):
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


class ListParentByUserRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
        user_id: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id
        # 用户userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListParentByUserResponseBody(TeaModel):
    def __init__(
        self,
        department_id_list: List[int] = None,
    ):
        # 上级部门ID列表
        self.department_id_list = department_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id_list is not None:
            result['departmentIdList'] = self.department_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIdList') is not None:
            self.department_id_list = m.get('departmentIdList')
        return self


class ListParentByUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListParentByUserResponseBody = None,
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
            temp_model = ListParentByUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResidentDeptUsersHeaders(TeaModel):
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


class ListResidentDeptUsersRequest(TeaModel):
    def __init__(
        self,
        cursor: int = None,
        role: str = None,
        size: int = None,
        sub_corp_id: str = None,
    ):
        # 游标，不传默认1
        self.cursor = cursor
        # 角色标签
        self.role = role
        # 大小
        self.size = size
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.role is not None:
            result['role'] = self.role
        if self.size is not None:
            result['size'] = self.size
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListResidentDeptUsersResponseBodyUserListRoles(TeaModel):
    def __init__(
        self,
        tag_code: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        # 标签名称 tagCode
        self.tag_code = tag_code
        # 标签id
        self.tag_id = tag_id
        # 标签名称
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.tag_id is not None:
            result['tagId'] = self.tag_id
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('tagId') is not None:
            self.tag_id = m.get('tagId')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class ListResidentDeptUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        feature: str = None,
        name: str = None,
        roles: List[ListResidentDeptUsersResponseBodyUserListRoles] = None,
        union_id: str = None,
        user_id: str = None,
    ):
        # 员工特征
        self.feature = feature
        # 员工名字
        self.name = name
        # 标签列表
        self.roles = roles
        # 钉钉唯一标识
        self.union_id = union_id
        # 员工id
        self.user_id = user_id

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature is not None:
            result['feature'] = self.feature
        if self.name is not None:
            result['name'] = self.name
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feature') is not None:
            self.feature = m.get('feature')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = ListResidentDeptUsersResponseBodyUserListRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListResidentDeptUsersResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_cursor: int = None,
        user_list: List[ListResidentDeptUsersResponseBodyUserList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # 下一个游标
        self.next_cursor = next_cursor
        # 用户列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = ListResidentDeptUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListResidentDeptUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResidentDeptUsersResponseBody = None,
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
            temp_model = ListResidentDeptUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResidentSubDeptsHeaders(TeaModel):
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


class ListResidentSubDeptsRequest(TeaModel):
    def __init__(
        self,
        cursor: int = None,
        size: int = None,
        sub_corp_id: str = None,
    ):
        # 游标，不传默认1
        self.cursor = cursor
        # 大小
        self.size = size
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.size is not None:
            result['size'] = self.size
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListResidentSubDeptsResponseBodyDepartmentList(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        super_department_id: int = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 组户名称
        self.department_name = department_name
        # 父部门ID
        self.super_department_id = super_department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.super_department_id is not None:
            result['superDepartmentId'] = self.super_department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('superDepartmentId') is not None:
            self.super_department_id = m.get('superDepartmentId')
        return self


class ListResidentSubDeptsResponseBody(TeaModel):
    def __init__(
        self,
        department_list: List[ListResidentSubDeptsResponseBodyDepartmentList] = None,
        has_more: bool = None,
        next_cursor: int = None,
        total: int = None,
    ):
        # 组户列表
        self.department_list = department_list
        # 是否还有记录
        self.has_more = has_more
        # 游标
        self.next_cursor = next_cursor
        # 总数
        self.total = total

    def validate(self):
        if self.department_list:
            for k in self.department_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['departmentList'] = []
        if self.department_list is not None:
            for k in self.department_list:
                result['departmentList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.department_list = []
        if m.get('departmentList') is not None:
            for k in m.get('departmentList'):
                temp_model = ListResidentSubDeptsResponseBodyDepartmentList()
                self.department_list.append(temp_model.from_map(k))
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListResidentSubDeptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResidentSubDeptsResponseBody = None,
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
            temp_model = ListResidentSubDeptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResidentUserInfosHeaders(TeaModel):
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


class ListResidentUserInfosRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
        user_ids: List[str] = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id
        # 用户id列表
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self


class ListResidentUserInfosShrinkRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
        user_ids_shrink: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id
        # 用户id列表
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        if self.user_ids_shrink is not None:
            result['userIds'] = self.user_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        if m.get('userIds') is not None:
            self.user_ids_shrink = m.get('userIds')
        return self


class ListResidentUserInfosResponseBodyUserListRoles(TeaModel):
    def __init__(
        self,
        tag_code: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        # 标签名称 tagCode
        self.tag_code = tag_code
        # 标签id
        self.tag_id = tag_id
        # 标签名称
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.tag_id is not None:
            result['tagId'] = self.tag_id
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('tagId') is not None:
            self.tag_id = m.get('tagId')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class ListResidentUserInfosResponseBodyUserList(TeaModel):
    def __init__(
        self,
        feature: str = None,
        roles: List[ListResidentUserInfosResponseBodyUserListRoles] = None,
        union_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 员工特征
        self.feature = feature
        # 标签列表
        self.roles = roles
        # 钉钉唯一标识
        self.union_id = union_id
        # 员工 ID
        self.user_id = user_id
        # 员工名字
        self.user_name = user_name

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature is not None:
            result['feature'] = self.feature
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feature') is not None:
            self.feature = m.get('feature')
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = ListResidentUserInfosResponseBodyUserListRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class ListResidentUserInfosResponseBody(TeaModel):
    def __init__(
        self,
        user_list: List[ListResidentUserInfosResponseBodyUserList] = None,
    ):
        # 员工信息列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = ListResidentUserInfosResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListResidentUserInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResidentUserInfosResponseBody = None,
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
            temp_model = ListResidentUserInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSimpleUsersByRoleHeaders(TeaModel):
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


class ListSimpleUsersByRoleRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        role_id: int = None,
        size: int = None,
        sub_corp_id: str = None,
    ):
        # 起始位置
        self.offset = offset
        # 角色ID
        self.role_id = role_id
        # 查询数量
        self.size = size
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.size is not None:
            result['size'] = self.size
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListSimpleUsersByRoleResponseBodyUserList(TeaModel):
    def __init__(
        self,
        job_number: str = None,
        name: str = None,
        union_id: str = None,
        user_id: str = None,
    ):
        # 工号
        self.job_number = job_number
        # 姓名
        self.name = name
        # unionId
        self.union_id = union_id
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_number is not None:
            result['jobNumber'] = self.job_number
        if self.name is not None:
            result['name'] = self.name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListSimpleUsersByRoleResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_cursor: int = None,
        user_list: List[ListSimpleUsersByRoleResponseBodyUserList] = None,
    ):
        # 是否还有记录
        self.has_more = has_more
        # 下一条记录
        self.next_cursor = next_cursor
        # 用户列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = ListSimpleUsersByRoleResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListSimpleUsersByRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSimpleUsersByRoleResponseBody = None,
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
            temp_model = ListSimpleUsersByRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubCorpsHeaders(TeaModel):
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


class ListSubCorpsRequest(TeaModel):
    def __init__(
        self,
        is_only_direct: bool = None,
        sub_corp_id: str = None,
        types: str = None,
    ):
        # 是否查询直接下级
        self.is_only_direct = is_only_direct
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id
        # 下级指定组织层级列表，组织层级为county,town,community,residential，依次为区/县、乡/镇/街道、社区/村、小区，如果查多个用 '|' 分隔
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_only_direct is not None:
            result['isOnlyDirect'] = self.is_only_direct
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isOnlyDirect') is not None:
            self.is_only_direct = m.get('isOnlyDirect')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListSubCorpsResponseBodyCorpList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        industry: str = None,
        industry_code: int = None,
        region_id: str = None,
        region_location: str = None,
        region_type: str = None,
    ):
        # 组织corpid
        self.corp_id = corp_id
        # 组织名字
        self.corp_name = corp_name
        # 组织行业名称
        self.industry = industry
        # 组织行业码
        self.industry_code = industry_code
        # 区域码
        self.region_id = region_id
        # 区域详细信息
        self.region_location = region_location
        # 区域类型，值为county,town,community,residential，依次为区/县、乡/镇/街道、社区/村、小区
        self.region_type = region_type

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
        if self.industry is not None:
            result['industry'] = self.industry
        if self.industry_code is not None:
            result['industryCode'] = self.industry_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.region_location is not None:
            result['regionLocation'] = self.region_location
        if self.region_type is not None:
            result['regionType'] = self.region_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('industryCode') is not None:
            self.industry_code = m.get('industryCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regionLocation') is not None:
            self.region_location = m.get('regionLocation')
        if m.get('regionType') is not None:
            self.region_type = m.get('regionType')
        return self


class ListSubCorpsResponseBody(TeaModel):
    def __init__(
        self,
        corp_list: List[ListSubCorpsResponseBodyCorpList] = None,
    ):
        # result
        self.corp_list = corp_list

    def validate(self):
        if self.corp_list:
            for k in self.corp_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['corpList'] = []
        if self.corp_list is not None:
            for k in self.corp_list:
                result['corpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.corp_list = []
        if m.get('corpList') is not None:
            for k in m.get('corpList'):
                temp_model = ListSubCorpsResponseBodyCorpList()
                self.corp_list.append(temp_model.from_map(k))
        return self


class ListSubCorpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubCorpsResponseBody = None,
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
            temp_model = ListSubCorpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubDeptHeaders(TeaModel):
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


class ListSubDeptRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        sub_corp_id: str = None,
    ):
        # 通讯录语言(默认zh_CN另外支持en_US)
        self.language = language
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListSubDeptResponseBodyResult(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        name: str = None,
    ):
        # 下属组织的部门ID
        self.department_id = department_id
        # 部门名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListSubDeptResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListSubDeptResponseBodyResult] = None,
    ):
        # 返回列表
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
                temp_model = ListSubDeptResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSubDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubDeptResponseBody = None,
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
            temp_model = ListSubDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubDeptIdsHeaders(TeaModel):
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


class ListSubDeptIdsRequest(TeaModel):
    def __init__(
        self,
        sub_corp_id: str = None,
    ):
        # 下属组织的组织ID，比如下属镇、村的corpId
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_corp_id is not None:
            result['subCorpId'] = self.sub_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subCorpId') is not None:
            self.sub_corp_id = m.get('subCorpId')
        return self


class ListSubDeptIdsResponseBody(TeaModel):
    def __init__(
        self,
        department_id_list: List[int] = None,
    ):
        # 下属组织的子部门 ID 列表
        self.department_id_list = department_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id_list is not None:
            result['departmentIdList'] = self.department_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIdList') is not None:
            self.department_id_list = m.get('departmentIdList')
        return self


class ListSubDeptIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubDeptIdsResponseBody = None,
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
            temp_model = ListSubDeptIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


