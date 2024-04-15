# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddCityCarApplyHeaders(TeaModel):
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


class AddCityCarApplyRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        city: str = None,
        corp_id: str = None,
        date: str = None,
        finished_date: str = None,
        project_code: str = None,
        project_name: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
        times_total: int = None,
        times_type: int = None,
        times_used: int = None,
        title: str = None,
        user_id: str = None,
    ):
        # 出差事由
        self.cause = cause
        # 用车城市
        self.city = city
        # 第三方企业ID
        self.corp_id = corp_id
        # 用车时间，按天管控，比如传值2021-03-18 20:26:56表示2021-03-18当天可用车，跨天情况配合finishedDate参数使用
        self.date = date
        # 用车截止时间，按天管控，比如date传值2021-03-18 20:26:56、finished_date传值2021-03-30 20:26:56表示2021-03-18(含)到2021-03-30(含)之间可用车，该参数不传值情况使用date作为用车截止时间；
        self.finished_date = finished_date
        # 审批单关联的项目code
        self.project_code = project_code
        # 审批单关联的项目名
        self.project_name = project_name
        # 审批单状态：0-申请，1-同意，2-拒绝
        self.status = status
        # 三方审批单ID
        self.third_part_apply_id = third_part_apply_id
        # 审批单关联的三方成本中心ID
        self.third_part_cost_center_id = third_part_cost_center_id
        # 审批单关联的三方发票抬头ID
        self.third_part_invoice_id = third_part_invoice_id
        # 审批单可用总次数
        self.times_total = times_total
        # 审批单可用次数类型：1-次数不限制，2-用户可指定次数，3-管理员限制次数；如果企业没有限制审批单使用次数的需求，这个参数传1(次数不限制)，同时times_total和times_used都传0即可
        self.times_type = times_type
        # 审批单已用次数
        self.times_used = times_used
        # 审批单标题
        self.title = title
        # 发起审批的第三方员工ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['cause'] = self.cause
        if self.city is not None:
            result['city'] = self.city
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.date is not None:
            result['date'] = self.date
        if self.finished_date is not None:
            result['finishedDate'] = self.finished_date
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.status is not None:
            result['status'] = self.status
        if self.third_part_apply_id is not None:
            result['thirdPartApplyId'] = self.third_part_apply_id
        if self.third_part_cost_center_id is not None:
            result['thirdPartCostCenterId'] = self.third_part_cost_center_id
        if self.third_part_invoice_id is not None:
            result['thirdPartInvoiceId'] = self.third_part_invoice_id
        if self.times_total is not None:
            result['timesTotal'] = self.times_total
        if self.times_type is not None:
            result['timesType'] = self.times_type
        if self.times_used is not None:
            result['timesUsed'] = self.times_used
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cause') is not None:
            self.cause = m.get('cause')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('finishedDate') is not None:
            self.finished_date = m.get('finishedDate')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdPartApplyId') is not None:
            self.third_part_apply_id = m.get('thirdPartApplyId')
        if m.get('thirdPartCostCenterId') is not None:
            self.third_part_cost_center_id = m.get('thirdPartCostCenterId')
        if m.get('thirdPartInvoiceId') is not None:
            self.third_part_invoice_id = m.get('thirdPartInvoiceId')
        if m.get('timesTotal') is not None:
            self.times_total = m.get('timesTotal')
        if m.get('timesType') is not None:
            self.times_type = m.get('timesType')
        if m.get('timesUsed') is not None:
            self.times_used = m.get('timesUsed')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AddCityCarApplyResponseBody(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
    ):
        # 商旅内部审批单ID
        self.apply_id = apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        return self


class AddCityCarApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCityCarApplyResponseBody = None,
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
            temp_model = AddCityCarApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveCityCarApplyHeaders(TeaModel):
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


class ApproveCityCarApplyRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        operate_time: str = None,
        remark: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        # 第三方企业ID
        self.corp_id = corp_id
        # 审批时间
        self.operate_time = operate_time
        # 审批备注
        self.remark = remark
        # 审批结果：1-同意，2-拒绝
        self.status = status
        # 第三方审批单ID
        self.third_part_apply_id = third_part_apply_id
        # 审批的第三方员工ID
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
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.third_part_apply_id is not None:
            result['thirdPartApplyId'] = self.third_part_apply_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdPartApplyId') is not None:
            self.third_part_apply_id = m.get('thirdPartApplyId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ApproveCityCarApplyResponseBody(TeaModel):
    def __init__(
        self,
        approve_result: bool = None,
    ):
        # 审批结果
        self.approve_result = approve_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_result is not None:
            result['approveResult'] = self.approve_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approveResult') is not None:
            self.approve_result = m.get('approveResult')
        return self


class ApproveCityCarApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveCityCarApplyResponseBody = None,
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
            temp_model = ApproveCityCarApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BillSettementBtripTrainHeaders(TeaModel):
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


class BillSettementBtripTrainRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        return self


class BillSettementBtripTrainResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        change_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        department: str = None,
        department_id: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        fee_type: str = None,
        index: str = None,
        invoice_title: str = None,
        order_id: str = None,
        order_price: float = None,
        over_apply_id: str = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        refund_fee: float = None,
        run_time: str = None,
        seat_no: str = None,
        seat_type: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        ticket_no: str = None,
        ticket_price: float = None,
        train_no: str = None,
        train_type: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
    ):
        # 交易流水号
        self.alipay_trade_no = alipay_trade_no
        # 审批单号
        self.apply_id = apply_id
        # 到达日期
        self.arr_date = arr_date
        # 到达站点
        self.arr_station = arr_station
        # 到达时间
        self.arr_time = arr_time
        # 预定时间
        self.book_time = book_time
        # 预定人use id
        self.booker_id = booker_id
        # 预订人工号
        self.booker_job_no = booker_job_no
        # 预订人名称
        self.booker_name = booker_name
        # 资金方向
        self.capital_direction = capital_direction
        # 级联部门
        self.cascade_department = cascade_department
        # 改签手续费
        self.change_fee = change_fee
        # 成本中心名称
        self.cost_center = cost_center
        # 成本中心编码
        self.cost_center_number = cost_center_number
        # 折扣率
        self.coupon = coupon
        # 末级部门
        self.department = department
        # 部门id
        self.department_id = department_id
        # 出发日期
        self.dept_date = dept_date
        # 出发站
        self.dept_station = dept_station
        # 出发时间
        self.dept_time = dept_time
        # 费用类型
        self.fee_type = fee_type
        # 序号
        self.index = index
        # 发票抬头
        self.invoice_title = invoice_title
        # 订单号
        self.order_id = order_id
        # 订单金额
        self.order_price = order_price
        # 超标审批单号
        self.over_apply_id = over_apply_id
        # 主键id
        self.primary_id = primary_id
        # 项目编号
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 退款手续费
        self.refund_fee = refund_fee
        # 运行时长
        self.run_time = run_time
        # 座位号
        self.seat_no = seat_no
        # 坐席
        self.seat_type = seat_type
        # 服务费，仅在feeType 6007、6008中展示
        self.service_fee = service_fee
        # 结算金额
        self.settlement_fee = settlement_fee
        # 结算时间
        self.settlement_time = settlement_time
        # 结算类型
        self.settlement_type = settlement_type
        # 入账状态
        self.status = status
        # 票面票号
        self.ticket_no = ticket_no
        # 票价
        self.ticket_price = ticket_price
        # 车次号
        self.train_no = train_no
        # 车次类型
        self.train_type = train_type
        # 出行人useId
        self.traveler_id = traveler_id
        # 出行人工号
        self.traveler_job_no = traveler_job_no
        # 出行人名称
        self.traveler_name = traveler_name
        # 发票类型
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipayTradeNo'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.arr_date is not None:
            result['arrDate'] = self.arr_date
        if self.arr_station is not None:
            result['arrStation'] = self.arr_station
        if self.arr_time is not None:
            result['arrTime'] = self.arr_time
        if self.book_time is not None:
            result['bookTime'] = self.book_time
        if self.booker_id is not None:
            result['bookerId'] = self.booker_id
        if self.booker_job_no is not None:
            result['bookerJobNo'] = self.booker_job_no
        if self.booker_name is not None:
            result['bookerName'] = self.booker_name
        if self.capital_direction is not None:
            result['capitalDirection'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascadeDepartment'] = self.cascade_department
        if self.change_fee is not None:
            result['changeFee'] = self.change_fee
        if self.cost_center is not None:
            result['costCenter'] = self.cost_center
        if self.cost_center_number is not None:
            result['costCenterNumber'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.dept_date is not None:
            result['deptDate'] = self.dept_date
        if self.dept_station is not None:
            result['deptStation'] = self.dept_station
        if self.dept_time is not None:
            result['deptTime'] = self.dept_time
        if self.fee_type is not None:
            result['feeType'] = self.fee_type
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoiceTitle'] = self.invoice_title
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_price is not None:
            result['orderPrice'] = self.order_price
        if self.over_apply_id is not None:
            result['overApplyId'] = self.over_apply_id
        if self.primary_id is not None:
            result['primaryId'] = self.primary_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.refund_fee is not None:
            result['refundFee'] = self.refund_fee
        if self.run_time is not None:
            result['runTime'] = self.run_time
        if self.seat_no is not None:
            result['seatNo'] = self.seat_no
        if self.seat_type is not None:
            result['seatType'] = self.seat_type
        if self.service_fee is not None:
            result['serviceFee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlementFee'] = self.settlement_fee
        if self.settlement_time is not None:
            result['settlementTime'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlementType'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.ticket_no is not None:
            result['ticketNo'] = self.ticket_no
        if self.ticket_price is not None:
            result['ticketPrice'] = self.ticket_price
        if self.train_no is not None:
            result['trainNo'] = self.train_no
        if self.train_type is not None:
            result['trainType'] = self.train_type
        if self.traveler_id is not None:
            result['travelerId'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['travelerJobNo'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['travelerName'] = self.traveler_name
        if self.voucher_type is not None:
            result['voucherType'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipayTradeNo') is not None:
            self.alipay_trade_no = m.get('alipayTradeNo')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('arrDate') is not None:
            self.arr_date = m.get('arrDate')
        if m.get('arrStation') is not None:
            self.arr_station = m.get('arrStation')
        if m.get('arrTime') is not None:
            self.arr_time = m.get('arrTime')
        if m.get('bookTime') is not None:
            self.book_time = m.get('bookTime')
        if m.get('bookerId') is not None:
            self.booker_id = m.get('bookerId')
        if m.get('bookerJobNo') is not None:
            self.booker_job_no = m.get('bookerJobNo')
        if m.get('bookerName') is not None:
            self.booker_name = m.get('bookerName')
        if m.get('capitalDirection') is not None:
            self.capital_direction = m.get('capitalDirection')
        if m.get('cascadeDepartment') is not None:
            self.cascade_department = m.get('cascadeDepartment')
        if m.get('changeFee') is not None:
            self.change_fee = m.get('changeFee')
        if m.get('costCenter') is not None:
            self.cost_center = m.get('costCenter')
        if m.get('costCenterNumber') is not None:
            self.cost_center_number = m.get('costCenterNumber')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('deptDate') is not None:
            self.dept_date = m.get('deptDate')
        if m.get('deptStation') is not None:
            self.dept_station = m.get('deptStation')
        if m.get('deptTime') is not None:
            self.dept_time = m.get('deptTime')
        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoiceTitle') is not None:
            self.invoice_title = m.get('invoiceTitle')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderPrice') is not None:
            self.order_price = m.get('orderPrice')
        if m.get('overApplyId') is not None:
            self.over_apply_id = m.get('overApplyId')
        if m.get('primaryId') is not None:
            self.primary_id = m.get('primaryId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('refundFee') is not None:
            self.refund_fee = m.get('refundFee')
        if m.get('runTime') is not None:
            self.run_time = m.get('runTime')
        if m.get('seatNo') is not None:
            self.seat_no = m.get('seatNo')
        if m.get('seatType') is not None:
            self.seat_type = m.get('seatType')
        if m.get('serviceFee') is not None:
            self.service_fee = m.get('serviceFee')
        if m.get('settlementFee') is not None:
            self.settlement_fee = m.get('settlementFee')
        if m.get('settlementTime') is not None:
            self.settlement_time = m.get('settlementTime')
        if m.get('settlementType') is not None:
            self.settlement_type = m.get('settlementType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ticketNo') is not None:
            self.ticket_no = m.get('ticketNo')
        if m.get('ticketPrice') is not None:
            self.ticket_price = m.get('ticketPrice')
        if m.get('trainNo') is not None:
            self.train_no = m.get('trainNo')
        if m.get('trainType') is not None:
            self.train_type = m.get('trainType')
        if m.get('travelerId') is not None:
            self.traveler_id = m.get('travelerId')
        if m.get('travelerJobNo') is not None:
            self.traveler_job_no = m.get('travelerJobNo')
        if m.get('travelerName') is not None:
            self.traveler_name = m.get('travelerName')
        if m.get('voucherType') is not None:
            self.voucher_type = m.get('voucherType')
        return self


class BillSettementBtripTrainResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[BillSettementBtripTrainResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        # 类目
        self.category = category
        # 企业id
        self.corp_id = corp_id
        # 数据集合
        self.data_list = data_list
        # 记账更新开始时间
        self.period_end = period_end
        # 记账更新结束时间
        self.period_start = period_start
        # 总数据量
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = BillSettementBtripTrainResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class BillSettementBtripTrainResponseBody(TeaModel):
    def __init__(
        self,
        module: BillSettementBtripTrainResponseBodyModule = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
    ):
        # module
        self.module = module
        # 结果code
        self.result_code = result_code
        # 结果msg
        self.result_msg = result_msg
        # 是否成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.result_msg is not None:
            result['resultMsg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = BillSettementBtripTrainResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('resultMsg') is not None:
            self.result_msg = m.get('resultMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BillSettementBtripTrainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BillSettementBtripTrainResponseBody = None,
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
            temp_model = BillSettementBtripTrainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BillSettementCarHeaders(TeaModel):
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


class BillSettementCarRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        return self


class BillSettementCarResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_city: str = None,
        arr_date: str = None,
        arr_location: str = None,
        arr_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        business_category: str = None,
        capital_direction: str = None,
        car_level: str = None,
        cascade_department: str = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        coupon_price: float = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_location: str = None,
        dept_time: str = None,
        estimate_drive_distance: str = None,
        estimate_price: float = None,
        fee_type: str = None,
        index: str = None,
        invoice_title: str = None,
        memo: str = None,
        order_id: str = None,
        order_price: float = None,
        over_apply_id: str = None,
        person_settle_fee: float = None,
        primary_id: str = None,
        project_code: str = None,
        project_name: str = None,
        provider_name: str = None,
        real_drive_distance: str = None,
        real_from_addr: str = None,
        real_to_addr: str = None,
        service_fee: str = None,
        settlement_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        special_order: str = None,
        special_reason: str = None,
        status: int = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        user_confirm_desc: str = None,
        voucher_type: int = None,
    ):
        # 支付交易流水号
        self.alipay_trade_no = alipay_trade_no
        # 审批单号
        self.apply_id = apply_id
        # 到达城市
        self.arr_city = arr_city
        # 到达日期
        self.arr_date = arr_date
        # 到达地
        self.arr_location = arr_location
        # 到达时间
        self.arr_time = arr_time
        # 预定时间
        self.book_time = book_time
        # 预定人use id
        self.booker_id = booker_id
        # 预订人工号
        self.booker_job_no = booker_job_no
        # 预订人名称
        self.booker_name = booker_name
        # 用车事由
        self.business_category = business_category
        # 资金方向
        self.capital_direction = capital_direction
        # 车型
        self.car_level = car_level
        # 级联部门
        self.cascade_department = cascade_department
        # 成本中心名称
        self.cost_center = cost_center
        # 成本中心编号
        self.cost_center_number = cost_center_number
        # 优惠券
        self.coupon = coupon
        # 优惠金额
        self.coupon_price = coupon_price
        # 末级部门
        self.department = department
        # 部门id
        self.department_id = department_id
        # 出发城市
        self.dept_city = dept_city
        # 出发日期
        self.dept_date = dept_date
        # 出发地
        self.dept_location = dept_location
        # 出发时间
        self.dept_time = dept_time
        # 预估行驶距离
        self.estimate_drive_distance = estimate_drive_distance
        # 预估金额
        self.estimate_price = estimate_price
        # 费用类型
        self.fee_type = fee_type
        # 序号
        self.index = index
        # 发票抬头
        self.invoice_title = invoice_title
        # 用车事由
        self.memo = memo
        # 订单id
        self.order_id = order_id
        # 订单金额
        self.order_price = order_price
        # 超标审批单号
        self.over_apply_id = over_apply_id
        # 个人支付金额
        self.person_settle_fee = person_settle_fee
        self.primary_id = primary_id
        # 项目编码
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 供应商
        self.provider_name = provider_name
        # 实际行驶距离
        self.real_drive_distance = real_drive_distance
        # 实际上车点
        self.real_from_addr = real_from_addr
        # 实际下车点
        self.real_to_addr = real_to_addr
        # 服务费，仅在feeType 40111 中展示
        self.service_fee = service_fee
        # 结算金额
        self.settlement_fee = settlement_fee
        # 结算时间
        self.settlement_time = settlement_time
        # 结算类型
        self.settlement_type = settlement_type
        # 特别关注订单
        self.special_order = special_order
        # 特别关注原因
        self.special_reason = special_reason
        # 入账状态
        self.status = status
        # 出行人use id
        self.traveler_id = traveler_id
        # 出行人工号
        self.traveler_job_no = traveler_job_no
        # 出行人名称
        self.traveler_name = traveler_name
        # 员工是否认可
        self.user_confirm_desc = user_confirm_desc
        # 发票类型
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipayTradeNo'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.arr_city is not None:
            result['arrCity'] = self.arr_city
        if self.arr_date is not None:
            result['arrDate'] = self.arr_date
        if self.arr_location is not None:
            result['arrLocation'] = self.arr_location
        if self.arr_time is not None:
            result['arrTime'] = self.arr_time
        if self.book_time is not None:
            result['bookTime'] = self.book_time
        if self.booker_id is not None:
            result['bookerId'] = self.booker_id
        if self.booker_job_no is not None:
            result['bookerJobNo'] = self.booker_job_no
        if self.booker_name is not None:
            result['bookerName'] = self.booker_name
        if self.business_category is not None:
            result['businessCategory'] = self.business_category
        if self.capital_direction is not None:
            result['capitalDirection'] = self.capital_direction
        if self.car_level is not None:
            result['carLevel'] = self.car_level
        if self.cascade_department is not None:
            result['cascadeDepartment'] = self.cascade_department
        if self.cost_center is not None:
            result['costCenter'] = self.cost_center
        if self.cost_center_number is not None:
            result['costCenterNumber'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.coupon_price is not None:
            result['couponPrice'] = self.coupon_price
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.dept_city is not None:
            result['deptCity'] = self.dept_city
        if self.dept_date is not None:
            result['deptDate'] = self.dept_date
        if self.dept_location is not None:
            result['deptLocation'] = self.dept_location
        if self.dept_time is not None:
            result['deptTime'] = self.dept_time
        if self.estimate_drive_distance is not None:
            result['estimateDriveDistance'] = self.estimate_drive_distance
        if self.estimate_price is not None:
            result['estimatePrice'] = self.estimate_price
        if self.fee_type is not None:
            result['feeType'] = self.fee_type
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoiceTitle'] = self.invoice_title
        if self.memo is not None:
            result['memo'] = self.memo
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_price is not None:
            result['orderPrice'] = self.order_price
        if self.over_apply_id is not None:
            result['overApplyId'] = self.over_apply_id
        if self.person_settle_fee is not None:
            result['personSettleFee'] = self.person_settle_fee
        if self.primary_id is not None:
            result['primaryId'] = self.primary_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provider_name is not None:
            result['providerName'] = self.provider_name
        if self.real_drive_distance is not None:
            result['realDriveDistance'] = self.real_drive_distance
        if self.real_from_addr is not None:
            result['realFromAddr'] = self.real_from_addr
        if self.real_to_addr is not None:
            result['realToAddr'] = self.real_to_addr
        if self.service_fee is not None:
            result['serviceFee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlementFee'] = self.settlement_fee
        if self.settlement_time is not None:
            result['settlementTime'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlementType'] = self.settlement_type
        if self.special_order is not None:
            result['specialOrder'] = self.special_order
        if self.special_reason is not None:
            result['specialReason'] = self.special_reason
        if self.status is not None:
            result['status'] = self.status
        if self.traveler_id is not None:
            result['travelerId'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['travelerJobNo'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['travelerName'] = self.traveler_name
        if self.user_confirm_desc is not None:
            result['userConfirmDesc'] = self.user_confirm_desc
        if self.voucher_type is not None:
            result['voucherType'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipayTradeNo') is not None:
            self.alipay_trade_no = m.get('alipayTradeNo')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('arrCity') is not None:
            self.arr_city = m.get('arrCity')
        if m.get('arrDate') is not None:
            self.arr_date = m.get('arrDate')
        if m.get('arrLocation') is not None:
            self.arr_location = m.get('arrLocation')
        if m.get('arrTime') is not None:
            self.arr_time = m.get('arrTime')
        if m.get('bookTime') is not None:
            self.book_time = m.get('bookTime')
        if m.get('bookerId') is not None:
            self.booker_id = m.get('bookerId')
        if m.get('bookerJobNo') is not None:
            self.booker_job_no = m.get('bookerJobNo')
        if m.get('bookerName') is not None:
            self.booker_name = m.get('bookerName')
        if m.get('businessCategory') is not None:
            self.business_category = m.get('businessCategory')
        if m.get('capitalDirection') is not None:
            self.capital_direction = m.get('capitalDirection')
        if m.get('carLevel') is not None:
            self.car_level = m.get('carLevel')
        if m.get('cascadeDepartment') is not None:
            self.cascade_department = m.get('cascadeDepartment')
        if m.get('costCenter') is not None:
            self.cost_center = m.get('costCenter')
        if m.get('costCenterNumber') is not None:
            self.cost_center_number = m.get('costCenterNumber')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('couponPrice') is not None:
            self.coupon_price = m.get('couponPrice')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('deptCity') is not None:
            self.dept_city = m.get('deptCity')
        if m.get('deptDate') is not None:
            self.dept_date = m.get('deptDate')
        if m.get('deptLocation') is not None:
            self.dept_location = m.get('deptLocation')
        if m.get('deptTime') is not None:
            self.dept_time = m.get('deptTime')
        if m.get('estimateDriveDistance') is not None:
            self.estimate_drive_distance = m.get('estimateDriveDistance')
        if m.get('estimatePrice') is not None:
            self.estimate_price = m.get('estimatePrice')
        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoiceTitle') is not None:
            self.invoice_title = m.get('invoiceTitle')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderPrice') is not None:
            self.order_price = m.get('orderPrice')
        if m.get('overApplyId') is not None:
            self.over_apply_id = m.get('overApplyId')
        if m.get('personSettleFee') is not None:
            self.person_settle_fee = m.get('personSettleFee')
        if m.get('primaryId') is not None:
            self.primary_id = m.get('primaryId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')
        if m.get('realDriveDistance') is not None:
            self.real_drive_distance = m.get('realDriveDistance')
        if m.get('realFromAddr') is not None:
            self.real_from_addr = m.get('realFromAddr')
        if m.get('realToAddr') is not None:
            self.real_to_addr = m.get('realToAddr')
        if m.get('serviceFee') is not None:
            self.service_fee = m.get('serviceFee')
        if m.get('settlementFee') is not None:
            self.settlement_fee = m.get('settlementFee')
        if m.get('settlementTime') is not None:
            self.settlement_time = m.get('settlementTime')
        if m.get('settlementType') is not None:
            self.settlement_type = m.get('settlementType')
        if m.get('specialOrder') is not None:
            self.special_order = m.get('specialOrder')
        if m.get('specialReason') is not None:
            self.special_reason = m.get('specialReason')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('travelerId') is not None:
            self.traveler_id = m.get('travelerId')
        if m.get('travelerJobNo') is not None:
            self.traveler_job_no = m.get('travelerJobNo')
        if m.get('travelerName') is not None:
            self.traveler_name = m.get('travelerName')
        if m.get('userConfirmDesc') is not None:
            self.user_confirm_desc = m.get('userConfirmDesc')
        if m.get('voucherType') is not None:
            self.voucher_type = m.get('voucherType')
        return self


class BillSettementCarResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[BillSettementCarResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        # 类目
        self.category = category
        # 企业id
        self.corp_id = corp_id
        # 数据集合
        self.data_list = data_list
        # 记账更新开始日期
        self.period_end = period_end
        # 记账更新结束日期
        self.period_start = period_start
        # 总数量
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = BillSettementCarResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class BillSettementCarResponseBody(TeaModel):
    def __init__(
        self,
        module: BillSettementCarResponseBodyModule = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
    ):
        # module
        self.module = module
        # 结果code
        self.result_code = result_code
        # 结果msg
        self.result_msg = result_msg
        # 是否成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.result_msg is not None:
            result['resultMsg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = BillSettementCarResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('resultMsg') is not None:
            self.result_msg = m.get('resultMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BillSettementCarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BillSettementCarResponseBody = None,
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
            temp_model = BillSettementCarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BillSettementFlightHeaders(TeaModel):
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


class BillSettementFlightRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        # 类目：机酒火车 1：机票； 2：酒店； 4：用车 6：商旅火车票
        self.category = category
        # 第三方企业ID
        self.corp_id = corp_id
        # 页数，从1开始
        self.page_number = page_number
        # 每页数据量，默认100，最高500
        self.page_size = page_size
        # 记账更新结束日期
        self.period_end = period_end
        # 记账更新开始日期
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        return self


class BillSettementFlightResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        advance_day: int = None,
        airline_corp_code: str = None,
        airline_corp_name: str = None,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        btrip_coupon_fee: float = None,
        build_fee: float = None,
        cabin: str = None,
        cabin_class: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        change_fee: float = None,
        corp_pay_order_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        dep_airport_code: str = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        discount: str = None,
        fee_type: str = None,
        flight_no: str = None,
        index: str = None,
        insurance_fee: float = None,
        invoice_title: str = None,
        itinerary_num: str = None,
        itinerary_price: float = None,
        most_difference_dept_time: str = None,
        most_difference_discount: float = None,
        most_difference_flight_no: str = None,
        most_difference_price: float = None,
        most_difference_reason: str = None,
        most_price: float = None,
        negotiation_coupon_fee: float = None,
        oil_fee: float = None,
        order_id: str = None,
        over_apply_id: str = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        refund_fee: float = None,
        refund_upgrade_cost: float = None,
        repeat_refund: str = None,
        seal_price: float = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        ticket_id: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        upgrade_cost: float = None,
        voucher_type: int = None,
    ):
        # 提前预定天数
        self.advance_day = advance_day
        # 航司三字码
        self.airline_corp_code = airline_corp_code
        # 航司名称
        self.airline_corp_name = airline_corp_name
        # 交易流水号
        self.alipay_trade_no = alipay_trade_no
        # 审批单号
        self.apply_id = apply_id
        # 到达机场二字码
        self.arr_airport_code = arr_airport_code
        # 到达城市
        self.arr_city = arr_city
        # 到达日期
        self.arr_date = arr_date
        # 到达机场
        self.arr_station = arr_station
        # 到达时间
        self.arr_time = arr_time
        # 预定时间
        self.book_time = book_time
        # 预订人use id
        self.booker_id = booker_id
        # 预订人工号
        self.booker_job_no = booker_job_no
        # 预订人名称
        self.booker_name = booker_name
        # 商旅优惠金额
        self.btrip_coupon_fee = btrip_coupon_fee
        # 基建费
        self.build_fee = build_fee
        # 舱位
        self.cabin = cabin
        # 舱位码
        self.cabin_class = cabin_class
        # 资金方向
        self.capital_direction = capital_direction
        # 级联部门
        self.cascade_department = cascade_department
        # 改签费用
        self.change_fee = change_fee
        # 订单金额
        self.corp_pay_order_fee = corp_pay_order_fee
        # 成本中心名称
        self.cost_center = cost_center
        # 成本中心编号
        self.cost_center_number = cost_center_number
        # 优惠券
        self.coupon = coupon
        # 起飞机场二字码
        self.dep_airport_code = dep_airport_code
        # 末级部门
        self.department = department
        # 部门id
        self.department_id = department_id
        # 起飞城市
        self.dept_city = dept_city
        # 起飞日期
        self.dept_date = dept_date
        # 起飞机场
        self.dept_station = dept_station
        # 起飞时间
        self.dept_time = dept_time
        # 折扣率
        self.discount = discount
        # 费用类型
        self.fee_type = fee_type
        # 航班号
        self.flight_no = flight_no
        # 序号
        self.index = index
        # 保险费
        self.insurance_fee = insurance_fee
        # 发票抬头
        self.invoice_title = invoice_title
        # 行程单打印序号
        self.itinerary_num = itinerary_num
        # 行程单金额
        self.itinerary_price = itinerary_price
        # 低价提醒（起飞时间）
        self.most_difference_dept_time = most_difference_dept_time
        # 低价提醒（折扣）
        self.most_difference_discount = most_difference_discount
        # 低价提醒(航班号)
        self.most_difference_flight_no = most_difference_flight_no
        # 低价提醒(与最低价差额)
        self.most_difference_price = most_difference_price
        # 不选低价原因
        self.most_difference_reason = most_difference_reason
        # 低价航班价格
        self.most_price = most_price
        # 协议价优惠金额
        self.negotiation_coupon_fee = negotiation_coupon_fee
        # 燃油费
        self.oil_fee = oil_fee
        # 订单号
        self.order_id = order_id
        # 超标审批单号
        self.over_apply_id = over_apply_id
        # 主键id
        self.primary_id = primary_id
        # 项目代码
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 退款手续费
        self.refund_fee = refund_fee
        # 改签退票手续费
        self.refund_upgrade_cost = refund_upgrade_cost
        # 是否重复退
        self.repeat_refund = repeat_refund
        # 销售价
        self.seal_price = seal_price
        # 服务费，仅在feeType  11001、11002中展示
        self.service_fee = service_fee
        # 结算金额
        self.settlement_fee = settlement_fee
        # 结算时间
        self.settlement_time = settlement_time
        # 结算类型
        self.settlement_type = settlement_type
        # 入账状态
        self.status = status
        # 行程单号
        self.ticket_id = ticket_id
        # 出行人use id
        self.traveler_id = traveler_id
        # 出行人工号
        self.traveler_job_no = traveler_job_no
        # 出行人名称
        self.traveler_name = traveler_name
        # 改签差价
        self.upgrade_cost = upgrade_cost
        # 发票类型
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_day is not None:
            result['advanceDay'] = self.advance_day
        if self.airline_corp_code is not None:
            result['airlineCorpCode'] = self.airline_corp_code
        if self.airline_corp_name is not None:
            result['airlineCorpName'] = self.airline_corp_name
        if self.alipay_trade_no is not None:
            result['alipayTradeNo'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.arr_airport_code is not None:
            result['arrAirportCode'] = self.arr_airport_code
        if self.arr_city is not None:
            result['arrCity'] = self.arr_city
        if self.arr_date is not None:
            result['arrDate'] = self.arr_date
        if self.arr_station is not None:
            result['arrStation'] = self.arr_station
        if self.arr_time is not None:
            result['arrTime'] = self.arr_time
        if self.book_time is not None:
            result['bookTime'] = self.book_time
        if self.booker_id is not None:
            result['bookerId'] = self.booker_id
        if self.booker_job_no is not None:
            result['bookerJobNo'] = self.booker_job_no
        if self.booker_name is not None:
            result['bookerName'] = self.booker_name
        if self.btrip_coupon_fee is not None:
            result['btripCouponFee'] = self.btrip_coupon_fee
        if self.build_fee is not None:
            result['buildFee'] = self.build_fee
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabinClass'] = self.cabin_class
        if self.capital_direction is not None:
            result['capitalDirection'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascadeDepartment'] = self.cascade_department
        if self.change_fee is not None:
            result['changeFee'] = self.change_fee
        if self.corp_pay_order_fee is not None:
            result['corpPayOrderFee'] = self.corp_pay_order_fee
        if self.cost_center is not None:
            result['costCenter'] = self.cost_center
        if self.cost_center_number is not None:
            result['costCenterNumber'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.dep_airport_code is not None:
            result['depAirportCode'] = self.dep_airport_code
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.dept_city is not None:
            result['deptCity'] = self.dept_city
        if self.dept_date is not None:
            result['deptDate'] = self.dept_date
        if self.dept_station is not None:
            result['deptStation'] = self.dept_station
        if self.dept_time is not None:
            result['deptTime'] = self.dept_time
        if self.discount is not None:
            result['discount'] = self.discount
        if self.fee_type is not None:
            result['feeType'] = self.fee_type
        if self.flight_no is not None:
            result['flightNo'] = self.flight_no
        if self.index is not None:
            result['index'] = self.index
        if self.insurance_fee is not None:
            result['insuranceFee'] = self.insurance_fee
        if self.invoice_title is not None:
            result['invoiceTitle'] = self.invoice_title
        if self.itinerary_num is not None:
            result['itineraryNum'] = self.itinerary_num
        if self.itinerary_price is not None:
            result['itineraryPrice'] = self.itinerary_price
        if self.most_difference_dept_time is not None:
            result['mostDifferenceDeptTime'] = self.most_difference_dept_time
        if self.most_difference_discount is not None:
            result['mostDifferenceDiscount'] = self.most_difference_discount
        if self.most_difference_flight_no is not None:
            result['mostDifferenceFlightNo'] = self.most_difference_flight_no
        if self.most_difference_price is not None:
            result['mostDifferencePrice'] = self.most_difference_price
        if self.most_difference_reason is not None:
            result['mostDifferenceReason'] = self.most_difference_reason
        if self.most_price is not None:
            result['mostPrice'] = self.most_price
        if self.negotiation_coupon_fee is not None:
            result['negotiationCouponFee'] = self.negotiation_coupon_fee
        if self.oil_fee is not None:
            result['oilFee'] = self.oil_fee
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.over_apply_id is not None:
            result['overApplyId'] = self.over_apply_id
        if self.primary_id is not None:
            result['primaryId'] = self.primary_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.refund_fee is not None:
            result['refundFee'] = self.refund_fee
        if self.refund_upgrade_cost is not None:
            result['refundUpgradeCost'] = self.refund_upgrade_cost
        if self.repeat_refund is not None:
            result['repeatRefund'] = self.repeat_refund
        if self.seal_price is not None:
            result['sealPrice'] = self.seal_price
        if self.service_fee is not None:
            result['serviceFee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlementFee'] = self.settlement_fee
        if self.settlement_time is not None:
            result['settlementTime'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlementType'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        if self.traveler_id is not None:
            result['travelerId'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['travelerJobNo'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['travelerName'] = self.traveler_name
        if self.upgrade_cost is not None:
            result['upgradeCost'] = self.upgrade_cost
        if self.voucher_type is not None:
            result['voucherType'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceDay') is not None:
            self.advance_day = m.get('advanceDay')
        if m.get('airlineCorpCode') is not None:
            self.airline_corp_code = m.get('airlineCorpCode')
        if m.get('airlineCorpName') is not None:
            self.airline_corp_name = m.get('airlineCorpName')
        if m.get('alipayTradeNo') is not None:
            self.alipay_trade_no = m.get('alipayTradeNo')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('arrAirportCode') is not None:
            self.arr_airport_code = m.get('arrAirportCode')
        if m.get('arrCity') is not None:
            self.arr_city = m.get('arrCity')
        if m.get('arrDate') is not None:
            self.arr_date = m.get('arrDate')
        if m.get('arrStation') is not None:
            self.arr_station = m.get('arrStation')
        if m.get('arrTime') is not None:
            self.arr_time = m.get('arrTime')
        if m.get('bookTime') is not None:
            self.book_time = m.get('bookTime')
        if m.get('bookerId') is not None:
            self.booker_id = m.get('bookerId')
        if m.get('bookerJobNo') is not None:
            self.booker_job_no = m.get('bookerJobNo')
        if m.get('bookerName') is not None:
            self.booker_name = m.get('bookerName')
        if m.get('btripCouponFee') is not None:
            self.btrip_coupon_fee = m.get('btripCouponFee')
        if m.get('buildFee') is not None:
            self.build_fee = m.get('buildFee')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabinClass') is not None:
            self.cabin_class = m.get('cabinClass')
        if m.get('capitalDirection') is not None:
            self.capital_direction = m.get('capitalDirection')
        if m.get('cascadeDepartment') is not None:
            self.cascade_department = m.get('cascadeDepartment')
        if m.get('changeFee') is not None:
            self.change_fee = m.get('changeFee')
        if m.get('corpPayOrderFee') is not None:
            self.corp_pay_order_fee = m.get('corpPayOrderFee')
        if m.get('costCenter') is not None:
            self.cost_center = m.get('costCenter')
        if m.get('costCenterNumber') is not None:
            self.cost_center_number = m.get('costCenterNumber')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('depAirportCode') is not None:
            self.dep_airport_code = m.get('depAirportCode')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('deptCity') is not None:
            self.dept_city = m.get('deptCity')
        if m.get('deptDate') is not None:
            self.dept_date = m.get('deptDate')
        if m.get('deptStation') is not None:
            self.dept_station = m.get('deptStation')
        if m.get('deptTime') is not None:
            self.dept_time = m.get('deptTime')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')
        if m.get('flightNo') is not None:
            self.flight_no = m.get('flightNo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('insuranceFee') is not None:
            self.insurance_fee = m.get('insuranceFee')
        if m.get('invoiceTitle') is not None:
            self.invoice_title = m.get('invoiceTitle')
        if m.get('itineraryNum') is not None:
            self.itinerary_num = m.get('itineraryNum')
        if m.get('itineraryPrice') is not None:
            self.itinerary_price = m.get('itineraryPrice')
        if m.get('mostDifferenceDeptTime') is not None:
            self.most_difference_dept_time = m.get('mostDifferenceDeptTime')
        if m.get('mostDifferenceDiscount') is not None:
            self.most_difference_discount = m.get('mostDifferenceDiscount')
        if m.get('mostDifferenceFlightNo') is not None:
            self.most_difference_flight_no = m.get('mostDifferenceFlightNo')
        if m.get('mostDifferencePrice') is not None:
            self.most_difference_price = m.get('mostDifferencePrice')
        if m.get('mostDifferenceReason') is not None:
            self.most_difference_reason = m.get('mostDifferenceReason')
        if m.get('mostPrice') is not None:
            self.most_price = m.get('mostPrice')
        if m.get('negotiationCouponFee') is not None:
            self.negotiation_coupon_fee = m.get('negotiationCouponFee')
        if m.get('oilFee') is not None:
            self.oil_fee = m.get('oilFee')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('overApplyId') is not None:
            self.over_apply_id = m.get('overApplyId')
        if m.get('primaryId') is not None:
            self.primary_id = m.get('primaryId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('refundFee') is not None:
            self.refund_fee = m.get('refundFee')
        if m.get('refundUpgradeCost') is not None:
            self.refund_upgrade_cost = m.get('refundUpgradeCost')
        if m.get('repeatRefund') is not None:
            self.repeat_refund = m.get('repeatRefund')
        if m.get('sealPrice') is not None:
            self.seal_price = m.get('sealPrice')
        if m.get('serviceFee') is not None:
            self.service_fee = m.get('serviceFee')
        if m.get('settlementFee') is not None:
            self.settlement_fee = m.get('settlementFee')
        if m.get('settlementTime') is not None:
            self.settlement_time = m.get('settlementTime')
        if m.get('settlementType') is not None:
            self.settlement_type = m.get('settlementType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        if m.get('travelerId') is not None:
            self.traveler_id = m.get('travelerId')
        if m.get('travelerJobNo') is not None:
            self.traveler_job_no = m.get('travelerJobNo')
        if m.get('travelerName') is not None:
            self.traveler_name = m.get('travelerName')
        if m.get('upgradeCost') is not None:
            self.upgrade_cost = m.get('upgradeCost')
        if m.get('voucherType') is not None:
            self.voucher_type = m.get('voucherType')
        return self


class BillSettementFlightResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[BillSettementFlightResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        # 类目
        self.category = category
        # 企业id
        self.corp_id = corp_id
        # 数据集合
        self.data_list = data_list
        # 记账更新开始日期
        self.period_end = period_end
        # 记账更新结束日期
        self.period_start = period_start
        # 总数据量
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = BillSettementFlightResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class BillSettementFlightResponseBody(TeaModel):
    def __init__(
        self,
        module: BillSettementFlightResponseBodyModule = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
    ):
        # module
        self.module = module
        # 结果code
        self.result_code = result_code
        # 结果msg
        self.result_msg = result_msg
        # 是否成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.result_msg is not None:
            result['resultMsg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = BillSettementFlightResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('resultMsg') is not None:
            self.result_msg = m.get('resultMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BillSettementFlightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BillSettementFlightResponseBody = None,
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
            temp_model = BillSettementFlightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BillSettementHotelHeaders(TeaModel):
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


class BillSettementHotelRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        # 类目：机酒火车 1：机票； 2：酒店； 4：用车 6：商旅火车票
        self.category = category
        # 第三方企业
        self.corp_id = corp_id
        # 页数，从1开始
        self.page_number = page_number
        # 每页数据量，默认100，最高500
        self.page_size = page_size
        # 记账更新结束日期
        self.period_end = period_end
        # 记账更新开始日期
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        return self


class BillSettementHotelResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        check_in_date: str = None,
        checkout_date: str = None,
        city: str = None,
        city_code: str = None,
        corp_refund_fee: float = None,
        corp_total_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        department: str = None,
        department_id: str = None,
        fee_type: str = None,
        fees: float = None,
        fu_point_fee: float = None,
        hotel_name: str = None,
        index: str = None,
        invoice_title: str = None,
        is_negotiation: bool = None,
        is_share_str: str = None,
        nights: int = None,
        order_id: str = None,
        order_price: float = None,
        order_type: str = None,
        over_apply_id: str = None,
        person_refund_fee: float = None,
        person_settle_price: float = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        promotion_fee: float = None,
        room_number: int = None,
        room_price: float = None,
        room_type: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        total_nights: int = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
    ):
        # 交易流水号
        self.alipay_trade_no = alipay_trade_no
        # 审批单号
        self.apply_id = apply_id
        # 预定时间
        self.book_time = book_time
        # 预定人use id
        self.booker_id = booker_id
        # 预订人工号
        self.booker_job_no = booker_job_no
        # 预订人名称
        self.booker_name = booker_name
        # 资金方向
        self.capital_direction = capital_direction
        # 级联部门
        self.cascade_department = cascade_department
        # 入住时间
        self.check_in_date = check_in_date
        # 离店时间
        self.checkout_date = checkout_date
        # 入住城市
        self.city = city
        # 城市编码
        self.city_code = city_code
        # 企业退款金额
        self.corp_refund_fee = corp_refund_fee
        # 企业支付金额
        self.corp_total_fee = corp_total_fee
        # 成本中心名称
        self.cost_center = cost_center
        # 成本中心编码
        self.cost_center_number = cost_center_number
        # 末级部门
        self.department = department
        # 部门id
        self.department_id = department_id
        # 费用类型
        self.fee_type = fee_type
        # 杂费
        self.fees = fees
        # 福豆支付
        self.fu_point_fee = fu_point_fee
        # 酒店名称
        self.hotel_name = hotel_name
        # 序号
        self.index = index
        # 发票抬头
        self.invoice_title = invoice_title
        # 是否协议价
        self.is_negotiation = is_negotiation
        # 是否合住
        self.is_share_str = is_share_str
        # 入住天数
        self.nights = nights
        # 订单号
        self.order_id = order_id
        # 订单金额
        self.order_price = order_price
        # 订单类型
        self.order_type = order_type
        # 超标审批单号
        self.over_apply_id = over_apply_id
        # 个人退款金额
        self.person_refund_fee = person_refund_fee
        # 个人支付金额
        self.person_settle_price = person_settle_price
        # 主键id
        self.primary_id = primary_id
        # 项目编码
        self.project_code = project_code
        # 项目名称
        self.project_name = project_name
        # 优惠券
        self.promotion_fee = promotion_fee
        # 房间数
        self.room_number = room_number
        # 房价
        self.room_price = room_price
        # 房间类型
        self.room_type = room_type
        # 服务费,仅在 feeType 20111、20112中展示
        self.service_fee = service_fee
        # 结算金额
        self.settlement_fee = settlement_fee
        # 结算时间
        self.settlement_time = settlement_time
        # 结算类型
        self.settlement_type = settlement_type
        # 入账状态
        self.status = status
        # 总间夜数
        self.total_nights = total_nights
        # 出行人use id
        self.traveler_id = traveler_id
        # 出行人工号
        self.traveler_job_no = traveler_job_no
        # 出行人名称
        self.traveler_name = traveler_name
        # 发票类型
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipayTradeNo'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.book_time is not None:
            result['bookTime'] = self.book_time
        if self.booker_id is not None:
            result['bookerId'] = self.booker_id
        if self.booker_job_no is not None:
            result['bookerJobNo'] = self.booker_job_no
        if self.booker_name is not None:
            result['bookerName'] = self.booker_name
        if self.capital_direction is not None:
            result['capitalDirection'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascadeDepartment'] = self.cascade_department
        if self.check_in_date is not None:
            result['checkInDate'] = self.check_in_date
        if self.checkout_date is not None:
            result['checkoutDate'] = self.checkout_date
        if self.city is not None:
            result['city'] = self.city
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.corp_refund_fee is not None:
            result['corpRefundFee'] = self.corp_refund_fee
        if self.corp_total_fee is not None:
            result['corpTotalFee'] = self.corp_total_fee
        if self.cost_center is not None:
            result['costCenter'] = self.cost_center
        if self.cost_center_number is not None:
            result['costCenterNumber'] = self.cost_center_number
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['departmentId'] = self.department_id
        if self.fee_type is not None:
            result['feeType'] = self.fee_type
        if self.fees is not None:
            result['fees'] = self.fees
        if self.fu_point_fee is not None:
            result['fuPointFee'] = self.fu_point_fee
        if self.hotel_name is not None:
            result['hotelName'] = self.hotel_name
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoiceTitle'] = self.invoice_title
        if self.is_negotiation is not None:
            result['isNegotiation'] = self.is_negotiation
        if self.is_share_str is not None:
            result['isShareStr'] = self.is_share_str
        if self.nights is not None:
            result['nights'] = self.nights
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_price is not None:
            result['orderPrice'] = self.order_price
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.over_apply_id is not None:
            result['overApplyId'] = self.over_apply_id
        if self.person_refund_fee is not None:
            result['personRefundFee'] = self.person_refund_fee
        if self.person_settle_price is not None:
            result['personSettlePrice'] = self.person_settle_price
        if self.primary_id is not None:
            result['primaryId'] = self.primary_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.promotion_fee is not None:
            result['promotionFee'] = self.promotion_fee
        if self.room_number is not None:
            result['roomNumber'] = self.room_number
        if self.room_price is not None:
            result['roomPrice'] = self.room_price
        if self.room_type is not None:
            result['roomType'] = self.room_type
        if self.service_fee is not None:
            result['serviceFee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlementFee'] = self.settlement_fee
        if self.settlement_time is not None:
            result['settlementTime'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlementType'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_nights is not None:
            result['totalNights'] = self.total_nights
        if self.traveler_id is not None:
            result['travelerId'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['travelerJobNo'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['travelerName'] = self.traveler_name
        if self.voucher_type is not None:
            result['voucherType'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipayTradeNo') is not None:
            self.alipay_trade_no = m.get('alipayTradeNo')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('bookTime') is not None:
            self.book_time = m.get('bookTime')
        if m.get('bookerId') is not None:
            self.booker_id = m.get('bookerId')
        if m.get('bookerJobNo') is not None:
            self.booker_job_no = m.get('bookerJobNo')
        if m.get('bookerName') is not None:
            self.booker_name = m.get('bookerName')
        if m.get('capitalDirection') is not None:
            self.capital_direction = m.get('capitalDirection')
        if m.get('cascadeDepartment') is not None:
            self.cascade_department = m.get('cascadeDepartment')
        if m.get('checkInDate') is not None:
            self.check_in_date = m.get('checkInDate')
        if m.get('checkoutDate') is not None:
            self.checkout_date = m.get('checkoutDate')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('corpRefundFee') is not None:
            self.corp_refund_fee = m.get('corpRefundFee')
        if m.get('corpTotalFee') is not None:
            self.corp_total_fee = m.get('corpTotalFee')
        if m.get('costCenter') is not None:
            self.cost_center = m.get('costCenter')
        if m.get('costCenterNumber') is not None:
            self.cost_center_number = m.get('costCenterNumber')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('departmentId') is not None:
            self.department_id = m.get('departmentId')
        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')
        if m.get('fees') is not None:
            self.fees = m.get('fees')
        if m.get('fuPointFee') is not None:
            self.fu_point_fee = m.get('fuPointFee')
        if m.get('hotelName') is not None:
            self.hotel_name = m.get('hotelName')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoiceTitle') is not None:
            self.invoice_title = m.get('invoiceTitle')
        if m.get('isNegotiation') is not None:
            self.is_negotiation = m.get('isNegotiation')
        if m.get('isShareStr') is not None:
            self.is_share_str = m.get('isShareStr')
        if m.get('nights') is not None:
            self.nights = m.get('nights')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderPrice') is not None:
            self.order_price = m.get('orderPrice')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('overApplyId') is not None:
            self.over_apply_id = m.get('overApplyId')
        if m.get('personRefundFee') is not None:
            self.person_refund_fee = m.get('personRefundFee')
        if m.get('personSettlePrice') is not None:
            self.person_settle_price = m.get('personSettlePrice')
        if m.get('primaryId') is not None:
            self.primary_id = m.get('primaryId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('promotionFee') is not None:
            self.promotion_fee = m.get('promotionFee')
        if m.get('roomNumber') is not None:
            self.room_number = m.get('roomNumber')
        if m.get('roomPrice') is not None:
            self.room_price = m.get('roomPrice')
        if m.get('roomType') is not None:
            self.room_type = m.get('roomType')
        if m.get('serviceFee') is not None:
            self.service_fee = m.get('serviceFee')
        if m.get('settlementFee') is not None:
            self.settlement_fee = m.get('settlementFee')
        if m.get('settlementTime') is not None:
            self.settlement_time = m.get('settlementTime')
        if m.get('settlementType') is not None:
            self.settlement_type = m.get('settlementType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('totalNights') is not None:
            self.total_nights = m.get('totalNights')
        if m.get('travelerId') is not None:
            self.traveler_id = m.get('travelerId')
        if m.get('travelerJobNo') is not None:
            self.traveler_job_no = m.get('travelerJobNo')
        if m.get('travelerName') is not None:
            self.traveler_name = m.get('travelerName')
        if m.get('voucherType') is not None:
            self.voucher_type = m.get('voucherType')
        return self


class BillSettementHotelResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[BillSettementHotelResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        # 类目
        self.category = category
        # 企业id
        self.corp_id = corp_id
        # 数据集合
        self.data_list = data_list
        # 记账更新结束日期
        self.period_end = period_end
        # 记账更新开始日期
        self.period_start = period_start
        # 总数据量
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['periodEnd'] = self.period_end
        if self.period_start is not None:
            result['periodStart'] = self.period_start
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = BillSettementHotelResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('periodEnd') is not None:
            self.period_end = m.get('periodEnd')
        if m.get('periodStart') is not None:
            self.period_start = m.get('periodStart')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class BillSettementHotelResponseBody(TeaModel):
    def __init__(
        self,
        module: BillSettementHotelResponseBodyModule = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
    ):
        # module
        self.module = module
        # 结果code
        self.result_code = result_code
        # 结果msg
        self.result_msg = result_msg
        # 是否成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.result_code is not None:
            result['resultCode'] = self.result_code
        if self.result_msg is not None:
            result['resultMsg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = BillSettementHotelResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')
        if m.get('resultMsg') is not None:
            self.result_msg = m.get('resultMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BillSettementHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BillSettementHotelResponseBody = None,
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
            temp_model = BillSettementHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlightExceedApplyHeaders(TeaModel):
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


class GetFlightExceedApplyRequest(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        corp_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 第三方企业id
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class GetFlightExceedApplyResponseBodyApplyIntentionInfoDO(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: int = None,
        cabin_class_str: str = None,
        dep_city: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        discount: float = None,
        flight_no: str = None,
        price: int = None,
        type: int = None,
    ):
        # 到达城市三字码
        self.arr_city = arr_city
        # 到达城市名称
        self.arr_city_name = arr_city_name
        # 到达时间
        self.arr_time = arr_time
        # 超标的舱位，F：头等舱 C：商务舱 Y：经济舱 P：超值经济舱
        self.cabin = cabin
        # 申请超标的舱等 0：头等舱 1：商务舱 2：经济舱 3：超值经济舱
        self.cabin_class = cabin_class
        # 舱等描述，头等舱，商务舱，经济舱，超值经济舱
        self.cabin_class_str = cabin_class_str
        # 出发城市三字码
        self.dep_city = dep_city
        # 出发城市名称
        self.dep_city_name = dep_city_name
        # 出发时间
        self.dep_time = dep_time
        # 折扣
        self.discount = discount
        # 航班号
        self.flight_no = flight_no
        # 意向航班价格（元）
        self.price = price
        # 超标类型，1:折扣 2,8,10:时间 3,9,11:折扣和时间
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arrCity'] = self.arr_city
        if self.arr_city_name is not None:
            result['arrCityName'] = self.arr_city_name
        if self.arr_time is not None:
            result['arrTime'] = self.arr_time
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabinClass'] = self.cabin_class
        if self.cabin_class_str is not None:
            result['cabinClassStr'] = self.cabin_class_str
        if self.dep_city is not None:
            result['depCity'] = self.dep_city
        if self.dep_city_name is not None:
            result['depCityName'] = self.dep_city_name
        if self.dep_time is not None:
            result['depTime'] = self.dep_time
        if self.discount is not None:
            result['discount'] = self.discount
        if self.flight_no is not None:
            result['flightNo'] = self.flight_no
        if self.price is not None:
            result['price'] = self.price
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrCity') is not None:
            self.arr_city = m.get('arrCity')
        if m.get('arrCityName') is not None:
            self.arr_city_name = m.get('arrCityName')
        if m.get('arrTime') is not None:
            self.arr_time = m.get('arrTime')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabinClass') is not None:
            self.cabin_class = m.get('cabinClass')
        if m.get('cabinClassStr') is not None:
            self.cabin_class_str = m.get('cabinClassStr')
        if m.get('depCity') is not None:
            self.dep_city = m.get('depCity')
        if m.get('depCityName') is not None:
            self.dep_city_name = m.get('depCityName')
        if m.get('depTime') is not None:
            self.dep_time = m.get('depTime')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('flightNo') is not None:
            self.flight_no = m.get('flightNo')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetFlightExceedApplyResponseBody(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: GetFlightExceedApplyResponseBodyApplyIntentionInfoDO = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        user_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 意向出行信息
        self.apply_intention_info_do = apply_intention_info_do
        # 出差原因
        self.btrip_cause = btrip_cause
        # 第三方企业id
        self.corp_id = corp_id
        # 超标原因
        self.exceed_reason = exceed_reason
        # 超标类型，1:折扣 2,8,10:时间 3,9,11:折扣和时间
        self.exceed_type = exceed_type
        # 原差旅标准
        self.origin_standard = origin_standard
        # 审批单状态 0:审批中 1:已同意 2:已拒绝
        self.status = status
        # 审批单提交时间
        self.submit_time = submit_time
        # 第三方出差审批单号
        self.thirdpart_apply_id = thirdpart_apply_id
        # 第三方用户id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['applyIntentionInfoDO'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btripCause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceedReason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceedType'] = self.exceed_type
        if self.origin_standard is not None:
            result['originStandard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpartApplyId'] = self.thirdpart_apply_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('applyIntentionInfoDO') is not None:
            temp_model = GetFlightExceedApplyResponseBodyApplyIntentionInfoDO()
            self.apply_intention_info_do = temp_model.from_map(m['applyIntentionInfoDO'])
        if m.get('btripCause') is not None:
            self.btrip_cause = m.get('btripCause')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('exceedReason') is not None:
            self.exceed_reason = m.get('exceedReason')
        if m.get('exceedType') is not None:
            self.exceed_type = m.get('exceedType')
        if m.get('originStandard') is not None:
            self.origin_standard = m.get('originStandard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        if m.get('thirdpartApplyId') is not None:
            self.thirdpart_apply_id = m.get('thirdpartApplyId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetFlightExceedApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFlightExceedApplyResponseBody = None,
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
            temp_model = GetFlightExceedApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelExceedApplyHeaders(TeaModel):
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


class GetHotelExceedApplyRequest(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        corp_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 第三方企业id
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class GetHotelExceedApplyResponseBodyApplyIntentionInfoDO(TeaModel):
    def __init__(
        self,
        check_in: str = None,
        check_out: str = None,
        city_code: str = None,
        city_name: str = None,
        price: int = None,
        together: bool = None,
        type: int = None,
    ):
        # 入住日期
        self.check_in = check_in
        # 离店日期
        self.check_out = check_out
        # 入住城市三字码
        self.city_code = city_code
        # 入住城市名称
        self.city_name = city_name
        # 意向酒店金额（分）
        self.price = price
        # 是否合住
        self.together = together
        # 超标类型，32：金额超标
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in is not None:
            result['checkIn'] = self.check_in
        if self.check_out is not None:
            result['checkOut'] = self.check_out
        if self.city_code is not None:
            result['cityCode'] = self.city_code
        if self.city_name is not None:
            result['cityName'] = self.city_name
        if self.price is not None:
            result['price'] = self.price
        if self.together is not None:
            result['together'] = self.together
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkIn') is not None:
            self.check_in = m.get('checkIn')
        if m.get('checkOut') is not None:
            self.check_out = m.get('checkOut')
        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')
        if m.get('cityName') is not None:
            self.city_name = m.get('cityName')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('together') is not None:
            self.together = m.get('together')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetHotelExceedApplyResponseBody(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: GetHotelExceedApplyResponseBodyApplyIntentionInfoDO = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        user_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 意向出行信息
        self.apply_intention_info_do = apply_intention_info_do
        # 出差原因
        self.btrip_cause = btrip_cause
        # 第三方企业id
        self.corp_id = corp_id
        # 超标原因
        self.exceed_reason = exceed_reason
        # 超标类型，32：金额超标
        self.exceed_type = exceed_type
        # 原差旅标准
        self.origin_standard = origin_standard
        # 审批单状态 0:审批中 1:已同意 2:已拒绝
        self.status = status
        # 审批单提交时间
        self.submit_time = submit_time
        # 第三方出差审批单号
        self.thirdpart_apply_id = thirdpart_apply_id
        # 第三方用户id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['applyIntentionInfoDO'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btripCause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceedReason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceedType'] = self.exceed_type
        if self.origin_standard is not None:
            result['originStandard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpartApplyId'] = self.thirdpart_apply_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('applyIntentionInfoDO') is not None:
            temp_model = GetHotelExceedApplyResponseBodyApplyIntentionInfoDO()
            self.apply_intention_info_do = temp_model.from_map(m['applyIntentionInfoDO'])
        if m.get('btripCause') is not None:
            self.btrip_cause = m.get('btripCause')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('exceedReason') is not None:
            self.exceed_reason = m.get('exceedReason')
        if m.get('exceedType') is not None:
            self.exceed_type = m.get('exceedType')
        if m.get('originStandard') is not None:
            self.origin_standard = m.get('originStandard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        if m.get('thirdpartApplyId') is not None:
            self.thirdpart_apply_id = m.get('thirdpartApplyId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetHotelExceedApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotelExceedApplyResponseBody = None,
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
            temp_model = GetHotelExceedApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainExceedApplyHeaders(TeaModel):
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


class GetTrainExceedApplyRequest(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        corp_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 第三方企业id
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class GetTrainExceedApplyResponseBodyApplyIntentionInfoDO(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_name: str = None,
        arr_station: str = None,
        arr_time: str = None,
        dep_city: str = None,
        dep_city_name: str = None,
        dep_station: str = None,
        dep_time: str = None,
        price: int = None,
        seat_name: str = None,
        train_no: str = None,
        train_type_desc: str = None,
    ):
        # 到达城市三字码
        self.arr_city = arr_city
        # 到达城市名
        self.arr_city_name = arr_city_name
        # 到达站点名称
        self.arr_station = arr_station
        # 到达时间
        self.arr_time = arr_time
        # 出发城市三字码
        self.dep_city = dep_city
        # 出发城市名
        self.dep_city_name = dep_city_name
        # 出发站点名称
        self.dep_station = dep_station
        # 出发时间
        self.dep_time = dep_time
        # 意向坐席价格（分）
        self.price = price
        # 意向坐席名称
        self.seat_name = seat_name
        # 意向车次号
        self.train_no = train_no
        # 意向车次类型
        self.train_type_desc = train_type_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arrCity'] = self.arr_city
        if self.arr_city_name is not None:
            result['arrCityName'] = self.arr_city_name
        if self.arr_station is not None:
            result['arrStation'] = self.arr_station
        if self.arr_time is not None:
            result['arrTime'] = self.arr_time
        if self.dep_city is not None:
            result['depCity'] = self.dep_city
        if self.dep_city_name is not None:
            result['depCityName'] = self.dep_city_name
        if self.dep_station is not None:
            result['depStation'] = self.dep_station
        if self.dep_time is not None:
            result['depTime'] = self.dep_time
        if self.price is not None:
            result['price'] = self.price
        if self.seat_name is not None:
            result['seatName'] = self.seat_name
        if self.train_no is not None:
            result['trainNo'] = self.train_no
        if self.train_type_desc is not None:
            result['trainTypeDesc'] = self.train_type_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrCity') is not None:
            self.arr_city = m.get('arrCity')
        if m.get('arrCityName') is not None:
            self.arr_city_name = m.get('arrCityName')
        if m.get('arrStation') is not None:
            self.arr_station = m.get('arrStation')
        if m.get('arrTime') is not None:
            self.arr_time = m.get('arrTime')
        if m.get('depCity') is not None:
            self.dep_city = m.get('depCity')
        if m.get('depCityName') is not None:
            self.dep_city_name = m.get('depCityName')
        if m.get('depStation') is not None:
            self.dep_station = m.get('depStation')
        if m.get('depTime') is not None:
            self.dep_time = m.get('depTime')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('seatName') is not None:
            self.seat_name = m.get('seatName')
        if m.get('trainNo') is not None:
            self.train_no = m.get('trainNo')
        if m.get('trainTypeDesc') is not None:
            self.train_type_desc = m.get('trainTypeDesc')
        return self


class GetTrainExceedApplyResponseBody(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: GetTrainExceedApplyResponseBodyApplyIntentionInfoDO = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        user_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 意向出行信息
        self.apply_intention_info_do = apply_intention_info_do
        # 出差原因
        self.btrip_cause = btrip_cause
        # 第三方企业id
        self.corp_id = corp_id
        # 超标原因
        self.exceed_reason = exceed_reason
        # 超标类型，32：坐席超标
        self.exceed_type = exceed_type
        # 原差旅标准
        self.origin_standard = origin_standard
        # 审批单状态 0:审批中 1:已同意 2:已拒绝
        self.status = status
        # 审批单提交时间
        self.submit_time = submit_time
        # 第三方出差审批单号
        self.thirdpart_apply_id = thirdpart_apply_id
        # 第三方用户id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['applyIntentionInfoDO'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btripCause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceedReason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceedType'] = self.exceed_type
        if self.origin_standard is not None:
            result['originStandard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpartApplyId'] = self.thirdpart_apply_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('applyIntentionInfoDO') is not None:
            temp_model = GetTrainExceedApplyResponseBodyApplyIntentionInfoDO()
            self.apply_intention_info_do = temp_model.from_map(m['applyIntentionInfoDO'])
        if m.get('btripCause') is not None:
            self.btrip_cause = m.get('btripCause')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('exceedReason') is not None:
            self.exceed_reason = m.get('exceedReason')
        if m.get('exceedType') is not None:
            self.exceed_type = m.get('exceedType')
        if m.get('originStandard') is not None:
            self.origin_standard = m.get('originStandard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        if m.get('thirdpartApplyId') is not None:
            self.thirdpart_apply_id = m.get('thirdpartApplyId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetTrainExceedApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrainExceedApplyResponseBody = None,
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
            temp_model = GetTrainExceedApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCityCarApplyHeaders(TeaModel):
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


class QueryCityCarApplyRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        created_end_at: str = None,
        created_start_at: str = None,
        page_number: int = None,
        page_size: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        # 第三方企业ID
        self.corp_id = corp_id
        # 审批单创建时间小于值
        self.created_end_at = created_end_at
        # 审批单创建时间大于等于值
        self.created_start_at = created_start_at
        # 页码，要求大于等于1，默认1
        self.page_number = page_number
        # 每页数据量，要求大于等于1，默认20
        self.page_size = page_size
        # 三方审批单ID
        self.third_part_apply_id = third_part_apply_id
        # 第三方员工ID
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
        if self.created_end_at is not None:
            result['createdEndAt'] = self.created_end_at
        if self.created_start_at is not None:
            result['createdStartAt'] = self.created_start_at
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.third_part_apply_id is not None:
            result['thirdPartApplyId'] = self.third_part_apply_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createdEndAt') is not None:
            self.created_end_at = m.get('createdEndAt')
        if m.get('createdStartAt') is not None:
            self.created_start_at = m.get('createdStartAt')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('thirdPartApplyId') is not None:
            self.third_part_apply_id = m.get('thirdPartApplyId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryCityCarApplyResponseBodyApplyListApproverList(TeaModel):
    def __init__(
        self,
        note: str = None,
        operate_time: str = None,
        order: int = None,
        status: int = None,
        status_desc: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 审批备注
        self.note = note
        # 审批时间
        self.operate_time = operate_time
        # 审批人排序值
        self.order = order
        # 审批状态枚举：审批状态：0-审批中，1-已同意，2-已拒绝
        self.status = status
        # 审批状态描述
        self.status_desc = status_desc
        # 审批员工ID
        self.user_id = user_id
        # 审批员工名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['note'] = self.note
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.order is not None:
            result['order'] = self.order
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('note') is not None:
            self.note = m.get('note')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class QueryCityCarApplyResponseBodyApplyListItineraryList(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_id: int = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
    ):
        # 目的地城市
        self.arr_city = arr_city
        # 目的地城市三字码
        self.arr_city_code = arr_city_code
        # 到达目的地城市时间
        self.arr_date = arr_date
        # 商旅内部成本中心ID
        self.cost_center_id = cost_center_id
        # 成本中心名称
        self.cost_center_name = cost_center_name
        # 出发城市
        self.dep_city = dep_city
        # 出发城市三字码
        self.dep_city_code = dep_city_code
        # 出发时间
        self.dep_date = dep_date
        # 商旅内部发票抬头ID
        self.invoice_id = invoice_id
        # 发票抬头名称
        self.invoice_name = invoice_name
        # 商旅内部行程单ID
        self.itinerary_id = itinerary_id
        # 项目code
        self.project_code = project_code
        # 项目名称
        self.project_title = project_title
        # 交通方式：4-市内交通
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arrCity'] = self.arr_city
        if self.arr_city_code is not None:
            result['arrCityCode'] = self.arr_city_code
        if self.arr_date is not None:
            result['arrDate'] = self.arr_date
        if self.cost_center_id is not None:
            result['costCenterId'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['costCenterName'] = self.cost_center_name
        if self.dep_city is not None:
            result['depCity'] = self.dep_city
        if self.dep_city_code is not None:
            result['depCityCode'] = self.dep_city_code
        if self.dep_date is not None:
            result['depDate'] = self.dep_date
        if self.invoice_id is not None:
            result['invoiceId'] = self.invoice_id
        if self.invoice_name is not None:
            result['invoiceName'] = self.invoice_name
        if self.itinerary_id is not None:
            result['itineraryId'] = self.itinerary_id
        if self.project_code is not None:
            result['projectCode'] = self.project_code
        if self.project_title is not None:
            result['projectTitle'] = self.project_title
        if self.traffic_type is not None:
            result['trafficType'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrCity') is not None:
            self.arr_city = m.get('arrCity')
        if m.get('arrCityCode') is not None:
            self.arr_city_code = m.get('arrCityCode')
        if m.get('arrDate') is not None:
            self.arr_date = m.get('arrDate')
        if m.get('costCenterId') is not None:
            self.cost_center_id = m.get('costCenterId')
        if m.get('costCenterName') is not None:
            self.cost_center_name = m.get('costCenterName')
        if m.get('depCity') is not None:
            self.dep_city = m.get('depCity')
        if m.get('depCityCode') is not None:
            self.dep_city_code = m.get('depCityCode')
        if m.get('depDate') is not None:
            self.dep_date = m.get('depDate')
        if m.get('invoiceId') is not None:
            self.invoice_id = m.get('invoiceId')
        if m.get('invoiceName') is not None:
            self.invoice_name = m.get('invoiceName')
        if m.get('itineraryId') is not None:
            self.itinerary_id = m.get('itineraryId')
        if m.get('projectCode') is not None:
            self.project_code = m.get('projectCode')
        if m.get('projectTitle') is not None:
            self.project_title = m.get('projectTitle')
        if m.get('trafficType') is not None:
            self.traffic_type = m.get('trafficType')
        return self


class QueryCityCarApplyResponseBodyApplyList(TeaModel):
    def __init__(
        self,
        approver_list: List[QueryCityCarApplyResponseBodyApplyListApproverList] = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        itinerary_list: List[QueryCityCarApplyResponseBodyApplyListItineraryList] = None,
        status: int = None,
        status_desc: str = None,
        third_part_apply_id: str = None,
        trip_cause: str = None,
        trip_title: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 审批单列表
        self.approver_list = approver_list
        # 员工所在部门ID
        self.depart_id = depart_id
        # 员工所在部门名
        self.depart_name = depart_name
        # 创建时间
        self.gmt_create = gmt_create
        # 最近修改时间
        self.gmt_modified = gmt_modified
        # 审批单关联的行程
        self.itinerary_list = itinerary_list
        # 审批单状态：0-申请，1-同意，2-拒绝
        self.status = status
        # 审批单状态：0-申请，1-同意，2-拒绝
        self.status_desc = status_desc
        # 三方审批单ID
        self.third_part_apply_id = third_part_apply_id
        # 申请事由
        self.trip_cause = trip_cause
        # 审批单标题
        self.trip_title = trip_title
        # 发起审批员工ID
        self.user_id = user_id
        # 发起审批员工名
        self.user_name = user_name

    def validate(self):
        if self.approver_list:
            for k in self.approver_list:
                if k:
                    k.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['approverList'] = []
        if self.approver_list is not None:
            for k in self.approver_list:
                result['approverList'].append(k.to_map() if k else None)
        if self.depart_id is not None:
            result['departId'] = self.depart_id
        if self.depart_name is not None:
            result['departName'] = self.depart_name
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        result['itineraryList'] = []
        if self.itinerary_list is not None:
            for k in self.itinerary_list:
                result['itineraryList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        if self.third_part_apply_id is not None:
            result['thirdPartApplyId'] = self.third_part_apply_id
        if self.trip_cause is not None:
            result['tripCause'] = self.trip_cause
        if self.trip_title is not None:
            result['tripTitle'] = self.trip_title
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_list = []
        if m.get('approverList') is not None:
            for k in m.get('approverList'):
                temp_model = QueryCityCarApplyResponseBodyApplyListApproverList()
                self.approver_list.append(temp_model.from_map(k))
        if m.get('departId') is not None:
            self.depart_id = m.get('departId')
        if m.get('departName') is not None:
            self.depart_name = m.get('departName')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        self.itinerary_list = []
        if m.get('itineraryList') is not None:
            for k in m.get('itineraryList'):
                temp_model = QueryCityCarApplyResponseBodyApplyListItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        if m.get('thirdPartApplyId') is not None:
            self.third_part_apply_id = m.get('thirdPartApplyId')
        if m.get('tripCause') is not None:
            self.trip_cause = m.get('tripCause')
        if m.get('tripTitle') is not None:
            self.trip_title = m.get('tripTitle')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class QueryCityCarApplyResponseBody(TeaModel):
    def __init__(
        self,
        apply_list: List[QueryCityCarApplyResponseBodyApplyList] = None,
        total: int = None,
    ):
        # 审批单列表
        self.apply_list = apply_list
        # 总数
        self.total = total

    def validate(self):
        if self.apply_list:
            for k in self.apply_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyList'] = []
        if self.apply_list is not None:
            for k in self.apply_list:
                result['applyList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_list = []
        if m.get('applyList') is not None:
            for k in m.get('applyList'):
                temp_model = QueryCityCarApplyResponseBodyApplyList()
                self.apply_list.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryCityCarApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCityCarApplyResponseBody = None,
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
            temp_model = QueryCityCarApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnionOrderHeaders(TeaModel):
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


class QueryUnionOrderRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        third_part_apply_id: str = None,
        union_no: str = None,
    ):
        # 第三方企业id
        self.corp_id = corp_id
        # 第三方申请单id
        self.third_part_apply_id = third_part_apply_id
        # 关联单号
        self.union_no = union_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.third_part_apply_id is not None:
            result['thirdPartApplyId'] = self.third_part_apply_id
        if self.union_no is not None:
            result['unionNo'] = self.union_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('thirdPartApplyId') is not None:
            self.third_part_apply_id = m.get('thirdPartApplyId')
        if m.get('unionNo') is not None:
            self.union_no = m.get('unionNo')
        return self


class QueryUnionOrderResponseBodyFlightList(TeaModel):
    def __init__(
        self,
        flight_order_id: int = None,
        flight_order_status: int = None,
    ):
        # 订单id
        self.flight_order_id = flight_order_id
        # 订单状态：0待支付,1出票中,2已关闭,3有改签单,4有退票单,5出票成功,6退票申请中,7改签申请中
        self.flight_order_status = flight_order_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flight_order_id is not None:
            result['flightOrderId'] = self.flight_order_id
        if self.flight_order_status is not None:
            result['flightOrderStatus'] = self.flight_order_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flightOrderId') is not None:
            self.flight_order_id = m.get('flightOrderId')
        if m.get('flightOrderStatus') is not None:
            self.flight_order_status = m.get('flightOrderStatus')
        return self


class QueryUnionOrderResponseBodyHotelList(TeaModel):
    def __init__(
        self,
        hotel_order_id: int = None,
        hotel_order_status: int = None,
    ):
        # 酒店订单号
        self.hotel_order_id = hotel_order_id
        # 订单状态1:等待确认,2:等待付款,3:预订成功,4:申请退款,5:退款成功,6:已关闭,7:结账成功,8:支付成功
        self.hotel_order_status = hotel_order_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_order_id is not None:
            result['hotelOrderId'] = self.hotel_order_id
        if self.hotel_order_status is not None:
            result['hotelOrderStatus'] = self.hotel_order_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotelOrderId') is not None:
            self.hotel_order_id = m.get('hotelOrderId')
        if m.get('hotelOrderStatus') is not None:
            self.hotel_order_status = m.get('hotelOrderStatus')
        return self


class QueryUnionOrderResponseBodyTrainList(TeaModel):
    def __init__(
        self,
        train_order_id: int = None,
        train_orderstatus: int = None,
    ):
        # 火车订单号
        self.train_order_id = train_order_id
        # 订单状态：0待支付,1出票中,2已关闭,3,改签成功,4退票成功,5出票完成,6退票申请中,7改签申请中,8已出票,已发货,9出票失败,10改签失败,11退票失败
        self.train_orderstatus = train_orderstatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.train_order_id is not None:
            result['trainOrderId'] = self.train_order_id
        if self.train_orderstatus is not None:
            result['trainOrderstatus'] = self.train_orderstatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('trainOrderId') is not None:
            self.train_order_id = m.get('trainOrderId')
        if m.get('trainOrderstatus') is not None:
            self.train_orderstatus = m.get('trainOrderstatus')
        return self


class QueryUnionOrderResponseBodyVehicleList(TeaModel):
    def __init__(
        self,
        vehicle_order_id: int = None,
        vehicle_order_status: int = None,
    ):
        # 用车订单号
        self.vehicle_order_id = vehicle_order_id
        # 订单状态:0:初始状态,1:已超时,2:派单成功,3:派单失败,4:已退款,5:已支付,6:已取消
        self.vehicle_order_status = vehicle_order_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vehicle_order_id is not None:
            result['vehicleOrderId'] = self.vehicle_order_id
        if self.vehicle_order_status is not None:
            result['vehicleOrderStatus'] = self.vehicle_order_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vehicleOrderId') is not None:
            self.vehicle_order_id = m.get('vehicleOrderId')
        if m.get('vehicleOrderStatus') is not None:
            self.vehicle_order_status = m.get('vehicleOrderStatus')
        return self


class QueryUnionOrderResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        flight_list: List[QueryUnionOrderResponseBodyFlightList] = None,
        hotel_list: List[QueryUnionOrderResponseBodyHotelList] = None,
        train_list: List[QueryUnionOrderResponseBodyTrainList] = None,
        vehicle_list: List[QueryUnionOrderResponseBodyVehicleList] = None,
    ):
        # 企业id
        self.corp_id = corp_id
        # 飞机订单信息
        self.flight_list = flight_list
        # 酒店订单信息
        self.hotel_list = hotel_list
        # 火车订单信息
        self.train_list = train_list
        # 用车订单信息
        self.vehicle_list = vehicle_list

    def validate(self):
        if self.flight_list:
            for k in self.flight_list:
                if k:
                    k.validate()
        if self.hotel_list:
            for k in self.hotel_list:
                if k:
                    k.validate()
        if self.train_list:
            for k in self.train_list:
                if k:
                    k.validate()
        if self.vehicle_list:
            for k in self.vehicle_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['flightList'] = []
        if self.flight_list is not None:
            for k in self.flight_list:
                result['flightList'].append(k.to_map() if k else None)
        result['hotelList'] = []
        if self.hotel_list is not None:
            for k in self.hotel_list:
                result['hotelList'].append(k.to_map() if k else None)
        result['trainList'] = []
        if self.train_list is not None:
            for k in self.train_list:
                result['trainList'].append(k.to_map() if k else None)
        result['vehicleList'] = []
        if self.vehicle_list is not None:
            for k in self.vehicle_list:
                result['vehicleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.flight_list = []
        if m.get('flightList') is not None:
            for k in m.get('flightList'):
                temp_model = QueryUnionOrderResponseBodyFlightList()
                self.flight_list.append(temp_model.from_map(k))
        self.hotel_list = []
        if m.get('hotelList') is not None:
            for k in m.get('hotelList'):
                temp_model = QueryUnionOrderResponseBodyHotelList()
                self.hotel_list.append(temp_model.from_map(k))
        self.train_list = []
        if m.get('trainList') is not None:
            for k in m.get('trainList'):
                temp_model = QueryUnionOrderResponseBodyTrainList()
                self.train_list.append(temp_model.from_map(k))
        self.vehicle_list = []
        if m.get('vehicleList') is not None:
            for k in m.get('vehicleList'):
                temp_model = QueryUnionOrderResponseBodyVehicleList()
                self.vehicle_list.append(temp_model.from_map(k))
        return self


class QueryUnionOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUnionOrderResponseBody = None,
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
            temp_model = QueryUnionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncExceedApplyHeaders(TeaModel):
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


class SyncExceedApplyRequest(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        corp_id: str = None,
        remark: str = None,
        status: int = None,
        thirdparty_flow_id: str = None,
        user_id: str = None,
    ):
        # 商旅超标审批单id
        self.apply_id = apply_id
        # 企业id
        self.corp_id = corp_id
        # 审批意见
        self.remark = remark
        # 审批单状态 1同意2拒绝
        self.status = status
        # 第三方流程实例id
        self.thirdparty_flow_id = thirdparty_flow_id
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.thirdparty_flow_id is not None:
            result['thirdpartyFlowId'] = self.thirdparty_flow_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpartyFlowId') is not None:
            self.thirdparty_flow_id = m.get('thirdpartyFlowId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SyncExceedApplyResponseBody(TeaModel):
    def __init__(
        self,
        module: bool = None,
    ):
        # 是否同步成功
        self.module = module

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class SyncExceedApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncExceedApplyResponseBody = None,
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
            temp_model = SyncExceedApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


