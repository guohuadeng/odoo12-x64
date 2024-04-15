# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddHrmPreentryHeaders(TeaModel):
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


class AddHrmPreentryRequestGroupsSectionsEmpFieldVOList(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['fieldCode'] = self.field_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AddHrmPreentryRequestGroupsSections(TeaModel):
    def __init__(
        self,
        emp_field_volist: List[AddHrmPreentryRequestGroupsSectionsEmpFieldVOList] = None,
        old_index: int = None,
    ):
        self.emp_field_volist = emp_field_volist
        self.old_index = old_index

    def validate(self):
        if self.emp_field_volist:
            for k in self.emp_field_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['empFieldVOList'] = []
        if self.emp_field_volist is not None:
            for k in self.emp_field_volist:
                result['empFieldVOList'].append(k.to_map() if k else None)
        if self.old_index is not None:
            result['oldIndex'] = self.old_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.emp_field_volist = []
        if m.get('empFieldVOList') is not None:
            for k in m.get('empFieldVOList'):
                temp_model = AddHrmPreentryRequestGroupsSectionsEmpFieldVOList()
                self.emp_field_volist.append(temp_model.from_map(k))
        if m.get('oldIndex') is not None:
            self.old_index = m.get('oldIndex')
        return self


class AddHrmPreentryRequestGroups(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        sections: List[AddHrmPreentryRequestGroupsSections] = None,
    ):
        self.group_id = group_id
        self.sections = sections

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['sections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.sections = []
        if m.get('sections') is not None:
            for k in m.get('sections'):
                temp_model = AddHrmPreentryRequestGroupsSections()
                self.sections.append(temp_model.from_map(k))
        return self


class AddHrmPreentryRequest(TeaModel):
    def __init__(
        self,
        agent_id: int = None,
        groups: List[AddHrmPreentryRequestGroups] = None,
        mobile: str = None,
        name: str = None,
        pre_entry_time: int = None,
    ):
        self.agent_id = agent_id
        self.groups = groups
        self.mobile = mobile
        self.name = name
        self.pre_entry_time = pre_entry_time

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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.pre_entry_time is not None:
            result['preEntryTime'] = self.pre_entry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = AddHrmPreentryRequestGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('preEntryTime') is not None:
            self.pre_entry_time = m.get('preEntryTime')
        return self


class AddHrmPreentryResponseBody(TeaModel):
    def __init__(
        self,
        tmp_user_id: str = None,
    ):
        # result
        self.tmp_user_id = tmp_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tmp_user_id is not None:
            result['tmpUserId'] = self.tmp_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tmpUserId') is not None:
            self.tmp_user_id = m.get('tmpUserId')
        return self


class AddHrmPreentryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHrmPreentryResponseBody = None,
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
            temp_model = AddHrmPreentryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ECertQueryHeaders(TeaModel):
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


class ECertQueryRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 用户ID
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


class ECertQueryResponseBody(TeaModel):
    def __init__(
        self,
        cert_no: str = None,
        employ_job_id: str = None,
        employ_job_id_label: str = None,
        employ_position_id: str = None,
        employ_position_id_label: str = None,
        employ_position_rank_id: str = None,
        employ_position_rank_id_label: str = None,
        hired_date: str = None,
        last_work_day: str = None,
        main_dept_id: int = None,
        main_dept_name: str = None,
        name: str = None,
        real_name: str = None,
        termination_reason_passive: List[str] = None,
        termination_reason_voluntary: List[str] = None,
    ):
        # 身份证号码
        self.cert_no = cert_no
        # 职务ID
        self.employ_job_id = employ_job_id
        # 职务名称
        self.employ_job_id_label = employ_job_id_label
        # 职位ID
        self.employ_position_id = employ_position_id
        # 职位名称
        self.employ_position_id_label = employ_position_id_label
        # 职级ID
        self.employ_position_rank_id = employ_position_rank_id
        # 职级名称
        self.employ_position_rank_id_label = employ_position_rank_id_label
        # 入职日期
        self.hired_date = hired_date
        # 离职日期
        self.last_work_day = last_work_day
        # 主部门ID
        self.main_dept_id = main_dept_id
        # 主部门
        self.main_dept_name = main_dept_name
        # 姓名
        self.name = name
        # 身份证姓名
        self.real_name = real_name
        # 被动离职原因
        self.termination_reason_passive = termination_reason_passive
        # 主动离职原因
        self.termination_reason_voluntary = termination_reason_voluntary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_no is not None:
            result['certNO'] = self.cert_no
        if self.employ_job_id is not None:
            result['employJobId'] = self.employ_job_id
        if self.employ_job_id_label is not None:
            result['employJobIdLabel'] = self.employ_job_id_label
        if self.employ_position_id is not None:
            result['employPositionId'] = self.employ_position_id
        if self.employ_position_id_label is not None:
            result['employPositionIdLabel'] = self.employ_position_id_label
        if self.employ_position_rank_id is not None:
            result['employPositionRankId'] = self.employ_position_rank_id
        if self.employ_position_rank_id_label is not None:
            result['employPositionRankIdLabel'] = self.employ_position_rank_id_label
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.last_work_day is not None:
            result['lastWorkDay'] = self.last_work_day
        if self.main_dept_id is not None:
            result['mainDeptId'] = self.main_dept_id
        if self.main_dept_name is not None:
            result['mainDeptName'] = self.main_dept_name
        if self.name is not None:
            result['name'] = self.name
        if self.real_name is not None:
            result['realName'] = self.real_name
        if self.termination_reason_passive is not None:
            result['terminationReasonPassive'] = self.termination_reason_passive
        if self.termination_reason_voluntary is not None:
            result['terminationReasonVoluntary'] = self.termination_reason_voluntary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certNO') is not None:
            self.cert_no = m.get('certNO')
        if m.get('employJobId') is not None:
            self.employ_job_id = m.get('employJobId')
        if m.get('employJobIdLabel') is not None:
            self.employ_job_id_label = m.get('employJobIdLabel')
        if m.get('employPositionId') is not None:
            self.employ_position_id = m.get('employPositionId')
        if m.get('employPositionIdLabel') is not None:
            self.employ_position_id_label = m.get('employPositionIdLabel')
        if m.get('employPositionRankId') is not None:
            self.employ_position_rank_id = m.get('employPositionRankId')
        if m.get('employPositionRankIdLabel') is not None:
            self.employ_position_rank_id_label = m.get('employPositionRankIdLabel')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('lastWorkDay') is not None:
            self.last_work_day = m.get('lastWorkDay')
        if m.get('mainDeptId') is not None:
            self.main_dept_id = m.get('mainDeptId')
        if m.get('mainDeptName') is not None:
            self.main_dept_name = m.get('mainDeptName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('realName') is not None:
            self.real_name = m.get('realName')
        if m.get('terminationReasonPassive') is not None:
            self.termination_reason_passive = m.get('terminationReasonPassive')
        if m.get('terminationReasonVoluntary') is not None:
            self.termination_reason_voluntary = m.get('terminationReasonVoluntary')
        return self


class ECertQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ECertQueryResponseBody = None,
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
            temp_model = ECertQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MasterDataQueryHeaders(TeaModel):
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


class MasterDataQueryRequestQueryParamsConditionList(TeaModel):
    def __init__(
        self,
        operate: str = None,
        value: str = None,
    ):
        # 字段关系符
        self.operate = operate
        # 操作值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate is not None:
            result['operate'] = self.operate
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class MasterDataQueryRequestQueryParams(TeaModel):
    def __init__(
        self,
        condition_list: List[MasterDataQueryRequestQueryParamsConditionList] = None,
        field_code: str = None,
        join_type: str = None,
    ):
        # 筛选条件
        self.condition_list = condition_list
        # 需要筛选的字段
        self.field_code = field_code
        # 筛选条件连接类型
        self.join_type = join_type

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['conditionList'].append(k.to_map() if k else None)
        if self.field_code is not None:
            result['fieldCode'] = self.field_code
        if self.join_type is not None:
            result['joinType'] = self.join_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_list = []
        if m.get('conditionList') is not None:
            for k in m.get('conditionList'):
                temp_model = MasterDataQueryRequestQueryParamsConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')
        if m.get('joinType') is not None:
            self.join_type = m.get('joinType')
        return self


class MasterDataQueryRequest(TeaModel):
    def __init__(
        self,
        biz_uk: str = None,
        max_results: int = None,
        next_token: int = None,
        opt_user_id: str = None,
        query_params: List[MasterDataQueryRequestQueryParams] = None,
        relation_ids: List[str] = None,
        scope_code: str = None,
        tenant_id: int = None,
        view_entity_code: str = None,
    ):
        # 数据唯一键
        self.biz_uk = biz_uk
        # 分页查询每页数据条数
        self.max_results = max_results
        # 分页查询的游标
        self.next_token = next_token
        # 当前操作人userId
        self.opt_user_id = opt_user_id
        # 其他查询条件
        self.query_params = query_params
        # 关联id列表，一般为userId
        self.relation_ids = relation_ids
        # 领域code 由钉钉分配
        self.scope_code = scope_code
        # 数据生产方的租户id，由钉钉分配
        self.tenant_id = tenant_id
        # 实体code
        self.view_entity_code = view_entity_code

    def validate(self):
        if self.query_params:
            for k in self.query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_uk is not None:
            result['bizUK'] = self.biz_uk
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.opt_user_id is not None:
            result['optUserId'] = self.opt_user_id
        result['queryParams'] = []
        if self.query_params is not None:
            for k in self.query_params:
                result['queryParams'].append(k.to_map() if k else None)
        if self.relation_ids is not None:
            result['relationIds'] = self.relation_ids
        if self.scope_code is not None:
            result['scopeCode'] = self.scope_code
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.view_entity_code is not None:
            result['viewEntityCode'] = self.view_entity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizUK') is not None:
            self.biz_uk = m.get('bizUK')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('optUserId') is not None:
            self.opt_user_id = m.get('optUserId')
        self.query_params = []
        if m.get('queryParams') is not None:
            for k in m.get('queryParams'):
                temp_model = MasterDataQueryRequestQueryParams()
                self.query_params.append(temp_model.from_map(k))
        if m.get('relationIds') is not None:
            self.relation_ids = m.get('relationIds')
        if m.get('scopeCode') is not None:
            self.scope_code = m.get('scopeCode')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('viewEntityCode') is not None:
            self.view_entity_code = m.get('viewEntityCode')
        return self


class MasterDataQueryResponseBodyResultViewEntityFieldVOListFieldDataVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 字段值的key
        self.key = key
        # 字段值的文本
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class MasterDataQueryResponseBodyResultViewEntityFieldVOList(TeaModel):
    def __init__(
        self,
        field_code: str = None,
        field_data_vo: MasterDataQueryResponseBodyResultViewEntityFieldVOListFieldDataVO = None,
        field_name: str = None,
        field_type: str = None,
    ):
        # 字段code
        self.field_code = field_code
        # 字段值
        self.field_data_vo = field_data_vo
        # 字段名称
        self.field_name = field_name
        # 字段类型
        self.field_type = field_type

    def validate(self):
        if self.field_data_vo:
            self.field_data_vo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_code is not None:
            result['fieldCode'] = self.field_code
        if self.field_data_vo is not None:
            result['fieldDataVO'] = self.field_data_vo.to_map()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.field_type is not None:
            result['fieldType'] = self.field_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')
        if m.get('fieldDataVO') is not None:
            temp_model = MasterDataQueryResponseBodyResultViewEntityFieldVOListFieldDataVO()
            self.field_data_vo = temp_model.from_map(m['fieldDataVO'])
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')
        return self


class MasterDataQueryResponseBodyResult(TeaModel):
    def __init__(
        self,
        outer_id: str = None,
        relation_id: str = None,
        scope_code: str = None,
        view_entity_code: str = None,
        view_entity_field_volist: List[MasterDataQueryResponseBodyResultViewEntityFieldVOList] = None,
    ):
        # 唯一id
        self.outer_id = outer_id
        # 关联id列表，一般为userId
        self.relation_id = relation_id
        # 领域
        self.scope_code = scope_code
        # 编码
        self.view_entity_code = view_entity_code
        # 字段列表
        self.view_entity_field_volist = view_entity_field_volist

    def validate(self):
        if self.view_entity_field_volist:
            for k in self.view_entity_field_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_id is not None:
            result['outerId'] = self.outer_id
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.scope_code is not None:
            result['scopeCode'] = self.scope_code
        if self.view_entity_code is not None:
            result['viewEntityCode'] = self.view_entity_code
        result['viewEntityFieldVOList'] = []
        if self.view_entity_field_volist is not None:
            for k in self.view_entity_field_volist:
                result['viewEntityFieldVOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outerId') is not None:
            self.outer_id = m.get('outerId')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('scopeCode') is not None:
            self.scope_code = m.get('scopeCode')
        if m.get('viewEntityCode') is not None:
            self.view_entity_code = m.get('viewEntityCode')
        self.view_entity_field_volist = []
        if m.get('viewEntityFieldVOList') is not None:
            for k in m.get('viewEntityFieldVOList'):
                temp_model = MasterDataQueryResponseBodyResultViewEntityFieldVOList()
                self.view_entity_field_volist.append(temp_model.from_map(k))
        return self


class MasterDataQueryResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: int = None,
        result: List[MasterDataQueryResponseBodyResult] = None,
        success: bool = None,
        total: int = None,
    ):
        # 是否还有更多
        self.has_more = has_more
        # 分页游标
        self.next_token = next_token
        # 结果
        self.result = result
        # 是否成功
        self.success = success
        # 总条目数
        self.total = total

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
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = MasterDataQueryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class MasterDataQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MasterDataQueryResponseBody = None,
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
            temp_model = MasterDataQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MasterDataSaveHeaders(TeaModel):
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


class MasterDataSaveRequestBodyFieldList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value_str: str = None,
    ):
        # 字段名
        self.name = name
        # 字段string值
        self.value_str = value_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value_str is not None:
            result['valueStr'] = self.value_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('valueStr') is not None:
            self.value_str = m.get('valueStr')
        return self


class MasterDataSaveRequestBodyScope(TeaModel):
    def __init__(
        self,
        scope_code: str = None,
        version: int = None,
    ):
        # 业务域code，如PERFORMANCE，系统分配
        self.scope_code = scope_code
        # 业务域版本，接入时系统分配，默认传1
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_code is not None:
            result['scopeCode'] = self.scope_code
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopeCode') is not None:
            self.scope_code = m.get('scopeCode')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class MasterDataSaveRequestBody(TeaModel):
    def __init__(
        self,
        biz_time: int = None,
        biz_uk: str = None,
        entity_code: str = None,
        field_list: List[MasterDataSaveRequestBodyFieldList] = None,
        scope: MasterDataSaveRequestBodyScope = None,
        user_id: str = None,
    ):
        # 数据变更时间戳，用以保证更新操作的顺序性
        self.biz_time = biz_time
        # 数据流水唯一标识，如流水号，用以唯一确认一条写入数据
        self.biz_uk = biz_uk
        # 业务域下的细分领域实体
        self.entity_code = entity_code
        # 数据字段列表
        self.field_list = field_list
        # 业务域描述，系统分配
        self.scope = scope
        # 员工id
        self.user_id = user_id

    def validate(self):
        if self.field_list:
            for k in self.field_list:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_time is not None:
            result['bizTime'] = self.biz_time
        if self.biz_uk is not None:
            result['bizUk'] = self.biz_uk
        if self.entity_code is not None:
            result['entityCode'] = self.entity_code
        result['fieldList'] = []
        if self.field_list is not None:
            for k in self.field_list:
                result['fieldList'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTime') is not None:
            self.biz_time = m.get('bizTime')
        if m.get('bizUk') is not None:
            self.biz_uk = m.get('bizUk')
        if m.get('entityCode') is not None:
            self.entity_code = m.get('entityCode')
        self.field_list = []
        if m.get('fieldList') is not None:
            for k in m.get('fieldList'):
                temp_model = MasterDataSaveRequestBodyFieldList()
                self.field_list.append(temp_model.from_map(k))
        if m.get('scope') is not None:
            temp_model = MasterDataSaveRequestBodyScope()
            self.scope = temp_model.from_map(m['scope'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class MasterDataSaveRequest(TeaModel):
    def __init__(
        self,
        body: List[MasterDataSaveRequestBody] = None,
        tenant_id: int = None,
    ):
        # 主数据
        self.body = body
        # 租户id
        self.tenant_id = tenant_id

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
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = MasterDataSaveRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class MasterDataSaveResponseBodyFailResult(TeaModel):
    def __init__(
        self,
        biz_uk: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # 业务流水唯一标识，和入参一致
        self.biz_uk = biz_uk
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_uk is not None:
            result['bizUk'] = self.biz_uk
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizUk') is not None:
            self.biz_uk = m.get('bizUk')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class MasterDataSaveResponseBody(TeaModel):
    def __init__(
        self,
        all_success: bool = None,
        fail_result: List[MasterDataSaveResponseBodyFailResult] = None,
    ):
        # 是否全部保存成功
        self.all_success = all_success
        # 保存失败的结果，全部保存成功时为空
        self.fail_result = fail_result

    def validate(self):
        if self.fail_result:
            for k in self.fail_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_success is not None:
            result['allSuccess'] = self.all_success
        result['failResult'] = []
        if self.fail_result is not None:
            for k in self.fail_result:
                result['failResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allSuccess') is not None:
            self.all_success = m.get('allSuccess')
        self.fail_result = []
        if m.get('failResult') is not None:
            for k in m.get('failResult'):
                temp_model = MasterDataSaveResponseBodyFailResult()
                self.fail_result.append(temp_model.from_map(k))
        return self


class MasterDataSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MasterDataSaveResponseBody = None,
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
            temp_model = MasterDataSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MasterDataTenantQueyHeaders(TeaModel):
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


class MasterDataTenantQueyRequest(TeaModel):
    def __init__(
        self,
        entity_code: str = None,
        scope_code: str = None,
    ):
        # 实体 code
        self.entity_code = entity_code
        # isv的业务领域
        self.scope_code = scope_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_code is not None:
            result['entityCode'] = self.entity_code
        if self.scope_code is not None:
            result['scopeCode'] = self.scope_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityCode') is not None:
            self.entity_code = m.get('entityCode')
        if m.get('scopeCode') is not None:
            self.scope_code = m.get('scopeCode')
        return self


class MasterDataTenantQueyResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_data: bool = None,
        integrate_data_auth: bool = None,
        name: str = None,
        read_auth: bool = None,
        tenant_id: int = None,
        type: int = None,
    ):
        # 该租户是否已向主数据同步数据
        self.has_data = has_data
        # 该租户是否有向主数据写数据的权限
        self.integrate_data_auth = integrate_data_auth
        # 租户名称
        self.name = name
        # 调用方是否有读该租户数据的权限
        self.read_auth = read_auth
        # 租户 id
        self.tenant_id = tenant_id
        # 租户类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_data is not None:
            result['hasData'] = self.has_data
        if self.integrate_data_auth is not None:
            result['integrateDataAuth'] = self.integrate_data_auth
        if self.name is not None:
            result['name'] = self.name
        if self.read_auth is not None:
            result['readAuth'] = self.read_auth
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasData') is not None:
            self.has_data = m.get('hasData')
        if m.get('integrateDataAuth') is not None:
            self.integrate_data_auth = m.get('integrateDataAuth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('readAuth') is not None:
            self.read_auth = m.get('readAuth')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MasterDataTenantQueyResponseBody(TeaModel):
    def __init__(
        self,
        result: List[MasterDataTenantQueyResponseBodyResult] = None,
    ):
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
                temp_model = MasterDataTenantQueyResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class MasterDataTenantQueyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MasterDataTenantQueyResponseBody = None,
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
            temp_model = MasterDataTenantQueyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomEntryProcessesHeaders(TeaModel):
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


class QueryCustomEntryProcessesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
        operate_user_id: str = None,
    ):
        # 最大值
        self.max_results = max_results
        # 偏移量
        self.next_token = next_token
        # 操作人id
        self.operate_user_id = operate_user_id

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
        if self.operate_user_id is not None:
            result['operateUserId'] = self.operate_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('operateUserId') is not None:
            self.operate_user_id = m.get('operateUserId')
        return self


class QueryCustomEntryProcessesResponseBodyList(TeaModel):
    def __init__(
        self,
        form_desc: str = None,
        form_id: str = None,
        form_name: str = None,
        short_url: str = None,
    ):
        self.form_desc = form_desc
        self.form_id = form_id
        self.form_name = form_name
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_desc is not None:
            result['formDesc'] = self.form_desc
        if self.form_id is not None:
            result['formId'] = self.form_id
        if self.form_name is not None:
            result['formName'] = self.form_name
        if self.short_url is not None:
            result['shortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formDesc') is not None:
            self.form_desc = m.get('formDesc')
        if m.get('formId') is not None:
            self.form_id = m.get('formId')
        if m.get('formName') is not None:
            self.form_name = m.get('formName')
        if m.get('shortUrl') is not None:
            self.short_url = m.get('shortUrl')
        return self


class QueryCustomEntryProcessesResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryCustomEntryProcessesResponseBodyList] = None,
        next_token: int = None,
    ):
        # 是否有更多
        self.has_more = has_more
        # 表单信息列表
        self.list = list
        # 下次获取数据的起始游标
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
                temp_model = QueryCustomEntryProcessesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryCustomEntryProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCustomEntryProcessesResponseBody = None,
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
            temp_model = QueryCustomEntryProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHrmEmployeeDismissionInfoHeaders(TeaModel):
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


class QueryHrmEmployeeDismissionInfoRequest(TeaModel):
    def __init__(
        self,
        user_id_list: List[str] = None,
    ):
        # 员工 ids
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


class QueryHrmEmployeeDismissionInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        user_id_list_shrink: str = None,
    ):
        # 员工 ids
        self.user_id_list_shrink = user_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id_list_shrink is not None:
            result['userIdList'] = self.user_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userIdList') is not None:
            self.user_id_list_shrink = m.get('userIdList')
        return self


class QueryHrmEmployeeDismissionInfoResponseBodyResultDeptList(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
        dept_path: str = None,
    ):
        # 部门id
        self.dept_id = dept_id
        # 部门路径
        self.dept_path = dept_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['dept_id'] = self.dept_id
        if self.dept_path is not None:
            result['dept_path'] = self.dept_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dept_id') is not None:
            self.dept_id = m.get('dept_id')
        if m.get('dept_path') is not None:
            self.dept_path = m.get('dept_path')
        return self


class QueryHrmEmployeeDismissionInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        dept_list: List[QueryHrmEmployeeDismissionInfoResponseBodyResultDeptList] = None,
        handover_user_id: str = None,
        last_work_day: int = None,
        main_dept_id: int = None,
        main_dept_name: str = None,
        passive_reason: List[str] = None,
        pre_status: int = None,
        reason_memo: str = None,
        status: int = None,
        user_id: str = None,
        voluntary_reason: List[str] = None,
    ):
        # 离职部门列表
        self.dept_list = dept_list
        # 离职交接人
        self.handover_user_id = handover_user_id
        # 最后工作日
        self.last_work_day = last_work_day
        # 离职前主部门id
        self.main_dept_id = main_dept_id
        # 离职前主部门名称
        self.main_dept_name = main_dept_name
        # 离职原因-被动
        self.passive_reason = passive_reason
        # 离职前工作状态：1，待入职；2，试用期；3，正式
        self.pre_status = pre_status
        # 离职原因备注
        self.reason_memo = reason_memo
        # 离职状态：1，待离职；2，已离职
        self.status = status
        # 员工id
        self.user_id = user_id
        # 离职原因-主动
        self.voluntary_reason = voluntary_reason

    def validate(self):
        if self.dept_list:
            for k in self.dept_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['deptList'] = []
        if self.dept_list is not None:
            for k in self.dept_list:
                result['deptList'].append(k.to_map() if k else None)
        if self.handover_user_id is not None:
            result['handoverUserId'] = self.handover_user_id
        if self.last_work_day is not None:
            result['lastWorkDay'] = self.last_work_day
        if self.main_dept_id is not None:
            result['mainDeptId'] = self.main_dept_id
        if self.main_dept_name is not None:
            result['mainDeptName'] = self.main_dept_name
        if self.passive_reason is not None:
            result['passiveReason'] = self.passive_reason
        if self.pre_status is not None:
            result['preStatus'] = self.pre_status
        if self.reason_memo is not None:
            result['reasonMemo'] = self.reason_memo
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.voluntary_reason is not None:
            result['voluntaryReason'] = self.voluntary_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dept_list = []
        if m.get('deptList') is not None:
            for k in m.get('deptList'):
                temp_model = QueryHrmEmployeeDismissionInfoResponseBodyResultDeptList()
                self.dept_list.append(temp_model.from_map(k))
        if m.get('handoverUserId') is not None:
            self.handover_user_id = m.get('handoverUserId')
        if m.get('lastWorkDay') is not None:
            self.last_work_day = m.get('lastWorkDay')
        if m.get('mainDeptId') is not None:
            self.main_dept_id = m.get('mainDeptId')
        if m.get('mainDeptName') is not None:
            self.main_dept_name = m.get('mainDeptName')
        if m.get('passiveReason') is not None:
            self.passive_reason = m.get('passiveReason')
        if m.get('preStatus') is not None:
            self.pre_status = m.get('preStatus')
        if m.get('reasonMemo') is not None:
            self.reason_memo = m.get('reasonMemo')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('voluntaryReason') is not None:
            self.voluntary_reason = m.get('voluntaryReason')
        return self


class QueryHrmEmployeeDismissionInfoResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryHrmEmployeeDismissionInfoResponseBodyResult] = None,
    ):
        # 名称列表
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
                temp_model = QueryHrmEmployeeDismissionInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryHrmEmployeeDismissionInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHrmEmployeeDismissionInfoResponseBody = None,
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
            temp_model = QueryHrmEmployeeDismissionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryJobRanksHeaders(TeaModel):
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


class QueryJobRanksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
        rank_category_id: str = None,
        rank_code: str = None,
        rank_name: str = None,
    ):
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置
        self.next_token = next_token
        # 职级序列
        self.rank_category_id = rank_category_id
        # 职级编码
        self.rank_code = rank_code
        # 职级名称
        self.rank_name = rank_name

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
        if self.rank_category_id is not None:
            result['rankCategoryId'] = self.rank_category_id
        if self.rank_code is not None:
            result['rankCode'] = self.rank_code
        if self.rank_name is not None:
            result['rankName'] = self.rank_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('rankCategoryId') is not None:
            self.rank_category_id = m.get('rankCategoryId')
        if m.get('rankCode') is not None:
            self.rank_code = m.get('rankCode')
        if m.get('rankName') is not None:
            self.rank_name = m.get('rankName')
        return self


class QueryJobRanksResponseBodyList(TeaModel):
    def __init__(
        self,
        max_job_grade: int = None,
        min_job_grade: int = None,
        rank_category_id: str = None,
        rank_code: str = None,
        rank_description: str = None,
        rank_id: str = None,
        rank_name: str = None,
    ):
        # 最大等级
        self.max_job_grade = max_job_grade
        # 最小等级
        self.min_job_grade = min_job_grade
        # 职级序列ID
        self.rank_category_id = rank_category_id
        # 职级编码
        self.rank_code = rank_code
        # 职级描述
        self.rank_description = rank_description
        # 职级ID
        self.rank_id = rank_id
        # 职级名称
        self.rank_name = rank_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_job_grade is not None:
            result['maxJobGrade'] = self.max_job_grade
        if self.min_job_grade is not None:
            result['minJobGrade'] = self.min_job_grade
        if self.rank_category_id is not None:
            result['rankCategoryId'] = self.rank_category_id
        if self.rank_code is not None:
            result['rankCode'] = self.rank_code
        if self.rank_description is not None:
            result['rankDescription'] = self.rank_description
        if self.rank_id is not None:
            result['rankId'] = self.rank_id
        if self.rank_name is not None:
            result['rankName'] = self.rank_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxJobGrade') is not None:
            self.max_job_grade = m.get('maxJobGrade')
        if m.get('minJobGrade') is not None:
            self.min_job_grade = m.get('minJobGrade')
        if m.get('rankCategoryId') is not None:
            self.rank_category_id = m.get('rankCategoryId')
        if m.get('rankCode') is not None:
            self.rank_code = m.get('rankCode')
        if m.get('rankDescription') is not None:
            self.rank_description = m.get('rankDescription')
        if m.get('rankId') is not None:
            self.rank_id = m.get('rankId')
        if m.get('rankName') is not None:
            self.rank_name = m.get('rankName')
        return self


class QueryJobRanksResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryJobRanksResponseBodyList] = None,
        next_token: int = None,
    ):
        # 是否有更多数据
        self.has_more = has_more
        # 职级列表
        self.list = list
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
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
                temp_model = QueryJobRanksResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryJobRanksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryJobRanksResponseBody = None,
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
            temp_model = QueryJobRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryJobsHeaders(TeaModel):
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


class QueryJobsRequest(TeaModel):
    def __init__(
        self,
        job_name: str = None,
        max_results: int = None,
        next_token: int = None,
    ):
        # 职务名称
        self.job_name = job_name
        # 最大值
        self.max_results = max_results
        # 偏移量
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryJobsResponseBodyList(TeaModel):
    def __init__(
        self,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
    ):
        # 职务描述
        self.job_description = job_description
        # 职务ID
        self.job_id = job_id
        # 职务名称
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_description is not None:
            result['jobDescription'] = self.job_description
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_name is not None:
            result['jobName'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobDescription') is not None:
            self.job_description = m.get('jobDescription')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        return self


class QueryJobsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryJobsResponseBodyList] = None,
        next_token: int = None,
    ):
        # 是否有更多数据
        self.has_more = has_more
        # 职务列表
        self.list = list
        # 下次获取数据的起始游标
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
                temp_model = QueryJobsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryJobsResponseBody = None,
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
            temp_model = QueryJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPositionsHeaders(TeaModel):
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


class QueryPositionsRequest(TeaModel):
    def __init__(
        self,
        in_category_ids: List[str] = None,
        in_position_ids: List[str] = None,
        position_name: str = None,
        max_results: int = None,
        next_token: int = None,
    ):
        # 职位类别列表
        self.in_category_ids = in_category_ids
        # 职位id列表
        self.in_position_ids = in_position_ids
        # 职位名称
        self.position_name = position_name
        # 一次查询获取记录数
        self.max_results = max_results
        # 偏移量
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_category_ids is not None:
            result['inCategoryIds'] = self.in_category_ids
        if self.in_position_ids is not None:
            result['inPositionIds'] = self.in_position_ids
        if self.position_name is not None:
            result['positionName'] = self.position_name
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inCategoryIds') is not None:
            self.in_category_ids = m.get('inCategoryIds')
        if m.get('inPositionIds') is not None:
            self.in_position_ids = m.get('inPositionIds')
        if m.get('positionName') is not None:
            self.position_name = m.get('positionName')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryPositionsResponseBodyList(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        position_category_id: str = None,
        position_des: str = None,
        position_id: str = None,
        position_name: str = None,
        rank_id_list: List[str] = None,
        status: int = None,
    ):
        # 所属职务ID
        self.job_id = job_id
        # 职位类别ID
        self.position_category_id = position_category_id
        # 职位描述
        self.position_des = position_des
        # 职位ID
        self.position_id = position_id
        # 职位名称
        self.position_name = position_name
        # 职位对应职级列表
        self.rank_id_list = rank_id_list
        # 职位状态-0，启用；1，停用
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.position_category_id is not None:
            result['positionCategoryId'] = self.position_category_id
        if self.position_des is not None:
            result['positionDes'] = self.position_des
        if self.position_id is not None:
            result['positionId'] = self.position_id
        if self.position_name is not None:
            result['positionName'] = self.position_name
        if self.rank_id_list is not None:
            result['rankIdList'] = self.rank_id_list
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('positionCategoryId') is not None:
            self.position_category_id = m.get('positionCategoryId')
        if m.get('positionDes') is not None:
            self.position_des = m.get('positionDes')
        if m.get('positionId') is not None:
            self.position_id = m.get('positionId')
        if m.get('positionName') is not None:
            self.position_name = m.get('positionName')
        if m.get('rankIdList') is not None:
            self.rank_id_list = m.get('rankIdList')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryPositionsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryPositionsResponseBodyList] = None,
        next_token: int = None,
    ):
        # 是否有更多数据
        self.has_more = has_more
        # 职位列表
        self.list = list
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
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
                temp_model = QueryPositionsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryPositionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPositionsResponseBody = None,
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
            temp_model = QueryPositionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


