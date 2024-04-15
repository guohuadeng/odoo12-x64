# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class IndustrializeManufactureJobBookRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        extend: str = None,
        inst_no: str = None,
        is_batch_job: str = None,
        manufacture_date: str = None,
        mes_app_key: str = None,
        process_en_name: str = None,
        process_name: str = None,
        product_code: str = None,
        product_en_name: str = None,
        product_name: str = None,
        product_specification: str = None,
        qualified_quantity: str = None,
        reworkable_quantity: str = None,
        scrapped_quantity: str = None,
        unit_price: str = None,
        user_id_list: str = None,
        user_name: str = None,
        user_name_list: str = None,
        uuid: str = None,
    ):
        # 钉钉组织id
        self.corp_id = corp_id
        # 扩展字段，用于增加自定义字段
        self.extend = extend
        # 工单编号
        self.inst_no = inst_no
        # 是否是批量报工(取值[n,y])
        self.is_batch_job = is_batch_job
        # 生产日期时间(到时分秒)
        self.manufacture_date = manufacture_date
        # mes 系统唯一标识
        self.mes_app_key = mes_app_key
        # 制程英文名称
        self.process_en_name = process_en_name
        # 制程名称
        self.process_name = process_name
        # 产品唯一标识
        self.product_code = product_code
        # 产品英文名称
        self.product_en_name = product_en_name
        # 产品名称，例如"双头螺柱001"
        self.product_name = product_name
        # 产品规格
        self.product_specification = product_specification
        # 合格数量
        self.qualified_quantity = qualified_quantity
        # 可重工数量
        self.reworkable_quantity = reworkable_quantity
        # 报废数量
        self.scrapped_quantity = scrapped_quantity
        # 计件单价，单位：分
        self.unit_price = unit_price
        # 批量报工时多个工人userId以英文逗号分隔
        self.user_id_list = user_id_list
        # 员工姓名
        self.user_name = user_name
        # 批量报工时多个人名以英文逗号分隔
        self.user_name_list = user_name_list
        # 随机串，唯一标识(用于幂等及更新)
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
        if self.extend is not None:
            result['extend'] = self.extend
        if self.inst_no is not None:
            result['instNo'] = self.inst_no
        if self.is_batch_job is not None:
            result['isBatchJob'] = self.is_batch_job
        if self.manufacture_date is not None:
            result['manufactureDate'] = self.manufacture_date
        if self.mes_app_key is not None:
            result['mesAppKey'] = self.mes_app_key
        if self.process_en_name is not None:
            result['processEnName'] = self.process_en_name
        if self.process_name is not None:
            result['processName'] = self.process_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_en_name is not None:
            result['productEnName'] = self.product_en_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_specification is not None:
            result['productSpecification'] = self.product_specification
        if self.qualified_quantity is not None:
            result['qualifiedQuantity'] = self.qualified_quantity
        if self.reworkable_quantity is not None:
            result['reworkableQuantity'] = self.reworkable_quantity
        if self.scrapped_quantity is not None:
            result['scrappedQuantity'] = self.scrapped_quantity
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_name_list is not None:
            result['userNameList'] = self.user_name_list
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('instNo') is not None:
            self.inst_no = m.get('instNo')
        if m.get('isBatchJob') is not None:
            self.is_batch_job = m.get('isBatchJob')
        if m.get('manufactureDate') is not None:
            self.manufacture_date = m.get('manufactureDate')
        if m.get('mesAppKey') is not None:
            self.mes_app_key = m.get('mesAppKey')
        if m.get('processEnName') is not None:
            self.process_en_name = m.get('processEnName')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productEnName') is not None:
            self.product_en_name = m.get('productEnName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productSpecification') is not None:
            self.product_specification = m.get('productSpecification')
        if m.get('qualifiedQuantity') is not None:
            self.qualified_quantity = m.get('qualifiedQuantity')
        if m.get('reworkableQuantity') is not None:
            self.reworkable_quantity = m.get('reworkableQuantity')
        if m.get('scrappedQuantity') is not None:
            self.scrapped_quantity = m.get('scrappedQuantity')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userNameList') is not None:
            self.user_name_list = m.get('userNameList')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class IndustrializeManufactureJobBookResponseBodyContent(TeaModel):
    def __init__(
        self,
        count: int = None,
        id: int = None,
    ):
        # 影响行数
        self.count = count
        # 新增记录的数据库id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class IndustrializeManufactureJobBookResponseBody(TeaModel):
    def __init__(
        self,
        content: IndustrializeManufactureJobBookResponseBodyContent = None,
        error_code: str = None,
        error_level: int = None,
        error_msg: str = None,
        http_code: str = None,
        success: bool = None,
        uuid: str = None,
    ):
        # content
        self.content = content
        # errorCode
        self.error_code = error_code
        # errorLevel
        self.error_level = error_level
        # errorMsg
        self.error_msg = error_msg
        # httpCode
        self.http_code = http_code
        # success
        self.success = success
        # 此次报工记录的唯一标识
        self.uuid = uuid

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_level is not None:
            result['errorLevel'] = self.error_level
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.success is not None:
            result['success'] = self.success
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = IndustrializeManufactureJobBookResponseBodyContent()
            self.content = temp_model.from_map(m['content'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorLevel') is not None:
            self.error_level = m.get('errorLevel')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class IndustrializeManufactureJobBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IndustrializeManufactureJobBookResponseBody = None,
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
            temp_model = IndustrializeManufactureJobBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndustrializeManufactureQueryJobsHeaders(TeaModel):
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


class IndustrializeManufactureQueryJobsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        inst_no: str = None,
        manufacture_day: str = None,
        mes_app_key: str = None,
        page_size: int = None,
        process_name: str = None,
        product_code: str = None,
        product_name: str = None,
        product_specification: str = None,
        qualified_quantity: str = None,
        unit_price: str = None,
        user_id: str = None,
        user_id_list: str = None,
        user_name: str = None,
        uuid: str = None,
    ):
        # 当前页序号(从1开始)
        self.current_page = current_page
        # 工单编号
        self.inst_no = inst_no
        # 生产日期
        self.manufacture_day = manufacture_day
        # MES系统唯一标识
        self.mes_app_key = mes_app_key
        # 每页显示记录条数
        self.page_size = page_size
        # 工序名称
        self.process_name = process_name
        # 产品唯一标识
        self.product_code = product_code
        # 产品中文名称
        self.product_name = product_name
        # 产品规格
        self.product_specification = product_specification
        # 报工合格数量
        self.qualified_quantity = qualified_quantity
        # 计件单价，单位：分
        self.unit_price = unit_price
        # 员工钉钉userId
        self.user_id = user_id
        # 批量报工时多个人钉钉工号以英文逗号分隔
        self.user_id_list = user_id_list
        # 员工姓名
        self.user_name = user_name
        # 报工记录的唯一标识
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.inst_no is not None:
            result['instNo'] = self.inst_no
        if self.manufacture_day is not None:
            result['manufactureDay'] = self.manufacture_day
        if self.mes_app_key is not None:
            result['mesAppKey'] = self.mes_app_key
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.process_name is not None:
            result['processName'] = self.process_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_specification is not None:
            result['productSpecification'] = self.product_specification
        if self.qualified_quantity is not None:
            result['qualifiedQuantity'] = self.qualified_quantity
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('instNo') is not None:
            self.inst_no = m.get('instNo')
        if m.get('manufactureDay') is not None:
            self.manufacture_day = m.get('manufactureDay')
        if m.get('mesAppKey') is not None:
            self.mes_app_key = m.get('mesAppKey')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productSpecification') is not None:
            self.product_specification = m.get('productSpecification')
        if m.get('qualifiedQuantity') is not None:
            self.qualified_quantity = m.get('qualifiedQuantity')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class IndustrializeManufactureQueryJobsResponseBodyContent(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        inst_no: str = None,
        is_batch_job: str = None,
        manufacture_date: str = None,
        manufacture_day: str = None,
        mes_app_key: str = None,
        process_name: str = None,
        qualified_quantity: str = None,
        scrapped_quantity: str = None,
        unit_price: str = None,
        user_id: str = None,
        user_id_list: str = None,
        user_name_list: str = None,
        uuid: str = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据库id
        self.id = id
        # 工单id
        self.inst_no = inst_no
        # 是否是批量报工，即一次报工由多个工人一起分担，取值[n,y],y表示是批量，批量时多个人名以英文逗号分隔
        self.is_batch_job = is_batch_job
        # 生产日期时间(到时分秒),格式:2021-07-05 08:00:21
        self.manufacture_date = manufacture_date
        # 生产日期(到天)
        self.manufacture_day = manufacture_day
        # 分配给mes系统的appkey
        self.mes_app_key = mes_app_key
        # 工序名称
        self.process_name = process_name
        # 合格数
        self.qualified_quantity = qualified_quantity
        # 不合格数
        self.scrapped_quantity = scrapped_quantity
        # 计件单价，单位：分
        self.unit_price = unit_price
        # 工人工号(isBatchJob=='n'时)
        self.user_id = user_id
        # 批量报工时多个人钉钉工号以英文逗号分隔
        self.user_id_list = user_id_list
        # 批量报工时多个人名以英文逗号分隔
        self.user_name_list = user_name_list
        # 报工记录的唯一标识
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
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.inst_no is not None:
            result['instNo'] = self.inst_no
        if self.is_batch_job is not None:
            result['isBatchJob'] = self.is_batch_job
        if self.manufacture_date is not None:
            result['manufactureDate'] = self.manufacture_date
        if self.manufacture_day is not None:
            result['manufactureDay'] = self.manufacture_day
        if self.mes_app_key is not None:
            result['mesAppKey'] = self.mes_app_key
        if self.process_name is not None:
            result['processName'] = self.process_name
        if self.qualified_quantity is not None:
            result['qualifiedQuantity'] = self.qualified_quantity
        if self.scrapped_quantity is not None:
            result['scrappedQuantity'] = self.scrapped_quantity
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_id_list is not None:
            result['userIdList'] = self.user_id_list
        if self.user_name_list is not None:
            result['userNameList'] = self.user_name_list
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instNo') is not None:
            self.inst_no = m.get('instNo')
        if m.get('isBatchJob') is not None:
            self.is_batch_job = m.get('isBatchJob')
        if m.get('manufactureDate') is not None:
            self.manufacture_date = m.get('manufactureDate')
        if m.get('manufactureDay') is not None:
            self.manufacture_day = m.get('manufactureDay')
        if m.get('mesAppKey') is not None:
            self.mes_app_key = m.get('mesAppKey')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        if m.get('qualifiedQuantity') is not None:
            self.qualified_quantity = m.get('qualifiedQuantity')
        if m.get('scrappedQuantity') is not None:
            self.scrapped_quantity = m.get('scrappedQuantity')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userIdList') is not None:
            self.user_id_list = m.get('userIdList')
        if m.get('userNameList') is not None:
            self.user_name_list = m.get('userNameList')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class IndustrializeManufactureQueryJobsResponseBody(TeaModel):
    def __init__(
        self,
        content: IndustrializeManufactureQueryJobsResponseBodyContent = None,
        http_code: str = None,
    ):
        # 查询的数据结果
        self.content = content
        # httpCode
        self.http_code = http_code

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = IndustrializeManufactureQueryJobsResponseBodyContent()
            self.content = temp_model.from_map(m['content'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        return self


class IndustrializeManufactureQueryJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IndustrializeManufactureQueryJobsResponseBody = None,
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
            temp_model = IndustrializeManufactureQueryJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


