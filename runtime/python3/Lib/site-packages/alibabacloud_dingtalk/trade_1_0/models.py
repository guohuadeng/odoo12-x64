# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CheckOpportunityResultHeaders(TeaModel):
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


class CheckOpportunityResultRequest(TeaModel):
    def __init__(
        self,
        belong_to_phone_num: str = None,
        contact_phone_num: str = None,
        corp_id: str = None,
        dept_id: int = None,
        market_code: str = None,
    ):
        # belongToPhoneNum
        self.belong_to_phone_num = belong_to_phone_num
        # contactPhoneNum
        self.contact_phone_num = contact_phone_num
        # corpId
        self.corp_id = corp_id
        # deptId
        self.dept_id = dept_id
        # marketCode
        self.market_code = market_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belong_to_phone_num is not None:
            result['belongToPhoneNum'] = self.belong_to_phone_num
        if self.contact_phone_num is not None:
            result['contactPhoneNum'] = self.contact_phone_num
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.market_code is not None:
            result['marketCode'] = self.market_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('belongToPhoneNum') is not None:
            self.belong_to_phone_num = m.get('belongToPhoneNum')
        if m.get('contactPhoneNum') is not None:
            self.contact_phone_num = m.get('contactPhoneNum')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('marketCode') is not None:
            self.market_code = m.get('marketCode')
        return self


class CheckOpportunityResultResponseBody(TeaModel):
    def __init__(
        self,
        biz_success: bool = None,
    ):
        # success
        self.biz_success = biz_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_success is not None:
            result['bizSuccess'] = self.biz_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizSuccess') is not None:
            self.biz_success = m.get('bizSuccess')
        return self


class CheckOpportunityResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckOpportunityResultResponseBody = None,
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
            temp_model = CheckOpportunityResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOpportunityHeaders(TeaModel):
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


class CreateOpportunityRequest(TeaModel):
    def __init__(
        self,
        belong_to_phone_num: str = None,
        contact_phone_num: str = None,
        corp_id: str = None,
        dept_id: int = None,
        market_code: str = None,
    ):
        # 归属人电话号码
        self.belong_to_phone_num = belong_to_phone_num
        # 联系人电话
        self.contact_phone_num = contact_phone_num
        # 企业CorpId
        self.corp_id = corp_id
        # 部门Id
        self.dept_id = dept_id
        # 商品码
        self.market_code = market_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belong_to_phone_num is not None:
            result['belongToPhoneNum'] = self.belong_to_phone_num
        if self.contact_phone_num is not None:
            result['contactPhoneNum'] = self.contact_phone_num
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.market_code is not None:
            result['marketCode'] = self.market_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('belongToPhoneNum') is not None:
            self.belong_to_phone_num = m.get('belongToPhoneNum')
        if m.get('contactPhoneNum') is not None:
            self.contact_phone_num = m.get('contactPhoneNum')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('marketCode') is not None:
            self.market_code = m.get('marketCode')
        return self


class CreateOpportunityResponse(TeaModel):
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


class QueryTradeOrderHeaders(TeaModel):
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


class QueryTradeOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        outer_order_id: str = None,
    ):
        # 内部订单号
        self.order_id = order_id
        # 外部订单号
        self.outer_order_id = outer_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.outer_order_id is not None:
            result['outerOrderId'] = self.outer_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('outerOrderId') is not None:
            self.outer_order_id = m.get('outerOrderId')
        return self


class QueryTradeOrderResponseBody(TeaModel):
    def __init__(
        self,
        article_code: str = None,
        article_item_code: str = None,
        article_item_name: str = None,
        article_name: str = None,
        close_time: int = None,
        create_time: int = None,
        fee: int = None,
        isv_crop_id: str = None,
        order_id: int = None,
        outer_order_id: str = None,
        pay_fee: int = None,
        pay_time: int = None,
        quantity: int = None,
        refund_time: int = None,
        status: int = None,
    ):
        # 商品编码
        self.article_code = article_code
        # 规格编码
        self.article_item_code = article_item_code
        # 规格名称
        self.article_item_name = article_item_name
        # 商品名称
        self.article_name = article_name
        # 订单关闭时间（单位：ms）
        self.close_time = close_time
        # 订单创建时间（单位：ms）
        self.create_time = create_time
        # 原价（单位：分）
        self.fee = fee
        # ISV的组织ID
        self.isv_crop_id = isv_crop_id
        # 内部订单号
        self.order_id = order_id
        # 外部订单号
        self.outer_order_id = outer_order_id
        # 实际支付的价格（单位：分）
        self.pay_fee = pay_fee
        # 订单支付时间（单位：ms）
        self.pay_time = pay_time
        # 商品数量
        self.quantity = quantity
        # 订单退款时间（单位：ms）
        self.refund_time = refund_time
        # 订单状态：-1表示已关闭、0表示未支付、1表示已支付、2表示已退款
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_code is not None:
            result['articleCode'] = self.article_code
        if self.article_item_code is not None:
            result['articleItemCode'] = self.article_item_code
        if self.article_item_name is not None:
            result['articleItemName'] = self.article_item_name
        if self.article_name is not None:
            result['articleName'] = self.article_name
        if self.close_time is not None:
            result['closeTime'] = self.close_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.fee is not None:
            result['fee'] = self.fee
        if self.isv_crop_id is not None:
            result['isvCropId'] = self.isv_crop_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.outer_order_id is not None:
            result['outerOrderId'] = self.outer_order_id
        if self.pay_fee is not None:
            result['payFee'] = self.pay_fee
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.refund_time is not None:
            result['refundTime'] = self.refund_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleCode') is not None:
            self.article_code = m.get('articleCode')
        if m.get('articleItemCode') is not None:
            self.article_item_code = m.get('articleItemCode')
        if m.get('articleItemName') is not None:
            self.article_item_name = m.get('articleItemName')
        if m.get('articleName') is not None:
            self.article_name = m.get('articleName')
        if m.get('closeTime') is not None:
            self.close_time = m.get('closeTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('fee') is not None:
            self.fee = m.get('fee')
        if m.get('isvCropId') is not None:
            self.isv_crop_id = m.get('isvCropId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('outerOrderId') is not None:
            self.outer_order_id = m.get('outerOrderId')
        if m.get('payFee') is not None:
            self.pay_fee = m.get('payFee')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('refundTime') is not None:
            self.refund_time = m.get('refundTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryTradeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeOrderResponseBody = None,
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
            temp_model = QueryTradeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


