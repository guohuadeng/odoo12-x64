# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AttendanceBleDevicesAddHeaders(TeaModel):
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


class AttendanceBleDevicesAddRequest(TeaModel):
    def __init__(
        self,
        device_id_list: List[int] = None,
        group_key: str = None,
        op_user_id: str = None,
    ):
        # 蓝牙设备Id列表
        self.device_id_list = device_id_list
        # 考勤组Id
        self.group_key = group_key
        # 操作人Id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id_list is not None:
            result['deviceIdList'] = self.device_id_list
        if self.group_key is not None:
            result['groupKey'] = self.group_key
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceIdList') is not None:
            self.device_id_list = m.get('deviceIdList')
        if m.get('groupKey') is not None:
            self.group_key = m.get('groupKey')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class AttendanceBleDevicesAddResponseBodyErrorListFailureList(TeaModel):
    def __init__(
        self,
        device_id: int = None,
        device_name: str = None,
        sn: str = None,
    ):
        # 蓝牙设备Id
        self.device_id = device_id
        # 蓝牙设备名称
        self.device_name = device_name
        # sn
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class AttendanceBleDevicesAddResponseBodyErrorList(TeaModel):
    def __init__(
        self,
        code: str = None,
        failure_list: List[AttendanceBleDevicesAddResponseBodyErrorListFailureList] = None,
        msg: str = None,
    ):
        # 错误code
        self.code = code
        # 失败蓝牙设备列表
        self.failure_list = failure_list
        # errorMsg
        self.msg = msg

    def validate(self):
        if self.failure_list:
            for k in self.failure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['failureList'] = []
        if self.failure_list is not None:
            for k in self.failure_list:
                result['failureList'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.failure_list = []
        if m.get('failureList') is not None:
            for k in m.get('failureList'):
                temp_model = AttendanceBleDevicesAddResponseBodyErrorListFailureList()
                self.failure_list.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AttendanceBleDevicesAddResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        device_id: int = None,
        device_name: str = None,
        sn: str = None,
    ):
        # 蓝牙设备Id
        self.device_id = device_id
        # 蓝牙设备名称
        self.device_name = device_name
        # sn
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class AttendanceBleDevicesAddResponseBody(TeaModel):
    def __init__(
        self,
        error_list: List[AttendanceBleDevicesAddResponseBodyErrorList] = None,
        success_list: List[AttendanceBleDevicesAddResponseBodySuccessList] = None,
    ):
        # 添加错误列表
        self.error_list = error_list
        # 添加成功蓝牙设备列表
        self.success_list = success_list

    def validate(self):
        if self.error_list:
            for k in self.error_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['errorList'] = []
        if self.error_list is not None:
            for k in self.error_list:
                result['errorList'].append(k.to_map() if k else None)
        result['successList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['successList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_list = []
        if m.get('errorList') is not None:
            for k in m.get('errorList'):
                temp_model = AttendanceBleDevicesAddResponseBodyErrorList()
                self.error_list.append(temp_model.from_map(k))
        self.success_list = []
        if m.get('successList') is not None:
            for k in m.get('successList'):
                temp_model = AttendanceBleDevicesAddResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class AttendanceBleDevicesAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttendanceBleDevicesAddResponseBody = None,
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
            temp_model = AttendanceBleDevicesAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttendanceBleDevicesQueryHeaders(TeaModel):
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


class AttendanceBleDevicesQueryRequest(TeaModel):
    def __init__(
        self,
        group_key: str = None,
        op_user_id: str = None,
    ):
        # 考勤组Id
        self.group_key = group_key
        # 操作人Id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_key is not None:
            result['groupKey'] = self.group_key
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupKey') is not None:
            self.group_key = m.get('groupKey')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class AttendanceBleDevicesQueryResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_id: int = None,
        device_name: str = None,
        sn: str = None,
    ):
        # 蓝牙设备Id
        self.device_id = device_id
        # 蓝牙设备名称
        self.device_name = device_name
        # sn
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class AttendanceBleDevicesQueryResponseBody(TeaModel):
    def __init__(
        self,
        result: List[AttendanceBleDevicesQueryResponseBodyResult] = None,
    ):
        # 蓝牙列表
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
                temp_model = AttendanceBleDevicesQueryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class AttendanceBleDevicesQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttendanceBleDevicesQueryResponseBody = None,
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
            temp_model = AttendanceBleDevicesQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttendanceBleDevicesRemoveHeaders(TeaModel):
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


class AttendanceBleDevicesRemoveRequest(TeaModel):
    def __init__(
        self,
        device_id_list: List[int] = None,
        group_key: str = None,
        op_user_id: str = None,
    ):
        # 蓝牙设备Id列表
        self.device_id_list = device_id_list
        # 考勤组Id
        self.group_key = group_key
        # 操作人id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id_list is not None:
            result['deviceIdList'] = self.device_id_list
        if self.group_key is not None:
            result['groupKey'] = self.group_key
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceIdList') is not None:
            self.device_id_list = m.get('deviceIdList')
        if m.get('groupKey') is not None:
            self.group_key = m.get('groupKey')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class AttendanceBleDevicesRemoveResponseBodyErrorList(TeaModel):
    def __init__(
        self,
        code: str = None,
        failure_list: List[int] = None,
        msg: str = None,
    ):
        # 错误code
        self.code = code
        # 移除失败蓝牙设备Id列表
        self.failure_list = failure_list
        # 错误信息
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.failure_list is not None:
            result['failureList'] = self.failure_list
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('failureList') is not None:
            self.failure_list = m.get('failureList')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AttendanceBleDevicesRemoveResponseBody(TeaModel):
    def __init__(
        self,
        error_list: List[AttendanceBleDevicesRemoveResponseBodyErrorList] = None,
        success_list: List[int] = None,
    ):
        # 移出错误列表
        self.error_list = error_list
        # 移除成功蓝牙设备Id列表
        self.success_list = success_list

    def validate(self):
        if self.error_list:
            for k in self.error_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['errorList'] = []
        if self.error_list is not None:
            for k in self.error_list:
                result['errorList'].append(k.to_map() if k else None)
        if self.success_list is not None:
            result['successList'] = self.success_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_list = []
        if m.get('errorList') is not None:
            for k in m.get('errorList'):
                temp_model = AttendanceBleDevicesRemoveResponseBodyErrorList()
                self.error_list.append(temp_model.from_map(k))
        if m.get('successList') is not None:
            self.success_list = m.get('successList')
        return self


class AttendanceBleDevicesRemoveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttendanceBleDevicesRemoveResponseBody = None,
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
            temp_model = AttendanceBleDevicesRemoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClosingAccountHeaders(TeaModel):
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


class CheckClosingAccountRequestUserTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class CheckClosingAccountRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        user_ids: List[str] = None,
        user_time_range: List[CheckClosingAccountRequestUserTimeRange] = None,
    ):
        # 情景
        self.biz_code = biz_code
        # 员工列表
        self.user_ids = user_ids
        # 时间段
        self.user_time_range = user_time_range

    def validate(self):
        if self.user_time_range:
            for k in self.user_time_range:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        result['userTimeRange'] = []
        if self.user_time_range is not None:
            for k in self.user_time_range:
                result['userTimeRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        self.user_time_range = []
        if m.get('userTimeRange') is not None:
            for k in m.get('userTimeRange'):
                temp_model = CheckClosingAccountRequestUserTimeRange()
                self.user_time_range.append(temp_model.from_map(k))
        return self


class CheckClosingAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        mesage: str = None,
        pass_: bool = None,
    ):
        self.code = code
        self.mesage = mesage
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.mesage is not None:
            result['mesage'] = self.mesage
        if self.pass_ is not None:
            result['pass'] = self.pass_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('mesage') is not None:
            self.mesage = m.get('mesage')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        return self


class CheckClosingAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckClosingAccountResponseBody = None,
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
            temp_model = CheckClosingAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckWritePermissionHeaders(TeaModel):
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


class CheckWritePermissionRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        entity_ids: List[int] = None,
        op_user_id: str = None,
        resource_key: str = None,
        corp_id: str = None,
    ):
        # category
        self.category = category
        # entityIds
        self.entity_ids = entity_ids
        # opUserId
        self.op_user_id = op_user_id
        # resourceKey
        self.resource_key = resource_key
        # corpId
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.entity_ids is not None:
            result['entityIds'] = self.entity_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.resource_key is not None:
            result['resourceKey'] = self.resource_key
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('entityIds') is not None:
            self.entity_ids = m.get('entityIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('resourceKey') is not None:
            self.resource_key = m.get('resourceKey')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class CheckWritePermissionResponseBody(TeaModel):
    def __init__(
        self,
        entity_permission_map: Dict[str, bool] = None,
    ):
        # entityPermissionMap
        self.entity_permission_map = entity_permission_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_permission_map is not None:
            result['entityPermissionMap'] = self.entity_permission_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityPermissionMap') is not None:
            self.entity_permission_map = m.get('entityPermissionMap')
        return self


class CheckWritePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckWritePermissionResponseBody = None,
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
            temp_model = CheckWritePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApproveHeaders(TeaModel):
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


class CreateApproveRequestPunchParam(TeaModel):
    def __init__(
        self,
        position_id: str = None,
        position_name: str = None,
        position_type: str = None,
        punch_time: int = None,
    ):
        # 地理位置标识：wifi:ssid_macAddress ble: deviceId gps:longitude_latitude
        self.position_id = position_id
        # 地理位置名称
        self.position_name = position_name
        # 地理位置类型：wifi/ble/gps
        self.position_type = position_type
        # 打卡时间，单位毫秒
        self.punch_time = punch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.position_id is not None:
            result['positionId'] = self.position_id
        if self.position_name is not None:
            result['positionName'] = self.position_name
        if self.position_type is not None:
            result['positionType'] = self.position_type
        if self.punch_time is not None:
            result['punchTime'] = self.punch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('positionId') is not None:
            self.position_id = m.get('positionId')
        if m.get('positionName') is not None:
            self.position_name = m.get('positionName')
        if m.get('positionType') is not None:
            self.position_type = m.get('positionType')
        if m.get('punchTime') is not None:
            self.punch_time = m.get('punchTime')
        return self


class CreateApproveRequest(TeaModel):
    def __init__(
        self,
        approve_id: str = None,
        op_userid: str = None,
        punch_param: CreateApproveRequestPunchParam = None,
        sub_type: str = None,
        tag_name: str = None,
        userid: str = None,
    ):
        # 三方审批单id，全局唯一
        self.approve_id = approve_id
        # 审批人员工id
        self.op_userid = op_userid
        # 审批单关联的打卡信息
        self.punch_param = punch_param
        # 子类型名称，最大长度20个字符
        self.sub_type = sub_type
        # 审批单类型名称，最大长度20个字符
        self.tag_name = tag_name
        # 员工id
        self.userid = userid

    def validate(self):
        if self.punch_param:
            self.punch_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_id is not None:
            result['approveId'] = self.approve_id
        if self.op_userid is not None:
            result['opUserid'] = self.op_userid
        if self.punch_param is not None:
            result['punchParam'] = self.punch_param.to_map()
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approveId') is not None:
            self.approve_id = m.get('approveId')
        if m.get('opUserid') is not None:
            self.op_userid = m.get('opUserid')
        if m.get('punchParam') is not None:
            temp_model = CreateApproveRequestPunchParam()
            self.punch_param = temp_model.from_map(m['punchParam'])
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class CreateApproveResponseBody(TeaModel):
    def __init__(
        self,
        dingtalk_approve_id: str = None,
    ):
        # 返回结果
        self.dingtalk_approve_id = dingtalk_approve_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dingtalk_approve_id is not None:
            result['dingtalkApproveId'] = self.dingtalk_approve_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingtalkApproveId') is not None:
            self.dingtalk_approve_id = m.get('dingtalkApproveId')
        return self


class CreateApproveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApproveResponseBody = None,
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
            temp_model = CreateApproveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DingTalkSecurityCheckHeaders(TeaModel):
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


class DingTalkSecurityCheckRequest(TeaModel):
    def __init__(
        self,
        client_ver: str = None,
        platform: str = None,
        platform_ver: str = None,
        sec: str = None,
        user_id: str = None,
    ):
        # 客户端版本号
        self.client_ver = client_ver
        # 客户端平台类型(iOS,Android)
        self.platform = platform
        # 客户端平台平台版本
        self.platform_ver = platform_ver
        # 加密字符
        self.sec = sec
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ver is not None:
            result['clientVer'] = self.client_ver
        if self.platform is not None:
            result['platform'] = self.platform
        if self.platform_ver is not None:
            result['platformVer'] = self.platform_ver
        if self.sec is not None:
            result['sec'] = self.sec
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientVer') is not None:
            self.client_ver = m.get('clientVer')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('platformVer') is not None:
            self.platform_ver = m.get('platformVer')
        if m.get('sec') is not None:
            self.sec = m.get('sec')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DingTalkSecurityCheckResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_risk: bool = None,
        risk_info: Dict[str, str] = None,
    ):
        # 是否有风险
        self.has_risk = has_risk
        # 风险信息
        self.risk_info = risk_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_risk is not None:
            result['hasRisk'] = self.has_risk
        if self.risk_info is not None:
            result['riskInfo'] = self.risk_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasRisk') is not None:
            self.has_risk = m.get('hasRisk')
        if m.get('riskInfo') is not None:
            self.risk_info = m.get('riskInfo')
        return self


class DingTalkSecurityCheckResponseBody(TeaModel):
    def __init__(
        self,
        result: DingTalkSecurityCheckResponseBodyResult = None,
    ):
        # 返回参数
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = DingTalkSecurityCheckResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DingTalkSecurityCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DingTalkSecurityCheckResponseBody = None,
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
            temp_model = DingTalkSecurityCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClosingAccountsHeaders(TeaModel):
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


class GetClosingAccountsRequest(TeaModel):
    def __init__(
        self,
        user_ids: List[str] = None,
    ):
        # 人员列表
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self


class GetClosingAccountsResponseBodyResultClosingAccountModel(TeaModel):
    def __init__(
        self,
        closing_day: int = None,
        closing_hour_minutes: int = None,
        end_day: int = None,
        end_month: int = None,
        start_day: int = None,
        start_month: int = None,
    ):
        # 封账时间-日
        self.closing_day = closing_day
        # 封账时间-时分
        self.closing_hour_minutes = closing_hour_minutes
        # 封账范围-结束日
        self.end_day = end_day
        # 封账范围-结束月
        self.end_month = end_month
        # 封账范围-开始日
        self.start_day = start_day
        # 封账范围-开始月
        self.start_month = start_month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.closing_day is not None:
            result['closingDay'] = self.closing_day
        if self.closing_hour_minutes is not None:
            result['closingHourMinutes'] = self.closing_hour_minutes
        if self.end_day is not None:
            result['endDay'] = self.end_day
        if self.end_month is not None:
            result['endMonth'] = self.end_month
        if self.start_day is not None:
            result['startDay'] = self.start_day
        if self.start_month is not None:
            result['startMonth'] = self.start_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('closingDay') is not None:
            self.closing_day = m.get('closingDay')
        if m.get('closingHourMinutes') is not None:
            self.closing_hour_minutes = m.get('closingHourMinutes')
        if m.get('endDay') is not None:
            self.end_day = m.get('endDay')
        if m.get('endMonth') is not None:
            self.end_month = m.get('endMonth')
        if m.get('startDay') is not None:
            self.start_day = m.get('startDay')
        if m.get('startMonth') is not None:
            self.start_month = m.get('startMonth')
        return self


class GetClosingAccountsResponseBodyResultUnsealClosingAccountModel(TeaModel):
    def __init__(
        self,
        invalid_time_stamp: int = None,
    ):
        # 解封时间点
        self.invalid_time_stamp = invalid_time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_time_stamp is not None:
            result['invalidTimeStamp'] = self.invalid_time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('invalidTimeStamp') is not None:
            self.invalid_time_stamp = m.get('invalidTimeStamp')
        return self


class GetClosingAccountsResponseBodyResult(TeaModel):
    def __init__(
        self,
        closing_account_model: GetClosingAccountsResponseBodyResultClosingAccountModel = None,
        switch_on: bool = None,
        unseal_closing_account_model: GetClosingAccountsResponseBodyResultUnsealClosingAccountModel = None,
        user_id: str = None,
    ):
        # 封账规则
        self.closing_account_model = closing_account_model
        # 开关
        self.switch_on = switch_on
        # 解封规则
        self.unseal_closing_account_model = unseal_closing_account_model
        # 人员ID
        self.user_id = user_id

    def validate(self):
        if self.closing_account_model:
            self.closing_account_model.validate()
        if self.unseal_closing_account_model:
            self.unseal_closing_account_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.closing_account_model is not None:
            result['closingAccountModel'] = self.closing_account_model.to_map()
        if self.switch_on is not None:
            result['switchOn'] = self.switch_on
        if self.unseal_closing_account_model is not None:
            result['unsealClosingAccountModel'] = self.unseal_closing_account_model.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('closingAccountModel') is not None:
            temp_model = GetClosingAccountsResponseBodyResultClosingAccountModel()
            self.closing_account_model = temp_model.from_map(m['closingAccountModel'])
        if m.get('switchOn') is not None:
            self.switch_on = m.get('switchOn')
        if m.get('unsealClosingAccountModel') is not None:
            temp_model = GetClosingAccountsResponseBodyResultUnsealClosingAccountModel()
            self.unseal_closing_account_model = temp_model.from_map(m['unsealClosingAccountModel'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetClosingAccountsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetClosingAccountsResponseBodyResult] = None,
    ):
        # 规则列表
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
                temp_model = GetClosingAccountsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetClosingAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetClosingAccountsResponseBody = None,
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
            temp_model = GetClosingAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMachineHeaders(TeaModel):
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


class GetMachineResponseBodyResultMachineBluetoothVO(TeaModel):
    def __init__(
        self,
        address: str = None,
        bluetooth_check_with_face: bool = None,
        bluetooth_distance_mode: str = None,
        bluetooth_distance_mode_desc: str = None,
        bluetooth_value: bool = None,
        latitude: float = None,
        limit_user_device_count: bool = None,
        longitude: float = None,
        monitor_location_abnormal: bool = None,
        user_device_count: int = None,
    ):
        # 地址位置描述
        self.address = address
        # 蓝牙打卡人脸识别开关值
        self.bluetooth_check_with_face = bluetooth_check_with_face
        # 蓝牙打卡范围
        self.bluetooth_distance_mode = bluetooth_distance_mode
        # 蓝牙打卡范围描述
        self.bluetooth_distance_mode_desc = bluetooth_distance_mode_desc
        # 蓝牙打卡开关
        self.bluetooth_value = bluetooth_value
        # 纬度
        self.latitude = latitude
        # 是否限制员工常用手机
        self.limit_user_device_count = limit_user_device_count
        # 经度
        self.longitude = longitude
        # 是否打开位置异常监控
        self.monitor_location_abnormal = monitor_location_abnormal
        # 员工常用手机数量
        self.user_device_count = user_device_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.bluetooth_check_with_face is not None:
            result['bluetoothCheckWithFace'] = self.bluetooth_check_with_face
        if self.bluetooth_distance_mode is not None:
            result['bluetoothDistanceMode'] = self.bluetooth_distance_mode
        if self.bluetooth_distance_mode_desc is not None:
            result['bluetoothDistanceModeDesc'] = self.bluetooth_distance_mode_desc
        if self.bluetooth_value is not None:
            result['bluetoothValue'] = self.bluetooth_value
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.limit_user_device_count is not None:
            result['limitUserDeviceCount'] = self.limit_user_device_count
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.monitor_location_abnormal is not None:
            result['monitorLocationAbnormal'] = self.monitor_location_abnormal
        if self.user_device_count is not None:
            result['userDeviceCount'] = self.user_device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('bluetoothCheckWithFace') is not None:
            self.bluetooth_check_with_face = m.get('bluetoothCheckWithFace')
        if m.get('bluetoothDistanceMode') is not None:
            self.bluetooth_distance_mode = m.get('bluetoothDistanceMode')
        if m.get('bluetoothDistanceModeDesc') is not None:
            self.bluetooth_distance_mode_desc = m.get('bluetoothDistanceModeDesc')
        if m.get('bluetoothValue') is not None:
            self.bluetooth_value = m.get('bluetoothValue')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('limitUserDeviceCount') is not None:
            self.limit_user_device_count = m.get('limitUserDeviceCount')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('monitorLocationAbnormal') is not None:
            self.monitor_location_abnormal = m.get('monitorLocationAbnormal')
        if m.get('userDeviceCount') is not None:
            self.user_device_count = m.get('userDeviceCount')
        return self


class GetMachineResponseBodyResult(TeaModel):
    def __init__(
        self,
        atm_manager_list: List[str] = None,
        dev_id: int = None,
        device_id: str = None,
        device_name: str = None,
        device_sn: str = None,
        machine_bluetooth_vo: GetMachineResponseBodyResultMachineBluetoothVO = None,
        max_face: int = None,
        net_status: str = None,
        product_name: str = None,
        product_version: str = None,
        voice_mode: int = None,
    ):
        # 设备管理员列表
        self.atm_manager_list = atm_manager_list
        # 设备id (deviceId)
        self.dev_id = dev_id
        # 设备id (deviceUid加密之后)
        self.device_id = device_id
        # 设备名称
        self.device_name = device_name
        # 设备sn号
        self.device_sn = device_sn
        # 考勤机蓝牙相关设置信息
        self.machine_bluetooth_vo = machine_bluetooth_vo
        # 人脸容量
        self.max_face = max_face
        # 网络状态
        self.net_status = net_status
        # 设备类型名称
        self.product_name = product_name
        # 固件版本
        self.product_version = product_version
        # 音量模式
        self.voice_mode = voice_mode

    def validate(self):
        if self.machine_bluetooth_vo:
            self.machine_bluetooth_vo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atm_manager_list is not None:
            result['atmManagerList'] = self.atm_manager_list
        if self.dev_id is not None:
            result['devId'] = self.dev_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.device_sn is not None:
            result['deviceSn'] = self.device_sn
        if self.machine_bluetooth_vo is not None:
            result['machineBluetoothVO'] = self.machine_bluetooth_vo.to_map()
        if self.max_face is not None:
            result['maxFace'] = self.max_face
        if self.net_status is not None:
            result['netStatus'] = self.net_status
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.voice_mode is not None:
            result['voiceMode'] = self.voice_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atmManagerList') is not None:
            self.atm_manager_list = m.get('atmManagerList')
        if m.get('devId') is not None:
            self.dev_id = m.get('devId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('deviceSn') is not None:
            self.device_sn = m.get('deviceSn')
        if m.get('machineBluetoothVO') is not None:
            temp_model = GetMachineResponseBodyResultMachineBluetoothVO()
            self.machine_bluetooth_vo = temp_model.from_map(m['machineBluetoothVO'])
        if m.get('maxFace') is not None:
            self.max_face = m.get('maxFace')
        if m.get('netStatus') is not None:
            self.net_status = m.get('netStatus')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('voiceMode') is not None:
            self.voice_mode = m.get('voiceMode')
        return self


class GetMachineResponseBody(TeaModel):
    def __init__(
        self,
        result: GetMachineResponseBodyResult = None,
    ):
        # 查询结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetMachineResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMachineResponseBody = None,
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
            temp_model = GetMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMachineUserHeaders(TeaModel):
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


class GetMachineUserRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
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


class GetMachineUserResponseBodyResultUserList(TeaModel):
    def __init__(
        self,
        has_face: bool = None,
        name: str = None,
        user_id: str = None,
    ):
        self.has_face = has_face
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_face is not None:
            result['hasFace'] = self.has_face
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasFace') is not None:
            self.has_face = m.get('hasFace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetMachineUserResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        user_list: List[GetMachineUserResponseBodyResultUserList] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['userList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['userList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.user_list = []
        if m.get('userList') is not None:
            for k in m.get('userList'):
                temp_model = GetMachineUserResponseBodyResultUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class GetMachineUserResponseBody(TeaModel):
    def __init__(
        self,
        result: GetMachineUserResponseBodyResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetMachineUserResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetMachineUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMachineUserResponseBody = None,
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
            temp_model = GetMachineUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOvertimeSettingHeaders(TeaModel):
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


class GetOvertimeSettingRequest(TeaModel):
    def __init__(
        self,
        overtime_setting_ids: List[int] = None,
    ):
        self.overtime_setting_ids = overtime_setting_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overtime_setting_ids is not None:
            result['overtimeSettingIds'] = self.overtime_setting_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('overtimeSettingIds') is not None:
            self.overtime_setting_ids = m.get('overtimeSettingIds')
        return self


class GetOvertimeSettingResponseBodyResultOvertimeDivisions(TeaModel):
    def __init__(
        self,
        next_day_type: str = None,
        previous_day_type: str = None,
        time_split_point: str = None,
    ):
        # 后一日类型
        self.next_day_type = next_day_type
        # 前一日类型
        self.previous_day_type = previous_day_type
        # 分割时间点
        self.time_split_point = time_split_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_day_type is not None:
            result['nextDayType'] = self.next_day_type
        if self.previous_day_type is not None:
            result['previousDayType'] = self.previous_day_type
        if self.time_split_point is not None:
            result['timeSplitPoint'] = self.time_split_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextDayType') is not None:
            self.next_day_type = m.get('nextDayType')
        if m.get('previousDayType') is not None:
            self.previous_day_type = m.get('previousDayType')
        if m.get('timeSplitPoint') is not None:
            self.time_split_point = m.get('timeSplitPoint')
        return self


class GetOvertimeSettingResponseBodyResultWarningSettings(TeaModel):
    def __init__(
        self,
        action: str = None,
        threshold: int = None,
        time: str = None,
    ):
        # 风险预警 或 最大加班时间
        self.action = action
        # 提醒阈值
        self.threshold = threshold
        # 预警类型
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class ResultDurationSettingsValueSkipTimeByFrames(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        valid: bool = None,
    ):
        # 开始时间，格式为"HH:mm"
        self.start_time = start_time
        # 结束时间，格式为"HH:mm"
        self.end_time = end_time
        # 是否生效
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class ResultDurationSettingsValueSkipTimeByDurations(TeaModel):
    def __init__(
        self,
        duration: int = None,
        minus: int = None,
    ):
        # 每天加班满 x小时，单位 秒
        self.duration = duration
        # 扣除 x小时，单位 秒
        self.minus = minus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.minus is not None:
            result['minus'] = self.minus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('minus') is not None:
            self.minus = m.get('minus')
        return self


class ResultDurationSettingsValue(TeaModel):
    def __init__(
        self,
        calc_type: int = None,
        duration_type: int = None,
        overtime_redress: bool = None,
        settings: Dict[str, Any] = None,
        overtime_redress_by: str = None,
        vacation_rate: float = None,
        skip_time: str = None,
        skip_time_by_frames: List[ResultDurationSettingsValueSkipTimeByFrames] = None,
        skip_time_by_durations: List[ResultDurationSettingsValueSkipTimeByDurations] = None,
        holiday_plan_overtime_redress: bool = None,
        holiday_plan_overtime_redress_by: str = None,
        holiday_plan_vacation_rate: float = None,
    ):
        self.calc_type = calc_type
        self.duration_type = duration_type
        # 加班时长计为调休或加班费开关
        self.overtime_redress = overtime_redress
        # 加班开始时间 或 最小加班时间
        self.settings = settings
        # 加班时长计为方式
        self.overtime_redress_by = overtime_redress_by
        # 调休时长计算
        self.vacation_rate = vacation_rate
        # 扣除休息时间
        self.skip_time = skip_time
        # 休息时段
        self.skip_time_by_frames = skip_time_by_frames
        # 加班时长
        self.skip_time_by_durations = skip_time_by_durations
        # 休息日或节假日排班加班时长计为调休或加班费开关
        self.holiday_plan_overtime_redress = holiday_plan_overtime_redress
        # 休息日或节假日排班加班时长计为方式
        self.holiday_plan_overtime_redress_by = holiday_plan_overtime_redress_by
        # 休息日或节假日排班调休时长计算
        self.holiday_plan_vacation_rate = holiday_plan_vacation_rate

    def validate(self):
        if self.skip_time_by_frames:
            for k in self.skip_time_by_frames:
                if k:
                    k.validate()
        if self.skip_time_by_durations:
            for k in self.skip_time_by_durations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calc_type is not None:
            result['calcType'] = self.calc_type
        if self.duration_type is not None:
            result['durationType'] = self.duration_type
        if self.overtime_redress is not None:
            result['overtimeRedress'] = self.overtime_redress
        if self.settings is not None:
            result['settings'] = self.settings
        if self.overtime_redress_by is not None:
            result['overtimeRedressBy'] = self.overtime_redress_by
        if self.vacation_rate is not None:
            result['vacationRate'] = self.vacation_rate
        if self.skip_time is not None:
            result['skipTime'] = self.skip_time
        result['skipTimeByFrames'] = []
        if self.skip_time_by_frames is not None:
            for k in self.skip_time_by_frames:
                result['skipTimeByFrames'].append(k.to_map() if k else None)
        result['skipTimeByDurations'] = []
        if self.skip_time_by_durations is not None:
            for k in self.skip_time_by_durations:
                result['skipTimeByDurations'].append(k.to_map() if k else None)
        if self.holiday_plan_overtime_redress is not None:
            result['holidayPlanOvertimeRedress'] = self.holiday_plan_overtime_redress
        if self.holiday_plan_overtime_redress_by is not None:
            result['holidayPlanOvertimeRedressBy'] = self.holiday_plan_overtime_redress_by
        if self.holiday_plan_vacation_rate is not None:
            result['holidayPlanVacationRate'] = self.holiday_plan_vacation_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('calcType') is not None:
            self.calc_type = m.get('calcType')
        if m.get('durationType') is not None:
            self.duration_type = m.get('durationType')
        if m.get('overtimeRedress') is not None:
            self.overtime_redress = m.get('overtimeRedress')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('overtimeRedressBy') is not None:
            self.overtime_redress_by = m.get('overtimeRedressBy')
        if m.get('vacationRate') is not None:
            self.vacation_rate = m.get('vacationRate')
        if m.get('skipTime') is not None:
            self.skip_time = m.get('skipTime')
        self.skip_time_by_frames = []
        if m.get('skipTimeByFrames') is not None:
            for k in m.get('skipTimeByFrames'):
                temp_model = ResultDurationSettingsValueSkipTimeByFrames()
                self.skip_time_by_frames.append(temp_model.from_map(k))
        self.skip_time_by_durations = []
        if m.get('skipTimeByDurations') is not None:
            for k in m.get('skipTimeByDurations'):
                temp_model = ResultDurationSettingsValueSkipTimeByDurations()
                self.skip_time_by_durations.append(temp_model.from_map(k))
        if m.get('holidayPlanOvertimeRedress') is not None:
            self.holiday_plan_overtime_redress = m.get('holidayPlanOvertimeRedress')
        if m.get('holidayPlanOvertimeRedressBy') is not None:
            self.holiday_plan_overtime_redress_by = m.get('holidayPlanOvertimeRedressBy')
        if m.get('holidayPlanVacationRate') is not None:
            self.holiday_plan_vacation_rate = m.get('holidayPlanVacationRate')
        return self


class GetOvertimeSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        default: bool = None,
        duration_settings: Dict[str, ResultDurationSettingsValue] = None,
        id: int = None,
        name: str = None,
        overtime_divisions: List[GetOvertimeSettingResponseBodyResultOvertimeDivisions] = None,
        setting_id: int = None,
        step_type: int = None,
        step_value: float = None,
        warning_settings: List[GetOvertimeSettingResponseBodyResultWarningSettings] = None,
        work_minutes_per_day: int = None,
    ):
        # 是否默认
        self.default = default
        self.duration_settings = duration_settings
        # 历史加班规则设置id
        self.id = id
        # 规则名称
        self.name = name
        # 时间分割规则
        self.overtime_divisions = overtime_divisions
        # 设置id
        self.setting_id = setting_id
        # 加班时长单位
        self.step_type = step_type
        # 加班时长是否取整 单位 小时
        self.step_value = step_value
        self.warning_settings = warning_settings
        # 日折算时长 单位：分钟
        self.work_minutes_per_day = work_minutes_per_day

    def validate(self):
        if self.duration_settings:
            for v in self.duration_settings.values():
                if v:
                    v.validate()
        if self.overtime_divisions:
            for k in self.overtime_divisions:
                if k:
                    k.validate()
        if self.warning_settings:
            for k in self.warning_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['default'] = self.default
        result['durationSettings'] = {}
        if self.duration_settings is not None:
            for k, v in self.duration_settings.items():
                result['durationSettings'][k] = v.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        result['overtimeDivisions'] = []
        if self.overtime_divisions is not None:
            for k in self.overtime_divisions:
                result['overtimeDivisions'].append(k.to_map() if k else None)
        if self.setting_id is not None:
            result['settingId'] = self.setting_id
        if self.step_type is not None:
            result['stepType'] = self.step_type
        if self.step_value is not None:
            result['stepValue'] = self.step_value
        result['warningSettings'] = []
        if self.warning_settings is not None:
            for k in self.warning_settings:
                result['warningSettings'].append(k.to_map() if k else None)
        if self.work_minutes_per_day is not None:
            result['workMinutesPerDay'] = self.work_minutes_per_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')
        self.duration_settings = {}
        if m.get('durationSettings') is not None:
            for k, v in m.get('durationSettings').items():
                temp_model = ResultDurationSettingsValue()
                self.duration_settings[k] = temp_model.from_map(v)
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.overtime_divisions = []
        if m.get('overtimeDivisions') is not None:
            for k in m.get('overtimeDivisions'):
                temp_model = GetOvertimeSettingResponseBodyResultOvertimeDivisions()
                self.overtime_divisions.append(temp_model.from_map(k))
        if m.get('settingId') is not None:
            self.setting_id = m.get('settingId')
        if m.get('stepType') is not None:
            self.step_type = m.get('stepType')
        if m.get('stepValue') is not None:
            self.step_value = m.get('stepValue')
        self.warning_settings = []
        if m.get('warningSettings') is not None:
            for k in m.get('warningSettings'):
                temp_model = GetOvertimeSettingResponseBodyResultWarningSettings()
                self.warning_settings.append(temp_model.from_map(k))
        if m.get('workMinutesPerDay') is not None:
            self.work_minutes_per_day = m.get('workMinutesPerDay')
        return self


class GetOvertimeSettingResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetOvertimeSettingResponseBodyResult] = None,
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
                temp_model = GetOvertimeSettingResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetOvertimeSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOvertimeSettingResponseBody = None,
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
            temp_model = GetOvertimeSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserHolidaysHeaders(TeaModel):
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


class GetUserHolidaysRequest(TeaModel):
    def __init__(
        self,
        user_ids: List[str] = None,
        work_date_from: int = None,
        work_date_to: int = None,
    ):
        # 员工列表
        self.user_ids = user_ids
        # 开始日期
        self.work_date_from = work_date_from
        # 结束日期
        self.work_date_to = work_date_to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        if self.work_date_from is not None:
            result['workDateFrom'] = self.work_date_from
        if self.work_date_to is not None:
            result['workDateTo'] = self.work_date_to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        if m.get('workDateFrom') is not None:
            self.work_date_from = m.get('workDateFrom')
        if m.get('workDateTo') is not None:
            self.work_date_to = m.get('workDateTo')
        return self


class GetUserHolidaysResponseBodyResultHolidays(TeaModel):
    def __init__(
        self,
        holiday_name: str = None,
        holiday_type: str = None,
        real_work_date: int = None,
        work_date: int = None,
    ):
        # 假期名称
        self.holiday_name = holiday_name
        # 假期类型，festival：法定节假日；rest：调休日；overtime：加班日；
        self.holiday_type = holiday_type
        # 补休日，只有假期类型为加班日时才有值
        self.real_work_date = real_work_date
        # 日期
        self.work_date = work_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.holiday_name is not None:
            result['holidayName'] = self.holiday_name
        if self.holiday_type is not None:
            result['holidayType'] = self.holiday_type
        if self.real_work_date is not None:
            result['realWorkDate'] = self.real_work_date
        if self.work_date is not None:
            result['workDate'] = self.work_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('holidayName') is not None:
            self.holiday_name = m.get('holidayName')
        if m.get('holidayType') is not None:
            self.holiday_type = m.get('holidayType')
        if m.get('realWorkDate') is not None:
            self.real_work_date = m.get('realWorkDate')
        if m.get('workDate') is not None:
            self.work_date = m.get('workDate')
        return self


class GetUserHolidaysResponseBodyResult(TeaModel):
    def __init__(
        self,
        holidays: List[GetUserHolidaysResponseBodyResultHolidays] = None,
        user_id: str = None,
    ):
        # 假期列表
        self.holidays = holidays
        # 员工id
        self.user_id = user_id

    def validate(self):
        if self.holidays:
            for k in self.holidays:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['holidays'] = []
        if self.holidays is not None:
            for k in self.holidays:
                result['holidays'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.holidays = []
        if m.get('holidays') is not None:
            for k in m.get('holidays'):
                temp_model = GetUserHolidaysResponseBodyResultHolidays()
                self.holidays.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserHolidaysResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetUserHolidaysResponseBodyResult] = None,
    ):
        # 员工假期列表
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
                temp_model = GetUserHolidaysResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetUserHolidaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserHolidaysResponseBody = None,
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
            temp_model = GetUserHolidaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncScheduleInfoHeaders(TeaModel):
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


class SyncScheduleInfoRequestScheduleInfos(TeaModel):
    def __init__(
        self,
        plan_id: int = None,
        position_keys: List[str] = None,
        retain_attendance_check: bool = None,
        wifi_keys: List[str] = None,
    ):
        self.plan_id = plan_id
        self.position_keys = position_keys
        self.retain_attendance_check = retain_attendance_check
        self.wifi_keys = wifi_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.position_keys is not None:
            result['positionKeys'] = self.position_keys
        if self.retain_attendance_check is not None:
            result['retainAttendanceCheck'] = self.retain_attendance_check
        if self.wifi_keys is not None:
            result['wifiKeys'] = self.wifi_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('positionKeys') is not None:
            self.position_keys = m.get('positionKeys')
        if m.get('retainAttendanceCheck') is not None:
            self.retain_attendance_check = m.get('retainAttendanceCheck')
        if m.get('wifiKeys') is not None:
            self.wifi_keys = m.get('wifiKeys')
        return self


class SyncScheduleInfoRequest(TeaModel):
    def __init__(
        self,
        op_user_id: str = None,
        schedule_infos: List[SyncScheduleInfoRequestScheduleInfos] = None,
    ):
        self.op_user_id = op_user_id
        self.schedule_infos = schedule_infos

    def validate(self):
        if self.schedule_infos:
            for k in self.schedule_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        result['scheduleInfos'] = []
        if self.schedule_infos is not None:
            for k in self.schedule_infos:
                result['scheduleInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        self.schedule_infos = []
        if m.get('scheduleInfos') is not None:
            for k in m.get('scheduleInfos'):
                temp_model = SyncScheduleInfoRequestScheduleInfos()
                self.schedule_infos.append(temp_model.from_map(k))
        return self


class SyncScheduleInfoResponse(TeaModel):
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


