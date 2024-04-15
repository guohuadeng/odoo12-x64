# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ApprovalListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ApprovalListResponseBodyDataApprovalNodes(TeaModel):
    def __init__(
        self,
        approval_time: str = None,
        approver_name: str = None,
        start_time: float = None,
        status: str = None,
    ):
        self.approval_time = approval_time
        self.approver_name = approver_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_time is not None:
            result['approvalTime'] = self.approval_time
        if self.approver_name is not None:
            result['approverName'] = self.approver_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approvalTime') is not None:
            self.approval_time = m.get('approvalTime')
        if m.get('approverName') is not None:
            self.approver_name = m.get('approverName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ApprovalListResponseBodyData(TeaModel):
    def __init__(
        self,
        approval_name: str = None,
        approval_nodes: List[ApprovalListResponseBodyDataApprovalNodes] = None,
        end_time: float = None,
        refuse_reason: str = None,
        seal_id_img: str = None,
        sponsor_account_name: str = None,
        start_time: float = None,
        status: str = None,
    ):
        self.approval_name = approval_name
        self.approval_nodes = approval_nodes
        self.end_time = end_time
        self.refuse_reason = refuse_reason
        self.seal_id_img = seal_id_img
        self.sponsor_account_name = sponsor_account_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.approval_nodes:
            for k in self.approval_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_name is not None:
            result['approvalName'] = self.approval_name
        result['approvalNodes'] = []
        if self.approval_nodes is not None:
            for k in self.approval_nodes:
                result['approvalNodes'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.refuse_reason is not None:
            result['refuseReason'] = self.refuse_reason
        if self.seal_id_img is not None:
            result['sealIdImg'] = self.seal_id_img
        if self.sponsor_account_name is not None:
            result['sponsorAccountName'] = self.sponsor_account_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approvalName') is not None:
            self.approval_name = m.get('approvalName')
        self.approval_nodes = []
        if m.get('approvalNodes') is not None:
            for k in m.get('approvalNodes'):
                temp_model = ApprovalListResponseBodyDataApprovalNodes()
                self.approval_nodes.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('refuseReason') is not None:
            self.refuse_reason = m.get('refuseReason')
        if m.get('sealIdImg') is not None:
            self.seal_id_img = m.get('sealIdImg')
        if m.get('sponsorAccountName') is not None:
            self.sponsor_account_name = m.get('sponsorAccountName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ApprovalListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ApprovalListResponseBodyData] = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ApprovalListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ApprovalListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApprovalListResponseBody = None,
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
            temp_model = ApprovalListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCorpAuthHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CancelCorpAuthRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelCorpAuthResponseBody(TeaModel):
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


class CancelCorpAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelCorpAuthResponseBody = None,
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
            temp_model = CancelCorpAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChannelOrdersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ChannelOrdersRequest(TeaModel):
    def __init__(
        self,
        item_code: str = None,
        item_name: str = None,
        order_create_time: float = None,
        order_id: str = None,
        pay_fee: float = None,
        quantity: float = None,
    ):
        # 商品id
        self.item_code = item_code
        # 商品名称
        self.item_name = item_name
        # 下单时间
        self.order_create_time = order_create_time
        # isv方的订单Id（用于幂等，请保证唯一性）
        self.order_id = order_id
        # 支付金额（以分为单位，仅作记录，不作为凭证）
        self.pay_fee = pay_fee
        # 购买数量
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_code is not None:
            result['itemCode'] = self.item_code
        if self.item_name is not None:
            result['itemName'] = self.item_name
        if self.order_create_time is not None:
            result['orderCreateTime'] = self.order_create_time
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.pay_fee is not None:
            result['payFee'] = self.pay_fee
        if self.quantity is not None:
            result['quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemCode') is not None:
            self.item_code = m.get('itemCode')
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')
        if m.get('orderCreateTime') is not None:
            self.order_create_time = m.get('orderCreateTime')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('payFee') is not None:
            self.pay_fee = m.get('payFee')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        return self


class ChannelOrdersResponseBody(TeaModel):
    def __init__(
        self,
        esign_order_id: str = None,
    ):
        self.esign_order_id = esign_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esign_order_id is not None:
            result['esignOrderId'] = self.esign_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esignOrderId') is not None:
            self.esign_order_id = m.get('esignOrderId')
        return self


class ChannelOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChannelOrdersResponseBody = None,
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
            temp_model = ChannelOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CorpRealnameHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CorpRealnameRequest(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        user_id: str = None,
    ):
        self.redirect_url = redirect_url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['redirectUrl'] = self.redirect_url
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('redirectUrl') is not None:
            self.redirect_url = m.get('redirectUrl')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CorpRealnameResponseBody(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        task_id: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CorpRealnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CorpRealnameResponseBody = None,
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
            temp_model = CorpRealnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevelopersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class CreateDevelopersRequest(TeaModel):
    def __init__(
        self,
        notice_url: str = None,
    ):
        self.notice_url = notice_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_url is not None:
            result['noticeUrl'] = self.notice_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('noticeUrl') is not None:
            self.notice_url = m.get('noticeUrl')
        return self


class CreateDevelopersResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateDevelopersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevelopersResponseBody = None,
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
            temp_model = CreateDevelopersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProcessHeaders(TeaModel):
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


class CreateProcessRequestCcs(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_name: str = None,
        account_type: str = None,
        org_name: str = None,
        user_id: str = None,
    ):
        self.account = account
        self.account_name = account_name
        self.account_type = account_type
        self.org_name = org_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateProcessRequestFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_type: int = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.file_type = file_type

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
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class CreateProcessRequestParticipantsSignPosListSignDate(TeaModel):
    def __init__(
        self,
        format: str = None,
    ):
        # 签署区时间格式， 支持yyyy/MM/dd, yyyy-MM-dd, yyyy年MM月dd日
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['format'] = self.format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')
        return self


class CreateProcessRequestParticipantsSignPosList(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        is_cross_page: bool = None,
        need_sign_date: bool = None,
        page: str = None,
        sign_date: CreateProcessRequestParticipantsSignPosListSignDate = None,
        sign_requirement: str = None,
        x: float = None,
        y: float = None,
    ):
        # 文件id
        self.file_id = file_id
        # 是否为骑缝章
        self.is_cross_page = is_cross_page
        # 是否需要显示签署时间
        self.need_sign_date = need_sign_date
        # 签署区页码
        self.page = page
        self.sign_date = sign_date
        # 签署要求,1-企业章 2-经办人
        self.sign_requirement = sign_requirement
        # 签署区x坐标
        self.x = x
        # 签署区y坐标
        self.y = y

    def validate(self):
        if self.sign_date:
            self.sign_date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.is_cross_page is not None:
            result['isCrossPage'] = self.is_cross_page
        if self.need_sign_date is not None:
            result['needSignDate'] = self.need_sign_date
        if self.page is not None:
            result['page'] = self.page
        if self.sign_date is not None:
            result['signDate'] = self.sign_date.to_map()
        if self.sign_requirement is not None:
            result['signRequirement'] = self.sign_requirement
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('isCrossPage') is not None:
            self.is_cross_page = m.get('isCrossPage')
        if m.get('needSignDate') is not None:
            self.need_sign_date = m.get('needSignDate')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('signDate') is not None:
            temp_model = CreateProcessRequestParticipantsSignPosListSignDate()
            self.sign_date = temp_model.from_map(m['signDate'])
        if m.get('signRequirement') is not None:
            self.sign_requirement = m.get('signRequirement')
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class CreateProcessRequestParticipants(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_name: str = None,
        account_type: str = None,
        org_name: str = None,
        sign_order: int = None,
        sign_pos_list: List[CreateProcessRequestParticipantsSignPosList] = None,
        sign_requirements: str = None,
        user_id: str = None,
    ):
        self.account = account
        self.account_name = account_name
        self.account_type = account_type
        self.org_name = org_name
        self.sign_order = sign_order
        # 参与方签署位置信息列表
        self.sign_pos_list = sign_pos_list
        self.sign_requirements = sign_requirements
        self.user_id = user_id

    def validate(self):
        if self.sign_pos_list:
            for k in self.sign_pos_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.sign_order is not None:
            result['signOrder'] = self.sign_order
        result['signPosList'] = []
        if self.sign_pos_list is not None:
            for k in self.sign_pos_list:
                result['signPosList'].append(k.to_map() if k else None)
        if self.sign_requirements is not None:
            result['signRequirements'] = self.sign_requirements
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('signOrder') is not None:
            self.sign_order = m.get('signOrder')
        self.sign_pos_list = []
        if m.get('signPosList') is not None:
            for k in m.get('signPosList'):
                temp_model = CreateProcessRequestParticipantsSignPosList()
                self.sign_pos_list.append(temp_model.from_map(k))
        if m.get('signRequirements') is not None:
            self.sign_requirements = m.get('signRequirements')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateProcessRequestSourceInfo(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        show_text: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.show_text = show_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.show_text is not None:
            result['showText'] = self.show_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('showText') is not None:
            self.show_text = m.get('showText')
        return self


class CreateProcessRequest(TeaModel):
    def __init__(
        self,
        ccs: List[CreateProcessRequestCcs] = None,
        files: List[CreateProcessRequestFiles] = None,
        initiator_user_id: str = None,
        participants: List[CreateProcessRequestParticipants] = None,
        redirect_url: str = None,
        sign_end_time: int = None,
        source_info: CreateProcessRequestSourceInfo = None,
        task_name: str = None,
    ):
        self.ccs = ccs
        self.files = files
        self.initiator_user_id = initiator_user_id
        self.participants = participants
        self.redirect_url = redirect_url
        self.sign_end_time = sign_end_time
        self.source_info = source_info
        self.task_name = task_name

    def validate(self):
        if self.ccs:
            for k in self.ccs:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.participants:
            for k in self.participants:
                if k:
                    k.validate()
        if self.source_info:
            self.source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ccs'] = []
        if self.ccs is not None:
            for k in self.ccs:
                result['ccs'].append(k.to_map() if k else None)
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.initiator_user_id is not None:
            result['initiatorUserId'] = self.initiator_user_id
        result['participants'] = []
        if self.participants is not None:
            for k in self.participants:
                result['participants'].append(k.to_map() if k else None)
        if self.redirect_url is not None:
            result['redirectUrl'] = self.redirect_url
        if self.sign_end_time is not None:
            result['signEndTime'] = self.sign_end_time
        if self.source_info is not None:
            result['sourceInfo'] = self.source_info.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ccs = []
        if m.get('ccs') is not None:
            for k in m.get('ccs'):
                temp_model = CreateProcessRequestCcs()
                self.ccs.append(temp_model.from_map(k))
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = CreateProcessRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('initiatorUserId') is not None:
            self.initiator_user_id = m.get('initiatorUserId')
        self.participants = []
        if m.get('participants') is not None:
            for k in m.get('participants'):
                temp_model = CreateProcessRequestParticipants()
                self.participants.append(temp_model.from_map(k))
        if m.get('redirectUrl') is not None:
            self.redirect_url = m.get('redirectUrl')
        if m.get('signEndTime') is not None:
            self.sign_end_time = m.get('signEndTime')
        if m.get('sourceInfo') is not None:
            temp_model = CreateProcessRequestSourceInfo()
            self.source_info = temp_model.from_map(m['sourceInfo'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class CreateProcessResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProcessResponseBody = None,
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
            temp_model = CreateProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachsApprovalHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        tsign_open_app_id: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
        self.tsign_open_app_id = tsign_open_app_id
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.tsign_open_app_id is not None:
            result['tsignOpenAppId'] = self.tsign_open_app_id
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('tsignOpenAppId') is not None:
            self.tsign_open_app_id = m.get('tsignOpenAppId')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetAttachsApprovalResponseBodyDataFiles(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        original_file_url: str = None,
        sign_finish_file_url: str = None,
    ):
        self.file_name = file_name
        self.original_file_url = original_file_url
        self.sign_finish_file_url = sign_finish_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.original_file_url is not None:
            result['originalFileUrl'] = self.original_file_url
        if self.sign_finish_file_url is not None:
            result['signFinishFileUrl'] = self.sign_finish_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('originalFileUrl') is not None:
            self.original_file_url = m.get('originalFileUrl')
        if m.get('signFinishFileUrl') is not None:
            self.sign_finish_file_url = m.get('signFinishFileUrl')
        return self


class GetAttachsApprovalResponseBodyData(TeaModel):
    def __init__(
        self,
        files: List[GetAttachsApprovalResponseBodyDataFiles] = None,
        flow_id: str = None,
        status: str = None,
    ):
        self.files = files
        self.flow_id = flow_id
        self.status = status

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.flow_id is not None:
            result['flowId'] = self.flow_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GetAttachsApprovalResponseBodyDataFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetAttachsApprovalResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetAttachsApprovalResponseBodyData] = None,
    ):
        # Id of the request
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetAttachsApprovalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAttachsApprovalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAttachsApprovalResponseBody = None,
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
            temp_model = GetAttachsApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthUrlHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetAuthUrlRequest(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
    ):
        self.redirect_url = redirect_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['redirectUrl'] = self.redirect_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('redirectUrl') is not None:
            self.redirect_url = m.get('redirectUrl')
        return self


class GetAuthUrlResponseBody(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        task_id: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetAuthUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthUrlResponseBody = None,
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
            temp_model = GetAuthUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContractMarginHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetContractMarginResponseBody(TeaModel):
    def __init__(
        self,
        margin: float = None,
    ):
        self.margin = margin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.margin is not None:
            result['margin'] = self.margin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('margin') is not None:
            self.margin = m.get('margin')
        return self


class GetContractMarginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetContractMarginResponseBody = None,
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
            temp_model = GetContractMarginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpConsoleHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCorpConsoleResponseBody(TeaModel):
    def __init__(
        self,
        org_console_url: str = None,
    ):
        self.org_console_url = org_console_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_console_url is not None:
            result['orgConsoleUrl'] = self.org_console_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orgConsoleUrl') is not None:
            self.org_console_url = m.get('orgConsoleUrl')
        return self


class GetCorpConsoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpConsoleResponseBody = None,
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
            temp_model = GetCorpConsoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetCorpInfoResponseBody(TeaModel):
    def __init__(
        self,
        is_real_name: str = None,
        org_real_name: str = None,
    ):
        self.is_real_name = is_real_name
        self.org_real_name = org_real_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_real_name is not None:
            result['isRealName'] = self.is_real_name
        if self.org_real_name is not None:
            result['orgRealName'] = self.org_real_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isRealName') is not None:
            self.is_real_name = m.get('isRealName')
        if m.get('orgRealName') is not None:
            self.org_real_name = m.get('orgRealName')
        return self


class GetCorpInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpInfoResponseBody = None,
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
            temp_model = GetCorpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteUrlHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetExecuteUrlRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        sign_container: int = None,
        task_id: str = None,
    ):
        self.account = account
        self.sign_container = sign_container
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.sign_container is not None:
            result['signContainer'] = self.sign_container
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('signContainer') is not None:
            self.sign_container = m.get('signContainer')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetExecuteUrlResponseBody(TeaModel):
    def __init__(
        self,
        long_url: str = None,
        mobile_url: str = None,
        pc_url: str = None,
        short_url: str = None,
    ):
        self.long_url = long_url
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.long_url is not None:
            result['longUrl'] = self.long_url
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.short_url is not None:
            result['shortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('longUrl') is not None:
            self.long_url = m.get('longUrl')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('shortUrl') is not None:
            self.short_url = m.get('shortUrl')
        return self


class GetExecuteUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExecuteUrlResponseBody = None,
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
            temp_model = GetExecuteUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetFileInfoResponseBody(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        file_id: str = None,
        name: str = None,
        pdf_total_pages: int = None,
        size: int = None,
        status: int = None,
    ):
        self.download_url = download_url
        self.file_id = file_id
        self.name = name
        self.pdf_total_pages = pdf_total_pages
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.name is not None:
            result['name'] = self.name
        if self.pdf_total_pages is not None:
            result['pdfTotalPages'] = self.pdf_total_pages
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pdfTotalPages') is not None:
            self.pdf_total_pages = m.get('pdfTotalPages')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetFileInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileInfoResponseBody = None,
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
            temp_model = GetFileInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileUploadUrlHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetFileUploadUrlRequest(TeaModel):
    def __init__(
        self,
        content_md_5: str = None,
        content_type: str = None,
        convert_2pdf: bool = None,
        file_name: str = None,
        file_size: int = None,
    ):
        self.content_md_5 = content_md_5
        self.content_type = content_type
        self.convert_2pdf = convert_2pdf
        self.file_name = file_name
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_md_5 is not None:
            result['contentMd5'] = self.content_md_5
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.convert_2pdf is not None:
            result['convert2Pdf'] = self.convert_2pdf
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentMd5') is not None:
            self.content_md_5 = m.get('contentMd5')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('convert2Pdf') is not None:
            self.convert_2pdf = m.get('convert2Pdf')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class GetFileUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        upload_url: str = None,
    ):
        self.file_id = file_id
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')
        return self


class GetFileUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileUploadUrlResponseBody = None,
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
            temp_model = GetFileUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetFlowDetailResponseBodyLogs(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        operate_description: str = None,
        operate_time: float = None,
        operator_account_name: str = None,
    ):
        self.log_type = log_type
        self.operate_description = operate_description
        self.operate_time = operate_time
        self.operator_account_name = operator_account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['logType'] = self.log_type
        if self.operate_description is not None:
            result['operateDescription'] = self.operate_description
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.operator_account_name is not None:
            result['operatorAccountName'] = self.operator_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logType') is not None:
            self.log_type = m.get('logType')
        if m.get('operateDescription') is not None:
            self.operate_description = m.get('operateDescription')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('operatorAccountName') is not None:
            self.operator_account_name = m.get('operatorAccountName')
        return self


class GetFlowDetailResponseBody(TeaModel):
    def __init__(
        self,
        business_scene: str = None,
        flow_status: float = None,
        initiator_authorized_name: str = None,
        initiator_name: str = None,
        logs: List[GetFlowDetailResponseBodyLogs] = None,
    ):
        self.business_scene = business_scene
        self.flow_status = flow_status
        self.initiator_authorized_name = initiator_authorized_name
        self.initiator_name = initiator_name
        self.logs = logs

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_scene is not None:
            result['businessScene'] = self.business_scene
        if self.flow_status is not None:
            result['flowStatus'] = self.flow_status
        if self.initiator_authorized_name is not None:
            result['initiatorAuthorizedName'] = self.initiator_authorized_name
        if self.initiator_name is not None:
            result['initiatorName'] = self.initiator_name
        result['logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessScene') is not None:
            self.business_scene = m.get('businessScene')
        if m.get('flowStatus') is not None:
            self.flow_status = m.get('flowStatus')
        if m.get('initiatorAuthorizedName') is not None:
            self.initiator_authorized_name = m.get('initiatorAuthorizedName')
        if m.get('initiatorName') is not None:
            self.initiator_name = m.get('initiatorName')
        self.logs = []
        if m.get('logs') is not None:
            for k in m.get('logs'):
                temp_model = GetFlowDetailResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class GetFlowDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFlowDetailResponseBody = None,
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
            temp_model = GetFlowDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowDocsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetFlowDocsResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_url: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.file_url = file_url

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
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        return self


class GetFlowDocsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetFlowDocsResponseBodyData] = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetFlowDocsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetFlowDocsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFlowDocsResponseBody = None,
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
            temp_model = GetFlowDocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIsvStatusHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetIsvStatusResponseBody(TeaModel):
    def __init__(
        self,
        auth_status: str = None,
        install_status: str = None,
    ):
        self.auth_status = auth_status
        self.install_status = install_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_status is not None:
            result['authStatus'] = self.auth_status
        if self.install_status is not None:
            result['installStatus'] = self.install_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authStatus') is not None:
            self.auth_status = m.get('authStatus')
        if m.get('installStatus') is not None:
            self.install_status = m.get('installStatus')
        return self


class GetIsvStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIsvStatusResponseBody = None,
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
            temp_model = GetIsvStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetSignDetailResponseBodySigners(TeaModel):
    def __init__(
        self,
        sign_status: float = None,
        signer_name: str = None,
    ):
        self.sign_status = sign_status
        self.signer_name = signer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_status is not None:
            result['signStatus'] = self.sign_status
        if self.signer_name is not None:
            result['signerName'] = self.signer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('signStatus') is not None:
            self.sign_status = m.get('signStatus')
        if m.get('signerName') is not None:
            self.signer_name = m.get('signerName')
        return self


class GetSignDetailResponseBody(TeaModel):
    def __init__(
        self,
        business_scene: str = None,
        flow_status: float = None,
        signers: List[GetSignDetailResponseBodySigners] = None,
    ):
        self.business_scene = business_scene
        self.flow_status = flow_status
        self.signers = signers

    def validate(self):
        if self.signers:
            for k in self.signers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_scene is not None:
            result['businessScene'] = self.business_scene
        if self.flow_status is not None:
            result['flowStatus'] = self.flow_status
        result['signers'] = []
        if self.signers is not None:
            for k in self.signers:
                result['signers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessScene') is not None:
            self.business_scene = m.get('businessScene')
        if m.get('flowStatus') is not None:
            self.flow_status = m.get('flowStatus')
        self.signers = []
        if m.get('signers') is not None:
            for k in m.get('signers'):
                temp_model = GetSignDetailResponseBodySigners()
                self.signers.append(temp_model.from_map(k))
        return self


class GetSignDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignDetailResponseBody = None,
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
            temp_model = GetSignDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GetUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        is_real_name: str = None,
        user_real_name: str = None,
    ):
        self.is_real_name = is_real_name
        self.user_real_name = user_real_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_real_name is not None:
            result['isRealName'] = self.is_real_name
        if self.user_real_name is not None:
            result['userRealName'] = self.user_real_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isRealName') is not None:
            self.is_real_name = m.get('isRealName')
        if m.get('userRealName') is not None:
            self.user_real_name = m.get('userRealName')
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserInfoResponseBody = None,
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
            temp_model = GetUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessStartHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ProcessStartRequestCcs(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_name: str = None,
        account_type: str = None,
        org_name: str = None,
        user_id: str = None,
    ):
        # OUTER_USER必填
        self.account = account
        # OUTER_USER必填
        self.account_name = account_name
        # 用户类型（"DING_USER":钉钉用户，"OUTER_USER":外部用户）
        self.account_type = account_type
        # 发给企业方必填
        self.org_name = org_name
        # DING_USER必填
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ProcessStartRequestFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ProcessStartRequestParticipants(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_name: str = None,
        account_type: str = None,
        org_name: str = None,
        sign_requirements: str = None,
        user_id: str = None,
    ):
        # OUTER_USER必填
        self.account = account
        # OUTER_USER必填
        self.account_name = account_name
        # 用户类型（"DING_USER":钉钉用户，"OUTER_USER":外部用户）
        self.account_type = account_type
        # OUTER_USER需要盖企业章必填(如果不传，默认会赋值当前企业名称)
        self.org_name = org_name
        # 签署印章类型（1：企业章 2：个人章  1,2：个人和企业章）
        self.sign_requirements = sign_requirements
        # DING_USER必填
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.sign_requirements is not None:
            result['signRequirements'] = self.sign_requirements
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('signRequirements') is not None:
            self.sign_requirements = m.get('signRequirements')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ProcessStartRequestSourceInfo(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        show_text: str = None,
    ):
        # 移动端跳转地址
        self.mobile_url = mobile_url
        # pc端跳转地址
        self.pc_url = pc_url
        # 展示文案
        self.show_text = show_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.show_text is not None:
            result['showText'] = self.show_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('showText') is not None:
            self.show_text = m.get('showText')
        return self


class ProcessStartRequest(TeaModel):
    def __init__(
        self,
        auto_start: str = None,
        ccs: List[ProcessStartRequestCcs] = None,
        files: List[ProcessStartRequestFiles] = None,
        initiator_user_id: str = None,
        participants: List[ProcessStartRequestParticipants] = None,
        redirect_url: str = None,
        source_info: ProcessStartRequestSourceInfo = None,
        task_name: str = None,
    ):
        # 是否自动发起
        self.auto_start = auto_start
        # 抄送人列表
        self.ccs = ccs
        # 文件列表
        self.files = files
        # 发起方userId
        self.initiator_user_id = initiator_user_id
        # 参与方列表
        self.participants = participants
        # 回跳地址
        self.redirect_url = redirect_url
        # 来源信息(目前支持传入审批信息和跳转地址)
        self.source_info = source_info
        # 任务名称（默认文件名）
        self.task_name = task_name

    def validate(self):
        if self.ccs:
            for k in self.ccs:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.participants:
            for k in self.participants:
                if k:
                    k.validate()
        if self.source_info:
            self.source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['autoStart'] = self.auto_start
        result['ccs'] = []
        if self.ccs is not None:
            for k in self.ccs:
                result['ccs'].append(k.to_map() if k else None)
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.initiator_user_id is not None:
            result['initiatorUserId'] = self.initiator_user_id
        result['participants'] = []
        if self.participants is not None:
            for k in self.participants:
                result['participants'].append(k.to_map() if k else None)
        if self.redirect_url is not None:
            result['redirectUrl'] = self.redirect_url
        if self.source_info is not None:
            result['sourceInfo'] = self.source_info.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoStart') is not None:
            self.auto_start = m.get('autoStart')
        self.ccs = []
        if m.get('ccs') is not None:
            for k in m.get('ccs'):
                temp_model = ProcessStartRequestCcs()
                self.ccs.append(temp_model.from_map(k))
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ProcessStartRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('initiatorUserId') is not None:
            self.initiator_user_id = m.get('initiatorUserId')
        self.participants = []
        if m.get('participants') is not None:
            for k in m.get('participants'):
                temp_model = ProcessStartRequestParticipants()
                self.participants.append(temp_model.from_map(k))
        if m.get('redirectUrl') is not None:
            self.redirect_url = m.get('redirectUrl')
        if m.get('sourceInfo') is not None:
            temp_model = ProcessStartRequestSourceInfo()
            self.source_info = temp_model.from_map(m['sourceInfo'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class ProcessStartResponseBody(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        task_id: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ProcessStartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessStartResponseBody = None,
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
            temp_model = ProcessStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResaleOrderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class ResaleOrderRequest(TeaModel):
    def __init__(
        self,
        order_create_time: float = None,
        order_id: str = None,
        quantity: float = None,
        service_start_time: float = None,
        service_stop_time: float = None,
    ):
        # 下单时间
        self.order_create_time = order_create_time
        # isv方的订单Id（用于幂等，请保证唯一性）
        self.order_id = order_id
        # 购买数量（电子合同份数）
        self.quantity = quantity
        # 合同生效起始时间
        self.service_start_time = service_start_time
        # 合同失效截止日期，默认有效时间一年
        self.service_stop_time = service_stop_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_create_time is not None:
            result['orderCreateTime'] = self.order_create_time
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.service_start_time is not None:
            result['serviceStartTime'] = self.service_start_time
        if self.service_stop_time is not None:
            result['serviceStopTime'] = self.service_stop_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderCreateTime') is not None:
            self.order_create_time = m.get('orderCreateTime')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('serviceStartTime') is not None:
            self.service_start_time = m.get('serviceStartTime')
        if m.get('serviceStopTime') is not None:
            self.service_stop_time = m.get('serviceStopTime')
        return self


class ResaleOrderResponseBody(TeaModel):
    def __init__(
        self,
        esign_order_id: str = None,
    ):
        self.esign_order_id = esign_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esign_order_id is not None:
            result['esignOrderId'] = self.esign_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esignOrderId') is not None:
            self.esign_order_id = m.get('esignOrderId')
        return self


class ResaleOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResaleOrderResponseBody = None,
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
            temp_model = ResaleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UsersRealnameHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        service_group: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.service_group = service_group
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
        if self.service_group is not None:
            result['serviceGroup'] = self.service_group
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('serviceGroup') is not None:
            self.service_group = m.get('serviceGroup')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class UsersRealnameRequest(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        user_id: str = None,
    ):
        self.redirect_url = redirect_url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['redirectUrl'] = self.redirect_url
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('redirectUrl') is not None:
            self.redirect_url = m.get('redirectUrl')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UsersRealnameResponseBody(TeaModel):
    def __init__(
        self,
        mobile_url: str = None,
        pc_url: str = None,
        task_id: str = None,
    ):
        self.mobile_url = mobile_url
        self.pc_url = pc_url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UsersRealnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UsersRealnameResponseBody = None,
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
            temp_model = UsersRealnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


