# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class EditContactHeaders(TeaModel):
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


class EditContactRequestData(TeaModel):
    def __init__(
        self,
        data_userid: str = None,
        lxr_address: str = None,
        lxr_birthday: str = None,
        lxr_chengwei: str = None,
        lxr_ctnumber: str = None,
        lxr_cttype: str = None,
        lxr_customerid: str = None,
        lxr_department: str = None,
        lxr_dingtalk: str = None,
        lxr_email: str = None,
        lxr_fax: str = None,
        lxr_group: str = None,
        lxr_handset: str = None,
        lxr_headship: str = None,
        lxr_like: str = None,
        lxr_name: str = None,
        lxr_photo: str = None,
        lxr_preside: str = None,
        lxr_pst: str = None,
        lxr_qq: str = None,
        lxr_remark: str = None,
        lxr_sex: str = None,
        lxr_skype: str = None,
        lxr_tel: str = None,
        lxr_type: str = None,
        lxr_wangwang: str = None,
        lxr_weixin: str = None,
        lxr_worktel: str = None,
    ):
        # 创建人
        self.data_userid = data_userid
        # 住址
        self.lxr_address = lxr_address
        # 生日
        self.lxr_birthday = lxr_birthday
        # 称谓
        self.lxr_chengwei = lxr_chengwei
        # 证件号码
        self.lxr_ctnumber = lxr_ctnumber
        # 证件类型
        self.lxr_cttype = lxr_cttype
        # 对应客户
        self.lxr_customerid = lxr_customerid
        # 部门
        self.lxr_department = lxr_department
        # 钉钉号
        self.lxr_dingtalk = lxr_dingtalk
        # Email
        self.lxr_email = lxr_email
        # 传真
        self.lxr_fax = lxr_fax
        # 分类
        self.lxr_group = lxr_group
        # 手机
        self.lxr_handset = lxr_handset
        # 职务
        self.lxr_headship = lxr_headship
        # 爱好
        self.lxr_like = lxr_like
        # 姓名
        self.lxr_name = lxr_name
        # 联系名片
        self.lxr_photo = lxr_photo
        # 负责业务
        self.lxr_preside = lxr_preside
        # 邮编
        self.lxr_pst = lxr_pst
        # QQ
        self.lxr_qq = lxr_qq
        # 备注
        self.lxr_remark = lxr_remark
        # 性别（男，女）
        self.lxr_sex = lxr_sex
        # Skype
        self.lxr_skype = lxr_skype
        # 家庭电话
        self.lxr_tel = lxr_tel
        # 类型（联系人，主联系人）
        self.lxr_type = lxr_type
        # 旺旺
        self.lxr_wangwang = lxr_wangwang
        # 微信号
        self.lxr_weixin = lxr_weixin
        # 工作电话
        self.lxr_worktel = lxr_worktel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.lxr_address is not None:
            result['lxr_address'] = self.lxr_address
        if self.lxr_birthday is not None:
            result['lxr_birthday'] = self.lxr_birthday
        if self.lxr_chengwei is not None:
            result['lxr_chengwei'] = self.lxr_chengwei
        if self.lxr_ctnumber is not None:
            result['lxr_ctnumber'] = self.lxr_ctnumber
        if self.lxr_cttype is not None:
            result['lxr_cttype'] = self.lxr_cttype
        if self.lxr_customerid is not None:
            result['lxr_customerid'] = self.lxr_customerid
        if self.lxr_department is not None:
            result['lxr_department'] = self.lxr_department
        if self.lxr_dingtalk is not None:
            result['lxr_dingtalk'] = self.lxr_dingtalk
        if self.lxr_email is not None:
            result['lxr_email'] = self.lxr_email
        if self.lxr_fax is not None:
            result['lxr_fax'] = self.lxr_fax
        if self.lxr_group is not None:
            result['lxr_group'] = self.lxr_group
        if self.lxr_handset is not None:
            result['lxr_handset'] = self.lxr_handset
        if self.lxr_headship is not None:
            result['lxr_headship'] = self.lxr_headship
        if self.lxr_like is not None:
            result['lxr_like'] = self.lxr_like
        if self.lxr_name is not None:
            result['lxr_name'] = self.lxr_name
        if self.lxr_photo is not None:
            result['lxr_photo'] = self.lxr_photo
        if self.lxr_preside is not None:
            result['lxr_preside'] = self.lxr_preside
        if self.lxr_pst is not None:
            result['lxr_pst'] = self.lxr_pst
        if self.lxr_qq is not None:
            result['lxr_qq'] = self.lxr_qq
        if self.lxr_remark is not None:
            result['lxr_remark'] = self.lxr_remark
        if self.lxr_sex is not None:
            result['lxr_sex'] = self.lxr_sex
        if self.lxr_skype is not None:
            result['lxr_skype'] = self.lxr_skype
        if self.lxr_tel is not None:
            result['lxr_tel'] = self.lxr_tel
        if self.lxr_type is not None:
            result['lxr_type'] = self.lxr_type
        if self.lxr_wangwang is not None:
            result['lxr_wangwang'] = self.lxr_wangwang
        if self.lxr_weixin is not None:
            result['lxr_weixin'] = self.lxr_weixin
        if self.lxr_worktel is not None:
            result['lxr_worktel'] = self.lxr_worktel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('lxr_address') is not None:
            self.lxr_address = m.get('lxr_address')
        if m.get('lxr_birthday') is not None:
            self.lxr_birthday = m.get('lxr_birthday')
        if m.get('lxr_chengwei') is not None:
            self.lxr_chengwei = m.get('lxr_chengwei')
        if m.get('lxr_ctnumber') is not None:
            self.lxr_ctnumber = m.get('lxr_ctnumber')
        if m.get('lxr_cttype') is not None:
            self.lxr_cttype = m.get('lxr_cttype')
        if m.get('lxr_customerid') is not None:
            self.lxr_customerid = m.get('lxr_customerid')
        if m.get('lxr_department') is not None:
            self.lxr_department = m.get('lxr_department')
        if m.get('lxr_dingtalk') is not None:
            self.lxr_dingtalk = m.get('lxr_dingtalk')
        if m.get('lxr_email') is not None:
            self.lxr_email = m.get('lxr_email')
        if m.get('lxr_fax') is not None:
            self.lxr_fax = m.get('lxr_fax')
        if m.get('lxr_group') is not None:
            self.lxr_group = m.get('lxr_group')
        if m.get('lxr_handset') is not None:
            self.lxr_handset = m.get('lxr_handset')
        if m.get('lxr_headship') is not None:
            self.lxr_headship = m.get('lxr_headship')
        if m.get('lxr_like') is not None:
            self.lxr_like = m.get('lxr_like')
        if m.get('lxr_name') is not None:
            self.lxr_name = m.get('lxr_name')
        if m.get('lxr_photo') is not None:
            self.lxr_photo = m.get('lxr_photo')
        if m.get('lxr_preside') is not None:
            self.lxr_preside = m.get('lxr_preside')
        if m.get('lxr_pst') is not None:
            self.lxr_pst = m.get('lxr_pst')
        if m.get('lxr_qq') is not None:
            self.lxr_qq = m.get('lxr_qq')
        if m.get('lxr_remark') is not None:
            self.lxr_remark = m.get('lxr_remark')
        if m.get('lxr_sex') is not None:
            self.lxr_sex = m.get('lxr_sex')
        if m.get('lxr_skype') is not None:
            self.lxr_skype = m.get('lxr_skype')
        if m.get('lxr_tel') is not None:
            self.lxr_tel = m.get('lxr_tel')
        if m.get('lxr_type') is not None:
            self.lxr_type = m.get('lxr_type')
        if m.get('lxr_wangwang') is not None:
            self.lxr_wangwang = m.get('lxr_wangwang')
        if m.get('lxr_weixin') is not None:
            self.lxr_weixin = m.get('lxr_weixin')
        if m.get('lxr_worktel') is not None:
            self.lxr_worktel = m.get('lxr_worktel')
        return self


class EditContactRequest(TeaModel):
    def __init__(
        self,
        data: EditContactRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写197
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditContactRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditContactResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditContactResponseBody = None,
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
            temp_model = EditContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditCustomerHeaders(TeaModel):
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


class EditCustomerRequestData(TeaModel):
    def __init__(
        self,
        data_userid: str = None,
        kh_address: str = None,
        kh_appellation: str = None,
        kh_befontof: str = None,
        kh_billinfo: str = None,
        kh_city: str = None,
        kh_class: str = None,
        kh_coaddress: str = None,
        kh_contype: str = None,
        kh_country: str = None,
        kh_creditgrade: str = None,
        kh_ctnumber: str = None,
        kh_cttype: str = None,
        kh_department: str = None,
        kh_dingtalk: str = None,
        kh_email: str = None,
        kh_employees: str = None,
        kh_fax: str = None,
        kh_from: str = None,
        kh_handset: str = None,
        kh_headship: str = None,
        kh_hotfl: str = None,
        kh_hotlevel: str = None,
        kh_hotmemo: str = None,
        kh_hottype: str = None,
        kh_industry: str = None,
        kh_info: str = None,
        kh_jibie: str = None,
        kh_name: str = None,
        kh_pkhid: str = None,
        kh_preside: str = None,
        kh_province: str = None,
        kh_pst: str = None,
        kh_qq: str = None,
        kh_ralagrade: str = None,
        kh_remark: str = None,
        kh_sex: str = None,
        kh_shortname: str = None,
        kh_skype: str = None,
        kh_sn: str = None,
        kh_status: str = None,
        kh_tel: str = None,
        kh_type: str = None,
        kh_valrating: str = None,
        kh_wangwang: str = None,
        kh_web: str = None,
        kh_weixin: str = None,
        kh_worktel: str = None,
    ):
        # 创建人
        self.data_userid = data_userid
        # 家庭地址
        self.kh_address = kh_address
        # 称谓
        self.kh_appellation = kh_appellation
        # 爱好
        self.kh_befontof = kh_befontof
        # 开票资料
        self.kh_billinfo = kh_billinfo
        # 城市
        self.kh_city = kh_city
        # 类别（企业客户，个人客户，供应商，个人供应商）
        self.kh_class = kh_class
        # 单位地址
        self.kh_coaddress = kh_coaddress
        # 联系人分类
        self.kh_contype = kh_contype
        # 国家地区
        self.kh_country = kh_country
        # 信用等级（低，中，高）
        self.kh_creditgrade = kh_creditgrade
        # 证件号码
        self.kh_ctnumber = kh_ctnumber
        # 证件类型
        self.kh_cttype = kh_cttype
        # 部门
        self.kh_department = kh_department
        # 钉钉号
        self.kh_dingtalk = kh_dingtalk
        # 邮箱
        self.kh_email = kh_email
        # 人员规模
        self.kh_employees = kh_employees
        # 传真
        self.kh_fax = kh_fax
        # 来源
        self.kh_from = kh_from
        # 手机
        self.kh_handset = kh_handset
        # 职务
        self.kh_headship = kh_headship
        # 热点分类
        self.kh_hotfl = kh_hotfl
        # 热度（无，低热，中热，高热）
        self.kh_hotlevel = kh_hotlevel
        # 热点说明
        self.kh_hotmemo = kh_hotmemo
        # 热点客户（是，否）
        self.kh_hottype = kh_hottype
        # 行业
        self.kh_industry = kh_industry
        # 公司简介
        self.kh_info = kh_info
        # 客户级别
        self.kh_jibie = kh_jibie
        # 客户名称
        self.kh_name = kh_name
        # 上级客户
        self.kh_pkhid = kh_pkhid
        # 负责业务
        self.kh_preside = kh_preside
        # 省份
        self.kh_province = kh_province
        # 邮编
        self.kh_pst = kh_pst
        # QQ
        self.kh_qq = kh_qq
        # 关系等级
        self.kh_ralagrade = kh_ralagrade
        # 备注
        self.kh_remark = kh_remark
        # 性别（男，女）
        self.kh_sex = kh_sex
        # 助记简称
        self.kh_shortname = kh_shortname
        # Skype
        self.kh_skype = kh_skype
        # 编号
        self.kh_sn = kh_sn
        # 阶段
        self.kh_status = kh_status
        # 家庭电话
        self.kh_tel = kh_tel
        # 种类
        self.kh_type = kh_type
        # 价值评估（低，中，高）
        self.kh_valrating = kh_valrating
        # 旺旺
        self.kh_wangwang = kh_wangwang
        # 网址
        self.kh_web = kh_web
        # 微信号
        self.kh_weixin = kh_weixin
        # 工作电话
        self.kh_worktel = kh_worktel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.kh_address is not None:
            result['kh_address'] = self.kh_address
        if self.kh_appellation is not None:
            result['kh_appellation'] = self.kh_appellation
        if self.kh_befontof is not None:
            result['kh_befontof'] = self.kh_befontof
        if self.kh_billinfo is not None:
            result['kh_billinfo'] = self.kh_billinfo
        if self.kh_city is not None:
            result['kh_city'] = self.kh_city
        if self.kh_class is not None:
            result['kh_class'] = self.kh_class
        if self.kh_coaddress is not None:
            result['kh_coaddress'] = self.kh_coaddress
        if self.kh_contype is not None:
            result['kh_contype'] = self.kh_contype
        if self.kh_country is not None:
            result['kh_country'] = self.kh_country
        if self.kh_creditgrade is not None:
            result['kh_creditgrade'] = self.kh_creditgrade
        if self.kh_ctnumber is not None:
            result['kh_ctnumber'] = self.kh_ctnumber
        if self.kh_cttype is not None:
            result['kh_cttype'] = self.kh_cttype
        if self.kh_department is not None:
            result['kh_department'] = self.kh_department
        if self.kh_dingtalk is not None:
            result['kh_dingtalk'] = self.kh_dingtalk
        if self.kh_email is not None:
            result['kh_email'] = self.kh_email
        if self.kh_employees is not None:
            result['kh_employees'] = self.kh_employees
        if self.kh_fax is not None:
            result['kh_fax'] = self.kh_fax
        if self.kh_from is not None:
            result['kh_from'] = self.kh_from
        if self.kh_handset is not None:
            result['kh_handset'] = self.kh_handset
        if self.kh_headship is not None:
            result['kh_headship'] = self.kh_headship
        if self.kh_hotfl is not None:
            result['kh_hotfl'] = self.kh_hotfl
        if self.kh_hotlevel is not None:
            result['kh_hotlevel'] = self.kh_hotlevel
        if self.kh_hotmemo is not None:
            result['kh_hotmemo'] = self.kh_hotmemo
        if self.kh_hottype is not None:
            result['kh_hottype'] = self.kh_hottype
        if self.kh_industry is not None:
            result['kh_industry'] = self.kh_industry
        if self.kh_info is not None:
            result['kh_info'] = self.kh_info
        if self.kh_jibie is not None:
            result['kh_jibie'] = self.kh_jibie
        if self.kh_name is not None:
            result['kh_name'] = self.kh_name
        if self.kh_pkhid is not None:
            result['kh_pkhid'] = self.kh_pkhid
        if self.kh_preside is not None:
            result['kh_preside'] = self.kh_preside
        if self.kh_province is not None:
            result['kh_province'] = self.kh_province
        if self.kh_pst is not None:
            result['kh_pst'] = self.kh_pst
        if self.kh_qq is not None:
            result['kh_qq'] = self.kh_qq
        if self.kh_ralagrade is not None:
            result['kh_ralagrade'] = self.kh_ralagrade
        if self.kh_remark is not None:
            result['kh_remark'] = self.kh_remark
        if self.kh_sex is not None:
            result['kh_sex'] = self.kh_sex
        if self.kh_shortname is not None:
            result['kh_shortname'] = self.kh_shortname
        if self.kh_skype is not None:
            result['kh_skype'] = self.kh_skype
        if self.kh_sn is not None:
            result['kh_sn'] = self.kh_sn
        if self.kh_status is not None:
            result['kh_status'] = self.kh_status
        if self.kh_tel is not None:
            result['kh_tel'] = self.kh_tel
        if self.kh_type is not None:
            result['kh_type'] = self.kh_type
        if self.kh_valrating is not None:
            result['kh_valrating'] = self.kh_valrating
        if self.kh_wangwang is not None:
            result['kh_wangwang'] = self.kh_wangwang
        if self.kh_web is not None:
            result['kh_web'] = self.kh_web
        if self.kh_weixin is not None:
            result['kh_weixin'] = self.kh_weixin
        if self.kh_worktel is not None:
            result['kh_worktel'] = self.kh_worktel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('kh_address') is not None:
            self.kh_address = m.get('kh_address')
        if m.get('kh_appellation') is not None:
            self.kh_appellation = m.get('kh_appellation')
        if m.get('kh_befontof') is not None:
            self.kh_befontof = m.get('kh_befontof')
        if m.get('kh_billinfo') is not None:
            self.kh_billinfo = m.get('kh_billinfo')
        if m.get('kh_city') is not None:
            self.kh_city = m.get('kh_city')
        if m.get('kh_class') is not None:
            self.kh_class = m.get('kh_class')
        if m.get('kh_coaddress') is not None:
            self.kh_coaddress = m.get('kh_coaddress')
        if m.get('kh_contype') is not None:
            self.kh_contype = m.get('kh_contype')
        if m.get('kh_country') is not None:
            self.kh_country = m.get('kh_country')
        if m.get('kh_creditgrade') is not None:
            self.kh_creditgrade = m.get('kh_creditgrade')
        if m.get('kh_ctnumber') is not None:
            self.kh_ctnumber = m.get('kh_ctnumber')
        if m.get('kh_cttype') is not None:
            self.kh_cttype = m.get('kh_cttype')
        if m.get('kh_department') is not None:
            self.kh_department = m.get('kh_department')
        if m.get('kh_dingtalk') is not None:
            self.kh_dingtalk = m.get('kh_dingtalk')
        if m.get('kh_email') is not None:
            self.kh_email = m.get('kh_email')
        if m.get('kh_employees') is not None:
            self.kh_employees = m.get('kh_employees')
        if m.get('kh_fax') is not None:
            self.kh_fax = m.get('kh_fax')
        if m.get('kh_from') is not None:
            self.kh_from = m.get('kh_from')
        if m.get('kh_handset') is not None:
            self.kh_handset = m.get('kh_handset')
        if m.get('kh_headship') is not None:
            self.kh_headship = m.get('kh_headship')
        if m.get('kh_hotfl') is not None:
            self.kh_hotfl = m.get('kh_hotfl')
        if m.get('kh_hotlevel') is not None:
            self.kh_hotlevel = m.get('kh_hotlevel')
        if m.get('kh_hotmemo') is not None:
            self.kh_hotmemo = m.get('kh_hotmemo')
        if m.get('kh_hottype') is not None:
            self.kh_hottype = m.get('kh_hottype')
        if m.get('kh_industry') is not None:
            self.kh_industry = m.get('kh_industry')
        if m.get('kh_info') is not None:
            self.kh_info = m.get('kh_info')
        if m.get('kh_jibie') is not None:
            self.kh_jibie = m.get('kh_jibie')
        if m.get('kh_name') is not None:
            self.kh_name = m.get('kh_name')
        if m.get('kh_pkhid') is not None:
            self.kh_pkhid = m.get('kh_pkhid')
        if m.get('kh_preside') is not None:
            self.kh_preside = m.get('kh_preside')
        if m.get('kh_province') is not None:
            self.kh_province = m.get('kh_province')
        if m.get('kh_pst') is not None:
            self.kh_pst = m.get('kh_pst')
        if m.get('kh_qq') is not None:
            self.kh_qq = m.get('kh_qq')
        if m.get('kh_ralagrade') is not None:
            self.kh_ralagrade = m.get('kh_ralagrade')
        if m.get('kh_remark') is not None:
            self.kh_remark = m.get('kh_remark')
        if m.get('kh_sex') is not None:
            self.kh_sex = m.get('kh_sex')
        if m.get('kh_shortname') is not None:
            self.kh_shortname = m.get('kh_shortname')
        if m.get('kh_skype') is not None:
            self.kh_skype = m.get('kh_skype')
        if m.get('kh_sn') is not None:
            self.kh_sn = m.get('kh_sn')
        if m.get('kh_status') is not None:
            self.kh_status = m.get('kh_status')
        if m.get('kh_tel') is not None:
            self.kh_tel = m.get('kh_tel')
        if m.get('kh_type') is not None:
            self.kh_type = m.get('kh_type')
        if m.get('kh_valrating') is not None:
            self.kh_valrating = m.get('kh_valrating')
        if m.get('kh_wangwang') is not None:
            self.kh_wangwang = m.get('kh_wangwang')
        if m.get('kh_web') is not None:
            self.kh_web = m.get('kh_web')
        if m.get('kh_weixin') is not None:
            self.kh_weixin = m.get('kh_weixin')
        if m.get('kh_worktel') is not None:
            self.kh_worktel = m.get('kh_worktel')
        return self


class EditCustomerRequest(TeaModel):
    def __init__(
        self,
        data: EditCustomerRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写148
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditCustomerRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditCustomerResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditCustomerResponseBody = None,
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
            temp_model = EditCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditCustomerPoolHeaders(TeaModel):
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


class EditCustomerPoolRequestData(TeaModel):
    def __init__(
        self,
        data_userid: str = None,
        kh_address: str = None,
        kh_appellation: str = None,
        kh_befontof: str = None,
        kh_billinfo: str = None,
        kh_city: str = None,
        kh_class: str = None,
        kh_coaddress: str = None,
        kh_contype: str = None,
        kh_country: str = None,
        kh_creditgrade: str = None,
        kh_ctnumber: str = None,
        kh_cttype: str = None,
        kh_department: str = None,
        kh_dingtalk: str = None,
        kh_email: str = None,
        kh_employees: str = None,
        kh_fax: str = None,
        kh_from: str = None,
        kh_genzongtime: str = None,
        kh_handset: str = None,
        kh_headship: str = None,
        kh_hotfl: str = None,
        kh_hotlevel: str = None,
        kh_hotmemo: str = None,
        kh_hottype: str = None,
        kh_industry: str = None,
        kh_info: str = None,
        kh_jibie: str = None,
        kh_name: str = None,
        kh_pkhid: str = None,
        kh_preside: str = None,
        kh_province: str = None,
        kh_pst: str = None,
        kh_qq: str = None,
        kh_ralagrade: str = None,
        kh_remark: str = None,
        kh_sex: str = None,
        kh_shortname: str = None,
        kh_skype: str = None,
        kh_sn: str = None,
        kh_status: str = None,
        kh_tel: str = None,
        kh_type: str = None,
        kh_valrating: str = None,
        kh_wangwang: str = None,
        kh_web: str = None,
        kh_weixin: str = None,
        kh_worktel: str = None,
    ):
        # 创建人
        self.data_userid = data_userid
        # 家庭地址
        self.kh_address = kh_address
        # 称谓
        self.kh_appellation = kh_appellation
        # 爱好
        self.kh_befontof = kh_befontof
        # 开票资料
        self.kh_billinfo = kh_billinfo
        # 城市
        self.kh_city = kh_city
        # 类别（企业客户，个人客户，供应商，个人供应商）
        self.kh_class = kh_class
        # 单位地址
        self.kh_coaddress = kh_coaddress
        # 联系人分类
        self.kh_contype = kh_contype
        # 国家地区
        self.kh_country = kh_country
        # 信用等级（低，中，高）
        self.kh_creditgrade = kh_creditgrade
        # 证件号码
        self.kh_ctnumber = kh_ctnumber
        # 证件类型
        self.kh_cttype = kh_cttype
        # 部门
        self.kh_department = kh_department
        # 钉钉号
        self.kh_dingtalk = kh_dingtalk
        # 邮箱
        self.kh_email = kh_email
        # 人员规模
        self.kh_employees = kh_employees
        # 传真
        self.kh_fax = kh_fax
        # 来源
        self.kh_from = kh_from
        # 最后跟踪
        self.kh_genzongtime = kh_genzongtime
        # 手机
        self.kh_handset = kh_handset
        # 职务
        self.kh_headship = kh_headship
        # 热点分类
        self.kh_hotfl = kh_hotfl
        # 热度（无，低热，中热，高热）
        self.kh_hotlevel = kh_hotlevel
        # 热点说明
        self.kh_hotmemo = kh_hotmemo
        # 热点客户（是，否）
        self.kh_hottype = kh_hottype
        # 行业
        self.kh_industry = kh_industry
        # 公司简介
        self.kh_info = kh_info
        # 客户级别
        self.kh_jibie = kh_jibie
        # 客户名称
        self.kh_name = kh_name
        # 上级客户
        self.kh_pkhid = kh_pkhid
        # 负责业务
        self.kh_preside = kh_preside
        # 省份
        self.kh_province = kh_province
        # 邮编
        self.kh_pst = kh_pst
        # QQ
        self.kh_qq = kh_qq
        # 关系等级
        self.kh_ralagrade = kh_ralagrade
        # 备注
        self.kh_remark = kh_remark
        # 性别（男，女）
        self.kh_sex = kh_sex
        # 助记简称
        self.kh_shortname = kh_shortname
        # Skype
        self.kh_skype = kh_skype
        # 编号
        self.kh_sn = kh_sn
        # 阶段
        self.kh_status = kh_status
        # 家庭电话
        self.kh_tel = kh_tel
        # 种类
        self.kh_type = kh_type
        # 价值评估（低，中，高）
        self.kh_valrating = kh_valrating
        # 旺旺
        self.kh_wangwang = kh_wangwang
        # 网址
        self.kh_web = kh_web
        # 微信号
        self.kh_weixin = kh_weixin
        # 工作电话
        self.kh_worktel = kh_worktel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.kh_address is not None:
            result['kh_address'] = self.kh_address
        if self.kh_appellation is not None:
            result['kh_appellation'] = self.kh_appellation
        if self.kh_befontof is not None:
            result['kh_befontof'] = self.kh_befontof
        if self.kh_billinfo is not None:
            result['kh_billinfo'] = self.kh_billinfo
        if self.kh_city is not None:
            result['kh_city'] = self.kh_city
        if self.kh_class is not None:
            result['kh_class'] = self.kh_class
        if self.kh_coaddress is not None:
            result['kh_coaddress'] = self.kh_coaddress
        if self.kh_contype is not None:
            result['kh_contype'] = self.kh_contype
        if self.kh_country is not None:
            result['kh_country'] = self.kh_country
        if self.kh_creditgrade is not None:
            result['kh_creditgrade'] = self.kh_creditgrade
        if self.kh_ctnumber is not None:
            result['kh_ctnumber'] = self.kh_ctnumber
        if self.kh_cttype is not None:
            result['kh_cttype'] = self.kh_cttype
        if self.kh_department is not None:
            result['kh_department'] = self.kh_department
        if self.kh_dingtalk is not None:
            result['kh_dingtalk'] = self.kh_dingtalk
        if self.kh_email is not None:
            result['kh_email'] = self.kh_email
        if self.kh_employees is not None:
            result['kh_employees'] = self.kh_employees
        if self.kh_fax is not None:
            result['kh_fax'] = self.kh_fax
        if self.kh_from is not None:
            result['kh_from'] = self.kh_from
        if self.kh_genzongtime is not None:
            result['kh_genzongtime'] = self.kh_genzongtime
        if self.kh_handset is not None:
            result['kh_handset'] = self.kh_handset
        if self.kh_headship is not None:
            result['kh_headship'] = self.kh_headship
        if self.kh_hotfl is not None:
            result['kh_hotfl'] = self.kh_hotfl
        if self.kh_hotlevel is not None:
            result['kh_hotlevel'] = self.kh_hotlevel
        if self.kh_hotmemo is not None:
            result['kh_hotmemo'] = self.kh_hotmemo
        if self.kh_hottype is not None:
            result['kh_hottype'] = self.kh_hottype
        if self.kh_industry is not None:
            result['kh_industry'] = self.kh_industry
        if self.kh_info is not None:
            result['kh_info'] = self.kh_info
        if self.kh_jibie is not None:
            result['kh_jibie'] = self.kh_jibie
        if self.kh_name is not None:
            result['kh_name'] = self.kh_name
        if self.kh_pkhid is not None:
            result['kh_pkhid'] = self.kh_pkhid
        if self.kh_preside is not None:
            result['kh_preside'] = self.kh_preside
        if self.kh_province is not None:
            result['kh_province'] = self.kh_province
        if self.kh_pst is not None:
            result['kh_pst'] = self.kh_pst
        if self.kh_qq is not None:
            result['kh_qq'] = self.kh_qq
        if self.kh_ralagrade is not None:
            result['kh_ralagrade'] = self.kh_ralagrade
        if self.kh_remark is not None:
            result['kh_remark'] = self.kh_remark
        if self.kh_sex is not None:
            result['kh_sex'] = self.kh_sex
        if self.kh_shortname is not None:
            result['kh_shortname'] = self.kh_shortname
        if self.kh_skype is not None:
            result['kh_skype'] = self.kh_skype
        if self.kh_sn is not None:
            result['kh_sn'] = self.kh_sn
        if self.kh_status is not None:
            result['kh_status'] = self.kh_status
        if self.kh_tel is not None:
            result['kh_tel'] = self.kh_tel
        if self.kh_type is not None:
            result['kh_type'] = self.kh_type
        if self.kh_valrating is not None:
            result['kh_valrating'] = self.kh_valrating
        if self.kh_wangwang is not None:
            result['kh_wangwang'] = self.kh_wangwang
        if self.kh_web is not None:
            result['kh_web'] = self.kh_web
        if self.kh_weixin is not None:
            result['kh_weixin'] = self.kh_weixin
        if self.kh_worktel is not None:
            result['kh_worktel'] = self.kh_worktel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('kh_address') is not None:
            self.kh_address = m.get('kh_address')
        if m.get('kh_appellation') is not None:
            self.kh_appellation = m.get('kh_appellation')
        if m.get('kh_befontof') is not None:
            self.kh_befontof = m.get('kh_befontof')
        if m.get('kh_billinfo') is not None:
            self.kh_billinfo = m.get('kh_billinfo')
        if m.get('kh_city') is not None:
            self.kh_city = m.get('kh_city')
        if m.get('kh_class') is not None:
            self.kh_class = m.get('kh_class')
        if m.get('kh_coaddress') is not None:
            self.kh_coaddress = m.get('kh_coaddress')
        if m.get('kh_contype') is not None:
            self.kh_contype = m.get('kh_contype')
        if m.get('kh_country') is not None:
            self.kh_country = m.get('kh_country')
        if m.get('kh_creditgrade') is not None:
            self.kh_creditgrade = m.get('kh_creditgrade')
        if m.get('kh_ctnumber') is not None:
            self.kh_ctnumber = m.get('kh_ctnumber')
        if m.get('kh_cttype') is not None:
            self.kh_cttype = m.get('kh_cttype')
        if m.get('kh_department') is not None:
            self.kh_department = m.get('kh_department')
        if m.get('kh_dingtalk') is not None:
            self.kh_dingtalk = m.get('kh_dingtalk')
        if m.get('kh_email') is not None:
            self.kh_email = m.get('kh_email')
        if m.get('kh_employees') is not None:
            self.kh_employees = m.get('kh_employees')
        if m.get('kh_fax') is not None:
            self.kh_fax = m.get('kh_fax')
        if m.get('kh_from') is not None:
            self.kh_from = m.get('kh_from')
        if m.get('kh_genzongtime') is not None:
            self.kh_genzongtime = m.get('kh_genzongtime')
        if m.get('kh_handset') is not None:
            self.kh_handset = m.get('kh_handset')
        if m.get('kh_headship') is not None:
            self.kh_headship = m.get('kh_headship')
        if m.get('kh_hotfl') is not None:
            self.kh_hotfl = m.get('kh_hotfl')
        if m.get('kh_hotlevel') is not None:
            self.kh_hotlevel = m.get('kh_hotlevel')
        if m.get('kh_hotmemo') is not None:
            self.kh_hotmemo = m.get('kh_hotmemo')
        if m.get('kh_hottype') is not None:
            self.kh_hottype = m.get('kh_hottype')
        if m.get('kh_industry') is not None:
            self.kh_industry = m.get('kh_industry')
        if m.get('kh_info') is not None:
            self.kh_info = m.get('kh_info')
        if m.get('kh_jibie') is not None:
            self.kh_jibie = m.get('kh_jibie')
        if m.get('kh_name') is not None:
            self.kh_name = m.get('kh_name')
        if m.get('kh_pkhid') is not None:
            self.kh_pkhid = m.get('kh_pkhid')
        if m.get('kh_preside') is not None:
            self.kh_preside = m.get('kh_preside')
        if m.get('kh_province') is not None:
            self.kh_province = m.get('kh_province')
        if m.get('kh_pst') is not None:
            self.kh_pst = m.get('kh_pst')
        if m.get('kh_qq') is not None:
            self.kh_qq = m.get('kh_qq')
        if m.get('kh_ralagrade') is not None:
            self.kh_ralagrade = m.get('kh_ralagrade')
        if m.get('kh_remark') is not None:
            self.kh_remark = m.get('kh_remark')
        if m.get('kh_sex') is not None:
            self.kh_sex = m.get('kh_sex')
        if m.get('kh_shortname') is not None:
            self.kh_shortname = m.get('kh_shortname')
        if m.get('kh_skype') is not None:
            self.kh_skype = m.get('kh_skype')
        if m.get('kh_sn') is not None:
            self.kh_sn = m.get('kh_sn')
        if m.get('kh_status') is not None:
            self.kh_status = m.get('kh_status')
        if m.get('kh_tel') is not None:
            self.kh_tel = m.get('kh_tel')
        if m.get('kh_type') is not None:
            self.kh_type = m.get('kh_type')
        if m.get('kh_valrating') is not None:
            self.kh_valrating = m.get('kh_valrating')
        if m.get('kh_wangwang') is not None:
            self.kh_wangwang = m.get('kh_wangwang')
        if m.get('kh_web') is not None:
            self.kh_web = m.get('kh_web')
        if m.get('kh_weixin') is not None:
            self.kh_weixin = m.get('kh_weixin')
        if m.get('kh_worktel') is not None:
            self.kh_worktel = m.get('kh_worktel')
        return self


class EditCustomerPoolRequest(TeaModel):
    def __init__(
        self,
        data: EditCustomerPoolRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写238
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditCustomerPoolRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditCustomerPoolResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditCustomerPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditCustomerPoolResponseBody = None,
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
            temp_model = EditCustomerPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditExchangeHeaders(TeaModel):
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


class EditExchangeRequestData(TeaModel):
    def __init__(
        self,
        child_mx: str = None,
        data_userid: str = None,
        hh_customerid: str = None,
        hh_date: str = None,
        hh_inempid: str = None,
        hh_inlibid: str = None,
        hh_intime: str = None,
        hh_number: str = None,
        hh_orderid: str = None,
        hh_outempid: str = None,
        hh_outlibid: str = None,
        hh_outtime: str = None,
        hh_remark: str = None,
        hh_state: str = None,
        hh_title: str = None,
        hh_type: str = None,
    ):
        # 产品明细，json格式
        self.child_mx = child_mx
        # 创建人
        self.data_userid = data_userid
        # 对应客户
        self.hh_customerid = hh_customerid
        # 换货日期
        self.hh_date = hh_date
        # 换入操作员
        self.hh_inempid = hh_inempid
        # 换入仓库
        self.hh_inlibid = hh_inlibid
        # 换入时间
        self.hh_intime = hh_intime
        # 换货单号
        self.hh_number = hh_number
        # 合同/订单
        self.hh_orderid = hh_orderid
        # 换出操作员
        self.hh_outempid = hh_outempid
        # 换出仓库
        self.hh_outlibid = hh_outlibid
        # 换出时间
        self.hh_outtime = hh_outtime
        # 备注
        self.hh_remark = hh_remark
        # 状态（未执行，已入待出，已出待入，结束）
        self.hh_state = hh_state
        # 主题
        self.hh_title = hh_title
        # 分类
        self.hh_type = hh_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.hh_customerid is not None:
            result['hh_customerid'] = self.hh_customerid
        if self.hh_date is not None:
            result['hh_date'] = self.hh_date
        if self.hh_inempid is not None:
            result['hh_inempid'] = self.hh_inempid
        if self.hh_inlibid is not None:
            result['hh_inlibid'] = self.hh_inlibid
        if self.hh_intime is not None:
            result['hh_intime'] = self.hh_intime
        if self.hh_number is not None:
            result['hh_number'] = self.hh_number
        if self.hh_orderid is not None:
            result['hh_orderid'] = self.hh_orderid
        if self.hh_outempid is not None:
            result['hh_outempid'] = self.hh_outempid
        if self.hh_outlibid is not None:
            result['hh_outlibid'] = self.hh_outlibid
        if self.hh_outtime is not None:
            result['hh_outtime'] = self.hh_outtime
        if self.hh_remark is not None:
            result['hh_remark'] = self.hh_remark
        if self.hh_state is not None:
            result['hh_state'] = self.hh_state
        if self.hh_title is not None:
            result['hh_title'] = self.hh_title
        if self.hh_type is not None:
            result['hh_type'] = self.hh_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('hh_customerid') is not None:
            self.hh_customerid = m.get('hh_customerid')
        if m.get('hh_date') is not None:
            self.hh_date = m.get('hh_date')
        if m.get('hh_inempid') is not None:
            self.hh_inempid = m.get('hh_inempid')
        if m.get('hh_inlibid') is not None:
            self.hh_inlibid = m.get('hh_inlibid')
        if m.get('hh_intime') is not None:
            self.hh_intime = m.get('hh_intime')
        if m.get('hh_number') is not None:
            self.hh_number = m.get('hh_number')
        if m.get('hh_orderid') is not None:
            self.hh_orderid = m.get('hh_orderid')
        if m.get('hh_outempid') is not None:
            self.hh_outempid = m.get('hh_outempid')
        if m.get('hh_outlibid') is not None:
            self.hh_outlibid = m.get('hh_outlibid')
        if m.get('hh_outtime') is not None:
            self.hh_outtime = m.get('hh_outtime')
        if m.get('hh_remark') is not None:
            self.hh_remark = m.get('hh_remark')
        if m.get('hh_state') is not None:
            self.hh_state = m.get('hh_state')
        if m.get('hh_title') is not None:
            self.hh_title = m.get('hh_title')
        if m.get('hh_type') is not None:
            self.hh_type = m.get('hh_type')
        return self


class EditExchangeRequest(TeaModel):
    def __init__(
        self,
        data: EditExchangeRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写228
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditExchangeRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditExchangeResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditExchangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditExchangeResponseBody = None,
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
            temp_model = EditExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditGoodsHeaders(TeaModel):
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


class EditGoodsRequestData(TeaModel):
    def __init__(
        self,
        addedtime: str = None,
        cbprice: str = None,
        cp_parentid: str = None,
        cparea: str = None,
        cpbarcode: str = None,
        cpbrand: str = None,
        cpcontent: str = None,
        cpguige: str = None,
        cpimg: str = None,
        cpname: str = None,
        cpno: str = None,
        cpremark: str = None,
        cptype: str = None,
        cpunit: str = None,
        cpweight: str = None,
        data_userid: str = None,
        gysid: str = None,
        ispicimanage: str = None,
        issnmanage: str = None,
        isstock: str = None,
        isstop: str = None,
        preprice_1: str = None,
        preprice_2: str = None,
        preprice_3: str = None,
        preprice_4: str = None,
        stockdown: str = None,
        stockup: str = None,
        typeid: str = None,
        unitrate: str = None,
    ):
        # 上架时间
        self.addedtime = addedtime
        # 成本价格
        self.cbprice = cbprice
        # 基准产品
        self.cp_parentid = cp_parentid
        # 产品产地
        self.cparea = cparea
        # 条形码
        self.cpbarcode = cpbarcode
        # 产品品牌
        self.cpbrand = cpbrand
        # 产品说明
        self.cpcontent = cpcontent
        # 产品规格
        self.cpguige = cpguige
        # 产品图片
        self.cpimg = cpimg
        # 产品名称
        self.cpname = cpname
        # 产品编号
        self.cpno = cpno
        # 产品备注
        self.cpremark = cpremark
        # 产品型号
        self.cptype = cptype
        # 产品单位
        self.cpunit = cpunit
        # 产品重量
        self.cpweight = cpweight
        # 创建人
        self.data_userid = data_userid
        # 默认供应商
        self.gysid = gysid
        # 批次号管理（是，否）
        self.ispicimanage = ispicimanage
        # 序列号管理（是，否）
        self.issnmanage = issnmanage
        # 是否算库存（计算，不计算，计算(按基准规格)）
        self.isstock = isstock
        # 产品状态（正常，停售，下架）
        self.isstop = isstop
        # 零售价格
        self.preprice_1 = preprice_1
        # 预设价格1
        self.preprice_2 = preprice_2
        # 预设价格2
        self.preprice_3 = preprice_3
        # 预设价格3
        self.preprice_4 = preprice_4
        # 库存下限
        self.stockdown = stockdown
        # 库存上限
        self.stockup = stockup
        # 产品类别
        self.typeid = typeid
        # 单位换算
        self.unitrate = unitrate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addedtime is not None:
            result['addedtime'] = self.addedtime
        if self.cbprice is not None:
            result['cbprice'] = self.cbprice
        if self.cp_parentid is not None:
            result['cp_parentid'] = self.cp_parentid
        if self.cparea is not None:
            result['cparea'] = self.cparea
        if self.cpbarcode is not None:
            result['cpbarcode'] = self.cpbarcode
        if self.cpbrand is not None:
            result['cpbrand'] = self.cpbrand
        if self.cpcontent is not None:
            result['cpcontent'] = self.cpcontent
        if self.cpguige is not None:
            result['cpguige'] = self.cpguige
        if self.cpimg is not None:
            result['cpimg'] = self.cpimg
        if self.cpname is not None:
            result['cpname'] = self.cpname
        if self.cpno is not None:
            result['cpno'] = self.cpno
        if self.cpremark is not None:
            result['cpremark'] = self.cpremark
        if self.cptype is not None:
            result['cptype'] = self.cptype
        if self.cpunit is not None:
            result['cpunit'] = self.cpunit
        if self.cpweight is not None:
            result['cpweight'] = self.cpweight
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.gysid is not None:
            result['gysid'] = self.gysid
        if self.ispicimanage is not None:
            result['ispicimanage'] = self.ispicimanage
        if self.issnmanage is not None:
            result['issnmanage'] = self.issnmanage
        if self.isstock is not None:
            result['isstock'] = self.isstock
        if self.isstop is not None:
            result['isstop'] = self.isstop
        if self.preprice_1 is not None:
            result['preprice1'] = self.preprice_1
        if self.preprice_2 is not None:
            result['preprice2'] = self.preprice_2
        if self.preprice_3 is not None:
            result['preprice3'] = self.preprice_3
        if self.preprice_4 is not None:
            result['preprice4'] = self.preprice_4
        if self.stockdown is not None:
            result['stockdown'] = self.stockdown
        if self.stockup is not None:
            result['stockup'] = self.stockup
        if self.typeid is not None:
            result['typeid'] = self.typeid
        if self.unitrate is not None:
            result['unitrate'] = self.unitrate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addedtime') is not None:
            self.addedtime = m.get('addedtime')
        if m.get('cbprice') is not None:
            self.cbprice = m.get('cbprice')
        if m.get('cp_parentid') is not None:
            self.cp_parentid = m.get('cp_parentid')
        if m.get('cparea') is not None:
            self.cparea = m.get('cparea')
        if m.get('cpbarcode') is not None:
            self.cpbarcode = m.get('cpbarcode')
        if m.get('cpbrand') is not None:
            self.cpbrand = m.get('cpbrand')
        if m.get('cpcontent') is not None:
            self.cpcontent = m.get('cpcontent')
        if m.get('cpguige') is not None:
            self.cpguige = m.get('cpguige')
        if m.get('cpimg') is not None:
            self.cpimg = m.get('cpimg')
        if m.get('cpname') is not None:
            self.cpname = m.get('cpname')
        if m.get('cpno') is not None:
            self.cpno = m.get('cpno')
        if m.get('cpremark') is not None:
            self.cpremark = m.get('cpremark')
        if m.get('cptype') is not None:
            self.cptype = m.get('cptype')
        if m.get('cpunit') is not None:
            self.cpunit = m.get('cpunit')
        if m.get('cpweight') is not None:
            self.cpweight = m.get('cpweight')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('gysid') is not None:
            self.gysid = m.get('gysid')
        if m.get('ispicimanage') is not None:
            self.ispicimanage = m.get('ispicimanage')
        if m.get('issnmanage') is not None:
            self.issnmanage = m.get('issnmanage')
        if m.get('isstock') is not None:
            self.isstock = m.get('isstock')
        if m.get('isstop') is not None:
            self.isstop = m.get('isstop')
        if m.get('preprice1') is not None:
            self.preprice_1 = m.get('preprice1')
        if m.get('preprice2') is not None:
            self.preprice_2 = m.get('preprice2')
        if m.get('preprice3') is not None:
            self.preprice_3 = m.get('preprice3')
        if m.get('preprice4') is not None:
            self.preprice_4 = m.get('preprice4')
        if m.get('stockdown') is not None:
            self.stockdown = m.get('stockdown')
        if m.get('stockup') is not None:
            self.stockup = m.get('stockup')
        if m.get('typeid') is not None:
            self.typeid = m.get('typeid')
        if m.get('unitrate') is not None:
            self.unitrate = m.get('unitrate')
        return self


class EditGoodsRequest(TeaModel):
    def __init__(
        self,
        data: EditGoodsRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写154
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditGoodsRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditGoodsResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditGoodsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditGoodsResponseBody = None,
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
            temp_model = EditGoodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditIntostockHeaders(TeaModel):
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


class EditIntostockRequestData(TeaModel):
    def __init__(
        self,
        askempid: str = None,
        auditreson: str = None,
        billno: str = None,
        child_mx: str = None,
        customerid: str = None,
        data_userid: str = None,
        empid: str = None,
        inorout: str = None,
        libiodate: str = None,
        libioname: str = None,
        libiostate: str = None,
        orderid: str = None,
        remark: str = None,
        stocklibid: str = None,
    ):
        # 入库申请人
        self.askempid = askempid
        # 入库备注
        self.auditreson = auditreson
        # 入库单号
        self.billno = billno
        # 产品明细，json格式
        self.child_mx = child_mx
        # 供应商/客户
        self.customerid = customerid
        # 创建人
        self.data_userid = data_userid
        # 入库经办人
        self.empid = empid
        # 单据类型（入库，销售退货，生产退料，生产入库，维修退货）
        self.inorout = inorout
        # 入库日期
        self.libiodate = libiodate
        # 入库主题
        self.libioname = libioname
        # 入库状态（未入库，已入库）
        self.libiostate = libiostate
        # 对应单据
        self.orderid = orderid
        # 申请备注
        self.remark = remark
        # 入库仓库
        self.stocklibid = stocklibid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.askempid is not None:
            result['askempid'] = self.askempid
        if self.auditreson is not None:
            result['auditreson'] = self.auditreson
        if self.billno is not None:
            result['billno'] = self.billno
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.customerid is not None:
            result['customerid'] = self.customerid
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.empid is not None:
            result['empid'] = self.empid
        if self.inorout is not None:
            result['inorout'] = self.inorout
        if self.libiodate is not None:
            result['libiodate'] = self.libiodate
        if self.libioname is not None:
            result['libioname'] = self.libioname
        if self.libiostate is not None:
            result['libiostate'] = self.libiostate
        if self.orderid is not None:
            result['orderid'] = self.orderid
        if self.remark is not None:
            result['remark'] = self.remark
        if self.stocklibid is not None:
            result['stocklibid'] = self.stocklibid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('askempid') is not None:
            self.askempid = m.get('askempid')
        if m.get('auditreson') is not None:
            self.auditreson = m.get('auditreson')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('customerid') is not None:
            self.customerid = m.get('customerid')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('empid') is not None:
            self.empid = m.get('empid')
        if m.get('inorout') is not None:
            self.inorout = m.get('inorout')
        if m.get('libiodate') is not None:
            self.libiodate = m.get('libiodate')
        if m.get('libioname') is not None:
            self.libioname = m.get('libioname')
        if m.get('libiostate') is not None:
            self.libiostate = m.get('libiostate')
        if m.get('orderid') is not None:
            self.orderid = m.get('orderid')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('stocklibid') is not None:
            self.stocklibid = m.get('stocklibid')
        return self


class EditIntostockRequest(TeaModel):
    def __init__(
        self,
        data: EditIntostockRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写189
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditIntostockRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditIntostockResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditIntostockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditIntostockResponseBody = None,
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
            temp_model = EditIntostockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditInvoiceHeaders(TeaModel):
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


class EditInvoiceRequestData(TeaModel):
    def __init__(
        self,
        child_mx: str = None,
        data_userid: str = None,
        fh_address: str = None,
        fh_customerid: str = None,
        fh_date: str = None,
        fh_email: str = None,
        fh_handset: str = None,
        fh_htorder: str = None,
        fh_jianshu: str = None,
        fh_kg: str = None,
        fh_linkman: str = None,
        fh_lxrid: str = None,
        fh_mode: str = None,
        fh_msn: str = None,
        fh_number: str = None,
        fh_post: str = None,
        fh_preside: str = None,
        fh_remark: str = None,
        fh_shipper: str = None,
        fh_state: str = None,
        fh_tel: str = None,
        fh_title: str = None,
        fh_yunfei: str = None,
    ):
        # 产品明细，json格式
        self.child_mx = child_mx
        # 创建人
        self.data_userid = data_userid
        # 地址
        self.fh_address = fh_address
        # 对应客户
        self.fh_customerid = fh_customerid
        # 发货日期
        self.fh_date = fh_date
        # Email
        self.fh_email = fh_email
        # 手机
        self.fh_handset = fh_handset
        # 对应订单
        self.fh_htorder = fh_htorder
        # 打包件数
        self.fh_jianshu = fh_jianshu
        # 重量(Kg)
        self.fh_kg = fh_kg
        # 收货人
        self.fh_linkman = fh_linkman
        # 联系人
        self.fh_lxrid = fh_lxrid
        # 发货方式
        self.fh_mode = fh_mode
        # MSN
        self.fh_msn = fh_msn
        # 发货单号
        self.fh_number = fh_number
        # 邮编
        self.fh_post = fh_post
        # 所有者
        self.fh_preside = fh_preside
        # 备注
        self.fh_remark = fh_remark
        # 发货人
        self.fh_shipper = fh_shipper
        # 发货状态
        self.fh_state = fh_state
        # 电话
        self.fh_tel = fh_tel
        # 发货主题
        self.fh_title = fh_title
        # 运费
        self.fh_yunfei = fh_yunfei

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.fh_address is not None:
            result['fh_address'] = self.fh_address
        if self.fh_customerid is not None:
            result['fh_customerid'] = self.fh_customerid
        if self.fh_date is not None:
            result['fh_date'] = self.fh_date
        if self.fh_email is not None:
            result['fh_email'] = self.fh_email
        if self.fh_handset is not None:
            result['fh_handset'] = self.fh_handset
        if self.fh_htorder is not None:
            result['fh_htorder'] = self.fh_htorder
        if self.fh_jianshu is not None:
            result['fh_jianshu'] = self.fh_jianshu
        if self.fh_kg is not None:
            result['fh_kg'] = self.fh_kg
        if self.fh_linkman is not None:
            result['fh_linkman'] = self.fh_linkman
        if self.fh_lxrid is not None:
            result['fh_lxrid'] = self.fh_lxrid
        if self.fh_mode is not None:
            result['fh_mode'] = self.fh_mode
        if self.fh_msn is not None:
            result['fh_msn'] = self.fh_msn
        if self.fh_number is not None:
            result['fh_number'] = self.fh_number
        if self.fh_post is not None:
            result['fh_post'] = self.fh_post
        if self.fh_preside is not None:
            result['fh_preside'] = self.fh_preside
        if self.fh_remark is not None:
            result['fh_remark'] = self.fh_remark
        if self.fh_shipper is not None:
            result['fh_shipper'] = self.fh_shipper
        if self.fh_state is not None:
            result['fh_state'] = self.fh_state
        if self.fh_tel is not None:
            result['fh_tel'] = self.fh_tel
        if self.fh_title is not None:
            result['fh_title'] = self.fh_title
        if self.fh_yunfei is not None:
            result['fh_yunfei'] = self.fh_yunfei
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('fh_address') is not None:
            self.fh_address = m.get('fh_address')
        if m.get('fh_customerid') is not None:
            self.fh_customerid = m.get('fh_customerid')
        if m.get('fh_date') is not None:
            self.fh_date = m.get('fh_date')
        if m.get('fh_email') is not None:
            self.fh_email = m.get('fh_email')
        if m.get('fh_handset') is not None:
            self.fh_handset = m.get('fh_handset')
        if m.get('fh_htorder') is not None:
            self.fh_htorder = m.get('fh_htorder')
        if m.get('fh_jianshu') is not None:
            self.fh_jianshu = m.get('fh_jianshu')
        if m.get('fh_kg') is not None:
            self.fh_kg = m.get('fh_kg')
        if m.get('fh_linkman') is not None:
            self.fh_linkman = m.get('fh_linkman')
        if m.get('fh_lxrid') is not None:
            self.fh_lxrid = m.get('fh_lxrid')
        if m.get('fh_mode') is not None:
            self.fh_mode = m.get('fh_mode')
        if m.get('fh_msn') is not None:
            self.fh_msn = m.get('fh_msn')
        if m.get('fh_number') is not None:
            self.fh_number = m.get('fh_number')
        if m.get('fh_post') is not None:
            self.fh_post = m.get('fh_post')
        if m.get('fh_preside') is not None:
            self.fh_preside = m.get('fh_preside')
        if m.get('fh_remark') is not None:
            self.fh_remark = m.get('fh_remark')
        if m.get('fh_shipper') is not None:
            self.fh_shipper = m.get('fh_shipper')
        if m.get('fh_state') is not None:
            self.fh_state = m.get('fh_state')
        if m.get('fh_tel') is not None:
            self.fh_tel = m.get('fh_tel')
        if m.get('fh_title') is not None:
            self.fh_title = m.get('fh_title')
        if m.get('fh_yunfei') is not None:
            self.fh_yunfei = m.get('fh_yunfei')
        return self


class EditInvoiceRequest(TeaModel):
    def __init__(
        self,
        data: EditInvoiceRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写169
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditInvoiceRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditInvoiceResponseBody = None,
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
            temp_model = EditInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditOrderHeaders(TeaModel):
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


class EditOrderRequestData(TeaModel):
    def __init__(
        self,
        child_mx: str = None,
        data_userid: str = None,
        fahuoaddressid: str = None,
        ht_begindate: str = None,
        ht_contract: str = None,
        ht_customerid: str = None,
        ht_cusub: str = None,
        ht_date: str = None,
        ht_deliplace: str = None,
        ht_enddate: str = None,
        ht_fjmoney: str = None,
        ht_fjmoneylx: str = None,
        ht_kjmoney: str = None,
        ht_lxrid: str = None,
        ht_lxrinfo: str = None,
        ht_moneyzhekou: str = None,
        ht_number: str = None,
        ht_order: str = None,
        ht_paymode: str = None,
        ht_preside: str = None,
        ht_remark: str = None,
        ht_state: str = None,
        ht_summemo: str = None,
        ht_summoney: str = None,
        ht_title: str = None,
        ht_type: str = None,
        ht_wesub: str = None,
        ht_wuliutype: str = None,
        ht_xshid: str = None,
        ht_yunfeimoney: str = None,
    ):
        # 产品明细，json格式
        self.child_mx = child_mx
        # 创建人
        self.data_userid = data_userid
        # 收货地址
        self.fahuoaddressid = fahuoaddressid
        # 开始日期
        self.ht_begindate = ht_begindate
        # 合同正文
        self.ht_contract = ht_contract
        # 对应客户
        self.ht_customerid = ht_customerid
        # 客户签约人
        self.ht_cusub = ht_cusub
        # 签单日期
        self.ht_date = ht_date
        # 交付地点
        self.ht_deliplace = ht_deliplace
        # 最晚发货日
        self.ht_enddate = ht_enddate
        # 附加费用金额
        self.ht_fjmoney = ht_fjmoney
        # 附加费用分类
        self.ht_fjmoneylx = ht_fjmoneylx
        # 优惠抹零金额
        self.ht_kjmoney = ht_kjmoney
        # 对应联系人
        self.ht_lxrid = ht_lxrid
        # 联系方式
        self.ht_lxrinfo = ht_lxrinfo
        # 优惠折扣率
        self.ht_moneyzhekou = ht_moneyzhekou
        # 合同单号
        self.ht_number = ht_number
        # 单据类型（合同，合同订单，店面单）
        self.ht_order = ht_order
        # 付款方式
        self.ht_paymode = ht_paymode
        # 所有者
        self.ht_preside = ht_preside
        # 备注
        self.ht_remark = ht_remark
        # 状态
        self.ht_state = ht_state
        # 外币备注
        self.ht_summemo = ht_summemo
        # 总金额
        self.ht_summoney = ht_summoney
        # 主题
        self.ht_title = ht_title
        # 分类
        self.ht_type = ht_type
        # 我方签约人
        self.ht_wesub = ht_wesub
        # 发货方式
        self.ht_wuliutype = ht_wuliutype
        # 对应机会
        self.ht_xshid = ht_xshid
        # 预计运费
        self.ht_yunfeimoney = ht_yunfeimoney

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.fahuoaddressid is not None:
            result['fahuoaddressid'] = self.fahuoaddressid
        if self.ht_begindate is not None:
            result['ht_begindate'] = self.ht_begindate
        if self.ht_contract is not None:
            result['ht_contract'] = self.ht_contract
        if self.ht_customerid is not None:
            result['ht_customerid'] = self.ht_customerid
        if self.ht_cusub is not None:
            result['ht_cusub'] = self.ht_cusub
        if self.ht_date is not None:
            result['ht_date'] = self.ht_date
        if self.ht_deliplace is not None:
            result['ht_deliplace'] = self.ht_deliplace
        if self.ht_enddate is not None:
            result['ht_enddate'] = self.ht_enddate
        if self.ht_fjmoney is not None:
            result['ht_fjmoney'] = self.ht_fjmoney
        if self.ht_fjmoneylx is not None:
            result['ht_fjmoneylx'] = self.ht_fjmoneylx
        if self.ht_kjmoney is not None:
            result['ht_kjmoney'] = self.ht_kjmoney
        if self.ht_lxrid is not None:
            result['ht_lxrid'] = self.ht_lxrid
        if self.ht_lxrinfo is not None:
            result['ht_lxrinfo'] = self.ht_lxrinfo
        if self.ht_moneyzhekou is not None:
            result['ht_moneyzhekou'] = self.ht_moneyzhekou
        if self.ht_number is not None:
            result['ht_number'] = self.ht_number
        if self.ht_order is not None:
            result['ht_order'] = self.ht_order
        if self.ht_paymode is not None:
            result['ht_paymode'] = self.ht_paymode
        if self.ht_preside is not None:
            result['ht_preside'] = self.ht_preside
        if self.ht_remark is not None:
            result['ht_remark'] = self.ht_remark
        if self.ht_state is not None:
            result['ht_state'] = self.ht_state
        if self.ht_summemo is not None:
            result['ht_summemo'] = self.ht_summemo
        if self.ht_summoney is not None:
            result['ht_summoney'] = self.ht_summoney
        if self.ht_title is not None:
            result['ht_title'] = self.ht_title
        if self.ht_type is not None:
            result['ht_type'] = self.ht_type
        if self.ht_wesub is not None:
            result['ht_wesub'] = self.ht_wesub
        if self.ht_wuliutype is not None:
            result['ht_wuliutype'] = self.ht_wuliutype
        if self.ht_xshid is not None:
            result['ht_xshid'] = self.ht_xshid
        if self.ht_yunfeimoney is not None:
            result['ht_yunfeimoney'] = self.ht_yunfeimoney
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('fahuoaddressid') is not None:
            self.fahuoaddressid = m.get('fahuoaddressid')
        if m.get('ht_begindate') is not None:
            self.ht_begindate = m.get('ht_begindate')
        if m.get('ht_contract') is not None:
            self.ht_contract = m.get('ht_contract')
        if m.get('ht_customerid') is not None:
            self.ht_customerid = m.get('ht_customerid')
        if m.get('ht_cusub') is not None:
            self.ht_cusub = m.get('ht_cusub')
        if m.get('ht_date') is not None:
            self.ht_date = m.get('ht_date')
        if m.get('ht_deliplace') is not None:
            self.ht_deliplace = m.get('ht_deliplace')
        if m.get('ht_enddate') is not None:
            self.ht_enddate = m.get('ht_enddate')
        if m.get('ht_fjmoney') is not None:
            self.ht_fjmoney = m.get('ht_fjmoney')
        if m.get('ht_fjmoneylx') is not None:
            self.ht_fjmoneylx = m.get('ht_fjmoneylx')
        if m.get('ht_kjmoney') is not None:
            self.ht_kjmoney = m.get('ht_kjmoney')
        if m.get('ht_lxrid') is not None:
            self.ht_lxrid = m.get('ht_lxrid')
        if m.get('ht_lxrinfo') is not None:
            self.ht_lxrinfo = m.get('ht_lxrinfo')
        if m.get('ht_moneyzhekou') is not None:
            self.ht_moneyzhekou = m.get('ht_moneyzhekou')
        if m.get('ht_number') is not None:
            self.ht_number = m.get('ht_number')
        if m.get('ht_order') is not None:
            self.ht_order = m.get('ht_order')
        if m.get('ht_paymode') is not None:
            self.ht_paymode = m.get('ht_paymode')
        if m.get('ht_preside') is not None:
            self.ht_preside = m.get('ht_preside')
        if m.get('ht_remark') is not None:
            self.ht_remark = m.get('ht_remark')
        if m.get('ht_state') is not None:
            self.ht_state = m.get('ht_state')
        if m.get('ht_summemo') is not None:
            self.ht_summemo = m.get('ht_summemo')
        if m.get('ht_summoney') is not None:
            self.ht_summoney = m.get('ht_summoney')
        if m.get('ht_title') is not None:
            self.ht_title = m.get('ht_title')
        if m.get('ht_type') is not None:
            self.ht_type = m.get('ht_type')
        if m.get('ht_wesub') is not None:
            self.ht_wesub = m.get('ht_wesub')
        if m.get('ht_wuliutype') is not None:
            self.ht_wuliutype = m.get('ht_wuliutype')
        if m.get('ht_xshid') is not None:
            self.ht_xshid = m.get('ht_xshid')
        if m.get('ht_yunfeimoney') is not None:
            self.ht_yunfeimoney = m.get('ht_yunfeimoney')
        return self


class EditOrderRequest(TeaModel):
    def __init__(
        self,
        data: EditOrderRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写150
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditOrderRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditOrderResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditOrderResponseBody = None,
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
            temp_model = EditOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditOutstockHeaders(TeaModel):
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


class EditOutstockRequestData(TeaModel):
    def __init__(
        self,
        askempid: str = None,
        auditreson: str = None,
        billno: str = None,
        child_mx: str = None,
        customerid: str = None,
        data_userid: str = None,
        empid: str = None,
        inorout: str = None,
        libiodate: str = None,
        libioname: str = None,
        libiostate: str = None,
        orderid: str = None,
        remark: str = None,
        stocklibid: str = None,
    ):
        # 申请人
        self.askempid = askempid
        # 出库备注
        self.auditreson = auditreson
        # 出库单号
        self.billno = billno
        # 产品明细，json格式
        self.child_mx = child_mx
        # 对应客户
        self.customerid = customerid
        # 创建人
        self.data_userid = data_userid
        # 经办人
        self.empid = empid
        # 单据类型
        self.inorout = inorout
        # 出库日期
        self.libiodate = libiodate
        # 出库主题
        self.libioname = libioname
        # 出库状态
        self.libiostate = libiostate
        # 对应订单
        self.orderid = orderid
        # 申请备注
        self.remark = remark
        # 出库仓库
        self.stocklibid = stocklibid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.askempid is not None:
            result['askempid'] = self.askempid
        if self.auditreson is not None:
            result['auditreson'] = self.auditreson
        if self.billno is not None:
            result['billno'] = self.billno
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.customerid is not None:
            result['customerid'] = self.customerid
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.empid is not None:
            result['empid'] = self.empid
        if self.inorout is not None:
            result['inorout'] = self.inorout
        if self.libiodate is not None:
            result['libiodate'] = self.libiodate
        if self.libioname is not None:
            result['libioname'] = self.libioname
        if self.libiostate is not None:
            result['libiostate'] = self.libiostate
        if self.orderid is not None:
            result['orderid'] = self.orderid
        if self.remark is not None:
            result['remark'] = self.remark
        if self.stocklibid is not None:
            result['stocklibid'] = self.stocklibid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('askempid') is not None:
            self.askempid = m.get('askempid')
        if m.get('auditreson') is not None:
            self.auditreson = m.get('auditreson')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('customerid') is not None:
            self.customerid = m.get('customerid')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('empid') is not None:
            self.empid = m.get('empid')
        if m.get('inorout') is not None:
            self.inorout = m.get('inorout')
        if m.get('libiodate') is not None:
            self.libiodate = m.get('libiodate')
        if m.get('libioname') is not None:
            self.libioname = m.get('libioname')
        if m.get('libiostate') is not None:
            self.libiostate = m.get('libiostate')
        if m.get('orderid') is not None:
            self.orderid = m.get('orderid')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('stocklibid') is not None:
            self.stocklibid = m.get('stocklibid')
        return self


class EditOutstockRequest(TeaModel):
    def __init__(
        self,
        data: EditOutstockRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写191
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditOutstockRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditOutstockResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditOutstockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditOutstockResponseBody = None,
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
            temp_model = EditOutstockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditProductionHeaders(TeaModel):
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


class EditProductionRequestData(TeaModel):
    def __init__(
        self,
        data_userid: str = None,
        sch_customerid: str = None,
        sch_endtime: str = None,
        sch_finished: str = None,
        sch_htid: str = None,
        sch_makeemp: str = None,
        sch_number: str = None,
        sch_planendtime: str = None,
        sch_principal: str = None,
        sch_remark: str = None,
        sch_starttime: str = None,
        sch_statesstr: str = None,
        sch_title: str = None,
    ):
        # 创建人
        self.data_userid = data_userid
        # 对应客户
        self.sch_customerid = sch_customerid
        # 完成日期
        self.sch_endtime = sch_endtime
        # 状态（未生产，生产中，生产中止，生产完成）
        self.sch_finished = sch_finished
        # 订单
        self.sch_htid = sch_htid
        # 生产人员
        self.sch_makeemp = sch_makeemp
        # 单号
        self.sch_number = sch_number
        # 计划完成
        self.sch_planendtime = sch_planendtime
        # 负责人
        self.sch_principal = sch_principal
        # 备注
        self.sch_remark = sch_remark
        # 开始日期
        self.sch_starttime = sch_starttime
        # 阶段（计划，审核，领料，生产，验收，入库/退料，结单，取消）
        self.sch_statesstr = sch_statesstr
        # 主题
        self.sch_title = sch_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.sch_customerid is not None:
            result['sch_customerid'] = self.sch_customerid
        if self.sch_endtime is not None:
            result['sch_endtime'] = self.sch_endtime
        if self.sch_finished is not None:
            result['sch_finished'] = self.sch_finished
        if self.sch_htid is not None:
            result['sch_htid'] = self.sch_htid
        if self.sch_makeemp is not None:
            result['sch_makeemp'] = self.sch_makeemp
        if self.sch_number is not None:
            result['sch_number'] = self.sch_number
        if self.sch_planendtime is not None:
            result['sch_planendtime'] = self.sch_planendtime
        if self.sch_principal is not None:
            result['sch_principal'] = self.sch_principal
        if self.sch_remark is not None:
            result['sch_remark'] = self.sch_remark
        if self.sch_starttime is not None:
            result['sch_starttime'] = self.sch_starttime
        if self.sch_statesstr is not None:
            result['sch_statesstr'] = self.sch_statesstr
        if self.sch_title is not None:
            result['sch_title'] = self.sch_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('sch_customerid') is not None:
            self.sch_customerid = m.get('sch_customerid')
        if m.get('sch_endtime') is not None:
            self.sch_endtime = m.get('sch_endtime')
        if m.get('sch_finished') is not None:
            self.sch_finished = m.get('sch_finished')
        if m.get('sch_htid') is not None:
            self.sch_htid = m.get('sch_htid')
        if m.get('sch_makeemp') is not None:
            self.sch_makeemp = m.get('sch_makeemp')
        if m.get('sch_number') is not None:
            self.sch_number = m.get('sch_number')
        if m.get('sch_planendtime') is not None:
            self.sch_planendtime = m.get('sch_planendtime')
        if m.get('sch_principal') is not None:
            self.sch_principal = m.get('sch_principal')
        if m.get('sch_remark') is not None:
            self.sch_remark = m.get('sch_remark')
        if m.get('sch_starttime') is not None:
            self.sch_starttime = m.get('sch_starttime')
        if m.get('sch_statesstr') is not None:
            self.sch_statesstr = m.get('sch_statesstr')
        if m.get('sch_title') is not None:
            self.sch_title = m.get('sch_title')
        return self


class EditProductionRequest(TeaModel):
    def __init__(
        self,
        data: EditProductionRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写156
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditProductionRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditProductionResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditProductionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditProductionResponseBody = None,
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
            temp_model = EditProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditPurchaseHeaders(TeaModel):
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


class EditPurchaseRequestData(TeaModel):
    def __init__(
        self,
        cg_fjmoney: str = None,
        cg_fjmoneylx: str = None,
        cg_kjmoney: str = None,
        cg_moneyzhekou: str = None,
        cg_zxstate: str = None,
        cgdate: str = None,
        cgname: str = None,
        cgno: str = None,
        cgremark: str = None,
        cgtype: str = None,
        child_mx: str = None,
        data_userid: str = None,
        empid: str = None,
        gys_lxrid: str = None,
        gys_lxrinfo: str = None,
        gysid: str = None,
        gysjingban: str = None,
        order_htid: str = None,
        order_khid: str = None,
        summoney: str = None,
    ):
        # 附加费用金额
        self.cg_fjmoney = cg_fjmoney
        # 附加费用分类
        self.cg_fjmoneylx = cg_fjmoneylx
        # 优惠抹零金额
        self.cg_kjmoney = cg_kjmoney
        # 优惠折扣率
        self.cg_moneyzhekou = cg_moneyzhekou
        # 执行状态
        self.cg_zxstate = cg_zxstate
        # 采购日期
        self.cgdate = cgdate
        # 采购主题
        self.cgname = cgname
        # 采购单号
        self.cgno = cgno
        # 采购摘要
        self.cgremark = cgremark
        # 采购分类
        self.cgtype = cgtype
        # 产品明细，json格式
        self.child_mx = child_mx
        # 创建人
        self.data_userid = data_userid
        # 我方代表
        self.empid = empid
        # 供应商联系人
        self.gys_lxrid = gys_lxrid
        # 联系方式
        self.gys_lxrinfo = gys_lxrinfo
        # 供应商
        self.gysid = gysid
        # 供应商代表
        self.gysjingban = gysjingban
        # 关联订单
        self.order_htid = order_htid
        # 关联订单客户
        self.order_khid = order_khid
        # 采购金额
        self.summoney = summoney

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cg_fjmoney is not None:
            result['cg_fjmoney'] = self.cg_fjmoney
        if self.cg_fjmoneylx is not None:
            result['cg_fjmoneylx'] = self.cg_fjmoneylx
        if self.cg_kjmoney is not None:
            result['cg_kjmoney'] = self.cg_kjmoney
        if self.cg_moneyzhekou is not None:
            result['cg_moneyzhekou'] = self.cg_moneyzhekou
        if self.cg_zxstate is not None:
            result['cg_zxstate'] = self.cg_zxstate
        if self.cgdate is not None:
            result['cgdate'] = self.cgdate
        if self.cgname is not None:
            result['cgname'] = self.cgname
        if self.cgno is not None:
            result['cgno'] = self.cgno
        if self.cgremark is not None:
            result['cgremark'] = self.cgremark
        if self.cgtype is not None:
            result['cgtype'] = self.cgtype
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.empid is not None:
            result['empid'] = self.empid
        if self.gys_lxrid is not None:
            result['gys_lxrid'] = self.gys_lxrid
        if self.gys_lxrinfo is not None:
            result['gys_lxrinfo'] = self.gys_lxrinfo
        if self.gysid is not None:
            result['gysid'] = self.gysid
        if self.gysjingban is not None:
            result['gysjingban'] = self.gysjingban
        if self.order_htid is not None:
            result['order_htid'] = self.order_htid
        if self.order_khid is not None:
            result['order_khid'] = self.order_khid
        if self.summoney is not None:
            result['summoney'] = self.summoney
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cg_fjmoney') is not None:
            self.cg_fjmoney = m.get('cg_fjmoney')
        if m.get('cg_fjmoneylx') is not None:
            self.cg_fjmoneylx = m.get('cg_fjmoneylx')
        if m.get('cg_kjmoney') is not None:
            self.cg_kjmoney = m.get('cg_kjmoney')
        if m.get('cg_moneyzhekou') is not None:
            self.cg_moneyzhekou = m.get('cg_moneyzhekou')
        if m.get('cg_zxstate') is not None:
            self.cg_zxstate = m.get('cg_zxstate')
        if m.get('cgdate') is not None:
            self.cgdate = m.get('cgdate')
        if m.get('cgname') is not None:
            self.cgname = m.get('cgname')
        if m.get('cgno') is not None:
            self.cgno = m.get('cgno')
        if m.get('cgremark') is not None:
            self.cgremark = m.get('cgremark')
        if m.get('cgtype') is not None:
            self.cgtype = m.get('cgtype')
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('empid') is not None:
            self.empid = m.get('empid')
        if m.get('gys_lxrid') is not None:
            self.gys_lxrid = m.get('gys_lxrid')
        if m.get('gys_lxrinfo') is not None:
            self.gys_lxrinfo = m.get('gys_lxrinfo')
        if m.get('gysid') is not None:
            self.gysid = m.get('gysid')
        if m.get('gysjingban') is not None:
            self.gysjingban = m.get('gysjingban')
        if m.get('order_htid') is not None:
            self.order_htid = m.get('order_htid')
        if m.get('order_khid') is not None:
            self.order_khid = m.get('order_khid')
        if m.get('summoney') is not None:
            self.summoney = m.get('summoney')
        return self


class EditPurchaseRequest(TeaModel):
    def __init__(
        self,
        data: EditPurchaseRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写153
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditPurchaseRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditPurchaseResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditPurchaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditPurchaseResponseBody = None,
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
            temp_model = EditPurchaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQuotationRecordHeaders(TeaModel):
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


class EditQuotationRecordRequestData(TeaModel):
    def __init__(
        self,
        bj_bjren: str = None,
        bj_bzremark: str = None,
        bj_customerid: str = None,
        bj_date: str = None,
        bj_fjmoney: str = None,
        bj_fjmoneylx: str = None,
        bj_fkremark: str = None,
        bj_jfremark: str = None,
        bj_jshren: str = None,
        bj_kjmoney: str = None,
        bj_lianxi: str = None,
        bj_moneyzhekou: str = None,
        bj_number: str = None,
        bj_price: str = None,
        bj_remark: str = None,
        bj_state: str = None,
        bj_title: str = None,
        bj_xshid: str = None,
        child_mx: str = None,
        data_userid: str = None,
    ):
        # 报价人
        self.bj_bjren = bj_bjren
        # 包装运输
        self.bj_bzremark = bj_bzremark
        # 对应客户
        self.bj_customerid = bj_customerid
        # 报价日期
        self.bj_date = bj_date
        # 附加费用金额
        self.bj_fjmoney = bj_fjmoney
        # 附加费用分类
        self.bj_fjmoneylx = bj_fjmoneylx
        # 付款说明
        self.bj_fkremark = bj_fkremark
        # 交付说明
        self.bj_jfremark = bj_jfremark
        # 接收人
        self.bj_jshren = bj_jshren
        # 优惠抹零金额
        self.bj_kjmoney = bj_kjmoney
        # 联系方式
        self.bj_lianxi = bj_lianxi
        # 优惠折扣率
        self.bj_moneyzhekou = bj_moneyzhekou
        # 报价单号
        self.bj_number = bj_number
        # 报价(总)
        self.bj_price = bj_price
        # 备注
        self.bj_remark = bj_remark
        # 转成订单
        self.bj_state = bj_state
        # 主题
        self.bj_title = bj_title
        # 对应机会
        self.bj_xshid = bj_xshid
        # 产品明细，json格式
        self.child_mx = child_mx
        # 创建人
        self.data_userid = data_userid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bj_bjren is not None:
            result['bj_bjren'] = self.bj_bjren
        if self.bj_bzremark is not None:
            result['bj_bzremark'] = self.bj_bzremark
        if self.bj_customerid is not None:
            result['bj_customerid'] = self.bj_customerid
        if self.bj_date is not None:
            result['bj_date'] = self.bj_date
        if self.bj_fjmoney is not None:
            result['bj_fjmoney'] = self.bj_fjmoney
        if self.bj_fjmoneylx is not None:
            result['bj_fjmoneylx'] = self.bj_fjmoneylx
        if self.bj_fkremark is not None:
            result['bj_fkremark'] = self.bj_fkremark
        if self.bj_jfremark is not None:
            result['bj_jfremark'] = self.bj_jfremark
        if self.bj_jshren is not None:
            result['bj_jshren'] = self.bj_jshren
        if self.bj_kjmoney is not None:
            result['bj_kjmoney'] = self.bj_kjmoney
        if self.bj_lianxi is not None:
            result['bj_lianxi'] = self.bj_lianxi
        if self.bj_moneyzhekou is not None:
            result['bj_moneyzhekou'] = self.bj_moneyzhekou
        if self.bj_number is not None:
            result['bj_number'] = self.bj_number
        if self.bj_price is not None:
            result['bj_price'] = self.bj_price
        if self.bj_remark is not None:
            result['bj_remark'] = self.bj_remark
        if self.bj_state is not None:
            result['bj_state'] = self.bj_state
        if self.bj_title is not None:
            result['bj_title'] = self.bj_title
        if self.bj_xshid is not None:
            result['bj_xshid'] = self.bj_xshid
        if self.child_mx is not None:
            result['child_mx'] = self.child_mx
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bj_bjren') is not None:
            self.bj_bjren = m.get('bj_bjren')
        if m.get('bj_bzremark') is not None:
            self.bj_bzremark = m.get('bj_bzremark')
        if m.get('bj_customerid') is not None:
            self.bj_customerid = m.get('bj_customerid')
        if m.get('bj_date') is not None:
            self.bj_date = m.get('bj_date')
        if m.get('bj_fjmoney') is not None:
            self.bj_fjmoney = m.get('bj_fjmoney')
        if m.get('bj_fjmoneylx') is not None:
            self.bj_fjmoneylx = m.get('bj_fjmoneylx')
        if m.get('bj_fkremark') is not None:
            self.bj_fkremark = m.get('bj_fkremark')
        if m.get('bj_jfremark') is not None:
            self.bj_jfremark = m.get('bj_jfremark')
        if m.get('bj_jshren') is not None:
            self.bj_jshren = m.get('bj_jshren')
        if m.get('bj_kjmoney') is not None:
            self.bj_kjmoney = m.get('bj_kjmoney')
        if m.get('bj_lianxi') is not None:
            self.bj_lianxi = m.get('bj_lianxi')
        if m.get('bj_moneyzhekou') is not None:
            self.bj_moneyzhekou = m.get('bj_moneyzhekou')
        if m.get('bj_number') is not None:
            self.bj_number = m.get('bj_number')
        if m.get('bj_price') is not None:
            self.bj_price = m.get('bj_price')
        if m.get('bj_remark') is not None:
            self.bj_remark = m.get('bj_remark')
        if m.get('bj_state') is not None:
            self.bj_state = m.get('bj_state')
        if m.get('bj_title') is not None:
            self.bj_title = m.get('bj_title')
        if m.get('bj_xshid') is not None:
            self.bj_xshid = m.get('bj_xshid')
        if m.get('child_mx') is not None:
            self.child_mx = m.get('child_mx')
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        return self


class EditQuotationRecordRequest(TeaModel):
    def __init__(
        self,
        data: EditQuotationRecordRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写161
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditQuotationRecordRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditQuotationRecordResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditQuotationRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditQuotationRecordResponseBody = None,
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
            temp_model = EditQuotationRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditSalesHeaders(TeaModel):
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


class EditSalesRequestData(TeaModel):
    def __init__(
        self,
        data_userid: str = None,
        xsh_customerid: str = None,
        xsh_date: str = None,
        xsh_expdate: str = None,
        xsh_expmoney: str = None,
        xsh_from: str = None,
        xsh_knx: str = None,
        xsh_lianxi: str = None,
        xsh_lxrid: str = None,
        xsh_moneynote: str = None,
        xsh_number: str = None,
        xsh_phase: str = None,
        xsh_phasenote: str = None,
        xsh_preside: str = None,
        xsh_provider: str = None,
        xsh_require: str = None,
        xsh_state: str = None,
        xsh_title: str = None,
        xsh_type: str = None,
    ):
        # 创建人
        self.data_userid = data_userid
        # 对应客户
        self.xsh_customerid = xsh_customerid
        # 发现时间
        self.xsh_date = xsh_date
        # 预计签单日
        self.xsh_expdate = xsh_expdate
        # 预期金额
        self.xsh_expmoney = xsh_expmoney
        # 来源
        self.xsh_from = xsh_from
        # 可能性
        self.xsh_knx = xsh_knx
        # 联系方式
        self.xsh_lianxi = xsh_lianxi
        # 联系人
        self.xsh_lxrid = xsh_lxrid
        # 外币备注
        self.xsh_moneynote = xsh_moneynote
        # 机会编号
        self.xsh_number = xsh_number
        # 阶段
        self.xsh_phase = xsh_phase
        # 阶段备注
        self.xsh_phasenote = xsh_phasenote
        # 所有者
        self.xsh_preside = xsh_preside
        # 提供人
        self.xsh_provider = xsh_provider
        # 客户需求
        self.xsh_require = xsh_require
        # 状态
        self.xsh_state = xsh_state
        # 主题
        self.xsh_title = xsh_title
        # 类型
        self.xsh_type = xsh_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_userid is not None:
            result['data_userid'] = self.data_userid
        if self.xsh_customerid is not None:
            result['xsh_customerid'] = self.xsh_customerid
        if self.xsh_date is not None:
            result['xsh_date'] = self.xsh_date
        if self.xsh_expdate is not None:
            result['xsh_expdate'] = self.xsh_expdate
        if self.xsh_expmoney is not None:
            result['xsh_expmoney'] = self.xsh_expmoney
        if self.xsh_from is not None:
            result['xsh_from'] = self.xsh_from
        if self.xsh_knx is not None:
            result['xsh_knx'] = self.xsh_knx
        if self.xsh_lianxi is not None:
            result['xsh_lianxi'] = self.xsh_lianxi
        if self.xsh_lxrid is not None:
            result['xsh_lxrid'] = self.xsh_lxrid
        if self.xsh_moneynote is not None:
            result['xsh_moneynote'] = self.xsh_moneynote
        if self.xsh_number is not None:
            result['xsh_number'] = self.xsh_number
        if self.xsh_phase is not None:
            result['xsh_phase'] = self.xsh_phase
        if self.xsh_phasenote is not None:
            result['xsh_phasenote'] = self.xsh_phasenote
        if self.xsh_preside is not None:
            result['xsh_preside'] = self.xsh_preside
        if self.xsh_provider is not None:
            result['xsh_provider'] = self.xsh_provider
        if self.xsh_require is not None:
            result['xsh_require'] = self.xsh_require
        if self.xsh_state is not None:
            result['xsh_state'] = self.xsh_state
        if self.xsh_title is not None:
            result['xsh_title'] = self.xsh_title
        if self.xsh_type is not None:
            result['xsh_type'] = self.xsh_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_userid') is not None:
            self.data_userid = m.get('data_userid')
        if m.get('xsh_customerid') is not None:
            self.xsh_customerid = m.get('xsh_customerid')
        if m.get('xsh_date') is not None:
            self.xsh_date = m.get('xsh_date')
        if m.get('xsh_expdate') is not None:
            self.xsh_expdate = m.get('xsh_expdate')
        if m.get('xsh_expmoney') is not None:
            self.xsh_expmoney = m.get('xsh_expmoney')
        if m.get('xsh_from') is not None:
            self.xsh_from = m.get('xsh_from')
        if m.get('xsh_knx') is not None:
            self.xsh_knx = m.get('xsh_knx')
        if m.get('xsh_lianxi') is not None:
            self.xsh_lianxi = m.get('xsh_lianxi')
        if m.get('xsh_lxrid') is not None:
            self.xsh_lxrid = m.get('xsh_lxrid')
        if m.get('xsh_moneynote') is not None:
            self.xsh_moneynote = m.get('xsh_moneynote')
        if m.get('xsh_number') is not None:
            self.xsh_number = m.get('xsh_number')
        if m.get('xsh_phase') is not None:
            self.xsh_phase = m.get('xsh_phase')
        if m.get('xsh_phasenote') is not None:
            self.xsh_phasenote = m.get('xsh_phasenote')
        if m.get('xsh_preside') is not None:
            self.xsh_preside = m.get('xsh_preside')
        if m.get('xsh_provider') is not None:
            self.xsh_provider = m.get('xsh_provider')
        if m.get('xsh_require') is not None:
            self.xsh_require = m.get('xsh_require')
        if m.get('xsh_state') is not None:
            self.xsh_state = m.get('xsh_state')
        if m.get('xsh_title') is not None:
            self.xsh_title = m.get('xsh_title')
        if m.get('xsh_type') is not None:
            self.xsh_type = m.get('xsh_type')
        return self


class EditSalesRequest(TeaModel):
    def __init__(
        self,
        data: EditSalesRequestData = None,
        datatype: int = None,
        msgid: int = None,
        stamp: int = None,
    ):
        # 编辑数据
        self.data = data
        # 数据类型，固定填写158
        self.datatype = datatype
        # 数据id，不填或者填0为新增数据
        self.msgid = msgid
        # 时间戳
        self.stamp = stamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.stamp is not None:
            result['stamp'] = self.stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EditSalesRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        return self


class EditSalesResponseBody(TeaModel):
    def __init__(
        self,
        msgid: int = None,
        time: str = None,
    ):
        # 编辑数据的id
        self.msgid = msgid
        # 响应时间
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msgid is not None:
            result['msgid'] = self.msgid
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EditSalesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditSalesResponseBody = None,
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
            temp_model = EditSalesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataListHeaders(TeaModel):
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


class GetDataListRequest(TeaModel):
    def __init__(
        self,
        datatype: str = None,
        page: int = None,
        pagesize: int = None,
    ):
        # 数据类型，参考数据类型ID对照表
        self.datatype = datatype
        # 页码
        self.page = page
        # 分页条数
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class GetDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        detail: Dict[str, str] = None,
    ):
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        return self


class GetDataListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetDataListResponseBodyData] = None,
        dataname: Dict[str, str] = None,
        page: int = None,
        page_size: int = None,
        time: str = None,
        total_count: int = None,
    ):
        # 数据列表
        self.data = data
        # 字段明细
        self.dataname = dataname
        # 当前页码
        self.page = page
        # 分页条数
        self.page_size = page_size
        # 响应时间
        self.time = time
        # 总条数
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
        if self.dataname is not None:
            result['dataname'] = self.dataname
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.time is not None:
            result['time'] = self.time
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetDataListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('dataname') is not None:
            self.dataname = m.get('dataname')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataListResponseBody = None,
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
            temp_model = GetDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataViewHeaders(TeaModel):
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


class GetDataViewRequest(TeaModel):
    def __init__(
        self,
        datatype: str = None,
        msgid: int = None,
    ):
        # 数据类型，参考数据类型ID对照表
        self.datatype = datatype
        # 数据id
        self.msgid = msgid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.msgid is not None:
            result['msgid'] = self.msgid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('msgid') is not None:
            self.msgid = m.get('msgid')
        return self


class GetDataViewResponseBodyData(TeaModel):
    def __init__(
        self,
        detail: Dict[str, str] = None,
    ):
        # 数据详情
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        return self


class GetDataViewResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDataViewResponseBodyData = None,
        dataname: Dict[str, dict] = None,
        time: str = None,
    ):
        self.data = data
        # 字段明细
        self.dataname = dataname
        # 响应时间
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dataname is not None:
            result['dataname'] = self.dataname
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDataViewResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataname') is not None:
            self.dataname = m.get('dataname')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDataViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataViewResponseBody = None,
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
            temp_model = GetDataViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


