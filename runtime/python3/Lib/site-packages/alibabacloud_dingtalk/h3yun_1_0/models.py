# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BatchInsertBizObjectHeaders(TeaModel):
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


class BatchInsertBizObjectRequest(TeaModel):
    def __init__(
        self,
        biz_object_json_array: List[str] = None,
        is_draft: bool = None,
        op_user_id: str = None,
        schema_code: str = None,
    ):
        # 待新增的业对象json数组
        self.biz_object_json_array = biz_object_json_array
        # 是否是草稿数据。true=创建草稿数据，false=创建生效数据
        self.is_draft = is_draft
        # 操作用户id
        self.op_user_id = op_user_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_json_array is not None:
            result['bizObjectJsonArray'] = self.biz_object_json_array
        if self.is_draft is not None:
            result['isDraft'] = self.is_draft
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectJsonArray') is not None:
            self.biz_object_json_array = m.get('bizObjectJsonArray')
        if m.get('isDraft') is not None:
            self.is_draft = m.get('isDraft')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class BatchInsertBizObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_object_ids: List[str] = None,
        failed_datas: List[str] = None,
        failed_messages: List[str] = None,
        process_ids: List[str] = None,
    ):
        # 成功新增的业务对象id数组
        self.biz_object_ids = biz_object_ids
        # 新增失败的数据数组
        self.failed_datas = failed_datas
        # 失败的提示信息数组
        self.failed_messages = failed_messages
        # 新增成功的流程实例id数组
        self.process_ids = process_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_ids is not None:
            result['bizObjectIds'] = self.biz_object_ids
        if self.failed_datas is not None:
            result['failedDatas'] = self.failed_datas
        if self.failed_messages is not None:
            result['failedMessages'] = self.failed_messages
        if self.process_ids is not None:
            result['processIds'] = self.process_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectIds') is not None:
            self.biz_object_ids = m.get('bizObjectIds')
        if m.get('failedDatas') is not None:
            self.failed_datas = m.get('failedDatas')
        if m.get('failedMessages') is not None:
            self.failed_messages = m.get('failedMessages')
        if m.get('processIds') is not None:
            self.process_ids = m.get('processIds')
        return self


class BatchInsertBizObjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchInsertBizObjectResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BatchInsertBizObjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class BatchInsertBizObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchInsertBizObjectResponseBody = None,
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
            temp_model = BatchInsertBizObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelProcessInstanceHeaders(TeaModel):
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


class CancelProcessInstanceRequest(TeaModel):
    def __init__(
        self,
        process_instance_id: str = None,
    ):
        # 流程实例id
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        return self


class CancelProcessInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 提示信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CancelProcessInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelProcessInstanceResponseBody = None,
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
            temp_model = CancelProcessInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBizObjectHeaders(TeaModel):
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


class CreateBizObjectRequest(TeaModel):
    def __init__(
        self,
        biz_object_json: str = None,
        is_draft: bool = None,
        op_user_id: str = None,
        schema_code: str = None,
    ):
        # json格式的业务数据
        self.biz_object_json = biz_object_json
        # 是否是草稿数据。true=草稿数据，false=生效数据
        self.is_draft = is_draft
        # 操作用户id。可从“获取用户信息”API获取
        self.op_user_id = op_user_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_json is not None:
            result['bizObjectJson'] = self.biz_object_json
        if self.is_draft is not None:
            result['isDraft'] = self.is_draft
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectJson') is not None:
            self.biz_object_json = m.get('bizObjectJson')
        if m.get('isDraft') is not None:
            self.is_draft = m.get('isDraft')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class CreateBizObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        form_usage_type: str = None,
        process_instance_id: str = None,
        schema_code: str = None,
    ):
        # 表单业务数据id
        self.biz_object_id = biz_object_id
        # 数据模型。DataList=本地存储的列表库，Workflow=工作流应用
        self.form_usage_type = form_usage_type
        # 流程实例id
        self.process_instance_id = process_instance_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.form_usage_type is not None:
            result['formUsageType'] = self.form_usage_type
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('formUsageType') is not None:
            self.form_usage_type = m.get('formUsageType')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class CreateBizObjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateBizObjectResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateBizObjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateBizObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBizObjectResponseBody = None,
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
            temp_model = CreateBizObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProcessesInstanceHeaders(TeaModel):
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


class CreateProcessesInstanceRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        op_user_id: str = None,
        schema_code: str = None,
    ):
        # 业务数据id
        self.biz_object_id = biz_object_id
        # 操作用户id。此为氚云的用户id，可从"获取用户数据API"获取
        self.op_user_id = op_user_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class CreateProcessesInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        process_instance_id: str = None,
    ):
        # 流程实例ID
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        return self


class CreateProcessesInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProcessesInstanceResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 业务响应结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProcessesInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateProcessesInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProcessesInstanceResponseBody = None,
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
            temp_model = CreateProcessesInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBizObjectHeaders(TeaModel):
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


class DeleteBizObjectRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        schema_code: str = None,
    ):
        # 业务数据id
        self.biz_object_id = biz_object_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class DeleteBizObjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 提示信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteBizObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBizObjectResponseBody = None,
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
            temp_model = DeleteBizObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProcessesInstanceHeaders(TeaModel):
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


class DeleteProcessesInstanceRequest(TeaModel):
    def __init__(
        self,
        is_auto_update_biz_object: bool = None,
        process_instance_id: str = None,
    ):
        # 删除成功后，是否需要更新业务表单关联的流程实例id
        self.is_auto_update_biz_object = is_auto_update_biz_object
        # 流程实例id
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_auto_update_biz_object is not None:
            result['isAutoUpdateBizObject'] = self.is_auto_update_biz_object
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isAutoUpdateBizObject') is not None:
            self.is_auto_update_biz_object = m.get('isAutoUpdateBizObject')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        return self


class DeleteProcessesInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 提示信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteProcessesInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProcessesInstanceResponseBody = None,
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
            temp_model = DeleteProcessesInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppsHeaders(TeaModel):
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


class GetAppsRequest(TeaModel):
    def __init__(
        self,
        query_type: str = None,
        values: List[str] = None,
    ):
        # 查询类型。All=全部，Solution=以解决方案编码为条件来查询应用，AppCode=以应用编码为条件来查询
        self.query_type = query_type
        # 待查询的编码数组。queryType参数为All时，此值可为空
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_source: str = None,
        app_state: str = None,
        display_name: str = None,
        solution: str = None,
    ):
        # 应用编码
        self.app_code = app_code
        # 应用的来源类型。Custom=自开发的、Installed=安装的
        self.app_source = app_source
        # 应用状态。Enable=启用、Forbidden=禁用、Warring=预警
        self.app_state = app_state
        # 应用显示名称
        self.display_name = display_name
        # 应用所属的解决方案名称
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.app_source is not None:
            result['appSource'] = self.app_source
        if self.app_state is not None:
            result['appState'] = self.app_state
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.solution is not None:
            result['solution'] = self.solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('appSource') is not None:
            self.app_source = m.get('appSource')
        if m.get('appState') is not None:
            self.app_state = m.get('appState')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('solution') is not None:
            self.solution = m.get('solution')
        return self


class GetAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAppsResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppsResponseBody = None,
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
            temp_model = GetAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachmentTemporaryUrlHeaders(TeaModel):
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


class GetAttachmentTemporaryUrlRequest(TeaModel):
    def __init__(
        self,
        attachment_id: str = None,
    ):
        # 附件id
        self.attachment_id = attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_id is not None:
            result['attachmentId'] = self.attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentId') is not None:
            self.attachment_id = m.get('attachmentId')
        return self


class GetAttachmentTemporaryUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        attachment_url: str = None,
    ):
        # 附件临时免登地址。有效期为30分钟
        self.attachment_url = attachment_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_url is not None:
            result['attachmentUrl'] = self.attachment_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentUrl') is not None:
            self.attachment_url = m.get('attachmentUrl')
        return self


class GetAttachmentTemporaryUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAttachmentTemporaryUrlResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 业务响应结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAttachmentTemporaryUrlResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAttachmentTemporaryUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAttachmentTemporaryUrlResponseBody = None,
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
            temp_model = GetAttachmentTemporaryUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationsHeaders(TeaModel):
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


class GetOrganizationsRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
    ):
        # 18f923a7-5a5e-426d-94ae-a55ad1a4b240
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


class GetOrganizationsResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
        sort_key: int = None,
        unit_type: str = None,
    ):
        # 部门编码
        self.code = code
        # 描述
        self.description = description
        # 部门id
        self.id = id
        # 部门名称
        self.name = name
        # 父级部门id
        self.parent_id = parent_id
        # 排序值
        self.sort_key = sort_key
        # 组织类型。Company=公司，OrganizationUnit=组织单元
        self.unit_type = unit_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.unit_type is not None:
            result['unitType'] = self.unit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('unitType') is not None:
            self.unit_type = m.get('unitType')
        return self


class GetOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOrganizationsResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码。success=成功
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetOrganizationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrganizationsResponseBody = None,
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
            temp_model = GetOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleUsersHeaders(TeaModel):
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


class GetRoleUsersRequest(TeaModel):
    def __init__(
        self,
        role_id: str = None,
    ):
        # 角色id
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['roleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        return self


class GetRoleUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        department_id: str = None,
        department_name: str = None,
        description: str = None,
        domain_type: str = None,
        email: str = None,
        mobile: str = None,
        name: str = None,
        part_department_ids: List[str] = None,
        sex: str = None,
        sort_key: int = None,
        user_id: str = None,
    ):
        # 用户编码
        self.code = code
        # 所属部门id
        self.department_id = department_id
        # 所属部门名称
        self.department_name = department_name
        # 描述
        self.description = description
        # 所属范围。Internal=内部，External=外部
        self.domain_type = domain_type
        # 邮箱
        self.email = email
        # 手机号码
        self.mobile = mobile
        # 用户名称
        self.name = name
        # 兼职部门id集合（含主部门id）
        self.part_department_ids = part_department_ids
        # 性别.None=未指定，Man=男性，Female=女性
        self.sex = sex
        # 排序值
        self.sort_key = sort_key
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_type is not None:
            result['domainType'] = self.domain_type
        if self.email is not None:
            result['email'] = self.email
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.part_department_ids is not None:
            result['partDepartmentIds'] = self.part_department_ids
        if self.sex is not None:
            result['sex'] = self.sex
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainType') is not None:
            self.domain_type = m.get('domainType')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partDepartmentIds') is not None:
            self.part_department_ids = m.get('partDepartmentIds')
        if m.get('sex') is not None:
            self.sex = m.get('sex')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRoleUsersResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetRoleUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRoleUsersResponseBody = None,
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
            temp_model = GetRoleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRolesHeaders(TeaModel):
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


class GetRolesResponseBodyDataRoleGroups(TeaModel):
    def __init__(
        self,
        company_id: str = None,
        description: str = None,
        group_code: str = None,
        group_id: str = None,
        group_name: str = None,
        state: str = None,
        visibility: str = None,
    ):
        # 所属企业id
        self.company_id = company_id
        # 描述
        self.description = description
        # 组编码
        self.group_code = group_code
        # 组id
        self.group_id = group_id
        # 组名称
        self.group_name = group_name
        # 状态。Active=激活、Inactive=未激活，Unspecified=未指定状态
        self.state = state
        # 可见性。All=全部可见、Normal=普通可见、OnlyAdmin=只有管理的时候可见、OnlyOrganization=本组织范围可见
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_id is not None:
            result['companyId'] = self.company_id
        if self.description is not None:
            result['description'] = self.description
        if self.group_code is not None:
            result['groupCode'] = self.group_code
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.state is not None:
            result['state'] = self.state
        if self.visibility is not None:
            result['visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupCode') is not None:
            self.group_code = m.get('groupCode')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')
        return self


class GetRolesResponseBodyDataRoles(TeaModel):
    def __init__(
        self,
        company_id: str = None,
        description: str = None,
        group_id: str = None,
        role_code: str = None,
        role_id: str = None,
        role_name: str = None,
        state: str = None,
        visibility: str = None,
    ):
        # 所属企业id
        self.company_id = company_id
        # 描述
        self.description = description
        # 所属的角色组id
        self.group_id = group_id
        # 角色编码
        self.role_code = role_code
        # 角色id
        self.role_id = role_id
        # 角色名称
        self.role_name = role_name
        # 状态。Active=激活、Inactive=未激活，Unspecified=未指定状态
        self.state = state
        # 可见性。All=全部可见、Normal=普通可见、OnlyAdmin=只有管理的时候可见、OnlyOrganization=本组织范围可见
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_id is not None:
            result['companyId'] = self.company_id
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.role_code is not None:
            result['roleCode'] = self.role_code
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.state is not None:
            result['state'] = self.state
        if self.visibility is not None:
            result['visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('roleCode') is not None:
            self.role_code = m.get('roleCode')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')
        return self


class GetRolesResponseBodyData(TeaModel):
    def __init__(
        self,
        role_groups: List[GetRolesResponseBodyDataRoleGroups] = None,
        roles: List[GetRolesResponseBodyDataRoles] = None,
    ):
        # 角色组数组
        self.role_groups = role_groups
        # 角色数组
        self.roles = roles

    def validate(self):
        if self.role_groups:
            for k in self.role_groups:
                if k:
                    k.validate()
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roleGroups'] = []
        if self.role_groups is not None:
            for k in self.role_groups:
                result['roleGroups'].append(k.to_map() if k else None)
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_groups = []
        if m.get('roleGroups') is not None:
            for k in m.get('roleGroups'):
                temp_model = GetRolesResponseBodyDataRoleGroups()
                self.role_groups.append(temp_model.from_map(k))
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = GetRolesResponseBodyDataRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class GetRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRolesResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetRolesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRolesResponseBody = None,
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
            temp_model = GetRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadUrlHeaders(TeaModel):
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


class GetUploadUrlRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        field_name: str = None,
        is_overwrite: bool = None,
        schema_code: str = None,
    ):
        # 业务数据实例id
        self.biz_object_id = biz_object_id
        # 文件上传至目标控件的字段名
        self.field_name = field_name
        # 是否覆盖。false=添加，true=覆盖
        self.is_overwrite = is_overwrite
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.is_overwrite is not None:
            result['isOverwrite'] = self.is_overwrite
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('isOverwrite') is not None:
            self.is_overwrite = m.get('isOverwrite')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class GetUploadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        upload_url: str = None,
    ):
        # 附件上传地址
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')
        return self


class GetUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUploadUrlResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUploadUrlResponseBody = None,
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
            temp_model = GetUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUsersHeaders(TeaModel):
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


class GetUsersRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        is_recursive: bool = None,
    ):
        # 部门id。
        self.department_id = department_id
        # 是否递归获取子级部门下的用户。默认值为false
        self.is_recursive = is_recursive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.is_recursive is not None:
            result['isRecursive'] = self.is_recursive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('isRecursive') is not None:
            self.is_recursive = m.get('isRecursive')
        return self


class GetUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        department_id: str = None,
        department_name: str = None,
        description: str = None,
        domain_type: str = None,
        email: str = None,
        id: str = None,
        mobile: str = None,
        name: str = None,
        part_department_ids: List[str] = None,
        sex: str = None,
        sort_key: int = None,
    ):
        # 用户编码
        self.code = code
        # 直属组织id
        self.department_id = department_id
        # 直属组织名称
        self.department_name = department_name
        # 描述
        self.description = description
        # 作用域类型。Unspecified=未指定、Internal=内部组织机构、External=外部组织机构
        self.domain_type = domain_type
        # 邮箱
        self.email = email
        # 用户id
        self.id = id
        # 电话
        self.mobile = mobile
        # 用户姓名
        self.name = name
        # 兼职部门id
        self.part_department_ids = part_department_ids
        # 性别.None=未指定，Man=男性，Female=女性
        self.sex = sex
        # 排序号
        self.sort_key = sort_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_type is not None:
            result['domainType'] = self.domain_type
        if self.email is not None:
            result['email'] = self.email
        if self.id is not None:
            result['id'] = self.id
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.part_department_ids is not None:
            result['partDepartmentIds'] = self.part_department_ids
        if self.sex is not None:
            result['sex'] = self.sex
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainType') is not None:
            self.domain_type = m.get('domainType')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partDepartmentIds') is not None:
            self.part_department_ids = m.get('partDepartmentIds')
        if m.get('sex') is not None:
            self.sex = m.get('sex')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        return self


class GetUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetUsersResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUsersResponseBody = None,
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
            temp_model = GetUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBizFieldsHeaders(TeaModel):
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


class LoadBizFieldsRequest(TeaModel):
    def __init__(
        self,
        schema_code: str = None,
    ):
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class LoadBizFieldsResponseBodyDataChildFormsFields(TeaModel):
    def __init__(
        self,
        biz_data_type: str = None,
        field_name: str = None,
        label: str = None,
    ):
        # 字段数据类型
        self.biz_data_type = biz_data_type
        # 字段名或组件名
        self.field_name = field_name
        # 显示名称
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data_type is not None:
            result['bizDataType'] = self.biz_data_type
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizDataType') is not None:
            self.biz_data_type = m.get('bizDataType')
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class LoadBizFieldsResponseBodyDataChildForms(TeaModel):
    def __init__(
        self,
        fields: List[LoadBizFieldsResponseBodyDataChildFormsFields] = None,
        form_name: str = None,
        schema_code: str = None,
    ):
        # 子表字段
        self.fields = fields
        # 子表名称
        self.form_name = form_name
        # 子表编码
        self.schema_code = schema_code

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.form_name is not None:
            result['formName'] = self.form_name
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = LoadBizFieldsResponseBodyDataChildFormsFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('formName') is not None:
            self.form_name = m.get('formName')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class LoadBizFieldsResponseBodyDataFields(TeaModel):
    def __init__(
        self,
        biz_data_type: str = None,
        field_name: str = None,
        label: str = None,
    ):
        # 字段、自定义组件的数据类型。Bool=逻辑型，DataTime=日期型、日期组件，Double=双精度数值型，Int=整形，Long=长整形，String=长文本，ShortString=短文本，ByteArray=二进制流， Image=图片类型、图片组件，File=附件类型组件，TimeSpan=时间段。Unit=参与者（单人），UnitArray=参与者（多人），Html=html类型，Xml=xml类型 BizObject=业务对象，BizObjectArray=业务对象数组、子表组件，Association=关联到其他对象、关联组件，AssociationArray=关联对象数组，Map=地图类型，Address=地址类型，Formula=公式型空间，Signature=签名控件，Plugin=文字识别Bool
        self.biz_data_type = biz_data_type
        # 字段名称
        self.field_name = field_name
        # 显示名称
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data_type is not None:
            result['bizDataType'] = self.biz_data_type
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizDataType') is not None:
            self.biz_data_type = m.get('bizDataType')
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class LoadBizFieldsResponseBodyData(TeaModel):
    def __init__(
        self,
        child_forms: List[LoadBizFieldsResponseBodyDataChildForms] = None,
        fields: List[LoadBizFieldsResponseBodyDataFields] = None,
        form_name: str = None,
        schema_code: str = None,
    ):
        # 子表结构
        self.child_forms = child_forms
        # 字段、组件结构数组
        self.fields = fields
        # 表单名称
        self.form_name = form_name
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        if self.child_forms:
            for k in self.child_forms:
                if k:
                    k.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['childForms'] = []
        if self.child_forms is not None:
            for k in self.child_forms:
                result['childForms'].append(k.to_map() if k else None)
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.form_name is not None:
            result['formName'] = self.form_name
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_forms = []
        if m.get('childForms') is not None:
            for k in m.get('childForms'):
                temp_model = LoadBizFieldsResponseBodyDataChildForms()
                self.child_forms.append(temp_model.from_map(k))
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = LoadBizFieldsResponseBodyDataFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('formName') is not None:
            self.form_name = m.get('formName')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class LoadBizFieldsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: LoadBizFieldsResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = LoadBizFieldsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class LoadBizFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LoadBizFieldsResponseBody = None,
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
            temp_model = LoadBizFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBizObjectHeaders(TeaModel):
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


class LoadBizObjectRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        schema_code: str = None,
    ):
        # 业务数据i实例id
        self.biz_object_id = biz_object_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class LoadBizObjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class LoadBizObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LoadBizObjectResponseBody = None,
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
            temp_model = LoadBizObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBizObjectsHeaders(TeaModel):
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


class LoadBizObjectsRequestSortByFields(TeaModel):
    def __init__(
        self,
        direction: str = None,
        field_name: str = None,
    ):
        # 排序方向。Ascending=升序，Descending=降序
        self.direction = direction
        # 排序字段名
        self.field_name = field_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        return self


class LoadBizObjectsRequest(TeaModel):
    def __init__(
        self,
        matcher_json: str = None,
        page_number: int = None,
        page_size: int = None,
        return_fields: List[str] = None,
        schema_code: str = None,
        sort_by_fields: List[LoadBizObjectsRequestSortByFields] = None,
    ):
        # json格式的动态条件过滤器参数
        self.matcher_json = matcher_json
        # 分页页码
        self.page_number = page_number
        # 分页页大小。限制在1~500
        self.page_size = page_size
        # 返回的字段.仅支持传入主表的字段
        self.return_fields = return_fields
        # 表单编码
        self.schema_code = schema_code
        # 排序字段结构数组
        self.sort_by_fields = sort_by_fields

    def validate(self):
        if self.sort_by_fields:
            for k in self.sort_by_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matcher_json is not None:
            result['matcherJson'] = self.matcher_json
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.return_fields is not None:
            result['returnFields'] = self.return_fields
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        result['sortByFields'] = []
        if self.sort_by_fields is not None:
            for k in self.sort_by_fields:
                result['sortByFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matcherJson') is not None:
            self.matcher_json = m.get('matcherJson')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('returnFields') is not None:
            self.return_fields = m.get('returnFields')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        self.sort_by_fields = []
        if m.get('sortByFields') is not None:
            for k in m.get('sortByFields'):
                temp_model = LoadBizObjectsRequestSortByFields()
                self.sort_by_fields.append(temp_model.from_map(k))
        return self


class LoadBizObjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_objects: List[Dict[str, Any]] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 业务数据实例数组
        self.biz_objects = biz_objects
        # 页码
        self.page_number = page_number
        # 页大小
        self.page_size = page_size
        # 匹配条件的结果总数量
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_objects is not None:
            result['bizObjects'] = self.biz_objects
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjects') is not None:
            self.biz_objects = m.get('bizObjects')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class LoadBizObjectsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: LoadBizObjectsResponseBodyData = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = LoadBizObjectsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class LoadBizObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LoadBizObjectsResponseBody = None,
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
            temp_model = LoadBizObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAppFunctionNodesHeaders(TeaModel):
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


class QueryAppFunctionNodesRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
    ):
        # 应用编码
        self.app_code = app_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        return self


class QueryAppFunctionNodesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        display_name: str = None,
        is_system: bool = None,
        node_type: str = None,
        node_visible_type: str = None,
        parent_code: str = None,
        schema_code: str = None,
        sort_key: int = None,
        state: str = None,
    ):
        # 节点所属的应用编码
        self.app_code = app_code
        # 显示名称
        self.display_name = display_name
        # 是否是系统节点，如果是则无法删除
        self.is_system = is_system
        # 菜单节点类型。 AppPackage=应用程序 FormModule=列表模块(不能发起流程)、 WorkflowModule=流程列表模块(可以发起流程) ReportModule=报表模块 GroupModule=节点分组
        self.node_type = node_type
        # 菜单可见类型。 Inactive=未指定 AllVisible=全部可见 PcVisible=仅pc可见 MobileVisible=仅移动端可见 InVisible=全部不可见
        self.node_visible_type = node_visible_type
        # 父节点的编码
        self.parent_code = parent_code
        # 节点编码。如果nodeType=FormModule,则为表单编码
        self.schema_code = schema_code
        # 排序编号
        self.sort_key = sort_key
        # 菜单状态。 Inactive=未激活 Active=激活
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.is_system is not None:
            result['isSystem'] = self.is_system
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.node_visible_type is not None:
            result['nodeVisibleType'] = self.node_visible_type
        if self.parent_code is not None:
            result['parentCode'] = self.parent_code
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('isSystem') is not None:
            self.is_system = m.get('isSystem')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('nodeVisibleType') is not None:
            self.node_visible_type = m.get('nodeVisibleType')
        if m.get('parentCode') is not None:
            self.parent_code = m.get('parentCode')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class QueryAppFunctionNodesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryAppFunctionNodesResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryAppFunctionNodesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryAppFunctionNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAppFunctionNodesResponseBody = None,
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
            temp_model = QueryAppFunctionNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProcessesInstanceHeaders(TeaModel):
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


class QueryProcessesInstanceRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        schema_code: str = None,
    ):
        # 业务数据id
        self.biz_object_id = biz_object_id
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class QueryProcessesInstanceResponseBodyDataOriginator(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 所属组织id
        self.department_id = department_id
        # 所属组织名称
        self.department_name = department_name
        # 用户名称
        self.name = name
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
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProcessesInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        biz_object_id: str = None,
        created_time_gmt: str = None,
        ding_talk_process_id: str = None,
        finish_time_gmt: str = None,
        originator: QueryProcessesInstanceResponseBodyDataOriginator = None,
        process_display_name: str = None,
        process_instance_id: str = None,
        process_version: int = None,
        schema_code: str = None,
        start_time_gmt: str = None,
        state: str = None,
    ):
        # 流程所属的应用编码
        self.app_code = app_code
        # 流程关联的业务对象id
        self.biz_object_id = biz_object_id
        # 创建时间
        self.created_time_gmt = created_time_gmt
        # 钉钉流程Id
        self.ding_talk_process_id = ding_talk_process_id
        # 完成时间
        self.finish_time_gmt = finish_time_gmt
        # 流程发起人信息
        self.originator = originator
        # 流程名称
        self.process_display_name = process_display_name
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 工作流模板的版本
        self.process_version = process_version
        # 流程所属的表单编码
        self.schema_code = schema_code
        # 开始时间
        self.start_time_gmt = start_time_gmt
        # 状态。Initiated=初始化完成，Starting=正在启动，Running=正在运行，Finishing=正在结束，Finished=已完成，Canceled=已取
        self.state = state

    def validate(self):
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.created_time_gmt is not None:
            result['createdTimeGMT'] = self.created_time_gmt
        if self.ding_talk_process_id is not None:
            result['dingTalkProcessId'] = self.ding_talk_process_id
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.process_display_name is not None:
            result['processDisplayName'] = self.process_display_name
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.process_version is not None:
            result['processVersion'] = self.process_version
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        if self.start_time_gmt is not None:
            result['startTimeGMT'] = self.start_time_gmt
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('createdTimeGMT') is not None:
            self.created_time_gmt = m.get('createdTimeGMT')
        if m.get('dingTalkProcessId') is not None:
            self.ding_talk_process_id = m.get('dingTalkProcessId')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('originator') is not None:
            temp_model = QueryProcessesInstanceResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('processDisplayName') is not None:
            self.process_display_name = m.get('processDisplayName')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('processVersion') is not None:
            self.process_version = m.get('processVersion')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        if m.get('startTimeGMT') is not None:
            self.start_time_gmt = m.get('startTimeGMT')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class QueryProcessesInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryProcessesInstanceResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryProcessesInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryProcessesInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProcessesInstanceResponseBody = None,
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
            temp_model = QueryProcessesInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProcessesWorkItemsHeaders(TeaModel):
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


class QueryProcessesWorkItemsRequest(TeaModel):
    def __init__(
        self,
        process_instance_id: str = None,
    ):
        # 流程实例ID
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        return self


class QueryProcessesWorkItemsResponseBodyDataFinisher(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 用户直属的部门id
        self.department_id = department_id
        # 用户直属的部门名称
        self.department_name = department_name
        # 用户名称
        self.name = name
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
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProcessesWorkItemsResponseBodyDataParticipant(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 用户直属的部门id
        self.department_id = department_id
        # 用户直属的部门名称
        self.department_name = department_name
        # 用户名称
        self.name = name
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
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProcessesWorkItemsResponseBodyDataReceiptor(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 用户直属的部门id
        self.department_id = department_id
        # 用户直属的部门名称
        self.department_name = department_name
        # 用户名称
        self.name = name
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
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProcessesWorkItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_name: str = None,
        app_code: str = None,
        biz_object_id: str = None,
        comment: str = None,
        display_name: str = None,
        finish_time_gmt: str = None,
        finisher: QueryProcessesWorkItemsResponseBodyDataFinisher = None,
        is_approval: bool = None,
        is_finish: bool = None,
        participant: QueryProcessesWorkItemsResponseBodyDataParticipant = None,
        process_instance_id: str = None,
        process_version: str = None,
        receiptor: QueryProcessesWorkItemsResponseBodyDataReceiptor = None,
        receive_time_gmt: str = None,
        schema_code: str = None,
        start_time_gmt: str = None,
        state: str = None,
        work_item_id: str = None,
        work_item_type: str = None,
    ):
        # 活动编码
        self.activity_code = activity_code
        # 当前活动名称
        self.activity_name = activity_name
        # 应用编码
        self.app_code = app_code
        # 工作项所关联的业务对象id
        self.biz_object_id = biz_object_id
        # 对该工作项的意见
        self.comment = comment
        # 显示名称
        self.display_name = display_name
        # 完成时间
        self.finish_time_gmt = finish_time_gmt
        # 完成者
        self.finisher = finisher
        # 对该工作项是否同意
        self.is_approval = is_approval
        # 是否已完成
        self.is_finish = is_finish
        # 参与者
        self.participant = participant
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 工作流版本
        self.process_version = process_version
        # 转交工作的接收人。如无转接人，则为空
        self.receiptor = receiptor
        # 接收时间
        self.receive_time_gmt = receive_time_gmt
        # 表单编码
        self.schema_code = schema_code
        # 开始这个任务的时间
        self.start_time_gmt = start_time_gmt
        # 状态。Waiting=等待的状态，Working=正在工作中的状态，Finished=处于完成状态，Canceled=已经被取消，Forwarded=已转交状态，Revoked=撤回
        self.state = state
        # 工作任务Id
        self.work_item_id = work_item_id
        # 工作项类型。Fill=普通工作项，Approve=审批类型工作项，Circulate=传阅
        self.work_item_type = work_item_type

    def validate(self):
        if self.finisher:
            self.finisher.validate()
        if self.participant:
            self.participant.validate()
        if self.receiptor:
            self.receiptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_code is not None:
            result['activityCode'] = self.activity_code
        if self.activity_name is not None:
            result['activityName'] = self.activity_name
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.comment is not None:
            result['comment'] = self.comment
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.finisher is not None:
            result['finisher'] = self.finisher.to_map()
        if self.is_approval is not None:
            result['isApproval'] = self.is_approval
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        if self.participant is not None:
            result['participant'] = self.participant.to_map()
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.process_version is not None:
            result['processVersion'] = self.process_version
        if self.receiptor is not None:
            result['receiptor'] = self.receiptor.to_map()
        if self.receive_time_gmt is not None:
            result['receiveTimeGMT'] = self.receive_time_gmt
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        if self.start_time_gmt is not None:
            result['startTimeGMT'] = self.start_time_gmt
        if self.state is not None:
            result['state'] = self.state
        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id
        if self.work_item_type is not None:
            result['workItemType'] = self.work_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityCode') is not None:
            self.activity_code = m.get('activityCode')
        if m.get('activityName') is not None:
            self.activity_name = m.get('activityName')
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('finisher') is not None:
            temp_model = QueryProcessesWorkItemsResponseBodyDataFinisher()
            self.finisher = temp_model.from_map(m['finisher'])
        if m.get('isApproval') is not None:
            self.is_approval = m.get('isApproval')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        if m.get('participant') is not None:
            temp_model = QueryProcessesWorkItemsResponseBodyDataParticipant()
            self.participant = temp_model.from_map(m['participant'])
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('processVersion') is not None:
            self.process_version = m.get('processVersion')
        if m.get('receiptor') is not None:
            temp_model = QueryProcessesWorkItemsResponseBodyDataReceiptor()
            self.receiptor = temp_model.from_map(m['receiptor'])
        if m.get('receiveTimeGMT') is not None:
            self.receive_time_gmt = m.get('receiveTimeGMT')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        if m.get('startTimeGMT') is not None:
            self.start_time_gmt = m.get('startTimeGMT')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')
        if m.get('workItemType') is not None:
            self.work_item_type = m.get('workItemType')
        return self


class QueryProcessesWorkItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryProcessesWorkItemsResponseBodyData] = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 返回结果
        self.data = data
        # 提示信息
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryProcessesWorkItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryProcessesWorkItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProcessesWorkItemsResponseBody = None,
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
            temp_model = QueryProcessesWorkItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizObjectHeaders(TeaModel):
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


class UpdateBizObjectRequest(TeaModel):
    def __init__(
        self,
        biz_object_id: str = None,
        biz_object_json: str = None,
        schema_code: str = None,
    ):
        # 业务数据id
        self.biz_object_id = biz_object_id
        # 待修改的json格式业务数据
        self.biz_object_json = biz_object_json
        # 表单编码
        self.schema_code = schema_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_object_id is not None:
            result['bizObjectId'] = self.biz_object_id
        if self.biz_object_json is not None:
            result['bizObjectJson'] = self.biz_object_json
        if self.schema_code is not None:
            result['schemaCode'] = self.schema_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizObjectId') is not None:
            self.biz_object_id = m.get('bizObjectId')
        if m.get('bizObjectJson') is not None:
            self.biz_object_json = m.get('bizObjectJson')
        if m.get('schemaCode') is not None:
            self.schema_code = m.get('schemaCode')
        return self


class UpdateBizObjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # 状态码
        self.code = code
        # 提示信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateBizObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateBizObjectResponseBody = None,
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
            temp_model = UpdateBizObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


