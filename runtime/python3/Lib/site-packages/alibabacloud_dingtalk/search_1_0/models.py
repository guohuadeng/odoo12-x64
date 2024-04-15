# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BatchInsertSearchItemHeaders(TeaModel):
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


class BatchInsertSearchItemRequestSearchItemModels(TeaModel):
    def __init__(
        self,
        footer: str = None,
        icon: str = None,
        item_id: str = None,
        mobile_url: str = None,
        pc_url: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        # 数据项的脚注，长度不能超过64
        self.footer = footer
        # 数据项的头像，长度不能超过512
        self.icon = icon
        # 数据项的id，tabId和orgId相同的情况下，itemId唯一标识一条数据项，长度不能超过128
        self.item_id = item_id
        # 数据项的移动端跳转url地址，若同时配置默认url和mobileUrl，移动端跳转链接优先使用mobileUrl
        self.mobile_url = mobile_url
        # 数据项的PC端跳转url地址，若同时配置默认url和pcUrl，PC端跳转链接优先使用pcUrl
        self.pc_url = pc_url
        # 数据项的摘要，长度不能超过64
        self.summary = summary
        # 数据项的标题，长度不能超过16
        self.title = title
        # 数据项的默认url地址，若mobileUrl或pcUrl没有配置，则使用该url地址，默认url和mobileUrl、pcUrl至少配置其中一个
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.footer is not None:
            result['footer'] = self.footer
        if self.icon is not None:
            result['icon'] = self.icon
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('footer') is not None:
            self.footer = m.get('footer')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class BatchInsertSearchItemRequest(TeaModel):
    def __init__(
        self,
        search_item_models: List[BatchInsertSearchItemRequestSearchItemModels] = None,
    ):
        self.search_item_models = search_item_models

    def validate(self):
        if self.search_item_models:
            for k in self.search_item_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['searchItemModels'] = []
        if self.search_item_models is not None:
            for k in self.search_item_models:
                result['searchItemModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_item_models = []
        if m.get('searchItemModels') is not None:
            for k in m.get('searchItemModels'):
                temp_model = BatchInsertSearchItemRequestSearchItemModels()
                self.search_item_models.append(temp_model.from_map(k))
        return self


class BatchInsertSearchItemResponse(TeaModel):
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


class CreateSearchTabHeaders(TeaModel):
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


class CreateSearchTabRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        priority: int = None,
        status: int = None,
    ):
        # 数据源名称
        self.name = name
        # 数据源优先级，数值越小优先级越高
        self.priority = priority
        # 数据源状态，1表示上线，0表示下线
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateSearchTabResponseBody(TeaModel):
    def __init__(
        self,
        tab_id: int = None,
    ):
        # 数据源的id,范围为3000-4000
        self.tab_id = tab_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tab_id is not None:
            result['tabId'] = self.tab_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tabId') is not None:
            self.tab_id = m.get('tabId')
        return self


class CreateSearchTabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSearchTabResponseBody = None,
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
            temp_model = CreateSearchTabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSearchItemHeaders(TeaModel):
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


class DeleteSearchItemResponse(TeaModel):
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


class DeleteSearchTabHeaders(TeaModel):
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


class DeleteSearchTabResponse(TeaModel):
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


class GetSearchItemHeaders(TeaModel):
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


class GetSearchItemResponseBody(TeaModel):
    def __init__(
        self,
        footer: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon: str = None,
        item_id: str = None,
        mobile_url: str = None,
        pc_url: str = None,
        summary: str = None,
        tab_id: int = None,
        title: str = None,
        url: str = None,
    ):
        # 数据项的脚注
        self.footer = footer
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据项的头像
        self.icon = icon
        # 数据项的id,tabId和orgId相同的情况下，itemId唯一标识一条数据项
        self.item_id = item_id
        # 数据项的移动端跳转url地址，若同时配置默认url和mobileUrl，移动端跳转链接优先使用mobileUrl
        self.mobile_url = mobile_url
        # 数据项的PC端跳转url地址，若同时配置默认url和pcUrl，PC端跳转链接优先使用pcUrl
        self.pc_url = pc_url
        # 数据项的摘要
        self.summary = summary
        # 数据源id
        self.tab_id = tab_id
        # 数据项的标题
        self.title = title
        # 数据项的默认url地址，若mobileUrl或pcUrl没有配置，则使用该url地址，默认url和mobileUrl、pcUrl至少配置其中一个
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.footer is not None:
            result['footer'] = self.footer
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['icon'] = self.icon
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.summary is not None:
            result['summary'] = self.summary
        if self.tab_id is not None:
            result['tabId'] = self.tab_id
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('footer') is not None:
            self.footer = m.get('footer')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('tabId') is not None:
            self.tab_id = m.get('tabId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetSearchItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSearchItemResponseBody = None,
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
            temp_model = GetSearchItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSearchItemsByKeyWordHeaders(TeaModel):
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


class GetSearchItemsByKeyWordRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 搜索关键词
        self.key_word = key_word
        # 一次性请求的item数量
        self.max_results = max_results
        # 加密偏移量，第一次请求取“0”值，后续请求根据接口返回的nextToken值进行填写
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['keyWord'] = self.key_word
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyWord') is not None:
            self.key_word = m.get('keyWord')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class GetSearchItemsByKeyWordResponseBodyValue(TeaModel):
    def __init__(
        self,
        footer: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon: str = None,
        item_id: str = None,
        mobile_url: str = None,
        pc_url: str = None,
        summary: str = None,
        tab_id: int = None,
        title: str = None,
        url: str = None,
    ):
        # 数据项的脚注
        self.footer = footer
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据项的头像
        self.icon = icon
        # 数据项的id,tabId和orgId相同的情况下，itemId唯一标识一条数据项
        self.item_id = item_id
        # 数据项的移动端跳转url地址，若同时配置默认url和mobileUrl，移动端跳转链接优先使用mobileUrl
        self.mobile_url = mobile_url
        # 数据项的PC端跳转url地址，若同时配置默认url和pcUrl，PC端跳转链接优先使用pcUrl
        self.pc_url = pc_url
        # 数据项的摘要
        self.summary = summary
        # 数据源id
        self.tab_id = tab_id
        # 数据项的标题
        self.title = title
        # 数据项的默认url地址，若mobileUrl或pcUrl没有配置，则使用该url地址，默认url和mobileUrl、pcUrl至少配置其中一个
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.footer is not None:
            result['footer'] = self.footer
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['icon'] = self.icon
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.summary is not None:
            result['summary'] = self.summary
        if self.tab_id is not None:
            result['tabId'] = self.tab_id
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('footer') is not None:
            self.footer = m.get('footer')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('tabId') is not None:
            self.tab_id = m.get('tabId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetSearchItemsByKeyWordResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        total_count: int = None,
        value: List[GetSearchItemsByKeyWordResponseBodyValue] = None,
    ):
        # 下一次请求的加密offset，若为空则代表item已经读取完毕
        self.next_token = next_token
        # 本次请求条件下的item总量
        self.total_count = total_count
        self.value = value

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['value'] = []
        if self.value is not None:
            for k in self.value:
                result['value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.value = []
        if m.get('value') is not None:
            for k in m.get('value'):
                temp_model = GetSearchItemsByKeyWordResponseBodyValue()
                self.value.append(temp_model.from_map(k))
        return self


class GetSearchItemsByKeyWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSearchItemsByKeyWordResponseBody = None,
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
            temp_model = GetSearchItemsByKeyWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSearchTabHeaders(TeaModel):
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


class GetSearchTabResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        priority: int = None,
        status: int = None,
        tab_id: int = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据源名称
        self.name = name
        # 数据源优先级，数值越小优先级越高
        self.priority = priority
        # 数据源状态，1表示上线，0表示下线
        self.status = status
        # 数据源的id,范围为3000-4000
        self.tab_id = tab_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.name is not None:
            result['name'] = self.name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.status is not None:
            result['status'] = self.status
        if self.tab_id is not None:
            result['tabId'] = self.tab_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tabId') is not None:
            self.tab_id = m.get('tabId')
        return self


class GetSearchTabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSearchTabResponseBody = None,
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
            temp_model = GetSearchTabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertSearchItemHeaders(TeaModel):
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


class InsertSearchItemRequest(TeaModel):
    def __init__(
        self,
        footer: str = None,
        icon: str = None,
        item_id: str = None,
        mobile_url: str = None,
        pc_url: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        # 数据项的脚注，长度不能超过64
        self.footer = footer
        # 数据项的头像，长度不能超过512
        self.icon = icon
        # 数据项的id，tabId和orgId相同的情况下，itemId唯一标识一条数据项，长度不能超过128
        self.item_id = item_id
        # 数据项的移动端跳转url地址，若同时配置默认url和mobileUrl，移动端跳转链接优先使用mobileUrl
        self.mobile_url = mobile_url
        # 数据项的PC端跳转url地址，若同时配置默认url和pcUrl，PC端跳转链接优先使用pcUrl
        self.pc_url = pc_url
        # 数据项的摘要，长度不能超过64
        self.summary = summary
        # 数据项的标题，长度不能超过16
        self.title = title
        # 数据项的默认url地址，若mobileUrl或pcUrl没有配置，则使用该url地址，默认url和mobileUrl、pcUrl至少配置其中一个
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.footer is not None:
            result['footer'] = self.footer
        if self.icon is not None:
            result['icon'] = self.icon
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.mobile_url is not None:
            result['mobileUrl'] = self.mobile_url
        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('footer') is not None:
            self.footer = m.get('footer')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('mobileUrl') is not None:
            self.mobile_url = m.get('mobileUrl')
        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class InsertSearchItemResponse(TeaModel):
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


class ListSearchTabsByOrgIdHeaders(TeaModel):
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


class ListSearchTabsByOrgIdResponseBodySearchTabResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        priority: int = None,
        status: int = None,
        tab_id: int = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据源名称
        self.name = name
        # 数据源优先级，数值越小优先级越高
        self.priority = priority
        # 数据源状态，1表示上线，0表示下线
        self.status = status
        # 数据源的id,范围为3000-4000
        self.tab_id = tab_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.name is not None:
            result['name'] = self.name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.status is not None:
            result['status'] = self.status
        if self.tab_id is not None:
            result['tabId'] = self.tab_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tabId') is not None:
            self.tab_id = m.get('tabId')
        return self


class ListSearchTabsByOrgIdResponseBody(TeaModel):
    def __init__(
        self,
        search_tab_result: List[ListSearchTabsByOrgIdResponseBodySearchTabResult] = None,
    ):
        # 该企业拥有的所有数据源信息
        self.search_tab_result = search_tab_result

    def validate(self):
        if self.search_tab_result:
            for k in self.search_tab_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['searchTabResult'] = []
        if self.search_tab_result is not None:
            for k in self.search_tab_result:
                result['searchTabResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_tab_result = []
        if m.get('searchTabResult') is not None:
            for k in m.get('searchTabResult'):
                temp_model = ListSearchTabsByOrgIdResponseBodySearchTabResult()
                self.search_tab_result.append(temp_model.from_map(k))
        return self


class ListSearchTabsByOrgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSearchTabsByOrgIdResponseBody = None,
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
            temp_model = ListSearchTabsByOrgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSearchTabHeaders(TeaModel):
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


class UpdateSearchTabRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        priority: int = None,
        status: int = None,
    ):
        # 数据源名称
        self.name = name
        # 数据源优先级，数值越小优先级越高
        self.priority = priority
        # 数据源状态，1表示上线，0表示下线
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateSearchTabResponse(TeaModel):
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


