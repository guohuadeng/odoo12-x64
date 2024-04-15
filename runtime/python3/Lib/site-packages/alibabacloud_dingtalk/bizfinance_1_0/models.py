# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateReceiptHeaders(TeaModel):
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


class CreateReceiptRequestReceipts(TeaModel):
    def __init__(
        self,
        amount: str = None,
        category_code: str = None,
        code: str = None,
        create_time: int = None,
        create_user_id: str = None,
        customer_code: str = None,
        enterprise_acount_code: str = None,
        occur_date: int = None,
        principal_id: str = None,
        project_code: str = None,
        receipt_type: int = None,
        remark: str = None,
        supplier_code: str = None,
        title: str = None,
    ):
        # 单据金额
        self.amount = amount
        # 关联收支类别code
        self.category_code = category_code
        # 单据唯一编号
        self.code = code
        # 单据创建时间，默认当前时间
        self.create_time = create_time
        # 创建人工号
        self.create_user_id = create_user_id
        # 关联客户code
        self.customer_code = customer_code
        # 关联企业账户code
        self.enterprise_acount_code = enterprise_acount_code
        # 业务发生时间，默认当前时间
        self.occur_date = occur_date
        # 负责人工号，传空代表不修改
        self.principal_id = principal_id
        # 关联项目code
        self.project_code = project_code
        # 单据类型：1付款单，2收款单
        self.receipt_type = receipt_type
        # 备注
        self.remark = remark
        # 关联供应商code
        self.supplier_code = supplier_code
        # 单据标题，不传由系统默认生成
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.category_code is not None:
            result['categoryCode'] = self.category_code
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.customer_code is not None:
            result['customerCode'] = self.customer_code
        if self.enterprise_acount_code is not None:
            result['enterpriseAcountCode'] = self.enterprise_acount_code
        if self.occur_date is not None:
            result['occurDate'] = self.occur_date
        if self.principal_id is not None:
            result['principalId'] = self.principal_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.receipt_type is not None:
            result['receiptType'] = self.receipt_type
        if self.remark is not None:
            result['remark'] = self.remark
        if self.supplier_code is not None:
            result['supplierCode'] = self.supplier_code
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('customerCode') is not None:
            self.customer_code = m.get('customerCode')
        if m.get('enterpriseAcountCode') is not None:
            self.enterprise_acount_code = m.get('enterpriseAcountCode')
        if m.get('occurDate') is not None:
            self.occur_date = m.get('occurDate')
        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('receiptType') is not None:
            self.receipt_type = m.get('receiptType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('supplierCode') is not None:
            self.supplier_code = m.get('supplierCode')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateReceiptRequest(TeaModel):
    def __init__(
        self,
        receipts: List[CreateReceiptRequestReceipts] = None,
    ):
        # 单据列表，不超过10条数据
        self.receipts = receipts

    def validate(self):
        if self.receipts:
            for k in self.receipts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receipts'] = []
        if self.receipts is not None:
            for k in self.receipts:
                result['receipts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receipts = []
        if m.get('receipts') is not None:
            for k in m.get('receipts'):
                temp_model = CreateReceiptRequestReceipts()
                self.receipts.append(temp_model.from_map(k))
        return self


class CreateReceiptResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # 数据唯一编号
        self.code = code
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
        if self.code is not None:
            result['code'] = self.code
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateReceiptResponseBody(TeaModel):
    def __init__(
        self,
        results: List[CreateReceiptResponseBodyResults] = None,
    ):
        # 结果列表
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = CreateReceiptResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class CreateReceiptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateReceiptResponseBody = None,
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
            temp_model = CreateReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReceiptHeaders(TeaModel):
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


class DeleteReceiptRequestReceipts(TeaModel):
    def __init__(
        self,
        code: str = None,
        delete_user_id: str = None,
        receipt_type: int = None,
    ):
        # 单据唯一编号
        self.code = code
        # 修改者工号
        self.delete_user_id = delete_user_id
        # 单据类型：1付款单，2收款单
        self.receipt_type = receipt_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.delete_user_id is not None:
            result['deleteUserId'] = self.delete_user_id
        if self.receipt_type is not None:
            result['receiptType'] = self.receipt_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('deleteUserId') is not None:
            self.delete_user_id = m.get('deleteUserId')
        if m.get('receiptType') is not None:
            self.receipt_type = m.get('receiptType')
        return self


class DeleteReceiptRequest(TeaModel):
    def __init__(
        self,
        receipts: List[DeleteReceiptRequestReceipts] = None,
    ):
        # 单据列表，最长不超过10条
        self.receipts = receipts

    def validate(self):
        if self.receipts:
            for k in self.receipts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receipts'] = []
        if self.receipts is not None:
            for k in self.receipts:
                result['receipts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receipts = []
        if m.get('receipts') is not None:
            for k in m.get('receipts'):
                temp_model = DeleteReceiptRequestReceipts()
                self.receipts.append(temp_model.from_map(k))
        return self


class DeleteReceiptResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # 数据唯一编号
        self.code = code
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
        if self.code is not None:
            result['code'] = self.code
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteReceiptResponseBody(TeaModel):
    def __init__(
        self,
        results: List[DeleteReceiptResponseBodyResults] = None,
    ):
        # 结果列表
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = DeleteReceiptResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DeleteReceiptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteReceiptResponseBody = None,
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
            temp_model = DeleteReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBookkeepingUserListHeaders(TeaModel):
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


class GetBookkeepingUserListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[str] = None,
    ):
        # staffId列表
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


class GetBookkeepingUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBookkeepingUserListResponseBody = None,
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
            temp_model = GetBookkeepingUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCategoryHeaders(TeaModel):
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


class GetCategoryRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # 类别code
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_dir: bool = None,
        name: str = None,
        parent_code: str = None,
        status: str = None,
        type: str = None,
    ):
        # 类别code
        self.code = code
        # 是否为目录
        self.is_dir = is_dir
        # 名称
        self.name = name
        # 父类别code
        self.parent_code = parent_code
        # 状态:valid,invalid,deleted
        self.status = status
        # 类型：income收入，expense支出
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent_code is not None:
            result['parentCode'] = self.parent_code
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentCode') is not None:
            self.parent_code = m.get('parentCode')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCategoryResponseBody = None,
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
            temp_model = GetCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerHeaders(TeaModel):
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


class GetCustomerRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # 客户code
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetCustomerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        description: str = None,
        name: str = None,
        status: str = None,
    ):
        # 客户Code
        self.code = code
        # 创建时间(单位MS)
        self.create_time = create_time
        # 客户描述
        self.description = description
        # 客户名称
        self.name = name
        # 状态：启用(valid), 停用(invalid), 删除(deleted)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomerResponseBody = None,
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
            temp_model = GetCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFinanceAccountHeaders(TeaModel):
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


class GetFinanceAccountRequest(TeaModel):
    def __init__(
        self,
        account_code: str = None,
    ):
        # 账户code
        self.account_code = account_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_code is not None:
            result['accountCode'] = self.account_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountCode') is not None:
            self.account_code = m.get('accountCode')
        return self


class GetFinanceAccountResponseBody(TeaModel):
    def __init__(
        self,
        account_code: str = None,
        account_id: str = None,
        account_name: str = None,
        account_remark: str = None,
        account_type: str = None,
        amount: str = None,
        create_time: int = None,
        creator: str = None,
    ):
        # 账户code
        self.account_code = account_code
        # 关联资金账户id
        self.account_id = account_id
        # 账户名称
        self.account_name = account_name
        # 备注
        self.account_remark = account_remark
        # 账户类型:ALIPAY, BANKCARD, CASH, WECHAT
        self.account_type = account_type
        # 账户总额，保留2位小数
        self.amount = amount
        # 创建时间
        self.create_time = create_time
        # 创建人工号
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_code is not None:
            result['accountCode'] = self.account_code
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_remark is not None:
            result['accountRemark'] = self.account_remark
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.amount is not None:
            result['amount'] = self.amount
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountCode') is not None:
            self.account_code = m.get('accountCode')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountRemark') is not None:
            self.account_remark = m.get('accountRemark')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        return self


class GetFinanceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFinanceAccountResponseBody = None,
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
            temp_model = GetFinanceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectHeaders(TeaModel):
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


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # 项目code
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        project_code: str = None,
        project_name: str = None,
        status: str = None,
    ):
        # 企业id
        self.corp_id = corp_id
        # 创建时间
        self.create_time = create_time
        # 创建人工号
        self.creator = creator
        # 项目描述
        self.description = description
        # 项目code
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 状态:valid, invalid, deleted
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectResponseBody = None,
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReceiptHeaders(TeaModel):
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


class GetReceiptRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        model_id: str = None,
    ):
        # 单据号
        self.code = code
        # 模型id
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class GetReceiptResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        model_id: str = None,
        source: str = None,
    ):
        # 数据来源于开放时，对应的微应用id
        self.app_id = app_id
        # 单据数据体json
        self.data = data
        # 数据模型id
        self.model_id = model_id
        # 数据来源：审批(approval)，开放接口(openapi)
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.data is not None:
            result['data'] = self.data
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class GetReceiptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetReceiptResponseBody = None,
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
            temp_model = GetReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupplierHeaders(TeaModel):
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


class GetSupplierRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # 供应商code
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetSupplierResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        description: str = None,
        name: str = None,
        status: str = None,
    ):
        # 供应商Code
        self.code = code
        # 创建时间(单位MS)
        self.create_time = create_time
        # 供应商描述
        self.description = description
        # 供应商名称
        self.name = name
        # 状态：启用(valid), 停用(invalid), 删除(deleted)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetSupplierResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSupplierResponseBody = None,
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
            temp_model = GetSupplierResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCategoryByPageHeaders(TeaModel):
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


class QueryCategoryByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10
        self.page_size = page_size
        # 类型：income收入，expense支出
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryCategoryByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_dir: bool = None,
        name: str = None,
        parent_code: str = None,
        status: str = None,
        type: str = None,
    ):
        # 类别code
        self.code = code
        # 是否为目录
        self.is_dir = is_dir
        # 名字
        self.name = name
        # 父类别code
        self.parent_code = parent_code
        # 状态:valid,invalid,deleted
        self.status = status
        # 类型:income收入，expense支出
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.parent_code is not None:
            result['parentCode'] = self.parent_code
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentCode') is not None:
            self.parent_code = m.get('parentCode')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryCategoryByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryCategoryByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # resultList
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QueryCategoryByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryCategoryByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCategoryByPageResponseBody = None,
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
            temp_model = QueryCategoryByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomerByPageHeaders(TeaModel):
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


class QueryCustomerByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryCustomerByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        description: str = None,
        name: str = None,
        status: str = None,
    ):
        # 客户Code
        self.code = code
        # 创建时间(单位MS)
        self.create_time = create_time
        # 客户描述
        self.description = description
        # 客户名称
        self.name = name
        # 状态：启用(valid), 停用(invalid), 删除(deleted)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryCustomerByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryCustomerByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # resultList
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QueryCustomerByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryCustomerByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCustomerByPageResponseBody = None,
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
            temp_model = QueryCustomerByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnterpriseAccountByPageHeaders(TeaModel):
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


class QueryEnterpriseAccountByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryEnterpriseAccountByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        account_code: str = None,
        account_id: str = None,
        account_name: str = None,
        account_remark: str = None,
        account_type: str = None,
        amount: str = None,
        create_time: int = None,
        creator: str = None,
    ):
        # 账户code
        self.account_code = account_code
        # 关联资金账号id
        self.account_id = account_id
        # 账户名称
        self.account_name = account_name
        # 备注
        self.account_remark = account_remark
        # 账户类型:ALIPAY, BANKCARD, CASH, WECHAT
        self.account_type = account_type
        # 账户总额，保留2位小数
        self.amount = amount
        # 创建时间
        self.create_time = create_time
        # 创建人工号
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_code is not None:
            result['accountCode'] = self.account_code
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_remark is not None:
            result['accountRemark'] = self.account_remark
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.amount is not None:
            result['amount'] = self.amount
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountCode') is not None:
            self.account_code = m.get('accountCode')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountRemark') is not None:
            self.account_remark = m.get('accountRemark')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        return self


class QueryEnterpriseAccountByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryEnterpriseAccountByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # resultList
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QueryEnterpriseAccountByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryEnterpriseAccountByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEnterpriseAccountByPageResponseBody = None,
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
            temp_model = QueryEnterpriseAccountByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectByPageHeaders(TeaModel):
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


class QueryProjectByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryProjectByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        project_code: str = None,
        project_name: str = None,
        status: str = None,
    ):
        # 企业id
        self.corp_id = corp_id
        # 创建时间
        self.create_time = create_time
        # 创建人工号
        self.creator = creator
        # 描述
        self.description = description
        # 项目code
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 状态: valid, invalid, deleted
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryProjectByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryProjectByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # resultList
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QueryProjectByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryProjectByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProjectByPageResponseBody = None,
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
            temp_model = QueryProjectByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReceiptsByPageHeaders(TeaModel):
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


class QueryReceiptsByPageRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        model_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        time_filter_field: str = None,
    ):
        # 检索结束时间，默认当前时间，离开始时间最长不超过180天
        self.end_time = end_time
        # 数据模型id
        self.model_id = model_id
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10，最大100
        self.page_size = page_size
        # 检索开始时间
        self.start_time = start_time
        # 检索排序时间类型：创建时间(gmt_create)，更新时间(gmt_modified)
        self.time_filter_field = time_filter_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.time_filter_field is not None:
            result['timeFilterField'] = self.time_filter_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timeFilterField') is not None:
            self.time_filter_field = m.get('timeFilterField')
        return self


class QueryReceiptsByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        model_id: str = None,
        source: str = None,
    ):
        # 数据来源于开放时，对应的微应用id
        self.app_id = app_id
        # 单据数据体json
        self.data = data
        # 模型id
        self.model_id = model_id
        # 数据来源：审批(approval)，开放接口(openapi)
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.data is not None:
            result['data'] = self.data
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class QueryReceiptsByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: str = None,
        list: List[QueryReceiptsByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # 数据列表
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QueryReceiptsByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryReceiptsByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryReceiptsByPageResponseBody = None,
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
            temp_model = QueryReceiptsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySupplierByPageHeaders(TeaModel):
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


class QuerySupplierByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 分页，从1开始
        self.page_number = page_number
        # 分页大小，默认10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QuerySupplierByPageResponseBodyList(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        description: str = None,
        name: str = None,
        status: str = None,
    ):
        # 供应商Code
        self.code = code
        # 创建时间(单位MS)
        self.create_time = create_time
        # 供应商描述
        self.description = description
        # 供应商名称
        self.name = name
        # 状态：启用(valid), 停用(invalid), 删除(deleted)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QuerySupplierByPageResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QuerySupplierByPageResponseBodyList] = None,
    ):
        # 是否还有更多数据
        self.has_more = has_more
        # resultList
        self.list = list

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = QuerySupplierByPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        return self


class QuerySupplierByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySupplierByPageResponseBody = None,
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
            temp_model = QuerySupplierByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReceiptHeaders(TeaModel):
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


class UpdateReceiptRequestReceipts(TeaModel):
    def __init__(
        self,
        amount: str = None,
        category_code: str = None,
        code: str = None,
        customer_code: str = None,
        enterprise_acount_code: str = None,
        occur_date: int = None,
        principal_id: str = None,
        project_code: str = None,
        receipt_type: int = None,
        remark: str = None,
        supplier_code: str = None,
        title: str = None,
        update_time: int = None,
        update_user_id: str = None,
    ):
        # 总金额，传空代表不修改
        self.amount = amount
        # 关联收支类别，传空代表不修改
        self.category_code = category_code
        # 单据唯一编号
        self.code = code
        # 关联客户code，传空代表不修改
        self.customer_code = customer_code
        # 关联企业账户code，传空代表不修改
        self.enterprise_acount_code = enterprise_acount_code
        # 业务发生时间，传空代表不修改
        self.occur_date = occur_date
        # 负责人工号，传空代表不修改
        self.principal_id = principal_id
        # 关联项目code，传空代表不修改
        self.project_code = project_code
        # 单据类型：1付款单，2收款单
        self.receipt_type = receipt_type
        # 备注，传空代表不修改
        self.remark = remark
        # 关联供应商code，传空代表不修改
        self.supplier_code = supplier_code
        # 单据标题，传空代表不修改
        self.title = title
        # 单据更新时间
        self.update_time = update_time
        # 修改者工号
        self.update_user_id = update_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.category_code is not None:
            result['categoryCode'] = self.category_code
        if self.code is not None:
            result['code'] = self.code
        if self.customer_code is not None:
            result['customerCode'] = self.customer_code
        if self.enterprise_acount_code is not None:
            result['enterpriseAcountCode'] = self.enterprise_acount_code
        if self.occur_date is not None:
            result['occurDate'] = self.occur_date
        if self.principal_id is not None:
            result['principalId'] = self.principal_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.receipt_type is not None:
            result['receiptType'] = self.receipt_type
        if self.remark is not None:
            result['remark'] = self.remark
        if self.supplier_code is not None:
            result['supplierCode'] = self.supplier_code
        if self.title is not None:
            result['title'] = self.title
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.update_user_id is not None:
            result['updateUserId'] = self.update_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('customerCode') is not None:
            self.customer_code = m.get('customerCode')
        if m.get('enterpriseAcountCode') is not None:
            self.enterprise_acount_code = m.get('enterpriseAcountCode')
        if m.get('occurDate') is not None:
            self.occur_date = m.get('occurDate')
        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('receiptType') is not None:
            self.receipt_type = m.get('receiptType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('supplierCode') is not None:
            self.supplier_code = m.get('supplierCode')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('updateUserId') is not None:
            self.update_user_id = m.get('updateUserId')
        return self


class UpdateReceiptRequest(TeaModel):
    def __init__(
        self,
        receipts: List[UpdateReceiptRequestReceipts] = None,
    ):
        # 单据列表 ，最长10
        self.receipts = receipts

    def validate(self):
        if self.receipts:
            for k in self.receipts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['receipts'] = []
        if self.receipts is not None:
            for k in self.receipts:
                result['receipts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receipts = []
        if m.get('receipts') is not None:
            for k in m.get('receipts'):
                temp_model = UpdateReceiptRequestReceipts()
                self.receipts.append(temp_model.from_map(k))
        return self


class UpdateReceiptResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # 数据唯一编号
        self.code = code
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
        if self.code is not None:
            result['code'] = self.code
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateReceiptResponseBody(TeaModel):
    def __init__(
        self,
        results: List[UpdateReceiptResponseBodyResults] = None,
    ):
        # 结果列表
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = UpdateReceiptResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class UpdateReceiptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateReceiptResponseBody = None,
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
            temp_model = UpdateReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


