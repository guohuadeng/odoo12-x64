# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BuyAuthorizationOrderHeaders(TeaModel):
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


class BuyAuthorizationOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        account_number: str = None,
        begin_time_gmt: int = None,
        caller_union_id: str = None,
        charge_type: str = None,
        commerce_type: str = None,
        commodity_type: str = None,
        end_time_gmt: int = None,
        instance_id: str = None,
        instance_name: str = None,
        produce_code: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 账户号
        self.account_number = account_number
        # 开始时间
        self.begin_time_gmt = begin_time_gmt
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 收费类型
        self.charge_type = charge_type
        # 商业类型
        self.commerce_type = commerce_type
        # 商品类型
        self.commodity_type = commodity_type
        # 结束时间
        self.end_time_gmt = end_time_gmt
        # 实例id
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 阿里云产品码
        self.produce_code = produce_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.begin_time_gmt is not None:
            result['beginTimeGMT'] = self.begin_time_gmt
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commerce_type is not None:
            result['commerceType'] = self.commerce_type
        if self.commodity_type is not None:
            result['commodityType'] = self.commodity_type
        if self.end_time_gmt is not None:
            result['endTimeGMT'] = self.end_time_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.produce_code is not None:
            result['produceCode'] = self.produce_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('beginTimeGMT') is not None:
            self.begin_time_gmt = m.get('beginTimeGMT')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commerceType') is not None:
            self.commerce_type = m.get('commerceType')
        if m.get('commodityType') is not None:
            self.commodity_type = m.get('commodityType')
        if m.get('endTimeGMT') is not None:
            self.end_time_gmt = m.get('endTimeGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('produceCode') is not None:
            self.produce_code = m.get('produceCode')
        return self


class BuyAuthorizationOrderResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class BuyAuthorizationOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BuyAuthorizationOrderResponseBody = None,
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
            temp_model = BuyAuthorizationOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuyFreshOrderHeaders(TeaModel):
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


class BuyFreshOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        account_number: str = None,
        begin_time_gmt: int = None,
        caller_union_id: str = None,
        charge_type: str = None,
        commerce_type: str = None,
        commodity_type: str = None,
        end_time_gmt: int = None,
        instance_id: str = None,
        instance_name: str = None,
        produce_code: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 账户号
        self.account_number = account_number
        # 开始时间
        self.begin_time_gmt = begin_time_gmt
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 收费类型
        self.charge_type = charge_type
        # 商业类型
        self.commerce_type = commerce_type
        # 商品类型
        self.commodity_type = commodity_type
        # 结束时间
        self.end_time_gmt = end_time_gmt
        # 实例id
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 阿里云产品码
        self.produce_code = produce_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.begin_time_gmt is not None:
            result['beginTimeGMT'] = self.begin_time_gmt
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commerce_type is not None:
            result['commerceType'] = self.commerce_type
        if self.commodity_type is not None:
            result['commodityType'] = self.commodity_type
        if self.end_time_gmt is not None:
            result['endTimeGMT'] = self.end_time_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.produce_code is not None:
            result['produceCode'] = self.produce_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('beginTimeGMT') is not None:
            self.begin_time_gmt = m.get('beginTimeGMT')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commerceType') is not None:
            self.commerce_type = m.get('commerceType')
        if m.get('commodityType') is not None:
            self.commodity_type = m.get('commodityType')
        if m.get('endTimeGMT') is not None:
            self.end_time_gmt = m.get('endTimeGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('produceCode') is not None:
            self.produce_code = m.get('produceCode')
        return self


class BuyFreshOrderResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class BuyFreshOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BuyFreshOrderResponseBody = None,
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
            temp_model = BuyFreshOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCloudAccountStatusHeaders(TeaModel):
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


class CheckCloudAccountStatusRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class CheckCloudAccountStatusResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class CheckCloudAccountStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckCloudAccountStatusResponseBody = None,
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
            temp_model = CheckCloudAccountStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFormDataHeaders(TeaModel):
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


class DeleteFormDataRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_instance_id: str = None,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 要删除的表单数据ID
        self.form_instance_id = form_instance_id
        # 语言
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteFormDataResponse(TeaModel):
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


class DeleteInstanceHeaders(TeaModel):
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


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言
        self.language = language
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteInstanceResponse(TeaModel):
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


class DeleteSequenceHeaders(TeaModel):
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


class DeleteSequenceRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        sequence: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.language = language
        self.sequence = sequence
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteSequenceResponse(TeaModel):
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


class DeployFunctionCallbackHeaders(TeaModel):
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


class DeployFunctionCallbackRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        custom_domain: str = None,
        deploy_stage: str = None,
        gate_way_app_key: str = None,
        gate_way_app_secret: str = None,
        gate_way_domain: str = None,
    ):
        # 云应用id
        self.app_id = app_id
        # 自定义域名
        self.custom_domain = custom_domain
        # 部署阶段
        self.deploy_stage = deploy_stage
        # api网关实例的AppKey
        self.gate_way_app_key = gate_way_app_key
        # api网关实例的APPSecret
        self.gate_way_app_secret = gate_way_app_secret
        # api网关二级域名
        self.gate_way_domain = gate_way_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.custom_domain is not None:
            result['customDomain'] = self.custom_domain
        if self.deploy_stage is not None:
            result['deployStage'] = self.deploy_stage
        if self.gate_way_app_key is not None:
            result['gateWayAppKey'] = self.gate_way_app_key
        if self.gate_way_app_secret is not None:
            result['gateWayAppSecret'] = self.gate_way_app_secret
        if self.gate_way_domain is not None:
            result['gateWayDomain'] = self.gate_way_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('customDomain') is not None:
            self.custom_domain = m.get('customDomain')
        if m.get('deployStage') is not None:
            self.deploy_stage = m.get('deployStage')
        if m.get('gateWayAppKey') is not None:
            self.gate_way_app_key = m.get('gateWayAppKey')
        if m.get('gateWayAppSecret') is not None:
            self.gate_way_app_secret = m.get('gateWayAppSecret')
        if m.get('gateWayDomain') is not None:
            self.gate_way_domain = m.get('gateWayDomain')
        return self


class DeployFunctionCallbackResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 是否处理成功
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


class DeployFunctionCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployFunctionCallbackResponseBody = None,
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
            temp_model = DeployFunctionCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteCustomApiHeaders(TeaModel):
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


class ExecuteCustomApiRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        data: str = None,
        language: str = None,
        service_id: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.data = data
        self.language = language
        self.service_id = service_id
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.data is not None:
            result['data'] = self.data
        if self.language is not None:
            result['language'] = self.language
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteCustomApiResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
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


class ExecuteCustomApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteCustomApiResponseBody = None,
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
            temp_model = ExecuteCustomApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecutePlatformTaskHeaders(TeaModel):
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


class ExecutePlatformTaskRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_data_json: str = None,
        language: str = None,
        no_execute_expressions: str = None,
        out_result: str = None,
        process_instance_id: str = None,
        remark: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 更新的表单数据
        self.form_data_json = form_data_json
        # 语言
        self.language = language
        # 是否不执行校验&关联操作
        self.no_execute_expressions = no_execute_expressions
        # 审批结果
        self.out_result = out_result
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 审批意见
        self.remark = remark
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_data_json is not None:
            result['formDataJson'] = self.form_data_json
        if self.language is not None:
            result['language'] = self.language
        if self.no_execute_expressions is not None:
            result['noExecuteExpressions'] = self.no_execute_expressions
        if self.out_result is not None:
            result['outResult'] = self.out_result
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formDataJson') is not None:
            self.form_data_json = m.get('formDataJson')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('noExecuteExpressions') is not None:
            self.no_execute_expressions = m.get('noExecuteExpressions')
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecutePlatformTaskResponse(TeaModel):
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


class ExecuteTaskHeaders(TeaModel):
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


class ExecuteTaskRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        digital_sign_url: str = None,
        form_data_json: str = None,
        language: str = None,
        no_execute_expressions: str = None,
        out_result: str = None,
        process_instance_id: str = None,
        remark: str = None,
        system_token: str = None,
        task_id: int = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 电子签名
        self.digital_sign_url = digital_sign_url
        # 更新的表单值
        self.form_data_json = form_data_json
        # 语言
        self.language = language
        # 是否不执行校验&关联操作
        self.no_execute_expressions = no_execute_expressions
        # 审批结果
        self.out_result = out_result
        # 实例ID
        self.process_instance_id = process_instance_id
        # 审批意见
        self.remark = remark
        # 应用秘钥
        self.system_token = system_token
        # 任务ID
        self.task_id = task_id
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.digital_sign_url is not None:
            result['digitalSignUrl'] = self.digital_sign_url
        if self.form_data_json is not None:
            result['formDataJson'] = self.form_data_json
        if self.language is not None:
            result['language'] = self.language
        if self.no_execute_expressions is not None:
            result['noExecuteExpressions'] = self.no_execute_expressions
        if self.out_result is not None:
            result['outResult'] = self.out_result
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('digitalSignUrl') is not None:
            self.digital_sign_url = m.get('digitalSignUrl')
        if m.get('formDataJson') is not None:
            self.form_data_json = m.get('formDataJson')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('noExecuteExpressions') is not None:
            self.no_execute_expressions = m.get('noExecuteExpressions')
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteTaskResponse(TeaModel):
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


class ExpireCommodityHeaders(TeaModel):
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


class ExpireCommodityRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ExpireCommodityResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExpireCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExpireCommodityResponseBody = None,
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
            temp_model = ExpireCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActivationCodeByCallerUnionIdHeaders(TeaModel):
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


class GetActivationCodeByCallerUnionIdRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class GetActivationCodeByCallerUnionIdResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
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


class GetActivationCodeByCallerUnionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetActivationCodeByCallerUnionIdResponseBody = None,
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
            temp_model = GetActivationCodeByCallerUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActivityButtonListHeaders(TeaModel):
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


class GetActivityButtonListRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 语言环境
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetActivityButtonListResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias_in_chinese: str = None,
        alias_in_english: str = None,
    ):
        # alias
        self.alias_in_chinese = alias_in_chinese
        # aliasEn
        self.alias_in_english = alias_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_in_chinese is not None:
            result['aliasInChinese'] = self.alias_in_chinese
        if self.alias_in_english is not None:
            result['aliasInEnglish'] = self.alias_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasInChinese') is not None:
            self.alias_in_chinese = m.get('aliasInChinese')
        if m.get('aliasInEnglish') is not None:
            self.alias_in_english = m.get('aliasInEnglish')
        return self


class GetActivityButtonListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetActivityButtonListResponseBodyResult] = None,
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
                temp_model = GetActivityButtonListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetActivityButtonListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetActivityButtonListResponseBody = None,
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
            temp_model = GetActivityButtonListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActivityListHeaders(TeaModel):
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


class GetActivityListRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_code: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.language = language
        self.process_code = process_code
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetActivityListResponseBodyResult(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_name: str = None,
        activity_name_in_english: str = None,
    ):
        # activityId
        self.activity_id = activity_id
        # activityName
        self.activity_name = activity_name
        # activityNameEn
        self.activity_name_in_english = activity_name_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.activity_name is not None:
            result['activityName'] = self.activity_name
        if self.activity_name_in_english is not None:
            result['activityNameInEnglish'] = self.activity_name_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('activityName') is not None:
            self.activity_name = m.get('activityName')
        if m.get('activityNameInEnglish') is not None:
            self.activity_name_in_english = m.get('activityNameInEnglish')
        return self


class GetActivityListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetActivityListResponseBodyResult] = None,
    ):
        # Id of the request
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
                temp_model = GetActivityListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetActivityListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetActivityListResponseBody = None,
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
            temp_model = GetActivityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationAuthorizationServicePlatformResourceHeaders(TeaModel):
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


class GetApplicationAuthorizationServicePlatformResourceRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class GetApplicationAuthorizationServicePlatformResourceResponseBody(TeaModel):
    def __init__(
        self,
        account_total_amount: int = None,
        account_usage_amount: int = None,
        app_total_amount: int = None,
        attachment_total_amount: int = None,
        attachment_usage_amount: int = None,
        instance_id: str = None,
        instance_total_amount: int = None,
        instance_usage_amount: int = None,
        plugin_usage_amount: int = None,
    ):
        # accountTotalAmount
        self.account_total_amount = account_total_amount
        # accountUsageAmount
        self.account_usage_amount = account_usage_amount
        # appTotalAmount
        self.app_total_amount = app_total_amount
        # attachmentTotalAmount
        self.attachment_total_amount = attachment_total_amount
        # attachmentUsageAmount
        self.attachment_usage_amount = attachment_usage_amount
        # instanceId
        self.instance_id = instance_id
        # instanceTotalAmount
        self.instance_total_amount = instance_total_amount
        # instanceUsageAmount
        self.instance_usage_amount = instance_usage_amount
        # pluginUsageAmount
        self.plugin_usage_amount = plugin_usage_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_total_amount is not None:
            result['accountTotalAmount'] = self.account_total_amount
        if self.account_usage_amount is not None:
            result['accountUsageAmount'] = self.account_usage_amount
        if self.app_total_amount is not None:
            result['appTotalAmount'] = self.app_total_amount
        if self.attachment_total_amount is not None:
            result['attachmentTotalAmount'] = self.attachment_total_amount
        if self.attachment_usage_amount is not None:
            result['attachmentUsageAmount'] = self.attachment_usage_amount
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_total_amount is not None:
            result['instanceTotalAmount'] = self.instance_total_amount
        if self.instance_usage_amount is not None:
            result['instanceUsageAmount'] = self.instance_usage_amount
        if self.plugin_usage_amount is not None:
            result['pluginUsageAmount'] = self.plugin_usage_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountTotalAmount') is not None:
            self.account_total_amount = m.get('accountTotalAmount')
        if m.get('accountUsageAmount') is not None:
            self.account_usage_amount = m.get('accountUsageAmount')
        if m.get('appTotalAmount') is not None:
            self.app_total_amount = m.get('appTotalAmount')
        if m.get('attachmentTotalAmount') is not None:
            self.attachment_total_amount = m.get('attachmentTotalAmount')
        if m.get('attachmentUsageAmount') is not None:
            self.attachment_usage_amount = m.get('attachmentUsageAmount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceTotalAmount') is not None:
            self.instance_total_amount = m.get('instanceTotalAmount')
        if m.get('instanceUsageAmount') is not None:
            self.instance_usage_amount = m.get('instanceUsageAmount')
        if m.get('pluginUsageAmount') is not None:
            self.plugin_usage_amount = m.get('pluginUsageAmount')
        return self


class GetApplicationAuthorizationServicePlatformResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApplicationAuthorizationServicePlatformResourceResponseBody = None,
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
            temp_model = GetApplicationAuthorizationServicePlatformResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpAccomplishmentTasksHeaders(TeaModel):
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


class GetCorpAccomplishmentTasksRequest(TeaModel):
    def __init__(
        self,
        app_types: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        token: str = None,
    ):
        # 应用标识列表
        self.app_types = app_types
        # 创建时间开始
        self.create_from_time_gmt = create_from_time_gmt
        # 创建时间结束
        self.create_to_time_gmt = create_to_time_gmt
        # 关键词
        self.keyword = keyword
        # 语言环境
        self.language = language
        # 当前页
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 流程code列表
        self.process_codes = process_codes
        # 验权token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_types is not None:
            result['appTypes'] = self.app_types
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_codes is not None:
            result['processCodes'] = self.process_codes
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appTypes') is not None:
            self.app_types = m.get('appTypes')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processCodes') is not None:
            self.process_codes = m.get('processCodes')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetCorpAccomplishmentTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        actual_actioner_id: str = None,
        app_type: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_email: str = None,
        originator_id: str = None,
        originator_name: str = None,
        originator_name_in_english: str = None,
        originator_nick_name: str = None,
        originator_nick_name_in_english: str = None,
        originator_photo: str = None,
        out_result: str = None,
        out_result_name: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        # activeTime
        self.active_time_gmt = active_time_gmt
        # actualActionerId
        self.actual_actioner_id = actual_actioner_id
        # appType
        self.app_type = app_type
        # createTime
        self.create_time_gmt = create_time_gmt
        # finishTime
        self.finish_time_gmt = finish_time_gmt
        # originatorEmail
        self.originator_email = originator_email
        # originatorId
        self.originator_id = originator_id
        # originatorName
        self.originator_name = originator_name
        # originatorNameEn
        self.originator_name_in_english = originator_name_in_english
        # originatorNickName
        self.originator_nick_name = originator_nick_name
        # originatorNickNameEn
        self.originator_nick_name_in_english = originator_nick_name_in_english
        # originatorPhoto
        self.originator_photo = originator_photo
        # outResult
        self.out_result = out_result
        # outResultName
        self.out_result_name = out_result_name
        # processInstanceId
        self.process_instance_id = process_instance_id
        # status
        self.status = status
        # taskId
        self.task_id = task_id
        # taskType
        self.task_type = task_type
        # title
        self.title = title
        # titleEn
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_gmt is not None:
            result['activeTimeGMT'] = self.active_time_gmt
        if self.actual_actioner_id is not None:
            result['actualActionerId'] = self.actual_actioner_id
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.originator_email is not None:
            result['originatorEmail'] = self.originator_email
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.originator_name is not None:
            result['originatorName'] = self.originator_name
        if self.originator_name_in_english is not None:
            result['originatorNameInEnglish'] = self.originator_name_in_english
        if self.originator_nick_name is not None:
            result['originatorNickName'] = self.originator_nick_name
        if self.originator_nick_name_in_english is not None:
            result['originatorNickNameInEnglish'] = self.originator_nick_name_in_english
        if self.originator_photo is not None:
            result['originatorPhoto'] = self.originator_photo
        if self.out_result is not None:
            result['outResult'] = self.out_result
        if self.out_result_name is not None:
            result['outResultName'] = self.out_result_name
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.title is not None:
            result['title'] = self.title
        if self.title_in_english is not None:
            result['titleInEnglish'] = self.title_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTimeGMT') is not None:
            self.active_time_gmt = m.get('activeTimeGMT')
        if m.get('actualActionerId') is not None:
            self.actual_actioner_id = m.get('actualActionerId')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('originatorEmail') is not None:
            self.originator_email = m.get('originatorEmail')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('originatorName') is not None:
            self.originator_name = m.get('originatorName')
        if m.get('originatorNameInEnglish') is not None:
            self.originator_name_in_english = m.get('originatorNameInEnglish')
        if m.get('originatorNickName') is not None:
            self.originator_nick_name = m.get('originatorNickName')
        if m.get('originatorNickNameInEnglish') is not None:
            self.originator_nick_name_in_english = m.get('originatorNickNameInEnglish')
        if m.get('originatorPhoto') is not None:
            self.originator_photo = m.get('originatorPhoto')
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        if m.get('outResultName') is not None:
            self.out_result_name = m.get('outResultName')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('titleInEnglish') is not None:
            self.title_in_english = m.get('titleInEnglish')
        return self


class GetCorpAccomplishmentTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetCorpAccomplishmentTasksResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetCorpAccomplishmentTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetCorpAccomplishmentTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpAccomplishmentTasksResponseBody = None,
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
            temp_model = GetCorpAccomplishmentTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpLevelByAccountIdHeaders(TeaModel):
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


class GetCorpLevelByAccountIdRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class GetCorpLevelByAccountIdResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
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


class GetCorpLevelByAccountIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpLevelByAccountIdResponseBody = None,
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
            temp_model = GetCorpLevelByAccountIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpTasksHeaders(TeaModel):
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


class GetCorpTasksRequest(TeaModel):
    def __init__(
        self,
        app_types: str = None,
        corp_id: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        token: str = None,
        user_id: str = None,
    ):
        # 应用标识列表
        self.app_types = app_types
        # 企业ID
        self.corp_id = corp_id
        # 创建时间开始
        self.create_from_time_gmt = create_from_time_gmt
        # 创建时间结束
        self.create_to_time_gmt = create_to_time_gmt
        # 关键词
        self.keyword = keyword
        # 语言环境
        self.language = language
        # 当前页
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 流程code列表
        self.process_codes = process_codes
        # 验权token
        self.token = token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_types is not None:
            result['appTypes'] = self.app_types
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_codes is not None:
            result['processCodes'] = self.process_codes
        if self.token is not None:
            result['token'] = self.token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appTypes') is not None:
            self.app_types = m.get('appTypes')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processCodes') is not None:
            self.process_codes = m.get('processCodes')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetCorpTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        actual_actioner_id: str = None,
        app_type: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_email: str = None,
        originator_id: str = None,
        originator_name: str = None,
        originator_name_in_english: str = None,
        originator_nick_name: str = None,
        originator_nick_name_en: str = None,
        originator_photo: str = None,
        out_result: str = None,
        out_result_name: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        # activeTime
        self.active_time_gmt = active_time_gmt
        # actualActionerId
        self.actual_actioner_id = actual_actioner_id
        # appType
        self.app_type = app_type
        # createTime
        self.create_time_gmt = create_time_gmt
        # finishTime
        self.finish_time_gmt = finish_time_gmt
        # originatorEmail
        self.originator_email = originator_email
        # originatorId
        self.originator_id = originator_id
        # originatorName
        self.originator_name = originator_name
        # originatorNameEn
        self.originator_name_in_english = originator_name_in_english
        # originatorNickName
        self.originator_nick_name = originator_nick_name
        # originatorNickNameEn
        self.originator_nick_name_en = originator_nick_name_en
        # originatorPhoto
        self.originator_photo = originator_photo
        # outResult
        self.out_result = out_result
        # outResultName
        self.out_result_name = out_result_name
        # processInstanceId
        self.process_instance_id = process_instance_id
        # status
        self.status = status
        # taskId
        self.task_id = task_id
        # taskType
        self.task_type = task_type
        # title
        self.title = title
        # titleEn
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_gmt is not None:
            result['activeTimeGMT'] = self.active_time_gmt
        if self.actual_actioner_id is not None:
            result['actualActionerId'] = self.actual_actioner_id
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.originator_email is not None:
            result['originatorEmail'] = self.originator_email
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.originator_name is not None:
            result['originatorName'] = self.originator_name
        if self.originator_name_in_english is not None:
            result['originatorNameInEnglish'] = self.originator_name_in_english
        if self.originator_nick_name is not None:
            result['originatorNickName'] = self.originator_nick_name
        if self.originator_nick_name_en is not None:
            result['originatorNickNameEn'] = self.originator_nick_name_en
        if self.originator_photo is not None:
            result['originatorPhoto'] = self.originator_photo
        if self.out_result is not None:
            result['outResult'] = self.out_result
        if self.out_result_name is not None:
            result['outResultName'] = self.out_result_name
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.title is not None:
            result['title'] = self.title
        if self.title_in_english is not None:
            result['titleInEnglish'] = self.title_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTimeGMT') is not None:
            self.active_time_gmt = m.get('activeTimeGMT')
        if m.get('actualActionerId') is not None:
            self.actual_actioner_id = m.get('actualActionerId')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('originatorEmail') is not None:
            self.originator_email = m.get('originatorEmail')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('originatorName') is not None:
            self.originator_name = m.get('originatorName')
        if m.get('originatorNameInEnglish') is not None:
            self.originator_name_in_english = m.get('originatorNameInEnglish')
        if m.get('originatorNickName') is not None:
            self.originator_nick_name = m.get('originatorNickName')
        if m.get('originatorNickNameEn') is not None:
            self.originator_nick_name_en = m.get('originatorNickNameEn')
        if m.get('originatorPhoto') is not None:
            self.originator_photo = m.get('originatorPhoto')
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        if m.get('outResultName') is not None:
            self.out_result_name = m.get('outResultName')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('titleInEnglish') is not None:
            self.title_in_english = m.get('titleInEnglish')
        return self


class GetCorpTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetCorpTasksResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetCorpTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetCorpTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpTasksResponseBody = None,
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
            temp_model = GetCorpTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFormComponentDefinitionListHeaders(TeaModel):
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


class GetFormComponentDefinitionListRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
        version: int = None,
    ):
        # 语言
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id
        # 表单版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetFormComponentDefinitionListResponseBodyResult(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        field_id: str = None,
        label: str = None,
        parent_id: str = None,
    ):
        # componentName
        self.component_name = component_name
        # key
        self.field_id = field_id
        # label
        self.label = label
        # parentId
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.field_id is not None:
            result['fieldId'] = self.field_id
        if self.label is not None:
            result['label'] = self.label
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        return self


class GetFormComponentDefinitionListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetFormComponentDefinitionListResponseBodyResult] = None,
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
                temp_model = GetFormComponentDefinitionListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetFormComponentDefinitionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFormComponentDefinitionListResponseBody = None,
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
            temp_model = GetFormComponentDefinitionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFormDataByIDHeaders(TeaModel):
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


class GetFormDataByIDRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 钉钉userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetFormDataByIDResponseBodyOriginatorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # 国际化
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetFormDataByIDResponseBodyOriginator(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: GetFormDataByIDResponseBodyOriginatorName = None,
        user_id: str = None,
    ):
        # 部门名称
        self.department_name = department_name
        # 邮箱
        self.email = email
        # 用户名
        self.name = name
        # 用户工号
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetFormDataByIDResponseBodyOriginatorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetFormDataByIDResponseBody(TeaModel):
    def __init__(
        self,
        form_data: Dict[str, Any] = None,
        form_inst_id: str = None,
        form_uuid: str = None,
        modified_time_gmt: str = None,
        originator: GetFormDataByIDResponseBodyOriginator = None,
    ):
        # 表单数据详情
        self.form_data = form_data
        # 表单实例ID
        self.form_inst_id = form_inst_id
        # 表单ID
        self.form_uuid = form_uuid
        # 最后修改时间
        self.modified_time_gmt = modified_time_gmt
        # 发起人详情
        self.originator = originator

    def validate(self):
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_data is not None:
            result['formData'] = self.form_data
        if self.form_inst_id is not None:
            result['formInstId'] = self.form_inst_id
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formData') is not None:
            self.form_data = m.get('formData')
        if m.get('formInstId') is not None:
            self.form_inst_id = m.get('formInstId')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('originator') is not None:
            temp_model = GetFormDataByIDResponseBodyOriginator()
            self.originator = temp_model.from_map(m['originator'])
        return self


class GetFormDataByIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFormDataByIDResponseBody = None,
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
            temp_model = GetFormDataByIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceByIdHeaders(TeaModel):
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


class GetInstanceByIdRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceByIdResponseBodyActionExecutorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstanceByIdResponseBodyActionExecutor(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: GetInstanceByIdResponseBodyActionExecutorName = None,
        user_id: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # email
        self.email = email
        # name
        self.name = name
        # userId
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstanceByIdResponseBodyActionExecutorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceByIdResponseBodyOriginatorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstanceByIdResponseBodyOriginator(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: GetInstanceByIdResponseBodyOriginatorName = None,
        user_id: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # email
        self.email = email
        # name
        self.name = name
        # userId
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstanceByIdResponseBodyOriginatorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceByIdResponseBody(TeaModel):
    def __init__(
        self,
        action_executor: List[GetInstanceByIdResponseBodyActionExecutor] = None,
        approved_result: str = None,
        create_time_gmt: str = None,
        data: Dict[str, Any] = None,
        form_uuid: str = None,
        instance_status: str = None,
        modified_time_gmt: str = None,
        originator: GetInstanceByIdResponseBodyOriginator = None,
        process_code: str = None,
        process_instance_id: str = None,
        title: str = None,
        version: int = None,
    ):
        # actionExecutor
        self.action_executor = action_executor
        # approvedResult
        self.approved_result = approved_result
        # 创建时间
        self.create_time_gmt = create_time_gmt
        # data
        self.data = data
        # formUuid
        self.form_uuid = form_uuid
        # instanceStatus
        self.instance_status = instance_status
        # 修改时间
        self.modified_time_gmt = modified_time_gmt
        # originator
        self.originator = originator
        # processCode
        self.process_code = process_code
        # processInstanceId
        self.process_instance_id = process_instance_id
        # title
        self.title = title
        # version
        self.version = version

    def validate(self):
        if self.action_executor:
            for k in self.action_executor:
                if k:
                    k.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actionExecutor'] = []
        if self.action_executor is not None:
            for k in self.action_executor:
                result['actionExecutor'].append(k.to_map() if k else None)
        if self.approved_result is not None:
            result['approvedResult'] = self.approved_result
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.data is not None:
            result['data'] = self.data
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_executor = []
        if m.get('actionExecutor') is not None:
            for k in m.get('actionExecutor'):
                temp_model = GetInstanceByIdResponseBodyActionExecutor()
                self.action_executor.append(temp_model.from_map(k))
        if m.get('approvedResult') is not None:
            self.approved_result = m.get('approvedResult')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('originator') is not None:
            temp_model = GetInstanceByIdResponseBodyOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetInstanceByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceByIdResponseBody = None,
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
            temp_model = GetInstanceByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceIdListHeaders(TeaModel):
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


class GetInstanceIdListRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        approved_result: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        instance_status: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        search_field_json: str = None,
        system_token: str = None,
        task_id: str = None,
        user_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 流程审批结果
        self.approved_result = approved_result
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表
        self.create_from_time_gmt = create_from_time_gmt
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。
        self.create_to_time_gmt = create_to_time_gmt
        # 表单ID
        self.form_uuid = form_uuid
        # 实例状态
        self.instance_status = instance_status
        # 语言
        self.language = language
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表
        self.modified_from_time_gmt = modified_from_time_gmt
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。
        self.modified_to_time_gmt = modified_to_time_gmt
        # 根据流程发起人工号查询
        self.originator_id = originator_id
        # 根据表单内组件值查询
        self.search_field_json = search_field_json
        # 应用秘钥
        self.system_token = system_token
        # 任务ID
        self.task_id = task_id
        # 钉钉的userId
        self.user_id = user_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.approved_result is not None:
            result['approvedResult'] = self.approved_result
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.language is not None:
            result['language'] = self.language
        if self.modified_from_time_gmt is not None:
            result['modifiedFromTimeGMT'] = self.modified_from_time_gmt
        if self.modified_to_time_gmt is not None:
            result['modifiedToTimeGMT'] = self.modified_to_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.search_field_json is not None:
            result['searchFieldJson'] = self.search_field_json
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('approvedResult') is not None:
            self.approved_result = m.get('approvedResult')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('modifiedFromTimeGMT')
        if m.get('modifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('modifiedToTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('searchFieldJson') is not None:
            self.search_field_json = m.get('searchFieldJson')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetInstanceIdListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetInstanceIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceIdListResponseBody = None,
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
            temp_model = GetInstanceIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancesHeaders(TeaModel):
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


class GetInstancesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        approved_result: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        instance_status: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        search_field_json: str = None,
        system_token: str = None,
        task_id: str = None,
        user_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 审批结果。可选值为：agree, disagree。 分别表示：同意， 拒绝。
        self.approved_result = approved_result
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表, 字符串格式，且为yyyy-MM-DD格式
        self.create_from_time_gmt = create_from_time_gmt
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。字符串格式，且为yyyy-MM-DD格式。 和createFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)创建的数据。
        self.create_to_time_gmt = create_to_time_gmt
        # 表单ID
        self.form_uuid = form_uuid
        # 实例状态, 可选值为：RUNNING,TERMINATED,COMPLETED,ERROR。 分别代表：运行中，已终止，已完成，异常。
        self.instance_status = instance_status
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。字符串格式，且为yyyy-MM-DD格式
        self.modified_from_time_gmt = modified_from_time_gmt
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。字符串格式，且为yyyy-MM-DD格式。 和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。
        self.modified_to_time_gmt = modified_to_time_gmt
        # 根据数据提交人工号查询
        self.originator_id = originator_id
        # 根据表单内组件值查询
        self.search_field_json = search_field_json
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 任务ID。一般用不到。
        self.task_id = task_id
        # 钉钉userId
        self.user_id = user_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.approved_result is not None:
            result['approvedResult'] = self.approved_result
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.language is not None:
            result['language'] = self.language
        if self.modified_from_time_gmt is not None:
            result['modifiedFromTimeGMT'] = self.modified_from_time_gmt
        if self.modified_to_time_gmt is not None:
            result['modifiedToTimeGMT'] = self.modified_to_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.search_field_json is not None:
            result['searchFieldJson'] = self.search_field_json
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('approvedResult') is not None:
            self.approved_result = m.get('approvedResult')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('modifiedFromTimeGMT')
        if m.get('modifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('modifiedToTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('searchFieldJson') is not None:
            self.search_field_json = m.get('searchFieldJson')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetInstancesResponseBodyDataActionExecutorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstancesResponseBodyDataActionExecutor(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: GetInstancesResponseBodyDataActionExecutorName = None,
        user_id: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # email
        self.email = email
        # name
        self.name = name
        # userId
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstancesResponseBodyDataActionExecutorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstancesResponseBodyDataOriginatorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstancesResponseBodyDataOriginator(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: GetInstancesResponseBodyDataOriginatorName = None,
        user_id: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # email
        self.email = email
        # name
        self.name = name
        # userId
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstancesResponseBodyDataOriginatorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        action_executor: List[GetInstancesResponseBodyDataActionExecutor] = None,
        approved_result: str = None,
        create_time_gmt: str = None,
        data: Dict[str, Any] = None,
        form_uuid: str = None,
        instance_status: str = None,
        modified_time_gmt: str = None,
        originator: GetInstancesResponseBodyDataOriginator = None,
        process_code: str = None,
        process_instance_id: str = None,
        title: str = None,
        version: int = None,
    ):
        # actioners
        self.action_executor = action_executor
        # approvedResult
        self.approved_result = approved_result
        # 创建时间
        self.create_time_gmt = create_time_gmt
        # data
        self.data = data
        # formUuid
        self.form_uuid = form_uuid
        # instanceStatus
        self.instance_status = instance_status
        # 修改时间
        self.modified_time_gmt = modified_time_gmt
        # originator
        self.originator = originator
        # processCode
        self.process_code = process_code
        # processInstanceId
        self.process_instance_id = process_instance_id
        # title
        self.title = title
        # version
        self.version = version

    def validate(self):
        if self.action_executor:
            for k in self.action_executor:
                if k:
                    k.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actionExecutor'] = []
        if self.action_executor is not None:
            for k in self.action_executor:
                result['actionExecutor'].append(k.to_map() if k else None)
        if self.approved_result is not None:
            result['approvedResult'] = self.approved_result
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.data is not None:
            result['data'] = self.data
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_executor = []
        if m.get('actionExecutor') is not None:
            for k in m.get('actionExecutor'):
                temp_model = GetInstancesResponseBodyDataActionExecutor()
                self.action_executor.append(temp_model.from_map(k))
        if m.get('approvedResult') is not None:
            self.approved_result = m.get('approvedResult')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('originator') is not None:
            temp_model = GetInstancesResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetInstancesResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstancesResponseBody = None,
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
            temp_model = GetInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancesByIdListHeaders(TeaModel):
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


class GetInstancesByIdListRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_ids: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言
        self.language = language
        # 流程实例ID列表，多个用,分割
        self.process_instance_ids = process_instance_ids
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_ids is not None:
            result['processInstanceIds'] = self.process_instance_ids
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceIds') is not None:
            self.process_instance_ids = m.get('processInstanceIds')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstancesByIdListResponseBodyResultActionExecutorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # 国际化
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstancesByIdListResponseBodyResultActionExecutor(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: GetInstancesByIdListResponseBodyResultActionExecutorName = None,
        user_id: str = None,
    ):
        # 部门名称
        self.department_name = department_name
        # 邮箱
        self.email = email
        # 用户名
        self.name = name
        # 用户工号
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstancesByIdListResponseBodyResultActionExecutorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstancesByIdListResponseBodyResultOriginatorName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # 国际化
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstancesByIdListResponseBodyResultOriginator(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: GetInstancesByIdListResponseBodyResultOriginatorName = None,
        user_id: str = None,
    ):
        # 部门名称
        self.department_name = department_name
        # 邮箱
        self.email = email
        # 用户名
        self.name = name
        # 用户工号
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.email is not None:
            result['email'] = self.email
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('name') is not None:
            temp_model = GetInstancesByIdListResponseBodyResultOriginatorName()
            self.name = temp_model.from_map(m['name'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstancesByIdListResponseBodyResult(TeaModel):
    def __init__(
        self,
        action_executor: List[GetInstancesByIdListResponseBodyResultActionExecutor] = None,
        approved_result: str = None,
        data: Dict[str, Any] = None,
        form_uuid: str = None,
        instance_status: str = None,
        originator: GetInstancesByIdListResponseBodyResultOriginator = None,
        process_code: str = None,
        process_instance_id: str = None,
        title: str = None,
    ):
        # 流程实例当前任务执行人列表
        self.action_executor = action_executor
        # 流程结束时的审批结论
        self.approved_result = approved_result
        # 表单数据
        self.data = data
        # 流程表单ID
        self.form_uuid = form_uuid
        # 实例状态
        self.instance_status = instance_status
        # 发起人信息
        self.originator = originator
        # 流程Code
        self.process_code = process_code
        # 实例ID
        self.process_instance_id = process_instance_id
        # 实例标题
        self.title = title

    def validate(self):
        if self.action_executor:
            for k in self.action_executor:
                if k:
                    k.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actionExecutor'] = []
        if self.action_executor is not None:
            for k in self.action_executor:
                result['actionExecutor'].append(k.to_map() if k else None)
        if self.approved_result is not None:
            result['approvedResult'] = self.approved_result
        if self.data is not None:
            result['data'] = self.data
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_executor = []
        if m.get('actionExecutor') is not None:
            for k in m.get('actionExecutor'):
                temp_model = GetInstancesByIdListResponseBodyResultActionExecutor()
                self.action_executor.append(temp_model.from_map(k))
        if m.get('approvedResult') is not None:
            self.approved_result = m.get('approvedResult')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('originator') is not None:
            temp_model = GetInstancesByIdListResponseBodyResultOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetInstancesByIdListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetInstancesByIdListResponseBodyResult] = None,
    ):
        # 流程实例列表
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
                temp_model = GetInstancesByIdListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetInstancesByIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstancesByIdListResponseBody = None,
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
            temp_model = GetInstancesByIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMeCorpSubmissionHeaders(TeaModel):
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


class GetMeCorpSubmissionRequest(TeaModel):
    def __init__(
        self,
        app_types: str = None,
        corp_id: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        token: str = None,
    ):
        # 应用标识列表
        self.app_types = app_types
        # 企业ID
        self.corp_id = corp_id
        # 创建时间开始
        self.create_from_time_gmt = create_from_time_gmt
        # 创建时间结束
        self.create_to_time_gmt = create_to_time_gmt
        # 关键词
        self.keyword = keyword
        # 语言环境
        self.language = language
        # 当前页
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 流程code列表
        self.process_codes = process_codes
        # 验权token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_types is not None:
            result['appTypes'] = self.app_types
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_codes is not None:
            result['processCodes'] = self.process_codes
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appTypes') is not None:
            self.app_types = m.get('appTypes')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processCodes') is not None:
            self.process_codes = m.get('processCodes')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetMeCorpSubmissionResponseBodyDataActioner(TeaModel):
    def __init__(
        self,
        bu_name: str = None,
        email: str = None,
        employee_type: str = None,
        employee_type_information: str = None,
        human_resource_group_work_number: str = None,
        is_system_admin: bool = None,
        level: str = None,
        name: str = None,
        nick_name: str = None,
        order_number: str = None,
        personal_photo: str = None,
        personal_photo_url: str = None,
        pinyin_name_all: str = None,
        pinyin_nick_name: str = None,
        state: str = None,
        super_user_id: str = None,
        tb_wang: str = None,
        user_id: str = None,
    ):
        # buName
        self.bu_name = bu_name
        # email
        self.email = email
        # empType
        self.employee_type = employee_type
        # employeeTypeInformation
        self.employee_type_information = employee_type_information
        # hrgWorkNo
        self.human_resource_group_work_number = human_resource_group_work_number
        # isSystemAdmin
        self.is_system_admin = is_system_admin
        # level
        self.level = level
        # name
        self.name = name
        # nickName
        self.nick_name = nick_name
        # orderNum
        self.order_number = order_number
        # personalPhoto
        self.personal_photo = personal_photo
        # personalPhotoUrl
        self.personal_photo_url = personal_photo_url
        # pinyinNameAll
        self.pinyin_name_all = pinyin_name_all
        # pinyinNick
        self.pinyin_nick_name = pinyin_nick_name
        # state
        self.state = state
        # superUserId
        self.super_user_id = super_user_id
        # tbWang
        self.tb_wang = tb_wang
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bu_name is not None:
            result['buName'] = self.bu_name
        if self.email is not None:
            result['email'] = self.email
        if self.employee_type is not None:
            result['employeeType'] = self.employee_type
        if self.employee_type_information is not None:
            result['employeeTypeInformation'] = self.employee_type_information
        if self.human_resource_group_work_number is not None:
            result['humanResourceGroupWorkNumber'] = self.human_resource_group_work_number
        if self.is_system_admin is not None:
            result['isSystemAdmin'] = self.is_system_admin
        if self.level is not None:
            result['level'] = self.level
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.order_number is not None:
            result['orderNumber'] = self.order_number
        if self.personal_photo is not None:
            result['personalPhoto'] = self.personal_photo
        if self.personal_photo_url is not None:
            result['personalPhotoUrl'] = self.personal_photo_url
        if self.pinyin_name_all is not None:
            result['pinyinNameAll'] = self.pinyin_name_all
        if self.pinyin_nick_name is not None:
            result['pinyinNickName'] = self.pinyin_nick_name
        if self.state is not None:
            result['state'] = self.state
        if self.super_user_id is not None:
            result['superUserId'] = self.super_user_id
        if self.tb_wang is not None:
            result['tbWang'] = self.tb_wang
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buName') is not None:
            self.bu_name = m.get('buName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('employeeType') is not None:
            self.employee_type = m.get('employeeType')
        if m.get('employeeTypeInformation') is not None:
            self.employee_type_information = m.get('employeeTypeInformation')
        if m.get('humanResourceGroupWorkNumber') is not None:
            self.human_resource_group_work_number = m.get('humanResourceGroupWorkNumber')
        if m.get('isSystemAdmin') is not None:
            self.is_system_admin = m.get('isSystemAdmin')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('orderNumber') is not None:
            self.order_number = m.get('orderNumber')
        if m.get('personalPhoto') is not None:
            self.personal_photo = m.get('personalPhoto')
        if m.get('personalPhotoUrl') is not None:
            self.personal_photo_url = m.get('personalPhotoUrl')
        if m.get('pinyinNameAll') is not None:
            self.pinyin_name_all = m.get('pinyinNameAll')
        if m.get('pinyinNickName') is not None:
            self.pinyin_nick_name = m.get('pinyinNickName')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('superUserId') is not None:
            self.super_user_id = m.get('superUserId')
        if m.get('tbWang') is not None:
            self.tb_wang = m.get('tbWang')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_instance_status: str = None,
        activity_name: str = None,
        activity_name_en: str = None,
        id: int = None,
    ):
        # activityId
        self.activity_id = activity_id
        # activityInstanceStatus
        self.activity_instance_status = activity_instance_status
        # activityName
        self.activity_name = activity_name
        # activityNameEn
        self.activity_name_en = activity_name_en
        # id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.activity_instance_status is not None:
            result['activityInstanceStatus'] = self.activity_instance_status
        if self.activity_name is not None:
            result['activityName'] = self.activity_name
        if self.activity_name_en is not None:
            result['activityNameEn'] = self.activity_name_en
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('activityInstanceStatus') is not None:
            self.activity_instance_status = m.get('activityInstanceStatus')
        if m.get('activityName') is not None:
            self.activity_name = m.get('activityName')
        if m.get('activityNameEn') is not None:
            self.activity_name_en = m.get('activityNameEn')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class GetMeCorpSubmissionResponseBodyData(TeaModel):
    def __init__(
        self,
        actioner: List[GetMeCorpSubmissionResponseBodyDataActioner] = None,
        actioner_id: List[str] = None,
        actioner_name: List[str] = None,
        app_type: str = None,
        create_time_gmt: str = None,
        current_activity_instances: List[GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances] = None,
        data_map: Dict[str, Any] = None,
        data_type: str = None,
        finish_time_gmt: str = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        instance_value: str = None,
        modified_time_gmt: str = None,
        originator_avatar: str = None,
        originator_display_name: str = None,
        originator_id: str = None,
        process_approved_result: str = None,
        process_approved_result_text: str = None,
        process_code: str = None,
        process_id: int = None,
        process_instance_id: str = None,
        process_instance_status: str = None,
        process_instance_status_text: str = None,
        process_name: str = None,
        title: str = None,
        version: int = None,
    ):
        # actioner
        self.actioner = actioner
        # actionerId
        self.actioner_id = actioner_id
        # actionerName
        self.actioner_name = actioner_name
        # appType
        self.app_type = app_type
        # createTime
        self.create_time_gmt = create_time_gmt
        # currentActivityInstances
        self.current_activity_instances = current_activity_instances
        # dataMap
        self.data_map = data_map
        # dataType
        self.data_type = data_type
        # finishTime
        self.finish_time_gmt = finish_time_gmt
        # formInstanceId
        self.form_instance_id = form_instance_id
        # formUuid
        self.form_uuid = form_uuid
        # instValue
        self.instance_value = instance_value
        # modifiedTime
        self.modified_time_gmt = modified_time_gmt
        # originatorAvatar
        self.originator_avatar = originator_avatar
        # originatorDisplayName
        self.originator_display_name = originator_display_name
        # originatorId
        self.originator_id = originator_id
        # processApprovedResult
        self.process_approved_result = process_approved_result
        # processApprovedResultText
        self.process_approved_result_text = process_approved_result_text
        # processCode
        self.process_code = process_code
        # processId
        self.process_id = process_id
        # processInstanceId
        self.process_instance_id = process_instance_id
        # processInstanceStatus
        self.process_instance_status = process_instance_status
        # processInstanceStatusText
        self.process_instance_status_text = process_instance_status_text
        # processName
        self.process_name = process_name
        # title
        self.title = title
        # version
        self.version = version

    def validate(self):
        if self.actioner:
            for k in self.actioner:
                if k:
                    k.validate()
        if self.current_activity_instances:
            for k in self.current_activity_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actioner'] = []
        if self.actioner is not None:
            for k in self.actioner:
                result['actioner'].append(k.to_map() if k else None)
        if self.actioner_id is not None:
            result['actionerId'] = self.actioner_id
        if self.actioner_name is not None:
            result['actionerName'] = self.actioner_name
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        result['currentActivityInstances'] = []
        if self.current_activity_instances is not None:
            for k in self.current_activity_instances:
                result['currentActivityInstances'].append(k.to_map() if k else None)
        if self.data_map is not None:
            result['dataMap'] = self.data_map
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_value is not None:
            result['instanceValue'] = self.instance_value
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.originator_avatar is not None:
            result['originatorAvatar'] = self.originator_avatar
        if self.originator_display_name is not None:
            result['originatorDisplayName'] = self.originator_display_name
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.process_approved_result is not None:
            result['processApprovedResult'] = self.process_approved_result
        if self.process_approved_result_text is not None:
            result['processApprovedResultText'] = self.process_approved_result_text
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.process_id is not None:
            result['processId'] = self.process_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.process_instance_status is not None:
            result['processInstanceStatus'] = self.process_instance_status
        if self.process_instance_status_text is not None:
            result['processInstanceStatusText'] = self.process_instance_status_text
        if self.process_name is not None:
            result['processName'] = self.process_name
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actioner = []
        if m.get('actioner') is not None:
            for k in m.get('actioner'):
                temp_model = GetMeCorpSubmissionResponseBodyDataActioner()
                self.actioner.append(temp_model.from_map(k))
        if m.get('actionerId') is not None:
            self.actioner_id = m.get('actionerId')
        if m.get('actionerName') is not None:
            self.actioner_name = m.get('actionerName')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        self.current_activity_instances = []
        if m.get('currentActivityInstances') is not None:
            for k in m.get('currentActivityInstances'):
                temp_model = GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances()
                self.current_activity_instances.append(temp_model.from_map(k))
        if m.get('dataMap') is not None:
            self.data_map = m.get('dataMap')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceValue') is not None:
            self.instance_value = m.get('instanceValue')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('originatorAvatar') is not None:
            self.originator_avatar = m.get('originatorAvatar')
        if m.get('originatorDisplayName') is not None:
            self.originator_display_name = m.get('originatorDisplayName')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('processApprovedResult') is not None:
            self.process_approved_result = m.get('processApprovedResult')
        if m.get('processApprovedResultText') is not None:
            self.process_approved_result_text = m.get('processApprovedResultText')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('processId') is not None:
            self.process_id = m.get('processId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('processInstanceStatus') is not None:
            self.process_instance_status = m.get('processInstanceStatus')
        if m.get('processInstanceStatusText') is not None:
            self.process_instance_status_text = m.get('processInstanceStatusText')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetMeCorpSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetMeCorpSubmissionResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetMeCorpSubmissionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetMeCorpSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMeCorpSubmissionResponseBody = None,
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
            temp_model = GetMeCorpSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotifyMeHeaders(TeaModel):
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


class GetNotifyMeRequest(TeaModel):
    def __init__(
        self,
        app_types: str = None,
        corp_id: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        instance_create_from_time_gmt: int = None,
        instance_create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        token: str = None,
    ):
        # 应用标识列表
        self.app_types = app_types
        # 企业ID
        self.corp_id = corp_id
        # 抄送到达时间开始
        self.create_from_time_gmt = create_from_time_gmt
        # 抄送到达时间结束
        self.create_to_time_gmt = create_to_time_gmt
        # 数据提交时间开始
        self.instance_create_from_time_gmt = instance_create_from_time_gmt
        # 数据提交时间结束
        self.instance_create_to_time_gmt = instance_create_to_time_gmt
        # 表单中组件数据模糊搜
        self.keyword = keyword
        # 语言环境
        self.language = language
        # 当前页
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 流程code列表
        self.process_codes = process_codes
        # 验权token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_types is not None:
            result['appTypes'] = self.app_types
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.instance_create_from_time_gmt is not None:
            result['instanceCreateFromTimeGMT'] = self.instance_create_from_time_gmt
        if self.instance_create_to_time_gmt is not None:
            result['instanceCreateToTimeGMT'] = self.instance_create_to_time_gmt
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_codes is not None:
            result['processCodes'] = self.process_codes
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appTypes') is not None:
            self.app_types = m.get('appTypes')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('instanceCreateFromTimeGMT') is not None:
            self.instance_create_from_time_gmt = m.get('instanceCreateFromTimeGMT')
        if m.get('instanceCreateToTimeGMT') is not None:
            self.instance_create_to_time_gmt = m.get('instanceCreateToTimeGMT')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processCodes') is not None:
            self.process_codes = m.get('processCodes')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetNotifyMeResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        app_type: str = None,
        corp_id: str = None,
        create_time_gmt: str = None,
        creator_user_id: str = None,
        form_instance_id: str = None,
        inst_status: str = None,
        mobile_url: str = None,
        modified_time_gmt: str = None,
        process_code: str = None,
        title: str = None,
        title_in_english: str = None,
        url: str = None,
    ):
        # activityId
        self.activity_id = activity_id
        # appType
        self.app_type = app_type
        # corpId
        self.corp_id = corp_id
        # 创建时间
        self.create_time_gmt = create_time_gmt
        # 创建者的userId
        self.creator_user_id = creator_user_id
        # 流程实例id
        self.form_instance_id = form_instance_id
        # instStatus
        self.inst_status = inst_status
        # mobileUrl
        self.mobile_url = mobile_url
        # 修改时间
        self.modified_time_gmt = modified_time_gmt
        # processCode
        self.process_code = process_code
        # title
        self.title = title
        # titleEn
        self.title_in_english = title_in_english
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.inst_status is not None:
            result['instStatus'] = self.inst_status
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.title is not None:
            result['title'] = self.title
        if self.title_in_english is not None:
            result['titleInEnglish'] = self.title_in_english
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('instStatus') is not None:
            self.inst_status = m.get('instStatus')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('titleInEnglish') is not None:
            self.title_in_english = m.get('titleInEnglish')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetNotifyMeResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetNotifyMeResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetNotifyMeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetNotifyMeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNotifyMeResponseBody = None,
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
            temp_model = GetNotifyMeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenUrlHeaders(TeaModel):
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


class GetOpenUrlRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        language: str = None,
        system_token: str = None,
        timeout: int = None,
        user_id: str = None,
    ):
        # 宜搭附件地址
        self.file_url = file_url
        # 语言
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 临时地址多久失效,单位毫秒
        self.timeout = timeout
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetOpenUrlResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 临时免登地址url
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


class GetOpenUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpenUrlResponseBody = None,
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
            temp_model = GetOpenUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationRecordsHeaders(TeaModel):
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


class GetOperationRecordsRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言
        self.language = language
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetOperationRecordsResponseBodyResult(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_exit: str = None,
        active_time_gmt: str = None,
        activity_id: str = None,
        data_id: int = None,
        digital_sign: str = None,
        files: str = None,
        operate_time_gmt: str = None,
        operate_type: str = None,
        operator_display_name: str = None,
        operator_name: str = None,
        operator_nick_name: str = None,
        operator_photo_url: str = None,
        operator_status: str = None,
        operator_user_id: str = None,
        process_instance_id: str = None,
        remark: str = None,
        show_name: str = None,
        size: int = None,
        task_execute_type: str = None,
        task_hold_time_gmt: int = None,
        task_id: str = None,
        task_type: str = None,
        type: str = None,
    ):
        # action
        self.action = action
        # actionExt
        self.action_exit = action_exit
        # activeTime
        self.active_time_gmt = active_time_gmt
        # activityId
        self.activity_id = activity_id
        # id
        self.data_id = data_id
        # digitalSign
        self.digital_sign = digital_sign
        # files
        self.files = files
        # operateTime
        self.operate_time_gmt = operate_time_gmt
        # operateType
        self.operate_type = operate_type
        # operatorDisplayName
        self.operator_display_name = operator_display_name
        # operatorName
        self.operator_name = operator_name
        # operatorNick
        self.operator_nick_name = operator_nick_name
        # operatorPhotoUrl
        self.operator_photo_url = operator_photo_url
        # operatorStatus
        self.operator_status = operator_status
        # operator
        self.operator_user_id = operator_user_id
        # processInstanceId
        self.process_instance_id = process_instance_id
        # remark
        self.remark = remark
        # showName
        self.show_name = show_name
        # size
        self.size = size
        # taskExecuteType
        self.task_execute_type = task_execute_type
        # taskHoldTime
        self.task_hold_time_gmt = task_hold_time_gmt
        # taskId
        self.task_id = task_id
        # taskType
        self.task_type = task_type
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.action_exit is not None:
            result['actionExit'] = self.action_exit
        if self.active_time_gmt is not None:
            result['activeTimeGMT'] = self.active_time_gmt
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.data_id is not None:
            result['dataId'] = self.data_id
        if self.digital_sign is not None:
            result['digitalSign'] = self.digital_sign
        if self.files is not None:
            result['files'] = self.files
        if self.operate_time_gmt is not None:
            result['operateTimeGMT'] = self.operate_time_gmt
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.operator_display_name is not None:
            result['operatorDisplayName'] = self.operator_display_name
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.operator_nick_name is not None:
            result['operatorNickName'] = self.operator_nick_name
        if self.operator_photo_url is not None:
            result['operatorPhotoUrl'] = self.operator_photo_url
        if self.operator_status is not None:
            result['operatorStatus'] = self.operator_status
        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.show_name is not None:
            result['showName'] = self.show_name
        if self.size is not None:
            result['size'] = self.size
        if self.task_execute_type is not None:
            result['taskExecuteType'] = self.task_execute_type
        if self.task_hold_time_gmt is not None:
            result['taskHoldTimeGMT'] = self.task_hold_time_gmt
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('actionExit') is not None:
            self.action_exit = m.get('actionExit')
        if m.get('activeTimeGMT') is not None:
            self.active_time_gmt = m.get('activeTimeGMT')
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        if m.get('digitalSign') is not None:
            self.digital_sign = m.get('digitalSign')
        if m.get('files') is not None:
            self.files = m.get('files')
        if m.get('operateTimeGMT') is not None:
            self.operate_time_gmt = m.get('operateTimeGMT')
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('operatorDisplayName') is not None:
            self.operator_display_name = m.get('operatorDisplayName')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('operatorNickName') is not None:
            self.operator_nick_name = m.get('operatorNickName')
        if m.get('operatorPhotoUrl') is not None:
            self.operator_photo_url = m.get('operatorPhotoUrl')
        if m.get('operatorStatus') is not None:
            self.operator_status = m.get('operatorStatus')
        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('showName') is not None:
            self.show_name = m.get('showName')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('taskExecuteType') is not None:
            self.task_execute_type = m.get('taskExecuteType')
        if m.get('taskHoldTimeGMT') is not None:
            self.task_hold_time_gmt = m.get('taskHoldTimeGMT')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetOperationRecordsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetOperationRecordsResponseBodyResult] = None,
    ):
        # 流程实例操作记录数组
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
                temp_model = GetOperationRecordsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetOperationRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOperationRecordsResponseBody = None,
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
            temp_model = GetOperationRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPlatformResourceHeaders(TeaModel):
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


class GetPlatformResourceRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class GetPlatformResourceResponseBody(TeaModel):
    def __init__(
        self,
        account_total_amount: int = None,
        account_usage_amount: int = None,
        app_total_amount: int = None,
        attachment_total_amount: int = None,
        attachment_usage_amount: int = None,
        instance_total_amount: int = None,
        instance_usage_amount: int = None,
        plugin_usage_amount: int = None,
    ):
        # accountTotalAmount
        self.account_total_amount = account_total_amount
        # accountUsageAmount
        self.account_usage_amount = account_usage_amount
        # appTotalAmount
        self.app_total_amount = app_total_amount
        # attachmentTotalAmount
        self.attachment_total_amount = attachment_total_amount
        # attachmentUsageAmount
        self.attachment_usage_amount = attachment_usage_amount
        # instanceTotalAmount
        self.instance_total_amount = instance_total_amount
        # instanceUsageAmount
        self.instance_usage_amount = instance_usage_amount
        # pluginUsageAmount
        self.plugin_usage_amount = plugin_usage_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_total_amount is not None:
            result['accountTotalAmount'] = self.account_total_amount
        if self.account_usage_amount is not None:
            result['accountUsageAmount'] = self.account_usage_amount
        if self.app_total_amount is not None:
            result['appTotalAmount'] = self.app_total_amount
        if self.attachment_total_amount is not None:
            result['attachmentTotalAmount'] = self.attachment_total_amount
        if self.attachment_usage_amount is not None:
            result['attachmentUsageAmount'] = self.attachment_usage_amount
        if self.instance_total_amount is not None:
            result['instanceTotalAmount'] = self.instance_total_amount
        if self.instance_usage_amount is not None:
            result['instanceUsageAmount'] = self.instance_usage_amount
        if self.plugin_usage_amount is not None:
            result['pluginUsageAmount'] = self.plugin_usage_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountTotalAmount') is not None:
            self.account_total_amount = m.get('accountTotalAmount')
        if m.get('accountUsageAmount') is not None:
            self.account_usage_amount = m.get('accountUsageAmount')
        if m.get('appTotalAmount') is not None:
            self.app_total_amount = m.get('appTotalAmount')
        if m.get('attachmentTotalAmount') is not None:
            self.attachment_total_amount = m.get('attachmentTotalAmount')
        if m.get('attachmentUsageAmount') is not None:
            self.attachment_usage_amount = m.get('attachmentUsageAmount')
        if m.get('instanceTotalAmount') is not None:
            self.instance_total_amount = m.get('instanceTotalAmount')
        if m.get('instanceUsageAmount') is not None:
            self.instance_usage_amount = m.get('instanceUsageAmount')
        if m.get('pluginUsageAmount') is not None:
            self.plugin_usage_amount = m.get('pluginUsageAmount')
        return self


class GetPlatformResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPlatformResourceResponseBody = None,
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
            temp_model = GetPlatformResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrintAppInfoHeaders(TeaModel):
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


class GetPrintAppInfoRequest(TeaModel):
    def __init__(
        self,
        name_like: str = None,
        user_id: str = None,
    ):
        # 搜索关键字
        self.name_like = name_like
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetPrintAppInfoResponseBodyResultFormInfoList(TeaModel):
    def __init__(
        self,
        form_name: str = None,
        form_uuid: str = None,
    ):
        # formName
        self.form_name = form_name
        # formUuid
        self.form_uuid = form_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_name is not None:
            result['formName'] = self.form_name
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formName') is not None:
            self.form_name = m.get('formName')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        return self


class GetPrintAppInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        form_info_list: List[GetPrintAppInfoResponseBodyResultFormInfoList] = None,
        icon_url: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # appType
        self.app_type = app_type
        # formInfoList
        self.form_info_list = form_info_list
        # 图标链接
        self.icon_url = icon_url

    def validate(self):
        if self.form_info_list:
            for k in self.form_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_type is not None:
            result['appType'] = self.app_type
        result['formInfoList'] = []
        if self.form_info_list is not None:
            for k in self.form_info_list:
                result['formInfoList'].append(k.to_map() if k else None)
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        self.form_info_list = []
        if m.get('formInfoList') is not None:
            for k in m.get('formInfoList'):
                temp_model = GetPrintAppInfoResponseBodyResultFormInfoList()
                self.form_info_list.append(temp_model.from_map(k))
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        return self


class GetPrintAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetPrintAppInfoResponseBodyResult] = None,
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
                temp_model = GetPrintAppInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetPrintAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPrintAppInfoResponseBody = None,
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
            temp_model = GetPrintAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrintDictionaryHeaders(TeaModel):
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


class GetPrintDictionaryRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_uuid: str = None,
        user_id: str = None,
        version: int = None,
    ):
        # 应用代码
        self.app_type = app_type
        # 表单id
        self.form_uuid = form_uuid
        # 用户id
        self.user_id = user_id
        # 版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetPrintDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
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


class GetPrintDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPrintDictionaryResponseBody = None,
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
            temp_model = GetPrintDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProcessDefinitionHeaders(TeaModel):
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


class GetProcessDefinitionRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        corp_id: str = None,
        group_id: str = None,
        language: str = None,
        name_space: str = None,
        order_number: str = None,
        system_token: str = None,
        system_type: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.corp_id = corp_id
        self.group_id = group_id
        self.language = language
        self.name_space = name_space
        self.order_number = order_number
        self.system_token = system_token
        self.system_type = system_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.language is not None:
            result['language'] = self.language
        if self.name_space is not None:
            result['nameSpace'] = self.name_space
        if self.order_number is not None:
            result['orderNumber'] = self.order_number
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.system_type is not None:
            result['systemType'] = self.system_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('nameSpace') is not None:
            self.name_space = m.get('nameSpace')
        if m.get('orderNumber') is not None:
            self.order_number = m.get('orderNumber')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('systemType') is not None:
            self.system_type = m.get('systemType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        dept_name_in_english: str = None,
        dept_no: str = None,
        dept_path: str = None,
        human_source_group_order_number: str = None,
        human_source_group_work_no: str = None,
        id: int = None,
        master_work_no: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # deptNameEn
        self.dept_name_in_english = dept_name_in_english
        # deptNo
        self.dept_no = dept_no
        # deptPath
        self.dept_path = dept_path
        # humanSourceGroupOrderNum
        self.human_source_group_order_number = human_source_group_order_number
        # humanSourceGroupWorkNo
        self.human_source_group_work_no = human_source_group_work_no
        # id
        self.id = id
        # masterWorkNo
        self.master_work_no = master_work_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.dept_name_in_english is not None:
            result['deptNameInEnglish'] = self.dept_name_in_english
        if self.dept_no is not None:
            result['deptNo'] = self.dept_no
        if self.dept_path is not None:
            result['deptPath'] = self.dept_path
        if self.human_source_group_order_number is not None:
            result['humanSourceGroupOrderNumber'] = self.human_source_group_order_number
        if self.human_source_group_work_no is not None:
            result['humanSourceGroupWorkNo'] = self.human_source_group_work_no
        if self.id is not None:
            result['id'] = self.id
        if self.master_work_no is not None:
            result['masterWorkNo'] = self.master_work_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('deptNameInEnglish') is not None:
            self.dept_name_in_english = m.get('deptNameInEnglish')
        if m.get('deptNo') is not None:
            self.dept_no = m.get('deptNo')
        if m.get('deptPath') is not None:
            self.dept_path = m.get('deptPath')
        if m.get('humanSourceGroupOrderNumber') is not None:
            self.human_source_group_order_number = m.get('humanSourceGroupOrderNumber')
        if m.get('humanSourceGroupWorkNo') is not None:
            self.human_source_group_work_no = m.get('humanSourceGroupWorkNo')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('masterWorkNo') is not None:
            self.master_work_no = m.get('masterWorkNo')
        return self


class GetProcessDefinitionResponseBodyOriginator(TeaModel):
    def __init__(
        self,
        department_description: str = None,
        display_en_name: str = None,
        display_name: str = None,
        master_data_departments: List[GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments] = None,
        order_number: str = None,
        personal_photo: str = None,
        status: str = None,
        tb_wang: str = None,
        user_id: str = None,
        user_info: str = None,
    ):
        # departmentDescription
        self.department_description = department_description
        # displayEnName
        self.display_en_name = display_en_name
        # displayName
        self.display_name = display_name
        # masterDataDepartments
        self.master_data_departments = master_data_departments
        # orderNum
        self.order_number = order_number
        # personalPhoto
        self.personal_photo = personal_photo
        # status
        self.status = status
        # tbWang
        self.tb_wang = tb_wang
        # userId
        self.user_id = user_id
        # userInfo
        self.user_info = user_info

    def validate(self):
        if self.master_data_departments:
            for k in self.master_data_departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_description is not None:
            result['departmentDescription'] = self.department_description
        if self.display_en_name is not None:
            result['displayEnName'] = self.display_en_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        result['masterDataDepartments'] = []
        if self.master_data_departments is not None:
            for k in self.master_data_departments:
                result['masterDataDepartments'].append(k.to_map() if k else None)
        if self.order_number is not None:
            result['orderNumber'] = self.order_number
        if self.personal_photo is not None:
            result['personalPhoto'] = self.personal_photo
        if self.status is not None:
            result['status'] = self.status
        if self.tb_wang is not None:
            result['tbWang'] = self.tb_wang
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_info is not None:
            result['userInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentDescription') is not None:
            self.department_description = m.get('departmentDescription')
        if m.get('displayEnName') is not None:
            self.display_en_name = m.get('displayEnName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        self.master_data_departments = []
        if m.get('masterDataDepartments') is not None:
            for k in m.get('masterDataDepartments'):
                temp_model = GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments()
                self.master_data_departments.append(temp_model.from_map(k))
        if m.get('orderNumber') is not None:
            self.order_number = m.get('orderNumber')
        if m.get('personalPhoto') is not None:
            self.personal_photo = m.get('personalPhoto')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tbWang') is not None:
            self.tb_wang = m.get('tbWang')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userInfo') is not None:
            self.user_info = m.get('userInfo')
        return self


class GetProcessDefinitionResponseBodyOwnersMasterDataDepartments(TeaModel):
    def __init__(
        self,
        dept_name: str = None,
        dept_name_in_english: str = None,
        dept_no: str = None,
        dept_path: str = None,
        human_source_group_order_number: str = None,
        human_source_group_work_no: str = None,
        id: int = None,
        master_work_no: str = None,
    ):
        # deptName
        self.dept_name = dept_name
        # deptNameEn
        self.dept_name_in_english = dept_name_in_english
        # deptNo
        self.dept_no = dept_no
        # deptPath
        self.dept_path = dept_path
        # humanSourceGroupOrderNum
        self.human_source_group_order_number = human_source_group_order_number
        # humanSourceGroupWorkNo
        self.human_source_group_work_no = human_source_group_work_no
        # id
        self.id = id
        # masterWorkNo
        self.master_work_no = master_work_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.dept_name_in_english is not None:
            result['deptNameInEnglish'] = self.dept_name_in_english
        if self.dept_no is not None:
            result['deptNo'] = self.dept_no
        if self.dept_path is not None:
            result['deptPath'] = self.dept_path
        if self.human_source_group_order_number is not None:
            result['humanSourceGroupOrderNumber'] = self.human_source_group_order_number
        if self.human_source_group_work_no is not None:
            result['humanSourceGroupWorkNo'] = self.human_source_group_work_no
        if self.id is not None:
            result['id'] = self.id
        if self.master_work_no is not None:
            result['masterWorkNo'] = self.master_work_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('deptNameInEnglish') is not None:
            self.dept_name_in_english = m.get('deptNameInEnglish')
        if m.get('deptNo') is not None:
            self.dept_no = m.get('deptNo')
        if m.get('deptPath') is not None:
            self.dept_path = m.get('deptPath')
        if m.get('humanSourceGroupOrderNumber') is not None:
            self.human_source_group_order_number = m.get('humanSourceGroupOrderNumber')
        if m.get('humanSourceGroupWorkNo') is not None:
            self.human_source_group_work_no = m.get('humanSourceGroupWorkNo')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('masterWorkNo') is not None:
            self.master_work_no = m.get('masterWorkNo')
        return self


class GetProcessDefinitionResponseBodyOwners(TeaModel):
    def __init__(
        self,
        department_description: str = None,
        display_en_name: str = None,
        display_name: str = None,
        master_data_departments: List[GetProcessDefinitionResponseBodyOwnersMasterDataDepartments] = None,
        order_number: str = None,
        personal_photo: str = None,
        status: str = None,
        tb_wang: str = None,
        user_id: str = None,
        user_info: str = None,
    ):
        # departmentDescription
        self.department_description = department_description
        # displayEnName
        self.display_en_name = display_en_name
        # displayName
        self.display_name = display_name
        # masterDataDepartments
        self.master_data_departments = master_data_departments
        # orderNum
        self.order_number = order_number
        # personalPhoto
        self.personal_photo = personal_photo
        # status
        self.status = status
        # tbWang
        self.tb_wang = tb_wang
        # userId
        self.user_id = user_id
        # userInfo
        self.user_info = user_info

    def validate(self):
        if self.master_data_departments:
            for k in self.master_data_departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_description is not None:
            result['departmentDescription'] = self.department_description
        if self.display_en_name is not None:
            result['displayEnName'] = self.display_en_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        result['masterDataDepartments'] = []
        if self.master_data_departments is not None:
            for k in self.master_data_departments:
                result['masterDataDepartments'].append(k.to_map() if k else None)
        if self.order_number is not None:
            result['orderNumber'] = self.order_number
        if self.personal_photo is not None:
            result['personalPhoto'] = self.personal_photo
        if self.status is not None:
            result['status'] = self.status
        if self.tb_wang is not None:
            result['tbWang'] = self.tb_wang
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_info is not None:
            result['userInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentDescription') is not None:
            self.department_description = m.get('departmentDescription')
        if m.get('displayEnName') is not None:
            self.display_en_name = m.get('displayEnName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        self.master_data_departments = []
        if m.get('masterDataDepartments') is not None:
            for k in m.get('masterDataDepartments'):
                temp_model = GetProcessDefinitionResponseBodyOwnersMasterDataDepartments()
                self.master_data_departments.append(temp_model.from_map(k))
        if m.get('orderNumber') is not None:
            self.order_number = m.get('orderNumber')
        if m.get('personalPhoto') is not None:
            self.personal_photo = m.get('personalPhoto')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tbWang') is not None:
            self.tb_wang = m.get('tbWang')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userInfo') is not None:
            self.user_info = m.get('userInfo')
        return self


class GetProcessDefinitionResponseBodyTasksActivity(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_instance_status: str = None,
        activity_name: str = None,
        activity_name_in_english: str = None,
        id: int = None,
    ):
        # activityId
        self.activity_id = activity_id
        # activityInstanceStatus
        self.activity_instance_status = activity_instance_status
        # activityName
        self.activity_name = activity_name
        # activityNameEn
        self.activity_name_in_english = activity_name_in_english
        # id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.activity_instance_status is not None:
            result['activityInstanceStatus'] = self.activity_instance_status
        if self.activity_name is not None:
            result['activityName'] = self.activity_name
        if self.activity_name_in_english is not None:
            result['activityNameInEnglish'] = self.activity_name_in_english
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('activityInstanceStatus') is not None:
            self.activity_instance_status = m.get('activityInstanceStatus')
        if m.get('activityName') is not None:
            self.activity_name = m.get('activityName')
        if m.get('activityNameInEnglish') is not None:
            self.activity_name_in_english = m.get('activityNameInEnglish')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class GetProcessDefinitionResponseBodyTasks(TeaModel):
    def __init__(
        self,
        actioner_id: str = None,
        activity: GetProcessDefinitionResponseBodyTasksActivity = None,
        status: str = None,
        task_id: int = None,
    ):
        # actioner
        self.actioner_id = actioner_id
        # activity
        self.activity = activity
        # status
        self.status = status
        # taskId
        self.task_id = task_id

    def validate(self):
        if self.activity:
            self.activity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actioner_id is not None:
            result['actionerId'] = self.actioner_id
        if self.activity is not None:
            result['activity'] = self.activity.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionerId') is not None:
            self.actioner_id = m.get('actionerId')
        if m.get('activity') is not None:
            temp_model = GetProcessDefinitionResponseBodyTasksActivity()
            self.activity = temp_model.from_map(m['activity'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetProcessDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        form_uuid: str = None,
        originator: GetProcessDefinitionResponseBodyOriginator = None,
        out_result: str = None,
        owners: List[GetProcessDefinitionResponseBodyOwners] = None,
        process_id: str = None,
        process_instance_id: str = None,
        status: str = None,
        tasks: List[GetProcessDefinitionResponseBodyTasks] = None,
        title: str = None,
        variables: Dict[str, Any] = None,
    ):
        # formUuid
        self.form_uuid = form_uuid
        # originator
        self.originator = originator
        # outResult
        self.out_result = out_result
        # owners
        self.owners = owners
        # processId
        self.process_id = process_id
        # processInstanceId
        self.process_instance_id = process_instance_id
        # status
        self.status = status
        # tasks
        self.tasks = tasks
        # title
        self.title = title
        # variables
        self.variables = variables

    def validate(self):
        if self.originator:
            self.originator.validate()
        if self.owners:
            for k in self.owners:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.out_result is not None:
            result['outResult'] = self.out_result
        result['owners'] = []
        if self.owners is not None:
            for k in self.owners:
                result['owners'].append(k.to_map() if k else None)
        if self.process_id is not None:
            result['processId'] = self.process_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.status is not None:
            result['status'] = self.status
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.title is not None:
            result['title'] = self.title
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('originator') is not None:
            temp_model = GetProcessDefinitionResponseBodyOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        self.owners = []
        if m.get('owners') is not None:
            for k in m.get('owners'):
                temp_model = GetProcessDefinitionResponseBodyOwners()
                self.owners.append(temp_model.from_map(k))
        if m.get('processId') is not None:
            self.process_id = m.get('processId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = GetProcessDefinitionResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class GetProcessDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProcessDefinitionResponseBody = None,
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
            temp_model = GetProcessDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningTaskListHeaders(TeaModel):
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


class GetRunningTaskListRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        process_instance_id_list: str = None,
        system_token: str = None,
        user_corp_id: str = None,
        user_id: str = None,
    ):
        # appType
        self.app_type = app_type
        # 流程实例id列表, 逗号分隔
        self.process_instance_id_list = process_instance_id_list
        # systemToken
        self.system_token = system_token
        # 用户所属的企业id
        self.user_corp_id = user_corp_id
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.process_instance_id_list is not None:
            result['processInstanceIdList'] = self.process_instance_id_list
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_corp_id is not None:
            result['userCorpId'] = self.user_corp_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('processInstanceIdList') is not None:
            self.process_instance_id_list = m.get('processInstanceIdList')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userCorpId') is not None:
            self.user_corp_id = m.get('userCorpId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetRunningTaskListResponseBodyResult(TeaModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        actual_action_executor_id: str = None,
        app_type: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_email: str = None,
        originator_id: str = None,
        originator_name: str = None,
        originator_name_in_english: str = None,
        originator_nick_name: str = None,
        originator_nick_name_in_english: str = None,
        originator_photo: str = None,
        out_result: str = None,
        out_result_name: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        # 激活时间
        self.active_time_gmt = active_time_gmt
        # 实际执行人id
        self.actual_action_executor_id = actual_action_executor_id
        # appType
        self.app_type = app_type
        # 创建时间
        self.create_time_gmt = create_time_gmt
        # 结束时间
        self.finish_time_gmt = finish_time_gmt
        # originatorEmail
        self.originator_email = originator_email
        # originatorId
        self.originator_id = originator_id
        # originatorName
        self.originator_name = originator_name
        # originatorNameEn
        self.originator_name_in_english = originator_name_in_english
        # originatorNickName
        self.originator_nick_name = originator_nick_name
        # originatorNickNameEn
        self.originator_nick_name_in_english = originator_nick_name_in_english
        # originatorPhoto
        self.originator_photo = originator_photo
        # outResult
        self.out_result = out_result
        # outResultName
        self.out_result_name = out_result_name
        # processInstanceId
        self.process_instance_id = process_instance_id
        # 状态
        self.status = status
        # 任务id
        self.task_id = task_id
        # 任务类型
        self.task_type = task_type
        # 标题
        self.title = title
        # 标题英文
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_gmt is not None:
            result['activeTimeGMT'] = self.active_time_gmt
        if self.actual_action_executor_id is not None:
            result['actualActionExecutorId'] = self.actual_action_executor_id
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.originator_email is not None:
            result['originatorEmail'] = self.originator_email
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.originator_name is not None:
            result['originatorName'] = self.originator_name
        if self.originator_name_in_english is not None:
            result['originatorNameInEnglish'] = self.originator_name_in_english
        if self.originator_nick_name is not None:
            result['originatorNickName'] = self.originator_nick_name
        if self.originator_nick_name_in_english is not None:
            result['originatorNickNameInEnglish'] = self.originator_nick_name_in_english
        if self.originator_photo is not None:
            result['originatorPhoto'] = self.originator_photo
        if self.out_result is not None:
            result['outResult'] = self.out_result
        if self.out_result_name is not None:
            result['outResultName'] = self.out_result_name
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.title is not None:
            result['title'] = self.title
        if self.title_in_english is not None:
            result['titleInEnglish'] = self.title_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTimeGMT') is not None:
            self.active_time_gmt = m.get('activeTimeGMT')
        if m.get('actualActionExecutorId') is not None:
            self.actual_action_executor_id = m.get('actualActionExecutorId')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('originatorEmail') is not None:
            self.originator_email = m.get('originatorEmail')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('originatorName') is not None:
            self.originator_name = m.get('originatorName')
        if m.get('originatorNameInEnglish') is not None:
            self.originator_name_in_english = m.get('originatorNameInEnglish')
        if m.get('originatorNickName') is not None:
            self.originator_nick_name = m.get('originatorNickName')
        if m.get('originatorNickNameInEnglish') is not None:
            self.originator_nick_name_in_english = m.get('originatorNickNameInEnglish')
        if m.get('originatorPhoto') is not None:
            self.originator_photo = m.get('originatorPhoto')
        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')
        if m.get('outResultName') is not None:
            self.out_result_name = m.get('outResultName')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('titleInEnglish') is not None:
            self.title_in_english = m.get('titleInEnglish')
        return self


class GetRunningTaskListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetRunningTaskListResponseBodyResult] = None,
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
                temp_model = GetRunningTaskListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetRunningTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunningTaskListResponseBody = None,
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
            temp_model = GetRunningTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningTasksHeaders(TeaModel):
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


class GetRunningTasksRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.language = language
        self.process_instance_id = process_instance_id
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetRunningTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        activity_id: str = None,
        actual_actioner_id: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_id: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        # activeTime
        self.active_time_gmt = active_time_gmt
        # activityId
        self.activity_id = activity_id
        # actualActionerId
        self.actual_actioner_id = actual_actioner_id
        # createTime
        self.create_time_gmt = create_time_gmt
        # finishTime
        self.finish_time_gmt = finish_time_gmt
        # originatorId
        self.originator_id = originator_id
        # processInstanceId
        self.process_instance_id = process_instance_id
        # status
        self.status = status
        # taskId
        self.task_id = task_id
        # taskType
        self.task_type = task_type
        # title
        self.title = title
        # titleEn
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_gmt is not None:
            result['activeTimeGMT'] = self.active_time_gmt
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.actual_actioner_id is not None:
            result['actualActionerId'] = self.actual_actioner_id
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.title is not None:
            result['title'] = self.title
        if self.title_in_english is not None:
            result['titleInEnglish'] = self.title_in_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTimeGMT') is not None:
            self.active_time_gmt = m.get('activeTimeGMT')
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('actualActionerId') is not None:
            self.actual_actioner_id = m.get('actualActionerId')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('titleInEnglish') is not None:
            self.title_in_english = m.get('titleInEnglish')
        return self


class GetRunningTasksResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetRunningTasksResponseBodyResult] = None,
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
                temp_model = GetRunningTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetRunningTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunningTasksResponseBody = None,
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
            temp_model = GetRunningTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaleUserInfoByUserIdHeaders(TeaModel):
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


class GetSaleUserInfoByUserIdRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        namespace: str = None,
        user_id: str = None,
    ):
        self.corp_id = corp_id
        self.namespace = namespace
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetSaleUserInfoByUserIdResponseBodyCorpList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        namespace: str = None,
    ):
        # corpId
        self.corp_id = corp_id
        # corpName
        self.corp_name = corp_name
        # namespace
        self.namespace = namespace

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
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class GetSaleUserInfoByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        corp_list: List[GetSaleUserInfoByUserIdResponseBodyCorpList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # accountId
        self.account_id = account_id
        # corpList
        self.corp_list = corp_list
        # userId
        self.user_id = user_id
        # userName
        self.user_name = user_name

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
        if self.account_id is not None:
            result['accountId'] = self.account_id
        result['corpList'] = []
        if self.corp_list is not None:
            for k in self.corp_list:
                result['corpList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        self.corp_list = []
        if m.get('corpList') is not None:
            for k in m.get('corpList'):
                temp_model = GetSaleUserInfoByUserIdResponseBodyCorpList()
                self.corp_list.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetSaleUserInfoByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSaleUserInfoByUserIdResponseBody = None,
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
            temp_model = GetSaleUserInfoByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskCopiesHeaders(TeaModel):
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


class GetTaskCopiesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: int = None,
        create_to_time_gmt: int = None,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        process_codes: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 创建时间开始; 时间戳
        self.create_from_time_gmt = create_from_time_gmt
        # 创建时间结束; 时间戳
        self.create_to_time_gmt = create_to_time_gmt
        # 关键词
        self.keyword = keyword
        # 语言环境; 可选值：zh_CN/en_US
        self.language = language
        # 当前页; 必须大于0 默认1
        self.page_number = page_number
        # 每页记录数; 必须大于0 默认10 最大值：100
        self.page_size = page_size
        # 流程code列表
        self.process_codes = process_codes
        # 验权token
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.language is not None:
            result['language'] = self.language
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_codes is not None:
            result['processCodes'] = self.process_codes
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processCodes') is not None:
            self.process_codes = m.get('processCodes')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetTaskCopiesResponseBodyDataCurrentActivityInstances(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_instance_status: str = None,
        activity_name: str = None,
        activity_name_in_english: str = None,
        id: int = None,
    ):
        # 节点id
        self.activity_id = activity_id
        # 节点实例状态
        self.activity_instance_status = activity_instance_status
        # 节点名称
        self.activity_name = activity_name
        # 节点英文名称
        self.activity_name_in_english = activity_name_in_english
        # 数据id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.activity_instance_status is not None:
            result['activityInstanceStatus'] = self.activity_instance_status
        if self.activity_name is not None:
            result['activityName'] = self.activity_name
        if self.activity_name_in_english is not None:
            result['activityNameInEnglish'] = self.activity_name_in_english
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('activityInstanceStatus') is not None:
            self.activity_instance_status = m.get('activityInstanceStatus')
        if m.get('activityName') is not None:
            self.activity_name = m.get('activityName')
        if m.get('activityNameInEnglish') is not None:
            self.activity_name_in_english = m.get('activityNameInEnglish')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class GetTaskCopiesResponseBodyData(TeaModel):
    def __init__(
        self,
        action_executor_id: List[str] = None,
        action_executor_name: List[str] = None,
        app_type: str = None,
        carbon_activity_id: str = None,
        create_time_gmt: str = None,
        current_activity_instances: List[GetTaskCopiesResponseBodyDataCurrentActivityInstances] = None,
        data_map: Dict[str, Any] = None,
        data_type: str = None,
        finish_time_gmt: str = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        instance_value: str = None,
        modified_time_gmt: str = None,
        originator_avatar: str = None,
        originator_display_name: str = None,
        originator_id: str = None,
        process_approved_result: str = None,
        process_approved_result_text: str = None,
        process_code: str = None,
        process_id: int = None,
        process_instance_id: str = None,
        process_instance_status: str = None,
        process_instance_status_text: str = None,
        process_name: str = None,
        serial_number: str = None,
        title: str = None,
        version: int = None,
    ):
        # actionerId
        self.action_executor_id = action_executor_id
        # actionerName
        self.action_executor_name = action_executor_name
        # appType
        self.app_type = app_type
        # carbonActivityId
        self.carbon_activity_id = carbon_activity_id
        # 创建时间
        self.create_time_gmt = create_time_gmt
        # currentActivityInstances
        self.current_activity_instances = current_activity_instances
        # dataMap
        self.data_map = data_map
        # dataType
        self.data_type = data_type
        # 结束时间
        self.finish_time_gmt = finish_time_gmt
        # formInstanceId
        self.form_instance_id = form_instance_id
        # formUuid
        self.form_uuid = form_uuid
        # 实例数据
        self.instance_value = instance_value
        # modifiedTime
        self.modified_time_gmt = modified_time_gmt
        # originatorAvatar
        self.originator_avatar = originator_avatar
        # originatorDisplayName
        self.originator_display_name = originator_display_name
        # originatorId
        self.originator_id = originator_id
        # processApprovedResult
        self.process_approved_result = process_approved_result
        # processApprovedResultText
        self.process_approved_result_text = process_approved_result_text
        # processCode
        self.process_code = process_code
        # 流程id
        self.process_id = process_id
        # processInstanceId
        self.process_instance_id = process_instance_id
        # processInstanceStatus
        self.process_instance_status = process_instance_status
        # processInstanceStatusText
        self.process_instance_status_text = process_instance_status_text
        # processName
        self.process_name = process_name
        # 序列号
        self.serial_number = serial_number
        # 标题
        self.title = title
        # 版本
        self.version = version

    def validate(self):
        if self.current_activity_instances:
            for k in self.current_activity_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_executor_id is not None:
            result['actionExecutorId'] = self.action_executor_id
        if self.action_executor_name is not None:
            result['actionExecutorName'] = self.action_executor_name
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.carbon_activity_id is not None:
            result['carbonActivityId'] = self.carbon_activity_id
        if self.create_time_gmt is not None:
            result['createTimeGMT'] = self.create_time_gmt
        result['currentActivityInstances'] = []
        if self.current_activity_instances is not None:
            for k in self.current_activity_instances:
                result['currentActivityInstances'].append(k.to_map() if k else None)
        if self.data_map is not None:
            result['dataMap'] = self.data_map
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.finish_time_gmt is not None:
            result['finishTimeGMT'] = self.finish_time_gmt
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_value is not None:
            result['instanceValue'] = self.instance_value
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.originator_avatar is not None:
            result['originatorAvatar'] = self.originator_avatar
        if self.originator_display_name is not None:
            result['originatorDisplayName'] = self.originator_display_name
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.process_approved_result is not None:
            result['processApprovedResult'] = self.process_approved_result
        if self.process_approved_result_text is not None:
            result['processApprovedResultText'] = self.process_approved_result_text
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.process_id is not None:
            result['processId'] = self.process_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.process_instance_status is not None:
            result['processInstanceStatus'] = self.process_instance_status
        if self.process_instance_status_text is not None:
            result['processInstanceStatusText'] = self.process_instance_status_text
        if self.process_name is not None:
            result['processName'] = self.process_name
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionExecutorId') is not None:
            self.action_executor_id = m.get('actionExecutorId')
        if m.get('actionExecutorName') is not None:
            self.action_executor_name = m.get('actionExecutorName')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('carbonActivityId') is not None:
            self.carbon_activity_id = m.get('carbonActivityId')
        if m.get('createTimeGMT') is not None:
            self.create_time_gmt = m.get('createTimeGMT')
        self.current_activity_instances = []
        if m.get('currentActivityInstances') is not None:
            for k in m.get('currentActivityInstances'):
                temp_model = GetTaskCopiesResponseBodyDataCurrentActivityInstances()
                self.current_activity_instances.append(temp_model.from_map(k))
        if m.get('dataMap') is not None:
            self.data_map = m.get('dataMap')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('finishTimeGMT') is not None:
            self.finish_time_gmt = m.get('finishTimeGMT')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceValue') is not None:
            self.instance_value = m.get('instanceValue')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('originatorAvatar') is not None:
            self.originator_avatar = m.get('originatorAvatar')
        if m.get('originatorDisplayName') is not None:
            self.originator_display_name = m.get('originatorDisplayName')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('processApprovedResult') is not None:
            self.process_approved_result = m.get('processApprovedResult')
        if m.get('processApprovedResultText') is not None:
            self.process_approved_result_text = m.get('processApprovedResultText')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('processId') is not None:
            self.process_id = m.get('processId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('processInstanceStatus') is not None:
            self.process_instance_status = m.get('processInstanceStatus')
        if m.get('processInstanceStatusText') is not None:
            self.process_instance_status_text = m.get('processInstanceStatusText')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetTaskCopiesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetTaskCopiesResponseBodyData] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # 数据
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetTaskCopiesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetTaskCopiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskCopiesResponseBody = None,
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
            temp_model = GetTaskCopiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationAuthorizationServiceApplicationInformationHeaders(TeaModel):
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


class ListApplicationAuthorizationServiceApplicationInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_union_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.access_key = access_key
        self.caller_union_id = caller_union_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformationUsagePlugins(TeaModel):
    def __init__(
        self,
        icon_url: str = None,
        plugin_name: str = None,
    ):
        # iconUrl
        self.icon_url = icon_url
        # pluginName
        self.plugin_name = plugin_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')
        return self


class ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformation(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        attachment_usage_amount: int = None,
        instance_usage_amount: int = None,
        usage_plugins: List[ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformationUsagePlugins] = None,
    ):
        # appName
        self.app_name = app_name
        # appType
        self.app_type = app_type
        # attachmentUsageAmount
        self.attachment_usage_amount = attachment_usage_amount
        # instanceUsageAmount
        self.instance_usage_amount = instance_usage_amount
        # usagePlugins
        self.usage_plugins = usage_plugins

    def validate(self):
        if self.usage_plugins:
            for k in self.usage_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.attachment_usage_amount is not None:
            result['attachmentUsageAmount'] = self.attachment_usage_amount
        if self.instance_usage_amount is not None:
            result['instanceUsageAmount'] = self.instance_usage_amount
        result['usagePlugins'] = []
        if self.usage_plugins is not None:
            for k in self.usage_plugins:
                result['usagePlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('attachmentUsageAmount') is not None:
            self.attachment_usage_amount = m.get('attachmentUsageAmount')
        if m.get('instanceUsageAmount') is not None:
            self.instance_usage_amount = m.get('instanceUsageAmount')
        self.usage_plugins = []
        if m.get('usagePlugins') is not None:
            for k in m.get('usagePlugins'):
                temp_model = ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformationUsagePlugins()
                self.usage_plugins.append(temp_model.from_map(k))
        return self


class ListApplicationAuthorizationServiceApplicationInformationResponseBody(TeaModel):
    def __init__(
        self,
        application_information: List[ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformation] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # applicationInformation
        self.application_information = application_information
        # 当前第几页
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.application_information:
            for k in self.application_information:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applicationInformation'] = []
        if self.application_information is not None:
            for k in self.application_information:
                result['applicationInformation'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_information = []
        if m.get('applicationInformation') is not None:
            for k in m.get('applicationInformation'):
                temp_model = ListApplicationAuthorizationServiceApplicationInformationResponseBodyApplicationInformation()
                self.application_information.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListApplicationAuthorizationServiceApplicationInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationAuthorizationServiceApplicationInformationResponseBody = None,
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
            temp_model = ListApplicationAuthorizationServiceApplicationInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationAuthorizationServiceConnectorInformationHeaders(TeaModel):
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


class ListApplicationAuthorizationServiceConnectorInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformationApplications(TeaModel):
    def __init__(
        self,
        app_name: str = None,
    ):
        # appName
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        return self


class ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformation(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformationApplications] = None,
        icon_url: str = None,
        plug_name: str = None,
        plug_pay_type: int = None,
        plug_status: int = None,
        plug_total_amount: int = None,
        plug_usage_amount: int = None,
        plug_uuid: str = None,
    ):
        # apps
        self.applications = applications
        # iconUrl
        self.icon_url = icon_url
        # pluginName
        self.plug_name = plug_name
        # pluginPayType
        self.plug_pay_type = plug_pay_type
        # pluginStatus
        self.plug_status = plug_status
        # pluginTotalAmount
        self.plug_total_amount = plug_total_amount
        # pluginUsageAmount
        self.plug_usage_amount = plug_usage_amount
        # pluginUuid
        self.plug_uuid = plug_uuid

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['applications'].append(k.to_map() if k else None)
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.plug_name is not None:
            result['plugName'] = self.plug_name
        if self.plug_pay_type is not None:
            result['plugPayType'] = self.plug_pay_type
        if self.plug_status is not None:
            result['plugStatus'] = self.plug_status
        if self.plug_total_amount is not None:
            result['plugTotalAmount'] = self.plug_total_amount
        if self.plug_usage_amount is not None:
            result['plugUsageAmount'] = self.plug_usage_amount
        if self.plug_uuid is not None:
            result['plugUuid'] = self.plug_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('applications') is not None:
            for k in m.get('applications'):
                temp_model = ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformationApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('plugName') is not None:
            self.plug_name = m.get('plugName')
        if m.get('plugPayType') is not None:
            self.plug_pay_type = m.get('plugPayType')
        if m.get('plugStatus') is not None:
            self.plug_status = m.get('plugStatus')
        if m.get('plugTotalAmount') is not None:
            self.plug_total_amount = m.get('plugTotalAmount')
        if m.get('plugUsageAmount') is not None:
            self.plug_usage_amount = m.get('plugUsageAmount')
        if m.get('plugUuid') is not None:
            self.plug_uuid = m.get('plugUuid')
        return self


class ListApplicationAuthorizationServiceConnectorInformationResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plug_information: List[ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformation] = None,
        total_count: int = None,
    ):
        # 当前第几页
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # pluginInfos
        self.plug_information = plug_information
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.plug_information:
            for k in self.plug_information:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['plugInformation'] = []
        if self.plug_information is not None:
            for k in self.plug_information:
                result['plugInformation'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.plug_information = []
        if m.get('plugInformation') is not None:
            for k in m.get('plugInformation'):
                temp_model = ListApplicationAuthorizationServiceConnectorInformationResponseBodyPlugInformation()
                self.plug_information.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListApplicationAuthorizationServiceConnectorInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationAuthorizationServiceConnectorInformationResponseBody = None,
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
            temp_model = ListApplicationAuthorizationServiceConnectorInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationInformationHeaders(TeaModel):
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


class ListApplicationInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListApplicationInformationResponseBodyApplicationInformationUsagePlugins(TeaModel):
    def __init__(
        self,
        icon_url: str = None,
        plugin_name: str = None,
    ):
        # iconUrl
        self.icon_url = icon_url
        # pluginName
        self.plugin_name = plugin_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')
        return self


class ListApplicationInformationResponseBodyApplicationInformation(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        attachment_usage_amount: int = None,
        instance_usage_amount: int = None,
        usage_plugins: List[ListApplicationInformationResponseBodyApplicationInformationUsagePlugins] = None,
    ):
        # appName
        self.app_name = app_name
        # appType
        self.app_type = app_type
        # attachmentUsageAmount
        self.attachment_usage_amount = attachment_usage_amount
        # instanceUsageAmount
        self.instance_usage_amount = instance_usage_amount
        # usagePlugins
        self.usage_plugins = usage_plugins

    def validate(self):
        if self.usage_plugins:
            for k in self.usage_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.attachment_usage_amount is not None:
            result['attachmentUsageAmount'] = self.attachment_usage_amount
        if self.instance_usage_amount is not None:
            result['instanceUsageAmount'] = self.instance_usage_amount
        result['usagePlugins'] = []
        if self.usage_plugins is not None:
            for k in self.usage_plugins:
                result['usagePlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('attachmentUsageAmount') is not None:
            self.attachment_usage_amount = m.get('attachmentUsageAmount')
        if m.get('instanceUsageAmount') is not None:
            self.instance_usage_amount = m.get('instanceUsageAmount')
        self.usage_plugins = []
        if m.get('usagePlugins') is not None:
            for k in m.get('usagePlugins'):
                temp_model = ListApplicationInformationResponseBodyApplicationInformationUsagePlugins()
                self.usage_plugins.append(temp_model.from_map(k))
        return self


class ListApplicationInformationResponseBody(TeaModel):
    def __init__(
        self,
        application_information: List[ListApplicationInformationResponseBodyApplicationInformation] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # applicationInformation
        self.application_information = application_information
        # 当前第几页
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.application_information:
            for k in self.application_information:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applicationInformation'] = []
        if self.application_information is not None:
            for k in self.application_information:
                result['applicationInformation'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_information = []
        if m.get('applicationInformation') is not None:
            for k in m.get('applicationInformation'):
                temp_model = ListApplicationInformationResponseBodyApplicationInformation()
                self.application_information.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListApplicationInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationInformationResponseBody = None,
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
            temp_model = ListApplicationInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommodityHeaders(TeaModel):
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


class ListCommodityRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # accessKey
        self.access_key = access_key
        # callerUid
        self.caller_uid = caller_uid
        # currentPage
        self.page_number = page_number
        # pageSize
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListCommodityResponseBodyCommodityVOList(TeaModel):
    def __init__(
        self,
        account_distribution_number: int = None,
        account_number: int = None,
        activation_code: str = None,
        buy_date_gmt: str = None,
        expire_date_gmt: str = None,
        instance_id: str = None,
        status: str = None,
        version: int = None,
    ):
        # accountDistributionNumber
        self.account_distribution_number = account_distribution_number
        # accountNum
        self.account_number = account_number
        # activationCode
        self.activation_code = activation_code
        # buyDate
        self.buy_date_gmt = buy_date_gmt
        # expireDate
        self.expire_date_gmt = expire_date_gmt
        # instanceId
        self.instance_id = instance_id
        # status
        self.status = status
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_distribution_number is not None:
            result['accountDistributionNumber'] = self.account_distribution_number
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.activation_code is not None:
            result['activationCode'] = self.activation_code
        if self.buy_date_gmt is not None:
            result['buyDateGMT'] = self.buy_date_gmt
        if self.expire_date_gmt is not None:
            result['expireDateGMT'] = self.expire_date_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountDistributionNumber') is not None:
            self.account_distribution_number = m.get('accountDistributionNumber')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('activationCode') is not None:
            self.activation_code = m.get('activationCode')
        if m.get('buyDateGMT') is not None:
            self.buy_date_gmt = m.get('buyDateGMT')
        if m.get('expireDateGMT') is not None:
            self.expire_date_gmt = m.get('expireDateGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListCommodityResponseBody(TeaModel):
    def __init__(
        self,
        commodity_volist: List[ListCommodityResponseBodyCommodityVOList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # commodityVOList
        self.commodity_volist = commodity_volist
        # 当前第几页
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.commodity_volist:
            for k in self.commodity_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['commodityVOList'] = []
        if self.commodity_volist is not None:
            for k in self.commodity_volist:
                result['commodityVOList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_volist = []
        if m.get('commodityVOList') is not None:
            for k in m.get('commodityVOList'):
                temp_model = ListCommodityResponseBodyCommodityVOList()
                self.commodity_volist.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCommodityResponseBody = None,
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
            temp_model = ListCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectorInformationHeaders(TeaModel):
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


class ListConnectorInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConnectorInformationResponseBodyPluginInfosApps(TeaModel):
    def __init__(
        self,
        app_name: str = None,
    ):
        # appName
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        return self


class ListConnectorInformationResponseBodyPluginInfos(TeaModel):
    def __init__(
        self,
        apps: List[ListConnectorInformationResponseBodyPluginInfosApps] = None,
        icon_url: str = None,
        plugin_name: str = None,
        plugin_pay_type: int = None,
        plugin_status: int = None,
        plugin_total_amount: int = None,
        plugin_usage_amount: int = None,
        plugin_uuid: str = None,
    ):
        # apps
        self.apps = apps
        # iconUrl
        self.icon_url = icon_url
        # pluginName
        self.plugin_name = plugin_name
        # pluginPayType
        self.plugin_pay_type = plugin_pay_type
        # pluginStatus
        self.plugin_status = plugin_status
        # pluginTotalAmount
        self.plugin_total_amount = plugin_total_amount
        # pluginUsageAmount
        self.plugin_usage_amount = plugin_usage_amount
        # pluginUuid
        self.plugin_uuid = plugin_uuid

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['apps'].append(k.to_map() if k else None)
        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url
        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name
        if self.plugin_pay_type is not None:
            result['pluginPayType'] = self.plugin_pay_type
        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status
        if self.plugin_total_amount is not None:
            result['pluginTotalAmount'] = self.plugin_total_amount
        if self.plugin_usage_amount is not None:
            result['pluginUsageAmount'] = self.plugin_usage_amount
        if self.plugin_uuid is not None:
            result['pluginUuid'] = self.plugin_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apps = []
        if m.get('apps') is not None:
            for k in m.get('apps'):
                temp_model = ListConnectorInformationResponseBodyPluginInfosApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')
        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')
        if m.get('pluginPayType') is not None:
            self.plugin_pay_type = m.get('pluginPayType')
        if m.get('pluginStatus') is not None:
            self.plugin_status = m.get('pluginStatus')
        if m.get('pluginTotalAmount') is not None:
            self.plugin_total_amount = m.get('pluginTotalAmount')
        if m.get('pluginUsageAmount') is not None:
            self.plugin_usage_amount = m.get('pluginUsageAmount')
        if m.get('pluginUuid') is not None:
            self.plugin_uuid = m.get('pluginUuid')
        return self


class ListConnectorInformationResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugin_infos: List[ListConnectorInformationResponseBodyPluginInfos] = None,
        total_count: int = None,
    ):
        # 当前第几页
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # pluginInfos
        self.plugin_infos = plugin_infos
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.plugin_infos:
            for k in self.plugin_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['pluginInfos'] = []
        if self.plugin_infos is not None:
            for k in self.plugin_infos:
                result['pluginInfos'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.plugin_infos = []
        if m.get('pluginInfos') is not None:
            for k in m.get('pluginInfos'):
                temp_model = ListConnectorInformationResponseBodyPluginInfos()
                self.plugin_infos.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListConnectorInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectorInformationResponseBody = None,
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
            temp_model = ListConnectorInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNavigationByFormTypeHeaders(TeaModel):
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


class ListNavigationByFormTypeRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_type: str = None,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 页面类型
        self.form_type = form_type
        # 语言
        self.language = language
        # 应用秘钥
        self.system_token = system_token
        # 评论人钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_type is not None:
            result['formType'] = self.form_type
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formType') is not None:
            self.form_type = m.get('formType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListNavigationByFormTypeResponseBodyResultTitle(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListNavigationByFormTypeResponseBodyResult(TeaModel):
    def __init__(
        self,
        form_uuid: str = None,
        process_code: str = None,
        title: ListNavigationByFormTypeResponseBodyResultTitle = None,
    ):
        # formUuid
        self.form_uuid = form_uuid
        # processCode
        self.process_code = process_code
        # title
        self.title = title

    def validate(self):
        if self.title:
            self.title.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.title is not None:
            result['title'] = self.title.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('title') is not None:
            temp_model = ListNavigationByFormTypeResponseBodyResultTitle()
            self.title = temp_model.from_map(m['title'])
        return self


class ListNavigationByFormTypeResponseBody(TeaModel):
    def __init__(
        self,
        result: List[ListNavigationByFormTypeResponseBodyResult] = None,
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
                temp_model = ListNavigationByFormTypeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListNavigationByFormTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNavigationByFormTypeResponseBody = None,
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
            temp_model = ListNavigationByFormTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTableDataByFormInstanceIdTableIdHeaders(TeaModel):
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


class ListTableDataByFormInstanceIdTableIdRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_uuid: str = None,
        page_number: int = None,
        page_size: int = None,
        system_token: str = None,
        table_field_id: str = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 表单ID
        self.form_uuid = form_uuid
        # 当前页
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 应用秘钥
        self.system_token = system_token
        # 需要查找的子表单组件的唯一标识
        self.table_field_id = table_field_id
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.table_field_id is not None:
            result['tableFieldId'] = self.table_field_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('tableFieldId') is not None:
            self.table_field_id = m.get('tableFieldId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListTableDataByFormInstanceIdTableIdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTableDataByFormInstanceIdTableIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTableDataByFormInstanceIdTableIdResponseBody = None,
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
            temp_model = ListTableDataByFormInstanceIdTableIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginCodeGenHeaders(TeaModel):
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


class LoginCodeGenRequest(TeaModel):
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


class LoginCodeGenResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # result
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


class LoginCodeGenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LoginCodeGenResponseBody = None,
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
            temp_model = LoginCodeGenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NotifyAuthorizationResultHeaders(TeaModel):
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


class NotifyAuthorizationResultRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        account_number: str = None,
        begin_time_gmt: int = None,
        caller_uid: str = None,
        charge_type: str = None,
        commerce_type: str = None,
        commodity_type: str = None,
        end_time_gmt: int = None,
        instance_id: str = None,
        instance_name: str = None,
        produce_code: str = None,
    ):
        self.access_key = access_key
        self.account_number = account_number
        self.begin_time_gmt = begin_time_gmt
        self.caller_uid = caller_uid
        self.charge_type = charge_type
        self.commerce_type = commerce_type
        self.commodity_type = commodity_type
        self.end_time_gmt = end_time_gmt
        self.instance_id = instance_id
        self.instance_name = instance_name
        # 阿里云产品code
        self.produce_code = produce_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.begin_time_gmt is not None:
            result['beginTimeGMT'] = self.begin_time_gmt
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commerce_type is not None:
            result['commerceType'] = self.commerce_type
        if self.commodity_type is not None:
            result['commodityType'] = self.commodity_type
        if self.end_time_gmt is not None:
            result['endTimeGMT'] = self.end_time_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.produce_code is not None:
            result['produceCode'] = self.produce_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('beginTimeGMT') is not None:
            self.begin_time_gmt = m.get('beginTimeGMT')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commerceType') is not None:
            self.commerce_type = m.get('commerceType')
        if m.get('commodityType') is not None:
            self.commodity_type = m.get('commodityType')
        if m.get('endTimeGMT') is not None:
            self.end_time_gmt = m.get('endTimeGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('produceCode') is not None:
            self.produce_code = m.get('produceCode')
        return self


class NotifyAuthorizationResultResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class NotifyAuthorizationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: NotifyAuthorizationResultResponseBody = None,
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
            temp_model = NotifyAuthorizationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RedirectTaskHeaders(TeaModel):
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


class RedirectTaskRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        by_manager: str = None,
        language: str = None,
        now_action_executor_id: str = None,
        process_instance_id: str = None,
        remark: str = None,
        system_token: str = None,
        task_id: int = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 是否应用管理员进行转交; ●
        # 可选项 : y/n
        # 
        # ●
        # y,则userId必须传应用管理员工号，或者yida_pub_account
        # 
        # ●
        # n, userId必须传任务的当前执行人
        self.by_manager = by_manager
        # 语言环境; 可选值：zh_CN/en_US
        self.language = language
        # 新的任务处理人工号
        self.now_action_executor_id = now_action_executor_id
        # 实例ID
        self.process_instance_id = process_instance_id
        # 转交备注
        self.remark = remark
        # 验权token; 在应用数据中获取。
        self.system_token = system_token
        # 任务ID
        self.task_id = task_id
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.by_manager is not None:
            result['byManager'] = self.by_manager
        if self.language is not None:
            result['language'] = self.language
        if self.now_action_executor_id is not None:
            result['nowActionExecutorId'] = self.now_action_executor_id
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('byManager') is not None:
            self.by_manager = m.get('byManager')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('nowActionExecutorId') is not None:
            self.now_action_executor_id = m.get('nowActionExecutorId')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class RedirectTaskResponse(TeaModel):
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


class RefundCommodityHeaders(TeaModel):
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


class RefundCommodityRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class RefundCommodityResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RefundCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundCommodityResponseBody = None,
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
            temp_model = RefundCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterAccountsHeaders(TeaModel):
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


class RegisterAccountsRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        active_code: str = None,
        corp_id: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 激活码
        self.active_code = active_code
        # 组织id
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.active_code is not None:
            result['activeCode'] = self.active_code
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('activeCode') is not None:
            self.active_code = m.get('activeCode')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class RegisterAccountsResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class RegisterAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterAccountsResponseBody = None,
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
            temp_model = RegisterAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseCommodityHeaders(TeaModel):
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


class ReleaseCommodityRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ReleaseCommodityResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ReleaseCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseCommodityResponseBody = None,
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
            temp_model = ReleaseCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTenantResourceHeaders(TeaModel):
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


class RemoveTenantResourceRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        # accessKey
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class RemoveTenantResourceResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class RemoveTenantResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTenantResourceResponseBody = None,
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
            temp_model = RemoveTenantResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderBatchCallbackHeaders(TeaModel):
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


class RenderBatchCallbackRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        corp_id: str = None,
        file_size: int = None,
        language: str = None,
        namespace: str = None,
        oss_url: str = None,
        sequence_id: str = None,
        source: str = None,
        status: str = None,
        system_token: str = None,
        time_zone: str = None,
        user_id: str = None,
    ):
        # appType
        self.app_type = app_type
        # 组织id
        self.corp_id = corp_id
        # 文件大小
        self.file_size = file_size
        # language
        self.language = language
        # 名称空间
        self.namespace = namespace
        # oss文件链接
        self.oss_url = oss_url
        # 流水号
        self.sequence_id = sequence_id
        # 源
        self.source = source
        # 状态
        self.status = status
        # systemToken
        self.system_token = system_token
        # 时间区域
        self.time_zone = time_zone
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.language is not None:
            result['language'] = self.language
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_url is not None:
            result['ossUrl'] = self.oss_url
        if self.sequence_id is not None:
            result['sequenceId'] = self.sequence_id
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossUrl') is not None:
            self.oss_url = m.get('ossUrl')
        if m.get('sequenceId') is not None:
            self.sequence_id = m.get('sequenceId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class RenderBatchCallbackResponse(TeaModel):
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


class RenewApplicationAuthorizationServiceOrderHeaders(TeaModel):
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


class RenewApplicationAuthorizationServiceOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_union_id: str = None,
        end_time_gmt: int = None,
        instance_id: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 结束时间
        self.end_time_gmt = end_time_gmt
        # 实例id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.end_time_gmt is not None:
            result['endTimeGMT'] = self.end_time_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('endTimeGMT') is not None:
            self.end_time_gmt = m.get('endTimeGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class RenewApplicationAuthorizationServiceOrderResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class RenewApplicationAuthorizationServiceOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewApplicationAuthorizationServiceOrderResponseBody = None,
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
            temp_model = RenewApplicationAuthorizationServiceOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewTenantOrderHeaders(TeaModel):
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


class RenewTenantOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_union_id: str = None,
        end_time_gmt: int = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 结束时间
        self.end_time_gmt = end_time_gmt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.end_time_gmt is not None:
            result['endTimeGMT'] = self.end_time_gmt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('endTimeGMT') is not None:
            self.end_time_gmt = m.get('endTimeGMT')
        return self


class RenewTenantOrderResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class RenewTenantOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewTenantOrderResponseBody = None,
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
            temp_model = RenewTenantOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveFormDataHeaders(TeaModel):
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


class SaveFormDataRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_data_json: str = None,
        form_uuid: str = None,
        language: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 表单数据
        self.form_data_json = form_data_json
        # 表单ID
        self.form_uuid = form_uuid
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 钉钉userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_data_json is not None:
            result['formDataJson'] = self.form_data_json
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formDataJson') is not None:
            self.form_data_json = m.get('formDataJson')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SaveFormDataResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 表单实例ID
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


class SaveFormDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveFormDataResponseBody = None,
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
            temp_model = SaveFormDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveFormRemarkHeaders(TeaModel):
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


class SaveFormRemarkRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        at_user_id: str = None,
        content: str = None,
        form_instance_id: str = None,
        language: str = None,
        reply_id: int = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 将评论内容通过钉钉发给指定用户
        self.at_user_id = at_user_id
        # 评论内容
        self.content = content
        # 实例ID
        self.form_instance_id = form_instance_id
        # 语言
        self.language = language
        # 对评论进行回复
        self.reply_id = reply_id
        # 应用秘钥
        self.system_token = system_token
        # 评论人钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.at_user_id is not None:
            result['atUserId'] = self.at_user_id
        if self.content is not None:
            result['content'] = self.content
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.language is not None:
            result['language'] = self.language
        if self.reply_id is not None:
            result['replyId'] = self.reply_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('atUserId') is not None:
            self.at_user_id = m.get('atUserId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('replyId') is not None:
            self.reply_id = m.get('replyId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SaveFormRemarkResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # 评论的ID
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


class SaveFormRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveFormRemarkResponseBody = None,
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
            temp_model = SaveFormRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SavePrintTplDetailInfoHeaders(TeaModel):
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


class SavePrintTplDetailInfoRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        description: str = None,
        file_name_config: str = None,
        form_uuid: str = None,
        form_version: int = None,
        setting: str = None,
        template_id: int = None,
        title: str = None,
        user_id: str = None,
        vm: str = None,
    ):
        # 应用代码
        self.app_type = app_type
        # 模板描述
        self.description = description
        # 文件名配置
        self.file_name_config = file_name_config
        # 表单id
        self.form_uuid = form_uuid
        # 表单版本
        self.form_version = form_version
        # 模板的其他配置信息
        self.setting = setting
        # 打印模板id
        self.template_id = template_id
        # 模板标题
        self.title = title
        # 用户id
        self.user_id = user_id
        # 模板的VM
        self.vm = vm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.description is not None:
            result['description'] = self.description
        if self.file_name_config is not None:
            result['fileNameConfig'] = self.file_name_config
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.form_version is not None:
            result['formVersion'] = self.form_version
        if self.setting is not None:
            result['setting'] = self.setting
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.vm is not None:
            result['vm'] = self.vm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fileNameConfig') is not None:
            self.file_name_config = m.get('fileNameConfig')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('formVersion') is not None:
            self.form_version = m.get('formVersion')
        if m.get('setting') is not None:
            self.setting = m.get('setting')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('vm') is not None:
            self.vm = m.get('vm')
        return self


class SavePrintTplDetailInfoResponseBody(TeaModel):
    def __init__(
        self,
        result: int = None,
    ):
        # 模板id
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


class SavePrintTplDetailInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SavePrintTplDetailInfoResponseBody = None,
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
            temp_model = SavePrintTplDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchActivationCodeHeaders(TeaModel):
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


class SearchActivationCodeRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
    ):
        # 访问key
        self.access_key = access_key
        # 用户的uid
        self.caller_uid = caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        return self


class SearchActivationCodeResponseBody(TeaModel):
    def __init__(
        self,
        activation_code: str = None,
        auth_type: str = None,
        expire_time_gmt: str = None,
        instance_id: str = None,
        status: int = None,
    ):
        # activationCode
        self.activation_code = activation_code
        # authType
        self.auth_type = auth_type
        # expireTime
        self.expire_time_gmt = expire_time_gmt
        # instanceId
        self.instance_id = instance_id
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activation_code is not None:
            result['activationCode'] = self.activation_code
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.expire_time_gmt is not None:
            result['expireTimeGMT'] = self.expire_time_gmt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activationCode') is not None:
            self.activation_code = m.get('activationCode')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('expireTimeGMT') is not None:
            self.expire_time_gmt = m.get('expireTimeGMT')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SearchActivationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchActivationCodeResponseBody = None,
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
            temp_model = SearchActivationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEmployeeFieldValuesHeaders(TeaModel):
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


class SearchEmployeeFieldValuesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        search_field_json: str = None,
        system_token: str = None,
        target_field_json: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        self.form_uuid = form_uuid
        self.language = language
        self.modified_from_time_gmt = modified_from_time_gmt
        self.modified_to_time_gmt = modified_to_time_gmt
        self.originator_id = originator_id
        self.search_field_json = search_field_json
        self.system_token = system_token
        self.target_field_json = target_field_json
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.language is not None:
            result['language'] = self.language
        if self.modified_from_time_gmt is not None:
            result['modifiedFromTimeGMT'] = self.modified_from_time_gmt
        if self.modified_to_time_gmt is not None:
            result['modifiedToTimeGMT'] = self.modified_to_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.search_field_json is not None:
            result['searchFieldJson'] = self.search_field_json
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.target_field_json is not None:
            result['targetFieldJson'] = self.target_field_json
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('modifiedFromTimeGMT')
        if m.get('modifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('modifiedToTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('searchFieldJson') is not None:
            self.search_field_json = m.get('searchFieldJson')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('targetFieldJson') is not None:
            self.target_field_json = m.get('targetFieldJson')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SearchEmployeeFieldValuesResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
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


class SearchEmployeeFieldValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchEmployeeFieldValuesResponseBody = None,
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
            temp_model = SearchEmployeeFieldValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFormDataIdListHeaders(TeaModel):
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


class SearchFormDataIdListRequest(TeaModel):
    def __init__(
        self,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        search_field_json: str = None,
        system_token: str = None,
        user_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表
        self.create_from_time_gmt = create_from_time_gmt
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。
        self.create_to_time_gmt = create_to_time_gmt
        # 语言
        self.language = language
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表
        self.modified_from_time_gmt = modified_from_time_gmt
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。
        self.modified_to_time_gmt = modified_to_time_gmt
        # 根据数据提交人工号查询
        self.originator_id = originator_id
        # 根据表单内组件值查询
        self.search_field_json = search_field_json
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.language is not None:
            result['language'] = self.language
        if self.modified_from_time_gmt is not None:
            result['modifiedFromTimeGMT'] = self.modified_from_time_gmt
        if self.modified_to_time_gmt is not None:
            result['modifiedToTimeGMT'] = self.modified_to_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.search_field_json is not None:
            result['searchFieldJson'] = self.search_field_json
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('modifiedFromTimeGMT')
        if m.get('modifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('modifiedToTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('searchFieldJson') is not None:
            self.search_field_json = m.get('searchFieldJson')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class SearchFormDataIdListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        page_number: int = None,
        total_count: int = None,
    ):
        # data
        self.data = data
        # 当前第几页
        self.page_number = page_number
        # 总数量
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class SearchFormDataIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFormDataIdListResponseBody = None,
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
            temp_model = SearchFormDataIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFormDatasHeaders(TeaModel):
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


class SearchFormDatasRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        current_page: int = None,
        dynamic_order: str = None,
        form_uuid: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        page_size: int = None,
        search_field_json: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表, 字符串格式，且为yyyy-MM-DD格式
        self.create_from_time_gmt = create_from_time_gmt
        # createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。字符串格式，且为yyyy-MM-DD格式。 和createFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)创建的数据。
        self.create_to_time_gmt = create_to_time_gmt
        # 当前页
        self.current_page = current_page
        # 指定排序字段
        self.dynamic_order = dynamic_order
        # 表单ID
        self.form_uuid = form_uuid
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。字符串格式，且为yyyy-MM-DD格式
        self.modified_from_time_gmt = modified_from_time_gmt
        # modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。字符串格式，且为yyyy-MM-DD格式。 和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。
        self.modified_to_time_gmt = modified_to_time_gmt
        # 根据数据提交人工号查询
        self.originator_id = originator_id
        # 每页记录数
        self.page_size = page_size
        # 根据表单内组件值查询
        self.search_field_json = search_field_json
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 钉钉userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.create_from_time_gmt is not None:
            result['createFromTimeGMT'] = self.create_from_time_gmt
        if self.create_to_time_gmt is not None:
            result['createToTimeGMT'] = self.create_to_time_gmt
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.dynamic_order is not None:
            result['dynamicOrder'] = self.dynamic_order
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.language is not None:
            result['language'] = self.language
        if self.modified_from_time_gmt is not None:
            result['modifiedFromTimeGMT'] = self.modified_from_time_gmt
        if self.modified_to_time_gmt is not None:
            result['modifiedToTimeGMT'] = self.modified_to_time_gmt
        if self.originator_id is not None:
            result['originatorId'] = self.originator_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.search_field_json is not None:
            result['searchFieldJson'] = self.search_field_json
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('createFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('createFromTimeGMT')
        if m.get('createToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('createToTimeGMT')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('dynamicOrder') is not None:
            self.dynamic_order = m.get('dynamicOrder')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('modifiedFromTimeGMT')
        if m.get('modifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('modifiedToTimeGMT')
        if m.get('originatorId') is not None:
            self.originator_id = m.get('originatorId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('searchFieldJson') is not None:
            self.search_field_json = m.get('searchFieldJson')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SearchFormDatasResponseBodyDataModifyUserUserName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # 国际化
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SearchFormDatasResponseBodyDataModifyUser(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        user_id: str = None,
        user_name: SearchFormDatasResponseBodyDataModifyUserUserName = None,
    ):
        # 部门名称
        self.department_name = department_name
        # 邮箱
        self.email = email
        # 用户工号
        self.user_id = user_id
        # 用户名
        self.user_name = user_name

    def validate(self):
        if self.user_name:
            self.user_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.email is not None:
            result['email'] = self.email
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            temp_model = SearchFormDatasResponseBodyDataModifyUserUserName()
            self.user_name = temp_model.from_map(m['userName'])
        return self


class SearchFormDatasResponseBodyDataOriginatorUserName(TeaModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        # 中文名称
        self.name_in_chinese = name_in_chinese
        # 英文名称
        self.name_in_english = name_in_english
        # 国际化
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_in_chinese is not None:
            result['nameInChinese'] = self.name_in_chinese
        if self.name_in_english is not None:
            result['nameInEnglish'] = self.name_in_english
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameInChinese') is not None:
            self.name_in_chinese = m.get('nameInChinese')
        if m.get('nameInEnglish') is not None:
            self.name_in_english = m.get('nameInEnglish')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SearchFormDatasResponseBodyDataOriginator(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        user_id: str = None,
        user_name: SearchFormDatasResponseBodyDataOriginatorUserName = None,
    ):
        # 部门名称
        self.department_name = department_name
        # 邮箱
        self.email = email
        # 用户工号
        self.user_id = user_id
        # 用户名
        self.user_name = user_name

    def validate(self):
        if self.user_name:
            self.user_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['departmentName'] = self.department_name
        if self.email is not None:
            result['email'] = self.email
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentName') is not None:
            self.department_name = m.get('departmentName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            temp_model = SearchFormDatasResponseBodyDataOriginatorUserName()
            self.user_name = temp_model.from_map(m['userName'])
        return self


class SearchFormDatasResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time_gmt: str = None,
        creator_user_id: str = None,
        data_id: int = None,
        form_data: Dict[str, Any] = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        instance_value: str = None,
        model_uuid: str = None,
        modified_time_gmt: str = None,
        modifier_user_id: str = None,
        modify_user: SearchFormDatasResponseBodyDataModifyUser = None,
        originator: SearchFormDatasResponseBodyDataOriginator = None,
        sequence: str = None,
        serial_no: str = None,
        title: str = None,
        version: int = None,
    ):
        # 数据创建时间
        self.created_time_gmt = created_time_gmt
        # 创建人
        self.creator_user_id = creator_user_id
        # 实体主键id
        self.data_id = data_id
        # 表单数据
        self.form_data = form_data
        # 表单实例ID
        self.form_instance_id = form_instance_id
        # 表单id
        self.form_uuid = form_uuid
        # 表单实例原始格式值
        self.instance_value = instance_value
        # 模型id
        self.model_uuid = model_uuid
        # 最近修改时间
        self.modified_time_gmt = modified_time_gmt
        # 修改人
        self.modifier_user_id = modifier_user_id
        # 修改者
        self.modify_user = modify_user
        # 发起人
        self.originator = originator
        # 批次号
        self.sequence = sequence
        # 流水号
        self.serial_no = serial_no
        # 标题
        self.title = title
        # 数据版本
        self.version = version

    def validate(self):
        if self.modify_user:
            self.modify_user.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time_gmt is not None:
            result['createdTimeGMT'] = self.created_time_gmt
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.data_id is not None:
            result['dataId'] = self.data_id
        if self.form_data is not None:
            result['formData'] = self.form_data
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.instance_value is not None:
            result['instanceValue'] = self.instance_value
        if self.model_uuid is not None:
            result['modelUuid'] = self.model_uuid
        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt
        if self.modifier_user_id is not None:
            result['modifierUserId'] = self.modifier_user_id
        if self.modify_user is not None:
            result['modifyUser'] = self.modify_user.to_map()
        if self.originator is not None:
            result['originator'] = self.originator.to_map()
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.serial_no is not None:
            result['serialNo'] = self.serial_no
        if self.title is not None:
            result['title'] = self.title
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTimeGMT') is not None:
            self.created_time_gmt = m.get('createdTimeGMT')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        if m.get('formData') is not None:
            self.form_data = m.get('formData')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('instanceValue') is not None:
            self.instance_value = m.get('instanceValue')
        if m.get('modelUuid') is not None:
            self.model_uuid = m.get('modelUuid')
        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')
        if m.get('modifierUserId') is not None:
            self.modifier_user_id = m.get('modifierUserId')
        if m.get('modifyUser') is not None:
            temp_model = SearchFormDatasResponseBodyDataModifyUser()
            self.modify_user = temp_model.from_map(m['modifyUser'])
        if m.get('originator') is not None:
            temp_model = SearchFormDatasResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m['originator'])
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('serialNo') is not None:
            self.serial_no = m.get('serialNo')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class SearchFormDatasResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[SearchFormDatasResponseBodyData] = None,
        total_count: int = None,
    ):
        # 当前页
        self.current_page = current_page
        # 实例详情列表
        self.data = data
        # 符合条件的实例总数
        self.total_count = total_count

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
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = SearchFormDatasResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class SearchFormDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFormDatasResponseBody = None,
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
            temp_model = SearchFormDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceHeaders(TeaModel):
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


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        department_id: str = None,
        form_data_json: str = None,
        form_uuid: str = None,
        language: str = None,
        process_code: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 发起人所在部门编号
        self.department_id = department_id
        # 表单数据
        self.form_data_json = form_data_json
        # 表单唯一编码
        self.form_uuid = form_uuid
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # 流程编码
        self.process_code = process_code
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 钉钉userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.form_data_json is not None:
            result['formDataJson'] = self.form_data_json
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid
        if self.language is not None:
            result['language'] = self.language
        if self.process_code is not None:
            result['processCode'] = self.process_code
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('formDataJson') is not None:
            self.form_data_json = m.get('formDataJson')
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processCode') is not None:
            self.process_code = m.get('processCode')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 流程实例ID
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


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateCloudAuthorizationHeaders(TeaModel):
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


class TerminateCloudAuthorizationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_union_id: str = None,
        instance_id: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 实例id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class TerminateCloudAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class TerminateCloudAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminateCloudAuthorizationResponseBody = None,
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
            temp_model = TerminateCloudAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateInstanceHeaders(TeaModel):
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


class TerminateInstanceRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言
        self.language = language
        # 流程实例ID
        self.process_instance_id = process_instance_id
        # 应用秘钥
        self.system_token = system_token
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class TerminateInstanceResponse(TeaModel):
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


class UpdateCloudAccountInformationHeaders(TeaModel):
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


class UpdateCloudAccountInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        account_number: str = None,
        caller_union_id: str = None,
        commodity_type: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 账户号
        self.account_number = account_number
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 商品类型
        self.commodity_type = commodity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.commodity_type is not None:
            result['commodityType'] = self.commodity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('commodityType') is not None:
            self.commodity_type = m.get('commodityType')
        return self


class UpdateCloudAccountInformationResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class UpdateCloudAccountInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCloudAccountInformationResponseBody = None,
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
            temp_model = UpdateCloudAccountInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFormDataHeaders(TeaModel):
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


class UpdateFormDataRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        form_instance_id: str = None,
        language: str = None,
        system_token: str = None,
        update_form_data_json: str = None,
        use_latest_version: bool = None,
        user_id: str = None,
    ):
        # 应用编码
        self.app_type = app_type
        # 要更新的表单数据ID
        self.form_instance_id = form_instance_id
        # 语言。可选值：zh_CN/en_US 默认：zh_CN
        self.language = language
        # 应用秘钥。在应用数据中获取。
        self.system_token = system_token
        # 要更新的表单组件值。参数有的组件更新，没有的组件保持不变。 明细的值只能统一更新，无法只更新明细下某个组件的值
        self.update_form_data_json = update_form_data_json
        # 使用最新的表单版本进行更新。默认为false
        self.use_latest_version = use_latest_version
        # 钉钉userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.form_instance_id is not None:
            result['formInstanceId'] = self.form_instance_id
        if self.language is not None:
            result['language'] = self.language
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.update_form_data_json is not None:
            result['updateFormDataJson'] = self.update_form_data_json
        if self.use_latest_version is not None:
            result['useLatestVersion'] = self.use_latest_version
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('formInstanceId') is not None:
            self.form_instance_id = m.get('formInstanceId')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('updateFormDataJson') is not None:
            self.update_form_data_json = m.get('updateFormDataJson')
        if m.get('useLatestVersion') is not None:
            self.use_latest_version = m.get('useLatestVersion')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateFormDataResponse(TeaModel):
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


class UpdateInstanceHeaders(TeaModel):
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


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        language: str = None,
        process_instance_id: str = None,
        system_token: str = None,
        update_form_data_json: str = None,
        user_id: str = None,
    ):
        # 应用ID
        self.app_type = app_type
        # 语言环境
        self.language = language
        # 实例ID
        self.process_instance_id = process_instance_id
        # 应用秘钥
        self.system_token = system_token
        # 更新的表单数据
        self.update_form_data_json = update_form_data_json
        # 钉钉的userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.language is not None:
            result['language'] = self.language
        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.update_form_data_json is not None:
            result['updateFormDataJson'] = self.update_form_data_json
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('updateFormDataJson') is not None:
            self.update_form_data_json = m.get('updateFormDataJson')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateInstanceResponse(TeaModel):
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


class UpdateStatusHeaders(TeaModel):
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


class UpdateStatusRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        error_lines: List[int] = None,
        import_sequence: str = None,
        language: str = None,
        status: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.error_lines = error_lines
        self.import_sequence = import_sequence
        self.language = language
        self.status = status
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.error_lines is not None:
            result['errorLines'] = self.error_lines
        if self.import_sequence is not None:
            result['importSequence'] = self.import_sequence
        if self.language is not None:
            result['language'] = self.language
        if self.status is not None:
            result['status'] = self.status
        if self.system_token is not None:
            result['systemToken'] = self.system_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('errorLines') is not None:
            self.error_lines = m.get('errorLines')
        if m.get('importSequence') is not None:
            self.import_sequence = m.get('importSequence')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('systemToken') is not None:
            self.system_token = m.get('systemToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateStatusResponse(TeaModel):
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


class UpgradeTenantInformationHeaders(TeaModel):
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


class UpgradeTenantInformationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        account_number: str = None,
        caller_union_id: str = None,
        commodity_type: str = None,
    ):
        # 访问秘钥
        self.access_key = access_key
        # 账户号
        self.account_number = account_number
        # 调用者unionId
        self.caller_union_id = caller_union_id
        # 商品类型
        self.commodity_type = commodity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.account_number is not None:
            result['accountNumber'] = self.account_number
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        if self.commodity_type is not None:
            result['commodityType'] = self.commodity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accountNumber') is not None:
            self.account_number = m.get('accountNumber')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        if m.get('commodityType') is not None:
            self.commodity_type = m.get('commodityType')
        return self


class UpgradeTenantInformationResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
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


class UpgradeTenantInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeTenantInformationResponseBody = None,
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
            temp_model = UpgradeTenantInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationAuthorizationOrderHeaders(TeaModel):
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


class ValidateApplicationAuthorizationOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_union_id: str = None,
    ):
        self.access_key = access_key
        self.caller_union_id = caller_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_union_id is not None:
            result['callerUnionId'] = self.caller_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUnionId') is not None:
            self.caller_union_id = m.get('callerUnionId')
        return self


class ValidateApplicationAuthorizationOrderResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateApplicationAuthorizationOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateApplicationAuthorizationOrderResponseBody = None,
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
            temp_model = ValidateApplicationAuthorizationOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationAuthorizationServiceOrderHeaders(TeaModel):
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


class ValidateApplicationAuthorizationServiceOrderRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class ValidateApplicationAuthorizationServiceOrderResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateApplicationAuthorizationServiceOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateApplicationAuthorizationServiceOrderResponseBody = None,
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
            temp_model = ValidateApplicationAuthorizationServiceOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationServiceOrderUpgradeHeaders(TeaModel):
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


class ValidateApplicationServiceOrderUpgradeRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        # accessKey
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class ValidateApplicationServiceOrderUpgradeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateApplicationServiceOrderUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateApplicationServiceOrderUpgradeResponseBody = None,
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
            temp_model = ValidateApplicationServiceOrderUpgradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateOrderBuyHeaders(TeaModel):
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


class ValidateOrderBuyRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        return self


class ValidateOrderBuyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateOrderBuyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateOrderBuyResponseBody = None,
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
            temp_model = ValidateOrderBuyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateOrderUpdateHeaders(TeaModel):
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


class ValidateOrderUpdateRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        return self


class ValidateOrderUpdateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateOrderUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateOrderUpdateResponseBody = None,
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
            temp_model = ValidateOrderUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateOrderUpgradeHeaders(TeaModel):
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


class ValidateOrderUpgradeRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        caller_uid: str = None,
        instance_id: str = None,
    ):
        self.access_key = access_key
        self.caller_uid = caller_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ValidateOrderUpgradeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        # message
        self.message = message
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateOrderUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateOrderUpgradeResponseBody = None,
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
            temp_model = ValidateOrderUpgradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


