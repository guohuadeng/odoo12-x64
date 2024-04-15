# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDeviceHeaders(TeaModel):
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


class AddDeviceRequest(TeaModel):
    def __init__(
        self,
        merchant_id: str = None,
        model: str = None,
        name: str = None,
        scene: int = None,
        sn: str = None,
        status: int = None,
        type: int = None,
    ):
        # 商户id
        self.merchant_id = merchant_id
        # 设备型号
        self.model = model
        # 设备名称
        self.name = name
        # 消费场景
        self.scene = scene
        # sn码
        self.sn = sn
        # 设备状态
        self.status = status
        # 设备类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.model is not None:
            result['model'] = self.model
        if self.name is not None:
            result['name'] = self.name
        if self.scene is not None:
            result['scene'] = self.scene
        if self.sn is not None:
            result['sn'] = self.sn
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AddDeviceResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        merchant_id: str = None,
        sn: str = None,
        status: int = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 设备id
        self.id = id
        # 商户id
        self.merchant_id = merchant_id
        # 设备sn码
        self.sn = sn
        # 状态
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
        if self.id is not None:
            result['id'] = self.id
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class AddDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDeviceResponseBody = None,
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
            temp_model = AddDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateHeaders(TeaModel):
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


class BatchCreateRequestDataCardRuleItemParamList(TeaModel):
    def __init__(
        self,
        card_rule_attr: str = None,
        card_task_code: str = None,
        daily_dubbing: int = None,
        relation_id: str = None,
        relation_title: str = None,
        relation_url: str = None,
    ):
        # 扩展属性，存放配音难度、每日配音视频的url等
        self.card_rule_attr = card_rule_attr
        # 卡片taskCode
        self.card_task_code = card_task_code
        # 每日配音数
        self.daily_dubbing = daily_dubbing
        # 关联的外部Id
        self.relation_id = relation_id
        # 关联内容标题（会在打卡详页页展示）
        self.relation_title = relation_title
        # relationUrl（点击打卡内容后跳转的链接）（点击卡片内容后跳转的链接）
        self.relation_url = relation_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_rule_attr is not None:
            result['cardRuleAttr'] = self.card_rule_attr
        if self.card_task_code is not None:
            result['cardTaskCode'] = self.card_task_code
        if self.daily_dubbing is not None:
            result['dailyDubbing'] = self.daily_dubbing
        if self.relation_id is not None:
            result['relationId'] = self.relation_id
        if self.relation_title is not None:
            result['relationTitle'] = self.relation_title
        if self.relation_url is not None:
            result['relationUrl'] = self.relation_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardRuleAttr') is not None:
            self.card_rule_attr = m.get('cardRuleAttr')
        if m.get('cardTaskCode') is not None:
            self.card_task_code = m.get('cardTaskCode')
        if m.get('dailyDubbing') is not None:
            self.daily_dubbing = m.get('dailyDubbing')
        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')
        if m.get('relationTitle') is not None:
            self.relation_title = m.get('relationTitle')
        if m.get('relationUrl') is not None:
            self.relation_url = m.get('relationUrl')
        return self


class BatchCreateRequestDataOrgClassStudentGroupListClassListStudents(TeaModel):
    def __init__(
        self,
        name: str = None,
        staff_id: str = None,
    ):
        # 学生名称
        self.name = name
        # 学生id
        self.staff_id = staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.staff_id is not None:
            result['staffId'] = self.staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')
        return self


class BatchCreateRequestDataOrgClassStudentGroupListClassList(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        class_name: str = None,
        students: List[BatchCreateRequestDataOrgClassStudentGroupListClassListStudents] = None,
    ):
        # 班级id
        self.class_id = class_id
        # 班级名称
        self.class_name = class_name
        # 班级学生
        self.students = students

    def validate(self):
        if self.students:
            for k in self.students:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.class_name is not None:
            result['className'] = self.class_name
        result['students'] = []
        if self.students is not None:
            for k in self.students:
                result['students'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        self.students = []
        if m.get('students') is not None:
            for k in m.get('students'):
                temp_model = BatchCreateRequestDataOrgClassStudentGroupListClassListStudents()
                self.students.append(temp_model.from_map(k))
        return self


class BatchCreateRequestDataOrgClassStudentGroupList(TeaModel):
    def __init__(
        self,
        class_list: List[BatchCreateRequestDataOrgClassStudentGroupListClassList] = None,
        corp_id: str = None,
    ):
        # 班级列表
        self.class_list = class_list
        # 组织id
        self.corp_id = corp_id

    def validate(self):
        if self.class_list:
            for k in self.class_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['classList'] = []
        if self.class_list is not None:
            for k in self.class_list:
                result['classList'].append(k.to_map() if k else None)
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_list = []
        if m.get('classList') is not None:
            for k in m.get('classList'):
                temp_model = BatchCreateRequestDataOrgClassStudentGroupListClassList()
                self.class_list.append(temp_model.from_map(k))
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        return self


class BatchCreateRequestData(TeaModel):
    def __init__(
        self,
        can_reissue_card: bool = None,
        card_cycle: int = None,
        card_frequency: List[int] = None,
        card_rule_item_param_list: List[BatchCreateRequestDataCardRuleItemParamList] = None,
        class_ids: List[str] = None,
        class_names: List[str] = None,
        content: str = None,
        effect_date: int = None,
        medias: str = None,
        need_metering: str = None,
        org_class_student_group_list: List[BatchCreateRequestDataOrgClassStudentGroupList] = None,
        remind_hour: int = None,
        remind_minute: int = None,
        target_role: str = None,
        template_id: int = None,
        title: str = None,
        unit_of_measurement: str = None,
    ):
        # 是否可以补卡
        self.can_reissue_card = can_reissue_card
        # 打卡周期,单位为天
        self.card_cycle = card_cycle
        # 打卡的频次设置："cardFrequency":[             1,//周天             2,//周一             3,//周二             4,//周三             5,//周四             6,//周五             7//周六         ]
        self.card_frequency = card_frequency
        self.card_rule_item_param_list = card_rule_item_param_list
        # 班级列表
        self.class_ids = class_ids
        # 班级名称列表
        self.class_names = class_names
        # 打卡的内容
        self.content = content
        # 卡片生效时间
        self.effect_date = effect_date
        # 上传相册，图片，录音，盯盘的信息
        self.medias = medias
        # 计量开启
        self.need_metering = need_metering
        self.org_class_student_group_list = org_class_student_group_list
        # 提醒时间（小时）
        self.remind_hour = remind_hour
        # 提醒时间（分钟）
        self.remind_minute = remind_minute
        # 默认：student_guardian
        self.target_role = target_role
        # 打卡模板id
        self.template_id = template_id
        # 卡片标题
        self.title = title
        # 计量单位
        self.unit_of_measurement = unit_of_measurement

    def validate(self):
        if self.card_rule_item_param_list:
            for k in self.card_rule_item_param_list:
                if k:
                    k.validate()
        if self.org_class_student_group_list:
            for k in self.org_class_student_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_reissue_card is not None:
            result['canReissueCard'] = self.can_reissue_card
        if self.card_cycle is not None:
            result['cardCycle'] = self.card_cycle
        if self.card_frequency is not None:
            result['cardFrequency'] = self.card_frequency
        result['cardRuleItemParamList'] = []
        if self.card_rule_item_param_list is not None:
            for k in self.card_rule_item_param_list:
                result['cardRuleItemParamList'].append(k.to_map() if k else None)
        if self.class_ids is not None:
            result['classIds'] = self.class_ids
        if self.class_names is not None:
            result['classNames'] = self.class_names
        if self.content is not None:
            result['content'] = self.content
        if self.effect_date is not None:
            result['effectDate'] = self.effect_date
        if self.medias is not None:
            result['medias'] = self.medias
        if self.need_metering is not None:
            result['needMetering'] = self.need_metering
        result['orgClassStudentGroupList'] = []
        if self.org_class_student_group_list is not None:
            for k in self.org_class_student_group_list:
                result['orgClassStudentGroupList'].append(k.to_map() if k else None)
        if self.remind_hour is not None:
            result['remindHour'] = self.remind_hour
        if self.remind_minute is not None:
            result['remindMinute'] = self.remind_minute
        if self.target_role is not None:
            result['targetRole'] = self.target_role
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.title is not None:
            result['title'] = self.title
        if self.unit_of_measurement is not None:
            result['unitOfMeasurement'] = self.unit_of_measurement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canReissueCard') is not None:
            self.can_reissue_card = m.get('canReissueCard')
        if m.get('cardCycle') is not None:
            self.card_cycle = m.get('cardCycle')
        if m.get('cardFrequency') is not None:
            self.card_frequency = m.get('cardFrequency')
        self.card_rule_item_param_list = []
        if m.get('cardRuleItemParamList') is not None:
            for k in m.get('cardRuleItemParamList'):
                temp_model = BatchCreateRequestDataCardRuleItemParamList()
                self.card_rule_item_param_list.append(temp_model.from_map(k))
        if m.get('classIds') is not None:
            self.class_ids = m.get('classIds')
        if m.get('classNames') is not None:
            self.class_names = m.get('classNames')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('effectDate') is not None:
            self.effect_date = m.get('effectDate')
        if m.get('medias') is not None:
            self.medias = m.get('medias')
        if m.get('needMetering') is not None:
            self.need_metering = m.get('needMetering')
        self.org_class_student_group_list = []
        if m.get('orgClassStudentGroupList') is not None:
            for k in m.get('orgClassStudentGroupList'):
                temp_model = BatchCreateRequestDataOrgClassStudentGroupList()
                self.org_class_student_group_list.append(temp_model.from_map(k))
        if m.get('remindHour') is not None:
            self.remind_hour = m.get('remindHour')
        if m.get('remindMinute') is not None:
            self.remind_minute = m.get('remindMinute')
        if m.get('targetRole') is not None:
            self.target_role = m.get('targetRole')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('unitOfMeasurement') is not None:
            self.unit_of_measurement = m.get('unitOfMeasurement')
        return self


class BatchCreateRequest(TeaModel):
    def __init__(
        self,
        card_biz_code: str = None,
        data: BatchCreateRequestData = None,
        identifier: str = None,
        js_version: int = None,
        source_type: str = None,
        userid: str = None,
    ):
        # 卡片业务类型，打卡写死：industry_center
        self.card_biz_code = card_biz_code
        # 卡片详细数据
        self.data = data
        # 卡片幂等唯一键
        self.identifier = identifier
        # 小程序版本号
        self.js_version = js_version
        # isv业务类型
        self.source_type = source_type
        # 老师用户id
        self.userid = userid

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_biz_code is not None:
            result['cardBizCode'] = self.card_biz_code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.js_version is not None:
            result['jsVersion'] = self.js_version
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardBizCode') is not None:
            self.card_biz_code = m.get('cardBizCode')
        if m.get('data') is not None:
            temp_model = BatchCreateRequestData()
            self.data = temp_model.from_map(m['data'])
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('jsVersion') is not None:
            self.js_version = m.get('jsVersion')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class BatchCreateResponseBodyResult(TeaModel):
    def __init__(
        self,
        corp_id_card_id_map: Dict[str, str] = None,
    ):
        self.corp_id_card_id_map = corp_id_card_id_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id_card_id_map is not None:
            result['corpIdCardIdMap'] = self.corp_id_card_id_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpIdCardIdMap') is not None:
            self.corp_id_card_id_map = m.get('corpIdCardIdMap')
        return self


class BatchCreateResponseBody(TeaModel):
    def __init__(
        self,
        result: BatchCreateResponseBodyResult = None,
    ):
        # result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = BatchCreateResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class BatchCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchCreateResponseBody = None,
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
            temp_model = BatchCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchOrgCreateHWHeaders(TeaModel):
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


class BatchOrgCreateHWRequestOpenSelectItemListClassListStudents(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        name: str = None,
        staff_id: str = None,
    ):
        # 学生头像
        self.avatar = avatar
        # 学生姓名
        self.name = name
        # 学生userid
        self.staff_id = staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.name is not None:
            result['name'] = self.name
        if self.staff_id is not None:
            result['staffId'] = self.staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')
        return self


class BatchOrgCreateHWRequestOpenSelectItemListClassList(TeaModel):
    def __init__(
        self,
        all: bool = None,
        class_id: str = None,
        class_name: str = None,
        students: List[BatchOrgCreateHWRequestOpenSelectItemListClassListStudents] = None,
    ):
        # 是否全选
        self.all = all
        # 班级id
        self.class_id = class_id
        # 班级名称
        self.class_name = class_name
        # 学生列表
        self.students = students

    def validate(self):
        if self.students:
            for k in self.students:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.class_name is not None:
            result['className'] = self.class_name
        result['students'] = []
        if self.students is not None:
            for k in self.students:
                result['students'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        self.students = []
        if m.get('students') is not None:
            for k in m.get('students'):
                temp_model = BatchOrgCreateHWRequestOpenSelectItemListClassListStudents()
                self.students.append(temp_model.from_map(k))
        return self


class BatchOrgCreateHWRequestOpenSelectItemList(TeaModel):
    def __init__(
        self,
        class_list: List[BatchOrgCreateHWRequestOpenSelectItemListClassList] = None,
        corp_id: str = None,
        selected_classes_desc: str = None,
    ):
        # 班级列表
        self.class_list = class_list
        # 组织corpId
        self.corp_id = corp_id
        # 选择内容
        self.selected_classes_desc = selected_classes_desc

    def validate(self):
        if self.class_list:
            for k in self.class_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['classList'] = []
        if self.class_list is not None:
            for k in self.class_list:
                result['classList'].append(k.to_map() if k else None)
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.selected_classes_desc is not None:
            result['selectedClassesDesc'] = self.selected_classes_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_list = []
        if m.get('classList') is not None:
            for k in m.get('classList'):
                temp_model = BatchOrgCreateHWRequestOpenSelectItemListClassList()
                self.class_list.append(temp_model.from_map(k))
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('selectedClassesDesc') is not None:
            self.selected_classes_desc = m.get('selectedClassesDesc')
        return self


class BatchOrgCreateHWRequest(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        biz_code: str = None,
        course_name: str = None,
        hw_content: str = None,
        hw_deadline: int = None,
        hw_deadline_open: str = None,
        hw_media: str = None,
        hw_photo: str = None,
        hw_title: str = None,
        hw_type: str = None,
        hw_video: str = None,
        identifier: str = None,
        open_select_item_list: List[BatchOrgCreateHWRequestOpenSelectItemList] = None,
        scheduled_release: str = None,
        scheduled_time: str = None,
        status: str = None,
        target_role: str = None,
        teacher_name: str = None,
        teacher_user_id: str = None,
    ):
        # 扩展属性
        self.attributes = attributes
        # 业务编码
        self.biz_code = biz_code
        # 作业课程名称
        self.course_name = course_name
        # 作业内容
        self.hw_content = hw_content
        # 截止时间
        self.hw_deadline = hw_deadline
        # 截止时间开启
        self.hw_deadline_open = hw_deadline_open
        # 作业视频
        self.hw_media = hw_media
        # 作业图片
        self.hw_photo = hw_photo
        # 作业标题
        self.hw_title = hw_title
        # 作业类型
        self.hw_type = hw_type
        # 作业音视频
        self.hw_video = hw_video
        # 幂等ID字段
        self.identifier = identifier
        # 选择跨组织班级
        self.open_select_item_list = open_select_item_list
        # 定时调度
        self.scheduled_release = scheduled_release
        # 定时调度时间
        self.scheduled_time = scheduled_time
        # 状态
        self.status = status
        # 发送对象
        self.target_role = target_role
        # 老师名称
        self.teacher_name = teacher_name
        # 老师userid
        self.teacher_user_id = teacher_user_id

    def validate(self):
        if self.open_select_item_list:
            for k in self.open_select_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.hw_content is not None:
            result['hwContent'] = self.hw_content
        if self.hw_deadline is not None:
            result['hwDeadline'] = self.hw_deadline
        if self.hw_deadline_open is not None:
            result['hwDeadlineOpen'] = self.hw_deadline_open
        if self.hw_media is not None:
            result['hwMedia'] = self.hw_media
        if self.hw_photo is not None:
            result['hwPhoto'] = self.hw_photo
        if self.hw_title is not None:
            result['hwTitle'] = self.hw_title
        if self.hw_type is not None:
            result['hwType'] = self.hw_type
        if self.hw_video is not None:
            result['hwVideo'] = self.hw_video
        if self.identifier is not None:
            result['identifier'] = self.identifier
        result['openSelectItemList'] = []
        if self.open_select_item_list is not None:
            for k in self.open_select_item_list:
                result['openSelectItemList'].append(k.to_map() if k else None)
        if self.scheduled_release is not None:
            result['scheduledRelease'] = self.scheduled_release
        if self.scheduled_time is not None:
            result['scheduledTime'] = self.scheduled_time
        if self.status is not None:
            result['status'] = self.status
        if self.target_role is not None:
            result['targetRole'] = self.target_role
        if self.teacher_name is not None:
            result['teacherName'] = self.teacher_name
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('hwContent') is not None:
            self.hw_content = m.get('hwContent')
        if m.get('hwDeadline') is not None:
            self.hw_deadline = m.get('hwDeadline')
        if m.get('hwDeadlineOpen') is not None:
            self.hw_deadline_open = m.get('hwDeadlineOpen')
        if m.get('hwMedia') is not None:
            self.hw_media = m.get('hwMedia')
        if m.get('hwPhoto') is not None:
            self.hw_photo = m.get('hwPhoto')
        if m.get('hwTitle') is not None:
            self.hw_title = m.get('hwTitle')
        if m.get('hwType') is not None:
            self.hw_type = m.get('hwType')
        if m.get('hwVideo') is not None:
            self.hw_video = m.get('hwVideo')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        self.open_select_item_list = []
        if m.get('openSelectItemList') is not None:
            for k in m.get('openSelectItemList'):
                temp_model = BatchOrgCreateHWRequestOpenSelectItemList()
                self.open_select_item_list.append(temp_model.from_map(k))
        if m.get('scheduledRelease') is not None:
            self.scheduled_release = m.get('scheduledRelease')
        if m.get('scheduledTime') is not None:
            self.scheduled_time = m.get('scheduledTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('targetRole') is not None:
            self.target_role = m.get('targetRole')
        if m.get('teacherName') is not None:
            self.teacher_name = m.get('teacherName')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        return self


class BatchOrgCreateHWResponseBodyResultPublishList(TeaModel):
    def __init__(
        self,
        corpid: str = None,
        hwid: int = None,
    ):
        self.corpid = corpid
        self.hwid = hwid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpid is not None:
            result['corpid'] = self.corpid
        if self.hwid is not None:
            result['hwid'] = self.hwid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpid') is not None:
            self.corpid = m.get('corpid')
        if m.get('hwid') is not None:
            self.hwid = m.get('hwid')
        return self


class BatchOrgCreateHWResponseBodyResult(TeaModel):
    def __init__(
        self,
        publish_list: List[BatchOrgCreateHWResponseBodyResultPublishList] = None,
    ):
        self.publish_list = publish_list

    def validate(self):
        if self.publish_list:
            for k in self.publish_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['publishList'] = []
        if self.publish_list is not None:
            for k in self.publish_list:
                result['publishList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.publish_list = []
        if m.get('publishList') is not None:
            for k in m.get('publishList'):
                temp_model = BatchOrgCreateHWResponseBodyResultPublishList()
                self.publish_list.append(temp_model.from_map(k))
        return self


class BatchOrgCreateHWResponseBody(TeaModel):
    def __init__(
        self,
        result: BatchOrgCreateHWResponseBodyResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = BatchOrgCreateHWResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class BatchOrgCreateHWResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchOrgCreateHWResponseBody = None,
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
            temp_model = BatchOrgCreateHWResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderHeaders(TeaModel):
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


class CancelOrderRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        order_no: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        user_id: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 订单号
        self.order_no = order_no
        # 签名
        self.signature = signature
        # 设备号
        self.sn = sn
        # utc时间戳
        self.timestamp = timestamp
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CancelOrderResponseBody(TeaModel):
    def __init__(
        self,
        need_retry: bool = None,
        trade_action: str = None,
    ):
        # 是否需要重试
        self.need_retry = need_retry
        # 交易动作
        self.trade_action = trade_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_retry is not None:
            result['needRetry'] = self.need_retry
        if self.trade_action is not None:
            result['tradeAction'] = self.trade_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('needRetry') is not None:
            self.need_retry = m.get('needRetry')
        if m.get('tradeAction') is not None:
            self.trade_action = m.get('tradeAction')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelOrderResponseBody = None,
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRestrictionHeaders(TeaModel):
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


class CheckRestrictionRequest(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        face_id: str = None,
        scene: int = None,
        sn: str = None,
        user_id: str = None,
    ):
        # 实付金额，单位分
        self.actual_amount = actual_amount
        # 人脸id
        self.face_id = face_id
        # 场景
        self.scene = scene
        # 设备号
        self.sn = sn
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.sn is not None:
            result['sn'] = self.sn
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CheckRestrictionResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 返回结果
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


class CheckRestrictionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckRestrictionResponseBody = None,
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
            temp_model = CheckRestrictionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CourseSchedulingComplimentNoticeHeaders(TeaModel):
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


class CourseSchedulingComplimentNoticeRequest(TeaModel):
    def __init__(
        self,
        op_user_id: str = None,
    ):
        # opUserId
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


class CourseSchedulingComplimentNoticeResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 通知课程导入完成是否成功。
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


class CourseSchedulingComplimentNoticeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CourseSchedulingComplimentNoticeResponseBody = None,
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
            temp_model = CourseSchedulingComplimentNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomClassHeaders(TeaModel):
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


class CreateCustomClassRequestCustomClass(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # 班级名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateCustomClassRequest(TeaModel):
    def __init__(
        self,
        custom_class: CreateCustomClassRequestCustomClass = None,
        operator: str = None,
        super_id: int = None,
    ):
        # 班级信息
        self.custom_class = custom_class
        # 钉钉企业管理员工ID
        self.operator = operator
        # 上级部门ID
        self.super_id = super_id

    def validate(self):
        if self.custom_class:
            self.custom_class.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_class is not None:
            result['customClass'] = self.custom_class.to_map()
        if self.operator is not None:
            result['operator'] = self.operator
        if self.super_id is not None:
            result['superId'] = self.super_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customClass') is not None:
            temp_model = CreateCustomClassRequestCustomClass()
            self.custom_class = temp_model.from_map(m['customClass'])
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('superId') is not None:
            self.super_id = m.get('superId')
        return self


class CreateCustomClassResponseBodyResult(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
    ):
        # 班级ID
        self.dept_id = dept_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        return self


class CreateCustomClassResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateCustomClassResponseBodyResult = None,
        success: bool = None,
    ):
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateCustomClassResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateCustomClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCustomClassResponseBody = None,
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
            temp_model = CreateCustomClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDeptHeaders(TeaModel):
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


class CreateCustomDeptRequestCustomDept(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # 自定义校区或部门名称
        self.name = name
        # 部门类型：custom_campus: 自定义校区；custom_dept: 自定义部门
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateCustomDeptRequest(TeaModel):
    def __init__(
        self,
        custom_dept: CreateCustomDeptRequestCustomDept = None,
        operator: str = None,
        super_id: int = None,
    ):
        self.custom_dept = custom_dept
        # 钉钉管理员员工ID
        self.operator = operator
        # 上级部门ID（type为custom_campus时，必须为-7）
        self.super_id = super_id

    def validate(self):
        if self.custom_dept:
            self.custom_dept.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_dept is not None:
            result['customDept'] = self.custom_dept.to_map()
        if self.operator is not None:
            result['operator'] = self.operator
        if self.super_id is not None:
            result['superId'] = self.super_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customDept') is not None:
            temp_model = CreateCustomDeptRequestCustomDept()
            self.custom_dept = temp_model.from_map(m['customDept'])
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('superId') is not None:
            self.super_id = m.get('superId')
        return self


class CreateCustomDeptResponseBodyResult(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
    ):
        # 部门ID
        self.dept_id = dept_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        return self


class CreateCustomDeptResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateCustomDeptResponseBodyResult = None,
        success: bool = None,
    ):
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateCustomDeptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateCustomDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCustomDeptResponseBody = None,
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
            temp_model = CreateCustomDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEduAssetSpaceHeaders(TeaModel):
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


class CreateEduAssetSpaceRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        space_desc: str = None,
        space_icon: str = None,
        space_name: str = None,
        user_id: str = None,
    ):
        # 业务类型编码
        self.biz_code = biz_code
        # 空间描述
        self.space_desc = space_desc
        # 空间图标
        self.space_icon = space_icon
        # 空间名称
        self.space_name = space_name
        # 用户staffId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.space_desc is not None:
            result['spaceDesc'] = self.space_desc
        if self.space_icon is not None:
            result['spaceIcon'] = self.space_icon
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('spaceDesc') is not None:
            self.space_desc = m.get('spaceDesc')
        if m.get('spaceIcon') is not None:
            self.space_icon = m.get('spaceIcon')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateEduAssetSpaceResponseBody(TeaModel):
    def __init__(
        self,
        create_time_millis: int = None,
        modify_time_millis: int = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间戳
        self.create_time_millis = create_time_millis
        # 修改时间戳
        self.modify_time_millis = modify_time_millis
        # 权限模型
        self.permission_mode = permission_mode
        # 总容量
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 已使用容量
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_millis is not None:
            result['createTimeMillis'] = self.create_time_millis
        if self.modify_time_millis is not None:
            result['modifyTimeMillis'] = self.modify_time_millis
        if self.permission_mode is not None:
            result['permissionMode'] = self.permission_mode
        if self.quota is not None:
            result['quota'] = self.quota
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimeMillis') is not None:
            self.create_time_millis = m.get('createTimeMillis')
        if m.get('modifyTimeMillis') is not None:
            self.modify_time_millis = m.get('modifyTimeMillis')
        if m.get('permissionMode') is not None:
            self.permission_mode = m.get('permissionMode')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')
        return self


class CreateEduAssetSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEduAssetSpaceResponseBody = None,
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
            temp_model = CreateEduAssetSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFulfilRecordHeaders(TeaModel):
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


class CreateFulfilRecordRequest(TeaModel):
    def __init__(
        self,
        biz_time: int = None,
        ext_info: str = None,
        face_id: str = None,
        scene: int = None,
        sn: str = None,
        user_id: str = None,
    ):
        # 业务发生时间
        self.biz_time = biz_time
        # 扩展信息，json格式
        self.ext_info = ext_info
        # 人脸id
        self.face_id = face_id
        # 场景
        self.scene = scene
        # 设备sn号
        self.sn = sn
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_time is not None:
            result['bizTime'] = self.biz_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.sn is not None:
            result['sn'] = self.sn
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTime') is not None:
            self.biz_time = m.get('bizTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateFulfilRecordResponseBody(TeaModel):
    def __init__(
        self,
        success_info: str = None,
    ):
        # 成功信息
        self.success_info = success_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_info is not None:
            result['successInfo'] = self.success_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('successInfo') is not None:
            self.success_info = m.get('successInfo')
        return self


class CreateFulfilRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFulfilRecordResponseBody = None,
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
            temp_model = CreateFulfilRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInviteUrlHeaders(TeaModel):
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


class CreateInviteUrlRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        target_corp_id: str = None,
        target_operator: str = None,
    ):
        self.auth_code = auth_code
        self.target_corp_id = target_corp_id
        self.target_operator = target_operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.target_corp_id is not None:
            result['targetCorpId'] = self.target_corp_id
        if self.target_operator is not None:
            result['targetOperator'] = self.target_operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('targetCorpId') is not None:
            self.target_corp_id = m.get('targetCorpId')
        if m.get('targetOperator') is not None:
            self.target_operator = m.get('targetOperator')
        return self


class CreateInviteUrlResponseBodyResult(TeaModel):
    def __init__(
        self,
        invite_url: str = None,
    ):
        self.invite_url = invite_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_url is not None:
            result['inviteUrl'] = self.invite_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inviteUrl') is not None:
            self.invite_url = m.get('inviteUrl')
        return self


class CreateInviteUrlResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateInviteUrlResponseBodyResult = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateInviteUrlResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateInviteUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInviteUrlResponseBody = None,
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
            temp_model = CreateInviteUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateItemHeaders(TeaModel):
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


class CreateItemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        effect_type: int = None,
        end_time: int = None,
        merchant_id: str = None,
        name: str = None,
        opt_user: str = None,
        period_type: int = None,
        price: int = None,
        scene: int = None,
        start_time: int = None,
        type: int = None,
    ):
        self.description = description
        self.effect_type = effect_type
        self.end_time = end_time
        self.merchant_id = merchant_id
        self.name = name
        self.opt_user = opt_user
        self.period_type = period_type
        self.price = price
        self.scene = scene
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.effect_type is not None:
            result['effectType'] = self.effect_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.name is not None:
            result['name'] = self.name
        if self.opt_user is not None:
            result['optUser'] = self.opt_user
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.price is not None:
            result['price'] = self.price
        if self.scene is not None:
            result['scene'] = self.scene
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effectType') is not None:
            self.effect_type = m.get('effectType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('optUser') is not None:
            self.opt_user = m.get('optUser')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateItemResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        merchant_id: str = None,
        status: int = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.merchant_id = merchant_id
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
        if self.id is not None:
            result['id'] = self.id
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateItemResponseBody = None,
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
            temp_model = CreateItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderHeaders(TeaModel):
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


class CreateOrderRequestDetailList(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        item_amount: int = None,
        item_name: str = None,
        scene: int = None,
    ):
        # 计算优惠后的实付金额，单位为分
        self.actual_amount = actual_amount
        # 应付金额，单位为分
        self.item_amount = item_amount
        # 商品名
        self.item_name = item_name
        # 场景
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.item_amount is not None:
            result['itemAmount'] = self.item_amount
        if self.item_name is not None:
            result['itemName'] = self.item_name
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('itemAmount') is not None:
            self.item_amount = m.get('itemAmount')
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        create_time: int = None,
        detail_list: List[CreateOrderRequestDetailList] = None,
        face_id: str = None,
        ftoken: str = None,
        signature: str = None,
        sn: str = None,
        terminal_params: str = None,
        timestamp: int = None,
        total_amount: int = None,
        user_id: str = None,
        version: str = None,
    ):
        # 实付金额，单位分（优惠计算后）
        self.actual_amount = actual_amount
        # 开单时间
        self.create_time = create_time
        # 订单明细信息
        self.detail_list = detail_list
        # 人脸id
        self.face_id = face_id
        # 刷脸token
        self.ftoken = ftoken
        # 签名
        self.signature = signature
        # 设备号
        self.sn = sn
        # 交易加签
        self.terminal_params = terminal_params
        # utc时间戳
        self.timestamp = timestamp
        # 应付价格，单位分
        self.total_amount = total_amount
        # 员工id
        self.user_id = user_id
        # 版本号
        self.version = version

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['detailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.ftoken is not None:
            result['ftoken'] = self.ftoken
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.terminal_params is not None:
            result['terminalParams'] = self.terminal_params
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.detail_list = []
        if m.get('detailList') is not None:
            for k in m.get('detailList'):
                temp_model = CreateOrderRequestDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('ftoken') is not None:
            self.ftoken = m.get('ftoken')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('terminalParams') is not None:
            self.terminal_params = m.get('terminalParams')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        order_no: str = None,
    ):
        # 订单号
        self.order_no = order_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderFlowHeaders(TeaModel):
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


class CreateOrderFlowRequestDetailList(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        item_amount: int = None,
        item_id: int = None,
        item_name: str = None,
        scene: int = None,
    ):
        # 计算优惠后的实付金额，单位为分
        self.actual_amount = actual_amount
        # 应付金额，单位为分
        self.item_amount = item_amount
        # 商品id
        self.item_id = item_id
        # 商品名
        self.item_name = item_name
        # 场景
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.item_amount is not None:
            result['itemAmount'] = self.item_amount
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.item_name is not None:
            result['itemName'] = self.item_name
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('itemAmount') is not None:
            self.item_amount = m.get('itemAmount')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class CreateOrderFlowRequest(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        alipay_uid: str = None,
        create_time: int = None,
        detail_list: List[CreateOrderFlowRequestDetailList] = None,
        face_id: str = None,
        merchant_id: str = None,
        order_no: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        total_amount: int = None,
        user_id: str = None,
    ):
        # 实付金额，单位分（优惠计算后）
        self.actual_amount = actual_amount
        # 支付宝用户id
        self.alipay_uid = alipay_uid
        # 开单时间
        self.create_time = create_time
        # 订单明细信息，来源于商户系统或APP的商品信息。
        self.detail_list = detail_list
        # 人脸id
        self.face_id = face_id
        # 商户id
        self.merchant_id = merchant_id
        # 订单号
        self.order_no = order_no
        # 签名
        self.signature = signature
        # 设备号
        self.sn = sn
        # utc时间戳
        self.timestamp = timestamp
        # 应付价格，单位分
        self.total_amount = total_amount
        # 员工id
        self.user_id = user_id

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.alipay_uid is not None:
            result['alipayUid'] = self.alipay_uid
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['detailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('alipayUid') is not None:
            self.alipay_uid = m.get('alipayUid')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.detail_list = []
        if m.get('detailList') is not None:
            for k in m.get('detailList'):
                temp_model = CreateOrderFlowRequestDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateOrderFlowResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 返回结果
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


class CreateOrderFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderFlowResponseBody = None,
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
            temp_model = CreateOrderFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhysicalClassroomHeaders(TeaModel):
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


class CreatePhysicalClassroomRequest(TeaModel):
    def __init__(
        self,
        classroom_building: str = None,
        classroom_campus: str = None,
        classroom_floor: str = None,
        classroom_name: str = None,
        classroom_number: str = None,
        direct_broadcast: str = None,
        ext: str = None,
        op_user_id: str = None,
    ):
        # 教室教学楼
        self.classroom_building = classroom_building
        # 教室校区
        self.classroom_campus = classroom_campus
        # 教室楼层
        self.classroom_floor = classroom_floor
        # 教室名称
        self.classroom_name = classroom_name
        # 教室房间号
        self.classroom_number = classroom_number
        # 是否支持直播
        self.direct_broadcast = direct_broadcast
        # 扩展信息
        self.ext = ext
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_building is not None:
            result['classroomBuilding'] = self.classroom_building
        if self.classroom_campus is not None:
            result['classroomCampus'] = self.classroom_campus
        if self.classroom_floor is not None:
            result['classroomFloor'] = self.classroom_floor
        if self.classroom_name is not None:
            result['classroomName'] = self.classroom_name
        if self.classroom_number is not None:
            result['classroomNumber'] = self.classroom_number
        if self.direct_broadcast is not None:
            result['directBroadcast'] = self.direct_broadcast
        if self.ext is not None:
            result['ext'] = self.ext
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomBuilding') is not None:
            self.classroom_building = m.get('classroomBuilding')
        if m.get('classroomCampus') is not None:
            self.classroom_campus = m.get('classroomCampus')
        if m.get('classroomFloor') is not None:
            self.classroom_floor = m.get('classroomFloor')
        if m.get('classroomName') is not None:
            self.classroom_name = m.get('classroomName')
        if m.get('classroomNumber') is not None:
            self.classroom_number = m.get('classroomNumber')
        if m.get('directBroadcast') is not None:
            self.direct_broadcast = m.get('directBroadcast')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class CreatePhysicalClassroomResponseBody(TeaModel):
    def __init__(
        self,
        classroom_id: int = None,
    ):
        # 教室id
        self.classroom_id = classroom_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        return self


class CreatePhysicalClassroomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePhysicalClassroomResponseBody = None,
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
            temp_model = CreatePhysicalClassroomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRefundFlowHeaders(TeaModel):
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


class CreateRefundFlowRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        operator_id: str = None,
        operator_name: str = None,
        order_no: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        user_id: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 操作人id
        self.operator_id = operator_id
        # 操作人名称
        self.operator_name = operator_name
        # 订单号
        self.order_no = order_no
        # 签名
        self.signature = signature
        # 设备号
        self.sn = sn
        # utc时间戳
        self.timestamp = timestamp
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateRefundFlowResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 返回结果
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


class CreateRefundFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRefundFlowResponseBody = None,
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
            temp_model = CreateRefundFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRemoteClassCourseHeaders(TeaModel):
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


class CreateRemoteClassCourseRequestAttendParticipants(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        participant_id: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 参与方ID
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        return self


class CreateRemoteClassCourseRequestTeachingParticipant(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        participant_id: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 参与方ID
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        return self


class CreateRemoteClassCourseRequest(TeaModel):
    def __init__(
        self,
        attend_participants: List[CreateRemoteClassCourseRequestAttendParticipants] = None,
        auth_code: str = None,
        course_name: str = None,
        end_time: int = None,
        start_time: int = None,
        teaching_participant: CreateRemoteClassCourseRequestTeachingParticipant = None,
    ):
        # 听课设备列表
        self.attend_participants = attend_participants
        # 免登码
        self.auth_code = auth_code
        # 课程名称
        self.course_name = course_name
        # 结束时间
        self.end_time = end_time
        # 开始时间
        self.start_time = start_time
        # 授课设备
        self.teaching_participant = teaching_participant

    def validate(self):
        if self.attend_participants:
            for k in self.attend_participants:
                if k:
                    k.validate()
        if self.teaching_participant:
            self.teaching_participant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendParticipants'] = []
        if self.attend_participants is not None:
            for k in self.attend_participants:
                result['attendParticipants'].append(k.to_map() if k else None)
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.teaching_participant is not None:
            result['teachingParticipant'] = self.teaching_participant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attend_participants = []
        if m.get('attendParticipants') is not None:
            for k in m.get('attendParticipants'):
                temp_model = CreateRemoteClassCourseRequestAttendParticipants()
                self.attend_participants.append(temp_model.from_map(k))
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('teachingParticipant') is not None:
            temp_model = CreateRemoteClassCourseRequestTeachingParticipant()
            self.teaching_participant = temp_model.from_map(m['teachingParticipant'])
        return self


class CreateRemoteClassCourseResponseBodyResult(TeaModel):
    def __init__(
        self,
        course_code: str = None,
    ):
        # 课程码
        self.course_code = course_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        return self


class CreateRemoteClassCourseResponseBody(TeaModel):
    def __init__(
        self,
        result: CreateRemoteClassCourseResponseBodyResult = None,
        success: bool = None,
    ):
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = CreateRemoteClassCourseResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateRemoteClassCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRemoteClassCourseResponseBody = None,
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
            temp_model = CreateRemoteClassCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSectionConfigHeaders(TeaModel):
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


class CreateSectionConfigRequestSectionConfigsSectionEndDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 日
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateSectionConfigRequestSectionConfigsSectionModelsSectionEndTime(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class CreateSectionConfigRequestSectionConfigsSectionModelsSectionStartTime(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class CreateSectionConfigRequestSectionConfigsSectionModels(TeaModel):
    def __init__(
        self,
        section_end_time: CreateSectionConfigRequestSectionConfigsSectionModelsSectionEndTime = None,
        section_index: int = None,
        section_name: str = None,
        section_start_time: CreateSectionConfigRequestSectionConfigsSectionModelsSectionStartTime = None,
        section_type: str = None,
    ):
        # 结束时间
        self.section_end_time = section_end_time
        # 第几节。
        self.section_index = section_index
        # 节次名称
        self.section_name = section_name
        # 开始时间
        self.section_start_time = section_start_time
        # 节次类型枚举：COURSE/REST
        self.section_type = section_type

    def validate(self):
        if self.section_end_time:
            self.section_end_time.validate()
        if self.section_start_time:
            self.section_start_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.section_end_time is not None:
            result['sectionEndTime'] = self.section_end_time.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.section_start_time is not None:
            result['sectionStartTime'] = self.section_start_time.to_map()
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sectionEndTime') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSectionModelsSectionEndTime()
            self.section_end_time = temp_model.from_map(m['sectionEndTime'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('sectionStartTime') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSectionModelsSectionStartTime()
            self.section_start_time = temp_model.from_map(m['sectionStartTime'])
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        return self


class CreateSectionConfigRequestSectionConfigsSectionStartDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 每个月的第几天。
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateSectionConfigRequestSectionConfigsSemesterEndDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 每月第几天
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateSectionConfigRequestSectionConfigsSemesterStartDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 日
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateSectionConfigRequestSectionConfigs(TeaModel):
    def __init__(
        self,
        schedule_name: str = None,
        school_year: str = None,
        section_end_date: CreateSectionConfigRequestSectionConfigsSectionEndDate = None,
        section_models: List[CreateSectionConfigRequestSectionConfigsSectionModels] = None,
        section_start_date: CreateSectionConfigRequestSectionConfigsSectionStartDate = None,
        semester: int = None,
        semester_end_date: CreateSectionConfigRequestSectionConfigsSemesterEndDate = None,
        semester_start_date: CreateSectionConfigRequestSectionConfigsSemesterStartDate = None,
    ):
        # 课表名称
        self.schedule_name = schedule_name
        # 学年
        self.school_year = school_year
        # 结束时间
        self.section_end_date = section_end_date
        # 节次模型
        self.section_models = section_models
        # 开始时间（精确到日）
        self.section_start_date = section_start_date
        # 学期
        self.semester = semester
        # 学期结束时间
        self.semester_end_date = semester_end_date
        # 学期开始时间
        self.semester_start_date = semester_start_date

    def validate(self):
        if self.section_end_date:
            self.section_end_date.validate()
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()
        if self.section_start_date:
            self.section_start_date.validate()
        if self.semester_end_date:
            self.semester_end_date.validate()
        if self.semester_start_date:
            self.semester_start_date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_name is not None:
            result['scheduleName'] = self.schedule_name
        if self.school_year is not None:
            result['schoolYear'] = self.school_year
        if self.section_end_date is not None:
            result['sectionEndDate'] = self.section_end_date.to_map()
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        if self.section_start_date is not None:
            result['sectionStartDate'] = self.section_start_date.to_map()
        if self.semester is not None:
            result['semester'] = self.semester
        if self.semester_end_date is not None:
            result['semesterEndDate'] = self.semester_end_date.to_map()
        if self.semester_start_date is not None:
            result['semesterStartDate'] = self.semester_start_date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheduleName') is not None:
            self.schedule_name = m.get('scheduleName')
        if m.get('schoolYear') is not None:
            self.school_year = m.get('schoolYear')
        if m.get('sectionEndDate') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSectionEndDate()
            self.section_end_date = temp_model.from_map(m['sectionEndDate'])
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = CreateSectionConfigRequestSectionConfigsSectionModels()
                self.section_models.append(temp_model.from_map(k))
        if m.get('sectionStartDate') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSectionStartDate()
            self.section_start_date = temp_model.from_map(m['sectionStartDate'])
        if m.get('semester') is not None:
            self.semester = m.get('semester')
        if m.get('semesterEndDate') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSemesterEndDate()
            self.semester_end_date = temp_model.from_map(m['semesterEndDate'])
        if m.get('semesterStartDate') is not None:
            temp_model = CreateSectionConfigRequestSectionConfigsSemesterStartDate()
            self.semester_start_date = temp_model.from_map(m['semesterStartDate'])
        return self


class CreateSectionConfigRequest(TeaModel):
    def __init__(
        self,
        ext: str = None,
        section_configs: List[CreateSectionConfigRequestSectionConfigs] = None,
        op_user_id: str = None,
    ):
        # 扩展参数
        self.ext = ext
        # 课表模板信息
        self.section_configs = section_configs
        # 操作人的userid。
        self.op_user_id = op_user_id

    def validate(self):
        if self.section_configs:
            for k in self.section_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext
        result['sectionConfigs'] = []
        if self.section_configs is not None:
            for k in self.section_configs:
                result['sectionConfigs'].append(k.to_map() if k else None)
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        self.section_configs = []
        if m.get('sectionConfigs') is not None:
            for k in m.get('sectionConfigs'):
                temp_model = CreateSectionConfigRequestSectionConfigs()
                self.section_configs.append(temp_model.from_map(k))
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class CreateSectionConfigResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 初始化是否成功。
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


class CreateSectionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSectionConfigResponseBody = None,
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
            temp_model = CreateSectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenHeaders(TeaModel):
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


class CreateTokenRequest(TeaModel):
    def __init__(
        self,
        sn: str = None,
        type: str = None,
    ):
        self.sn = sn
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sn is not None:
            result['sn'] = self.sn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
        ext_info: str = None,
        security_token: str = None,
        status: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.ext_info = ext_info
        self.security_token = security_token
        # Id of the request
        self.status = status

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
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTokenResponseBody = None,
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUniversityCourseGroupHeaders(TeaModel):
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


class CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月的第几天
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月的第几天
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class CreateUniversityCourseGroupRequestCourserGroupItemModels(TeaModel):
    def __init__(
        self,
        class_period_type: int = None,
        classroom_id: int = None,
        course_type: int = None,
        courser_group_item_end_date: CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate = None,
        courser_group_item_start_date: CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate = None,
        day_of_week: int = None,
        section_index: List[int] = None,
    ):
        # 上课周期
        self.class_period_type = class_period_type
        # 教室id
        self.classroom_id = classroom_id
        # 课程类型
        self.course_type = course_type
        # 课程组详细结束时间
        self.courser_group_item_end_date = courser_group_item_end_date
        # 课程组详细开始时间
        self.courser_group_item_start_date = courser_group_item_start_date
        # 一周的第几天
        self.day_of_week = day_of_week
        # 课节
        self.section_index = section_index

    def validate(self):
        if self.courser_group_item_end_date:
            self.courser_group_item_end_date.validate()
        if self.courser_group_item_start_date:
            self.courser_group_item_start_date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_period_type is not None:
            result['classPeriodType'] = self.class_period_type
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.course_type is not None:
            result['courseType'] = self.course_type
        if self.courser_group_item_end_date is not None:
            result['courserGroupItemEndDate'] = self.courser_group_item_end_date.to_map()
        if self.courser_group_item_start_date is not None:
            result['courserGroupItemStartDate'] = self.courser_group_item_start_date.to_map()
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classPeriodType') is not None:
            self.class_period_type = m.get('classPeriodType')
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('courseType') is not None:
            self.course_type = m.get('courseType')
        if m.get('courserGroupItemEndDate') is not None:
            temp_model = CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate()
            self.courser_group_item_end_date = temp_model.from_map(m['courserGroupItemEndDate'])
        if m.get('courserGroupItemStartDate') is not None:
            temp_model = CreateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate()
            self.courser_group_item_start_date = temp_model.from_map(m['courserGroupItemStartDate'])
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        return self


class CreateUniversityCourseGroupRequestTeacherInfos(TeaModel):
    def __init__(
        self,
        participant_role: str = None,
        user_id: str = None,
    ):
        # 角色类型
        self.participant_role = participant_role
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.participant_role is not None:
            result['participantRole'] = self.participant_role
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('participantRole') is not None:
            self.participant_role = m.get('participantRole')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_introduce: str = None,
        course_group_name: str = None,
        courser_group_item_models: List[CreateUniversityCourseGroupRequestCourserGroupItemModels] = None,
        ext: str = None,
        isv_course_group_code: str = None,
        period_code: str = None,
        school_year: str = None,
        semester: int = None,
        subject_name: str = None,
        teacher_infos: List[CreateUniversityCourseGroupRequestTeacherInfos] = None,
        op_user_id: str = None,
    ):
        # 课程组介绍
        self.course_group_introduce = course_group_introduce
        # 课程组名称
        self.course_group_name = course_group_name
        # 课程详细
        self.courser_group_item_models = courser_group_item_models
        # 扩展参数
        self.ext = ext
        # 合作方课程组code
        self.isv_course_group_code = isv_course_group_code
        # 学段code
        self.period_code = period_code
        # 学年
        self.school_year = school_year
        # 学期
        self.semester = semester
        # 学科
        self.subject_name = subject_name
        # 教师信息
        self.teacher_infos = teacher_infos
        # 操作人
        self.op_user_id = op_user_id

    def validate(self):
        if self.courser_group_item_models:
            for k in self.courser_group_item_models:
                if k:
                    k.validate()
        if self.teacher_infos:
            for k in self.teacher_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_introduce is not None:
            result['courseGroupIntroduce'] = self.course_group_introduce
        if self.course_group_name is not None:
            result['courseGroupName'] = self.course_group_name
        result['courserGroupItemModels'] = []
        if self.courser_group_item_models is not None:
            for k in self.courser_group_item_models:
                result['courserGroupItemModels'].append(k.to_map() if k else None)
        if self.ext is not None:
            result['ext'] = self.ext
        if self.isv_course_group_code is not None:
            result['isvCourseGroupCode'] = self.isv_course_group_code
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        if self.school_year is not None:
            result['schoolYear'] = self.school_year
        if self.semester is not None:
            result['semester'] = self.semester
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        result['teacherInfos'] = []
        if self.teacher_infos is not None:
            for k in self.teacher_infos:
                result['teacherInfos'].append(k.to_map() if k else None)
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupIntroduce') is not None:
            self.course_group_introduce = m.get('courseGroupIntroduce')
        if m.get('courseGroupName') is not None:
            self.course_group_name = m.get('courseGroupName')
        self.courser_group_item_models = []
        if m.get('courserGroupItemModels') is not None:
            for k in m.get('courserGroupItemModels'):
                temp_model = CreateUniversityCourseGroupRequestCourserGroupItemModels()
                self.courser_group_item_models.append(temp_model.from_map(k))
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('isvCourseGroupCode') is not None:
            self.isv_course_group_code = m.get('isvCourseGroupCode')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        if m.get('schoolYear') is not None:
            self.school_year = m.get('schoolYear')
        if m.get('semester') is not None:
            self.semester = m.get('semester')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        self.teacher_infos = []
        if m.get('teacherInfos') is not None:
            for k in m.get('teacherInfos'):
                temp_model = CreateUniversityCourseGroupRequestTeacherInfos()
                self.teacher_infos.append(temp_model.from_map(k))
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class CreateUniversityCourseGroupResponseBodyCourseGroupInfo(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
    ):
        # 课程组编码
        self.course_group_code = course_group_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        return self


class CreateUniversityCourseGroupResponseBody(TeaModel):
    def __init__(
        self,
        course_group_info: CreateUniversityCourseGroupResponseBodyCourseGroupInfo = None,
    ):
        # 课程组信息
        self.course_group_info = course_group_info

    def validate(self):
        if self.course_group_info:
            self.course_group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_info is not None:
            result['courseGroupInfo'] = self.course_group_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupInfo') is not None:
            temp_model = CreateUniversityCourseGroupResponseBodyCourseGroupInfo()
            self.course_group_info = temp_model.from_map(m['courseGroupInfo'])
        return self


class CreateUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUniversityCourseGroupResponseBody = None,
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
            temp_model = CreateUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUniversityStudentHeaders(TeaModel):
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


class CreateUniversityStudentRequest(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        gender: str = None,
        identity_number: str = None,
        mobile: str = None,
        name: str = None,
        student_number: str = None,
        op_user_id: str = None,
    ):
        # 班级id
        self.class_id = class_id
        # 性别
        self.gender = gender
        # 身份证号
        self.identity_number = identity_number
        # 电话
        self.mobile = mobile
        # 名字
        self.name = name
        # 学号
        self.student_number = student_number
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.gender is not None:
            result['gender'] = self.gender
        if self.identity_number is not None:
            result['identityNumber'] = self.identity_number
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.student_number is not None:
            result['studentNumber'] = self.student_number
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('identityNumber') is not None:
            self.identity_number = m.get('identityNumber')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('studentNumber') is not None:
            self.student_number = m.get('studentNumber')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class CreateUniversityStudentResponseBody(TeaModel):
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


class CreateUniversityStudentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUniversityStudentResponseBody = None,
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
            temp_model = CreateUniversityStudentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUniversityTeacherHeaders(TeaModel):
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


class CreateUniversityTeacherRequest(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        op_user_id: str = None,
        role: str = None,
        teacher_user_id: str = None,
    ):
        # 班级ID
        self.class_id = class_id
        # 操作人用户ID
        self.op_user_id = op_user_id
        # 角色
        self.role = role
        # 教师用户ID
        self.teacher_user_id = teacher_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.role is not None:
            result['role'] = self.role
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        return self


class CreateUniversityTeacherResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 返回结果
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


class CreateUniversityTeacherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUniversityTeacherResponseBody = None,
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
            temp_model = CreateUniversityTeacherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeptHeaders(TeaModel):
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


class DeleteDeptRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
    ):
        # 钉钉企业管理员员工ID
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class DeleteDeptResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class DeleteDeptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeptResponseBody = None,
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
            temp_model = DeleteDeptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceOrgHeaders(TeaModel):
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


class DeleteDeviceOrgRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        device_code: str = None,
    ):
        self.auth_code = auth_code
        self.device_code = device_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.device_code is not None:
            result['deviceCode'] = self.device_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('deviceCode') is not None:
            self.device_code = m.get('deviceCode')
        return self


class DeleteDeviceOrgResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # Id of the request
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


class DeleteDeviceOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceOrgResponseBody = None,
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
            temp_model = DeleteDeviceOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGuardianHeaders(TeaModel):
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


class DeleteGuardianRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
        stu_id: str = None,
    ):
        # 钉钉企业管理员员工ID
        self.operator = operator
        # 学生ID
        self.stu_id = stu_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        if self.stu_id is not None:
            result['stuId'] = self.stu_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('stuId') is not None:
            self.stu_id = m.get('stuId')
        return self


class DeleteGuardianResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class DeleteGuardianResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGuardianResponseBody = None,
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
            temp_model = DeleteGuardianResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOrgRelationHeaders(TeaModel):
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


class DeleteOrgRelationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        target_corp_id: str = None,
    ):
        self.auth_code = auth_code
        self.target_corp_id = target_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.target_corp_id is not None:
            result['targetCorpId'] = self.target_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('targetCorpId') is not None:
            self.target_corp_id = m.get('targetCorpId')
        return self


class DeleteOrgRelationResponseBody(TeaModel):
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


class DeleteOrgRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOrgRelationResponseBody = None,
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
            temp_model = DeleteOrgRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhysicalClassroomHeaders(TeaModel):
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


class DeletePhysicalClassroomRequest(TeaModel):
    def __init__(
        self,
        classroom_id: int = None,
        op_user_id: str = None,
    ):
        # 教室主键
        self.classroom_id = classroom_id
        # 操作人id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class DeletePhysicalClassroomResponseBody(TeaModel):
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


class DeletePhysicalClassroomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePhysicalClassroomResponseBody = None,
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
            temp_model = DeletePhysicalClassroomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRemoteClassCourseHeaders(TeaModel):
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


class DeleteRemoteClassCourseRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
    ):
        # 免登码
        self.auth_code = auth_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        return self


class DeleteRemoteClassCourseResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class DeleteRemoteClassCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRemoteClassCourseResponseBody = None,
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
            temp_model = DeleteRemoteClassCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStudentHeaders(TeaModel):
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


class DeleteStudentRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
    ):
        # 钉钉管理员员工ID
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class DeleteStudentResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class DeleteStudentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteStudentResponseBody = None,
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
            temp_model = DeleteStudentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTeacherHeaders(TeaModel):
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


class DeleteTeacherRequest(TeaModel):
    def __init__(
        self,
        adviser: int = None,
        operator: str = None,
    ):
        # 是否班主任；1:班主任；0:非班主任
        self.adviser = adviser
        # 钉钉企业管理员员工ID
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adviser is not None:
            result['adviser'] = self.adviser
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adviser') is not None:
            self.adviser = m.get('adviser')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class DeleteTeacherResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class DeleteTeacherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTeacherResponseBody = None,
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
            temp_model = DeleteTeacherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUniversityCourseGroupHeaders(TeaModel):
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


class DeleteUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        op_user_id: str = None,
    ):
        # 课程组编码
        self.course_group_code = course_group_code
        # 操作人
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class DeleteUniversityCourseGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 操作结果
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


class DeleteUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUniversityCourseGroupResponseBody = None,
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
            temp_model = DeleteUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUniversityStudentHeaders(TeaModel):
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


class DeleteUniversityStudentRequest(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        op_user_id: str = None,
        student_user_id: str = None,
    ):
        # 班级ID
        self.class_id = class_id
        # 操作人用户ID
        self.op_user_id = op_user_id
        # 学生用户ID
        self.student_user_id = student_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.student_user_id is not None:
            result['studentUserId'] = self.student_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('studentUserId') is not None:
            self.student_user_id = m.get('studentUserId')
        return self


class DeleteUniversityStudentResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 返回结果
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


class DeleteUniversityStudentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUniversityStudentResponseBody = None,
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
            temp_model = DeleteUniversityStudentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUniversityTeacherHeaders(TeaModel):
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


class DeleteUniversityTeacherRequest(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        op_user_id: str = None,
        role: str = None,
        teacher_user_id: str = None,
    ):
        # 班级id
        self.class_id = class_id
        # opUserId
        self.op_user_id = op_user_id
        # 角色
        self.role = role
        # 教师用户ID
        self.teacher_user_id = teacher_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.role is not None:
            result['role'] = self.role
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        return self


class DeleteUniversityTeacherResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 返回结果
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


class DeleteUniversityTeacherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUniversityTeacherResponseBody = None,
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
            temp_model = DeleteUniversityTeacherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceHeartbeatHeaders(TeaModel):
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


class DeviceHeartbeatRequest(TeaModel):
    def __init__(
        self,
        sn: str = None,
    ):
        # 设备序列号
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class DeviceHeartbeatResponseBody(TeaModel):
    def __init__(
        self,
        command: int = None,
    ):
        # 指令
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        return self


class DeviceHeartbeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeviceHeartbeatResponseBody = None,
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
            temp_model = DeviceHeartbeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EduTeacherListHeaders(TeaModel):
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


class EduTeacherListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 页码
        self.page_number = page_number
        # 分页大小
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


class EduTeacherListResponseBodyResultTeacherDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
        union_id: str = None,
        user_id: str = None,
    ):
        # 用户名称
        self.name = name
        # 角色
        self.role = role
        # PiiiPyQqBxxx
        self.union_id = union_id
        # 用户ID
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
        if self.role is not None:
            result['role'] = self.role
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class EduTeacherListResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        teacher_details: List[EduTeacherListResponseBodyResultTeacherDetails] = None,
    ):
        # 是否还有下一页
        self.has_more = has_more
        # 教师信息
        self.teacher_details = teacher_details

    def validate(self):
        if self.teacher_details:
            for k in self.teacher_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        result['teacherDetails'] = []
        if self.teacher_details is not None:
            for k in self.teacher_details:
                result['teacherDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.teacher_details = []
        if m.get('teacherDetails') is not None:
            for k in m.get('teacherDetails'):
                temp_model = EduTeacherListResponseBodyResultTeacherDetails()
                self.teacher_details.append(temp_model.from_map(k))
        return self


class EduTeacherListResponseBody(TeaModel):
    def __init__(
        self,
        result: EduTeacherListResponseBodyResult = None,
    ):
        # 返回结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = EduTeacherListResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class EduTeacherListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EduTeacherListResponseBody = None,
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
            temp_model = EduTeacherListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EndCourseHeaders(TeaModel):
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


class EndCourseRequestLivePlayInfoList(TeaModel):
    def __init__(
        self,
        live_input_url: str = None,
        live_output_flv_url: str = None,
        live_output_hls_url: str = None,
        live_type: int = None,
        replay_url: str = None,
    ):
        # 直播推流地址
        self.live_input_url = live_input_url
        # Flv直播拉回地址
        self.live_output_flv_url = live_output_flv_url
        # Hls直播拉流地址
        self.live_output_hls_url = live_output_hls_url
        # 直播流类型
        self.live_type = live_type
        # 回放视频地址
        self.replay_url = replay_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_input_url is not None:
            result['liveInputUrl'] = self.live_input_url
        if self.live_output_flv_url is not None:
            result['liveOutputFlvUrl'] = self.live_output_flv_url
        if self.live_output_hls_url is not None:
            result['liveOutputHlsUrl'] = self.live_output_hls_url
        if self.live_type is not None:
            result['liveType'] = self.live_type
        if self.replay_url is not None:
            result['replayUrl'] = self.replay_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveInputUrl') is not None:
            self.live_input_url = m.get('liveInputUrl')
        if m.get('liveOutputFlvUrl') is not None:
            self.live_output_flv_url = m.get('liveOutputFlvUrl')
        if m.get('liveOutputHlsUrl') is not None:
            self.live_output_hls_url = m.get('liveOutputHlsUrl')
        if m.get('liveType') is not None:
            self.live_type = m.get('liveType')
        if m.get('replayUrl') is not None:
            self.replay_url = m.get('replayUrl')
        return self


class EndCourseRequest(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        ext: str = None,
        isv_code: str = None,
        live_play_info_list: List[EndCourseRequestLivePlayInfoList] = None,
        op_user_id: str = None,
    ):
        # 课程编码
        self.course_code = course_code
        # 拓展字段
        self.ext = ext
        # isv编码
        self.isv_code = isv_code
        # 直播流信息
        self.live_play_info_list = live_play_info_list
        # 用户id
        self.op_user_id = op_user_id

    def validate(self):
        if self.live_play_info_list:
            for k in self.live_play_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.ext is not None:
            result['ext'] = self.ext
        if self.isv_code is not None:
            result['isvCode'] = self.isv_code
        result['livePlayInfoList'] = []
        if self.live_play_info_list is not None:
            for k in self.live_play_info_list:
                result['livePlayInfoList'].append(k.to_map() if k else None)
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('isvCode') is not None:
            self.isv_code = m.get('isvCode')
        self.live_play_info_list = []
        if m.get('livePlayInfoList') is not None:
            for k in m.get('livePlayInfoList'):
                temp_model = EndCourseRequestLivePlayInfoList()
                self.live_play_info_list.append(temp_model.from_map(k))
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class EndCourseResponseBodyUniversityCourseCommonResponse(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        success: bool = None,
    ):
        # 课程编码
        self.course_code = course_code
        # 调用是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class EndCourseResponseBody(TeaModel):
    def __init__(
        self,
        university_course_common_response: EndCourseResponseBodyUniversityCourseCommonResponse = None,
    ):
        self.university_course_common_response = university_course_common_response

    def validate(self):
        if self.university_course_common_response:
            self.university_course_common_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_course_common_response is not None:
            result['universityCourseCommonResponse'] = self.university_course_common_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universityCourseCommonResponse') is not None:
            temp_model = EndCourseResponseBodyUniversityCourseCommonResponse()
            self.university_course_common_response = temp_model.from_map(m['universityCourseCommonResponse'])
        return self


class EndCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EndCourseResponseBody = None,
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
            temp_model = EndCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultChildHeaders(TeaModel):
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


class GetDefaultChildResponseBodyBindStudents(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        corp_id: str = None,
        period: str = None,
        staff_id: str = None,
    ):
        self.class_id = class_id
        self.corp_id = corp_id
        self.period = period
        self.staff_id = staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.period is not None:
            result['period'] = self.period
        if self.staff_id is not None:
            result['staffId'] = self.staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')
        return self


class GetDefaultChildResponseBody(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        bind_students: List[GetDefaultChildResponseBodyBindStudents] = None,
        grade: int = None,
        name: str = None,
        nick: str = None,
        period: str = None,
        union_id: str = None,
    ):
        self.avatar = avatar
        self.bind_students = bind_students
        self.grade = grade
        self.name = name
        self.nick = nick
        self.period = period
        self.union_id = union_id

    def validate(self):
        if self.bind_students:
            for k in self.bind_students:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        result['bindStudents'] = []
        if self.bind_students is not None:
            for k in self.bind_students:
                result['bindStudents'].append(k.to_map() if k else None)
        if self.grade is not None:
            result['grade'] = self.grade
        if self.name is not None:
            result['name'] = self.name
        if self.nick is not None:
            result['nick'] = self.nick
        if self.period is not None:
            result['period'] = self.period
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        self.bind_students = []
        if m.get('bindStudents') is not None:
            for k in m.get('bindStudents'):
                temp_model = GetDefaultChildResponseBodyBindStudents()
                self.bind_students.append(temp_model.from_map(k))
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nick') is not None:
            self.nick = m.get('nick')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetDefaultChildResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDefaultChildResponseBody = None,
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
            temp_model = GetDefaultChildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenCourseDetailHeaders(TeaModel):
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


class GetOpenCourseDetailResponseBodyPushModel(TeaModel):
    def __init__(
        self,
        push_org_name_list: List[str] = None,
        push_role_name_list: List[str] = None,
    ):
        # 参与学校的名称列表
        self.push_org_name_list = push_org_name_list
        # 参与角色的名称列表
        self.push_role_name_list = push_role_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_org_name_list is not None:
            result['pushOrgNameList'] = self.push_org_name_list
        if self.push_role_name_list is not None:
            result['pushRoleNameList'] = self.push_role_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pushOrgNameList') is not None:
            self.push_org_name_list = m.get('pushOrgNameList')
        if m.get('pushRoleNameList') is not None:
            self.push_role_name_list = m.get('pushRoleNameList')
        return self


class GetOpenCourseDetailResponseBody(TeaModel):
    def __init__(
        self,
        course_id: str = None,
        course_type: int = None,
        cover_url: str = None,
        introduction: str = None,
        push_model: GetOpenCourseDetailResponseBodyPushModel = None,
        start_time: int = None,
        teacher_id: str = None,
        teacher_name: str = None,
        title: str = None,
    ):
        # 课程id
        self.course_id = course_id
        # 课程类型: 0-直播 2-视频内容
        self.course_type = course_type
        # 封面图片地址
        self.cover_url = cover_url
        # 课程介绍
        self.introduction = introduction
        # 发布详情model
        self.push_model = push_model
        # 课程开始时间
        self.start_time = start_time
        # 老师的userId
        self.teacher_id = teacher_id
        # 老师名称
        self.teacher_name = teacher_name
        # 课程标题
        self.title = title

    def validate(self):
        if self.push_model:
            self.push_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_id is not None:
            result['courseId'] = self.course_id
        if self.course_type is not None:
            result['courseType'] = self.course_type
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.introduction is not None:
            result['introduction'] = self.introduction
        if self.push_model is not None:
            result['pushModel'] = self.push_model.to_map()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.teacher_id is not None:
            result['teacherId'] = self.teacher_id
        if self.teacher_name is not None:
            result['teacherName'] = self.teacher_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseId') is not None:
            self.course_id = m.get('courseId')
        if m.get('courseType') is not None:
            self.course_type = m.get('courseType')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')
        if m.get('pushModel') is not None:
            temp_model = GetOpenCourseDetailResponseBodyPushModel()
            self.push_model = temp_model.from_map(m['pushModel'])
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('teacherId') is not None:
            self.teacher_id = m.get('teacherId')
        if m.get('teacherName') is not None:
            self.teacher_name = m.get('teacherName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetOpenCourseDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpenCourseDetailResponseBody = None,
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
            temp_model = GetOpenCourseDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenCoursesHeaders(TeaModel):
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


class GetOpenCoursesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 分页起始, 起始值为0
        self.page_number = page_number
        # 分页大小
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


class GetOpenCoursesResponseBodyCourseList(TeaModel):
    def __init__(
        self,
        course_id: str = None,
        cover_url: str = None,
        feed_type: int = None,
        jump_url: str = None,
        start_time: int = None,
        teacher_id: str = None,
        teacher_name: str = None,
        title: str = None,
    ):
        # 课程id
        self.course_id = course_id
        # 封面图片地址
        self.cover_url = cover_url
        # 课程类型: 0-直播 2-视频内容
        self.feed_type = feed_type
        # 课程观看地址
        self.jump_url = jump_url
        # 课程开始时间
        self.start_time = start_time
        # 老师的userId
        self.teacher_id = teacher_id
        # 老师名称
        self.teacher_name = teacher_name
        # 课程标题
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_id is not None:
            result['courseId'] = self.course_id
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.feed_type is not None:
            result['feedType'] = self.feed_type
        if self.jump_url is not None:
            result['jumpUrl'] = self.jump_url
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.teacher_id is not None:
            result['teacherId'] = self.teacher_id
        if self.teacher_name is not None:
            result['teacherName'] = self.teacher_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseId') is not None:
            self.course_id = m.get('courseId')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('feedType') is not None:
            self.feed_type = m.get('feedType')
        if m.get('jumpUrl') is not None:
            self.jump_url = m.get('jumpUrl')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('teacherId') is not None:
            self.teacher_id = m.get('teacherId')
        if m.get('teacherName') is not None:
            self.teacher_name = m.get('teacherName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetOpenCoursesResponseBody(TeaModel):
    def __init__(
        self,
        course_list: List[GetOpenCoursesResponseBodyCourseList] = None,
        total_count: int = None,
    ):
        self.course_list = course_list
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.course_list:
            for k in self.course_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['courseList'] = []
        if self.course_list is not None:
            for k in self.course_list:
                result['courseList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.course_list = []
        if m.get('courseList') is not None:
            for k in m.get('courseList'):
                temp_model = GetOpenCoursesResponseBodyCourseList()
                self.course_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetOpenCoursesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpenCoursesResponseBody = None,
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
            temp_model = GetOpenCoursesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRemoteClassCourseHeaders(TeaModel):
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


class GetRemoteClassCourseRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
    ):
        # 操作者用户ID
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class GetRemoteClassCourseResponseBodyResultAttendParticipants(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        org_name: str = None,
        participant_id: str = None,
        participant_name: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 组织名称
        self.org_name = org_name
        # 参与方ID
        self.participant_id = participant_id
        # 参与方名称
        self.participant_name = participant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        if self.participant_name is not None:
            result['participantName'] = self.participant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        if m.get('participantName') is not None:
            self.participant_name = m.get('participantName')
        return self


class GetRemoteClassCourseResponseBodyResultRecordInfos(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        stop_time: str = None,
        url: str = None,
    ):
        # 录制开始时间（UTC/GMT格式）
        self.start_time = start_time
        # 录制结束时间（UTC/GMT格式）
        self.stop_time = stop_time
        # 录制文件地址（文件有效期7天）
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetRemoteClassCourseResponseBodyResultTeachingParticipant(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        org_name: str = None,
        participant_id: str = None,
        participant_name: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 组织名称
        self.org_name = org_name
        # 参与方ID
        self.participant_id = participant_id
        # 参与方名称
        self.participant_name = participant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        if self.participant_name is not None:
            result['participantName'] = self.participant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        if m.get('participantName') is not None:
            self.participant_name = m.get('participantName')
        return self


class GetRemoteClassCourseResponseBodyResult(TeaModel):
    def __init__(
        self,
        attend_participants: List[GetRemoteClassCourseResponseBodyResultAttendParticipants] = None,
        can_edit: bool = None,
        course_code: str = None,
        course_name: str = None,
        end_time: int = None,
        live_url: str = None,
        record_infos: List[GetRemoteClassCourseResponseBodyResultRecordInfos] = None,
        room_status: int = None,
        start_time: int = None,
        status: int = None,
        teaching_participant: GetRemoteClassCourseResponseBodyResultTeachingParticipant = None,
    ):
        # 听课设备列表
        self.attend_participants = attend_participants
        # 课程是否可以编辑或删除
        self.can_edit = can_edit
        # 课程code
        self.course_code = course_code
        # 课程名称
        self.course_name = course_name
        # 结束时间
        self.end_time = end_time
        # 直播观看URL（如果有）
        self.live_url = live_url
        # 录制信息列表（如果有）。根据录制端的不同，有不同时长的延迟
        self.record_infos = record_infos
        # 课堂当前状态：0: 未进行；1: 进行中
        self.room_status = room_status
        # 开始时间
        self.start_time = start_time
        # 课程状态：0: 未开始；1: 已开始；2: 已结束
        self.status = status
        # 授课设备
        self.teaching_participant = teaching_participant

    def validate(self):
        if self.attend_participants:
            for k in self.attend_participants:
                if k:
                    k.validate()
        if self.record_infos:
            for k in self.record_infos:
                if k:
                    k.validate()
        if self.teaching_participant:
            self.teaching_participant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendParticipants'] = []
        if self.attend_participants is not None:
            for k in self.attend_participants:
                result['attendParticipants'].append(k.to_map() if k else None)
        if self.can_edit is not None:
            result['canEdit'] = self.can_edit
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.live_url is not None:
            result['liveUrl'] = self.live_url
        result['recordInfos'] = []
        if self.record_infos is not None:
            for k in self.record_infos:
                result['recordInfos'].append(k.to_map() if k else None)
        if self.room_status is not None:
            result['roomStatus'] = self.room_status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.teaching_participant is not None:
            result['teachingParticipant'] = self.teaching_participant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attend_participants = []
        if m.get('attendParticipants') is not None:
            for k in m.get('attendParticipants'):
                temp_model = GetRemoteClassCourseResponseBodyResultAttendParticipants()
                self.attend_participants.append(temp_model.from_map(k))
        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('liveUrl') is not None:
            self.live_url = m.get('liveUrl')
        self.record_infos = []
        if m.get('recordInfos') is not None:
            for k in m.get('recordInfos'):
                temp_model = GetRemoteClassCourseResponseBodyResultRecordInfos()
                self.record_infos.append(temp_model.from_map(k))
        if m.get('roomStatus') is not None:
            self.room_status = m.get('roomStatus')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('teachingParticipant') is not None:
            temp_model = GetRemoteClassCourseResponseBodyResultTeachingParticipant()
            self.teaching_participant = temp_model.from_map(m['teachingParticipant'])
        return self


class GetRemoteClassCourseResponseBody(TeaModel):
    def __init__(
        self,
        result: GetRemoteClassCourseResponseBodyResult = None,
        success: bool = None,
    ):
        self.result = result
        # 是否成功
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = GetRemoteClassCourseResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetRemoteClassCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRemoteClassCourseResponseBody = None,
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
            temp_model = GetRemoteClassCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareRoleMembersHeaders(TeaModel):
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


class GetShareRoleMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_user_id_list_in_trunk_org: List[str] = None,
    ):
        # 分支组织corpId
        self.corp_id = corp_id
        # 角色成员在主干组织中的userId列表
        self.member_user_id_list_in_trunk_org = member_user_id_list_in_trunk_org

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_user_id_list_in_trunk_org is not None:
            result['memberUserIdListInTrunkOrg'] = self.member_user_id_list_in_trunk_org
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberUserIdListInTrunkOrg') is not None:
            self.member_user_id_list_in_trunk_org = m.get('memberUserIdListInTrunkOrg')
        return self


class GetShareRoleMembersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetShareRoleMembersResponseBodyResult] = None,
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
                temp_model = GetShareRoleMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetShareRoleMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareRoleMembersResponseBody = None,
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
            temp_model = GetShareRoleMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareRolesHeaders(TeaModel):
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


class GetShareRolesResponseBodyResult(TeaModel):
    def __init__(
        self,
        share_role_code: str = None,
        share_role_name: str = None,
    ):
        # 角色code
        self.share_role_code = share_role_code
        # 角色名称
        self.share_role_name = share_role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_role_code is not None:
            result['shareRoleCode'] = self.share_role_code
        if self.share_role_name is not None:
            result['shareRoleName'] = self.share_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareRoleCode') is not None:
            self.share_role_code = m.get('shareRoleCode')
        if m.get('shareRoleName') is not None:
            self.share_role_name = m.get('shareRoleName')
        return self


class GetShareRolesResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetShareRolesResponseBodyResult] = None,
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
                temp_model = GetShareRolesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetShareRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetShareRolesResponseBody = None,
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
            temp_model = GetShareRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitCoursesOfClassHeaders(TeaModel):
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


class InitCoursesOfClassRequestCoursesDateModel(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 每个月的第几天。
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class InitCoursesOfClassRequestCoursesSectionModel(TeaModel):
    def __init__(
        self,
        section_index: int = None,
        section_name: str = None,
    ):
        # 节次序列号。
        self.section_index = section_index
        # 节次名称。
        self.section_name = section_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        return self


class InitCoursesOfClassRequestCourses(TeaModel):
    def __init__(
        self,
        course_name: str = None,
        creator_name: str = None,
        date_model: InitCoursesOfClassRequestCoursesDateModel = None,
        location: str = None,
        section_model: InitCoursesOfClassRequestCoursesSectionModel = None,
        teacher_staff_ids: List[str] = None,
    ):
        # 课程名称。
        self.course_name = course_name
        # 创建者名称。
        self.creator_name = creator_name
        # 上课时间。
        self.date_model = date_model
        # 上课地点
        self.location = location
        # 课程节次。
        self.section_model = section_model
        # 老师的staffId。
        self.teacher_staff_ids = teacher_staff_ids

    def validate(self):
        if self.date_model:
            self.date_model.validate()
        if self.section_model:
            self.section_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.date_model is not None:
            result['dateModel'] = self.date_model.to_map()
        if self.location is not None:
            result['location'] = self.location
        if self.section_model is not None:
            result['sectionModel'] = self.section_model.to_map()
        if self.teacher_staff_ids is not None:
            result['teacherStaffIds'] = self.teacher_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('dateModel') is not None:
            temp_model = InitCoursesOfClassRequestCoursesDateModel()
            self.date_model = temp_model.from_map(m['dateModel'])
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('sectionModel') is not None:
            temp_model = InitCoursesOfClassRequestCoursesSectionModel()
            self.section_model = temp_model.from_map(m['sectionModel'])
        if m.get('teacherStaffIds') is not None:
            self.teacher_staff_ids = m.get('teacherStaffIds')
        return self


class InitCoursesOfClassRequestSectionConfigEnd(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 每个月的第几天。
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class InitCoursesOfClassRequestSectionConfigSectionModelsEnd(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class InitCoursesOfClassRequestSectionConfigSectionModelsStart(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class InitCoursesOfClassRequestSectionConfigSectionModels(TeaModel):
    def __init__(
        self,
        end: InitCoursesOfClassRequestSectionConfigSectionModelsEnd = None,
        section_index: int = None,
        section_type: str = None,
        start: InitCoursesOfClassRequestSectionConfigSectionModelsStart = None,
    ):
        # 结束时间
        self.end = end
        # 第几节。
        self.section_index = section_index
        # 节次类型枚举：COURSE/REST
        self.section_type = section_type
        # 开始时间
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = InitCoursesOfClassRequestSectionConfigSectionModelsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        if m.get('start') is not None:
            temp_model = InitCoursesOfClassRequestSectionConfigSectionModelsStart()
            self.start = temp_model.from_map(m['start'])
        return self


class InitCoursesOfClassRequestSectionConfigStart(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 每个月的第几天。
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class InitCoursesOfClassRequestSectionConfig(TeaModel):
    def __init__(
        self,
        end: InitCoursesOfClassRequestSectionConfigEnd = None,
        section_models: List[InitCoursesOfClassRequestSectionConfigSectionModels] = None,
        start: InitCoursesOfClassRequestSectionConfigStart = None,
    ):
        # 课程表结束开始时间（精确到日）
        self.end = end
        # 节次模型
        self.section_models = section_models
        # 课程表开始时间（精确到日）
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = InitCoursesOfClassRequestSectionConfigEnd()
            self.end = temp_model.from_map(m['end'])
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = InitCoursesOfClassRequestSectionConfigSectionModels()
                self.section_models.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = InitCoursesOfClassRequestSectionConfigStart()
            self.start = temp_model.from_map(m['start'])
        return self


class InitCoursesOfClassRequest(TeaModel):
    def __init__(
        self,
        courses: List[InitCoursesOfClassRequestCourses] = None,
        section_config: InitCoursesOfClassRequestSectionConfig = None,
        op_user_id: str = None,
    ):
        # 课程设置。
        self.courses = courses
        # 节次设置
        self.section_config = section_config
        # 操作人的userid。
        self.op_user_id = op_user_id

    def validate(self):
        if self.courses:
            for k in self.courses:
                if k:
                    k.validate()
        if self.section_config:
            self.section_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['courses'] = []
        if self.courses is not None:
            for k in self.courses:
                result['courses'].append(k.to_map() if k else None)
        if self.section_config is not None:
            result['sectionConfig'] = self.section_config.to_map()
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.courses = []
        if m.get('courses') is not None:
            for k in m.get('courses'):
                temp_model = InitCoursesOfClassRequestCourses()
                self.courses.append(temp_model.from_map(k))
        if m.get('sectionConfig') is not None:
            temp_model = InitCoursesOfClassRequestSectionConfig()
            self.section_config = temp_model.from_map(m['sectionConfig'])
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class InitCoursesOfClassResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 初始化是否成功。
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


class InitCoursesOfClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitCoursesOfClassResponseBody = None,
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
            temp_model = InitCoursesOfClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDeviceHeaders(TeaModel):
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


class InitDeviceRequest(TeaModel):
    def __init__(
        self,
        encrypt_pub_key: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        version: str = None,
    ):
        # 公钥密文
        self.encrypt_pub_key = encrypt_pub_key
        # 签名
        self.signature = signature
        # 设备sn号
        self.sn = sn
        # 时间戳，utc时间
        self.timestamp = timestamp
        # 版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_pub_key is not None:
            result['encryptPubKey'] = self.encrypt_pub_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encryptPubKey') is not None:
            self.encrypt_pub_key = m.get('encryptPubKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class InitDeviceResponseBody(TeaModel):
    def __init__(
        self,
        success_info: str = None,
    ):
        # 成功信息
        self.success_info = success_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_info is not None:
            result['successInfo'] = self.success_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('successInfo') is not None:
            self.success_info = m.get('successInfo')
        return self


class InitDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitDeviceResponseBody = None,
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
            temp_model = InitDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertSectionConfigHeaders(TeaModel):
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


class InsertSectionConfigRequestEnd(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月中的第几天
        self.day_of_month = day_of_month
        # 月份
        self.month = month
        # 年份
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class InsertSectionConfigRequestSectionModelsEnd(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class InsertSectionConfigRequestSectionModelsStart(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class InsertSectionConfigRequestSectionModels(TeaModel):
    def __init__(
        self,
        end: InsertSectionConfigRequestSectionModelsEnd = None,
        section_index: int = None,
        section_name: str = None,
        section_type: str = None,
        start: InsertSectionConfigRequestSectionModelsStart = None,
    ):
        # 结束时间
        self.end = end
        # 节次序号
        self.section_index = section_index
        # 节次名称
        self.section_name = section_name
        # 节次类型
        self.section_type = section_type
        # 开始时间
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = InsertSectionConfigRequestSectionModelsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        if m.get('start') is not None:
            temp_model = InsertSectionConfigRequestSectionModelsStart()
            self.start = temp_model.from_map(m['start'])
        return self


class InsertSectionConfigRequestStart(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月中的第几天
        self.day_of_month = day_of_month
        # 月份
        self.month = month
        # 年份
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class InsertSectionConfigRequest(TeaModel):
    def __init__(
        self,
        end: InsertSectionConfigRequestEnd = None,
        schedule_name: str = None,
        section_models: List[InsertSectionConfigRequestSectionModels] = None,
        start: InsertSectionConfigRequestStart = None,
        op_user_id: str = None,
    ):
        # 结束日期
        self.end = end
        # 课程表名称
        self.schedule_name = schedule_name
        # 节次模型
        self.section_models = section_models
        # 开始日期
        self.start = start
        # 操作人的userid。
        self.op_user_id = op_user_id

    def validate(self):
        if self.end:
            self.end.validate()
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.schedule_name is not None:
            result['scheduleName'] = self.schedule_name
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = InsertSectionConfigRequestEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('scheduleName') is not None:
            self.schedule_name = m.get('scheduleName')
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = InsertSectionConfigRequestSectionModels()
                self.section_models.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = InsertSectionConfigRequestStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class InsertSectionConfigResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 初始化是否成功。
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


class InsertSectionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertSectionConfigResponseBody = None,
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
            temp_model = InsertSectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrderHeaders(TeaModel):
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


class ListOrderRequest(TeaModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        merchant_id: str = None,
        order_no: str = None,
        page_number: int = None,
        page_size: int = None,
        scene: int = None,
        status: int = None,
        trade_no: str = None,
        user_id: str = None,
    ):
        # 开单结束时间
        self.create_time_end = create_time_end
        # 开单开始时间，utc
        self.create_time_start = create_time_start
        # 商户id
        self.merchant_id = merchant_id
        # 订单号
        self.order_no = order_no
        # 分页下标
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 场景
        self.scene = scene
        # 状态
        self.status = status
        # 交易单号
        self.trade_no = trade_no
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        if self.trade_no is not None:
            result['tradeNo'] = self.trade_no
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')
        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tradeNo') is not None:
            self.trade_no = m.get('tradeNo')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListOrderResponseBodyList(TeaModel):
    def __init__(
        self,
        actual_amount: int = None,
        buyer_id: str = None,
        corp_id: str = None,
        create_time: int = None,
        end_time: int = None,
        order_no: str = None,
        pay_time: int = None,
        scene: int = None,
        start_time: int = None,
        status: int = None,
        trade_no: str = None,
        user_id: str = None,
    ):
        self.actual_amount = actual_amount
        self.buyer_id = buyer_id
        self.corp_id = corp_id
        self.create_time = create_time
        self.end_time = end_time
        self.order_no = order_no
        self.pay_time = pay_time
        self.scene = scene
        self.start_time = start_time
        self.status = status
        self.trade_no = trade_no
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_amount is not None:
            result['actualAmount'] = self.actual_amount
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.scene is not None:
            result['scene'] = self.scene
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.trade_no is not None:
            result['tradeNo'] = self.trade_no
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualAmount') is not None:
            self.actual_amount = m.get('actualAmount')
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tradeNo') is not None:
            self.trade_no = m.get('tradeNo')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListOrderResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListOrderResponseBodyList] = None,
        total: int = None,
    ):
        # 列表
        self.list = list
        # 总数
        self.total = total

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
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListOrderResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrderResponseBody = None,
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
            temp_model = ListOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveStudentHeaders(TeaModel):
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


class MoveStudentRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
        origin_class_id: int = None,
        target_class_id: int = None,
        user_id: str = None,
    ):
        # 管理员id
        self.operator = operator
        # 愿班级id
        self.origin_class_id = origin_class_id
        # 目标班级id
        self.target_class_id = target_class_id
        # 学生id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        if self.origin_class_id is not None:
            result['originClassId'] = self.origin_class_id
        if self.target_class_id is not None:
            result['targetClassId'] = self.target_class_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('originClassId') is not None:
            self.origin_class_id = m.get('originClassId')
        if m.get('targetClassId') is not None:
            self.target_class_id = m.get('targetClassId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class MoveStudentResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # success
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


class MoveStudentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveStudentResponseBody = None,
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
            temp_model = MoveStudentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderHeaders(TeaModel):
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


class PayOrderRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        order_no: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        user_id: str = None,
        version: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 订单号
        self.order_no = order_no
        # 签名
        self.signature = signature
        # 设备序列号
        self.sn = sn
        # utc时间戳
        self.timestamp = timestamp
        # 员工id
        self.user_id = user_id
        # 版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PayOrderResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 返回结果
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


class PayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PayOrderResponseBody = None,
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
            temp_model = PayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PollingConfirmStatusHeaders(TeaModel):
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


class PollingConfirmStatusRequest(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        ext: str = None,
        isv_code: str = None,
        op_user_id: str = None,
    ):
        # courseCode
        self.course_code = course_code
        # ext
        self.ext = ext
        # isvCode
        self.isv_code = isv_code
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.ext is not None:
            result['ext'] = self.ext
        if self.isv_code is not None:
            result['isvCode'] = self.isv_code
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('isvCode') is not None:
            self.isv_code = m.get('isvCode')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponseLivePlayInfoList(TeaModel):
    def __init__(
        self,
        live_input_url: str = None,
        live_output_url: str = None,
        live_type: int = None,
        replay_url: str = None,
    ):
        # 推流地址
        self.live_input_url = live_input_url
        # 直播拉流地址
        self.live_output_url = live_output_url
        # 视频流类型
        self.live_type = live_type
        # 视频回放地址
        self.replay_url = replay_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_input_url is not None:
            result['liveInputUrl'] = self.live_input_url
        if self.live_output_url is not None:
            result['liveOutputUrl'] = self.live_output_url
        if self.live_type is not None:
            result['liveType'] = self.live_type
        if self.replay_url is not None:
            result['replayUrl'] = self.replay_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveInputUrl') is not None:
            self.live_input_url = m.get('liveInputUrl')
        if m.get('liveOutputUrl') is not None:
            self.live_output_url = m.get('liveOutputUrl')
        if m.get('liveType') is not None:
            self.live_type = m.get('liveType')
        if m.get('replayUrl') is not None:
            self.replay_url = m.get('replayUrl')
        return self


class PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponse(TeaModel):
    def __init__(
        self,
        confirm_status: bool = None,
        course_code: str = None,
        live_play_info_list: List[PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponseLivePlayInfoList] = None,
    ):
        # 确认状态
        self.confirm_status = confirm_status
        # 课程编码
        self.course_code = course_code
        self.live_play_info_list = live_play_info_list

    def validate(self):
        if self.live_play_info_list:
            for k in self.live_play_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm_status is not None:
            result['confirmStatus'] = self.confirm_status
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        result['livePlayInfoList'] = []
        if self.live_play_info_list is not None:
            for k in self.live_play_info_list:
                result['livePlayInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confirmStatus') is not None:
            self.confirm_status = m.get('confirmStatus')
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        self.live_play_info_list = []
        if m.get('livePlayInfoList') is not None:
            for k in m.get('livePlayInfoList'):
                temp_model = PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponseLivePlayInfoList()
                self.live_play_info_list.append(temp_model.from_map(k))
        return self


class PollingConfirmStatusResponseBody(TeaModel):
    def __init__(
        self,
        university_polling_course_status_response: PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponse = None,
    ):
        self.university_polling_course_status_response = university_polling_course_status_response

    def validate(self):
        if self.university_polling_course_status_response:
            self.university_polling_course_status_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_polling_course_status_response is not None:
            result['universityPollingCourseStatusResponse'] = self.university_polling_course_status_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universityPollingCourseStatusResponse') is not None:
            temp_model = PollingConfirmStatusResponseBodyUniversityPollingCourseStatusResponse()
            self.university_polling_course_status_response = temp_model.from_map(m['universityPollingCourseStatusResponse'])
        return self


class PollingConfirmStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PollingConfirmStatusResponseBody = None,
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
            temp_model = PollingConfirmStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllSubjectsFromClassScheduleHeaders(TeaModel):
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


class QueryAllSubjectsFromClassScheduleRequest(TeaModel):
    def __init__(
        self,
        class_ids: List[int] = None,
        op_user_id: str = None,
        period_code: str = None,
    ):
        # 班级ID。
        self.class_ids = class_ids
        # 操作者的userid。
        self.op_user_id = op_user_id
        # 学段编码：KINDERGARTEN：小学 PRIMARY_SCHOOL：小学 MODDLE_SCHOOL： 初中 HIGH_SCHOOL： 高中 UNIVERSITY：大学 NOT_SCHOOL：无学段
        self.period_code = period_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids is not None:
            result['classIds'] = self.class_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        return self


class QueryAllSubjectsFromClassScheduleShrinkRequest(TeaModel):
    def __init__(
        self,
        class_ids_shrink: str = None,
        op_user_id: str = None,
        period_code: str = None,
    ):
        # 班级ID。
        self.class_ids_shrink = class_ids_shrink
        # 操作者的userid。
        self.op_user_id = op_user_id
        # 学段编码：KINDERGARTEN：小学 PRIMARY_SCHOOL：小学 MODDLE_SCHOOL： 初中 HIGH_SCHOOL： 高中 UNIVERSITY：大学 NOT_SCHOOL：无学段
        self.period_code = period_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids_shrink is not None:
            result['classIds'] = self.class_ids_shrink
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids_shrink = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        return self


class QueryAllSubjectsFromClassScheduleResponseBodyResultExtTeacherList(TeaModel):
    def __init__(
        self,
        avator: str = None,
        name: str = None,
        uid: int = None,
        user_id: str = None,
    ):
        # 老师的头像url
        self.avator = avator
        # 老师名称。
        self.name = name
        # 老师的uid。
        self.uid = uid
        # 老师的userid。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avator is not None:
            result['avator'] = self.avator
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avator') is not None:
            self.avator = m.get('avator')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryAllSubjectsFromClassScheduleResponseBodyResultExt(TeaModel):
    def __init__(
        self,
        background_color: str = None,
        class_id: int = None,
        font_color: str = None,
        teacher_list: List[QueryAllSubjectsFromClassScheduleResponseBodyResultExtTeacherList] = None,
    ):
        # 学科背景颜色
        self.background_color = background_color
        # 班级id。
        self.class_id = class_id
        # 学科字体颜色
        self.font_color = font_color
        # 老师列表
        self.teacher_list = teacher_list

    def validate(self):
        if self.teacher_list:
            for k in self.teacher_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_color is not None:
            result['backgroundColor'] = self.background_color
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.font_color is not None:
            result['fontColor'] = self.font_color
        result['teacherList'] = []
        if self.teacher_list is not None:
            for k in self.teacher_list:
                result['teacherList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundColor') is not None:
            self.background_color = m.get('backgroundColor')
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('fontColor') is not None:
            self.font_color = m.get('fontColor')
        self.teacher_list = []
        if m.get('teacherList') is not None:
            for k in m.get('teacherList'):
                temp_model = QueryAllSubjectsFromClassScheduleResponseBodyResultExtTeacherList()
                self.teacher_list.append(temp_model.from_map(k))
        return self


class QueryAllSubjectsFromClassScheduleResponseBodyResult(TeaModel):
    def __init__(
        self,
        creator_org_id: int = None,
        ext: QueryAllSubjectsFromClassScheduleResponseBodyResultExt = None,
        period_code: str = None,
        subject_code: str = None,
        subject_name: str = None,
    ):
        # creatorOrgId
        self.creator_org_id = creator_org_id
        # 拓展信息
        self.ext = ext
        # 学段编码：  KINDERGARTEN：小学 PRIMARY_SCHOOL：小学 MODDLE_SCHOOL： 初中 HIGH_SCHOOL： 高中 UNIVERSITY：大学 NOT_SCHOOL：无学段
        self.period_code = period_code
        # 学科code。
        self.subject_code = subject_code
        # 学科名称。
        self.subject_name = subject_name

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_org_id is not None:
            result['creatorOrgId'] = self.creator_org_id
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorOrgId') is not None:
            self.creator_org_id = m.get('creatorOrgId')
        if m.get('ext') is not None:
            temp_model = QueryAllSubjectsFromClassScheduleResponseBodyResultExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        return self


class QueryAllSubjectsFromClassScheduleResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryAllSubjectsFromClassScheduleResponseBodyResult] = None,
    ):
        # 查询结果。
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
                temp_model = QueryAllSubjectsFromClassScheduleResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryAllSubjectsFromClassScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAllSubjectsFromClassScheduleResponseBody = None,
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
            temp_model = QueryAllSubjectsFromClassScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClassScheduleHeaders(TeaModel):
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


class QueryClassScheduleRequest(TeaModel):
    def __init__(
        self,
        section_index_list: List[int] = None,
        subscriber_ids: List[str] = None,
        end_time: int = None,
        op_user_id: str = None,
        start_time: int = None,
        subscriber_type: str = None,
    ):
        # 查询课程的节次。
        self.section_index_list = section_index_list
        # 订阅者的Id。
        self.subscriber_ids = subscriber_ids
        # 结束时间（unix时间戳）
        self.end_time = end_time
        # 操作者UserId
        self.op_user_id = op_user_id
        # 开始时间（unix时间戳）
        self.start_time = start_time
        # 订阅者类型：  DEPARTMENT：班级订阅 USER：老师订阅
        self.subscriber_type = subscriber_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.section_index_list is not None:
            result['sectionIndexList'] = self.section_index_list
        if self.subscriber_ids is not None:
            result['subscriberIds'] = self.subscriber_ids
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.subscriber_type is not None:
            result['subscriberType'] = self.subscriber_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sectionIndexList') is not None:
            self.section_index_list = m.get('sectionIndexList')
        if m.get('subscriberIds') is not None:
            self.subscriber_ids = m.get('subscriberIds')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('subscriberType') is not None:
            self.subscriber_type = m.get('subscriberType')
        return self


class QueryClassScheduleResponseBodyConfigEnd(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一个月中第几天
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryClassScheduleResponseBodyConfigSectionModelsEnd(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时。
        self.hour = hour
        # 分钟。
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class QueryClassScheduleResponseBodyConfigSectionModelsStart(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时。
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class QueryClassScheduleResponseBodyConfigSectionModels(TeaModel):
    def __init__(
        self,
        end: QueryClassScheduleResponseBodyConfigSectionModelsEnd = None,
        section_index: int = None,
        section_name: str = None,
        section_type: str = None,
        start: QueryClassScheduleResponseBodyConfigSectionModelsStart = None,
    ):
        # 结束时间（时分级别）
        self.end = end
        # 节次序列。
        self.section_index = section_index
        # 节次名称。
        self.section_name = section_name
        # 节次类型：  COURSE：上课节次 REST：休息节次
        self.section_type = section_type
        # 开始时间（时分级别）。
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = QueryClassScheduleResponseBodyConfigSectionModelsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        if m.get('start') is not None:
            temp_model = QueryClassScheduleResponseBodyConfigSectionModelsStart()
            self.start = temp_model.from_map(m['start'])
        return self


class QueryClassScheduleResponseBodyConfigStart(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一个月中第几天
        self.day_of_month = day_of_month
        # 月份。
        self.month = month
        # 年份。
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryClassScheduleResponseBodyConfig(TeaModel):
    def __init__(
        self,
        end: QueryClassScheduleResponseBodyConfigEnd = None,
        section_models: List[QueryClassScheduleResponseBodyConfigSectionModels] = None,
        start: QueryClassScheduleResponseBodyConfigStart = None,
    ):
        # 开始时间（到日）。
        self.end = end
        # 节次模型。
        self.section_models = section_models
        # 开始时间（到日）。
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = QueryClassScheduleResponseBodyConfigEnd()
            self.end = temp_model.from_map(m['end'])
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = QueryClassScheduleResponseBodyConfigSectionModels()
                self.section_models.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = QueryClassScheduleResponseBodyConfigStart()
            self.start = temp_model.from_map(m['start'])
        return self


class QueryClassScheduleResponseBodyCourseDTOSClassrooms(TeaModel):
    def __init__(
        self,
        interact_info: str = None,
        target_id: str = None,
    ):
        # 交互信息
        self.interact_info = interact_info
        # 课堂唯一标识
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.interact_info is not None:
            result['interactInfo'] = self.interact_info
        if self.target_id is not None:
            result['targetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interactInfo') is not None:
            self.interact_info = m.get('interactInfo')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        return self


class QueryClassScheduleResponseBodyCourseDTOSEduUserModels(TeaModel):
    def __init__(
        self,
        name: str = None,
        uid: int = None,
        user_id: str = None,
    ):
        self.name = name
        # 用户uid
        self.uid = uid
        # 用户userid
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
        if self.uid is not None:
            result['uid'] = self.uid
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryClassScheduleResponseBodyCourseDTOS(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        classrooms: List[QueryClassScheduleResponseBodyCourseDTOSClassrooms] = None,
        code: str = None,
        course_group_code: str = None,
        cover_url: str = None,
        creator_corp_id: str = None,
        creator_user_id: str = None,
        creator_user_name: str = None,
        edu_user_models: List[QueryClassScheduleResponseBodyCourseDTOSEduUserModels] = None,
        end_time: int = None,
        ext_info: str = None,
        introduce: str = None,
        name: str = None,
        section_index: int = None,
        section_name: str = None,
        start_time: int = None,
        status: int = None,
        subject_code: str = None,
        teacher_corp_id: str = None,
        teacher_user_id: str = None,
        teacher_user_name: str = None,
    ):
        # 课程所在班级id
        self.class_id = class_id
        # 课堂列表
        self.classrooms = classrooms
        # 课程编码
        self.code = code
        # 课程组编码
        self.course_group_code = course_group_code
        # 课程封面地址
        self.cover_url = cover_url
        # 创建者组织id
        self.creator_corp_id = creator_corp_id
        # 创建者UserId
        self.creator_user_id = creator_user_id
        # 创建者UserName
        self.creator_user_name = creator_user_name
        # 课程参与人列表
        self.edu_user_models = edu_user_models
        # 结束时间
        self.end_time = end_time
        # 课程扩展信息
        self.ext_info = ext_info
        # 课程介绍
        self.introduce = introduce
        # 课程名称
        self.name = name
        # 课程所在节次序列号
        self.section_index = section_index
        # 课程名称
        self.section_name = section_name
        # 开始时间
        self.start_time = start_time
        # 课程状态
        self.status = status
        # 学科编码
        self.subject_code = subject_code
        # 老师CorpId
        self.teacher_corp_id = teacher_corp_id
        # 老师UserId
        self.teacher_user_id = teacher_user_id
        # 老师UserName
        self.teacher_user_name = teacher_user_name

    def validate(self):
        if self.classrooms:
            for k in self.classrooms:
                if k:
                    k.validate()
        if self.edu_user_models:
            for k in self.edu_user_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        result['classrooms'] = []
        if self.classrooms is not None:
            for k in self.classrooms:
                result['classrooms'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.creator_corp_id is not None:
            result['creatorCorpId'] = self.creator_corp_id
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.creator_user_name is not None:
            result['creatorUserName'] = self.creator_user_name
        result['eduUserModels'] = []
        if self.edu_user_models is not None:
            for k in self.edu_user_models:
                result['eduUserModels'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.teacher_corp_id is not None:
            result['teacherCorpId'] = self.teacher_corp_id
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        if self.teacher_user_name is not None:
            result['teacherUserName'] = self.teacher_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        self.classrooms = []
        if m.get('classrooms') is not None:
            for k in m.get('classrooms'):
                temp_model = QueryClassScheduleResponseBodyCourseDTOSClassrooms()
                self.classrooms.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('creatorCorpId') is not None:
            self.creator_corp_id = m.get('creatorCorpId')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('creatorUserName') is not None:
            self.creator_user_name = m.get('creatorUserName')
        self.edu_user_models = []
        if m.get('eduUserModels') is not None:
            for k in m.get('eduUserModels'):
                temp_model = QueryClassScheduleResponseBodyCourseDTOSEduUserModels()
                self.edu_user_models.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('teacherCorpId') is not None:
            self.teacher_corp_id = m.get('teacherCorpId')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        if m.get('teacherUserName') is not None:
            self.teacher_user_name = m.get('teacherUserName')
        return self


class QueryClassScheduleResponseBody(TeaModel):
    def __init__(
        self,
        config: QueryClassScheduleResponseBodyConfig = None,
        course_dtos: List[QueryClassScheduleResponseBodyCourseDTOS] = None,
    ):
        # 课表时间节次配置。
        self.config = config
        # 课程列表
        self.course_dtos = course_dtos

    def validate(self):
        if self.config:
            self.config.validate()
        if self.course_dtos:
            for k in self.course_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        result['courseDTOS'] = []
        if self.course_dtos is not None:
            for k in self.course_dtos:
                result['courseDTOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = QueryClassScheduleResponseBodyConfig()
            self.config = temp_model.from_map(m['config'])
        self.course_dtos = []
        if m.get('courseDTOS') is not None:
            for k in m.get('courseDTOS'):
                temp_model = QueryClassScheduleResponseBodyCourseDTOS()
                self.course_dtos.append(temp_model.from_map(k))
        return self


class QueryClassScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClassScheduleResponseBody = None,
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
            temp_model = QueryClassScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClassScheduleByTimeSchoolHeaders(TeaModel):
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


class QueryClassScheduleByTimeSchoolRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        op_user_id: str = None,
        start_time: int = None,
    ):
        # 1621676000000
        self.end_time = end_time
        # 1621566000000
        self.op_user_id = op_user_id
        # 开始时间
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QueryClassScheduleByTimeSchoolResponseBodyResultClassrooms(TeaModel):
    def __init__(
        self,
        interact_info: str = None,
        target_id: str = None,
    ):
        # 交互信息
        self.interact_info = interact_info
        # 课堂唯一标识
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.interact_info is not None:
            result['interactInfo'] = self.interact_info
        if self.target_id is not None:
            result['targetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interactInfo') is not None:
            self.interact_info = m.get('interactInfo')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        return self


class QueryClassScheduleByTimeSchoolResponseBodyResultEduUserModels(TeaModel):
    def __init__(
        self,
        name: str = None,
        uid: int = None,
        user_id: str = None,
    ):
        self.name = name
        # 用户uid
        self.uid = uid
        # 用户userid
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
        if self.uid is not None:
            result['uid'] = self.uid
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryClassScheduleByTimeSchoolResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_key: str = None,
        class_id: int = None,
        classrooms: List[QueryClassScheduleByTimeSchoolResponseBodyResultClassrooms] = None,
        code: str = None,
        course_group_code: str = None,
        cover_url: str = None,
        creator_corp_id: str = None,
        creator_user_id: str = None,
        creator_user_name: str = None,
        edu_user_models: List[QueryClassScheduleByTimeSchoolResponseBodyResultEduUserModels] = None,
        end_time: int = None,
        ext_info: str = None,
        introduce: str = None,
        name: str = None,
        section_index: int = None,
        section_name: str = None,
        start_time: int = None,
        status: int = None,
        subject_code: str = None,
        teacher_corp_id: str = None,
        teacher_user_id: str = None,
        teacher_user_name: str = None,
    ):
        # 业务唯一键
        self.biz_key = biz_key
        # 课程所在班级id
        self.class_id = class_id
        # 课堂列表
        self.classrooms = classrooms
        # 课程编码
        self.code = code
        # 课程组编码
        self.course_group_code = course_group_code
        # 课程封面地址
        self.cover_url = cover_url
        # 创建者组织id
        self.creator_corp_id = creator_corp_id
        # 创建者UserId
        self.creator_user_id = creator_user_id
        # 创建者UserName
        self.creator_user_name = creator_user_name
        # 课程参与人列表
        self.edu_user_models = edu_user_models
        # 结束时间
        self.end_time = end_time
        # 课程扩展信息
        self.ext_info = ext_info
        # 课程介绍
        self.introduce = introduce
        # 课程名称
        self.name = name
        # 课程所在节次序列号
        self.section_index = section_index
        # 课程编码
        self.section_name = section_name
        # 开始时间
        self.start_time = start_time
        # 课程状态
        self.status = status
        # 学科编码
        self.subject_code = subject_code
        # 老师CorpId
        self.teacher_corp_id = teacher_corp_id
        # 老师UserId
        self.teacher_user_id = teacher_user_id
        # 老师UserName
        self.teacher_user_name = teacher_user_name

    def validate(self):
        if self.classrooms:
            for k in self.classrooms:
                if k:
                    k.validate()
        if self.edu_user_models:
            for k in self.edu_user_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_key is not None:
            result['bizKey'] = self.biz_key
        if self.class_id is not None:
            result['classId'] = self.class_id
        result['classrooms'] = []
        if self.classrooms is not None:
            for k in self.classrooms:
                result['classrooms'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.creator_corp_id is not None:
            result['creatorCorpId'] = self.creator_corp_id
        if self.creator_user_id is not None:
            result['creatorUserId'] = self.creator_user_id
        if self.creator_user_name is not None:
            result['creatorUserName'] = self.creator_user_name
        result['eduUserModels'] = []
        if self.edu_user_models is not None:
            for k in self.edu_user_models:
                result['eduUserModels'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.teacher_corp_id is not None:
            result['teacherCorpId'] = self.teacher_corp_id
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        if self.teacher_user_name is not None:
            result['teacherUserName'] = self.teacher_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizKey') is not None:
            self.biz_key = m.get('bizKey')
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        self.classrooms = []
        if m.get('classrooms') is not None:
            for k in m.get('classrooms'):
                temp_model = QueryClassScheduleByTimeSchoolResponseBodyResultClassrooms()
                self.classrooms.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('creatorCorpId') is not None:
            self.creator_corp_id = m.get('creatorCorpId')
        if m.get('creatorUserId') is not None:
            self.creator_user_id = m.get('creatorUserId')
        if m.get('creatorUserName') is not None:
            self.creator_user_name = m.get('creatorUserName')
        self.edu_user_models = []
        if m.get('eduUserModels') is not None:
            for k in m.get('eduUserModels'):
                temp_model = QueryClassScheduleByTimeSchoolResponseBodyResultEduUserModels()
                self.edu_user_models.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('teacherCorpId') is not None:
            self.teacher_corp_id = m.get('teacherCorpId')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        if m.get('teacherUserName') is not None:
            self.teacher_user_name = m.get('teacherUserName')
        return self


class QueryClassScheduleByTimeSchoolResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryClassScheduleByTimeSchoolResponseBodyResult] = None,
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
                temp_model = QueryClassScheduleByTimeSchoolResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryClassScheduleByTimeSchoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClassScheduleByTimeSchoolResponseBody = None,
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
            temp_model = QueryClassScheduleByTimeSchoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClassScheduleConfigHeaders(TeaModel):
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


class QueryClassScheduleConfigRequest(TeaModel):
    def __init__(
        self,
        class_ids: List[int] = None,
        op_user_id: str = None,
    ):
        # 课程id列表
        self.class_ids = class_ids
        # 操作者的UserID
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids is not None:
            result['classIds'] = self.class_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryClassScheduleConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        class_ids_shrink: str = None,
        op_user_id: str = None,
    ):
        # 课程id列表
        self.class_ids_shrink = class_ids_shrink
        # 操作者的UserID
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids_shrink is not None:
            result['classIds'] = self.class_ids_shrink
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids_shrink = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryClassScheduleConfigResponseBodyResultEnd(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一个月中第几天
        self.day_of_month = day_of_month
        # 月份
        self.month = month
        # 年份
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryClassScheduleConfigResponseBodyResultSectionModelsEnd(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class QueryClassScheduleConfigResponseBodyResultSectionModelsStart(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class QueryClassScheduleConfigResponseBodyResultSectionModels(TeaModel):
    def __init__(
        self,
        end: QueryClassScheduleConfigResponseBodyResultSectionModelsEnd = None,
        section_index: int = None,
        section_name: str = None,
        section_type: str = None,
        start: QueryClassScheduleConfigResponseBodyResultSectionModelsStart = None,
    ):
        # 结束时间
        self.end = end
        # 节次设置
        self.section_index = section_index
        # 节次名称
        self.section_name = section_name
        # 节次类型：COURSE/REST
        self.section_type = section_type
        # 开始时间（时分）
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = QueryClassScheduleConfigResponseBodyResultSectionModelsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        if m.get('start') is not None:
            temp_model = QueryClassScheduleConfigResponseBodyResultSectionModelsStart()
            self.start = temp_model.from_map(m['start'])
        return self


class QueryClassScheduleConfigResponseBodyResultStart(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一个月中的第几天
        self.day_of_month = day_of_month
        # 月份
        self.month = month
        # 年份
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryClassScheduleConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        end: QueryClassScheduleConfigResponseBodyResultEnd = None,
        section_models: List[QueryClassScheduleConfigResponseBodyResultSectionModels] = None,
        start: QueryClassScheduleConfigResponseBodyResultStart = None,
    ):
        # 班级的Id.
        self.class_id = class_id
        self.end = end
        # 节次模型。
        self.section_models = section_models
        # 开始时间
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.end is not None:
            result['end'] = self.end.to_map()
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('end') is not None:
            temp_model = QueryClassScheduleConfigResponseBodyResultEnd()
            self.end = temp_model.from_map(m['end'])
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = QueryClassScheduleConfigResponseBodyResultSectionModels()
                self.section_models.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = QueryClassScheduleConfigResponseBodyResultStart()
            self.start = temp_model.from_map(m['start'])
        return self


class QueryClassScheduleConfigResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryClassScheduleConfigResponseBodyResult] = None,
    ):
        # 查询结果
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
                temp_model = QueryClassScheduleConfigResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryClassScheduleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClassScheduleConfigResponseBody = None,
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
            temp_model = QueryClassScheduleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceListByCorpIdHeaders(TeaModel):
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


class QueryDeviceListByCorpIdRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.operator = operator
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryDeviceListByCorpIdResponseBodyResultList(TeaModel):
    def __init__(
        self,
        app_status: int = None,
        device_code: str = None,
        device_name: str = None,
    ):
        self.app_status = app_status
        self.device_code = device_code
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['appStatus'] = self.app_status
        if self.device_code is not None:
            result['deviceCode'] = self.device_code
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appStatus') is not None:
            self.app_status = m.get('appStatus')
        if m.get('deviceCode') is not None:
            self.device_code = m.get('deviceCode')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        return self


class QueryDeviceListByCorpIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        list: List[QueryDeviceListByCorpIdResponseBodyResultList] = None,
    ):
        self.has_more = has_more
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
                temp_model = QueryDeviceListByCorpIdResponseBodyResultList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryDeviceListByCorpIdResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryDeviceListByCorpIdResponseBodyResult = None,
        success: bool = None,
    ):
        self.result = result
        # Id of the request
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = QueryDeviceListByCorpIdResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryDeviceListByCorpIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceListByCorpIdResponseBody = None,
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
            temp_model = QueryDeviceListByCorpIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEduAssetSpacesHeaders(TeaModel):
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


class QueryEduAssetSpacesRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        max_results: int = None,
        next_token: int = None,
    ):
        # 业务编码
        self.biz_code = biz_code
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['bizCode'] = self.biz_code
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizCode') is not None:
            self.biz_code = m.get('bizCode')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryEduAssetSpacesResponseBodySpaces(TeaModel):
    def __init__(
        self,
        create_time_millis: int = None,
        modify_time_millis: int = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间的时间戳
        self.create_time_millis = create_time_millis
        # 修改时间的时间戳
        self.modify_time_millis = modify_time_millis
        # 权限类型acl：acl授权；custom：自定义授权
        self.permission_mode = permission_mode
        # 空间容量
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 已使用容量
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_millis is not None:
            result['createTimeMillis'] = self.create_time_millis
        if self.modify_time_millis is not None:
            result['modifyTimeMillis'] = self.modify_time_millis
        if self.permission_mode is not None:
            result['permissionMode'] = self.permission_mode
        if self.quota is not None:
            result['quota'] = self.quota
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimeMillis') is not None:
            self.create_time_millis = m.get('createTimeMillis')
        if m.get('modifyTimeMillis') is not None:
            self.modify_time_millis = m.get('modifyTimeMillis')
        if m.get('permissionMode') is not None:
            self.permission_mode = m.get('permissionMode')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')
        return self


class QueryEduAssetSpacesResponseBody(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        spaces: List[QueryEduAssetSpacesResponseBodySpaces] = None,
    ):
        # 是否还有数据
        self.has_more = has_more
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 空间结果集
        self.spaces = spaces

    def validate(self):
        if self.spaces:
            for k in self.spaces:
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
        result['spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.spaces = []
        if m.get('spaces') is not None:
            for k in m.get('spaces'):
                temp_model = QueryEduAssetSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class QueryEduAssetSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEduAssetSpacesResponseBody = None,
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
            temp_model = QueryEduAssetSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupIdHeaders(TeaModel):
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


class QueryGroupIdRequest(TeaModel):
    def __init__(
        self,
        sn: str = None,
    ):
        # 设备序列号
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class QueryGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        group_id: str = None,
        merchant_id: str = None,
        merchant_name: str = None,
        name: str = None,
        pid: str = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 人脸库id
        self.group_id = group_id
        # 商户id
        self.merchant_id = merchant_id
        # 商户名称
        self.merchant_name = merchant_name
        # 开发者名称
        self.name = name
        # 开发者pid
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.merchant_name is not None:
            result['merchantName'] = self.merchant_name
        if self.name is not None:
            result['name'] = self.name
        if self.pid is not None:
            result['pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('merchantName') is not None:
            self.merchant_name = m.get('merchantName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        return self


class QueryGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGroupIdResponseBody = None,
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
            temp_model = QueryGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrgRelationListHeaders(TeaModel):
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


class QueryOrgRelationListRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
    ):
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class QueryOrgRelationListResponseBodyResult(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_count: int = None,
        name: str = None,
    ):
        self.corp_id = corp_id
        self.device_count = device_count
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.device_count is not None:
            result['deviceCount'] = self.device_count
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deviceCount') is not None:
            self.device_count = m.get('deviceCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryOrgRelationListResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryOrgRelationListResponseBodyResult] = None,
        success: bool = None,
    ):
        self.result = result
        # Id of the request
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = QueryOrgRelationListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryOrgRelationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrgRelationListResponseBody = None,
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
            temp_model = QueryOrgRelationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrgSecretKeyHeaders(TeaModel):
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


class QueryOrgSecretKeyRequest(TeaModel):
    def __init__(
        self,
        isv_code: str = None,
        op_user_id: str = None,
    ):
        # 合作方编码
        self.isv_code = isv_code
        # 操作人
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isv_code is not None:
            result['isvCode'] = self.isv_code
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isvCode') is not None:
            self.isv_code = m.get('isvCode')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryOrgSecretKeyResponseBodyUniversitySecretKeyInfo(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
    ):
        # 秘钥key
        self.secret_key = secret_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        return self


class QueryOrgSecretKeyResponseBody(TeaModel):
    def __init__(
        self,
        university_secret_key_info: QueryOrgSecretKeyResponseBodyUniversitySecretKeyInfo = None,
    ):
        # 秘钥信息
        self.university_secret_key_info = university_secret_key_info

    def validate(self):
        if self.university_secret_key_info:
            self.university_secret_key_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_secret_key_info is not None:
            result['universitySecretKeyInfo'] = self.university_secret_key_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universitySecretKeyInfo') is not None:
            temp_model = QueryOrgSecretKeyResponseBodyUniversitySecretKeyInfo()
            self.university_secret_key_info = temp_model.from_map(m['universitySecretKeyInfo'])
        return self


class QueryOrgSecretKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrgSecretKeyResponseBody = None,
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
            temp_model = QueryOrgSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrgTypeHeaders(TeaModel):
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


class QueryOrgTypeResponseBody(TeaModel):
    def __init__(
        self,
        org_type: int = None,
    ):
        # 组织类型
        self.org_type = org_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_type is not None:
            result['orgType'] = self.org_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')
        return self


class QueryOrgTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrgTypeResponseBody = None,
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
            temp_model = QueryOrgTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPayResultHeaders(TeaModel):
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


class QueryPayResultRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        order_no: str = None,
        signature: str = None,
        sn: str = None,
        timestamp: int = None,
        user_id: str = None,
        version: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 订单号
        self.order_no = order_no
        # 签名
        self.signature = signature
        # 设备序列号
        self.sn = sn
        # utc时间戳
        self.timestamp = timestamp
        # 用户id
        self.user_id = user_id
        # 版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.signature is not None:
            result['signature'] = self.signature
        if self.sn is not None:
            result['sn'] = self.sn
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class QueryPayResultResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
    ):
        # 状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryPayResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPayResultResponseBody = None,
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
            temp_model = QueryPayResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhysicalClassroomHeaders(TeaModel):
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


class QueryPhysicalClassroomRequest(TeaModel):
    def __init__(
        self,
        classroom_id: int = None,
        op_user_id: str = None,
    ):
        # 教室id
        self.classroom_id = classroom_id
        # 操作人id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryPhysicalClassroomResponseBodyResult(TeaModel):
    def __init__(
        self,
        classroom_building: str = None,
        classroom_campus: str = None,
        classroom_floor: str = None,
        classroom_id: int = None,
        classroom_name: str = None,
        classroom_number: str = None,
        direct_broadcast: str = None,
    ):
        # 教室教学楼
        self.classroom_building = classroom_building
        # 教室校区
        self.classroom_campus = classroom_campus
        # 教室楼层
        self.classroom_floor = classroom_floor
        # 教室ID
        self.classroom_id = classroom_id
        # 教室名称
        self.classroom_name = classroom_name
        # 教室房间号
        self.classroom_number = classroom_number
        # 是否支持直播
        self.direct_broadcast = direct_broadcast

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_building is not None:
            result['classroomBuilding'] = self.classroom_building
        if self.classroom_campus is not None:
            result['classroomCampus'] = self.classroom_campus
        if self.classroom_floor is not None:
            result['classroomFloor'] = self.classroom_floor
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.classroom_name is not None:
            result['classroomName'] = self.classroom_name
        if self.classroom_number is not None:
            result['classroomNumber'] = self.classroom_number
        if self.direct_broadcast is not None:
            result['directBroadcast'] = self.direct_broadcast
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomBuilding') is not None:
            self.classroom_building = m.get('classroomBuilding')
        if m.get('classroomCampus') is not None:
            self.classroom_campus = m.get('classroomCampus')
        if m.get('classroomFloor') is not None:
            self.classroom_floor = m.get('classroomFloor')
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('classroomName') is not None:
            self.classroom_name = m.get('classroomName')
        if m.get('classroomNumber') is not None:
            self.classroom_number = m.get('classroomNumber')
        if m.get('directBroadcast') is not None:
            self.direct_broadcast = m.get('directBroadcast')
        return self


class QueryPhysicalClassroomResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryPhysicalClassroomResponseBodyResult = None,
        success: bool = None,
    ):
        # 返回结果
        self.result = result
        # 请求是否成功
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = QueryPhysicalClassroomResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryPhysicalClassroomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPhysicalClassroomResponseBody = None,
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
            temp_model = QueryPhysicalClassroomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchaseInfoHeaders(TeaModel):
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


class QueryPurchaseInfoRequest(TeaModel):
    def __init__(
        self,
        merchant_id: str = None,
        scene: int = None,
        sn: str = None,
        user_id: str = None,
    ):
        # 商户id
        self.merchant_id = merchant_id
        # 场景
        self.scene = scene
        # 设备序列号
        self.sn = sn
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.sn is not None:
            result['sn'] = self.sn
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryPurchaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        merchant_id: str = None,
        name: str = None,
        scene: int = None,
        status: int = None,
        user_id: str = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 商户id
        self.merchant_id = merchant_id
        # 名字
        self.name = name
        # 场景id
        self.scene = scene
        # 状态
        self.status = status
        # 员工id
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
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.name is not None:
            result['name'] = self.name
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryPurchaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPurchaseInfoResponseBody = None,
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
            temp_model = QueryPurchaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRemoteClassCourseHeaders(TeaModel):
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


class QueryRemoteClassCourseRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        operator: str = None,
        start_time: int = None,
    ):
        # 结束时间
        self.end_time = end_time
        # 操作者用户ID
        self.operator = operator
        # 开始时间
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QueryRemoteClassCourseResponseBodyResultAttendParticipants(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        org_name: str = None,
        participant_id: str = None,
        participant_name: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 组织名称
        self.org_name = org_name
        # 参与方ID
        self.participant_id = participant_id
        # 参与方名称
        self.participant_name = participant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        if self.participant_name is not None:
            result['participantName'] = self.participant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        if m.get('participantName') is not None:
            self.participant_name = m.get('participantName')
        return self


class QueryRemoteClassCourseResponseBodyResultTeachingParticipant(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        org_name: str = None,
        participant_id: str = None,
        participant_name: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 组织名称
        self.org_name = org_name
        # 参与方ID
        self.participant_id = participant_id
        # 参与方名称
        self.participant_name = participant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.org_name is not None:
            result['orgName'] = self.org_name
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        if self.participant_name is not None:
            result['participantName'] = self.participant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        if m.get('participantName') is not None:
            self.participant_name = m.get('participantName')
        return self


class QueryRemoteClassCourseResponseBodyResult(TeaModel):
    def __init__(
        self,
        attend_participants: List[QueryRemoteClassCourseResponseBodyResultAttendParticipants] = None,
        can_edit: bool = None,
        course_code: str = None,
        course_name: str = None,
        course_ways: List[str] = None,
        end_time: int = None,
        start_time: int = None,
        status: int = None,
        teaching_participant: QueryRemoteClassCourseResponseBodyResultTeachingParticipant = None,
    ):
        # 听课设备列表
        self.attend_participants = attend_participants
        # 课程是否可以编辑或删除
        self.can_edit = can_edit
        # 课程code
        self.course_code = course_code
        # 课程名称
        self.course_name = course_name
        # 当前组织在课程中的角色列表：TEACHING：授课方；ATTEND：听课方
        self.course_ways = course_ways
        # 结束时间
        self.end_time = end_time
        # 开始时间
        self.start_time = start_time
        # 课程状态：0: 未开始；1: 已开始；2: 已结束
        self.status = status
        # 授课设备
        self.teaching_participant = teaching_participant

    def validate(self):
        if self.attend_participants:
            for k in self.attend_participants:
                if k:
                    k.validate()
        if self.teaching_participant:
            self.teaching_participant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendParticipants'] = []
        if self.attend_participants is not None:
            for k in self.attend_participants:
                result['attendParticipants'].append(k.to_map() if k else None)
        if self.can_edit is not None:
            result['canEdit'] = self.can_edit
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.course_ways is not None:
            result['courseWays'] = self.course_ways
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.teaching_participant is not None:
            result['teachingParticipant'] = self.teaching_participant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attend_participants = []
        if m.get('attendParticipants') is not None:
            for k in m.get('attendParticipants'):
                temp_model = QueryRemoteClassCourseResponseBodyResultAttendParticipants()
                self.attend_participants.append(temp_model.from_map(k))
        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('courseWays') is not None:
            self.course_ways = m.get('courseWays')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('teachingParticipant') is not None:
            temp_model = QueryRemoteClassCourseResponseBodyResultTeachingParticipant()
            self.teaching_participant = temp_model.from_map(m['teachingParticipant'])
        return self


class QueryRemoteClassCourseResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryRemoteClassCourseResponseBodyResult] = None,
        success: bool = None,
    ):
        self.result = result
        # 是否成功
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = QueryRemoteClassCourseResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryRemoteClassCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRemoteClassCourseResponseBody = None,
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
            temp_model = QueryRemoteClassCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySchoolUserFaceHeaders(TeaModel):
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


class QuerySchoolUserFaceRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        sn: str = None,
        type: int = None,
    ):
        # 页码
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        # 设备序列号
        self.sn = sn
        # 类型
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
        if self.sn is not None:
            result['sn'] = self.sn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QuerySchoolUserFaceResponseBodyUserFaceList(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        name: str = None,
        status: int = None,
        user_id: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 员工名字
        self.name = name
        # 员工状态
        self.status = status
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QuerySchoolUserFaceResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        has_more: bool = None,
        user_face_list: List[QuerySchoolUserFaceResponseBodyUserFaceList] = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 是否还有下一页
        self.has_more = has_more
        # 用户人脸列表
        self.user_face_list = user_face_list

    def validate(self):
        if self.user_face_list:
            for k in self.user_face_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.has_more is not None:
            result['hasMore'] = self.has_more
        result['userFaceList'] = []
        if self.user_face_list is not None:
            for k in self.user_face_list:
                result['userFaceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')
        self.user_face_list = []
        if m.get('userFaceList') is not None:
            for k in m.get('userFaceList'):
                temp_model = QuerySchoolUserFaceResponseBodyUserFaceList()
                self.user_face_list.append(temp_model.from_map(k))
        return self


class QuerySchoolUserFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySchoolUserFaceResponseBody = None,
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
            temp_model = QuerySchoolUserFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatisticsDataHeaders(TeaModel):
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


class QueryStatisticsDataRequest(TeaModel):
    def __init__(
        self,
        section_index_list: List[int] = None,
        teacher_user_ids: List[str] = None,
        end_time: int = None,
        op_user_id: str = None,
        start_time: int = None,
    ):
        # 课程节次列表
        self.section_index_list = section_index_list
        # 老师UserIds
        self.teacher_user_ids = teacher_user_ids
        # endTime
        self.end_time = end_time
        # opUserId
        self.op_user_id = op_user_id
        # startTime
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.section_index_list is not None:
            result['sectionIndexList'] = self.section_index_list
        if self.teacher_user_ids is not None:
            result['teacherUserIds'] = self.teacher_user_ids
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sectionIndexList') is not None:
            self.section_index_list = m.get('sectionIndexList')
        if m.get('teacherUserIds') is not None:
            self.teacher_user_ids = m.get('teacherUserIds')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QueryStatisticsDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        course_count: int = None,
        course_hours: float = None,
        subject_code: str = None,
        subject_name: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 班级id
        self.class_id = class_id
        # 总课程数
        self.course_count = course_count
        # 总学时
        self.course_hours = course_hours
        # 学科code
        self.subject_code = subject_code
        # 学科名称
        self.subject_name = subject_name
        # 用户id
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.course_count is not None:
            result['courseCount'] = self.course_count
        if self.course_hours is not None:
            result['courseHours'] = self.course_hours
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('courseCount') is not None:
            self.course_count = m.get('courseCount')
        if m.get('courseHours') is not None:
            self.course_hours = m.get('courseHours')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class QueryStatisticsDataResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryStatisticsDataResponseBodyResult] = None,
    ):
        # result
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
                temp_model = QueryStatisticsDataResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryStatisticsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryStatisticsDataResponseBody = None,
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
            temp_model = QueryStatisticsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubjectTeachersHeaders(TeaModel):
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


class QuerySubjectTeachersRequest(TeaModel):
    def __init__(
        self,
        class_ids: List[int] = None,
        op_user_id: str = None,
        subject_code: str = None,
    ):
        # 班级ids
        self.class_ids = class_ids
        # 操作人id
        self.op_user_id = op_user_id
        # 学科code
        self.subject_code = subject_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids is not None:
            result['classIds'] = self.class_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        return self


class QuerySubjectTeachersResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        corp_id: str = None,
        period_code: str = None,
        subject_code: str = None,
        subject_name: str = None,
        teacher_name: str = None,
        teacher_user_id: str = None,
    ):
        # 班级id
        self.class_id = class_id
        # 学校corpId
        self.corp_id = corp_id
        # 学段code
        self.period_code = period_code
        # 学科code
        self.subject_code = subject_code
        # 学科名称
        self.subject_name = subject_name
        # 老师名称
        self.teacher_name = teacher_name
        # 老师Userid
        self.teacher_user_id = teacher_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        if self.teacher_name is not None:
            result['teacherName'] = self.teacher_name
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        if m.get('teacherName') is not None:
            self.teacher_name = m.get('teacherName')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        return self


class QuerySubjectTeachersResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QuerySubjectTeachersResponseBodyResult] = None,
    ):
        # 结果
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
                temp_model = QuerySubjectTeachersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QuerySubjectTeachersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySubjectTeachersResponseBody = None,
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
            temp_model = QuerySubjectTeachersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTeachSubjectsHeaders(TeaModel):
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


class QueryTeachSubjectsRequest(TeaModel):
    def __init__(
        self,
        class_ids: List[int] = None,
        op_user_id: str = None,
    ):
        # 班级ids
        self.class_ids = class_ids
        # 操作者UserId
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ids is not None:
            result['classIds'] = self.class_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classIds') is not None:
            self.class_ids = m.get('classIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryTeachSubjectsResponseBodyResult(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        corp_id: str = None,
        period_code: str = None,
        subject_code: str = None,
        subject_name: str = None,
        teacher_name: str = None,
        teacher_user_id: str = None,
    ):
        # 班级id
        self.class_id = class_id
        # 学校corpId
        self.corp_id = corp_id
        # 学段code
        self.period_code = period_code
        # 学科code
        self.subject_code = subject_code
        # 学科名称
        self.subject_name = subject_name
        # 老师名称
        self.teacher_name = teacher_name
        # 老师Userid
        self.teacher_user_id = teacher_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        if self.subject_code is not None:
            result['subjectCode'] = self.subject_code
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        if self.teacher_name is not None:
            result['teacherName'] = self.teacher_name
        if self.teacher_user_id is not None:
            result['teacherUserId'] = self.teacher_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        if m.get('subjectCode') is not None:
            self.subject_code = m.get('subjectCode')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        if m.get('teacherName') is not None:
            self.teacher_name = m.get('teacherName')
        if m.get('teacherUserId') is not None:
            self.teacher_user_id = m.get('teacherUserId')
        return self


class QueryTeachSubjectsResponseBody(TeaModel):
    def __init__(
        self,
        result: List[QueryTeachSubjectsResponseBodyResult] = None,
    ):
        # 结果
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
                temp_model = QueryTeachSubjectsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryTeachSubjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTeachSubjectsResponseBody = None,
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
            temp_model = QueryTeachSubjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUniversityCourseGroupHeaders(TeaModel):
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


class QueryUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        op_user_id: str = None,
    ):
        # 课程编码
        self.course_group_code = course_group_code
        # 操作人
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemEndDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 日
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemStartDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 日
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModels(TeaModel):
    def __init__(
        self,
        class_period_type: int = None,
        classroom_id: int = None,
        course_type: int = None,
        courser_group_item_end_date: QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemEndDate = None,
        courser_group_item_start_date: QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemStartDate = None,
        day_of_week: int = None,
        section_index: List[int] = None,
    ):
        # 上课周期
        self.class_period_type = class_period_type
        # 教室主键
        self.classroom_id = classroom_id
        # 课程类型
        self.course_type = course_type
        # 结束时间
        self.courser_group_item_end_date = courser_group_item_end_date
        # 开始时间
        self.courser_group_item_start_date = courser_group_item_start_date
        # 一周的第几天
        self.day_of_week = day_of_week
        # 课节
        self.section_index = section_index

    def validate(self):
        if self.courser_group_item_end_date:
            self.courser_group_item_end_date.validate()
        if self.courser_group_item_start_date:
            self.courser_group_item_start_date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_period_type is not None:
            result['classPeriodType'] = self.class_period_type
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.course_type is not None:
            result['courseType'] = self.course_type
        if self.courser_group_item_end_date is not None:
            result['courserGroupItemEndDate'] = self.courser_group_item_end_date.to_map()
        if self.courser_group_item_start_date is not None:
            result['courserGroupItemStartDate'] = self.courser_group_item_start_date.to_map()
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classPeriodType') is not None:
            self.class_period_type = m.get('classPeriodType')
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('courseType') is not None:
            self.course_type = m.get('courseType')
        if m.get('courserGroupItemEndDate') is not None:
            temp_model = QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemEndDate()
            self.courser_group_item_end_date = temp_model.from_map(m['courserGroupItemEndDate'])
        if m.get('courserGroupItemStartDate') is not None:
            temp_model = QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModelsCourserGroupItemStartDate()
            self.courser_group_item_start_date = temp_model.from_map(m['courserGroupItemStartDate'])
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        return self


class QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfo(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        course_group_introduce: str = None,
        course_group_name: str = None,
        courser_group_item_models: List[QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModels] = None,
        isv_course_group_code: str = None,
        period_code: str = None,
        school_year: str = None,
        semester: int = None,
        subject_name: str = None,
    ):
        # 课程组编码
        self.course_group_code = course_group_code
        # 课程组介绍
        self.course_group_introduce = course_group_introduce
        # 课程组名称
        self.course_group_name = course_group_name
        # 课程组详细
        self.courser_group_item_models = courser_group_item_models
        # 合作方课程组code
        self.isv_course_group_code = isv_course_group_code
        # 学段编码
        self.period_code = period_code
        # 学年
        self.school_year = school_year
        # 学期
        self.semester = semester
        # 学科名称
        self.subject_name = subject_name

    def validate(self):
        if self.courser_group_item_models:
            for k in self.courser_group_item_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.course_group_introduce is not None:
            result['courseGroupIntroduce'] = self.course_group_introduce
        if self.course_group_name is not None:
            result['courseGroupName'] = self.course_group_name
        result['courserGroupItemModels'] = []
        if self.courser_group_item_models is not None:
            for k in self.courser_group_item_models:
                result['courserGroupItemModels'].append(k.to_map() if k else None)
        if self.isv_course_group_code is not None:
            result['isvCourseGroupCode'] = self.isv_course_group_code
        if self.period_code is not None:
            result['periodCode'] = self.period_code
        if self.school_year is not None:
            result['schoolYear'] = self.school_year
        if self.semester is not None:
            result['semester'] = self.semester
        if self.subject_name is not None:
            result['subjectName'] = self.subject_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('courseGroupIntroduce') is not None:
            self.course_group_introduce = m.get('courseGroupIntroduce')
        if m.get('courseGroupName') is not None:
            self.course_group_name = m.get('courseGroupName')
        self.courser_group_item_models = []
        if m.get('courserGroupItemModels') is not None:
            for k in m.get('courserGroupItemModels'):
                temp_model = QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfoCourserGroupItemModels()
                self.courser_group_item_models.append(temp_model.from_map(k))
        if m.get('isvCourseGroupCode') is not None:
            self.isv_course_group_code = m.get('isvCourseGroupCode')
        if m.get('periodCode') is not None:
            self.period_code = m.get('periodCode')
        if m.get('schoolYear') is not None:
            self.school_year = m.get('schoolYear')
        if m.get('semester') is not None:
            self.semester = m.get('semester')
        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')
        return self


class QueryUniversityCourseGroupResponseBody(TeaModel):
    def __init__(
        self,
        university_course_group_info: QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfo = None,
    ):
        # 课程组信息
        self.university_course_group_info = university_course_group_info

    def validate(self):
        if self.university_course_group_info:
            self.university_course_group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_course_group_info is not None:
            result['universityCourseGroupInfo'] = self.university_course_group_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universityCourseGroupInfo') is not None:
            temp_model = QueryUniversityCourseGroupResponseBodyUniversityCourseGroupInfo()
            self.university_course_group_info = temp_model.from_map(m['universityCourseGroupInfo'])
        return self


class QueryUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUniversityCourseGroupResponseBody = None,
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
            temp_model = QueryUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserFaceHeaders(TeaModel):
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


class QueryUserFaceRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        sn: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 设备序列号
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class QueryUserFaceResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        face_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 组织id
        self.corp_id = corp_id
        # 人脸id
        self.face_id = face_id
        # 员工姓名
        self.name = name
        # 员工id
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
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryUserFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUserFaceResponseBody = None,
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
            temp_model = QueryUserFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserPayInfoHeaders(TeaModel):
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


class QueryUserPayInfoRequest(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        sn: str = None,
        user_id: str = None,
    ):
        # 人脸id
        self.face_id = face_id
        # 设备id
        self.sn = sn
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['faceId'] = self.face_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceId') is not None:
            self.face_id = m.get('faceId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryUserPayInfoResponseBody(TeaModel):
    def __init__(
        self,
        sign_no: str = None,
    ):
        # 签约单号
        self.sign_no = sign_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_no is not None:
            result['signNo'] = self.sign_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('signNo') is not None:
            self.sign_no = m.get('signNo')
        return self


class QueryUserPayInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUserPayInfoResponseBody = None,
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
            temp_model = QueryUserPayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDeviceHeaders(TeaModel):
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


class RemoveDeviceRequest(TeaModel):
    def __init__(
        self,
        merchant_id: str = None,
        sn: str = None,
    ):
        # 商户id
        self.merchant_id = merchant_id
        # 设备sn
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_id is not None:
            result['merchantId'] = self.merchant_id
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('merchantId') is not None:
            self.merchant_id = m.get('merchantId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class RemoveDeviceResponseBody(TeaModel):
    def __init__(
        self,
        success: str = None,
    ):
        # 返回结果
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


class RemoveDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveDeviceResponseBody = None,
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
            temp_model = RemoveDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportDeviceLogHeaders(TeaModel):
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


class ReportDeviceLogRequest(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        sn: str = None,
        type: str = None,
    ):
        # 文件id
        self.media_id = media_id
        # 设备序列号
        self.sn = sn
        # 文件类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ReportDeviceLogResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 上传成功
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


class ReportDeviceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportDeviceLogResponseBody = None,
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
            temp_model = ReportDeviceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportDeviceUseLogHeaders(TeaModel):
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


class ReportDeviceUseLogRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        order_no: str = None,
        sn: str = None,
        user_id: str = None,
    ):
        # 操作
        self.action = action
        # 订单号
        self.order_no = order_no
        # 设备序列号
        self.sn = sn
        # 员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.sn is not None:
            result['sn'] = self.sn
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ReportDeviceUseLogResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 返回结果
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


class ReportDeviceUseLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportDeviceUseLogResponseBody = None,
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
            temp_model = ReportDeviceUseLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTeachersHeaders(TeaModel):
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


class SearchTeachersRequest(TeaModel):
    def __init__(
        self,
        name_keyword: str = None,
    ):
        self.name_keyword = name_keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_keyword is not None:
            result['nameKeyword'] = self.name_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameKeyword') is not None:
            self.name_keyword = m.get('nameKeyword')
        return self


class SearchTeachersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        dept_name: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 所在其中一个班级ID
        self.class_id = class_id
        # 所在其中一个班级名称
        self.dept_name = dept_name
        # 名称
        self.name = name
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.dept_name is not None:
            result['deptName'] = self.dept_name
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SearchTeachersResponseBody(TeaModel):
    def __init__(
        self,
        users: List[SearchTeachersResponseBodyUsers] = None,
    ):
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = SearchTeachersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class SearchTeachersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTeachersResponseBody = None,
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
            temp_model = SearchTeachersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageHeaders(TeaModel):
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


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        from_user_id: str = None,
        sn: str = None,
        to_user_id_list: List[str] = None,
        type: int = None,
    ):
        # 消息的唯一id
        self.biz_id = biz_id
        # 发送者
        self.from_user_id = from_user_id
        # 设备sn
        self.sn = sn
        # 接收者
        self.to_user_id_list = to_user_id_list
        # 发送消息的类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.from_user_id is not None:
            result['fromUserId'] = self.from_user_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.to_user_id_list is not None:
            result['toUserIdList'] = self.to_user_id_list
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('fromUserId') is not None:
            self.from_user_id = m.get('fromUserId')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('toUserIdList') is not None:
            self.to_user_id_list = m.get('toUserIdList')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        success_info: str = None,
    ):
        # 成功信息
        self.success_info = success_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_info is not None:
            result['successInfo'] = self.success_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('successInfo') is not None:
            self.success_info = m.get('successInfo')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCourseHeaders(TeaModel):
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


class StartCourseRequestLivePlayInfoList(TeaModel):
    def __init__(
        self,
        live_input_url: str = None,
        live_output_flv_url: str = None,
        live_output_hls_url: str = None,
        live_type: int = None,
        replay_url: str = None,
    ):
        # 直播推流地址
        self.live_input_url = live_input_url
        # Flv格式直播地址
        self.live_output_flv_url = live_output_flv_url
        # Hls格式直播拉流地址
        self.live_output_hls_url = live_output_hls_url
        # 直播流类型
        self.live_type = live_type
        # 视频回放地址
        self.replay_url = replay_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_input_url is not None:
            result['liveInputUrl'] = self.live_input_url
        if self.live_output_flv_url is not None:
            result['liveOutputFlvUrl'] = self.live_output_flv_url
        if self.live_output_hls_url is not None:
            result['liveOutputHlsUrl'] = self.live_output_hls_url
        if self.live_type is not None:
            result['liveType'] = self.live_type
        if self.replay_url is not None:
            result['replayUrl'] = self.replay_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveInputUrl') is not None:
            self.live_input_url = m.get('liveInputUrl')
        if m.get('liveOutputFlvUrl') is not None:
            self.live_output_flv_url = m.get('liveOutputFlvUrl')
        if m.get('liveOutputHlsUrl') is not None:
            self.live_output_hls_url = m.get('liveOutputHlsUrl')
        if m.get('liveType') is not None:
            self.live_type = m.get('liveType')
        if m.get('replayUrl') is not None:
            self.replay_url = m.get('replayUrl')
        return self


class StartCourseRequest(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        ext: str = None,
        isv_code: str = None,
        live_play_info_list: List[StartCourseRequestLivePlayInfoList] = None,
        op_user_id: str = None,
    ):
        # 课程编码
        self.course_code = course_code
        # 拓展字段
        self.ext = ext
        # isvCode
        self.isv_code = isv_code
        # livePlayInfoList
        self.live_play_info_list = live_play_info_list
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        if self.live_play_info_list:
            for k in self.live_play_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.ext is not None:
            result['ext'] = self.ext
        if self.isv_code is not None:
            result['isvCode'] = self.isv_code
        result['livePlayInfoList'] = []
        if self.live_play_info_list is not None:
            for k in self.live_play_info_list:
                result['livePlayInfoList'].append(k.to_map() if k else None)
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('isvCode') is not None:
            self.isv_code = m.get('isvCode')
        self.live_play_info_list = []
        if m.get('livePlayInfoList') is not None:
            for k in m.get('livePlayInfoList'):
                temp_model = StartCourseRequestLivePlayInfoList()
                self.live_play_info_list.append(temp_model.from_map(k))
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class StartCourseResponseBodyUniversityCourseCommonResponse(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        success: bool = None,
    ):
        # 课程编码
        self.course_code = course_code
        # 调用是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartCourseResponseBody(TeaModel):
    def __init__(
        self,
        university_course_common_response: StartCourseResponseBodyUniversityCourseCommonResponse = None,
    ):
        self.university_course_common_response = university_course_common_response

    def validate(self):
        if self.university_course_common_response:
            self.university_course_common_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_course_common_response is not None:
            result['universityCourseCommonResponse'] = self.university_course_common_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universityCourseCommonResponse') is not None:
            temp_model = StartCourseResponseBodyUniversityCourseCommonResponse()
            self.university_course_common_response = temp_model.from_map(m['universityCourseCommonResponse'])
        return self


class StartCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCourseResponseBody = None,
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
            temp_model = StartCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCoursePrepareHeaders(TeaModel):
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


class StartCoursePrepareRequest(TeaModel):
    def __init__(
        self,
        course_date: str = None,
        course_group_code: str = None,
        device_id: str = None,
        ext: str = None,
        isv_code: str = None,
        live_cover_image: str = None,
        section_index: List[int] = None,
        op_user_id: str = None,
    ):
        # 上课日期
        self.course_date = course_date
        # 课程组编号
        self.course_group_code = course_group_code
        # 设备id
        self.device_id = device_id
        # 拓展信息
        self.ext = ext
        # isv编号
        self.isv_code = isv_code
        # 封面url
        self.live_cover_image = live_cover_image
        # 课节信息
        self.section_index = section_index
        # 操作人
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_date is not None:
            result['courseDate'] = self.course_date
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.ext is not None:
            result['ext'] = self.ext
        if self.isv_code is not None:
            result['isvCode'] = self.isv_code
        if self.live_cover_image is not None:
            result['liveCoverImage'] = self.live_cover_image
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseDate') is not None:
            self.course_date = m.get('courseDate')
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('isvCode') is not None:
            self.isv_code = m.get('isvCode')
        if m.get('liveCoverImage') is not None:
            self.live_cover_image = m.get('liveCoverImage')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class StartCoursePrepareResponseBodyUniversityCourseCommonResponse(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        success: bool = None,
    ):
        # 课程编码
        self.course_code = course_code
        # 调用是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartCoursePrepareResponseBody(TeaModel):
    def __init__(
        self,
        university_course_common_response: StartCoursePrepareResponseBodyUniversityCourseCommonResponse = None,
    ):
        self.university_course_common_response = university_course_common_response

    def validate(self):
        if self.university_course_common_response:
            self.university_course_common_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.university_course_common_response is not None:
            result['universityCourseCommonResponse'] = self.university_course_common_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('universityCourseCommonResponse') is not None:
            temp_model = StartCoursePrepareResponseBodyUniversityCourseCommonResponse()
            self.university_course_common_response = temp_model.from_map(m['universityCourseCommonResponse'])
        return self


class StartCoursePrepareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCoursePrepareResponseBody = None,
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
            temp_model = StartCoursePrepareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeUniversityCourseGroupHeaders(TeaModel):
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


class SubscribeUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        student_user_ids: List[str] = None,
        op_user_id: str = None,
    ):
        # 课程组编号
        self.course_group_code = course_group_code
        # 学生用户Id
        self.student_user_ids = student_user_ids
        # 操作人id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.student_user_ids is not None:
            result['studentUserIds'] = self.student_user_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('studentUserIds') is not None:
            self.student_user_ids = m.get('studentUserIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class SubscribeUniversityCourseGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 订阅结果
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


class SubscribeUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubscribeUniversityCourseGroupResponseBody = None,
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
            temp_model = SubscribeUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeUniversityCourseGroupHeaders(TeaModel):
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


class UnsubscribeUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        student_user_ids: List[str] = None,
        op_user_id: str = None,
    ):
        # 课程组
        self.course_group_code = course_group_code
        # 学生用户id
        self.student_user_ids = student_user_ids
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.student_user_ids is not None:
            result['studentUserIds'] = self.student_user_ids
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('studentUserIds') is not None:
            self.student_user_ids = m.get('studentUserIds')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class UnsubscribeUniversityCourseGroupResponseBody(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 取消订阅结果
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


class UnsubscribeUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnsubscribeUniversityCourseGroupResponseBody = None,
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
            temp_model = UnsubscribeUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCoursesOfClassHeaders(TeaModel):
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


class UpdateCoursesOfClassRequestCoursesDateModel(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # dayOfMonth
        self.day_of_month = day_of_month
        # month
        self.month = month
        # year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class UpdateCoursesOfClassRequestCoursesSectionModel(TeaModel):
    def __init__(
        self,
        section_index: int = None,
        section_name: str = None,
        section_type: str = None,
    ):
        # 节次index
        self.section_index = section_index
        # 节次名称
        self.section_name = section_name
        # sectionType
        self.section_type = section_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_name is not None:
            result['sectionName'] = self.section_name
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionName') is not None:
            self.section_name = m.get('sectionName')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        return self


class UpdateCoursesOfClassRequestCourses(TeaModel):
    def __init__(
        self,
        course_code: str = None,
        course_group_code: str = None,
        course_name: str = None,
        creator_name: str = None,
        date_model: UpdateCoursesOfClassRequestCoursesDateModel = None,
        delete_tag: bool = None,
        location: str = None,
        section_model: UpdateCoursesOfClassRequestCoursesSectionModel = None,
        teacher_staff_ids: List[str] = None,
    ):
        # 课程code：删除/更新必填
        self.course_code = course_code
        # 课组code
        self.course_group_code = course_group_code
        # 课程名称
        self.course_name = course_name
        # 创建者名字
        self.creator_name = creator_name
        # 上课日期
        self.date_model = date_model
        # 删除标记：要删除为ture
        self.delete_tag = delete_tag
        # 上课地点
        self.location = location
        # 节次模型
        self.section_model = section_model
        # 老师Staffid
        self.teacher_staff_ids = teacher_staff_ids

    def validate(self):
        if self.date_model:
            self.date_model.validate()
        if self.section_model:
            self.section_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.date_model is not None:
            result['dateModel'] = self.date_model.to_map()
        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag
        if self.location is not None:
            result['location'] = self.location
        if self.section_model is not None:
            result['sectionModel'] = self.section_model.to_map()
        if self.teacher_staff_ids is not None:
            result['teacherStaffIds'] = self.teacher_staff_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('dateModel') is not None:
            temp_model = UpdateCoursesOfClassRequestCoursesDateModel()
            self.date_model = temp_model.from_map(m['dateModel'])
        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('sectionModel') is not None:
            temp_model = UpdateCoursesOfClassRequestCoursesSectionModel()
            self.section_model = temp_model.from_map(m['sectionModel'])
        if m.get('teacherStaffIds') is not None:
            self.teacher_staff_ids = m.get('teacherStaffIds')
        return self


class UpdateCoursesOfClassRequestSectionConfigSectionModelsEnd(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class UpdateCoursesOfClassRequestSectionConfigSectionModelsStart(TeaModel):
    def __init__(
        self,
        hour: int = None,
        min: int = None,
    ):
        # 小时
        self.hour = hour
        # 分钟
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['hour'] = self.hour
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self


class UpdateCoursesOfClassRequestSectionConfigSectionModels(TeaModel):
    def __init__(
        self,
        end: UpdateCoursesOfClassRequestSectionConfigSectionModelsEnd = None,
        section_index: int = None,
        section_type: str = None,
        start: UpdateCoursesOfClassRequestSectionConfigSectionModelsStart = None,
    ):
        # 结束时间
        self.end = end
        # 第几节。
        self.section_index = section_index
        # 节次类型枚举：COURSE/REST
        self.section_type = section_type
        # 开始时间
        self.start = start

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        if self.section_type is not None:
            result['sectionType'] = self.section_type
        if self.start is not None:
            result['start'] = self.start.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = UpdateCoursesOfClassRequestSectionConfigSectionModelsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        if m.get('sectionType') is not None:
            self.section_type = m.get('sectionType')
        if m.get('start') is not None:
            temp_model = UpdateCoursesOfClassRequestSectionConfigSectionModelsStart()
            self.start = temp_model.from_map(m['start'])
        return self


class UpdateCoursesOfClassRequestSectionConfig(TeaModel):
    def __init__(
        self,
        section_models: List[UpdateCoursesOfClassRequestSectionConfigSectionModels] = None,
    ):
        # 节次模型
        self.section_models = section_models

    def validate(self):
        if self.section_models:
            for k in self.section_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['sectionModels'] = []
        if self.section_models is not None:
            for k in self.section_models:
                result['sectionModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.section_models = []
        if m.get('sectionModels') is not None:
            for k in m.get('sectionModels'):
                temp_model = UpdateCoursesOfClassRequestSectionConfigSectionModels()
                self.section_models.append(temp_model.from_map(k))
        return self


class UpdateCoursesOfClassRequest(TeaModel):
    def __init__(
        self,
        courses: List[UpdateCoursesOfClassRequestCourses] = None,
        section_config: UpdateCoursesOfClassRequestSectionConfig = None,
        op_user_id: str = None,
    ):
        self.courses = courses
        # 节次设置
        self.section_config = section_config
        # 操作者id
        self.op_user_id = op_user_id

    def validate(self):
        if self.courses:
            for k in self.courses:
                if k:
                    k.validate()
        if self.section_config:
            self.section_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['courses'] = []
        if self.courses is not None:
            for k in self.courses:
                result['courses'].append(k.to_map() if k else None)
        if self.section_config is not None:
            result['sectionConfig'] = self.section_config.to_map()
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.courses = []
        if m.get('courses') is not None:
            for k in m.get('courses'):
                temp_model = UpdateCoursesOfClassRequestCourses()
                self.courses.append(temp_model.from_map(k))
        if m.get('sectionConfig') is not None:
            temp_model = UpdateCoursesOfClassRequestSectionConfig()
            self.section_config = temp_model.from_map(m['sectionConfig'])
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class UpdateCoursesOfClassResponseBody(TeaModel):
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


class UpdateCoursesOfClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCoursesOfClassResponseBody = None,
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
            temp_model = UpdateCoursesOfClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhysicalClassroomHeaders(TeaModel):
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


class UpdatePhysicalClassroomRequest(TeaModel):
    def __init__(
        self,
        classroom_building: str = None,
        classroom_campus: str = None,
        classroom_floor: str = None,
        classroom_id: int = None,
        classroom_name: str = None,
        classroom_number: str = None,
        direct_broadcast: str = None,
        ext: str = None,
        op_user_id: str = None,
    ):
        # 教室教学楼
        self.classroom_building = classroom_building
        # 教室校区
        self.classroom_campus = classroom_campus
        # 教室楼层
        self.classroom_floor = classroom_floor
        # 教室id
        self.classroom_id = classroom_id
        # 教室名称
        self.classroom_name = classroom_name
        # 教室房间号
        self.classroom_number = classroom_number
        # 是否支持直播
        self.direct_broadcast = direct_broadcast
        # 扩展信息
        self.ext = ext
        # 操作人id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classroom_building is not None:
            result['classroomBuilding'] = self.classroom_building
        if self.classroom_campus is not None:
            result['classroomCampus'] = self.classroom_campus
        if self.classroom_floor is not None:
            result['classroomFloor'] = self.classroom_floor
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.classroom_name is not None:
            result['classroomName'] = self.classroom_name
        if self.classroom_number is not None:
            result['classroomNumber'] = self.classroom_number
        if self.direct_broadcast is not None:
            result['directBroadcast'] = self.direct_broadcast
        if self.ext is not None:
            result['ext'] = self.ext
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classroomBuilding') is not None:
            self.classroom_building = m.get('classroomBuilding')
        if m.get('classroomCampus') is not None:
            self.classroom_campus = m.get('classroomCampus')
        if m.get('classroomFloor') is not None:
            self.classroom_floor = m.get('classroomFloor')
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('classroomName') is not None:
            self.classroom_name = m.get('classroomName')
        if m.get('classroomNumber') is not None:
            self.classroom_number = m.get('classroomNumber')
        if m.get('directBroadcast') is not None:
            self.direct_broadcast = m.get('directBroadcast')
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class UpdatePhysicalClassroomResponseBody(TeaModel):
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


class UpdatePhysicalClassroomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePhysicalClassroomResponseBody = None,
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
            temp_model = UpdatePhysicalClassroomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRemoteClassCourseHeaders(TeaModel):
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


class UpdateRemoteClassCourseRequestAttendParticipants(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        participant_id: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 参与方ID
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        return self


class UpdateRemoteClassCourseRequestTeachingParticipant(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        participant_id: str = None,
    ):
        # 组织ID
        self.corp_id = corp_id
        # 参与方ID
        self.participant_id = participant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.participant_id is not None:
            result['participantId'] = self.participant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('participantId') is not None:
            self.participant_id = m.get('participantId')
        return self


class UpdateRemoteClassCourseRequest(TeaModel):
    def __init__(
        self,
        attend_participants: List[UpdateRemoteClassCourseRequestAttendParticipants] = None,
        auth_code: str = None,
        course_code: str = None,
        course_name: str = None,
        end_time: int = None,
        start_time: int = None,
        teaching_participant: UpdateRemoteClassCourseRequestTeachingParticipant = None,
    ):
        # 听课设备
        self.attend_participants = attend_participants
        self.auth_code = auth_code
        # 课程码
        self.course_code = course_code
        # 课程名称
        self.course_name = course_name
        # 课程结束时间
        self.end_time = end_time
        # 课程开始时间
        self.start_time = start_time
        # 授课设备
        self.teaching_participant = teaching_participant

    def validate(self):
        if self.attend_participants:
            for k in self.attend_participants:
                if k:
                    k.validate()
        if self.teaching_participant:
            self.teaching_participant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendParticipants'] = []
        if self.attend_participants is not None:
            for k in self.attend_participants:
                result['attendParticipants'].append(k.to_map() if k else None)
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.course_code is not None:
            result['courseCode'] = self.course_code
        if self.course_name is not None:
            result['courseName'] = self.course_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.teaching_participant is not None:
            result['teachingParticipant'] = self.teaching_participant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attend_participants = []
        if m.get('attendParticipants') is not None:
            for k in m.get('attendParticipants'):
                temp_model = UpdateRemoteClassCourseRequestAttendParticipants()
                self.attend_participants.append(temp_model.from_map(k))
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('courseCode') is not None:
            self.course_code = m.get('courseCode')
        if m.get('courseName') is not None:
            self.course_name = m.get('courseName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('teachingParticipant') is not None:
            temp_model = UpdateRemoteClassCourseRequestTeachingParticipant()
            self.teaching_participant = temp_model.from_map(m['teachingParticipant'])
        return self


class UpdateRemoteClassCourseResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
        success: bool = None,
    ):
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateRemoteClassCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRemoteClassCourseResponseBody = None,
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
            temp_model = UpdateRemoteClassCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRemoteClassDeviceHeaders(TeaModel):
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


class UpdateRemoteClassDeviceRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        device_code: str = None,
        device_name: str = None,
    ):
        self.auth_code = auth_code
        self.device_code = device_code
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['authCode'] = self.auth_code
        if self.device_code is not None:
            result['deviceCode'] = self.device_code
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCode') is not None:
            self.auth_code = m.get('authCode')
        if m.get('deviceCode') is not None:
            self.device_code = m.get('deviceCode')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        return self


class UpdateRemoteClassDeviceResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # Id of the request
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


class UpdateRemoteClassDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRemoteClassDeviceResponseBody = None,
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
            temp_model = UpdateRemoteClassDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUniversityCourseGroupHeaders(TeaModel):
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


class UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月的第几天
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        month: int = None,
        year: int = None,
    ):
        # 一月的第几天
        self.day_of_month = day_of_month
        # 月
        self.month = month
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class UpdateUniversityCourseGroupRequestCourserGroupItemModels(TeaModel):
    def __init__(
        self,
        class_period_type: int = None,
        classroom_id: int = None,
        course_type: int = None,
        courser_group_item_end_date: UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate = None,
        courser_group_item_start_date: UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate = None,
        day_of_week: int = None,
        section_index: List[int] = None,
    ):
        # 上课周期
        self.class_period_type = class_period_type
        # classroomId
        self.classroom_id = classroom_id
        # 课程类型
        self.course_type = course_type
        # 结束时间
        self.courser_group_item_end_date = courser_group_item_end_date
        # 开始时间
        self.courser_group_item_start_date = courser_group_item_start_date
        # 一周的第几天
        self.day_of_week = day_of_week
        # 课节
        self.section_index = section_index

    def validate(self):
        if self.courser_group_item_end_date:
            self.courser_group_item_end_date.validate()
        if self.courser_group_item_start_date:
            self.courser_group_item_start_date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_period_type is not None:
            result['classPeriodType'] = self.class_period_type
        if self.classroom_id is not None:
            result['classroomId'] = self.classroom_id
        if self.course_type is not None:
            result['courseType'] = self.course_type
        if self.courser_group_item_end_date is not None:
            result['courserGroupItemEndDate'] = self.courser_group_item_end_date.to_map()
        if self.courser_group_item_start_date is not None:
            result['courserGroupItemStartDate'] = self.courser_group_item_start_date.to_map()
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week
        if self.section_index is not None:
            result['sectionIndex'] = self.section_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classPeriodType') is not None:
            self.class_period_type = m.get('classPeriodType')
        if m.get('classroomId') is not None:
            self.classroom_id = m.get('classroomId')
        if m.get('courseType') is not None:
            self.course_type = m.get('courseType')
        if m.get('courserGroupItemEndDate') is not None:
            temp_model = UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemEndDate()
            self.courser_group_item_end_date = temp_model.from_map(m['courserGroupItemEndDate'])
        if m.get('courserGroupItemStartDate') is not None:
            temp_model = UpdateUniversityCourseGroupRequestCourserGroupItemModelsCourserGroupItemStartDate()
            self.courser_group_item_start_date = temp_model.from_map(m['courserGroupItemStartDate'])
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')
        if m.get('sectionIndex') is not None:
            self.section_index = m.get('sectionIndex')
        return self


class UpdateUniversityCourseGroupRequest(TeaModel):
    def __init__(
        self,
        course_group_code: str = None,
        course_group_introduce: str = None,
        course_group_name: str = None,
        courser_group_item_models: List[UpdateUniversityCourseGroupRequestCourserGroupItemModels] = None,
        ext: str = None,
        op_user_id: str = None,
    ):
        # 课程组编码
        self.course_group_code = course_group_code
        # 课程组介绍
        self.course_group_introduce = course_group_introduce
        # 课程组名称
        self.course_group_name = course_group_name
        # 课程组详细
        self.courser_group_item_models = courser_group_item_models
        # 扩展信息
        self.ext = ext
        # opUserId
        self.op_user_id = op_user_id

    def validate(self):
        if self.courser_group_item_models:
            for k in self.courser_group_item_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_group_code is not None:
            result['courseGroupCode'] = self.course_group_code
        if self.course_group_introduce is not None:
            result['courseGroupIntroduce'] = self.course_group_introduce
        if self.course_group_name is not None:
            result['courseGroupName'] = self.course_group_name
        result['courserGroupItemModels'] = []
        if self.courser_group_item_models is not None:
            for k in self.courser_group_item_models:
                result['courserGroupItemModels'].append(k.to_map() if k else None)
        if self.ext is not None:
            result['ext'] = self.ext
        if self.op_user_id is not None:
            result['opUserId'] = self.op_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('courseGroupCode') is not None:
            self.course_group_code = m.get('courseGroupCode')
        if m.get('courseGroupIntroduce') is not None:
            self.course_group_introduce = m.get('courseGroupIntroduce')
        if m.get('courseGroupName') is not None:
            self.course_group_name = m.get('courseGroupName')
        self.courser_group_item_models = []
        if m.get('courserGroupItemModels') is not None:
            for k in m.get('courserGroupItemModels'):
                temp_model = UpdateUniversityCourseGroupRequestCourserGroupItemModels()
                self.courser_group_item_models.append(temp_model.from_map(k))
        if m.get('ext') is not None:
            self.ext = m.get('ext')
        if m.get('opUserId') is not None:
            self.op_user_id = m.get('opUserId')
        return self


class UpdateUniversityCourseGroupResponseBody(TeaModel):
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


class UpdateUniversityCourseGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUniversityCourseGroupResponseBody = None,
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
            temp_model = UpdateUniversityCourseGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


