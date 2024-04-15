# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GrantHonorHeaders(TeaModel):
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


class GrantHonorRequest(TeaModel):
    def __init__(
        self,
        expiration_time: str = None,
        grant_reason: str = None,
        granter_name: str = None,
        notice_announcer: bool = None,
        notice_single: bool = None,
        receiver_user_ids: List[str] = None,
        sender_user_id: str = None,
    ):
        # 有效期到期时间 时间戳. 会处理成到期那天的23:59:59秒的时间戳
        self.expiration_time = expiration_time
        # 颁奖词，最多可以填50字
        self.grant_reason = grant_reason
        # 颁奖人名字，最多15个字
        self.granter_name = granter_name
        # 是否使用官宣号通知获奖人
        self.notice_announcer = notice_announcer
        # 是否触达单聊会话通知
        self.notice_single = notice_single
        # 接受人staffId
        self.receiver_user_ids = receiver_user_ids
        # 发送人userId
        self.sender_user_id = sender_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.grant_reason is not None:
            result['grantReason'] = self.grant_reason
        if self.granter_name is not None:
            result['granterName'] = self.granter_name
        if self.notice_announcer is not None:
            result['noticeAnnouncer'] = self.notice_announcer
        if self.notice_single is not None:
            result['noticeSingle'] = self.notice_single
        if self.receiver_user_ids is not None:
            result['receiverUserIds'] = self.receiver_user_ids
        if self.sender_user_id is not None:
            result['senderUserId'] = self.sender_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('grantReason') is not None:
            self.grant_reason = m.get('grantReason')
        if m.get('granterName') is not None:
            self.granter_name = m.get('granterName')
        if m.get('noticeAnnouncer') is not None:
            self.notice_announcer = m.get('noticeAnnouncer')
        if m.get('noticeSingle') is not None:
            self.notice_single = m.get('noticeSingle')
        if m.get('receiverUserIds') is not None:
            self.receiver_user_ids = m.get('receiverUserIds')
        if m.get('senderUserId') is not None:
            self.sender_user_id = m.get('senderUserId')
        return self


class GrantHonorResponseBodyResult(TeaModel):
    def __init__(
        self,
        failed_user_ids: List[str] = None,
        success_user_ids: List[str] = None,
    ):
        # 失败的userId
        self.failed_user_ids = failed_user_ids
        # 成功的userId
        self.success_user_ids = success_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_user_ids is not None:
            result['failedUserIds'] = self.failed_user_ids
        if self.success_user_ids is not None:
            result['successUserIds'] = self.success_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedUserIds') is not None:
            self.failed_user_ids = m.get('failedUserIds')
        if m.get('successUserIds') is not None:
            self.success_user_ids = m.get('successUserIds')
        return self


class GrantHonorResponseBody(TeaModel):
    def __init__(
        self,
        result: GrantHonorResponseBodyResult = None,
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
            temp_model = GrantHonorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GrantHonorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantHonorResponseBody = None,
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
            temp_model = GrantHonorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrgHonorsHeaders(TeaModel):
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


class QueryOrgHonorsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryOrgHonorsResponseBodyResultOpenHonors(TeaModel):
    def __init__(
        self,
        honor_desc: str = None,
        honor_id: int = None,
        honor_img_url: str = None,
        honor_name: str = None,
        honor_pendant_img_url: str = None,
    ):
        # 荣誉含义
        self.honor_desc = honor_desc
        # 荣誉id
        self.honor_id = honor_id
        # 荣誉图片url
        self.honor_img_url = honor_img_url
        # 荣誉名字
        self.honor_name = honor_name
        # 荣誉附赠的挂件图url
        self.honor_pendant_img_url = honor_pendant_img_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.honor_desc is not None:
            result['honorDesc'] = self.honor_desc
        if self.honor_id is not None:
            result['honorId'] = self.honor_id
        if self.honor_img_url is not None:
            result['honorImgUrl'] = self.honor_img_url
        if self.honor_name is not None:
            result['honorName'] = self.honor_name
        if self.honor_pendant_img_url is not None:
            result['honorPendantImgUrl'] = self.honor_pendant_img_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('honorDesc') is not None:
            self.honor_desc = m.get('honorDesc')
        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')
        if m.get('honorImgUrl') is not None:
            self.honor_img_url = m.get('honorImgUrl')
        if m.get('honorName') is not None:
            self.honor_name = m.get('honorName')
        if m.get('honorPendantImgUrl') is not None:
            self.honor_pendant_img_url = m.get('honorPendantImgUrl')
        return self


class QueryOrgHonorsResponseBodyResult(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        open_honors: List[QueryOrgHonorsResponseBodyResultOpenHonors] = None,
    ):
        # 下次获取数据的游标
        self.next_token = next_token
        self.open_honors = open_honors

    def validate(self):
        if self.open_honors:
            for k in self.open_honors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['openHonors'] = []
        if self.open_honors is not None:
            for k in self.open_honors:
                result['openHonors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.open_honors = []
        if m.get('openHonors') is not None:
            for k in m.get('openHonors'):
                temp_model = QueryOrgHonorsResponseBodyResultOpenHonors()
                self.open_honors.append(temp_model.from_map(k))
        return self


class QueryOrgHonorsResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryOrgHonorsResponseBodyResult = None,
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
            temp_model = QueryOrgHonorsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryOrgHonorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrgHonorsResponseBody = None,
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
            temp_model = QueryOrgHonorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserHonorsHeaders(TeaModel):
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


class QueryUserHonorsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryUserHonorsResponseBodyResultHonorsGrantHistory(TeaModel):
    def __init__(
        self,
        grant_time: int = None,
        sender_userid: str = None,
    ):
        # 授予时间 时间戳
        self.grant_time = grant_time
        # 必须。荣誉发放人userid
        self.sender_userid = sender_userid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_time is not None:
            result['grantTime'] = self.grant_time
        if self.sender_userid is not None:
            result['senderUserid'] = self.sender_userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grantTime') is not None:
            self.grant_time = m.get('grantTime')
        if m.get('senderUserid') is not None:
            self.sender_userid = m.get('senderUserid')
        return self


class QueryUserHonorsResponseBodyResultHonors(TeaModel):
    def __init__(
        self,
        expiration_time: int = None,
        grant_history: List[QueryUserHonorsResponseBodyResultHonorsGrantHistory] = None,
        honor_desc: str = None,
        honor_id: str = None,
        honor_name: str = None,
    ):
        # 有效期截止时间点，没有该属性则为永久生效
        self.expiration_time = expiration_time
        # 授予历史记录 包含用户及授予时间
        self.grant_history = grant_history
        # 荣誉含义
        self.honor_desc = honor_desc
        # 必须。荣誉id
        self.honor_id = honor_id
        # 必须。荣誉名字
        self.honor_name = honor_name

    def validate(self):
        if self.grant_history:
            for k in self.grant_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        result['grantHistory'] = []
        if self.grant_history is not None:
            for k in self.grant_history:
                result['grantHistory'].append(k.to_map() if k else None)
        if self.honor_desc is not None:
            result['honorDesc'] = self.honor_desc
        if self.honor_id is not None:
            result['honorId'] = self.honor_id
        if self.honor_name is not None:
            result['honorName'] = self.honor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        self.grant_history = []
        if m.get('grantHistory') is not None:
            for k in m.get('grantHistory'):
                temp_model = QueryUserHonorsResponseBodyResultHonorsGrantHistory()
                self.grant_history.append(temp_model.from_map(k))
        if m.get('honorDesc') is not None:
            self.honor_desc = m.get('honorDesc')
        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')
        if m.get('honorName') is not None:
            self.honor_name = m.get('honorName')
        return self


class QueryUserHonorsResponseBodyResult(TeaModel):
    def __init__(
        self,
        honors: List[QueryUserHonorsResponseBodyResultHonors] = None,
        next_token: str = None,
    ):
        self.honors = honors
        self.next_token = next_token

    def validate(self):
        if self.honors:
            for k in self.honors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['honors'] = []
        if self.honors is not None:
            for k in self.honors:
                result['honors'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.honors = []
        if m.get('honors') is not None:
            for k in m.get('honors'):
                temp_model = QueryUserHonorsResponseBodyResultHonors()
                self.honors.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class QueryUserHonorsResponseBody(TeaModel):
    def __init__(
        self,
        result: QueryUserHonorsResponseBodyResult = None,
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
            temp_model = QueryUserHonorsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryUserHonorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUserHonorsResponseBody = None,
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
            temp_model = QueryUserHonorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


