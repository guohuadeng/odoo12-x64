# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class AlignObjectiveHeaders(TeaModel):
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


class AlignObjectiveRequest(TeaModel):
    def __init__(
        self,
        period_id: str = None,
        target_id: str = None,
        user_id: str = None,
    ):
        # 周期 ID。
        self.period_id = period_id
        # 对齐目标的 ID。
        self.target_id = target_id
        # 当前用户的 user ID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AlignObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        align_id: BinaryIO = None,
        id: BinaryIO = None,
    ):
        # 对齐目标的 ID。
        self.align_id = align_id
        # 当前 Objective 的ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align_id is not None:
            result['alignId'] = self.align_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignId') is not None:
            self.align_id = m.get('alignId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class AlignObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: AlignObjectiveResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # success
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AlignObjectiveResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AlignObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AlignObjectiveResponseBody = None,
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
            temp_model = AlignObjectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddPermissionHeaders(TeaModel):
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


class BatchAddPermissionRequestListMember(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BatchAddPermissionRequestList(TeaModel):
    def __init__(
        self,
        member: BatchAddPermissionRequestListMember = None,
        policy_type: int = None,
    ):
        self.member = member
        self.policy_type = policy_type

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member is not None:
            result['member'] = self.member.to_map()
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('member') is not None:
            temp_model = BatchAddPermissionRequestListMember()
            self.member = temp_model.from_map(m['member'])
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self


class BatchAddPermissionRequest(TeaModel):
    def __init__(
        self,
        list: List[BatchAddPermissionRequestList] = None,
        target_id: str = None,
        target_type: str = None,
        user_id: str = None,
    ):
        self.list = list
        self.target_id = target_id
        self.target_type = target_type
        # A short description of struct
        self.user_id = user_id

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
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = BatchAddPermissionRequestList()
                self.list.append(temp_model.from_map(k))
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class BatchAddPermissionResponseBodyDataPermissionTreePolicyListMemberList(TeaModel):
    def __init__(
        self,
        id: str = None,
        nickname: str = None,
        type: str = None,
    ):
        self.id = id
        self.nickname = nickname
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BatchAddPermissionResponseBodyDataPermissionTreePolicyList(TeaModel):
    def __init__(
        self,
        member_list: List[BatchAddPermissionResponseBodyDataPermissionTreePolicyListMemberList] = None,
        name: str = None,
        type: int = None,
    ):
        self.member_list = member_list
        self.name = name
        self.type = type

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['memberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['memberList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('memberList') is not None:
            for k in m.get('memberList'):
                temp_model = BatchAddPermissionResponseBodyDataPermissionTreePolicyListMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BatchAddPermissionResponseBodyDataPermissionTree(TeaModel):
    def __init__(
        self,
        id: str = None,
        policy_list: List[BatchAddPermissionResponseBodyDataPermissionTreePolicyList] = None,
        privacy: str = None,
        type: str = None,
    ):
        # 权限 ID。
        self.id = id
        # 权限列表
        self.policy_list = policy_list
        # 是否可见的标识。
        self.privacy = privacy
        # 哪种类型的权限。
        self.type = type

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        result['policyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['policyList'].append(k.to_map() if k else None)
        if self.privacy is not None:
            result['privacy'] = self.privacy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        self.policy_list = []
        if m.get('policyList') is not None:
            for k in m.get('policyList'):
                temp_model = BatchAddPermissionResponseBodyDataPermissionTreePolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('privacy') is not None:
            self.privacy = m.get('privacy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BatchAddPermissionResponseBodyData(TeaModel):
    def __init__(
        self,
        has_invalid_user: bool = None,
        permission_tree: BatchAddPermissionResponseBodyDataPermissionTree = None,
    ):
        # 是否有无效的成员。
        self.has_invalid_user = has_invalid_user
        # 权限信息。
        self.permission_tree = permission_tree

    def validate(self):
        if self.permission_tree:
            self.permission_tree.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_invalid_user is not None:
            result['hasInvalidUser'] = self.has_invalid_user
        if self.permission_tree is not None:
            result['permissionTree'] = self.permission_tree.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasInvalidUser') is not None:
            self.has_invalid_user = m.get('hasInvalidUser')
        if m.get('permissionTree') is not None:
            temp_model = BatchAddPermissionResponseBodyDataPermissionTree()
            self.permission_tree = temp_model.from_map(m['permissionTree'])
        return self


class BatchAddPermissionResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchAddPermissionResponseBodyData = None,
        success: bool = None,
    ):
        # 返回的数据。
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = BatchAddPermissionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchAddPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchAddPermissionResponseBody = None,
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
            temp_model = BatchAddPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryObjectiveHeaders(TeaModel):
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


class BatchQueryObjectiveRequest(TeaModel):
    def __init__(
        self,
        objective_ids: List[str] = None,
        period_id: str = None,
        with_align: bool = None,
        with_kr: bool = None,
        with_progress: bool = None,
        user_id: str = None,
    ):
        # 需要查看的 Objective ID。
        self.objective_ids = objective_ids
        # 周期 ID。
        self.period_id = period_id
        # 是否返回关联信息。
        self.with_align = with_align
        # 是否返回 KR 信息。
        self.with_kr = with_kr
        # 是否返回进度信息
        self.with_progress = with_progress
        # 当前用户的 staff ID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_ids is not None:
            result['objectiveIds'] = self.objective_ids
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.with_align is not None:
            result['withAlign'] = self.with_align
        if self.with_kr is not None:
            result['withKr'] = self.with_kr
        if self.with_progress is not None:
            result['withProgress'] = self.with_progress
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveIds') is not None:
            self.objective_ids = m.get('objectiveIds')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('withAlign') is not None:
            self.with_align = m.get('withAlign')
        if m.get('withKr') is not None:
            self.with_kr = m.get('withKr')
        if m.get('withProgress') is not None:
            self.with_progress = m.get('withProgress')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class BatchQueryObjectiveResponseBodyDataKrListProgress(TeaModel):
    def __init__(
        self,
        percent: int = None,
    ):
        # 百分比。
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class BatchQueryObjectiveResponseBodyDataKrList(TeaModel):
    def __init__(
        self,
        content: BinaryIO = None,
        gmt_create: float = None,
        gmt_modified: float = None,
        id: BinaryIO = None,
        objective_id: BinaryIO = None,
        permission: List[float] = None,
        position: int = None,
        progress: BatchQueryObjectiveResponseBodyDataKrListProgress = None,
        score: float = None,
        weight: float = None,
    ):
        # KR 内容。
        self.content = content
        # 创建时间。时间戳
        self.gmt_create = gmt_create
        # 更新时间。时间戳
        self.gmt_modified = gmt_modified
        # KR 的 ID。
        self.id = id
        # 所属 Objective ID。
        self.objective_id = objective_id
        # KR 权限。
        self.permission = permission
        # 所处位置。
        self.position = position
        # KR 进度。
        self.progress = progress
        # 所占分数。
        self.score = score
        # 所占权重。
        self.weight = weight

    def validate(self):
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.permission is not None:
            result['permission'] = self.permission
        if self.position is not None:
            result['position'] = self.position
        if self.progress is not None:
            result['progress'] = self.progress.to_map()
        if self.score is not None:
            result['score'] = self.score
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('progress') is not None:
            temp_model = BatchQueryObjectiveResponseBodyDataKrListProgress()
            self.progress = temp_model.from_map(m['progress'])
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class BatchQueryObjectiveResponseBodyDataOwner(TeaModel):
    def __init__(
        self,
        avatar_media_id: BinaryIO = None,
        corp_id: BinaryIO = None,
        id: BinaryIO = None,
        nickname: BinaryIO = None,
        user_id: BinaryIO = None,
    ):
        # 所属者头像。 ID
        self.avatar_media_id = avatar_media_id
        # 所属者组织 I。D
        self.corp_id = corp_id
        # 所属者在 OKR 系统中的 ID。
        self.id = id
        # 所属者昵称。
        self.nickname = nickname
        # 所属者 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_media_id is not None:
            result['avatarMediaId'] = self.avatar_media_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarMediaId') is not None:
            self.avatar_media_id = m.get('avatarMediaId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class BatchQueryObjectiveResponseBodyDataProgress(TeaModel):
    def __init__(
        self,
        percent: int = None,
    ):
        # 百分比。
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class BatchQueryObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        align_from_ids: List[BinaryIO] = None,
        align_to_ids: List[BinaryIO] = None,
        content: BinaryIO = None,
        gmt_create: float = None,
        gmt_modified: float = None,
        id: BinaryIO = None,
        kr_list: List[BatchQueryObjectiveResponseBodyDataKrList] = None,
        owner: BatchQueryObjectiveResponseBodyDataOwner = None,
        period_id: BinaryIO = None,
        permission: List[float] = None,
        position: int = None,
        progress: BatchQueryObjectiveResponseBodyDataProgress = None,
        progress_percent: float = None,
        published: bool = None,
        score: float = None,
        status: int = None,
        user_id: BinaryIO = None,
        weight: float = None,
    ):
        # 被对齐的 Objective。
        self.align_from_ids = align_from_ids
        # 对齐的 Objective。
        self.align_to_ids = align_to_ids
        # Objective 内容。
        self.content = content
        # 创建时间。时间戳
        self.gmt_create = gmt_create
        # 更新时间。时间戳
        self.gmt_modified = gmt_modified
        # objective。
        self.id = id
        # KR 详情列表。
        self.kr_list = kr_list
        # 所属者信息。
        self.owner = owner
        # 周期 ID。
        self.period_id = period_id
        # 权限值。
        self.permission = permission
        # 所在位置。
        self.position = position
        # 进度值。
        self.progress = progress
        # 百分比值。
        self.progress_percent = progress_percent
        # 是否已发布。
        self.published = published
        # 分数值。
        self.score = score
        # 当前内容状态。
        self.status = status
        # 用户 ID。
        self.user_id = user_id
        # 权重值。
        self.weight = weight

    def validate(self):
        if self.kr_list:
            for k in self.kr_list:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align_from_ids is not None:
            result['alignFromIds'] = self.align_from_ids
        if self.align_to_ids is not None:
            result['alignToIds'] = self.align_to_ids
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        result['krList'] = []
        if self.kr_list is not None:
            for k in self.kr_list:
                result['krList'].append(k.to_map() if k else None)
        if self.owner is not None:
            result['owner'] = self.owner.to_map()
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.permission is not None:
            result['permission'] = self.permission
        if self.position is not None:
            result['position'] = self.position
        if self.progress is not None:
            result['progress'] = self.progress.to_map()
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.published is not None:
            result['published'] = self.published
        if self.score is not None:
            result['score'] = self.score
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignFromIds') is not None:
            self.align_from_ids = m.get('alignFromIds')
        if m.get('alignToIds') is not None:
            self.align_to_ids = m.get('alignToIds')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.kr_list = []
        if m.get('krList') is not None:
            for k in m.get('krList'):
                temp_model = BatchQueryObjectiveResponseBodyDataKrList()
                self.kr_list.append(temp_model.from_map(k))
        if m.get('owner') is not None:
            temp_model = BatchQueryObjectiveResponseBodyDataOwner()
            self.owner = temp_model.from_map(m['owner'])
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('progress') is not None:
            temp_model = BatchQueryObjectiveResponseBodyDataProgress()
            self.progress = temp_model.from_map(m['progress'])
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class BatchQueryObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: List[BatchQueryObjectiveResponseBodyData] = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = BatchQueryObjectiveResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchQueryObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchQueryObjectiveResponseBody = None,
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
            temp_model = BatchQueryObjectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryUserHeaders(TeaModel):
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


class BatchQueryUserRequest(TeaModel):
    def __init__(
        self,
        user_ids: List[str] = None,
    ):
        # 需要查询的用户ID
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self


class BatchQueryUserResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_media_id: BinaryIO = None,
        avatar_url: BinaryIO = None,
        corp_id: BinaryIO = None,
        id: BinaryIO = None,
        nickname: BinaryIO = None,
        user_id: BinaryIO = None,
    ):
        # 所属者头像。 ID
        self.avatar_media_id = avatar_media_id
        # 所属者头像。 URL
        self.avatar_url = avatar_url
        # 所属者组织 I。D
        self.corp_id = corp_id
        # 所属者在 OKR 系统中的 ID。
        self.id = id
        # 所属者昵称。
        self.nickname = nickname
        # 所属者 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_media_id is not None:
            result['avatarMediaId'] = self.avatar_media_id
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarMediaId') is not None:
            self.avatar_media_id = m.get('avatarMediaId')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class BatchQueryUserResponseBody(TeaModel):
    def __init__(
        self,
        data: List[BatchQueryUserResponseBodyData] = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = BatchQueryUserResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchQueryUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchQueryUserResponseBody = None,
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
            temp_model = BatchQueryUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyResultHeaders(TeaModel):
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


class CreateKeyResultRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        objective_id: str = None,
        period_id: str = None,
        prev_position: int = None,
        weight: int = None,
        user_id: str = None,
    ):
        # KR 内容。
        self.content = content
        # 所属 Objective ID。
        self.objective_id = objective_id
        # 周期 ID。
        self.period_id = period_id
        # 上一个 KR 的位置。
        self.prev_position = prev_position
        # KR 的权重比。
        self.weight = weight
        # 当前用户的 user ID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.prev_position is not None:
            result['prevPosition'] = self.prev_position
        if self.weight is not None:
            result['weight'] = self.weight
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('prevPosition') is not None:
            self.prev_position = m.get('prevPosition')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateKeyResultResponseBodyData(TeaModel):
    def __init__(
        self,
        id: BinaryIO = None,
        position: int = None,
        weight: int = None,
    ):
        # 创建成功的 KR ID。
        self.id = id
        # KR的位置。
        self.position = position
        # KR 的权重。
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.position is not None:
            result['position'] = self.position
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreateKeyResultResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateKeyResultResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateKeyResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateKeyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateKeyResultResponseBody = None,
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
            temp_model = CreateKeyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateObjectiveHeaders(TeaModel):
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


class CreateObjectiveRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        period_id: str = None,
        prev_position: str = None,
        user_id: str = None,
    ):
        # 创建Objective 的内容
        self.content = content
        # 当前周期 ID。
        self.period_id = period_id
        # 上一个 Objective 的位置。
        self.prev_position = prev_position
        # 当前用户的 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.prev_position is not None:
            result['prevPosition'] = self.prev_position
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('prevPosition') is not None:
            self.prev_position = m.get('prevPosition')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        position: str = None,
    ):
        # 当前 Objective ID。
        self.id = id
        # 当前 Objective 的位置。
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self


class CreateObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateObjectiveResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateObjectiveResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateObjectiveResponseBody = None,
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
            temp_model = CreateObjectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyResultHeaders(TeaModel):
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


class DeleteKeyResultRequest(TeaModel):
    def __init__(
        self,
        kr_id: str = None,
        user_id: str = None,
    ):
        # 当前 KR id。
        self.kr_id = kr_id
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteKeyResultResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        success: bool = None,
    ):
        # 返回的信息
        self.data = data
        # 请求成功的标识。
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteKeyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteKeyResultResponseBody = None,
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
            temp_model = DeleteKeyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteObjectiveHeaders(TeaModel):
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


class DeleteObjectiveRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 当前用户的 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 当前 Objective ID。
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteObjectiveResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeleteObjectiveResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteObjectiveResponseBody = None,
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
            temp_model = DeleteObjectiveResponseBody()
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


class DeletePermissionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        policy_type: int = None,
        target_id: str = None,
        target_type: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.id = id
        self.policy_type = policy_type
        self.target_id = target_id
        self.target_type = target_type
        self.type = type
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeletePermissionResponseBodyDataPolicyListMemberList(TeaModel):
    def __init__(
        self,
        id: str = None,
        nickname: str = None,
        type: str = None,
    ):
        self.id = id
        self.nickname = nickname
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeletePermissionResponseBodyDataPolicyList(TeaModel):
    def __init__(
        self,
        member_list: List[DeletePermissionResponseBodyDataPolicyListMemberList] = None,
        name: str = None,
        type: int = None,
    ):
        self.member_list = member_list
        self.name = name
        self.type = type

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['memberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['memberList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('memberList') is not None:
            for k in m.get('memberList'):
                temp_model = DeletePermissionResponseBodyDataPolicyListMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeletePermissionResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        policy_list: List[DeletePermissionResponseBodyDataPolicyList] = None,
        privacy: str = None,
        type: str = None,
    ):
        self.id = id
        # 权限列表
        self.policy_list = policy_list
        # 是否可见的标识。
        self.privacy = privacy
        # 哪种类型的权限。
        self.type = type

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        result['policyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['policyList'].append(k.to_map() if k else None)
        if self.privacy is not None:
            result['privacy'] = self.privacy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        self.policy_list = []
        if m.get('policyList') is not None:
            for k in m.get('policyList'):
                temp_model = DeletePermissionResponseBodyDataPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('privacy') is not None:
            self.privacy = m.get('privacy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeletePermissionResponseBody(TeaModel):
    def __init__(
        self,
        data: DeletePermissionResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeletePermissionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeletePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePermissionResponseBody = None,
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
            temp_model = DeletePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPeriodListHeaders(TeaModel):
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


class GetPeriodListResponseBodyDataPeriodList(TeaModel):
    def __init__(
        self,
        end_time: float = None,
        id: BinaryIO = None,
        is_current: bool = None,
        is_yearly: bool = None,
        name: BinaryIO = None,
        start_time: float = None,
    ):
        self.end_time = end_time
        self.id = id
        self.is_current = is_current
        self.is_yearly = is_yearly
        self.name = name
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
        if self.id is not None:
            result['id'] = self.id
        if self.is_current is not None:
            result['isCurrent'] = self.is_current
        if self.is_yearly is not None:
            result['isYearly'] = self.is_yearly
        if self.name is not None:
            result['name'] = self.name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isCurrent') is not None:
            self.is_current = m.get('isCurrent')
        if m.get('isYearly') is not None:
            self.is_yearly = m.get('isYearly')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetPeriodListResponseBodyData(TeaModel):
    def __init__(
        self,
        period_list: List[GetPeriodListResponseBodyDataPeriodList] = None,
    ):
        self.period_list = period_list

    def validate(self):
        if self.period_list:
            for k in self.period_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['periodList'] = []
        if self.period_list is not None:
            for k in self.period_list:
                result['periodList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.period_list = []
        if m.get('periodList') is not None:
            for k in m.get('periodList'):
                temp_model = GetPeriodListResponseBodyDataPeriodList()
                self.period_list.append(temp_model.from_map(k))
        return self


class GetPeriodListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPeriodListResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # success
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPeriodListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPeriodListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPeriodListResponseBody = None,
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
            temp_model = GetPeriodListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionHeaders(TeaModel):
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


class GetPermissionRequest(TeaModel):
    def __init__(
        self,
        target_id: str = None,
        target_type: str = None,
        user_id: str = None,
        with_kr: bool = None,
        with_objective: bool = None,
    ):
        self.target_id = target_id
        self.target_type = target_type
        # A short description of struct
        self.user_id = user_id
        self.with_kr = with_kr
        self.with_objective = with_objective

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.with_kr is not None:
            result['withKr'] = self.with_kr
        if self.with_objective is not None:
            result['withObjective'] = self.with_objective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('withKr') is not None:
            self.with_kr = m.get('withKr')
        if m.get('withObjective') is not None:
            self.with_objective = m.get('withObjective')
        return self


class GetPermissionResponseBodyDataPolicyListMemberList(TeaModel):
    def __init__(
        self,
        id: str = None,
        nickname: str = None,
        type: str = None,
    ):
        self.id = id
        self.nickname = nickname
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPermissionResponseBodyDataPolicyList(TeaModel):
    def __init__(
        self,
        member_list: List[GetPermissionResponseBodyDataPolicyListMemberList] = None,
        name: str = None,
        type: int = None,
    ):
        self.member_list = member_list
        self.name = name
        self.type = type

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['memberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['memberList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('memberList') is not None:
            for k in m.get('memberList'):
                temp_model = GetPermissionResponseBodyDataPolicyListMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPermissionResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        policy_list: List[GetPermissionResponseBodyDataPolicyList] = None,
        privacy: str = None,
        type: str = None,
    ):
        self.id = id
        # 权限列表
        self.policy_list = policy_list
        # 是否可见的标识。
        self.privacy = privacy
        # 哪种类型的权限。
        self.type = type

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        result['policyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['policyList'].append(k.to_map() if k else None)
        if self.privacy is not None:
            result['privacy'] = self.privacy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        self.policy_list = []
        if m.get('policyList') is not None:
            for k in m.get('policyList'):
                temp_model = GetPermissionResponseBodyDataPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('privacy') is not None:
            self.privacy = m.get('privacy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPermissionResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPermissionResponseBodyData = None,
        success: bool = None,
    ):
        # 返回的数据。
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPermissionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPermissionResponseBody = None,
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
            temp_model = GetPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserOkrHeaders(TeaModel):
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


class GetUserOkrRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        period_id: str = None,
        user_id: str = None,
    ):
        # 页码，默认 为 1。
        self.page_number = page_number
        # 每页的个数，默认100。
        self.page_size = page_size
        # 周期 ID。
        self.period_id = period_id
        # 当前用户的user ID。
        self.user_id = user_id

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
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserOkrResponseBodyDataListKrListProgress(TeaModel):
    def __init__(
        self,
        percent: int = None,
    ):
        # 百分比。
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class GetUserOkrResponseBodyDataListKrList(TeaModel):
    def __init__(
        self,
        content: BinaryIO = None,
        gmt_create: float = None,
        gmt_modified: float = None,
        id: BinaryIO = None,
        objective_id: BinaryIO = None,
        permission: List[float] = None,
        position: int = None,
        progress: GetUserOkrResponseBodyDataListKrListProgress = None,
        score: float = None,
        weight: float = None,
    ):
        # KR 内容。
        self.content = content
        # 创建时间。时间戳
        self.gmt_create = gmt_create
        # 更新时间。时间戳
        self.gmt_modified = gmt_modified
        # KR 的 ID。
        self.id = id
        # 所属 Objective ID。
        self.objective_id = objective_id
        # KR 权限。
        self.permission = permission
        # 所处位置。
        self.position = position
        # KR 进度。
        self.progress = progress
        # 所占分数。
        self.score = score
        # 所占权重。
        self.weight = weight

    def validate(self):
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.permission is not None:
            result['permission'] = self.permission
        if self.position is not None:
            result['position'] = self.position
        if self.progress is not None:
            result['progress'] = self.progress.to_map()
        if self.score is not None:
            result['score'] = self.score
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('progress') is not None:
            temp_model = GetUserOkrResponseBodyDataListKrListProgress()
            self.progress = temp_model.from_map(m['progress'])
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetUserOkrResponseBodyDataListOwner(TeaModel):
    def __init__(
        self,
        avatar_media_id: BinaryIO = None,
        corp_id: BinaryIO = None,
        id: BinaryIO = None,
        nickname: BinaryIO = None,
        user_id: BinaryIO = None,
    ):
        # 所属者头像。 ID
        self.avatar_media_id = avatar_media_id
        # 所属者组织 I。D
        self.corp_id = corp_id
        # 所属者 OKR 系统中的 ID。
        self.id = id
        # 所属者昵称。
        self.nickname = nickname
        # 所属者 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_media_id is not None:
            result['avatarMediaId'] = self.avatar_media_id
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarMediaId') is not None:
            self.avatar_media_id = m.get('avatarMediaId')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserOkrResponseBodyDataListProgress(TeaModel):
    def __init__(
        self,
        percent: int = None,
    ):
        # 百分比。
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class GetUserOkrResponseBodyDataList(TeaModel):
    def __init__(
        self,
        align_from_ids: List[BinaryIO] = None,
        align_to_ids: List[BinaryIO] = None,
        content: BinaryIO = None,
        gmt_create: float = None,
        gmt_modified: float = None,
        id: BinaryIO = None,
        kr_list: List[GetUserOkrResponseBodyDataListKrList] = None,
        owner: GetUserOkrResponseBodyDataListOwner = None,
        period_id: BinaryIO = None,
        permission: List[float] = None,
        position: int = None,
        progress: GetUserOkrResponseBodyDataListProgress = None,
        progress_percent: float = None,
        published: bool = None,
        score: float = None,
        status: int = None,
        user_id: BinaryIO = None,
        weight: float = None,
    ):
        # 被对齐的 Objective。
        self.align_from_ids = align_from_ids
        # 对齐的 Objective。
        self.align_to_ids = align_to_ids
        # Objective 内容。
        self.content = content
        # 创建时间。时间戳
        self.gmt_create = gmt_create
        # 更新时间。时间戳
        self.gmt_modified = gmt_modified
        # objective。
        self.id = id
        # KR 详情列表。
        self.kr_list = kr_list
        # 所属者信息。
        self.owner = owner
        # 周期 ID。
        self.period_id = period_id
        # 权限值。
        self.permission = permission
        # 所在位置。
        self.position = position
        # 进度值。
        self.progress = progress
        # 百分比值。
        self.progress_percent = progress_percent
        # 是否已发布。
        self.published = published
        # 分数值。
        self.score = score
        # 当前内容状态。
        self.status = status
        # 用户 ID。
        self.user_id = user_id
        # 权重值。
        self.weight = weight

    def validate(self):
        if self.kr_list:
            for k in self.kr_list:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align_from_ids is not None:
            result['alignFromIds'] = self.align_from_ids
        if self.align_to_ids is not None:
            result['alignToIds'] = self.align_to_ids
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        result['krList'] = []
        if self.kr_list is not None:
            for k in self.kr_list:
                result['krList'].append(k.to_map() if k else None)
        if self.owner is not None:
            result['owner'] = self.owner.to_map()
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.permission is not None:
            result['permission'] = self.permission
        if self.position is not None:
            result['position'] = self.position
        if self.progress is not None:
            result['progress'] = self.progress.to_map()
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.published is not None:
            result['published'] = self.published
        if self.score is not None:
            result['score'] = self.score
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignFromIds') is not None:
            self.align_from_ids = m.get('alignFromIds')
        if m.get('alignToIds') is not None:
            self.align_to_ids = m.get('alignToIds')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.kr_list = []
        if m.get('krList') is not None:
            for k in m.get('krList'):
                temp_model = GetUserOkrResponseBodyDataListKrList()
                self.kr_list.append(temp_model.from_map(k))
        if m.get('owner') is not None:
            temp_model = GetUserOkrResponseBodyDataListOwner()
            self.owner = temp_model.from_map(m['owner'])
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('progress') is not None:
            temp_model = GetUserOkrResponseBodyDataListProgress()
            self.progress = temp_model.from_map(m['progress'])
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetUserOkrResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetUserOkrResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # OKR 列表详情。
        self.list = list
        # 当前页码。
        self.page_number = page_number
        # 每一页的个数。
        self.page_size = page_size
        # 总数。
        self.total_count = total_count

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
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetUserOkrResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetUserOkrResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserOkrResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetUserOkrResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetUserOkrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserOkrResponseBody = None,
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
            temp_model = GetUserOkrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAlignObjectiveHeaders(TeaModel):
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


class UnAlignObjectiveRequest(TeaModel):
    def __init__(
        self,
        period_id: str = None,
        target_id: str = None,
        user_id: str = None,
    ):
        # 周期 ID
        self.period_id = period_id
        # 对齐目标的 ID
        self.target_id = target_id
        # 当前用户的 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_id is not None:
            result['periodId'] = self.period_id
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('periodId') is not None:
            self.period_id = m.get('periodId')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UnAlignObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        align_id: BinaryIO = None,
        id: BinaryIO = None,
    ):
        # 对齐的 Objective ID。
        self.align_id = align_id
        # 当前 Objective ID。
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align_id is not None:
            result['alignId'] = self.align_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignId') is not None:
            self.align_id = m.get('alignId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UnAlignObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: UnAlignObjectiveResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # success
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UnAlignObjectiveResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UnAlignObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnAlignObjectiveResponseBody = None,
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
            temp_model = UnAlignObjectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKROfContentHeaders(TeaModel):
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


class UpdateKROfContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        update_quote_list: List[str] = None,
        kr_id: str = None,
        user_id: str = None,
    ):
        # KR的内容。
        self.content = content
        # 待更新的划词 ID 列表。
        self.update_quote_list = update_quote_list
        # 当前 KR ID。
        self.kr_id = kr_id
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.update_quote_list is not None:
            result['updateQuoteList'] = self.update_quote_list
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('updateQuoteList') is not None:
            self.update_quote_list = m.get('updateQuoteList')
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateKROfContentResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        success: bool = None,
    ):
        self.data = data
        # 请求成功的标识。
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateKROfContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKROfContentResponseBody = None,
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
            temp_model = UpdateKROfContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKROfScoreHeaders(TeaModel):
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


class UpdateKROfScoreRequest(TeaModel):
    def __init__(
        self,
        score: int = None,
        kr_id: str = None,
        user_id: str = None,
    ):
        # 分数值。
        self.score = score
        # 当前 KR ID。
        self.kr_id = kr_id
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['score'] = self.score
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateKROfScoreResponseBodyData(TeaModel):
    def __init__(
        self,
        objective_score: int = None,
    ):
        # 目标分数。
        self.objective_score = objective_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_score is not None:
            result['objectiveScore'] = self.objective_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveScore') is not None:
            self.objective_score = m.get('objectiveScore')
        return self


class UpdateKROfScoreResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateKROfScoreResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateKROfScoreResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateKROfScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKROfScoreResponseBody = None,
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
            temp_model = UpdateKROfScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKROfWeightHeaders(TeaModel):
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


class UpdateKROfWeightRequest(TeaModel):
    def __init__(
        self,
        weight: int = None,
        kr_id: str = None,
        user_id: str = None,
    ):
        # 权重比。
        self.weight = weight
        # 当前 KR ID。
        self.kr_id = kr_id
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['weight'] = self.weight
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateKROfWeightResponseBodyDataObjectiveProgress(TeaModel):
    def __init__(
        self,
        percent: int = None,
    ):
        # 目标百分比。
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class UpdateKROfWeightResponseBodyData(TeaModel):
    def __init__(
        self,
        objective_progress: UpdateKROfWeightResponseBodyDataObjectiveProgress = None,
        objective_score: int = None,
    ):
        self.objective_progress = objective_progress
        # 目标分数。
        self.objective_score = objective_score

    def validate(self):
        if self.objective_progress:
            self.objective_progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_progress is not None:
            result['objectiveProgress'] = self.objective_progress.to_map()
        if self.objective_score is not None:
            result['objectiveScore'] = self.objective_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveProgress') is not None:
            temp_model = UpdateKROfWeightResponseBodyDataObjectiveProgress()
            self.objective_progress = temp_model.from_map(m['objectiveProgress'])
        if m.get('objectiveScore') is not None:
            self.objective_score = m.get('objectiveScore')
        return self


class UpdateKROfWeightResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateKROfWeightResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateKROfWeightResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateKROfWeightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKROfWeightResponseBody = None,
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
            temp_model = UpdateKROfWeightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateObjectiveHeaders(TeaModel):
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


class UpdateObjectiveRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        user_id: str = None,
    ):
        # 当前 Objective 的内容。
        self.content = content
        # 当前用户的 userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateObjectiveResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        position: float = None,
    ):
        # 当前 Objective ID。
        self.id = id
        # 当前 Objective 的位置。
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self


class UpdateObjectiveResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateObjectiveResponseBodyData = None,
        success: bool = None,
    ):
        # data
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateObjectiveResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateObjectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateObjectiveResponseBody = None,
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
            temp_model = UpdateObjectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivacyHeaders(TeaModel):
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


class UpdatePrivacyRequest(TeaModel):
    def __init__(
        self,
        privacy: str = None,
        target_id: str = None,
        target_type: str = None,
        user_id: str = None,
    ):
        # 权限修改的类型
        self.privacy = privacy
        # 当前目标的 ID
        self.target_id = target_id
        # 当前目标的权限类型。
        self.target_type = target_type
        # 当前用户的userId。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy is not None:
            result['privacy'] = self.privacy
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privacy') is not None:
            self.privacy = m.get('privacy')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdatePrivacyResponseBodyDataPolicyListMemberList(TeaModel):
    def __init__(
        self,
        id: str = None,
        nickname: str = None,
        type: str = None,
    ):
        self.id = id
        self.nickname = nickname
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdatePrivacyResponseBodyDataPolicyList(TeaModel):
    def __init__(
        self,
        member_list: List[UpdatePrivacyResponseBodyDataPolicyListMemberList] = None,
        name: str = None,
        type: int = None,
    ):
        self.member_list = member_list
        self.name = name
        self.type = type

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['memberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['memberList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('memberList') is not None:
            for k in m.get('memberList'):
                temp_model = UpdatePrivacyResponseBodyDataPolicyListMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdatePrivacyResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        policy_list: List[UpdatePrivacyResponseBodyDataPolicyList] = None,
        privacy: str = None,
        type: str = None,
    ):
        self.id = id
        # 权限列表
        self.policy_list = policy_list
        # 是否可见的标识。
        self.privacy = privacy
        # 哪种类型的权限。
        self.type = type

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        result['policyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['policyList'].append(k.to_map() if k else None)
        if self.privacy is not None:
            result['privacy'] = self.privacy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        self.policy_list = []
        if m.get('policyList') is not None:
            for k in m.get('policyList'):
                temp_model = UpdatePrivacyResponseBodyDataPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('privacy') is not None:
            self.privacy = m.get('privacy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdatePrivacyResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdatePrivacyResponseBodyData = None,
        success: bool = None,
    ):
        # 返回的数据。
        self.data = data
        # 请求成功的标识。
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdatePrivacyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdatePrivacyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePrivacyResponseBody = None,
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
            temp_model = UpdatePrivacyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


