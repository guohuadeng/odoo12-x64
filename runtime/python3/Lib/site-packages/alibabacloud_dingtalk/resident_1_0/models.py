# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddPointHeaders(TeaModel):
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


class AddPointRequest(TeaModel):
    def __init__(
        self,
        action_time: int = None,
        is_circle: bool = None,
        rule_code: str = None,
        rule_name: str = None,
        score: int = None,
        user_id: str = None,
        uuid: str = None,
    ):
        # 增加积分的时间戳毫秒数，如果为空使用系统当前毫秒数
        self.action_time = action_time
        # 是否查询全员圈积分
        self.is_circle = is_circle
        # 规则代码（可空）,如果不为空的话，score值使用ruleCode对应的score增加分数
        self.rule_code = rule_code
        # 规则名字
        self.rule_name = rule_name
        # 本次增加积分：正数表示增加/负数表示扣减
        self.score = score
        # 成员id
        self.user_id = user_id
        # 加积分的唯一幂等标志
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.is_circle is not None:
            result['isCircle'] = self.is_circle
        if self.rule_code is not None:
            result['ruleCode'] = self.rule_code
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.score is not None:
            result['score'] = self.score
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('isCircle') is not None:
            self.is_circle = m.get('isCircle')
        if m.get('ruleCode') is not None:
            self.rule_code = m.get('ruleCode')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class AddPointResponse(TeaModel):
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


class AddResidentDepartmentHeaders(TeaModel):
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


class AddResidentDepartmentRequest(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        is_residence_group: bool = None,
        parent_department_id: int = None,
    ):
        # 部门名字
        self.department_name = department_name
        # 是否为组
        self.is_residence_group = is_residence_group
        # 父部门id
        self.parent_department_id = parent_department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.is_residence_group is not None:
            result['isResidenceGroup'] = self.is_residence_group
        if self.parent_department_id is not None:
            result['parentDepartmentId'] = self.parent_department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('isResidenceGroup') is not None:
            self.is_residence_group = m.get('isResidenceGroup')
        if m.get('parentDepartmentId') is not None:
            self.parent_department_id = m.get('parentDepartmentId')
        return self


class AddResidentDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # 创建成功的deptId
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


class AddResidentDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddResidentDepartmentResponseBody = None,
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
            temp_model = AddResidentDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddResidentUsersHeaders(TeaModel):
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


class AddResidentUsersRequestExtField(TeaModel):
    def __init__(
        self,
        item_name: str = None,
        item_value: str = None,
    ):
        # 扩展字段名字
        self.item_name = item_name
        # 扩展字段值
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_name is not None:
            result['itemName'] = self.item_name
        if self.item_value is not None:
            result['itemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')
        if m.get('itemValue') is not None:
            self.item_value = m.get('itemValue')
        return self


class AddResidentUsersRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        department_id: int = None,
        ext_field: List[AddResidentUsersRequestExtField] = None,
        is_leaseholder: bool = None,
        mobile: str = None,
        relate_type: str = None,
        user_name: str = None,
    ):
        # 家庭住址
        self.address = address
        # 户/租户部门id
        self.department_id = department_id
        # 扩展字段（包括身份证/性别/民族）
        self.ext_field = ext_field
        # 是否是租客
        self.is_leaseholder = is_leaseholder
        # 手机号码
        self.mobile = mobile
        # 与户主的关系
        self.relate_type = relate_type
        # 居民名字
        self.user_name = user_name

    def validate(self):
        if self.ext_field:
            for k in self.ext_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        result['extField'] = []
        if self.ext_field is not None:
            for k in self.ext_field:
                result['extField'].append(k.to_map() if k else None)
        if self.is_leaseholder is not None:
            result['isLeaseholder'] = self.is_leaseholder
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.relate_type is not None:
            result['relateType'] = self.relate_type
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        self.ext_field = []
        if m.get('extField') is not None:
            for k in m.get('extField'):
                temp_model = AddResidentUsersRequestExtField()
                self.ext_field.append(temp_model.from_map(k))
        if m.get('isLeaseholder') is not None:
            self.is_leaseholder = m.get('isLeaseholder')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('relateType') is not None:
            self.relate_type = m.get('relateType')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class AddResidentUsersResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 创建成功的userId
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


class AddResidentUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddResidentUsersResponseBody = None,
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
            temp_model = AddResidentUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResidentBlackBoardHeaders(TeaModel):
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


class CreateResidentBlackBoardRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        media_id: str = None,
        send_time: str = None,
        title: str = None,
    ):
        self.context = context
        self.media_id = media_id
        # 格式yyyy-MM-dd HH:mm:ss
        self.send_time = send_time
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.send_time is not None:
            result['sendTime'] = self.send_time
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            self.context = m.get('context')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('sendTime') is not None:
            self.send_time = m.get('sendTime')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateResidentBlackBoardResponseBody(TeaModel):
    def __init__(
        self,
        black_board_id: str = None,
    ):
        self.black_board_id = black_board_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_board_id is not None:
            result['blackBoardId'] = self.black_board_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blackBoardId') is not None:
            self.black_board_id = m.get('blackBoardId')
        return self


class CreateResidentBlackBoardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResidentBlackBoardResponseBody = None,
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
            temp_model = CreateResidentBlackBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResidentBlackBoardHeaders(TeaModel):
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


class DeleteResidentBlackBoardRequest(TeaModel):
    def __init__(
        self,
        blackboard_id: str = None,
    ):
        self.blackboard_id = blackboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackboard_id is not None:
            result['blackboardId'] = self.blackboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blackboardId') is not None:
            self.blackboard_id = m.get('blackboardId')
        return self


class DeleteResidentBlackBoardResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
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


class DeleteResidentBlackBoardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteResidentBlackBoardResponseBody = None,
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
            temp_model = DeleteResidentBlackBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResidentDepartmentHeaders(TeaModel):
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


class DeleteResidentDepartmentRequest(TeaModel):
    def __init__(
        self,
        department_id: int = None,
    ):
        # 组/户id
        self.department_id = department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        return self


class DeleteResidentDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否删除成功
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


class DeleteResidentDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteResidentDepartmentResponseBody = None,
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
            temp_model = DeleteResidentDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationIdHeaders(TeaModel):
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


class GetConversationIdRequest(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
    ):
        self.chat_id = chat_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        return self


class GetConversationIdResponseBody(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
    ):
        self.open_conversation_id = open_conversation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        return self


class GetConversationIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConversationIdResponseBody = None,
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
            temp_model = GetConversationIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndustryTypeHeaders(TeaModel):
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


class GetIndustryTypeResponseBody(TeaModel):
    def __init__(
        self,
        industry_type: str = None,
    ):
        # 行业类型
        self.industry_type = industry_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry_type is not None:
            result['industryType'] = self.industry_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industryType') is not None:
            self.industry_type = m.get('industryType')
        return self


class GetIndustryTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIndustryTypeResponseBody = None,
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
            temp_model = GetIndustryTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPropertyInfoHeaders(TeaModel):
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


class GetPropertyInfoRequest(TeaModel):
    def __init__(
        self,
        property_corp_id: str = None,
    ):
        # dingCropId
        self.property_corp_id = property_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_corp_id is not None:
            result['propertyCorpId'] = self.property_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyCorpId') is not None:
            self.property_corp_id = m.get('propertyCorpId')
        return self


class GetPropertyInfoResponseBody(TeaModel):
    def __init__(
        self,
        admin_name: str = None,
        admin_user_id: str = None,
        name: str = None,
        org_id: int = None,
        unified_social_credit: str = None,
    ):
        self.admin_name = admin_name
        self.admin_user_id = admin_user_id
        self.name = name
        self.org_id = org_id
        self.unified_social_credit = unified_social_credit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_name is not None:
            result['adminName'] = self.admin_name
        if self.admin_user_id is not None:
            result['adminUserId'] = self.admin_user_id
        if self.name is not None:
            result['name'] = self.name
        if self.org_id is not None:
            result['orgId'] = self.org_id
        if self.unified_social_credit is not None:
            result['unifiedSocialCredit'] = self.unified_social_credit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adminName') is not None:
            self.admin_name = m.get('adminName')
        if m.get('adminUserId') is not None:
            self.admin_user_id = m.get('adminUserId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')
        if m.get('unifiedSocialCredit') is not None:
            self.unified_social_credit = m.get('unifiedSocialCredit')
        return self


class GetPropertyInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPropertyInfoResponseBody = None,
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
            temp_model = GetPropertyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResidentInfoHeaders(TeaModel):
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


class GetResidentInfoRequest(TeaModel):
    def __init__(
        self,
        resident_corp_id: str = None,
    ):
        self.resident_corp_id = resident_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resident_corp_id is not None:
            result['residentCorpId'] = self.resident_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('residentCorpId') is not None:
            self.resident_corp_id = m.get('residentCorpId')
        return self


class GetResidentInfoResponseBodyProjectManager(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # 人员唯一标识
        self.user_id = user_id
        # 姓名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetResidentInfoResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        all_user_group_open_conversation_id: str = None,
        all_user_group_owner_user_id: str = None,
        building_area: float = None,
        city_id: int = None,
        contact_mode: int = None,
        county_id: int = None,
        delivery_time: int = None,
        location: str = None,
        name: str = None,
        project_manager: GetResidentInfoResponseBodyProjectManager = None,
        property_dept_group_open_conversation_id: str = None,
        property_dept_group_owner_user_id: str = None,
        prov_id: int = None,
        scope_east: str = None,
        scope_north: str = None,
        scope_south: str = None,
        scope_west: str = None,
        telephone: str = None,
        town_id: int = None,
        type: int = None,
    ):
        # 小区地址
        self.address = address
        # 全员群opencid
        self.all_user_group_open_conversation_id = all_user_group_open_conversation_id
        # 全员群群主 userid
        self.all_user_group_owner_user_id = all_user_group_owner_user_id
        self.building_area = building_area
        # 小区归属的市的id
        self.city_id = city_id
        # 通信录模式:0标准/1自定义
        self.contact_mode = contact_mode
        # 小区归属的区/县的id
        self.county_id = county_id
        # 交付时间
        self.delivery_time = delivery_time
        # 经纬度，格式：经度,纬度
        self.location = location
        # 小区名称
        self.name = name
        self.project_manager = project_manager
        # 物业部门群cid
        self.property_dept_group_open_conversation_id = property_dept_group_open_conversation_id
        # 物业部门群主userid
        self.property_dept_group_owner_user_id = property_dept_group_owner_user_id
        # 小区归属的省的id
        self.prov_id = prov_id
        # 物业管理范围-东
        self.scope_east = scope_east
        # 物业管理范围-北
        self.scope_north = scope_north
        # 物业管理范围-南
        self.scope_south = scope_south
        # 物业管理范围-西
        self.scope_west = scope_west
        # 物业电话
        self.telephone = telephone
        # 小区归属的街道/镇的id
        self.town_id = town_id
        # 1纯住宅；2:商住混合；3:办公；4:办公商业混合；5:商业；6:公共场所；7:其他
        self.type = type

    def validate(self):
        if self.project_manager:
            self.project_manager.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.all_user_group_open_conversation_id is not None:
            result['allUserGroupOpenConversationId'] = self.all_user_group_open_conversation_id
        if self.all_user_group_owner_user_id is not None:
            result['allUserGroupOwnerUserId'] = self.all_user_group_owner_user_id
        if self.building_area is not None:
            result['buildingArea'] = self.building_area
        if self.city_id is not None:
            result['cityId'] = self.city_id
        if self.contact_mode is not None:
            result['contactMode'] = self.contact_mode
        if self.county_id is not None:
            result['countyId'] = self.county_id
        if self.delivery_time is not None:
            result['deliveryTime'] = self.delivery_time
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.project_manager is not None:
            result['projectManager'] = self.project_manager.to_map()
        if self.property_dept_group_open_conversation_id is not None:
            result['propertyDeptGroupOpenConversationId'] = self.property_dept_group_open_conversation_id
        if self.property_dept_group_owner_user_id is not None:
            result['propertyDeptGroupOwnerUserId'] = self.property_dept_group_owner_user_id
        if self.prov_id is not None:
            result['provId'] = self.prov_id
        if self.scope_east is not None:
            result['scopeEast'] = self.scope_east
        if self.scope_north is not None:
            result['scopeNorth'] = self.scope_north
        if self.scope_south is not None:
            result['scopeSouth'] = self.scope_south
        if self.scope_west is not None:
            result['scopeWest'] = self.scope_west
        if self.telephone is not None:
            result['telephone'] = self.telephone
        if self.town_id is not None:
            result['townId'] = self.town_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('allUserGroupOpenConversationId') is not None:
            self.all_user_group_open_conversation_id = m.get('allUserGroupOpenConversationId')
        if m.get('allUserGroupOwnerUserId') is not None:
            self.all_user_group_owner_user_id = m.get('allUserGroupOwnerUserId')
        if m.get('buildingArea') is not None:
            self.building_area = m.get('buildingArea')
        if m.get('cityId') is not None:
            self.city_id = m.get('cityId')
        if m.get('contactMode') is not None:
            self.contact_mode = m.get('contactMode')
        if m.get('countyId') is not None:
            self.county_id = m.get('countyId')
        if m.get('deliveryTime') is not None:
            self.delivery_time = m.get('deliveryTime')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectManager') is not None:
            temp_model = GetResidentInfoResponseBodyProjectManager()
            self.project_manager = temp_model.from_map(m['projectManager'])
        if m.get('propertyDeptGroupOpenConversationId') is not None:
            self.property_dept_group_open_conversation_id = m.get('propertyDeptGroupOpenConversationId')
        if m.get('propertyDeptGroupOwnerUserId') is not None:
            self.property_dept_group_owner_user_id = m.get('propertyDeptGroupOwnerUserId')
        if m.get('provId') is not None:
            self.prov_id = m.get('provId')
        if m.get('scopeEast') is not None:
            self.scope_east = m.get('scopeEast')
        if m.get('scopeNorth') is not None:
            self.scope_north = m.get('scopeNorth')
        if m.get('scopeSouth') is not None:
            self.scope_south = m.get('scopeSouth')
        if m.get('scopeWest') is not None:
            self.scope_west = m.get('scopeWest')
        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')
        if m.get('townId') is not None:
            self.town_id = m.get('townId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetResidentInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResidentInfoResponseBody = None,
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
            temp_model = GetResidentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResidentMembersInfoHeaders(TeaModel):
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


class GetResidentMembersInfoRequest(TeaModel):
    def __init__(
        self,
        resident_crop_id: str = None,
        user_id_list: List[str] = None,
    ):
        self.resident_crop_id = resident_crop_id
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resident_crop_id is not None:
            result['residentCropId'] = self.resident_crop_id
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('residentCropId') is not None:
            self.resident_crop_id = m.get('residentCropId')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        return self


class GetResidentMembersInfoResponseBodyResidenceList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        ext_field: str = None,
        is_property_owner: bool = None,
        name: str = None,
        relate_type: str = None,
    ):
        # 是否激活
        self.active = active
        # 扩展字段，如果是租客存起止时间
        self.ext_field = ext_field
        # 是否是产权人
        self.is_property_owner = is_property_owner
        self.name = name
        # 业主/租客/亲友等
        self.relate_type = relate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.ext_field is not None:
            result['extField'] = self.ext_field
        if self.is_property_owner is not None:
            result['isPropertyOwner'] = self.is_property_owner
        if self.name is not None:
            result['name'] = self.name
        if self.relate_type is not None:
            result['relateType'] = self.relate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('extField') is not None:
            self.ext_field = m.get('extField')
        if m.get('isPropertyOwner') is not None:
            self.is_property_owner = m.get('isPropertyOwner')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('relateType') is not None:
            self.relate_type = m.get('relateType')
        return self


class GetResidentMembersInfoResponseBody(TeaModel):
    def __init__(
        self,
        residence_list: List[GetResidentMembersInfoResponseBodyResidenceList] = None,
    ):
        # result
        self.residence_list = residence_list

    def validate(self):
        if self.residence_list:
            for k in self.residence_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['residenceList'] = []
        if self.residence_list is not None:
            for k in self.residence_list:
                result['residenceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.residence_list = []
        if m.get('residenceList') is not None:
            for k in m.get('residenceList'):
                temp_model = GetResidentMembersInfoResponseBodyResidenceList()
                self.residence_list.append(temp_model.from_map(k))
        return self


class GetResidentMembersInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResidentMembersInfoResponseBody = None,
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
            temp_model = GetResidentMembersInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpaceIdByTypeHeaders(TeaModel):
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


class GetSpaceIdByTypeRequest(TeaModel):
    def __init__(
        self,
        department_type: str = None,
    ):
        # 部门类型
        self.department_type = department_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_type is not None:
            result['departmentType'] = self.department_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentType') is not None:
            self.department_type = m.get('departmentType')
        return self


class GetSpaceIdByTypeResponseBody(TeaModel):
    def __init__(
        self,
        refer_id: int = None,
    ):
        # 部门id
        self.refer_id = refer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refer_id is not None:
            result['referId'] = self.refer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referId') is not None:
            self.refer_id = m.get('referId')
        return self


class GetSpaceIdByTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSpaceIdByTypeResponseBody = None,
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
            temp_model = GetSpaceIdByTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpacesInfoHeaders(TeaModel):
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


class GetSpacesInfoRequest(TeaModel):
    def __init__(
        self,
        refer_ids: List[int] = None,
        resident_corp_id: str = None,
    ):
        self.refer_ids = refer_ids
        self.resident_corp_id = resident_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refer_ids is not None:
            result['referIds'] = self.refer_ids
        if self.resident_corp_id is not None:
            result['residentCorpId'] = self.resident_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referIds') is not None:
            self.refer_ids = m.get('referIds')
        if m.get('residentCorpId') is not None:
            self.resident_corp_id = m.get('residentCorpId')
        return self


class GetSpacesInfoResponseBodySpaceList(TeaModel):
    def __init__(
        self,
        billing_area: float = None,
        building_area: float = None,
        floor: str = None,
        house_state: int = None,
        is_virtual: int = None,
        parent_refer_id: int = None,
        refer_id: int = None,
        space_name: str = None,
        tag_code: str = None,
        type: str = None,
    ):
        self.billing_area = billing_area
        self.building_area = building_area
        self.floor = floor
        # 房屋状态：0空置/1未领/2入住/3空关/4装修
        self.house_state = house_state
        self.is_virtual = is_virtual
        self.parent_refer_id = parent_refer_id
        self.refer_id = refer_id
        self.space_name = space_name
        self.tag_code = tag_code
        # 空间类型为楼时，1高层/2低层/3别墅/4其他，空间类型为房屋是，1住宅/2公寓/3排屋/4洋房/5叠墅/6别墅/7商铺/8办公用房/9经营用房/10其他
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_area is not None:
            result['billingArea'] = self.billing_area
        if self.building_area is not None:
            result['buildingArea'] = self.building_area
        if self.floor is not None:
            result['floor'] = self.floor
        if self.house_state is not None:
            result['houseState'] = self.house_state
        if self.is_virtual is not None:
            result['isVirtual'] = self.is_virtual
        if self.parent_refer_id is not None:
            result['parentReferId'] = self.parent_refer_id
        if self.refer_id is not None:
            result['referId'] = self.refer_id
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingArea') is not None:
            self.billing_area = m.get('billingArea')
        if m.get('buildingArea') is not None:
            self.building_area = m.get('buildingArea')
        if m.get('floor') is not None:
            self.floor = m.get('floor')
        if m.get('houseState') is not None:
            self.house_state = m.get('houseState')
        if m.get('isVirtual') is not None:
            self.is_virtual = m.get('isVirtual')
        if m.get('parentReferId') is not None:
            self.parent_refer_id = m.get('parentReferId')
        if m.get('referId') is not None:
            self.refer_id = m.get('referId')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSpacesInfoResponseBody(TeaModel):
    def __init__(
        self,
        space_list: List[GetSpacesInfoResponseBodySpaceList] = None,
    ):
        # result
        self.space_list = space_list

    def validate(self):
        if self.space_list:
            for k in self.space_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['spaceList'] = []
        if self.space_list is not None:
            for k in self.space_list:
                result['spaceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.space_list = []
        if m.get('spaceList') is not None:
            for k in m.get('spaceList'):
                temp_model = GetSpacesInfoResponseBodySpaceList()
                self.space_list.append(temp_model.from_map(k))
        return self


class GetSpacesInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSpacesInfoResponseBody = None,
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
            temp_model = GetSpacesInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPointRulesHeaders(TeaModel):
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


class ListPointRulesRequest(TeaModel):
    def __init__(
        self,
        is_circle: bool = None,
    ):
        # 是否查询全员圈积分
        self.is_circle = is_circle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_circle is not None:
            result['isCircle'] = self.is_circle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isCircle') is not None:
            self.is_circle = m.get('isCircle')
        return self


class ListPointRulesResponseBodyPointRuleList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        day_limit_times: int = None,
        extension: str = None,
        group_id: int = None,
        order_id: int = None,
        rule_code: str = None,
        rule_name: str = None,
        score: int = None,
        status: int = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 单日计次上限，0表示无上限
        self.day_limit_times = day_limit_times
        # 扩展字段
        self.extension = extension
        # 分组ID, 默认写入为0
        self.group_id = group_id
        # 排序ID
        self.order_id = order_id
        # 对应的行为代码（可空）
        self.rule_code = rule_code
        # 对应的行为名字
        self.rule_name = rule_name
        # 增加或减少的分数（增加为正数，减少为负数）
        self.score = score
        # 生效状态 0：不生效，1：生效
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.day_limit_times is not None:
            result['dayLimitTimes'] = self.day_limit_times
        if self.extension is not None:
            result['extension'] = self.extension
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.rule_code is not None:
            result['ruleCode'] = self.rule_code
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.score is not None:
            result['score'] = self.score
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('dayLimitTimes') is not None:
            self.day_limit_times = m.get('dayLimitTimes')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('ruleCode') is not None:
            self.rule_code = m.get('ruleCode')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPointRulesResponseBody(TeaModel):
    def __init__(
        self,
        point_rule_list: List[ListPointRulesResponseBodyPointRuleList] = None,
    ):
        # 查询所得积分规则集合
        self.point_rule_list = point_rule_list

    def validate(self):
        if self.point_rule_list:
            for k in self.point_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['pointRuleList'] = []
        if self.point_rule_list is not None:
            for k in self.point_rule_list:
                result['pointRuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.point_rule_list = []
        if m.get('pointRuleList') is not None:
            for k in m.get('pointRuleList'):
                temp_model = ListPointRulesResponseBodyPointRuleList()
                self.point_rule_list.append(temp_model.from_map(k))
        return self


class ListPointRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPointRulesResponseBody = None,
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
            temp_model = ListPointRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubSpaceHeaders(TeaModel):
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


class ListSubSpaceRequest(TeaModel):
    def __init__(
        self,
        refer_id: int = None,
        resident_corp_id: str = None,
    ):
        self.refer_id = refer_id
        # A short description of struct
        self.resident_corp_id = resident_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refer_id is not None:
            result['referId'] = self.refer_id
        if self.resident_corp_id is not None:
            result['residentCorpId'] = self.resident_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referId') is not None:
            self.refer_id = m.get('referId')
        if m.get('residentCorpId') is not None:
            self.resident_corp_id = m.get('residentCorpId')
        return self


class ListSubSpaceResponseBodySpaceList(TeaModel):
    def __init__(
        self,
        billing_area: float = None,
        building_area: float = None,
        floor: str = None,
        house_state: int = None,
        is_virtual: int = None,
        parent_refer_id: int = None,
        refer_id: int = None,
        space_name: str = None,
        tag_code: str = None,
        type: str = None,
    ):
        self.billing_area = billing_area
        self.building_area = building_area
        self.floor = floor
        # 房屋状态：0空置/1未领/2入住/3空关/4装修
        self.house_state = house_state
        self.is_virtual = is_virtual
        self.parent_refer_id = parent_refer_id
        self.refer_id = refer_id
        self.space_name = space_name
        self.tag_code = tag_code
        # 空间类型为楼时，1高层/2低层/3别墅/4其他，空间类型为房屋是，1住宅/2公寓/3排屋/4洋房/5叠墅/6别墅/7商铺/8办公用房/9经营用房/10其他
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_area is not None:
            result['billingArea'] = self.billing_area
        if self.building_area is not None:
            result['buildingArea'] = self.building_area
        if self.floor is not None:
            result['floor'] = self.floor
        if self.house_state is not None:
            result['houseState'] = self.house_state
        if self.is_virtual is not None:
            result['isVirtual'] = self.is_virtual
        if self.parent_refer_id is not None:
            result['parentReferId'] = self.parent_refer_id
        if self.refer_id is not None:
            result['referId'] = self.refer_id
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingArea') is not None:
            self.billing_area = m.get('billingArea')
        if m.get('buildingArea') is not None:
            self.building_area = m.get('buildingArea')
        if m.get('floor') is not None:
            self.floor = m.get('floor')
        if m.get('houseState') is not None:
            self.house_state = m.get('houseState')
        if m.get('isVirtual') is not None:
            self.is_virtual = m.get('isVirtual')
        if m.get('parentReferId') is not None:
            self.parent_refer_id = m.get('parentReferId')
        if m.get('referId') is not None:
            self.refer_id = m.get('referId')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSubSpaceResponseBody(TeaModel):
    def __init__(
        self,
        space_list: List[ListSubSpaceResponseBodySpaceList] = None,
    ):
        # result
        self.space_list = space_list

    def validate(self):
        if self.space_list:
            for k in self.space_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['spaceList'] = []
        if self.space_list is not None:
            for k in self.space_list:
                result['spaceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.space_list = []
        if m.get('spaceList') is not None:
            for k in m.get('spaceList'):
                temp_model = ListSubSpaceResponseBodySpaceList()
                self.space_list.append(temp_model.from_map(k))
        return self


class ListSubSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubSpaceResponseBody = None,
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
            temp_model = ListSubSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PagePointHistoryHeaders(TeaModel):
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


class PagePointHistoryRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        is_circle: bool = None,
        max_results: int = None,
        next_token: int = None,
        start_time: int = None,
        user_id: str = None,
    ):
        # 结束时间Unix时间戳（不包含），可空
        self.end_time = end_time
        # 是否查询全员圈积分
        self.is_circle = is_circle
        # 本次读取的最大数据记录数量，最大20
        self.max_results = max_results
        # 用来标记当前开始读取的位置
        self.next_token = next_token
        # 起始时间Unix时间戳，可空
        self.start_time = start_time
        # 用户userid，可空，不传表示查询组织内所有用户的流水数据
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_circle is not None:
            result['isCircle'] = self.is_circle
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isCircle') is not None:
            self.is_circle = m.get('isCircle')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class PagePointHistoryResponseBodyPointRecordList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        create_at: int = None,
        rule_code: str = None,
        rule_name: str = None,
        score: int = None,
        user_id: str = None,
        uuid: str = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 创建时间（精确到毫秒数）
        self.create_at = create_at
        # 对应的行为代码（可空）
        self.rule_code = rule_code
        # 对应的行为名字
        self.rule_name = rule_name
        # 增加或减少的分数（增加为正数，减少为负数）
        self.score = score
        # 成员id
        self.user_id = user_id
        # 幂等键
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_at is not None:
            result['createAt'] = self.create_at
        if self.rule_code is not None:
            result['ruleCode'] = self.rule_code
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.score is not None:
            result['score'] = self.score
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')
        if m.get('ruleCode') is not None:
            self.rule_code = m.get('ruleCode')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class PagePointHistoryResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: int = None,
        point_record_list: List[PagePointHistoryResponseBodyPointRecordList] = None,
        total_count: int = None,
    ):
        # 是否有下一页
        self.has_more = has_more
        # 下一个游标值
        self.next_token = next_token
        # 查询所得积分流水集合
        self.point_record_list = point_record_list
        # 总数，如果为-1则不计算总数
        self.total_count = total_count

    def validate(self):
        if self.point_record_list:
            for k in self.point_record_list:
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
        result['pointRecordList'] = []
        if self.point_record_list is not None:
            for k in self.point_record_list:
                result['pointRecordList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.point_record_list = []
        if m.get('pointRecordList') is not None:
            for k in m.get('pointRecordList'):
                temp_model = PagePointHistoryResponseBodyPointRecordList()
                self.point_record_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class PagePointHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PagePointHistoryResponseBody = None,
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
            temp_model = PagePointHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveResidentUserHeaders(TeaModel):
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


class RemoveResidentUserRequest(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        user_id: str = None,
    ):
        # 户/租户部门id
        self.department_id = department_id
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class RemoveResidentUserResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否移除成功
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


class RemoveResidentUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveResidentUserResponseBody = None,
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
            temp_model = RemoveResidentUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchResidentHeaders(TeaModel):
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


class SearchResidentRequest(TeaModel):
    def __init__(
        self,
        resident_crop_id: str = None,
        search_word: str = None,
    ):
        self.resident_crop_id = resident_crop_id
        self.search_word = search_word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resident_crop_id is not None:
            result['residentCropId'] = self.resident_crop_id
        if self.search_word is not None:
            result['searchWord'] = self.search_word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('residentCropId') is not None:
            self.resident_crop_id = m.get('residentCropId')
        if m.get('searchWord') is not None:
            self.search_word = m.get('searchWord')
        return self


class SearchResidentResponseBodyResidenceList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        ext_field: str = None,
        is_property_owner: bool = None,
        name: str = None,
        relate_type: str = None,
    ):
        # 是否激活
        self.active = active
        # 扩展字段，如果是租客存起止时间
        self.ext_field = ext_field
        # 是否是产权人
        self.is_property_owner = is_property_owner
        self.name = name
        # 业主/租客/亲友等
        self.relate_type = relate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.ext_field is not None:
            result['extField'] = self.ext_field
        if self.is_property_owner is not None:
            result['isPropertyOwner'] = self.is_property_owner
        if self.name is not None:
            result['name'] = self.name
        if self.relate_type is not None:
            result['relateType'] = self.relate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('extField') is not None:
            self.ext_field = m.get('extField')
        if m.get('isPropertyOwner') is not None:
            self.is_property_owner = m.get('isPropertyOwner')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('relateType') is not None:
            self.relate_type = m.get('relateType')
        return self


class SearchResidentResponseBody(TeaModel):
    def __init__(
        self,
        residence_list: List[SearchResidentResponseBodyResidenceList] = None,
    ):
        # result
        self.residence_list = residence_list

    def validate(self):
        if self.residence_list:
            for k in self.residence_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['residenceList'] = []
        if self.residence_list is not None:
            for k in self.residence_list:
                result['residenceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.residence_list = []
        if m.get('residenceList') is not None:
            for k in m.get('residenceList'):
                temp_model = SearchResidentResponseBodyResidenceList()
                self.residence_list.append(temp_model.from_map(k))
        return self


class SearchResidentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchResidentResponseBody = None,
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
            temp_model = SearchResidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResideceGroupHeaders(TeaModel):
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


class UpdateResideceGroupRequest(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        manager_user_id: str = None,
    ):
        # 组id
        self.department_id = department_id
        # 组名字
        self.department_name = department_name
        # 组长userid
        self.manager_user_id = manager_user_id

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
        if self.manager_user_id is not None:
            result['managerUserId'] = self.manager_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('managerUserId') is not None:
            self.manager_user_id = m.get('managerUserId')
        return self


class UpdateResideceGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否更新成功
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


class UpdateResideceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResideceGroupResponseBody = None,
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
            temp_model = UpdateResideceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResidenceHeaders(TeaModel):
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


class UpdateResidenceRequest(TeaModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        destitute: bool = None,
        grid: str = None,
        home_tel: str = None,
        manager_user_id: str = None,
        parent_department_id: int = None,
    ):
        # 组id
        self.department_id = department_id
        # 户名字
        self.department_name = department_name
        # 是否是贫困户
        self.destitute = destitute
        # 所属网格
        self.grid = grid
        # 家庭电话
        self.home_tel = home_tel
        # 家庭管理员用户id
        self.manager_user_id = manager_user_id
        # 组id
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
        if self.destitute is not None:
            result['destitute'] = self.destitute
        if self.grid is not None:
            result['grid'] = self.grid
        if self.home_tel is not None:
            result['homeTel'] = self.home_tel
        if self.manager_user_id is not None:
            result['managerUserId'] = self.manager_user_id
        if self.parent_department_id is not None:
            result['parentDepartmentId'] = self.parent_department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('destitute') is not None:
            self.destitute = m.get('destitute')
        if m.get('grid') is not None:
            self.grid = m.get('grid')
        if m.get('homeTel') is not None:
            self.home_tel = m.get('homeTel')
        if m.get('managerUserId') is not None:
            self.manager_user_id = m.get('managerUserId')
        if m.get('parentDepartmentId') is not None:
            self.parent_department_id = m.get('parentDepartmentId')
        return self


class UpdateResidenceResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否更新成功
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


class UpdateResidenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResidenceResponseBody = None,
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
            temp_model = UpdateResidenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResidentBlackBoardHeaders(TeaModel):
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


class UpdateResidentBlackBoardRequest(TeaModel):
    def __init__(
        self,
        blackboard_id: str = None,
        context: str = None,
        media_id: str = None,
        title: str = None,
    ):
        self.blackboard_id = blackboard_id
        self.context = context
        self.media_id = media_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackboard_id is not None:
            result['blackboardId'] = self.blackboard_id
        if self.context is not None:
            result['context'] = self.context
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blackboardId') is not None:
            self.blackboard_id = m.get('blackboardId')
        if m.get('context') is not None:
            self.context = m.get('context')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class UpdateResidentBlackBoardResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
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


class UpdateResidentBlackBoardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResidentBlackBoardResponseBody = None,
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
            temp_model = UpdateResidentBlackBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResidentUserHeaders(TeaModel):
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


class UpdateResidentUserRequestExtField(TeaModel):
    def __init__(
        self,
        item_name: str = None,
        item_value: str = None,
    ):
        # 扩展字段名字
        self.item_name = item_name
        # 扩展字段值
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_name is not None:
            result['itemName'] = self.item_name
        if self.item_value is not None:
            result['itemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')
        if m.get('itemValue') is not None:
            self.item_value = m.get('itemValue')
        return self


class UpdateResidentUserRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        department_id: int = None,
        ext_field: List[UpdateResidentUserRequestExtField] = None,
        is_retain_old_dept: bool = None,
        mobile: str = None,
        old_department_id: int = None,
        relate_type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 家庭住址
        self.address = address
        # 所在新的户/租户部门id
        self.department_id = department_id
        # 扩展字段（包括身份证/性别/民族）
        self.ext_field = ext_field
        # 是否保留原部门
        self.is_retain_old_dept = is_retain_old_dept
        # 手机号码
        self.mobile = mobile
        # 原所在部门id
        self.old_department_id = old_department_id
        # 与户主的关系
        self.relate_type = relate_type
        # 人员userId
        self.user_id = user_id
        # 居民名字
        self.user_name = user_name

    def validate(self):
        if self.ext_field:
            for k in self.ext_field:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        result['extField'] = []
        if self.ext_field is not None:
            for k in self.ext_field:
                result['extField'].append(k.to_map() if k else None)
        if self.is_retain_old_dept is not None:
            result['isRetainOldDept'] = self.is_retain_old_dept
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.old_department_id is not None:
            result['oldDepartmentId'] = self.old_department_id
        if self.relate_type is not None:
            result['relateType'] = self.relate_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        self.ext_field = []
        if m.get('extField') is not None:
            for k in m.get('extField'):
                temp_model = UpdateResidentUserRequestExtField()
                self.ext_field.append(temp_model.from_map(k))
        if m.get('isRetainOldDept') is not None:
            self.is_retain_old_dept = m.get('isRetainOldDept')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('oldDepartmentId') is not None:
            self.old_department_id = m.get('oldDepartmentId')
        if m.get('relateType') is not None:
            self.relate_type = m.get('relateType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class UpdateResidentUserResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否更新成功
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


class UpdateResidentUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResidentUserResponseBody = None,
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
            temp_model = UpdateResidentUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


