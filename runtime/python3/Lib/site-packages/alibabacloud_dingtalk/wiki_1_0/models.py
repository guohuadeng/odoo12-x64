# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class WikiWordsDetailHeaders(TeaModel):
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


class WikiWordsDetailRequest(TeaModel):
    def __init__(
        self,
        word_name: str = None,
    ):
        # 传递的词条名称
        self.word_name = word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word_name is not None:
            result['wordName'] = self.word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wordName') is not None:
            self.word_name = m.get('wordName')
        return self


class WikiWordsDetailResponseBodyDataAppLink(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        icon_link: str = None,
        pc_link: str = None,
        phone_link: str = None,
    ):
        # 应用编号
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        # 应用图片链接
        self.icon_link = icon_link
        # 应用PC端链接
        self.pc_link = pc_link
        # 应用手机端链接
        self.phone_link = phone_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.icon_link is not None:
            result['iconLink'] = self.icon_link
        if self.pc_link is not None:
            result['pcLink'] = self.pc_link
        if self.phone_link is not None:
            result['phoneLink'] = self.phone_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('iconLink') is not None:
            self.icon_link = m.get('iconLink')
        if m.get('pcLink') is not None:
            self.pc_link = m.get('pcLink')
        if m.get('phoneLink') is not None:
            self.phone_link = m.get('phoneLink')
        return self


class WikiWordsDetailResponseBodyDataRelatedDoc(TeaModel):
    def __init__(
        self,
        link: str = None,
        name: str = None,
        type: str = None,
    ):
        # 链接
        self.link = link
        # 名称
        self.name = name
        # 文档类型doc或者sheet
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['link'] = self.link
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class WikiWordsDetailResponseBodyDataRelatedLink(TeaModel):
    def __init__(
        self,
        link: str = None,
        name: str = None,
        type: str = None,
    ):
        # 链接
        self.link = link
        # 链接名称
        self.name = name
        # 链接类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['link'] = self.link
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class WikiWordsDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        app_link: List[WikiWordsDetailResponseBodyDataAppLink] = None,
        approve_name: str = None,
        contacts: List[str] = None,
        creator_name: str = None,
        gmt_create: int = None,
        gmt_modify: int = None,
        high_light_word_alias: List[str] = None,
        im_high_light: bool = None,
        org_name: str = None,
        related_doc: List[WikiWordsDetailResponseBodyDataRelatedDoc] = None,
        related_link: List[WikiWordsDetailResponseBodyDataRelatedLink] = None,
        sim_high_light: bool = None,
        simple_word_paraphrase: str = None,
        tags_list: List[str] = None,
        updater_name: str = None,
        uuid: int = None,
        word_alias: List[str] = None,
        word_full_name: str = None,
        word_name: str = None,
        word_paraphrase: str = None,
    ):
        # 应用对象
        self.app_link = app_link
        # 审批人
        self.approve_name = approve_name
        # 联系人
        self.contacts = contacts
        # 创建人
        self.creator_name = creator_name
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        self.high_light_word_alias = high_light_word_alias
        # 内部群是否高亮
        self.im_high_light = im_high_light
        # 组织名称
        self.org_name = org_name
        # 相关文档
        self.related_doc = related_doc
        # 相关链接
        self.related_link = related_link
        # 服务群是否高亮
        self.sim_high_light = sim_high_light
        # 抹除文本格式后的释义
        self.simple_word_paraphrase = simple_word_paraphrase
        # 标签列表
        self.tags_list = tags_list
        # 更新人
        self.updater_name = updater_name
        # 唯一编号
        self.uuid = uuid
        # 别名
        self.word_alias = word_alias
        # 全名
        self.word_full_name = word_full_name
        # 词条名称
        self.word_name = word_name
        # 原始释义(带格式数据的释义）
        self.word_paraphrase = word_paraphrase

    def validate(self):
        if self.app_link:
            for k in self.app_link:
                if k:
                    k.validate()
        if self.related_doc:
            for k in self.related_doc:
                if k:
                    k.validate()
        if self.related_link:
            for k in self.related_link:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['appLink'] = []
        if self.app_link is not None:
            for k in self.app_link:
                result['appLink'].append(k.to_map() if k else None)
        if self.approve_name is not None:
            result['approveName'] = self.approve_name
        if self.contacts is not None:
            result['contacts'] = self.contacts
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmtModify'] = self.gmt_modify
        if self.high_light_word_alias is not None:
            result['highLightWordAlias'] = self.high_light_word_alias
        if self.im_high_light is not None:
            result['imHighLight'] = self.im_high_light
        if self.org_name is not None:
            result['orgName'] = self.org_name
        result['relatedDoc'] = []
        if self.related_doc is not None:
            for k in self.related_doc:
                result['relatedDoc'].append(k.to_map() if k else None)
        result['relatedLink'] = []
        if self.related_link is not None:
            for k in self.related_link:
                result['relatedLink'].append(k.to_map() if k else None)
        if self.sim_high_light is not None:
            result['simHighLight'] = self.sim_high_light
        if self.simple_word_paraphrase is not None:
            result['simpleWordParaphrase'] = self.simple_word_paraphrase
        if self.tags_list is not None:
            result['tagsList'] = self.tags_list
        if self.updater_name is not None:
            result['updaterName'] = self.updater_name
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.word_alias is not None:
            result['wordAlias'] = self.word_alias
        if self.word_full_name is not None:
            result['wordFullName'] = self.word_full_name
        if self.word_name is not None:
            result['wordName'] = self.word_name
        if self.word_paraphrase is not None:
            result['wordParaphrase'] = self.word_paraphrase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_link = []
        if m.get('appLink') is not None:
            for k in m.get('appLink'):
                temp_model = WikiWordsDetailResponseBodyDataAppLink()
                self.app_link.append(temp_model.from_map(k))
        if m.get('approveName') is not None:
            self.approve_name = m.get('approveName')
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModify') is not None:
            self.gmt_modify = m.get('gmtModify')
        if m.get('highLightWordAlias') is not None:
            self.high_light_word_alias = m.get('highLightWordAlias')
        if m.get('imHighLight') is not None:
            self.im_high_light = m.get('imHighLight')
        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')
        self.related_doc = []
        if m.get('relatedDoc') is not None:
            for k in m.get('relatedDoc'):
                temp_model = WikiWordsDetailResponseBodyDataRelatedDoc()
                self.related_doc.append(temp_model.from_map(k))
        self.related_link = []
        if m.get('relatedLink') is not None:
            for k in m.get('relatedLink'):
                temp_model = WikiWordsDetailResponseBodyDataRelatedLink()
                self.related_link.append(temp_model.from_map(k))
        if m.get('simHighLight') is not None:
            self.sim_high_light = m.get('simHighLight')
        if m.get('simpleWordParaphrase') is not None:
            self.simple_word_paraphrase = m.get('simpleWordParaphrase')
        if m.get('tagsList') is not None:
            self.tags_list = m.get('tagsList')
        if m.get('updaterName') is not None:
            self.updater_name = m.get('updaterName')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('wordAlias') is not None:
            self.word_alias = m.get('wordAlias')
        if m.get('wordFullName') is not None:
            self.word_full_name = m.get('wordFullName')
        if m.get('wordName') is not None:
            self.word_name = m.get('wordName')
        if m.get('wordParaphrase') is not None:
            self.word_paraphrase = m.get('wordParaphrase')
        return self


class WikiWordsDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: List[WikiWordsDetailResponseBodyData] = None,
        err_msg: str = None,
        success: bool = None,
    ):
        # 返回的参数
        self.data = data
        # 返回的错误信息
        self.err_msg = err_msg
        # 查询是否成功
        self.success = success

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
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = WikiWordsDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WikiWordsDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WikiWordsDetailResponseBody = None,
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
            temp_model = WikiWordsDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WikiWordsParseHeaders(TeaModel):
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


class WikiWordsParseRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 消息体以及文章内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class WikiWordsParseResponseBodyData(TeaModel):
    def __init__(
        self,
        end_index: int = None,
        start_index: int = None,
        word_name: str = None,
    ):
        self.end_index = end_index
        self.start_index = start_index
        self.word_name = word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_index is not None:
            result['endIndex'] = self.end_index
        if self.start_index is not None:
            result['startIndex'] = self.start_index
        if self.word_name is not None:
            result['wordName'] = self.word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endIndex') is not None:
            self.end_index = m.get('endIndex')
        if m.get('startIndex') is not None:
            self.start_index = m.get('startIndex')
        if m.get('wordName') is not None:
            self.word_name = m.get('wordName')
        return self


class WikiWordsParseResponseBody(TeaModel):
    def __init__(
        self,
        data: List[WikiWordsParseResponseBodyData] = None,
        err_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_msg = err_msg
        # Id of the request
        self.success = success

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
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = WikiWordsParseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class WikiWordsParseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WikiWordsParseResponseBody = None,
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
            temp_model = WikiWordsParseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


