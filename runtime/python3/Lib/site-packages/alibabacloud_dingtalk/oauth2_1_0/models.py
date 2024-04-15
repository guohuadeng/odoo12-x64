# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateJsapiTicketHeaders(TeaModel):
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


class CreateJsapiTicketResponseBody(TeaModel):
    def __init__(
        self,
        expire_in: int = None,
        jsapi_ticket: str = None,
    ):
        # 超时时间
        self.expire_in = expire_in
        # jsapi ticket
        self.jsapi_ticket = jsapi_ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        if self.jsapi_ticket is not None:
            result['jsapiTicket'] = self.jsapi_ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        if m.get('jsapiTicket') is not None:
            self.jsapi_ticket = m.get('jsapiTicket')
        return self


class CreateJsapiTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJsapiTicketResponseBody = None,
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
            temp_model = CreateJsapiTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessTokenRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
    ):
        # 应用id
        self.app_key = app_key
        # 应用密码
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['appKey'] = self.app_key
        if self.app_secret is not None:
            result['appSecret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')
        if m.get('appSecret') is not None:
            self.app_secret = m.get('appSecret')
        return self


class GetAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expire_in: int = None,
    ):
        # accessToken
        self.access_token = access_token
        # 超时时间
        self.expire_in = expire_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        return self


class GetAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessTokenResponseBody = None,
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
            temp_model = GetAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthInfoHeaders(TeaModel):
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


class GetAuthInfoRequest(TeaModel):
    def __init__(
        self,
        auth_corp_id: str = None,
    ):
        self.auth_corp_id = auth_corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_corp_id is not None:
            result['authCorpId'] = self.auth_corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCorpId') is not None:
            self.auth_corp_id = m.get('authCorpId')
        return self


class GetAuthInfoResponseBodyAuthAppInfoAgentList(TeaModel):
    def __init__(
        self,
        admin_list: List[str] = None,
        agent_id: int = None,
        agent_name: str = None,
        app_id: int = None,
    ):
        # 对此微应用有管理权限的管理员列表
        self.admin_list = admin_list
        # 应用id
        self.agent_id = agent_id
        # 应用名称
        self.agent_name = agent_name
        # 三方应用id
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_list is not None:
            result['adminList'] = self.admin_list
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.agent_name is not None:
            result['agentName'] = self.agent_name
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adminList') is not None:
            self.admin_list = m.get('adminList')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self


class GetAuthInfoResponseBodyAuthAppInfo(TeaModel):
    def __init__(
        self,
        agent_list: List[GetAuthInfoResponseBodyAuthAppInfoAgentList] = None,
    ):
        self.agent_list = agent_list

    def validate(self):
        if self.agent_list:
            for k in self.agent_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['agentList'] = []
        if self.agent_list is not None:
            for k in self.agent_list:
                result['agentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_list = []
        if m.get('agentList') is not None:
            for k in m.get('agentList'):
                temp_model = GetAuthInfoResponseBodyAuthAppInfoAgentList()
                self.agent_list.append(temp_model.from_map(k))
        return self


class GetAuthInfoResponseBodyAuthCorpInfo(TeaModel):
    def __init__(
        self,
        auth_channel: str = None,
        auth_channel_type: str = None,
        auth_level: int = None,
        corp_logo_url: str = None,
        corp_name: str = None,
        industry: str = None,
        invite_code: str = None,
        invite_url: str = None,
        license_code: str = None,
    ):
        # 渠道码。
        self.auth_channel = auth_channel
        # 渠道类型。  为了避免渠道码重复，可与渠道码共同确认渠道。可能为空，非空时当前只有满天星类型，值为STAR_ACTIVITY。
        self.auth_channel_type = auth_channel_type
        # 企业认证等级：  0：未认证  1：高级认证  2：中级认证  3：初级认证
        self.auth_level = auth_level
        # 企业logo。
        self.corp_logo_url = corp_logo_url
        # 授权方企业名称。
        self.corp_name = corp_name
        # 企业所属行业。
        self.industry = industry
        # 邀请码，只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。
        self.invite_code = invite_code
        # 企业邀请链接。
        self.invite_url = invite_url
        # 序列号。
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_channel is not None:
            result['authChannel'] = self.auth_channel
        if self.auth_channel_type is not None:
            result['authChannelType'] = self.auth_channel_type
        if self.auth_level is not None:
            result['authLevel'] = self.auth_level
        if self.corp_logo_url is not None:
            result['corpLogoUrl'] = self.corp_logo_url
        if self.corp_name is not None:
            result['corpName'] = self.corp_name
        if self.industry is not None:
            result['industry'] = self.industry
        if self.invite_code is not None:
            result['inviteCode'] = self.invite_code
        if self.invite_url is not None:
            result['inviteUrl'] = self.invite_url
        if self.license_code is not None:
            result['licenseCode'] = self.license_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authChannel') is not None:
            self.auth_channel = m.get('authChannel')
        if m.get('authChannelType') is not None:
            self.auth_channel_type = m.get('authChannelType')
        if m.get('authLevel') is not None:
            self.auth_level = m.get('authLevel')
        if m.get('corpLogoUrl') is not None:
            self.corp_logo_url = m.get('corpLogoUrl')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('inviteCode') is not None:
            self.invite_code = m.get('inviteCode')
        if m.get('inviteUrl') is not None:
            self.invite_url = m.get('inviteUrl')
        if m.get('licenseCode') is not None:
            self.license_code = m.get('licenseCode')
        return self


class GetAuthInfoResponseBodyAuthUserInfo(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 授权管理员id
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


class GetAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        auth_app_info: GetAuthInfoResponseBodyAuthAppInfo = None,
        auth_corp_info: GetAuthInfoResponseBodyAuthCorpInfo = None,
        auth_user_info: GetAuthInfoResponseBodyAuthUserInfo = None,
    ):
        # 授权应用信息
        self.auth_app_info = auth_app_info
        # 应用企业信息
        self.auth_corp_info = auth_corp_info
        # 授权用户信息
        self.auth_user_info = auth_user_info

    def validate(self):
        if self.auth_app_info:
            self.auth_app_info.validate()
        if self.auth_corp_info:
            self.auth_corp_info.validate()
        if self.auth_user_info:
            self.auth_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_app_info is not None:
            result['authAppInfo'] = self.auth_app_info.to_map()
        if self.auth_corp_info is not None:
            result['authCorpInfo'] = self.auth_corp_info.to_map()
        if self.auth_user_info is not None:
            result['authUserInfo'] = self.auth_user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authAppInfo') is not None:
            temp_model = GetAuthInfoResponseBodyAuthAppInfo()
            self.auth_app_info = temp_model.from_map(m['authAppInfo'])
        if m.get('authCorpInfo') is not None:
            temp_model = GetAuthInfoResponseBodyAuthCorpInfo()
            self.auth_corp_info = temp_model.from_map(m['authCorpInfo'])
        if m.get('authUserInfo') is not None:
            temp_model = GetAuthInfoResponseBodyAuthUserInfo()
            self.auth_user_info = temp_model.from_map(m['authUserInfo'])
        return self


class GetAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthInfoResponseBody = None,
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
            temp_model = GetAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCorpAccessTokenRequest(TeaModel):
    def __init__(
        self,
        auth_corp_id: str = None,
        suite_key: str = None,
        suite_secret: str = None,
        suite_ticket: str = None,
    ):
        # OAuth 2.0 临时授权码
        self.auth_corp_id = auth_corp_id
        # 应用id
        self.suite_key = suite_key
        # 应用密码
        self.suite_secret = suite_secret
        # suiteTicket
        self.suite_ticket = suite_ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_corp_id is not None:
            result['authCorpId'] = self.auth_corp_id
        if self.suite_key is not None:
            result['suiteKey'] = self.suite_key
        if self.suite_secret is not None:
            result['suiteSecret'] = self.suite_secret
        if self.suite_ticket is not None:
            result['suiteTicket'] = self.suite_ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCorpId') is not None:
            self.auth_corp_id = m.get('authCorpId')
        if m.get('suiteKey') is not None:
            self.suite_key = m.get('suiteKey')
        if m.get('suiteSecret') is not None:
            self.suite_secret = m.get('suiteSecret')
        if m.get('suiteTicket') is not None:
            self.suite_ticket = m.get('suiteTicket')
        return self


class GetCorpAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expire_in: int = None,
    ):
        # accessToken
        self.access_token = access_token
        # 超时时间
        self.expire_in = expire_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        return self


class GetCorpAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCorpAccessTokenResponseBody = None,
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
            temp_model = GetCorpAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPersonalAuthRuleHeaders(TeaModel):
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


class GetPersonalAuthRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_items: List[str] = None,
        resource: str = None,
    ):
        # authItems
        self.auth_items = auth_items
        # resource
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_items is not None:
            result['authItems'] = self.auth_items
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authItems') is not None:
            self.auth_items = m.get('authItems')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetPersonalAuthRuleResponseBody(TeaModel):
    def __init__(
        self,
        result: List[GetPersonalAuthRuleResponseBodyResult] = None,
    ):
        # list
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
                temp_model = GetPersonalAuthRuleResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetPersonalAuthRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPersonalAuthRuleResponseBody = None,
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
            temp_model = GetPersonalAuthRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSsoAccessTokenRequest(TeaModel):
    def __init__(
        self,
        corpid: str = None,
        sso_secret: str = None,
    ):
        # 企业id
        self.corpid = corpid
        # sso密码
        self.sso_secret = sso_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpid is not None:
            result['corpid'] = self.corpid
        if self.sso_secret is not None:
            result['ssoSecret'] = self.sso_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpid') is not None:
            self.corpid = m.get('corpid')
        if m.get('ssoSecret') is not None:
            self.sso_secret = m.get('ssoSecret')
        return self


class GetSsoAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expire_in: int = None,
    ):
        # accessToken
        self.access_token = access_token
        # 超时时间
        self.expire_in = expire_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        return self


class GetSsoAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSsoAccessTokenResponseBody = None,
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
            temp_model = GetSsoAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSsoUserInfoHeaders(TeaModel):
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


class GetSsoUserInfoRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetSsoUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        corp_id: str = None,
        corp_name: str = None,
        email: str = None,
        is_admin: bool = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # 用户头像链接
        self.avatar = avatar
        # 微应用免登用户所在企业id
        self.corp_id = corp_id
        # 微应用免登用户所在企业名称
        self.corp_name = corp_name
        # 用户邮箱
        self.email = email
        # 是否为企业管理员
        self.is_admin = is_admin
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
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.corp_name is not None:
            result['corpName'] = self.corp_name
        if self.email is not None:
            result['email'] = self.email
        if self.is_admin is not None:
            result['isAdmin'] = self.is_admin
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('isAdmin') is not None:
            self.is_admin = m.get('isAdmin')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetSsoUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSsoUserInfoResponseBody = None,
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
            temp_model = GetSsoUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuiteAccessTokenRequest(TeaModel):
    def __init__(
        self,
        suite_key: str = None,
        suite_secret: str = None,
        suite_ticket: str = None,
    ):
        # 应用id
        self.suite_key = suite_key
        # 应用密码
        self.suite_secret = suite_secret
        # suiteTicket
        self.suite_ticket = suite_ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suite_key is not None:
            result['suiteKey'] = self.suite_key
        if self.suite_secret is not None:
            result['suiteSecret'] = self.suite_secret
        if self.suite_ticket is not None:
            result['suiteTicket'] = self.suite_ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('suiteKey') is not None:
            self.suite_key = m.get('suiteKey')
        if m.get('suiteSecret') is not None:
            self.suite_secret = m.get('suiteSecret')
        if m.get('suiteTicket') is not None:
            self.suite_ticket = m.get('suiteTicket')
        return self


class GetSuiteAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expire_in: int = None,
    ):
        # accessToken
        self.access_token = access_token
        # 超时时间
        self.expire_in = expire_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        return self


class GetSuiteAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSuiteAccessTokenResponseBody = None,
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
            temp_model = GetSuiteAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        grant_type: str = None,
        refresh_token: str = None,
    ):
        # 应用id
        self.client_id = client_id
        # 应用密码
        self.client_secret = client_secret
        # OAuth 2.0 临时授权码
        self.code = code
        # 分为authorization_code和refresh_token。使用授权码换token，传authorization_code；使用刷新token换用户token，传refresh_token
        self.grant_type = grant_type
        # OAuth 2.0 刷新令牌
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.code is not None:
            result['code'] = self.code
        if self.grant_type is not None:
            result['grantType'] = self.grant_type
        if self.refresh_token is not None:
            result['refreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('grantType') is not None:
            self.grant_type = m.get('grantType')
        if m.get('refreshToken') is not None:
            self.refresh_token = m.get('refreshToken')
        return self


class GetUserTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        corp_id: str = None,
        expire_in: int = None,
        refresh_token: str = None,
    ):
        # accessToken
        self.access_token = access_token
        # 所选企业corpId
        self.corp_id = corp_id
        # 超时时间
        self.expire_in = expire_in
        # refreshToken
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.expire_in is not None:
            result['expireIn'] = self.expire_in
        if self.refresh_token is not None:
            result['refreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('expireIn') is not None:
            self.expire_in = m.get('expireIn')
        if m.get('refreshToken') is not None:
            self.refresh_token = m.get('refreshToken')
        return self


class GetUserTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserTokenResponseBody = None,
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
            temp_model = GetUserTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


