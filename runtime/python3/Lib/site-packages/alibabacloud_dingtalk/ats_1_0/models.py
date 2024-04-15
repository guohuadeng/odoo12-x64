# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddApplicationRegFormTemplateHeaders(TeaModel):
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


class AddApplicationRegFormTemplateRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        content: str = None,
        name: str = None,
        outer_id: str = None,
        op_user_id: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 模板内容
        self.content = content
        # 模板名称
        self.name = name
        # 外部唯一标识
        self.outer_id = outer_id
        # 操作人员工标识
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        if self.outer_id is not None:
            result['outerId'] = self.outer_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('outerId') is not None:
            self.outer_id = m.get('outerId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class AddApplicationRegFormTemplateResponseBody(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        version: int = None,
    ):
        # 模板标识
        self.template_id = template_id
        # 模板版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class AddApplicationRegFormTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddApplicationRegFormTemplateResponseBody = None,
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
            temp_model = AddApplicationRegFormTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFileHeaders(TeaModel):
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


class AddFileRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        file_name: str = None,
        media_id: str = None,
        op_user_id: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 文件名称
        self.file_name = file_name
        # 文件mediaId
        self.media_id = media_id
        # 操作人员工标识，为空时默认以企业管理员身份进行操作
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class AddFileResponseBody(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        space_id: int = None,
    ):
        # 文件标识
        self.file_id = file_id
        # 文件名
        self.file_name = file_name
        # 空间标识
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class AddFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFileResponseBody = None,
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
            temp_model = AddFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmRightsHeaders(TeaModel):
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


class ConfirmRightsRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        return self


class ConfirmRightsResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 结果
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


class ConfirmRightsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmRightsResponseBody = None,
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
            temp_model = ConfirmRightsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishBeginnerTaskHeaders(TeaModel):
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


class FinishBeginnerTaskRequest(TeaModel):
    def __init__(
        self,
        scope: str = None,
        user_id: str = None,
    ):
        # 任务范围
        self.scope = scope
        # 员工标识
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class FinishBeginnerTaskResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否成功
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


class FinishBeginnerTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FinishBeginnerTaskResponseBody = None,
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
            temp_model = FinishBeginnerTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRegFormByFlowIdHeaders(TeaModel):
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


class GetApplicationRegFormByFlowIdRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        return self


class GetApplicationRegFormByFlowIdResponseBody(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        creator_user_id: str = None,
        flow_id: str = None,
        form_id: str = None,
        gmt_create_millis: int = None,
        gmt_modified_millis: int = None,
        job_id: str = None,
        status: int = None,
        template_id: str = None,
        template_version: int = None,
    ):
        # 候选人标识
        self.candidate_id = candidate_id
        # 邀填人员工标识
        self.creator_user_id = creator_user_id
        # 招聘流程标识
        self.flow_id = flow_id
        # 表单标识
        self.form_id = form_id
        # 创建时间（邀填时间，单位：毫秒）
        self.gmt_create_millis = gmt_create_millis
        # 更新时间（填写时间，单位：毫秒），仅当表单状态为已填写时有效
        self.gmt_modified_millis = gmt_modified_millis
        # 职位标识
        self.job_id = job_id
        # 表单状态（0表示未填写，1表示已填写）
        self.status = status
        # 模板标识
        self.template_id = template_id
        # 模板版本
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['candidateId'] = self.candidate_id
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.flow_id is not None:
            result['flowId'] = self.flow_id
        if self.form_id is not None:
            result['formId'] = self.form_id
        if self.gmt_create_millis is not None:
            result['gmtCreateMillis'] = self.gmt_create_millis
        if self.gmt_modified_millis is not None:
            result['gmtModifiedMillis'] = self.gmt_modified_millis
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('candidateId') is not None:
            self.candidate_id = m.get('candidateId')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')
        if m.get('formId') is not None:
            self.form_id = m.get('formId')
        if m.get('gmtCreateMillis') is not None:
            self.gmt_create_millis = m.get('gmtCreateMillis')
        if m.get('gmtModifiedMillis') is not None:
            self.gmt_modified_millis = m.get('gmtModifiedMillis')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class GetApplicationRegFormByFlowIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApplicationRegFormByFlowIdResponseBody = None,
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
            temp_model = GetApplicationRegFormByFlowIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCandidateByPhoneNumberHeaders(TeaModel):
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


class GetCandidateByPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        phone_number: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 候选人手机号
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        return self


class GetCandidateByPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        name: str = None,
    ):
        # 候选人标识
        self.candidate_id = candidate_id
        # 候选人姓名
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['candidateId'] = self.candidate_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('candidateId') is not None:
            self.candidate_id = m.get('candidateId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetCandidateByPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCandidateByPhoneNumberResponseBody = None,
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
            temp_model = GetCandidateByPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileUploadInfoHeaders(TeaModel):
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


class GetFileUploadInfoRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        file_name: str = None,
        file_size: int = None,
        md_5: str = None,
        op_user_id: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 文件名称
        self.file_name = file_name
        # 文件大小（单位：字节）
        self.file_size = file_size
        # 文件MD5摘要
        self.md_5 = md_5
        # 操作人员工标识，为空时默认以企业管理员身份进行操作
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class GetFileUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        access_token: str = None,
        access_token_expiration_millis: int = None,
        bucket: str = None,
        end_point: str = None,
        media_id: str = None,
    ):
        # OSS上传所需信息：accessKeyId
        self.access_key_id = access_key_id
        # OSS上传所需信息：accessKeySecret
        self.access_key_secret = access_key_secret
        # OSS上传所需信息：accessToken
        self.access_token = access_token
        # accessToken有效期截止时间（单位：毫秒），需要在此时间之前完成文件上传
        self.access_token_expiration_millis = access_token_expiration_millis
        # OSS上传所需信息：bucket
        self.bucket = bucket
        # OSS上传所需信息：endPoint
        self.end_point = end_point
        # 文件mediaId
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.access_token_expiration_millis is not None:
            result['accessTokenExpirationMillis'] = self.access_token_expiration_millis
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.end_point is not None:
            result['endPoint'] = self.end_point
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('accessTokenExpirationMillis') is not None:
            self.access_token_expiration_millis = m.get('accessTokenExpirationMillis')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endPoint') is not None:
            self.end_point = m.get('endPoint')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        return self


class GetFileUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileUploadInfoResponseBody = None,
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
            temp_model = GetFileUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowIdByRelationEntityIdHeaders(TeaModel):
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


class GetFlowIdByRelationEntityIdRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        relation_entity: str = None,
        relation_entity_id: str = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 招聘流程关联实体
        self.relation_entity = relation_entity
        # 招聘流程关联实体标识
        self.relation_entity_id = relation_entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.relation_entity is not None:
            result['relationEntity'] = self.relation_entity
        if self.relation_entity_id is not None:
            result['relationEntityId'] = self.relation_entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('relationEntity') is not None:
            self.relation_entity = m.get('relationEntity')
        if m.get('relationEntityId') is not None:
            self.relation_entity_id = m.get('relationEntityId')
        return self


class GetFlowIdByRelationEntityIdResponseBody(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        # 招聘流程标识
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['flowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')
        return self


class GetFlowIdByRelationEntityIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFlowIdByRelationEntityIdResponseBody = None,
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
            temp_model = GetFlowIdByRelationEntityIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobAuthHeaders(TeaModel):
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


class GetJobAuthRequest(TeaModel):
    def __init__(
        self,
        op_user_id: str = None,
    ):
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class GetJobAuthResponseBodyJobOwners(TeaModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        # 员工姓名
        self.name = name
        # 员工标识
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


class GetJobAuthResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        job_owners: List[GetJobAuthResponseBodyJobOwners] = None,
    ):
        # 职位ID
        self.job_id = job_id
        # 职位负责人
        self.job_owners = job_owners

    def validate(self):
        if self.job_owners:
            for k in self.job_owners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        result['jobOwners'] = []
        if self.job_owners is not None:
            for k in self.job_owners:
                result['jobOwners'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        self.job_owners = []
        if m.get('jobOwners') is not None:
            for k in m.get('jobOwners'):
                temp_model = GetJobAuthResponseBodyJobOwners()
                self.job_owners.append(temp_model.from_map(k))
        return self


class GetJobAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobAuthResponseBody = None,
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
            temp_model = GetJobAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInterviewsHeaders(TeaModel):
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


class QueryInterviewsRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        candidate_id: str = None,
        start_time_begin_millis: int = None,
        start_time_end_millis: int = None,
        next_token: str = None,
        size: int = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 候选人标识
        self.candidate_id = candidate_id
        # 面试开始时间的查询起始时间（单位：毫秒）
        self.start_time_begin_millis = start_time_begin_millis
        # 面试开始时间的查询结束时间（单位：毫秒）
        self.start_time_end_millis = start_time_end_millis
        # 分页游标，首次调用传空
        self.next_token = next_token
        # 分页大小
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.candidate_id is not None:
            result['candidateId'] = self.candidate_id
        if self.start_time_begin_millis is not None:
            result['startTimeBeginMillis'] = self.start_time_begin_millis
        if self.start_time_end_millis is not None:
            result['startTimeEndMillis'] = self.start_time_end_millis
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('candidateId') is not None:
            self.candidate_id = m.get('candidateId')
        if m.get('startTimeBeginMillis') is not None:
            self.start_time_begin_millis = m.get('startTimeBeginMillis')
        if m.get('startTimeEndMillis') is not None:
            self.start_time_end_millis = m.get('startTimeEndMillis')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class QueryInterviewsResponseBodyListInterviewers(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 面试官员工标识
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


class QueryInterviewsResponseBodyList(TeaModel):
    def __init__(
        self,
        cancelled: bool = None,
        creator_user_id: str = None,
        end_time_millis: int = None,
        interview_id: str = None,
        interviewers: List[QueryInterviewsResponseBodyListInterviewers] = None,
        job_id: str = None,
        start_time_millis: int = None,
    ):
        # 面试是否已取消
        self.cancelled = cancelled
        # 面试创建人员工标识
        self.creator_user_id = creator_user_id
        # 面试结束时间（单位：毫秒）
        self.end_time_millis = end_time_millis
        # 面试标识
        self.interview_id = interview_id
        # 面试官列表
        self.interviewers = interviewers
        # 职位标识
        self.job_id = job_id
        # 面试开始时间（单位：毫秒）
        self.start_time_millis = start_time_millis

    def validate(self):
        if self.interviewers:
            for k in self.interviewers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancelled is not None:
            result['cancelled'] = self.cancelled
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.end_time_millis is not None:
            result['endTimeMillis'] = self.end_time_millis
        if self.interview_id is not None:
            result['interviewId'] = self.interview_id
        result['interviewers'] = []
        if self.interviewers is not None:
            for k in self.interviewers:
                result['interviewers'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.start_time_millis is not None:
            result['startTimeMillis'] = self.start_time_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelled') is not None:
            self.cancelled = m.get('cancelled')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('endTimeMillis') is not None:
            self.end_time_millis = m.get('endTimeMillis')
        if m.get('interviewId') is not None:
            self.interview_id = m.get('interviewId')
        self.interviewers = []
        if m.get('interviewers') is not None:
            for k in m.get('interviewers'):
                temp_model = QueryInterviewsResponseBodyListInterviewers()
                self.interviewers.append(temp_model.from_map(k))
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('startTimeMillis') is not None:
            self.start_time_millis = m.get('startTimeMillis')
        return self


class QueryInterviewsResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryInterviewsResponseBodyList] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # 是否有更多数据
        self.has_more = has_more
        # 数据列表
        self.list = list
        # 下次查询的分页游标
        self.next_token = next_token
        # 总数量
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
                temp_model = QueryInterviewsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryInterviewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInterviewsResponseBody = None,
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
            temp_model = QueryInterviewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRegFormHeaders(TeaModel):
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


class UpdateApplicationRegFormRequestDingPanFile(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_size: int = None,
        file_type: str = None,
        space_id: int = None,
    ):
        # 钉盘文件标识
        self.file_id = file_id
        # 文件名
        self.file_name = file_name
        # 文件大小（单位：字节）
        self.file_size = file_size
        # 文件类型（支持：pdf，doc，docx，ppt，pptx，jpg等）
        self.file_type = file_type
        # 钉盘空间标识
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class UpdateApplicationRegFormRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        content: str = None,
        ding_pan_file: UpdateApplicationRegFormRequestDingPanFile = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 应聘登记表的表单内容
        self.content = content
        # 钉盘文件信息
        self.ding_pan_file = ding_pan_file

    def validate(self):
        if self.ding_pan_file:
            self.ding_pan_file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.content is not None:
            result['content'] = self.content
        if self.ding_pan_file is not None:
            result['dingPanFile'] = self.ding_pan_file.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dingPanFile') is not None:
            temp_model = UpdateApplicationRegFormRequestDingPanFile()
            self.ding_pan_file = temp_model.from_map(m['dingPanFile'])
        return self


class UpdateApplicationRegFormResponseBody(TeaModel):
    def __init__(
        self,
        creator_user_id: str = None,
        form_id: str = None,
        gmt_create_millis: int = None,
        gmt_modified_millis: int = None,
        status: int = None,
        template_id: str = None,
        template_version: int = None,
    ):
        # 邀填人员工标识
        self.creator_user_id = creator_user_id
        # 表单标识
        self.form_id = form_id
        # 创建时间（邀填时间，单位：毫秒）
        self.gmt_create_millis = gmt_create_millis
        # 更新时间（填写时间，单位：毫秒），仅当表单状态为已填写时有效
        self.gmt_modified_millis = gmt_modified_millis
        # 表单状态（0表示未填写，1表示已填写）
        self.status = status
        # 模板标识
        self.template_id = template_id
        # 模板版本
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.form_id is not None:
            result['formId'] = self.form_id
        if self.gmt_create_millis is not None:
            result['gmtCreateMillis'] = self.gmt_create_millis
        if self.gmt_modified_millis is not None:
            result['gmtModifiedMillis'] = self.gmt_modified_millis
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('formId') is not None:
            self.form_id = m.get('formId')
        if m.get('gmtCreateMillis') is not None:
            self.gmt_create_millis = m.get('gmtCreateMillis')
        if m.get('gmtModifiedMillis') is not None:
            self.gmt_modified_millis = m.get('gmtModifiedMillis')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class UpdateApplicationRegFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApplicationRegFormResponseBody = None,
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
            temp_model = UpdateApplicationRegFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInterviewSignInInfoHeaders(TeaModel):
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


class UpdateInterviewSignInInfoRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        sign_in_time_millis: int = None,
    ):
        # 业务标识
        self.biz_code = biz_code
        # 面试签到时间（单位：毫秒）
        self.sign_in_time_millis = sign_in_time_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.sign_in_time_millis is not None:
            result['signInTimeMillis'] = self.sign_in_time_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('signInTimeMillis') is not None:
            self.sign_in_time_millis = m.get('signInTimeMillis')
        return self


class UpdateInterviewSignInInfoResponse(TeaModel):
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


