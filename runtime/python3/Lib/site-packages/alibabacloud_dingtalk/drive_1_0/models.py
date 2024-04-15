# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddCustomSpaceHeaders(TeaModel):
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


class AddCustomSpaceRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        identifier: str = None,
        permission_mode: str = None,
        union_id: str = None,
    ):
        # 业务类型
        self.biz_type = biz_type
        # 空间标识
        self.identifier = identifier
        # 授权模式
        self.permission_mode = permission_mode
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.permission_mode is not None:
            result['permissionMode'] = self.permission_mode
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('permissionMode') is not None:
            self.permission_mode = m.get('permissionMode')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class AddCustomSpaceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 空间总额度
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 空间已使用额度
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class AddCustomSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCustomSpaceResponseBody = None,
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
            temp_model = AddCustomSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFileHeaders(TeaModel):
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


class AddFileRequest(TeaModel):
    def __init__(
        self,
        add_conflict_policy: str = None,
        file_name: str = None,
        file_type: str = None,
        media_id: str = None,
        parent_id: str = None,
        union_id: str = None,
    ):
        # 文件名冲突策略
        self.add_conflict_policy = add_conflict_policy
        # 文件名
        self.file_name = file_name
        # 文件类型
        self.file_type = file_type
        # mediaId
        self.media_id = media_id
        # 父目录id
        self.parent_id = parent_id
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_conflict_policy is not None:
            result['addConflictPolicy'] = self.add_conflict_policy
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addConflictPolicy') is not None:
            self.add_conflict_policy = m.get('addConflictPolicy')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class AddFileResponseBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class AddFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFileResponseBody = None,
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
            temp_model = AddFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPermissionHeaders(TeaModel):
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


class AddPermissionRequestMembers(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # 企业corpId
        self.corp_id = corp_id
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class AddPermissionRequest(TeaModel):
    def __init__(
        self,
        members: List[AddPermissionRequestMembers] = None,
        role: str = None,
        union_id: str = None,
    ):
        self.members = members
        # 权限角色
        self.role = role
        # 用户id
        self.union_id = union_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.role is not None:
            result['role'] = self.role
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = AddPermissionRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class AddPermissionResponse(TeaModel):
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


class AddSpaceHeaders(TeaModel):
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


class AddSpaceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        union_id: str = None,
    ):
        # 空间名称
        self.name = name
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class AddSpaceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 空间总额度
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 空间已使用额度
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class AddSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSpaceResponseBody = None,
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
            temp_model = AddSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearRecycleFilesHeaders(TeaModel):
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


class ClearRecycleFilesRequest(TeaModel):
    def __init__(
        self,
        recycle_type: str = None,
        union_id: str = None,
    ):
        # 回收站类型
        self.recycle_type = recycle_type
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recycle_type is not None:
            result['recycleType'] = self.recycle_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recycleType') is not None:
            self.recycle_type = m.get('recycleType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ClearRecycleFilesResponse(TeaModel):
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


class CopyFileHeaders(TeaModel):
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


class CopyFileRequest(TeaModel):
    def __init__(
        self,
        add_conflict_policy: str = None,
        target_parent_id: str = None,
        target_space_id: str = None,
        union_id: str = None,
    ):
        # 文件名冲突策略
        self.add_conflict_policy = add_conflict_policy
        # 目标父目录id
        self.target_parent_id = target_parent_id
        # 目标空间id
        self.target_space_id = target_space_id
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_conflict_policy is not None:
            result['addConflictPolicy'] = self.add_conflict_policy
        if self.target_parent_id is not None:
            result['targetParentId'] = self.target_parent_id
        if self.target_space_id is not None:
            result['targetSpaceId'] = self.target_space_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addConflictPolicy') is not None:
            self.add_conflict_policy = m.get('addConflictPolicy')
        if m.get('targetParentId') is not None:
            self.target_parent_id = m.get('targetParentId')
        if m.get('targetSpaceId') is not None:
            self.target_space_id = m.get('targetSpaceId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class CopyFileResponseBodyFile(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class CopyFileResponseBody(TeaModel):
    def __init__(
        self,
        file: CopyFileResponseBodyFile = None,
        task_id: str = None,
    ):
        # 文件信息
        self.file = file
        # 异步任务id
        self.task_id = task_id

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file') is not None:
            temp_model = CopyFileResponseBodyFile()
            self.file = temp_model.from_map(m['file'])
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CopyFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyFileResponseBody = None,
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
            temp_model = CopyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileHeaders(TeaModel):
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


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        delete_policy: str = None,
        union_id: str = None,
    ):
        # 删除策略
        self.delete_policy = delete_policy
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_policy is not None:
            result['deletePolicy'] = self.delete_policy
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletePolicy') is not None:
            self.delete_policy = m.get('deletePolicy')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class DeleteFileResponseBody(TeaModel):
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


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilesHeaders(TeaModel):
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


class DeleteFilesRequest(TeaModel):
    def __init__(
        self,
        delete_policy: str = None,
        file_ids: List[str] = None,
        union_id: str = None,
    ):
        # 删除策略
        self.delete_policy = delete_policy
        # 文件id列表
        self.file_ids = file_ids
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_policy is not None:
            result['deletePolicy'] = self.delete_policy
        if self.file_ids is not None:
            result['fileIds'] = self.file_ids
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletePolicy') is not None:
            self.delete_policy = m.get('deletePolicy')
        if m.get('fileIds') is not None:
            self.file_ids = m.get('fileIds')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class DeleteFilesResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        task_id: str = None,
    ):
        # 是否成功
        self.success = success
        # 异步任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFilesResponseBody = None,
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
            temp_model = DeleteFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePermissionHeaders(TeaModel):
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


class DeletePermissionRequestMembers(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # 企业corpId
        self.corp_id = corp_id
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class DeletePermissionRequest(TeaModel):
    def __init__(
        self,
        members: List[DeletePermissionRequestMembers] = None,
        role: str = None,
        union_id: str = None,
    ):
        self.members = members
        # 权限角色
        self.role = role
        # 用户id
        self.union_id = union_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.role is not None:
            result['role'] = self.role
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = DeletePermissionRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class DeletePermissionResponse(TeaModel):
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


class DeleteRecycleFilesHeaders(TeaModel):
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


class DeleteRecycleFilesRequest(TeaModel):
    def __init__(
        self,
        recycle_item_id_list: List[int] = None,
        recycle_type: str = None,
        union_id: str = None,
    ):
        # 回收站item id列表
        self.recycle_item_id_list = recycle_item_id_list
        # 回收站类型
        self.recycle_type = recycle_type
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recycle_item_id_list is not None:
            result['recycleItemIdList'] = self.recycle_item_id_list
        if self.recycle_type is not None:
            result['recycleType'] = self.recycle_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recycleItemIdList') is not None:
            self.recycle_item_id_list = m.get('recycleItemIdList')
        if m.get('recycleType') is not None:
            self.recycle_type = m.get('recycleType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class DeleteRecycleFilesResponse(TeaModel):
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


class DeleteSpaceHeaders(TeaModel):
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


class DeleteSpaceRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class DeleteSpaceResponse(TeaModel):
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


class GetAsyncTaskInfoHeaders(TeaModel):
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


class GetAsyncTaskInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetAsyncTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        failed: int = None,
        status: str = None,
        success: int = None,
        task_id: str = None,
        total: int = None,
    ):
        # 任务开始时间
        self.begin_time = begin_time
        # 任务结束时间
        self.end_time = end_time
        # 失败个数
        self.failed = failed
        # 任务状态
        self.status = status
        # 完成个数
        self.success = success
        # 异步任务id
        self.task_id = task_id
        # 任务总数
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.failed is not None:
            result['failed'] = self.failed
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetAsyncTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncTaskInfoResponseBody = None,
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
            temp_model = GetAsyncTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadInfoHeaders(TeaModel):
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


class GetDownloadInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
        with_internal_resource_url: bool = None,
        with_region: bool = None,
    ):
        # 用户id
        self.union_id = union_id
        # 是否返回内网加签url
        self.with_internal_resource_url = with_internal_resource_url
        # 是否返回区域信息
        self.with_region = with_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.with_internal_resource_url is not None:
            result['withInternalResourceUrl'] = self.with_internal_resource_url
        if self.with_region is not None:
            result['withRegion'] = self.with_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('withInternalResourceUrl') is not None:
            self.with_internal_resource_url = m.get('withInternalResourceUrl')
        if m.get('withRegion') is not None:
            self.with_region = m.get('withRegion')
        return self


class GetDownloadInfoResponseBodyDownloadInfo(TeaModel):
    def __init__(
        self,
        expiration_seconds: int = None,
        headers: Dict[str, Any] = None,
        internal_resource_url: str = None,
        resource_url: str = None,
    ):
        # 加签url过期时间
        self.expiration_seconds = expiration_seconds
        # headers
        self.headers = headers
        # 内网加签url
        self.internal_resource_url = internal_resource_url
        # 加签url
        self.resource_url = resource_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_seconds is not None:
            result['expirationSeconds'] = self.expiration_seconds
        if self.headers is not None:
            result['headers'] = self.headers
        if self.internal_resource_url is not None:
            result['internalResourceUrl'] = self.internal_resource_url
        if self.resource_url is not None:
            result['resourceUrl'] = self.resource_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationSeconds') is not None:
            self.expiration_seconds = m.get('expirationSeconds')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('internalResourceUrl') is not None:
            self.internal_resource_url = m.get('internalResourceUrl')
        if m.get('resourceUrl') is not None:
            self.resource_url = m.get('resourceUrl')
        return self


class GetDownloadInfoResponseBody(TeaModel):
    def __init__(
        self,
        download_info: GetDownloadInfoResponseBodyDownloadInfo = None,
        region: str = None,
    ):
        # 下载加签url信息
        self.download_info = download_info
        # 文件所存储的区域
        self.region = region

    def validate(self):
        if self.download_info:
            self.download_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_info is not None:
            result['downloadInfo'] = self.download_info.to_map()
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadInfo') is not None:
            temp_model = GetDownloadInfoResponseBodyDownloadInfo()
            self.download_info = temp_model.from_map(m['downloadInfo'])
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class GetDownloadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDownloadInfoResponseBody = None,
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
            temp_model = GetDownloadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileInfoHeaders(TeaModel):
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


class GetFileInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetFileInfoResponseBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
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


class GetMySpaceInfoHeaders(TeaModel):
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


class GetMySpaceInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetMySpaceInfoResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 容量
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class GetMySpaceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMySpaceInfoResponseBody = None,
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
            temp_model = GetMySpaceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreviewInfoHeaders(TeaModel):
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


class GetPreviewInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetPreviewInfoResponseBodyInfo(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # 预览url
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


class GetPreviewInfoResponseBody(TeaModel):
    def __init__(
        self,
        info: GetPreviewInfoResponseBodyInfo = None,
    ):
        # 预览信息
        self.info = info

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['info'] = self.info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info') is not None:
            temp_model = GetPreviewInfoResponseBodyInfo()
            self.info = temp_model.from_map(m['info'])
        return self


class GetPreviewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPreviewInfoResponseBody = None,
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
            temp_model = GetPreviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivilegeInfoHeaders(TeaModel):
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


class GetPrivilegeInfoRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetPrivilegeInfoResponseBody(TeaModel):
    def __init__(
        self,
        types: List[str] = None,
    ):
        # 类型列表
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class GetPrivilegeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPrivilegeInfoResponseBody = None,
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
            temp_model = GetPrivilegeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaInfosHeaders(TeaModel):
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


class GetQuotaInfosRequest(TeaModel):
    def __init__(
        self,
        identifiers: List[str] = None,
        type: str = None,
        union_id: str = None,
    ):
        # 容量标识符列表
        self.identifiers = identifiers
        # 容量类型
        self.type = type
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifiers is not None:
            result['identifiers'] = self.identifiers
        if self.type is not None:
            result['type'] = self.type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class GetQuotaInfosResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        quota: int = None,
        type: str = None,
        used_quota: int = None,
    ):
        # 容量标识符
        self.identifier = identifier
        # 总容量
        self.quota = quota
        # 容量类型
        self.type = type
        # 已使用容量
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.quota is not None:
            result['quota'] = self.quota
        if self.type is not None:
            result['type'] = self.type
        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')
        return self


class GetQuotaInfosResponseBody(TeaModel):
    def __init__(
        self,
        quotas: List[GetQuotaInfosResponseBodyQuotas] = None,
    ):
        # 容量信息列表
        self.quotas = quotas

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['quotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('quotas') is not None:
            for k in m.get('quotas'):
                temp_model = GetQuotaInfosResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        return self


class GetQuotaInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQuotaInfosResponseBody = None,
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
            temp_model = GetQuotaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadInfoHeaders(TeaModel):
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


class GetUploadInfoRequest(TeaModel):
    def __init__(
        self,
        add_conflict_policy: str = None,
        caller_region: str = None,
        file_name: str = None,
        file_size: int = None,
        md_5: str = None,
        media_id: str = None,
        union_id: str = None,
        with_internal_end_point: bool = None,
        with_region: bool = None,
    ):
        # 文件名称冲突策略
        self.add_conflict_policy = add_conflict_policy
        # 调用方所处区域
        self.caller_region = caller_region
        # 文件名
        self.file_name = file_name
        # 文件大小
        self.file_size = file_size
        # 文件md5
        self.md_5 = md_5
        # mediaId
        self.media_id = media_id
        # 用户id
        self.union_id = union_id
        # 是否返回OSS内网访问域名
        self.with_internal_end_point = with_internal_end_point
        # 是否返回区域
        self.with_region = with_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_conflict_policy is not None:
            result['addConflictPolicy'] = self.add_conflict_policy
        if self.caller_region is not None:
            result['callerRegion'] = self.caller_region
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.with_internal_end_point is not None:
            result['withInternalEndPoint'] = self.with_internal_end_point
        if self.with_region is not None:
            result['withRegion'] = self.with_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addConflictPolicy') is not None:
            self.add_conflict_policy = m.get('addConflictPolicy')
        if m.get('callerRegion') is not None:
            self.caller_region = m.get('callerRegion')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('withInternalEndPoint') is not None:
            self.with_internal_end_point = m.get('withInternalEndPoint')
        if m.get('withRegion') is not None:
            self.with_region = m.get('withRegion')
        return self


class GetUploadInfoResponseBodyHeaderSignatureUploadInfo(TeaModel):
    def __init__(
        self,
        expiration_seconds: int = None,
        headers: Dict[str, Any] = None,
        internal_resource_url: str = None,
        media_id: str = None,
        resource_url: str = None,
    ):
        # 过期秒数
        self.expiration_seconds = expiration_seconds
        # header加签信息
        self.headers = headers
        # 内网上传地址
        self.internal_resource_url = internal_resource_url
        # mediaId
        self.media_id = media_id
        # 上传地址
        self.resource_url = resource_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_seconds is not None:
            result['expirationSeconds'] = self.expiration_seconds
        if self.headers is not None:
            result['headers'] = self.headers
        if self.internal_resource_url is not None:
            result['internalResourceUrl'] = self.internal_resource_url
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        if self.resource_url is not None:
            result['resourceUrl'] = self.resource_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationSeconds') is not None:
            self.expiration_seconds = m.get('expirationSeconds')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('internalResourceUrl') is not None:
            self.internal_resource_url = m.get('internalResourceUrl')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        if m.get('resourceUrl') is not None:
            self.resource_url = m.get('resourceUrl')
        return self


class GetUploadInfoResponseBodyStsUploadInfo(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        access_token: str = None,
        access_token_expiration_millis: int = None,
        bucket: str = None,
        end_point: str = None,
        internal_end_point: str = None,
        media_id: str = None,
    ):
        # accessKeyId
        self.access_key_id = access_key_id
        # accessKeySecret
        self.access_key_secret = access_key_secret
        # accessToken
        self.access_token = access_token
        # accessTokenExpiration
        self.access_token_expiration_millis = access_token_expiration_millis
        # bucket
        self.bucket = bucket
        # endPoint
        self.end_point = end_point
        # 内网endPoint
        self.internal_end_point = internal_end_point
        # mediaId
        self.media_id = media_id

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
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.access_token_expiration_millis is not None:
            result['accessTokenExpirationMillis'] = self.access_token_expiration_millis
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.end_point is not None:
            result['endPoint'] = self.end_point
        if self.internal_end_point is not None:
            result['internalEndPoint'] = self.internal_end_point
        if self.media_id is not None:
            result['mediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('accessTokenExpirationMillis') is not None:
            self.access_token_expiration_millis = m.get('accessTokenExpirationMillis')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endPoint') is not None:
            self.end_point = m.get('endPoint')
        if m.get('internalEndPoint') is not None:
            self.internal_end_point = m.get('internalEndPoint')
        if m.get('mediaId') is not None:
            self.media_id = m.get('mediaId')
        return self


class GetUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        header_signature_upload_info: GetUploadInfoResponseBodyHeaderSignatureUploadInfo = None,
        region: str = None,
        sts_upload_info: GetUploadInfoResponseBodyStsUploadInfo = None,
    ):
        self.header_signature_upload_info = header_signature_upload_info
        # 文件所存储的区域
        self.region = region
        self.sts_upload_info = sts_upload_info

    def validate(self):
        if self.header_signature_upload_info:
            self.header_signature_upload_info.validate()
        if self.sts_upload_info:
            self.sts_upload_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_signature_upload_info is not None:
            result['headerSignatureUploadInfo'] = self.header_signature_upload_info.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.sts_upload_info is not None:
            result['stsUploadInfo'] = self.sts_upload_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headerSignatureUploadInfo') is not None:
            temp_model = GetUploadInfoResponseBodyHeaderSignatureUploadInfo()
            self.header_signature_upload_info = temp_model.from_map(m['headerSignatureUploadInfo'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('stsUploadInfo') is not None:
            temp_model = GetUploadInfoResponseBodyStsUploadInfo()
            self.sts_upload_info = temp_model.from_map(m['stsUploadInfo'])
        return self


class GetUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUploadInfoResponseBody = None,
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
            temp_model = GetUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPrivilegeOfCustomSpaceHeaders(TeaModel):
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


class GrantPrivilegeOfCustomSpaceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        file_ids: List[str] = None,
        type: str = None,
        union_id: str = None,
        user_id: str = None,
    ):
        # 权限有效时间
        self.duration = duration
        # 授权访问的文件id列表
        self.file_ids = file_ids
        # 权限类型
        self.type = type
        # 用户id
        self.union_id = union_id
        # 被授予权限的员工id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.file_ids is not None:
            result['fileIds'] = self.file_ids
        if self.type is not None:
            result['type'] = self.type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fileIds') is not None:
            self.file_ids = m.get('fileIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GrantPrivilegeOfCustomSpaceResponse(TeaModel):
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


class InfoSpaceHeaders(TeaModel):
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


class InfoSpaceRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class InfoSpaceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 容量
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class InfoSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InfoSpaceResponseBody = None,
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
            temp_model = InfoSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilesHeaders(TeaModel):
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


class ListFilesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order_type: str = None,
        parent_id: str = None,
        union_id: str = None,
        with_icon: bool = None,
    ):
        # 分页长度
        self.max_results = max_results
        # 分页查询锚点
        self.next_token = next_token
        # 排序类型
        self.order_type = order_type
        # 父目录id
        self.parent_id = parent_id
        # 用户id
        self.union_id = union_id
        # 是否返回文件图标
        self.with_icon = with_icon

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
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        if self.with_icon is not None:
            result['withIcon'] = self.with_icon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        if m.get('withIcon') is not None:
            self.with_icon = m.get('withIcon')
        return self


class ListFilesResponseBodyFiles(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        icon: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
        thumbnail: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 文件图标
        self.icon = icon
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id
        # 文件缩略图
        self.thumbnail = thumbnail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.icon is not None:
            result['icon'] = self.icon
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        return self


class ListFilesResponseBody(TeaModel):
    def __init__(
        self,
        files: List[ListFilesResponseBodyFiles] = None,
        next_token: str = None,
    ):
        # 文件列表
        self.files = files
        # 分页加载锚点, nextToken不为空表示有更多数据
        self.next_token = next_token

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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ListFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFilesResponseBody = None,
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
            temp_model = ListFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsHeaders(TeaModel):
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


class ListPermissionsRequest(TeaModel):
    def __init__(
        self,
        union_id: str = None,
    ):
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ListPermissionsResponseBodyMembersMember(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_id: str = None,
        member_name: str = None,
        member_type: str = None,
    ):
        # 企业corpId
        self.corp_id = corp_id
        # 成员id
        self.member_id = member_id
        # 成员名称
        self.member_name = member_name
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_name is not None:
            result['memberName'] = self.member_name
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberName') is not None:
            self.member_name = m.get('memberName')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class ListPermissionsResponseBodyMembers(TeaModel):
    def __init__(
        self,
        extend: bool = None,
        member: ListPermissionsResponseBodyMembersMember = None,
        role: str = None,
    ):
        # 是否是继承的权限
        self.extend = extend
        # 成员信息
        self.member = member
        # 权限角色
        self.role = role

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
        if self.member is not None:
            result['member'] = self.member.to_map()
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('member') is not None:
            temp_model = ListPermissionsResponseBodyMembersMember()
            self.member = temp_model.from_map(m['member'])
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ListPermissionsResponseBodyOutMembersMember(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_id: str = None,
        member_name: str = None,
        member_type: str = None,
    ):
        # 企业corpId
        self.corp_id = corp_id
        # 成员id
        self.member_id = member_id
        # 成员名称
        self.member_name = member_name
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_name is not None:
            result['memberName'] = self.member_name
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberName') is not None:
            self.member_name = m.get('memberName')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class ListPermissionsResponseBodyOutMembers(TeaModel):
    def __init__(
        self,
        extend: bool = None,
        member: ListPermissionsResponseBodyOutMembersMember = None,
        role: str = None,
    ):
        # 是否是继承的权限
        self.extend = extend
        # 成员信息
        self.member = member
        # 权限角色
        self.role = role

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
        if self.member is not None:
            result['member'] = self.member.to_map()
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('member') is not None:
            temp_model = ListPermissionsResponseBodyOutMembersMember()
            self.member = temp_model.from_map(m['member'])
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        members: List[ListPermissionsResponseBodyMembers] = None,
        out_members: List[ListPermissionsResponseBodyOutMembers] = None,
    ):
        # 企业内成员权限列表
        self.members = members
        # 企业外成员权限列表
        self.out_members = out_members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.out_members:
            for k in self.out_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        result['outMembers'] = []
        if self.out_members is not None:
            for k in self.out_members:
                result['outMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = ListPermissionsResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        self.out_members = []
        if m.get('outMembers') is not None:
            for k in m.get('outMembers'):
                temp_model = ListPermissionsResponseBodyOutMembers()
                self.out_members.append(temp_model.from_map(k))
        return self


class ListPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPermissionsResponseBody = None,
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
            temp_model = ListPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycleFilesHeaders(TeaModel):
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


class ListRecycleFilesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order_type: str = None,
        recycle_type: str = None,
        union_id: str = None,
    ):
        # 分页长度
        self.max_results = max_results
        # 分页加载更多锚点
        self.next_token = next_token
        # 文件排序类型
        self.order_type = order_type
        # 回收站类型
        self.recycle_type = recycle_type
        # 用户id
        self.union_id = union_id

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
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.recycle_type is not None:
            result['recycleType'] = self.recycle_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('recycleType') is not None:
            self.recycle_type = m.get('recycleType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ListRecycleFilesResponseBodyRecycleItems(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        delete_staff_id: str = None,
        delete_time: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        recycle_item_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 删除员工工号
        self.delete_staff_id = delete_staff_id
        # 删除时间
        self.delete_time = delete_time
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 回收站item id
        self.recycle_item_id = recycle_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.delete_staff_id is not None:
            result['deleteStaffId'] = self.delete_staff_id
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.recycle_item_id is not None:
            result['recycleItemId'] = self.recycle_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('deleteStaffId') is not None:
            self.delete_staff_id = m.get('deleteStaffId')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('recycleItemId') is not None:
            self.recycle_item_id = m.get('recycleItemId')
        return self


class ListRecycleFilesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        recycle_items: List[ListRecycleFilesResponseBodyRecycleItems] = None,
    ):
        # 加载更多锚点, nextToken不为空表示有更多数据
        self.next_token = next_token
        # 回收站文件列表
        self.recycle_items = recycle_items

    def validate(self):
        if self.recycle_items:
            for k in self.recycle_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['recycleItems'] = []
        if self.recycle_items is not None:
            for k in self.recycle_items:
                result['recycleItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.recycle_items = []
        if m.get('recycleItems') is not None:
            for k in m.get('recycleItems'):
                temp_model = ListRecycleFilesResponseBodyRecycleItems()
                self.recycle_items.append(temp_model.from_map(k))
        return self


class ListRecycleFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRecycleFilesResponseBody = None,
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
            temp_model = ListRecycleFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpacesHeaders(TeaModel):
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


class ListSpacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        space_type: str = None,
        union_id: str = None,
    ):
        # 分页大小
        self.max_results = max_results
        # 分页加载锚点
        self.next_token = next_token
        # 空间类型
        self.space_type = space_type
        # 用户id
        self.union_id = union_id

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
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ListSpacesResponseBodySpaces(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 空间总额度
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 空间已使用额度
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class ListSpacesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        spaces: List[ListSpacesResponseBodySpaces] = None,
    ):
        # 分页加载更多锚点, nextToken不为空表示有更多数据
        self.next_token = next_token
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.spaces = []
        if m.get('spaces') is not None:
            for k in m.get('spaces'):
                temp_model = ListSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ListSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSpacesResponseBody = None,
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
            temp_model = ListSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManagementBuyQuotaHeaders(TeaModel):
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


class ManagementBuyQuotaRequestOrder(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        capacity: int = None,
        capacity_type: str = None,
        day: int = None,
        money: int = None,
        order_id: int = None,
    ):
        # 业务类型
        self.biz_type = biz_type
        # 待扩容的容量
        self.capacity = capacity
        # 容量类型
        self.capacity_type = capacity_type
        # 时长
        self.day = day
        # 金额
        self.money = money
        # 订单id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.capacity_type is not None:
            result['capacityType'] = self.capacity_type
        if self.day is not None:
            result['day'] = self.day
        if self.money is not None:
            result['money'] = self.money
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('capacityType') is not None:
            self.capacity_type = m.get('capacityType')
        if m.get('day') is not None:
            self.day = m.get('day')
        if m.get('money') is not None:
            self.money = m.get('money')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ManagementBuyQuotaRequest(TeaModel):
    def __init__(
        self,
        order: ManagementBuyQuotaRequestOrder = None,
        token: str = None,
        union_id: str = None,
    ):
        # 订单
        self.order = order
        # token
        self.token = token
        # 用户id
        self.union_id = union_id

    def validate(self):
        if self.order:
            self.order.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order.to_map()
        if self.token is not None:
            result['token'] = self.token
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            temp_model = ManagementBuyQuotaRequestOrder()
            self.order = temp_model.from_map(m['order'])
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ManagementBuyQuotaResponse(TeaModel):
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


class ManagementListSpacesHeaders(TeaModel):
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


class ManagementListSpacesRequest(TeaModel):
    def __init__(
        self,
        space_ids: List[str] = None,
        union_id: str = None,
    ):
        # 空间id列表
        self.space_ids = space_ids
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_ids is not None:
            result['spaceIds'] = self.space_ids
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spaceIds') is not None:
            self.space_ids = m.get('spaceIds')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ManagementListSpacesResponseBodySpaces(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 空间总额度
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 空间已使用额度
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class ManagementListSpacesResponseBody(TeaModel):
    def __init__(
        self,
        spaces: List[ManagementListSpacesResponseBodySpaces] = None,
    ):
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
        result['spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spaces = []
        if m.get('spaces') is not None:
            for k in m.get('spaces'):
                temp_model = ManagementListSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ManagementListSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ManagementListSpacesResponseBody = None,
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
            temp_model = ManagementListSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManagementModifySpaceHeaders(TeaModel):
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


class ManagementModifySpaceRequest(TeaModel):
    def __init__(
        self,
        quota: int = None,
        space_ids: List[str] = None,
        union_id: str = None,
    ):
        # 容量
        self.quota = quota
        # 空间id列表
        self.space_ids = space_ids
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['quota'] = self.quota
        if self.space_ids is not None:
            result['spaceIds'] = self.space_ids
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('spaceIds') is not None:
            self.space_ids = m.get('spaceIds')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ManagementModifySpaceResponseBodySpaces(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 修改时间
        self.modify_time = modify_time
        # 授权模式
        self.permission_mode = permission_mode
        # 空间总额度
        self.quota = quota
        # 空间id
        self.space_id = space_id
        # 空间名称
        self.space_name = space_name
        # 空间类型
        self.space_type = space_type
        # 空间已使用额度
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
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


class ManagementModifySpaceResponseBody(TeaModel):
    def __init__(
        self,
        spaces: List[ManagementModifySpaceResponseBodySpaces] = None,
    ):
        # 空间列表
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
        result['spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spaces = []
        if m.get('spaces') is not None:
            for k in m.get('spaces'):
                temp_model = ManagementModifySpaceResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ManagementModifySpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ManagementModifySpaceResponseBody = None,
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
            temp_model = ManagementModifySpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPermissionHeaders(TeaModel):
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


class ModifyPermissionRequestMembers(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # 企业corpId
        self.corp_id = corp_id
        # 成员id
        self.member_id = member_id
        # 成员类型
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_type is not None:
            result['memberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberType') is not None:
            self.member_type = m.get('memberType')
        return self


class ModifyPermissionRequest(TeaModel):
    def __init__(
        self,
        members: List[ModifyPermissionRequestMembers] = None,
        role: str = None,
        union_id: str = None,
    ):
        self.members = members
        # 权限角色
        self.role = role
        # 用户id
        self.union_id = union_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.role is not None:
            result['role'] = self.role
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = ModifyPermissionRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class ModifyPermissionResponse(TeaModel):
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


class MoveFileHeaders(TeaModel):
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


class MoveFileRequest(TeaModel):
    def __init__(
        self,
        add_conflict_policy: str = None,
        target_parent_id: str = None,
        target_space_id: str = None,
        union_id: str = None,
    ):
        # 文件名冲突策略
        self.add_conflict_policy = add_conflict_policy
        # 目标父目录id
        self.target_parent_id = target_parent_id
        # 目标空间id
        self.target_space_id = target_space_id
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_conflict_policy is not None:
            result['addConflictPolicy'] = self.add_conflict_policy
        if self.target_parent_id is not None:
            result['targetParentId'] = self.target_parent_id
        if self.target_space_id is not None:
            result['targetSpaceId'] = self.target_space_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addConflictPolicy') is not None:
            self.add_conflict_policy = m.get('addConflictPolicy')
        if m.get('targetParentId') is not None:
            self.target_parent_id = m.get('targetParentId')
        if m.get('targetSpaceId') is not None:
            self.target_space_id = m.get('targetSpaceId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class MoveFileResponseBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class MoveFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveFileResponseBody = None,
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
            temp_model = MoveFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFilesHeaders(TeaModel):
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


class MoveFilesRequest(TeaModel):
    def __init__(
        self,
        add_conflict_policy: str = None,
        file_ids: List[str] = None,
        target_parent_id: str = None,
        target_space_id: str = None,
        union_id: str = None,
    ):
        # 文件名冲突策略
        self.add_conflict_policy = add_conflict_policy
        # 文件id列表
        self.file_ids = file_ids
        # 目标父目录id
        self.target_parent_id = target_parent_id
        # 目标空间id
        self.target_space_id = target_space_id
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_conflict_policy is not None:
            result['addConflictPolicy'] = self.add_conflict_policy
        if self.file_ids is not None:
            result['fileIds'] = self.file_ids
        if self.target_parent_id is not None:
            result['targetParentId'] = self.target_parent_id
        if self.target_space_id is not None:
            result['targetSpaceId'] = self.target_space_id
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addConflictPolicy') is not None:
            self.add_conflict_policy = m.get('addConflictPolicy')
        if m.get('fileIds') is not None:
            self.file_ids = m.get('fileIds')
        if m.get('targetParentId') is not None:
            self.target_parent_id = m.get('targetParentId')
        if m.get('targetSpaceId') is not None:
            self.target_space_id = m.get('targetSpaceId')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class MoveFilesResponseBodyFiles(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class MoveFilesResponseBody(TeaModel):
    def __init__(
        self,
        files: List[MoveFilesResponseBodyFiles] = None,
        task_id: str = None,
    ):
        # 文件信息列表
        self.files = files
        # 异步任务id
        self.task_id = task_id

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
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = MoveFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class MoveFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveFilesResponseBody = None,
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
            temp_model = MoveFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverRecycleFilesHeaders(TeaModel):
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


class RecoverRecycleFilesRequest(TeaModel):
    def __init__(
        self,
        recycle_item_id_list: List[int] = None,
        recycle_type: str = None,
        union_id: str = None,
    ):
        # 回收站item id列表
        self.recycle_item_id_list = recycle_item_id_list
        # 回收站类型
        self.recycle_type = recycle_type
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recycle_item_id_list is not None:
            result['recycleItemIdList'] = self.recycle_item_id_list
        if self.recycle_type is not None:
            result['recycleType'] = self.recycle_type
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recycleItemIdList') is not None:
            self.recycle_item_id_list = m.get('recycleItemIdList')
        if m.get('recycleType') is not None:
            self.recycle_type = m.get('recycleType')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class RecoverRecycleFilesResponse(TeaModel):
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


class RenameFileHeaders(TeaModel):
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


class RenameFileRequest(TeaModel):
    def __init__(
        self,
        new_file_name: str = None,
        union_id: str = None,
    ):
        # 新文件名称
        self.new_file_name = new_file_name
        # 用户id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_file_name is not None:
            result['newFileName'] = self.new_file_name
        if self.union_id is not None:
            result['unionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newFileName') is not None:
            self.new_file_name = m.get('newFileName')
        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')
        return self


class RenameFileResponseBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        file_type: str = None,
        modifier: str = None,
        modify_time: str = None,
        parent_id: str = None,
        space_id: str = None,
    ):
        # 文件内容类型
        self.content_type = content_type
        # 创建时间
        self.create_time = create_time
        # 创建者
        self.creator = creator
        # 文件后缀
        self.file_extension = file_extension
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 文件路径
        self.file_path = file_path
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 修改者
        self.modifier = modifier
        # 修改时间
        self.modify_time = modify_time
        # 父目录id
        self.parent_id = parent_id
        # 空间id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.file_extension is not None:
            result['fileExtension'] = self.file_extension
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fileExtension') is not None:
            self.file_extension = m.get('fileExtension')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        return self


class RenameFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameFileResponseBody = None,
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
            temp_model = RenameFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


