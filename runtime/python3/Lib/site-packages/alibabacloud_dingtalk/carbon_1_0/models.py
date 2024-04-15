# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class WriteAlibabaOrgCarbonHeaders(TeaModel):
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


class WriteAlibabaOrgCarbonRequestOrgDetailsList(TeaModel):
    def __init__(
        self,
        action_id: str = None,
        action_time: str = None,
        action_type: str = None,
        carbon_amount: str = None,
        corp_id: str = None,
        dept_id: int = None,
        version: int = None,
    ):
        # 系统唯一id，生成格式：userId+日期20211126
        self.action_id = action_id
        # 行为发生时间
        self.action_time = action_time
        # 碳能量行为类型，需要联系管理员添加
        self.action_type = action_type
        # 碳能量数据
        self.carbon_amount = carbon_amount
        # 钉钉组织id
        self.corp_id = corp_id
        # 钉钉部门id
        self.dept_id = dept_id
        # 版本，默认为1
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_id is not None:
            result['actionId'] = self.action_id
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.carbon_amount is not None:
            result['carbonAmount'] = self.carbon_amount
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionId') is not None:
            self.action_id = m.get('actionId')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('carbonAmount') is not None:
            self.carbon_amount = m.get('carbonAmount')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class WriteAlibabaOrgCarbonRequest(TeaModel):
    def __init__(
        self,
        org_details_list: List[WriteAlibabaOrgCarbonRequestOrgDetailsList] = None,
    ):
        # 入参集
        self.org_details_list = org_details_list

    def validate(self):
        if self.org_details_list:
            for k in self.org_details_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['orgDetailsList'] = []
        if self.org_details_list is not None:
            for k in self.org_details_list:
                result['orgDetailsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.org_details_list = []
        if m.get('orgDetailsList') is not None:
            for k in m.get('orgDetailsList'):
                temp_model = WriteAlibabaOrgCarbonRequestOrgDetailsList()
                self.org_details_list.append(temp_model.from_map(k))
        return self


class WriteAlibabaOrgCarbonResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
        success: bool = None,
    ):
        # 返回请求成功的数量
        self.result = result
        # 请求是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WriteAlibabaOrgCarbonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteAlibabaOrgCarbonResponseBody = None,
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
            temp_model = WriteAlibabaOrgCarbonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteAlibabaUserCarbonHeaders(TeaModel):
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


class WriteAlibabaUserCarbonRequestUserDetailsList(TeaModel):
    def __init__(
        self,
        action_end_time: str = None,
        action_id: str = None,
        action_start_time: str = None,
        action_type: str = None,
        carbon_amount: str = None,
        corp_id: str = None,
        dept_id: int = None,
        user_id: str = None,
        version: int = None,
    ):
        # 行为结束时间
        self.action_end_time = action_end_time
        # 系统唯一id，生成格式：userId+日期20211126
        self.action_id = action_id
        # 行为起始时间
        self.action_start_time = action_start_time
        # 碳能量行为类型，需要联系管理员添加
        self.action_type = action_type
        # 碳能量数据
        self.carbon_amount = carbon_amount
        # 钉钉组织id
        self.corp_id = corp_id
        # 钉钉部门id
        self.dept_id = dept_id
        # 钉钉用户id
        self.user_id = user_id
        # 版本，默认为1
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_end_time is not None:
            result['actionEndTime'] = self.action_end_time
        if self.action_id is not None:
            result['actionId'] = self.action_id
        if self.action_start_time is not None:
            result['actionStartTime'] = self.action_start_time
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.carbon_amount is not None:
            result['carbonAmount'] = self.carbon_amount
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionEndTime') is not None:
            self.action_end_time = m.get('actionEndTime')
        if m.get('actionId') is not None:
            self.action_id = m.get('actionId')
        if m.get('actionStartTime') is not None:
            self.action_start_time = m.get('actionStartTime')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('carbonAmount') is not None:
            self.carbon_amount = m.get('carbonAmount')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class WriteAlibabaUserCarbonRequest(TeaModel):
    def __init__(
        self,
        user_details_list: List[WriteAlibabaUserCarbonRequestUserDetailsList] = None,
    ):
        # 入参集
        self.user_details_list = user_details_list

    def validate(self):
        if self.user_details_list:
            for k in self.user_details_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['userDetailsList'] = []
        if self.user_details_list is not None:
            for k in self.user_details_list:
                result['userDetailsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_details_list = []
        if m.get('userDetailsList') is not None:
            for k in m.get('userDetailsList'):
                temp_model = WriteAlibabaUserCarbonRequestUserDetailsList()
                self.user_details_list.append(temp_model.from_map(k))
        return self


class WriteAlibabaUserCarbonResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
        success: bool = None,
    ):
        # 返回请求成功个数
        self.result = result
        # 请求是否写入成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WriteAlibabaUserCarbonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteAlibabaUserCarbonResponseBody = None,
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
            temp_model = WriteAlibabaUserCarbonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteIsvStateHeaders(TeaModel):
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


class WriteIsvStateRequest(TeaModel):
    def __init__(
        self,
        isv_name: str = None,
        stat_date: str = None,
    ):
        # ISV名称
        self.isv_name = isv_name
        # 数据完成日期
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isv_name is not None:
            result['isvName'] = self.isv_name
        if self.stat_date is not None:
            result['statDate'] = self.stat_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isvName') is not None:
            self.isv_name = m.get('isvName')
        if m.get('statDate') is not None:
            self.stat_date = m.get('statDate')
        return self


class WriteIsvStateResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # 数据写入标识
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


class WriteIsvStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteIsvStateResponseBody = None,
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
            temp_model = WriteIsvStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteOrgCarbonHeaders(TeaModel):
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


class WriteOrgCarbonRequestOrgDetailsList(TeaModel):
    def __init__(
        self,
        action_id: str = None,
        action_time: str = None,
        action_type: str = None,
        carbon_amount: str = None,
        corp_id: str = None,
        dept_id: int = None,
        version: int = None,
    ):
        # 系统唯一id，生成格式：userId+日期20211126
        self.action_id = action_id
        # 行为发生时间
        self.action_time = action_time
        # 碳能量行为类型，需要联系管理员添加
        self.action_type = action_type
        # 碳能量数据
        self.carbon_amount = carbon_amount
        # 钉钉组织id
        self.corp_id = corp_id
        # 钉钉部门id
        self.dept_id = dept_id
        # 版本，默认为1
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_id is not None:
            result['actionId'] = self.action_id
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.carbon_amount is not None:
            result['carbonAmount'] = self.carbon_amount
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionId') is not None:
            self.action_id = m.get('actionId')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('carbonAmount') is not None:
            self.carbon_amount = m.get('carbonAmount')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class WriteOrgCarbonRequest(TeaModel):
    def __init__(
        self,
        org_details_list: List[WriteOrgCarbonRequestOrgDetailsList] = None,
    ):
        # 入参集
        self.org_details_list = org_details_list

    def validate(self):
        if self.org_details_list:
            for k in self.org_details_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['orgDetailsList'] = []
        if self.org_details_list is not None:
            for k in self.org_details_list:
                result['orgDetailsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.org_details_list = []
        if m.get('orgDetailsList') is not None:
            for k in m.get('orgDetailsList'):
                temp_model = WriteOrgCarbonRequestOrgDetailsList()
                self.org_details_list.append(temp_model.from_map(k))
        return self


class WriteOrgCarbonResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
        success: bool = None,
    ):
        # 请求成功返回的个数
        self.result = result
        # 请求是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WriteOrgCarbonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteOrgCarbonResponseBody = None,
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
            temp_model = WriteOrgCarbonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteUserCarbonHeaders(TeaModel):
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


class WriteUserCarbonRequestUserDetailsList(TeaModel):
    def __init__(
        self,
        action_end_time: str = None,
        action_id: str = None,
        action_start_time: str = None,
        action_type: str = None,
        carbon_amount: str = None,
        corp_id: str = None,
        dept_id: int = None,
        user_id: str = None,
        version: int = None,
    ):
        # 行为结束时间
        self.action_end_time = action_end_time
        # 系统唯一id，生成格式：userId+日期20211126
        self.action_id = action_id
        # 行为起始时间
        self.action_start_time = action_start_time
        # 碳能量行为类型，需要联系管理员添加
        self.action_type = action_type
        # 碳能量数据
        self.carbon_amount = carbon_amount
        # 钉钉组织id
        self.corp_id = corp_id
        # 钉钉部门id
        self.dept_id = dept_id
        # 钉钉用户id
        self.user_id = user_id
        # 版本，默认为1
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_end_time is not None:
            result['actionEndTime'] = self.action_end_time
        if self.action_id is not None:
            result['actionId'] = self.action_id
        if self.action_start_time is not None:
            result['actionStartTime'] = self.action_start_time
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.carbon_amount is not None:
            result['carbonAmount'] = self.carbon_amount
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionEndTime') is not None:
            self.action_end_time = m.get('actionEndTime')
        if m.get('actionId') is not None:
            self.action_id = m.get('actionId')
        if m.get('actionStartTime') is not None:
            self.action_start_time = m.get('actionStartTime')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('carbonAmount') is not None:
            self.carbon_amount = m.get('carbonAmount')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class WriteUserCarbonRequest(TeaModel):
    def __init__(
        self,
        user_details_list: List[WriteUserCarbonRequestUserDetailsList] = None,
    ):
        # 入参集
        self.user_details_list = user_details_list

    def validate(self):
        if self.user_details_list:
            for k in self.user_details_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['userDetailsList'] = []
        if self.user_details_list is not None:
            for k in self.user_details_list:
                result['userDetailsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_details_list = []
        if m.get('userDetailsList') is not None:
            for k in m.get('userDetailsList'):
                temp_model = WriteUserCarbonRequestUserDetailsList()
                self.user_details_list.append(temp_model.from_map(k))
        return self


class WriteUserCarbonResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
        success: bool = None,
    ):
        # 返回请求成功个数
        self.result = result
        # 请求是否写入成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WriteUserCarbonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteUserCarbonResponseBody = None,
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
            temp_model = WriteUserCarbonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


