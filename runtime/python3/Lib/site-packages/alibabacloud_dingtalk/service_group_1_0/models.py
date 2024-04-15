# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddKnowledgeHeaders(TeaModel):
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


class AddKnowledgeRequestAttachmentList(TeaModel):
    def __init__(
        self,
        mime_type: str = None,
        path: str = None,
        size: int = None,
        suffix: str = None,
        title: str = None,
    ):
        # 多媒体类型
        self.mime_type = mime_type
        # 附件URL
        self.path = path
        # 附件大小
        self.size = size
        # 附件扩展名
        self.suffix = suffix
        # 附件名称
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mime_type is not None:
            result['mime_type'] = self.mime_type
        if self.path is not None:
            result['path'] = self.path
        if self.size is not None:
            result['size'] = self.size
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mime_type') is not None:
            self.mime_type = m.get('mime_type')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class AddKnowledgeRequest(TeaModel):
    def __init__(
        self,
        attachment_list: List[AddKnowledgeRequestAttachmentList] = None,
        content: str = None,
        ext_title: str = None,
        keyword: str = None,
        library_key: str = None,
        link_url: str = None,
        open_team_id: str = None,
        source: str = None,
        source_primary_key: str = None,
        title: str = None,
        type: str = None,
        version: str = None,
    ):
        # 附件列表
        self.attachment_list = attachment_list
        # 知识点内容
        self.content = content
        # 知识点扩展问(多个用英文逗号隔开)
        self.ext_title = ext_title
        # 关键字(多个用英文逗号隔开)
        self.keyword = keyword
        # 知识库的唯一标识
        self.library_key = library_key
        # CCM的知识点外链
        self.link_url = link_url
        # 开放团队ID
        self.open_team_id = open_team_id
        # 知识点来源
        self.source = source
        # 知识点唯一标识
        self.source_primary_key = source_primary_key
        # 知识点名称
        self.title = title
        # 知识点类型 NORMAL：普通型 CARD：卡片 CONDITION：条件
        self.type = type
        # 知识点版本号
        self.version = version

    def validate(self):
        if self.attachment_list:
            for k in self.attachment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachmentList'] = []
        if self.attachment_list is not None:
            for k in self.attachment_list:
                result['attachmentList'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.ext_title is not None:
            result['extTitle'] = self.ext_title
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.library_key is not None:
            result['libraryKey'] = self.library_key
        if self.link_url is not None:
            result['linkUrl'] = self.link_url
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.source is not None:
            result['source'] = self.source
        if self.source_primary_key is not None:
            result['sourcePrimaryKey'] = self.source_primary_key
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachment_list = []
        if m.get('attachmentList') is not None:
            for k in m.get('attachmentList'):
                temp_model = AddKnowledgeRequestAttachmentList()
                self.attachment_list.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extTitle') is not None:
            self.ext_title = m.get('extTitle')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('libraryKey') is not None:
            self.library_key = m.get('libraryKey')
        if m.get('linkUrl') is not None:
            self.link_url = m.get('linkUrl')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePrimaryKey') is not None:
            self.source_primary_key = m.get('sourcePrimaryKey')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class AddKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        open_knowledge_id: str = None,
    ):
        # 开放知识点ID
        self.open_knowledge_id = open_knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_knowledge_id is not None:
            result['openKnowledgeId'] = self.open_knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openKnowledgeId') is not None:
            self.open_knowledge_id = m.get('openKnowledgeId')
        return self


class AddKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddKnowledgeResponseBody = None,
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
            temp_model = AddKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLibraryHeaders(TeaModel):
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


class AddLibraryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        open_team_ids: List[str] = None,
        source: str = None,
        source_primary_key: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # 知识库描述
        self.description = description
        # 团队id列表
        self.open_team_ids = open_team_ids
        # 知识来源
        self.source = source
        # 知识库的唯一性标识
        self.source_primary_key = source_primary_key
        # 知识库名称
        self.title = title
        # 知识库类型 INTERNAL:内部知识库 EXTERNAL:外部知识库
        self.type = type
        # 员工ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.open_team_ids is not None:
            result['openTeamIds'] = self.open_team_ids
        if self.source is not None:
            result['source'] = self.source
        if self.source_primary_key is not None:
            result['sourcePrimaryKey'] = self.source_primary_key
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('openTeamIds') is not None:
            self.open_team_ids = m.get('openTeamIds')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePrimaryKey') is not None:
            self.source_primary_key = m.get('sourcePrimaryKey')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AddLibraryResponseBody(TeaModel):
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


class AddLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddLibraryResponseBody = None,
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
            temp_model = AddLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOpenCategoryHeaders(TeaModel):
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


class AddOpenCategoryRequest(TeaModel):
    def __init__(
        self,
        library_id: int = None,
        open_team_id: str = None,
        parent_id: int = None,
        title: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 所属知识库ID
        self.library_id = library_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 父类目ID(为0代表顶层id)
        self.parent_id = parent_id
        # 类目标题
        self.title = title
        # 员工/用户ID
        self.user_id = user_id
        # 用户昵称或姓名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class AddOpenCategoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: int = None,
        message: str = None,
        success: bool = None,
    ):
        # 添加成类目ID
        self.id = id
        # 失败时的错误消息
        self.message = message
        # 操作是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenCategoryResponseBody(TeaModel):
    def __init__(
        self,
        result: AddOpenCategoryResponseBodyResult = None,
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
            temp_model = AddOpenCategoryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOpenCategoryResponseBody = None,
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
            temp_model = AddOpenCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOpenKnowledgeHeaders(TeaModel):
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


class AddOpenKnowledgeRequestAttachments(TeaModel):
    def __init__(
        self,
        mime_type: str = None,
        path: str = None,
        size: float = None,
        suffix: str = None,
        title: str = None,
    ):
        # 媒体类型(扩展名大写)
        self.mime_type = mime_type
        # 附件URL
        self.path = path
        # 附件大小
        self.size = size
        # 扩展名
        self.suffix = suffix
        # 附件名称
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mime_type is not None:
            result['mimeType'] = self.mime_type
        if self.path is not None:
            result['path'] = self.path
        if self.size is not None:
            result['size'] = self.size
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class AddOpenKnowledgeRequest(TeaModel):
    def __init__(
        self,
        attachments: List[AddOpenKnowledgeRequestAttachments] = None,
        category_id: int = None,
        content: str = None,
        effect_timeend: str = None,
        effect_timestart: str = None,
        ext_title: str = None,
        keyword: str = None,
        library_id: int = None,
        open_team_id: str = None,
        source: str = None,
        tags: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 附件列表
        self.attachments = attachments
        # 知识点所属类目ID
        self.category_id = category_id
        # 知识点正文
        self.content = content
        # 生效结束时间(默认2100-01-01 23:59:59)
        self.effect_timeend = effect_timeend
        # 生效开始时间(默认1980-01-01 00:00:00)
        self.effect_timestart = effect_timestart
        # 扩展问法(多个英文逗号隔开)
        self.ext_title = ext_title
        # 关键词(多个逗号隔开)
        self.keyword = keyword
        # 所属知识库唯一标识id
        self.library_id = library_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 知识点来源
        self.source = source
        # 标签(多个可逗号隔开)
        self.tags = tags
        # 知识点标准问
        self.title = title
        # 知识点类型()
        self.type = type
        # 用户/员工ID
        self.user_id = user_id
        # 用户昵称或姓名
        self.user_name = user_name

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['categoryId'] = self.category_id
        if self.content is not None:
            result['content'] = self.content
        if self.effect_timeend is not None:
            result['effectTimeend'] = self.effect_timeend
        if self.effect_timestart is not None:
            result['effectTimestart'] = self.effect_timestart
        if self.ext_title is not None:
            result['extTitle'] = self.ext_title
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.source is not None:
            result['source'] = self.source
        if self.tags is not None:
            result['tags'] = self.tags
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = AddOpenKnowledgeRequestAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('effectTimeend') is not None:
            self.effect_timeend = m.get('effectTimeend')
        if m.get('effectTimestart') is not None:
            self.effect_timestart = m.get('effectTimestart')
        if m.get('extTitle') is not None:
            self.ext_title = m.get('extTitle')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class AddOpenKnowledgeResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: int = None,
        message: str = None,
        success: bool = None,
    ):
        # 知识点ID
        self.id = id
        # 失败错误消息
        self.message = message
        # 操作是否成功标识
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        result: AddOpenKnowledgeResponseBodyResult = None,
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
            temp_model = AddOpenKnowledgeResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOpenKnowledgeResponseBody = None,
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
            temp_model = AddOpenKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOpenLibraryHeaders(TeaModel):
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


class AddOpenLibraryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        open_team_id: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 知识库描述
        self.description = description
        # 开放团队ID
        self.open_team_id = open_team_id
        # 知识库来源
        self.source = source
        # 知识库名称
        self.title = title
        # 知识库类型
        self.type = type
        # 用户/员工ID
        self.user_id = user_id
        # 用户昵称或姓名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.source is not None:
            result['source'] = self.source
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class AddOpenLibraryResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: int = None,
        message: str = None,
        success: bool = None,
    ):
        # 知识库ID
        self.id = id
        # 失败时错误消息
        self.message = message
        # 添加/修改知识库是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenLibraryResponseBody(TeaModel):
    def __init__(
        self,
        result: AddOpenLibraryResponseBodyResult = None,
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
            temp_model = AddOpenLibraryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddOpenLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOpenLibraryResponseBody = None,
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
            temp_model = AddOpenLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTicketMemoHeaders(TeaModel):
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


class AddTicketMemoRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class AddTicketMemoRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[AddTicketMemoRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 文字备注
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = AddTicketMemoRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class AddTicketMemoRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
        processor_union_id: str = None,
        ticket_memo: AddTicketMemoRequestTicketMemo = None,
    ):
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 当前工单处理人
        self.processor_union_id = processor_union_id
        # 备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor_union_id is not None:
            result['processorUnionId'] = self.processor_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processorUnionId') is not None:
            self.processor_union_id = m.get('processorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = AddTicketMemoRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class AddTicketMemoResponse(TeaModel):
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


class AssignTicketHeaders(TeaModel):
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


class AssignTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class AssignTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class AssignTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[AssignTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 备注文字
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = AssignTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class AssignTicketRequest(TeaModel):
    def __init__(
        self,
        notify: AssignTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        operator_union_id: str = None,
        processor_union_ids: List[str] = None,
        ticket_memo: AssignTicketRequestTicketMemo = None,
    ):
        self.notify = notify
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 操作人unionId（管理员）
        self.operator_union_id = operator_union_id
        self.processor_union_ids = processor_union_ids
        # 备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.operator_union_id is not None:
            result['operatorUnionId'] = self.operator_union_id
        if self.processor_union_ids is not None:
            result['processorUnionIds'] = self.processor_union_ids
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notify') is not None:
            temp_model = AssignTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('operatorUnionId') is not None:
            self.operator_union_id = m.get('operatorUnionId')
        if m.get('processorUnionIds') is not None:
            self.processor_union_ids = m.get('processorUnionIds')
        if m.get('ticketMemo') is not None:
            temp_model = AssignTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class AssignTicketResponse(TeaModel):
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


class BatchGetGroupSetConfigHeaders(TeaModel):
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


class BatchGetGroupSetConfigRequest(TeaModel):
    def __init__(
        self,
        config_keys: List[str] = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
    ):
        # 配置项key列表
        self.config_keys = config_keys
        # 开放群组id
        self.open_group_set_id = open_group_set_id
        # 开放团队id
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_keys is not None:
            result['configKeys'] = self.config_keys
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configKeys') is not None:
            self.config_keys = m.get('configKeys')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class BatchGetGroupSetConfigResponseBodyGroupSetConfigs(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
    ):
        # 配置项key
        self.config_key = config_key
        # 配置项值
        self.config_value = config_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['configKey'] = self.config_key
        if self.config_value is not None:
            result['configValue'] = self.config_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        return self


class BatchGetGroupSetConfigResponseBody(TeaModel):
    def __init__(
        self,
        group_set_configs: List[BatchGetGroupSetConfigResponseBodyGroupSetConfigs] = None,
    ):
        # 群粗配置列表
        self.group_set_configs = group_set_configs

    def validate(self):
        if self.group_set_configs:
            for k in self.group_set_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['groupSetConfigs'] = []
        if self.group_set_configs is not None:
            for k in self.group_set_configs:
                result['groupSetConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_set_configs = []
        if m.get('groupSetConfigs') is not None:
            for k in m.get('groupSetConfigs'):
                temp_model = BatchGetGroupSetConfigResponseBodyGroupSetConfigs()
                self.group_set_configs.append(temp_model.from_map(k))
        return self


class BatchGetGroupSetConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchGetGroupSetConfigResponseBody = None,
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
            temp_model = BatchGetGroupSetConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BoundTemplateToTeamHeaders(TeaModel):
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


class BoundTemplateToTeamRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        robot_config: str = None,
        template_desc: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # 目标团队id
        self.open_team_id = open_team_id
        # 模板中的机器人配置信息
        self.robot_config = robot_config
        # 模板描述信息
        self.template_desc = template_desc
        # 模板id
        self.template_id = template_id
        # 模板名字
        self.template_name = template_name
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.robot_config is not None:
            result['robotConfig'] = self.robot_config
        if self.template_desc is not None:
            result['templateDesc'] = self.template_desc
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_type is not None:
            result['templateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('robotConfig') is not None:
            self.robot_config = m.get('robotConfig')
        if m.get('templateDesc') is not None:
            self.template_desc = m.get('templateDesc')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        return self


class BoundTemplateToTeamResponseBody(TeaModel):
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


class BoundTemplateToTeamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BoundTemplateToTeamResponseBody = None,
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
            temp_model = BoundTemplateToTeamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTicketHeaders(TeaModel):
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


class CancelTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class CancelTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class CancelTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[CancelTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        # 备注
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = CancelTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class CancelTicketRequest(TeaModel):
    def __init__(
        self,
        notify: CancelTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        operator_union_id: str = None,
        ticket_memo: CancelTicketRequestTicketMemo = None,
    ):
        self.notify = notify
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 操作人unionId
        self.operator_union_id = operator_union_id
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.operator_union_id is not None:
            result['operatorUnionId'] = self.operator_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notify') is not None:
            temp_model = CancelTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('operatorUnionId') is not None:
            self.operator_union_id = m.get('operatorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = CancelTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class CancelTicketResponse(TeaModel):
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


class CloseHumanSessionHeaders(TeaModel):
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


class CloseHumanSessionRequest(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        open_team_id: str = None,
    ):
        # 开放会话id
        self.open_conversation_id = open_conversation_id
        # 开放团队id
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class CloseHumanSessionResponseBody(TeaModel):
    def __init__(
        self,
        session_id: int = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CloseHumanSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseHumanSessionResponseBody = None,
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
            temp_model = CloseHumanSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupHeaders(TeaModel):
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


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        group_biz_id: str = None,
        group_name: str = None,
        group_tag_names: List[str] = None,
        member_staff_ids: List[str] = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        owner_staff_id: str = None,
    ):
        # 业务关联id
        self.group_biz_id = group_biz_id
        # 群名称
        self.group_name = group_name
        # 群标签
        self.group_tag_names = group_tag_names
        # 群成员员工ID列表
        self.member_staff_ids = member_staff_ids
        # 开放群组ID
        self.open_group_set_id = open_group_set_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 群主员工ID
        self.owner_staff_id = owner_staff_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_biz_id is not None:
            result['groupBizId'] = self.group_biz_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_tag_names is not None:
            result['groupTagNames'] = self.group_tag_names
        if self.member_staff_ids is not None:
            result['memberStaffIds'] = self.member_staff_ids
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.owner_staff_id is not None:
            result['ownerStaffId'] = self.owner_staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupBizId') is not None:
            self.group_biz_id = m.get('groupBizId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupTagNames') is not None:
            self.group_tag_names = m.get('groupTagNames')
        if m.get('memberStaffIds') is not None:
            self.member_staff_ids = m.get('memberStaffIds')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('ownerStaffId') is not None:
            self.owner_staff_id = m.get('ownerStaffId')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_url: str = None,
        open_conversation_id: str = None,
    ):
        # 入群url
        self.group_url = group_url
        # 开放群ID
        self.open_conversation_id = open_conversation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_url is not None:
            result['groupUrl'] = self.group_url
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupUrl') is not None:
            self.group_url = m.get('groupUrl')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupSetHeaders(TeaModel):
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


class CreateGroupSetRequest(TeaModel):
    def __init__(
        self,
        group_set_name: str = None,
        group_template_id: str = None,
        open_team_id: str = None,
    ):
        # groupSetName
        self.group_set_name = group_set_name
        self.group_template_id = group_template_id
        # openTeamId
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_set_name is not None:
            result['groupSetName'] = self.group_set_name
        if self.group_template_id is not None:
            result['groupTemplateId'] = self.group_template_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupSetName') is not None:
            self.group_set_name = m.get('groupSetName')
        if m.get('groupTemplateId') is not None:
            self.group_template_id = m.get('groupTemplateId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class CreateGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 群分组id
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


class CreateGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupSetResponseBody = None,
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
            temp_model = CreateGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTeamHeaders(TeaModel):
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


class CreateTeamRequest(TeaModel):
    def __init__(
        self,
        creator_ding_union_id: str = None,
        team_name: str = None,
    ):
        # 团队管理员钉钉unionId
        self.creator_ding_union_id = creator_ding_union_id
        # 团队名字
        self.team_name = team_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_ding_union_id is not None:
            result['creatorDingUnionId'] = self.creator_ding_union_id
        if self.team_name is not None:
            result['teamName'] = self.team_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorDingUnionId') is not None:
            self.creator_ding_union_id = m.get('creatorDingUnionId')
        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')
        return self


class CreateTeamResponseBody(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        # 团队id
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


class CreateTeamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTeamResponseBody = None,
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
            temp_model = CreateTeamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketHeaders(TeaModel):
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


class CreateTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        # 服务群通知接收人（钉钉UnionId）
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        # 企业工作通知接收人（钉钉UnionId）
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class CreateTicketRequestSceneContextGroupMsgs(TeaModel):
    def __init__(
        self,
        anchor: bool = None,
        open_msg_id: str = None,
    ):
        # 是否为锚点消息
        self.anchor = anchor
        # 勾选消息openMsgId
        self.open_msg_id = open_msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor is not None:
            result['anchor'] = self.anchor
        if self.open_msg_id is not None:
            result['openMsgId'] = self.open_msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchor') is not None:
            self.anchor = m.get('anchor')
        if m.get('openMsgId') is not None:
            self.open_msg_id = m.get('openMsgId')
        return self


class CreateTicketRequestSceneContext(TeaModel):
    def __init__(
        self,
        group_msgs: List[CreateTicketRequestSceneContextGroupMsgs] = None,
        open_conversation_id: str = None,
        relevantor_union_ids: List[str] = None,
        topic_id: str = None,
    ):
        # 工单相关的群消息列表
        self.group_msgs = group_msgs
        # 服务群openConversationId
        self.open_conversation_id = open_conversation_id
        # 工单相关人UnionId列表
        self.relevantor_union_ids = relevantor_union_ids
        # VOC类型工单，对应话题ID
        self.topic_id = topic_id

    def validate(self):
        if self.group_msgs:
            for k in self.group_msgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['groupMsgs'] = []
        if self.group_msgs is not None:
            for k in self.group_msgs:
                result['groupMsgs'].append(k.to_map() if k else None)
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.relevantor_union_ids is not None:
            result['relevantorUnionIds'] = self.relevantor_union_ids
        if self.topic_id is not None:
            result['topicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_msgs = []
        if m.get('groupMsgs') is not None:
            for k in m.get('groupMsgs'):
                temp_model = CreateTicketRequestSceneContextGroupMsgs()
                self.group_msgs.append(temp_model.from_map(k))
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('relevantorUnionIds') is not None:
            self.relevantor_union_ids = m.get('relevantorUnionIds')
        if m.get('topicId') is not None:
            self.topic_id = m.get('topicId')
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        creator_union_id: str = None,
        custom_fields: str = None,
        notify: CreateTicketRequestNotify = None,
        open_team_id: str = None,
        open_template_biz_id: str = None,
        processor_union_ids: List[str] = None,
        scene: str = None,
        scene_context: CreateTicketRequestSceneContext = None,
        title: str = None,
    ):
        # 工单创建人UnionId
        self.creator_union_id = creator_union_id
        # 自定义组件字段值(JSON格式)
        self.custom_fields = custom_fields
        # 通知接收人配置
        self.notify = notify
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单模板业务ID
        self.open_template_biz_id = open_template_biz_id
        # 工单处理人UnionId列表
        self.processor_union_ids = processor_union_ids
        # 工单场景 SG 或 VOC
        self.scene = scene
        # 工单场景信息
        self.scene_context = scene_context
        # 工单标题
        self.title = title

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.scene_context:
            self.scene_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_union_id is not None:
            result['creatorUnionId'] = self.creator_union_id
        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_template_biz_id is not None:
            result['openTemplateBizId'] = self.open_template_biz_id
        if self.processor_union_ids is not None:
            result['processorUnionIds'] = self.processor_union_ids
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_context is not None:
            result['sceneContext'] = self.scene_context.to_map()
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorUnionId') is not None:
            self.creator_union_id = m.get('creatorUnionId')
        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')
        if m.get('notify') is not None:
            temp_model = CreateTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTemplateBizId') is not None:
            self.open_template_biz_id = m.get('openTemplateBizId')
        if m.get('processorUnionIds') is not None:
            self.processor_union_ids = m.get('processorUnionIds')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneContext') is not None:
            temp_model = CreateTicketRequestSceneContext()
            self.scene_context = temp_model.from_map(m['sceneContext'])
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        open_ticket_id: str = None,
    ):
        # 工单开放ID
        self.open_ticket_id = open_ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTicketResponseBody = None,
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKnowledgeHeaders(TeaModel):
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


class DeleteKnowledgeRequest(TeaModel):
    def __init__(
        self,
        library_key: str = None,
        open_team_id: str = None,
        source: str = None,
        source_primary_key: str = None,
    ):
        # 知识库的唯一标识 比如:天工知识库ID
        self.library_key = library_key
        # 开放团队ID
        self.open_team_id = open_team_id
        # 知识点来源 CCM:天工知识库
        self.source = source
        # 知识点唯一标识
        self.source_primary_key = source_primary_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_key is not None:
            result['libraryKey'] = self.library_key
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.source is not None:
            result['source'] = self.source
        if self.source_primary_key is not None:
            result['sourcePrimaryKey'] = self.source_primary_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryKey') is not None:
            self.library_key = m.get('libraryKey')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePrimaryKey') is not None:
            self.source_primary_key = m.get('sourcePrimaryKey')
        return self


class DeleteKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        # 是否成功
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


class DeleteKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteKnowledgeResponseBody = None,
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
            temp_model = DeleteKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishTicketHeaders(TeaModel):
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


class FinishTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        # 群中通知接收人（钉钉UnionId）
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        # 企业工作通知接收人（钉钉UnionId）
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class FinishTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class FinishTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[FinishTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 备注文字
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = FinishTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class FinishTicketRequest(TeaModel):
    def __init__(
        self,
        notify: FinishTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        processor_union_id: str = None,
        ticket_memo: FinishTicketRequestTicketMemo = None,
    ):
        # 工单通知
        self.notify = notify
        self.open_team_id = open_team_id
        # 工单开放id
        self.open_ticket_id = open_ticket_id
        # 当前工单处理人
        self.processor_union_id = processor_union_id
        # 备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor_union_id is not None:
            result['processorUnionId'] = self.processor_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notify') is not None:
            temp_model = FinishTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processorUnionId') is not None:
            self.processor_union_id = m.get('processorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = FinishTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class FinishTicketResponse(TeaModel):
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


class GetOssTempUrlHeaders(TeaModel):
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


class GetOssTempUrlRequest(TeaModel):
    def __init__(
        self,
        fetch_mode: str = None,
        file_name: str = None,
        key: str = None,
        open_team_id: str = None,
    ):
        # 访问模式 AUTO(自动，例如在浏览器中如果是图片，PDF等可以在线直接查看，不能在线看时自动下载)、DOWNLOAD（直接下载）
        self.fetch_mode = fetch_mode
        # 文件名
        self.file_name = file_name
        # oss文件key
        self.key = key
        # 团队开放ID
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_mode is not None:
            result['fetchMode'] = self.fetch_mode
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fetchMode') is not None:
            self.fetch_mode = m.get('fetchMode')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class GetOssTempUrlResponseBody(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # Id of the request
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetOssTempUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOssTempUrlResponseBody = None,
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
            temp_model = GetOssTempUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoragePolicyHeaders(TeaModel):
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


class GetStoragePolicyRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        file_name: str = None,
        file_size: int = None,
        open_team_id: str = None,
    ):
        # 业务类型
        self.biz_type = biz_type
        # 文件名称
        self.file_name = file_name
        # 文件大小，单位字节
        self.file_size = file_size
        # 团队ID
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class GetStoragePolicyResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        endpoint: str = None,
        key: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_key_id = access_key_id
        self.endpoint = endpoint
        # Id of the request
        self.key = key
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class GetStoragePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStoragePolicyResponseBody = None,
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
            temp_model = GetStoragePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTicketHeaders(TeaModel):
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


class GetTicketRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
    ):
        # eKWh3GBwsKEiE
        self.open_team_id = open_team_id
        # hNiPO2OVktNMiE
        self.open_ticket_id = open_ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        return self


class GetTicketResponseBodyCreator(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetTicketResponseBodyProcessor(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetTicketResponseBodyTakers(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetTicketResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        open_template_biz_id: str = None,
        open_template_id: str = None,
        template_name: str = None,
    ):
        # 工单模版业务ID
        self.open_template_biz_id = open_template_biz_id
        # 工单模版ID
        self.open_template_id = open_template_id
        # 工单模版名称
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_template_biz_id is not None:
            result['openTemplateBizId'] = self.open_template_biz_id
        if self.open_template_id is not None:
            result['openTemplateId'] = self.open_template_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTemplateBizId') is not None:
            self.open_template_biz_id = m.get('openTemplateBizId')
        if m.get('openTemplateId') is not None:
            self.open_template_id = m.get('openTemplateId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class GetTicketResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator: GetTicketResponseBodyCreator = None,
        custom_fields: str = None,
        open_conversation_id: str = None,
        open_ticket_id: str = None,
        processor: GetTicketResponseBodyProcessor = None,
        scene: str = None,
        scene_context: str = None,
        stage: str = None,
        takers: List[GetTicketResponseBodyTakers] = None,
        template: GetTicketResponseBodyTemplate = None,
        title: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.custom_fields = custom_fields
        self.open_conversation_id = open_conversation_id
        # Id of the request
        self.open_ticket_id = open_ticket_id
        self.processor = processor
        self.scene = scene
        self.scene_context = scene_context
        self.stage = stage
        self.takers = takers
        self.template = template
        self.title = title
        self.update_time = update_time

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.processor:
            self.processor.validate()
        if self.takers:
            for k in self.takers:
                if k:
                    k.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator.to_map()
        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor is not None:
            result['processor'] = self.processor.to_map()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_context is not None:
            result['sceneContext'] = self.scene_context
        if self.stage is not None:
            result['stage'] = self.stage
        result['takers'] = []
        if self.takers is not None:
            for k in self.takers:
                result['takers'].append(k.to_map() if k else None)
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.title is not None:
            result['title'] = self.title
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            temp_model = GetTicketResponseBodyCreator()
            self.creator = temp_model.from_map(m['creator'])
        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processor') is not None:
            temp_model = GetTicketResponseBodyProcessor()
            self.processor = temp_model.from_map(m['processor'])
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneContext') is not None:
            self.scene_context = m.get('sceneContext')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        self.takers = []
        if m.get('takers') is not None:
            for k in m.get('takers'):
                temp_model = GetTicketResponseBodyTakers()
                self.takers.append(temp_model.from_map(k))
        if m.get('template') is not None:
            temp_model = GetTicketResponseBodyTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTicketResponseBody = None,
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
            temp_model = GetTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketOperateRecordHeaders(TeaModel):
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


class ListTicketOperateRecordRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
    ):
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        return self


class ListTicketOperateRecordResponseBodyRecordsOperator(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        self.file_name = file_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListTicketOperateRecordResponseBodyRecordsTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class ListTicketOperateRecordResponseBodyRecords(TeaModel):
    def __init__(
        self,
        open_ticket_id: str = None,
        operate_data: str = None,
        operate_time: str = None,
        operation: str = None,
        operation_display_name: str = None,
        operator: ListTicketOperateRecordResponseBodyRecordsOperator = None,
        ticket_memo: ListTicketOperateRecordResponseBodyRecordsTicketMemo = None,
    ):
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        self.operate_data = operate_data
        # 操作时间
        self.operate_time = operate_time
        # 动作
        self.operation = operation
        # 动作展示名
        self.operation_display_name = operation_display_name
        self.operator = operator
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.operator:
            self.operator.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.operate_data is not None:
            result['operateData'] = self.operate_data
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.operation is not None:
            result['operation'] = self.operation
        if self.operation_display_name is not None:
            result['operationDisplayName'] = self.operation_display_name
        if self.operator is not None:
            result['operator'] = self.operator.to_map()
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('operateData') is not None:
            self.operate_data = m.get('operateData')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('operationDisplayName') is not None:
            self.operation_display_name = m.get('operationDisplayName')
        if m.get('operator') is not None:
            temp_model = ListTicketOperateRecordResponseBodyRecordsOperator()
            self.operator = temp_model.from_map(m['operator'])
        if m.get('ticketMemo') is not None:
            temp_model = ListTicketOperateRecordResponseBodyRecordsTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class ListTicketOperateRecordResponseBody(TeaModel):
    def __init__(
        self,
        records: List[ListTicketOperateRecordResponseBodyRecords] = None,
    ):
        # Id of the request
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ListTicketOperateRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListTicketOperateRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTicketOperateRecordResponseBody = None,
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
            temp_model = ListTicketOperateRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserTeamsHeaders(TeaModel):
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


class ListUserTeamsResponseBodyTeams(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        team_name: str = None,
    ):
        # 开放团队ID
        self.open_team_id = open_team_id
        # 团队名称
        self.team_name = team_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.team_name is not None:
            result['teamName'] = self.team_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')
        return self


class ListUserTeamsResponseBody(TeaModel):
    def __init__(
        self,
        teams: List[ListUserTeamsResponseBodyTeams] = None,
    ):
        # teams
        self.teams = teams

    def validate(self):
        if self.teams:
            for k in self.teams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['teams'] = []
        if self.teams is not None:
            for k in self.teams:
                result['teams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.teams = []
        if m.get('teams') is not None:
            for k in m.get('teams'):
                temp_model = ListUserTeamsResponseBodyTeams()
                self.teams.append(temp_model.from_map(k))
        return self


class ListUserTeamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserTeamsResponseBody = None,
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
            temp_model = ListUserTeamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryActiveUsersHeaders(TeaModel):
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


class QueryActiveUsersRequest(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        open_team_id: str = None,
        top_n: int = None,
    ):
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 查询topN的数据
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.top_n is not None:
            result['topN'] = self.top_n
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('topN') is not None:
            self.top_n = m.get('topN')
        return self


class QueryActiveUsersResponseBodyActiveUserInfos(TeaModel):
    def __init__(
        self,
        action_index_l14d: float = None,
        action_index_l30d: float = None,
        action_index_l7d: float = None,
        active_score: float = None,
        nick_name: str = None,
        ranking: int = None,
        union_id: str = None,
    ):
        # 最近二周的行为指数
        self.action_index_l14d = action_index_l14d
        # 最近一个月的行为指数
        self.action_index_l30d = action_index_l30d
        # 最近一周的行为指数
        self.action_index_l7d = action_index_l7d
        # 活跃度
        self.active_score = active_score
        # 昵称
        self.nick_name = nick_name
        # 排名
        self.ranking = ranking
        # 钉钉用户unionId
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_index_l14d is not None:
            result['actionIndexL14d'] = self.action_index_l14d
        if self.action_index_l30d is not None:
            result['actionIndexL30d'] = self.action_index_l30d
        if self.action_index_l7d is not None:
            result['actionIndexL7d'] = self.action_index_l7d
        if self.active_score is not None:
            result['activeScore'] = self.active_score
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.ranking is not None:
            result['ranking'] = self.ranking
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionIndexL14d') is not None:
            self.action_index_l14d = m.get('actionIndexL14d')
        if m.get('actionIndexL30d') is not None:
            self.action_index_l30d = m.get('actionIndexL30d')
        if m.get('actionIndexL7d') is not None:
            self.action_index_l7d = m.get('actionIndexL7d')
        if m.get('activeScore') is not None:
            self.active_score = m.get('activeScore')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('ranking') is not None:
            self.ranking = m.get('ranking')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class QueryActiveUsersResponseBody(TeaModel):
    def __init__(
        self,
        active_user_infos: List[QueryActiveUsersResponseBodyActiveUserInfos] = None,
    ):
        # 活跃用户列表
        self.active_user_infos = active_user_infos

    def validate(self):
        if self.active_user_infos:
            for k in self.active_user_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['activeUserInfos'] = []
        if self.active_user_infos is not None:
            for k in self.active_user_infos:
                result['activeUserInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.active_user_infos = []
        if m.get('activeUserInfos') is not None:
            for k in m.get('activeUserInfos'):
                temp_model = QueryActiveUsersResponseBodyActiveUserInfos()
                self.active_user_infos.append(temp_model.from_map(k))
        return self


class QueryActiveUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryActiveUsersResponseBody = None,
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
            temp_model = QueryActiveUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupHeaders(TeaModel):
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


class QueryGroupRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        open_conversation_id: str = None,
        open_team_id: str = None,
    ):
        # 业务关联ID，和开放群ID二选一传
        self.biz_id = biz_id
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开放团队ID
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class QueryGroupResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        group_name: str = None,
        group_url: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        robot_code: str = None,
        robot_name: str = None,
    ):
        # 群bizId
        self.biz_id = biz_id
        # 群名称
        self.group_name = group_name
        # 入群URL
        self.group_url = group_url
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开放群组ID
        self.open_group_set_id = open_group_set_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 服务群机器人code
        self.robot_code = robot_code
        # 服务群机器人名称
        self.robot_name = robot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_url is not None:
            result['groupUrl'] = self.group_url
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.robot_code is not None:
            result['robotCode'] = self.robot_code
        if self.robot_name is not None:
            result['robotName'] = self.robot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupUrl') is not None:
            self.group_url = m.get('groupUrl')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('robotCode') is not None:
            self.robot_code = m.get('robotCode')
        if m.get('robotName') is not None:
            self.robot_name = m.get('robotName')
        return self


class QueryGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGroupResponseBody = None,
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
            temp_model = QueryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupSetHeaders(TeaModel):
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


class QueryGroupSetRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
    ):
        # openTeamId
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class QueryGroupSetResponseBodyRecords(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_set_name: str = None,
        open_group_set_id: str = None,
        template_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_set_name = group_set_name
        self.open_group_set_id = open_group_set_id
        self.template_id = template_id

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
        if self.group_set_name is not None:
            result['groupSetName'] = self.group_set_name
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('groupSetName') is not None:
            self.group_set_name = m.get('groupSetName')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class QueryGroupSetResponseBody(TeaModel):
    def __init__(
        self,
        records: List[QueryGroupSetResponseBodyRecords] = None,
    ):
        # records
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = QueryGroupSetResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class QueryGroupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGroupSetResponseBody = None,
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
            temp_model = QueryGroupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServiceGroupMessageReadStatusHeaders(TeaModel):
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


class QueryServiceGroupMessageReadStatusRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        open_conversation_id: str = None,
        open_msg_task_id: str = None,
        open_team_id: str = None,
    ):
        # 本次读取的最大数据记录数量，此参数为可选参数，用户传入为空时，应该有默认值。应设置最大值限制，最大不超过100
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开放消息ID
        self.open_msg_task_id = open_msg_task_id
        # 开放团队ID
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_msg_task_id is not None:
            result['openMsgTaskId'] = self.open_msg_task_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openMsgTaskId') is not None:
            self.open_msg_task_id = m.get('openMsgTaskId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class QueryServiceGroupMessageReadStatusResponseBodyRecords(TeaModel):
    def __init__(
        self,
        read_status: int = None,
        read_time_str: str = None,
        receiver_ding_talk_id: str = None,
        receiver_name: str = None,
        receiver_union_id: str = None,
        receiver_user_id: str = None,
        send_time_str: str = None,
    ):
        # 状态：已读1/未读0
        self.read_status = read_status
        # 已读时间
        self.read_time_str = read_time_str
        # 接收者dingtalkId
        self.receiver_ding_talk_id = receiver_ding_talk_id
        # 接收者昵称
        self.receiver_name = receiver_name
        # 已读人员为非企业员工则有值
        self.receiver_union_id = receiver_union_id
        # 已读人员为企业员工则有值
        self.receiver_user_id = receiver_user_id
        # 发送时间
        self.send_time_str = send_time_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_status is not None:
            result['readStatus'] = self.read_status
        if self.read_time_str is not None:
            result['readTimeStr'] = self.read_time_str
        if self.receiver_ding_talk_id is not None:
            result['receiverDingTalkId'] = self.receiver_ding_talk_id
        if self.receiver_name is not None:
            result['receiverName'] = self.receiver_name
        if self.receiver_union_id is not None:
            result['receiverUnionId'] = self.receiver_union_id
        if self.receiver_user_id is not None:
            result['receiverUserId'] = self.receiver_user_id
        if self.send_time_str is not None:
            result['sendTimeStr'] = self.send_time_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('readStatus') is not None:
            self.read_status = m.get('readStatus')
        if m.get('readTimeStr') is not None:
            self.read_time_str = m.get('readTimeStr')
        if m.get('receiverDingTalkId') is not None:
            self.receiver_ding_talk_id = m.get('receiverDingTalkId')
        if m.get('receiverName') is not None:
            self.receiver_name = m.get('receiverName')
        if m.get('receiverUnionId') is not None:
            self.receiver_union_id = m.get('receiverUnionId')
        if m.get('receiverUserId') is not None:
            self.receiver_user_id = m.get('receiverUserId')
        if m.get('sendTimeStr') is not None:
            self.send_time_str = m.get('sendTimeStr')
        return self


class QueryServiceGroupMessageReadStatusResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        records: List[QueryServiceGroupMessageReadStatusResponseBodyRecords] = None,
        total_count: int = None,
    ):
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 已读未读信息列表
        self.records = records
        # 本次请求条件下的数据总量，此参数为可选参数，默认可不返回。本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = QueryServiceGroupMessageReadStatusResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryServiceGroupMessageReadStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryServiceGroupMessageReadStatusResponseBody = None,
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
            temp_model = QueryServiceGroupMessageReadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResubmitTicketHeaders(TeaModel):
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


class ResubmitTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        # 服务群通知接收人（钉钉UnionId）
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        # 企业工作通知接收人（钉钉UnionId）
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class ResubmitTicketRequestSceneContextGroupMsgs(TeaModel):
    def __init__(
        self,
        anchor: bool = None,
        open_msg_id: str = None,
        topic_id: str = None,
    ):
        self.anchor = anchor
        # 勾选消息openMsgId
        self.open_msg_id = open_msg_id
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor is not None:
            result['anchor'] = self.anchor
        if self.open_msg_id is not None:
            result['openMsgId'] = self.open_msg_id
        if self.topic_id is not None:
            result['topicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchor') is not None:
            self.anchor = m.get('anchor')
        if m.get('openMsgId') is not None:
            self.open_msg_id = m.get('openMsgId')
        if m.get('topicId') is not None:
            self.topic_id = m.get('topicId')
        return self


class ResubmitTicketRequestSceneContext(TeaModel):
    def __init__(
        self,
        group_msgs: List[ResubmitTicketRequestSceneContextGroupMsgs] = None,
        open_conversation_id: str = None,
        relevantor_union_ids: List[str] = None,
    ):
        self.group_msgs = group_msgs
        # 服务群openConversationId
        self.open_conversation_id = open_conversation_id
        # 工单相关人UnionId列表
        self.relevantor_union_ids = relevantor_union_ids

    def validate(self):
        if self.group_msgs:
            for k in self.group_msgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['groupMsgs'] = []
        if self.group_msgs is not None:
            for k in self.group_msgs:
                result['groupMsgs'].append(k.to_map() if k else None)
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.relevantor_union_ids is not None:
            result['relevantorUnionIds'] = self.relevantor_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_msgs = []
        if m.get('groupMsgs') is not None:
            for k in m.get('groupMsgs'):
                temp_model = ResubmitTicketRequestSceneContextGroupMsgs()
                self.group_msgs.append(temp_model.from_map(k))
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('relevantorUnionIds') is not None:
            self.relevantor_union_ids = m.get('relevantorUnionIds')
        return self


class ResubmitTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ResubmitTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[ResubmitTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        # 备注文字
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = ResubmitTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class ResubmitTicketRequest(TeaModel):
    def __init__(
        self,
        creator_union_id: str = None,
        custom_fields: str = None,
        notify: ResubmitTicketRequestNotify = None,
        open_team_id: str = None,
        open_template_biz_id: str = None,
        open_ticket_id: str = None,
        processor_union_ids: List[str] = None,
        scene: str = None,
        scene_context: ResubmitTicketRequestSceneContext = None,
        ticket_memo: ResubmitTicketRequestTicketMemo = None,
        title: str = None,
    ):
        # 工单创建人UnionId
        self.creator_union_id = creator_union_id
        # 自定义组件字段值(JSON格式)
        self.custom_fields = custom_fields
        self.notify = notify
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单模板业务ID
        self.open_template_biz_id = open_template_biz_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 工单处理人UnionId列表
        self.processor_union_ids = processor_union_ids
        # 工单场景 SG 或 VOC
        self.scene = scene
        # 工单场景信息
        self.scene_context = scene_context
        # 备注
        self.ticket_memo = ticket_memo
        # 工单标题
        self.title = title

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.scene_context:
            self.scene_context.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_union_id is not None:
            result['creatorUnionId'] = self.creator_union_id
        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_template_biz_id is not None:
            result['openTemplateBizId'] = self.open_template_biz_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor_union_ids is not None:
            result['processorUnionIds'] = self.processor_union_ids
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_context is not None:
            result['sceneContext'] = self.scene_context.to_map()
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorUnionId') is not None:
            self.creator_union_id = m.get('creatorUnionId')
        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')
        if m.get('notify') is not None:
            temp_model = ResubmitTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTemplateBizId') is not None:
            self.open_template_biz_id = m.get('openTemplateBizId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processorUnionIds') is not None:
            self.processor_union_ids = m.get('processorUnionIds')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneContext') is not None:
            temp_model = ResubmitTicketRequestSceneContext()
            self.scene_context = temp_model.from_map(m['sceneContext'])
        if m.get('ticketMemo') is not None:
            temp_model = ResubmitTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ResubmitTicketResponse(TeaModel):
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


class RetractTicketHeaders(TeaModel):
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


class RetractTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class RetractTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        self.file_name = file_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class RetractTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[RetractTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = RetractTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class RetractTicketRequest(TeaModel):
    def __init__(
        self,
        notify: RetractTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        operator_union_id: str = None,
        ticket_memo: RetractTicketRequestTicketMemo = None,
    ):
        self.notify = notify
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 操作人ID
        self.operator_union_id = operator_union_id
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.operator_union_id is not None:
            result['operatorUnionId'] = self.operator_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notify') is not None:
            temp_model = RetractTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('operatorUnionId') is not None:
            self.operator_union_id = m.get('operatorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = RetractTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class RetractTicketResponse(TeaModel):
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


class SearchGroupHeaders(TeaModel):
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


class SearchGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        max_results: int = None,
        next_token: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        search_type: str = None,
    ):
        # 群名称
        self.group_name = group_name
        # 本次读取的最大数据记录数量，此参数为可选参数，用户传入为空时，应该有默认值。应设置最大值限制，最大不超过100
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开群组ID
        self.open_group_set_id = open_group_set_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 搜索类型
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.search_type is not None:
            result['searchType'] = self.search_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')
        return self


class SearchGroupResponseBodyRecords(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        group_url: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
    ):
        # 群名称
        self.group_name = group_name
        # 入群链接
        self.group_url = group_url
        # 开放群ID
        self.open_conversation_id = open_conversation_id
        # 开放群组ID
        self.open_group_set_id = open_group_set_id
        # 开放团队ID
        self.open_team_id = open_team_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_url is not None:
            result['groupUrl'] = self.group_url
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupUrl') is not None:
            self.group_url = m.get('groupUrl')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        return self


class SearchGroupResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        records: List[SearchGroupResponseBodyRecords] = None,
        total_count: int = None,
    ):
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 已读未读信息列表
        self.records = records
        # 本次请求条件下的数据总量，此参数为可选参数，默认可不返回。本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = SearchGroupResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class SearchGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchGroupResponseBody = None,
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
            temp_model = SearchGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMsgByTaskHeaders(TeaModel):
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


class SendMsgByTaskRequestMessageContentBtns(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        self.action_url = action_url
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionURL'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionURL') is not None:
            self.action_url = m.get('actionURL')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendMsgByTaskRequestMessageContent(TeaModel):
    def __init__(
        self,
        at_active_member_num: int = None,
        at_active_user: bool = None,
        at_all: bool = None,
        btns: List[SendMsgByTaskRequestMessageContentBtns] = None,
        content: str = None,
        images: List[str] = None,
        message_type: str = None,
        title: str = None,
    ):
        # at活跃成员数量
        self.at_active_member_num = at_active_member_num
        # 是否At活跃成员
        self.at_active_user = at_active_user
        # 是否At全部人员
        self.at_all = at_all
        self.btns = btns
        # 内容
        self.content = content
        # 图片列表
        self.images = images
        # 消息类型
        self.message_type = message_type
        # 标题
        self.title = title

    def validate(self):
        if self.btns:
            for k in self.btns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_active_member_num is not None:
            result['atActiveMemberNum'] = self.at_active_member_num
        if self.at_active_user is not None:
            result['atActiveUser'] = self.at_active_user
        if self.at_all is not None:
            result['atAll'] = self.at_all
        result['btns'] = []
        if self.btns is not None:
            for k in self.btns:
                result['btns'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.images is not None:
            result['images'] = self.images
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atActiveMemberNum') is not None:
            self.at_active_member_num = m.get('atActiveMemberNum')
        if m.get('atActiveUser') is not None:
            self.at_active_user = m.get('atActiveUser')
        if m.get('atAll') is not None:
            self.at_all = m.get('atAll')
        self.btns = []
        if m.get('btns') is not None:
            for k in m.get('btns'):
                temp_model = SendMsgByTaskRequestMessageContentBtns()
                self.btns.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendMsgByTaskRequestQueryGroup(TeaModel):
    def __init__(
        self,
        group_tag_names: List[str] = None,
        last_active_date_filter_type: str = None,
        last_active_time_end: str = None,
        last_active_time_start: str = None,
        open_conversation_ids: List[str] = None,
        open_group_set_id: str = None,
        query_type: str = None,
    ):
        # 群标签
        self.group_tag_names = group_tag_names
        # 活跃日期筛选类型，ACTIVE=活跃      NOTACTIVE=不活跃
        self.last_active_date_filter_type = last_active_date_filter_type
        # 最近活跃时间的结束时间
        self.last_active_time_end = last_active_time_end
        # 最近活跃时间的开始时间
        self.last_active_time_start = last_active_time_start
        # 精准圈选-群ID集合
        self.open_conversation_ids = open_conversation_ids
        # 开放群组ID
        self.open_group_set_id = open_group_set_id
        # 群发圈选类型 1. AIMED 精准圈选 2. MULTI_CONDITIONS 多条件圈选
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_tag_names is not None:
            result['groupTagNames'] = self.group_tag_names
        if self.last_active_date_filter_type is not None:
            result['lastActiveDateFilterType'] = self.last_active_date_filter_type
        if self.last_active_time_end is not None:
            result['lastActiveTimeEnd'] = self.last_active_time_end
        if self.last_active_time_start is not None:
            result['lastActiveTimeStart'] = self.last_active_time_start
        if self.open_conversation_ids is not None:
            result['openConversationIds'] = self.open_conversation_ids
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.query_type is not None:
            result['queryType'] = self.query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupTagNames') is not None:
            self.group_tag_names = m.get('groupTagNames')
        if m.get('lastActiveDateFilterType') is not None:
            self.last_active_date_filter_type = m.get('lastActiveDateFilterType')
        if m.get('lastActiveTimeEnd') is not None:
            self.last_active_time_end = m.get('lastActiveTimeEnd')
        if m.get('lastActiveTimeStart') is not None:
            self.last_active_time_start = m.get('lastActiveTimeStart')
        if m.get('openConversationIds') is not None:
            self.open_conversation_ids = m.get('openConversationIds')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        return self


class SendMsgByTaskRequestSendConfigUrlTrackConfig(TeaModel):
    def __init__(
        self,
        title: str = None,
        track_id: str = None,
        track_url: str = None,
    ):
        # 跟踪链接的标题
        self.title = title
        # 跟踪链接的坑位ID（sg开头）
        self.track_id = track_id
        # 跟踪链接URL
        self.track_url = track_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.track_id is not None:
            result['trackId'] = self.track_id
        if self.track_url is not None:
            result['trackUrl'] = self.track_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('trackId') is not None:
            self.track_id = m.get('trackId')
        if m.get('trackUrl') is not None:
            self.track_url = m.get('trackUrl')
        return self


class SendMsgByTaskRequestSendConfig(TeaModel):
    def __init__(
        self,
        need_url_track: bool = None,
        send_time: str = None,
        send_type: str = None,
        url_track_config: List[SendMsgByTaskRequestSendConfigUrlTrackConfig] = None,
    ):
        # 是否链接追踪
        self.need_url_track = need_url_track
        # 执行时间（sendType=TIMING时传入）
        self.send_time = send_time
        # 发送类型      * TIMING=定时执行      * INSTANT=立即执行
        self.send_type = send_type
        # 链接跟踪配置
        self.url_track_config = url_track_config

    def validate(self):
        if self.url_track_config:
            for k in self.url_track_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_url_track is not None:
            result['needUrlTrack'] = self.need_url_track
        if self.send_time is not None:
            result['sendTime'] = self.send_time
        if self.send_type is not None:
            result['sendType'] = self.send_type
        result['urlTrackConfig'] = []
        if self.url_track_config is not None:
            for k in self.url_track_config:
                result['urlTrackConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('needUrlTrack') is not None:
            self.need_url_track = m.get('needUrlTrack')
        if m.get('sendTime') is not None:
            self.send_time = m.get('sendTime')
        if m.get('sendType') is not None:
            self.send_type = m.get('sendType')
        self.url_track_config = []
        if m.get('urlTrackConfig') is not None:
            for k in m.get('urlTrackConfig'):
                temp_model = SendMsgByTaskRequestSendConfigUrlTrackConfig()
                self.url_track_config.append(temp_model.from_map(k))
        return self


class SendMsgByTaskRequest(TeaModel):
    def __init__(
        self,
        message_content: SendMsgByTaskRequestMessageContent = None,
        open_team_id: str = None,
        query_group: SendMsgByTaskRequestQueryGroup = None,
        send_config: SendMsgByTaskRequestSendConfig = None,
        task_name: str = None,
    ):
        # 群发内容
        self.message_content = message_content
        # 开放团队ID
        self.open_team_id = open_team_id
        self.query_group = query_group
        # 发送配置
        self.send_config = send_config
        # 群发任务名称
        self.task_name = task_name

    def validate(self):
        if self.message_content:
            self.message_content.validate()
        if self.query_group:
            self.query_group.validate()
        if self.send_config:
            self.send_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_content is not None:
            result['messageContent'] = self.message_content.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.query_group is not None:
            result['queryGroup'] = self.query_group.to_map()
        if self.send_config is not None:
            result['sendConfig'] = self.send_config.to_map()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageContent') is not None:
            temp_model = SendMsgByTaskRequestMessageContent()
            self.message_content = temp_model.from_map(m['messageContent'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('queryGroup') is not None:
            temp_model = SendMsgByTaskRequestQueryGroup()
            self.query_group = temp_model.from_map(m['queryGroup'])
        if m.get('sendConfig') is not None:
            temp_model = SendMsgByTaskRequestSendConfig()
            self.send_config = temp_model.from_map(m['sendConfig'])
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class SendMsgByTaskResponseBody(TeaModel):
    def __init__(
        self,
        open_batch_task_id: str = None,
    ):
        # Id of the request
        self.open_batch_task_id = open_batch_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_batch_task_id is not None:
            result['openBatchTaskId'] = self.open_batch_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openBatchTaskId') is not None:
            self.open_batch_task_id = m.get('openBatchTaskId')
        return self


class SendMsgByTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMsgByTaskResponseBody = None,
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
            temp_model = SendMsgByTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendServiceGroupMessageHeaders(TeaModel):
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


class SendServiceGroupMessageRequestBtns(TeaModel):
    def __init__(
        self,
        action_url: str = None,
        title: str = None,
    ):
        # 跳转地址
        self.action_url = action_url
        # 按钮名称
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_url is not None:
            result['actionURL'] = self.action_url
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionURL') is not None:
            self.action_url = m.get('actionURL')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendServiceGroupMessageRequest(TeaModel):
    def __init__(
        self,
        at_dingtalk_ids: List[str] = None,
        at_mobiles: List[str] = None,
        at_union_ids: List[str] = None,
        btn_orientation: str = None,
        btns: List[SendServiceGroupMessageRequestBtns] = None,
        content: str = None,
        has_content_links: bool = None,
        is_at_all: bool = None,
        message_type: str = None,
        receiver_dingtalk_ids: List[str] = None,
        receiver_mobiles: List[str] = None,
        receiver_union_ids: List[str] = None,
        target_open_conversation_id: str = None,
        title: str = None,
    ):
        # at dingtalkId
        self.at_dingtalk_ids = at_dingtalk_ids
        # at 手机号
        self.at_mobiles = at_mobiles
        # at unionIds
        self.at_union_ids = at_union_ids
        # 排列方式：0-按钮竖直排列，1-按钮横向排列
        self.btn_orientation = btn_orientation
        # actionCard按钮
        self.btns = btns
        # 内容
        self.content = content
        # 如果正文内容包含链接，并且按钮链接和文本链接分开跳转，则传递true; 否则传递false
        self.has_content_links = has_content_links
        # 是否 at所有人
        self.is_at_all = is_at_all
        # 消息类型：MARKDOWN，ACTIONCARD
        self.message_type = message_type
        # dingtalkId接收者
        self.receiver_dingtalk_ids = receiver_dingtalk_ids
        # 手机号接收者
        self.receiver_mobiles = receiver_mobiles
        # unionId接收者
        self.receiver_union_ids = receiver_union_ids
        # 开放群ID
        self.target_open_conversation_id = target_open_conversation_id
        # 标题
        self.title = title

    def validate(self):
        if self.btns:
            for k in self.btns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_dingtalk_ids is not None:
            result['atDingtalkIds'] = self.at_dingtalk_ids
        if self.at_mobiles is not None:
            result['atMobiles'] = self.at_mobiles
        if self.at_union_ids is not None:
            result['atUnionIds'] = self.at_union_ids
        if self.btn_orientation is not None:
            result['btnOrientation'] = self.btn_orientation
        result['btns'] = []
        if self.btns is not None:
            for k in self.btns:
                result['btns'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.has_content_links is not None:
            result['hasContentLinks'] = self.has_content_links
        if self.is_at_all is not None:
            result['isAtAll'] = self.is_at_all
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.receiver_dingtalk_ids is not None:
            result['receiverDingtalkIds'] = self.receiver_dingtalk_ids
        if self.receiver_mobiles is not None:
            result['receiverMobiles'] = self.receiver_mobiles
        if self.receiver_union_ids is not None:
            result['receiverUnionIds'] = self.receiver_union_ids
        if self.target_open_conversation_id is not None:
            result['targetOpenConversationId'] = self.target_open_conversation_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atDingtalkIds') is not None:
            self.at_dingtalk_ids = m.get('atDingtalkIds')
        if m.get('atMobiles') is not None:
            self.at_mobiles = m.get('atMobiles')
        if m.get('atUnionIds') is not None:
            self.at_union_ids = m.get('atUnionIds')
        if m.get('btnOrientation') is not None:
            self.btn_orientation = m.get('btnOrientation')
        self.btns = []
        if m.get('btns') is not None:
            for k in m.get('btns'):
                temp_model = SendServiceGroupMessageRequestBtns()
                self.btns.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('hasContentLinks') is not None:
            self.has_content_links = m.get('hasContentLinks')
        if m.get('isAtAll') is not None:
            self.is_at_all = m.get('isAtAll')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('receiverDingtalkIds') is not None:
            self.receiver_dingtalk_ids = m.get('receiverDingtalkIds')
        if m.get('receiverMobiles') is not None:
            self.receiver_mobiles = m.get('receiverMobiles')
        if m.get('receiverUnionIds') is not None:
            self.receiver_union_ids = m.get('receiverUnionIds')
        if m.get('targetOpenConversationId') is not None:
            self.target_open_conversation_id = m.get('targetOpenConversationId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SendServiceGroupMessageResponseBody(TeaModel):
    def __init__(
        self,
        open_msg_task_id: str = None,
    ):
        # 开放消息任务ID
        self.open_msg_task_id = open_msg_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_msg_task_id is not None:
            result['openMsgTaskId'] = self.open_msg_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openMsgTaskId') is not None:
            self.open_msg_task_id = m.get('openMsgTaskId')
        return self


class SendServiceGroupMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendServiceGroupMessageResponseBody = None,
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
            temp_model = SendServiceGroupMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRobotConfigHeaders(TeaModel):
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


class SetRobotConfigRequest(TeaModel):
    def __init__(
        self,
        ding_isv_org_id: int = None,
        ding_org_id: int = None,
        ding_suite_key: str = None,
        ding_token_grant_type: int = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        status: str = None,
    ):
        self.ding_isv_org_id = ding_isv_org_id
        self.ding_org_id = ding_org_id
        self.ding_suite_key = ding_suite_key
        self.ding_token_grant_type = ding_token_grant_type
        # 群组开放ID
        self.open_group_set_id = open_group_set_id
        # 开放团队ID
        self.open_team_id = open_team_id
        # 设置状态，0代表关闭,1代表开启
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_isv_org_id is not None:
            result['dingIsvOrgId'] = self.ding_isv_org_id
        if self.ding_org_id is not None:
            result['dingOrgId'] = self.ding_org_id
        if self.ding_suite_key is not None:
            result['dingSuiteKey'] = self.ding_suite_key
        if self.ding_token_grant_type is not None:
            result['dingTokenGrantType'] = self.ding_token_grant_type
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingIsvOrgId') is not None:
            self.ding_isv_org_id = m.get('dingIsvOrgId')
        if m.get('dingOrgId') is not None:
            self.ding_org_id = m.get('dingOrgId')
        if m.get('dingSuiteKey') is not None:
            self.ding_suite_key = m.get('dingSuiteKey')
        if m.get('dingTokenGrantType') is not None:
            self.ding_token_grant_type = m.get('dingTokenGrantType')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SetRobotConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
    ):
        # 业务Key
        self.config_key = config_key
        # 业务value
        self.config_value = config_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['configKey'] = self.config_key
        if self.config_value is not None:
            result['configValue'] = self.config_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        return self


class SetRobotConfigResponseBody(TeaModel):
    def __init__(
        self,
        result: SetRobotConfigResponseBodyResult = None,
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
            temp_model = SetRobotConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class SetRobotConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRobotConfigResponseBody = None,
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
            temp_model = SetRobotConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TakeTicketHeaders(TeaModel):
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


class TakeTicketRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
        taker_union_id: str = None,
    ):
        self.open_team_id = open_team_id
        self.open_ticket_id = open_ticket_id
        self.taker_union_id = taker_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.taker_union_id is not None:
            result['takerUnionId'] = self.taker_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('takerUnionId') is not None:
            self.taker_union_id = m.get('takerUnionId')
        return self


class TakeTicketResponse(TeaModel):
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


class TransferTicketHeaders(TeaModel):
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


class TransferTicketRequestNotify(TeaModel):
    def __init__(
        self,
        group_notice_receiver_union_ids: List[str] = None,
        notice_all_group_member: bool = None,
        work_notice_receiver_union_ids: List[str] = None,
    ):
        # 群中通知接收人（钉钉UnionId）
        self.group_notice_receiver_union_ids = group_notice_receiver_union_ids
        # 是否向群内推送一个全员可见工单通知卡片
        self.notice_all_group_member = notice_all_group_member
        # 企业工作通知接收人（钉钉UnionId）
        self.work_notice_receiver_union_ids = work_notice_receiver_union_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_notice_receiver_union_ids is not None:
            result['groupNoticeReceiverUnionIds'] = self.group_notice_receiver_union_ids
        if self.notice_all_group_member is not None:
            result['noticeAllGroupMember'] = self.notice_all_group_member
        if self.work_notice_receiver_union_ids is not None:
            result['workNoticeReceiverUnionIds'] = self.work_notice_receiver_union_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNoticeReceiverUnionIds') is not None:
            self.group_notice_receiver_union_ids = m.get('groupNoticeReceiverUnionIds')
        if m.get('noticeAllGroupMember') is not None:
            self.notice_all_group_member = m.get('noticeAllGroupMember')
        if m.get('workNoticeReceiverUnionIds') is not None:
            self.work_notice_receiver_union_ids = m.get('workNoticeReceiverUnionIds')
        return self


class TransferTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        self.file_name = file_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class TransferTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[TransferTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 文字备注
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = TransferTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class TransferTicketRequest(TeaModel):
    def __init__(
        self,
        notify: TransferTicketRequestNotify = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        processor_union_id: str = None,
        processor_union_ids: List[str] = None,
        ticket_memo: TransferTicketRequestTicketMemo = None,
    ):
        self.notify = notify
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放ID
        self.open_ticket_id = open_ticket_id
        # 工单处理人
        self.processor_union_id = processor_union_id
        # 被转单人UnionId列表
        self.processor_union_ids = processor_union_ids
        # 工单备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.notify:
            self.notify.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify is not None:
            result['notify'] = self.notify.to_map()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor_union_id is not None:
            result['processorUnionId'] = self.processor_union_id
        if self.processor_union_ids is not None:
            result['processorUnionIds'] = self.processor_union_ids
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notify') is not None:
            temp_model = TransferTicketRequestNotify()
            self.notify = temp_model.from_map(m['notify'])
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processorUnionId') is not None:
            self.processor_union_id = m.get('processorUnionId')
        if m.get('processorUnionIds') is not None:
            self.processor_union_ids = m.get('processorUnionIds')
        if m.get('ticketMemo') is not None:
            temp_model = TransferTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class TransferTicketResponse(TeaModel):
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


class UpdateGroupTagHeaders(TeaModel):
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


class UpdateGroupTagRequest(TeaModel):
    def __init__(
        self,
        open_conversation_ids: List[str] = None,
        tag_names: List[str] = None,
        update_type: str = None,
    ):
        # 群会话ID集合
        self.open_conversation_ids = open_conversation_ids
        self.tag_names = tag_names
        # 更新类型，APPEND、NOTAPPEND、DELETE三种类型
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_ids is not None:
            result['openConversationIds'] = self.open_conversation_ids
        if self.tag_names is not None:
            result['tagNames'] = self.tag_names
        if self.update_type is not None:
            result['updateType'] = self.update_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationIds') is not None:
            self.open_conversation_ids = m.get('openConversationIds')
        if m.get('tagNames') is not None:
            self.tag_names = m.get('tagNames')
        if m.get('updateType') is not None:
            self.update_type = m.get('updateType')
        return self


class UpdateGroupTagResponse(TeaModel):
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


class UpdateTicketHeaders(TeaModel):
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


class UpdateTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class UpdateTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[UpdateTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 备注文字
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = UpdateTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class UpdateTicketRequest(TeaModel):
    def __init__(
        self,
        custom_fields: str = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        processor_union_id: str = None,
        ticket_memo: UpdateTicketRequestTicketMemo = None,
    ):
        # 自定义字段值JSON格式
        self.custom_fields = custom_fields
        # 团队ID
        self.open_team_id = open_team_id
        # 工单开放id
        self.open_ticket_id = open_ticket_id
        # 工单处理人unionId
        self.processor_union_id = processor_union_id
        # 备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.processor_union_id is not None:
            result['processorUnionId'] = self.processor_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('processorUnionId') is not None:
            self.processor_union_id = m.get('processorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = UpdateTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class UpdateTicketResponse(TeaModel):
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


class UpgradeCloudGroupHeaders(TeaModel):
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


class UpgradeCloudGroupRequest(TeaModel):
    def __init__(
        self,
        ccs_instance_id: str = None,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        template_id: str = None,
    ):
        # 云客服租户id
        self.ccs_instance_id = ccs_instance_id
        # 钉钉群id
        self.open_conversation_id = open_conversation_id
        # 升级的目标群组id
        self.open_group_set_id = open_group_set_id
        # 升级的目标团队id
        self.open_team_id = open_team_id
        # 升级的目标模板id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ccs_instance_id is not None:
            result['ccsInstanceId'] = self.ccs_instance_id
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ccsInstanceId') is not None:
            self.ccs_instance_id = m.get('ccsInstanceId')
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class UpgradeCloudGroupResponse(TeaModel):
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


class UpgradeNormalGroupHeaders(TeaModel):
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


class UpgradeNormalGroupRequest(TeaModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        open_group_set_id: str = None,
        open_team_id: str = None,
        template_id: str = None,
    ):
        # 群id
        self.open_conversation_id = open_conversation_id
        # 升级的目标群组id
        self.open_group_set_id = open_group_set_id
        # 升级的目标团队id
        self.open_team_id = open_team_id
        # 升级的目标模板id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_conversation_id is not None:
            result['openConversationId'] = self.open_conversation_id
        if self.open_group_set_id is not None:
            result['openGroupSetId'] = self.open_group_set_id
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openConversationId') is not None:
            self.open_conversation_id = m.get('openConversationId')
        if m.get('openGroupSetId') is not None:
            self.open_group_set_id = m.get('openGroupSetId')
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class UpgradeNormalGroupResponse(TeaModel):
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


class UrgeTicketHeaders(TeaModel):
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


class UrgeTicketRequestTicketMemoAttachments(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class UrgeTicketRequestTicketMemo(TeaModel):
    def __init__(
        self,
        attachments: List[UrgeTicketRequestTicketMemoAttachments] = None,
        memo: str = None,
    ):
        # 备注相关的附件
        self.attachments = attachments
        # 备注文字
        self.memo = memo

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = UrgeTicketRequestTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k))
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class UrgeTicketRequest(TeaModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
        operator_union_id: str = None,
        ticket_memo: UrgeTicketRequestTicketMemo = None,
    ):
        # 开放团队ID
        self.open_team_id = open_team_id
        # 工单开放id
        self.open_ticket_id = open_ticket_id
        # 工单催单操作人UnionId
        self.operator_union_id = operator_union_id
        # 备注
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_team_id is not None:
            result['openTeamId'] = self.open_team_id
        if self.open_ticket_id is not None:
            result['openTicketId'] = self.open_ticket_id
        if self.operator_union_id is not None:
            result['operatorUnionId'] = self.operator_union_id
        if self.ticket_memo is not None:
            result['ticketMemo'] = self.ticket_memo.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openTeamId') is not None:
            self.open_team_id = m.get('openTeamId')
        if m.get('openTicketId') is not None:
            self.open_ticket_id = m.get('openTicketId')
        if m.get('operatorUnionId') is not None:
            self.operator_union_id = m.get('operatorUnionId')
        if m.get('ticketMemo') is not None:
            temp_model = UrgeTicketRequestTicketMemo()
            self.ticket_memo = temp_model.from_map(m['ticketMemo'])
        return self


class UrgeTicketResponse(TeaModel):
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


