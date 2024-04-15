# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddAttendeeHeaders(TeaModel):
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


class AddAttendeeRequestAttendeesToAdd(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
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


class AddAttendeeRequest(TeaModel):
    def __init__(
        self,
        attendees_to_add: List[AddAttendeeRequestAttendeesToAdd] = None,
    ):
        self.attendees_to_add = attendees_to_add

    def validate(self):
        if self.attendees_to_add:
            for k in self.attendees_to_add:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendeesToAdd'] = []
        if self.attendees_to_add is not None:
            for k in self.attendees_to_add:
                result['attendeesToAdd'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees_to_add = []
        if m.get('attendeesToAdd') is not None:
            for k in m.get('attendeesToAdd'):
                temp_model = AddAttendeeRequestAttendeesToAdd()
                self.attendees_to_add.append(temp_model.from_map(k))
        return self


class AddAttendeeResponse(TeaModel):
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


class CheckInHeaders(TeaModel):
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


class CheckInResponseBody(TeaModel):
    def __init__(
        self,
        check_in_time: int = None,
    ):
        # 签到时间戳
        self.check_in_time = check_in_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['checkInTime'] = self.check_in_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkInTime') is not None:
            self.check_in_time = m.get('checkInTime')
        return self


class CheckInResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckInResponseBody = None,
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
            temp_model = CheckInResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertLegacyEventIdHeaders(TeaModel):
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


class ConvertLegacyEventIdRequest(TeaModel):
    def __init__(
        self,
        legacy_event_ids: List[str] = None,
    ):
        self.legacy_event_ids = legacy_event_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.legacy_event_ids is not None:
            result['legacyEventIds'] = self.legacy_event_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('legacyEventIds') is not None:
            self.legacy_event_ids = m.get('legacyEventIds')
        return self


class ConvertLegacyEventIdResponseBody(TeaModel):
    def __init__(
        self,
        legacy_event_id_map: Dict[str, Any] = None,
    ):
        # legacyEventIdMap
        self.legacy_event_id_map = legacy_event_id_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.legacy_event_id_map is not None:
            result['legacyEventIdMap'] = self.legacy_event_id_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('legacyEventIdMap') is not None:
            self.legacy_event_id_map = m.get('legacyEventIdMap')
        return self


class ConvertLegacyEventIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertLegacyEventIdResponseBody = None,
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
            temp_model = ConvertLegacyEventIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclsHeaders(TeaModel):
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


class CreateAclsRequestScope(TeaModel):
    def __init__(
        self,
        scope_type: str = None,
        user_id: str = None,
    ):
        # 权限类型
        self.scope_type = scope_type
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateAclsRequest(TeaModel):
    def __init__(
        self,
        privilege: str = None,
        scope: CreateAclsRequestScope = None,
        send_msg: bool = None,
    ):
        # 对日历的访问权限
        self.privilege = privilege
        # 权限范围
        self.scope = scope
        # 是否向授权人发消息
        self.send_msg = send_msg

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privilege is not None:
            result['privilege'] = self.privilege
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        if self.send_msg is not None:
            result['sendMsg'] = self.send_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privilege') is not None:
            self.privilege = m.get('privilege')
        if m.get('scope') is not None:
            temp_model = CreateAclsRequestScope()
            self.scope = temp_model.from_map(m['scope'])
        if m.get('sendMsg') is not None:
            self.send_msg = m.get('sendMsg')
        return self


class CreateAclsResponseBodyScope(TeaModel):
    def __init__(
        self,
        scope_type: str = None,
        user_id: str = None,
    ):
        # 权限类型
        self.scope_type = scope_type
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateAclsResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        privilege: str = None,
        scope: CreateAclsResponseBodyScope = None,
    ):
        # acl资源ID
        self.acl_id = acl_id
        # 对日历的访问权限
        self.privilege = privilege
        # 权限范围
        self.scope = scope

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['aclId'] = self.acl_id
        if self.privilege is not None:
            result['privilege'] = self.privilege
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclId') is not None:
            self.acl_id = m.get('aclId')
        if m.get('privilege') is not None:
            self.privilege = m.get('privilege')
        if m.get('scope') is not None:
            temp_model = CreateAclsResponseBodyScope()
            self.scope = temp_model.from_map(m['scope'])
        return self


class CreateAclsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAclsResponseBody = None,
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
            temp_model = CreateAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventHeaders(TeaModel):
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


class CreateEventRequestAttendees(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
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


class CreateEventRequestEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日程结束日期，如果是全天日程必须有值，非全天日程必须留空，格式：yyyy-MM-dd
        self.date = date
        # 日程结束时间，非全天日程必须有值，全天日程必须留空，格式为ISO-8601的date-time格式
        self.date_time = date_time
        # 日程结束时间所属时区，非全天日程必须有值，全天日程必须留空，tz database name格式，参考：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class CreateEventRequestLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class CreateEventRequestOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEventRequestRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        # 循环规则类型：  daily：每interval天 weekly：每interval周的第daysOfWeek天 absoluteMonthly：每interval月的第dayOfMonth天 relativeMonthly：每interval月的第index周的第daysOfWeek天 absoluteYearly：每interval年
        # 
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEventRequestRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEventRequestRecurrence(TeaModel):
    def __init__(
        self,
        pattern: CreateEventRequestRecurrencePattern = None,
        range: CreateEventRequestRecurrenceRange = None,
    ):
        # 循环规则
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = CreateEventRequestRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = CreateEventRequestRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class CreateEventRequestReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: int = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class CreateEventRequestStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日程开始日期，如果是全天日程必须有值，非全天日程必须留空，格式：yyyy-MM-dd
        self.date = date
        # 日程开始时间，非全天日程必须有值，全天日程必须留空，格式为ISO-8601的date-time格式
        self.date_time = date_time
        # 日程开始时间所属时区，非全天日程必须有值，全天日程必须留空，tz database name格式，参考：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class CreateEventRequest(TeaModel):
    def __init__(
        self,
        attendees: List[CreateEventRequestAttendees] = None,
        description: str = None,
        end: CreateEventRequestEnd = None,
        extra: Dict[str, str] = None,
        is_all_day: bool = None,
        location: CreateEventRequestLocation = None,
        online_meeting_info: CreateEventRequestOnlineMeetingInfo = None,
        recurrence: CreateEventRequestRecurrence = None,
        reminders: List[CreateEventRequestReminders] = None,
        start: CreateEventRequestStart = None,
        summary: str = None,
    ):
        self.attendees = attendees
        # 日程描述
        self.description = description
        # 日程结束时间
        self.end = end
        # 扩展信息
        self.extra = extra
        # 是否为全天日程
        self.is_all_day = is_all_day
        self.location = location
        self.online_meeting_info = online_meeting_info
        # 日程循环规则
        self.recurrence = recurrence
        self.reminders = reminders
        # 日程开始时间
        self.start = start
        # 日程标题
        self.summary = summary

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = CreateEventRequestAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = CreateEventRequestEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = CreateEventRequestLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = CreateEventRequestOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('recurrence') is not None:
            temp_model = CreateEventRequestRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = CreateEventRequestReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = CreateEventRequestStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        return self


class CreateEventResponseBodyAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class CreateEventResponseBodyEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class CreateEventResponseBodyLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class CreateEventResponseBodyOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        url: str = None,
    ):
        self.conference_id = conference_id
        self.extra_info = extra_info
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateEventResponseBodyOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class CreateEventResponseBodyRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEventResponseBodyRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEventResponseBodyRecurrence(TeaModel):
    def __init__(
        self,
        pattern: CreateEventResponseBodyRecurrencePattern = None,
        range: CreateEventResponseBodyRecurrenceRange = None,
    ):
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = CreateEventResponseBodyRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = CreateEventResponseBodyRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class CreateEventResponseBodyReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class CreateEventResponseBodyStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class CreateEventResponseBody(TeaModel):
    def __init__(
        self,
        attendees: List[CreateEventResponseBodyAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: CreateEventResponseBodyEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: CreateEventResponseBodyLocation = None,
        online_meeting_info: CreateEventResponseBodyOnlineMeetingInfo = None,
        organizer: CreateEventResponseBodyOrganizer = None,
        recurrence: CreateEventResponseBodyRecurrence = None,
        reminders: List[CreateEventResponseBodyReminders] = None,
        start: CreateEventResponseBodyStart = None,
        summary: str = None,
        update_time: str = None,
    ):
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        self.description = description
        self.end = end
        self.id = id
        self.is_all_day = is_all_day
        self.location = location
        self.online_meeting_info = online_meeting_info
        self.organizer = organizer
        self.recurrence = recurrence
        self.reminders = reminders
        # 日程开始时间
        self.start = start
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = CreateEventResponseBodyAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = CreateEventResponseBodyEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = CreateEventResponseBodyLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = CreateEventResponseBodyOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('organizer') is not None:
            temp_model = CreateEventResponseBodyOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = CreateEventResponseBodyRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = CreateEventResponseBodyReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = CreateEventResponseBodyStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class CreateEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEventResponseBody = None,
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
            temp_model = CreateEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclHeaders(TeaModel):
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


class DeleteAclResponse(TeaModel):
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


class DeleteEventHeaders(TeaModel):
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


class DeleteEventResponse(TeaModel):
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


class GenerateCaldavAccountHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        ding_uid: str = None,
        x_acs_dingtalk_access_token: str = None,
    ):
        self.common_headers = common_headers
        # 授权本次调用的用户id，该字段有值时认为本次调用已被授权访问该用户可以访问的所有数据
        self.ding_uid = ding_uid
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
        if self.ding_uid is not None:
            result['dingUid'] = self.ding_uid
        if self.x_acs_dingtalk_access_token is not None:
            result['x-acs-dingtalk-access-token'] = self.x_acs_dingtalk_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('dingUid') is not None:
            self.ding_uid = m.get('dingUid')
        if m.get('x-acs-dingtalk-access-token') is not None:
            self.x_acs_dingtalk_access_token = m.get('x-acs-dingtalk-access-token')
        return self


class GenerateCaldavAccountRequest(TeaModel):
    def __init__(
        self,
        device: str = None,
    ):
        # 设备名称
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['device'] = self.device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('device') is not None:
            self.device = m.get('device')
        return self


class GenerateCaldavAccountResponseBody(TeaModel):
    def __init__(
        self,
        password: str = None,
        server_address: str = None,
        username: str = None,
    ):
        self.password = password
        self.server_address = server_address
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.server_address is not None:
            result['serverAddress'] = self.server_address
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('serverAddress') is not None:
            self.server_address = m.get('serverAddress')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GenerateCaldavAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateCaldavAccountResponseBody = None,
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
            temp_model = GenerateCaldavAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventHeaders(TeaModel):
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


class GetEventRequest(TeaModel):
    def __init__(
        self,
        max_attendees: int = None,
    ):
        # 返回参与人，上限500人，默认为0
        self.max_attendees = max_attendees

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_attendees is not None:
            result['maxAttendees'] = self.max_attendees
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAttendees') is not None:
            self.max_attendees = m.get('maxAttendees')
        return self


class GetEventResponseBodyAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class GetEventResponseBodyEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class GetEventResponseBodyLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class GetEventResponseBodyOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        url: str = None,
    ):
        self.conference_id = conference_id
        self.extra_info = extra_info
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetEventResponseBodyOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class GetEventResponseBodyRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        # 循环模式类型(type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetEventResponseBodyRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        # 范围类型(endDate, noEnd, numbered)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetEventResponseBodyRecurrence(TeaModel):
    def __init__(
        self,
        pattern: GetEventResponseBodyRecurrencePattern = None,
        range: GetEventResponseBodyRecurrenceRange = None,
    ):
        # 重复模式
        self.pattern = pattern
        # 重复范围
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = GetEventResponseBodyRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = GetEventResponseBodyRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class GetEventResponseBodyReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class GetEventResponseBodyStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日期，格式：yyyyMMdd
        self.date = date
        # 时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class GetEventResponseBody(TeaModel):
    def __init__(
        self,
        attendees: List[GetEventResponseBodyAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: GetEventResponseBodyEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: GetEventResponseBodyLocation = None,
        online_meeting_info: GetEventResponseBodyOnlineMeetingInfo = None,
        organizer: GetEventResponseBodyOrganizer = None,
        recurrence: GetEventResponseBodyRecurrence = None,
        reminders: List[GetEventResponseBodyReminders] = None,
        series_master_id: str = None,
        start: GetEventResponseBodyStart = None,
        status: str = None,
        summary: str = None,
        update_time: str = None,
    ):
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        # 日程描述
        self.description = description
        # 日程结束时间
        self.end = end
        self.id = id
        # 是否为全天日程
        self.is_all_day = is_all_day
        self.location = location
        self.online_meeting_info = online_meeting_info
        self.organizer = organizer
        self.recurrence = recurrence
        self.reminders = reminders
        # 重复日程的主日程id，非重复日程为空
        self.series_master_id = series_master_id
        # 日程开始时间
        self.start = start
        # 日程状态
        self.status = status
        # 日程标题
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.series_master_id is not None:
            result['seriesMasterId'] = self.series_master_id
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = GetEventResponseBodyAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = GetEventResponseBodyEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = GetEventResponseBodyLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = GetEventResponseBodyOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('organizer') is not None:
            temp_model = GetEventResponseBodyOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = GetEventResponseBodyRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = GetEventResponseBodyReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('seriesMasterId') is not None:
            self.series_master_id = m.get('seriesMasterId')
        if m.get('start') is not None:
            temp_model = GetEventResponseBodyStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEventResponseBody = None,
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
            temp_model = GetEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduleHeaders(TeaModel):
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


class GetScheduleRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        user_ids: List[str] = None,
    ):
        # 查询结束时间
        self.end_time = end_time
        # 查询开始时间
        self.start_time = start_time
        # 待查询的用户列表
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self


class GetScheduleResponseBodyScheduleInformationScheduleItemsEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 结束日期
        self.date = date
        # 结束时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时间戳所属时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class GetScheduleResponseBodyScheduleInformationScheduleItemsStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 开始日期
        self.date = date
        # 开始时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 所属时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class GetScheduleResponseBodyScheduleInformationScheduleItems(TeaModel):
    def __init__(
        self,
        end: GetScheduleResponseBodyScheduleInformationScheduleItemsEnd = None,
        start: GetScheduleResponseBodyScheduleInformationScheduleItemsStart = None,
        status: str = None,
    ):
        # 结束时间，表示一个日期，或者一个带时区的时间戳
        self.end = end
        # 开始时间，表示一个日期，或者一个带时区的时间戳
        self.start = start
        # 状态: - BUSY：繁忙, - TENTATIVE：暂定繁忙
        self.status = status

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
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            temp_model = GetScheduleResponseBodyScheduleInformationScheduleItemsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('start') is not None:
            temp_model = GetScheduleResponseBodyScheduleInformationScheduleItemsStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetScheduleResponseBodyScheduleInformation(TeaModel):
    def __init__(
        self,
        error: str = None,
        schedule_items: List[GetScheduleResponseBodyScheduleInformationScheduleItems] = None,
        user_id: str = None,
    ):
        # 异常描述
        self.error = error
        self.schedule_items = schedule_items
        # 用户userId
        self.user_id = user_id

    def validate(self):
        if self.schedule_items:
            for k in self.schedule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['error'] = self.error
        result['scheduleItems'] = []
        if self.schedule_items is not None:
            for k in self.schedule_items:
                result['scheduleItems'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            self.error = m.get('error')
        self.schedule_items = []
        if m.get('scheduleItems') is not None:
            for k in m.get('scheduleItems'):
                temp_model = GetScheduleResponseBodyScheduleInformationScheduleItems()
                self.schedule_items.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetScheduleResponseBody(TeaModel):
    def __init__(
        self,
        schedule_information: List[GetScheduleResponseBodyScheduleInformation] = None,
    ):
        # 闲忙信息
        self.schedule_information = schedule_information

    def validate(self):
        if self.schedule_information:
            for k in self.schedule_information:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['scheduleInformation'] = []
        if self.schedule_information is not None:
            for k in self.schedule_information:
                result['scheduleInformation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schedule_information = []
        if m.get('scheduleInformation') is not None:
            for k in m.get('scheduleInformation'):
                temp_model = GetScheduleResponseBodyScheduleInformation()
                self.schedule_information.append(temp_model.from_map(k))
        return self


class GetScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScheduleResponseBody = None,
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
            temp_model = GetScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignInListHeaders(TeaModel):
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


class GetSignInListRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # 查询返回结果数（上限200）
        self.max_results = max_results
        self.next_token = next_token
        # 签到信息类型（check_in，not_yet_check_in)
        self.type = type

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
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSignInListResponseBodyUsers(TeaModel):
    def __init__(
        self,
        check_in_time: int = None,
        display_name: str = None,
        user_id: str = None,
    ):
        # 签到时间
        self.check_in_time = check_in_time
        # 用户名
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['checkInTime'] = self.check_in_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkInTime') is not None:
            self.check_in_time = m.get('checkInTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetSignInListResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        users: List[GetSignInListResponseBodyUsers] = None,
    ):
        # 翻页token
        self.next_token = next_token
        # 签到信息
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetSignInListResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetSignInListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignInListResponseBody = None,
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
            temp_model = GetSignInListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignOutListHeaders(TeaModel):
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


class GetSignOutListRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # 查询返回结果数（上限200）
        self.max_results = max_results
        self.next_token = next_token
        # 签到信息类型（sign_out，not_yet_sign_out)
        self.type = type

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
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSignOutListResponseBodyUsers(TeaModel):
    def __init__(
        self,
        check_out_time: int = None,
        display_name: str = None,
        user_id: str = None,
    ):
        # 签退时间
        self.check_out_time = check_out_time
        # 用户名
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_out_time is not None:
            result['checkOutTime'] = self.check_out_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkOutTime') is not None:
            self.check_out_time = m.get('checkOutTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetSignOutListResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        users: List[GetSignOutListResponseBodyUsers] = None,
    ):
        # 翻页token
        self.next_token = next_token
        # 签退信息
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetSignOutListResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetSignOutListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignOutListResponseBody = None,
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
            temp_model = GetSignOutListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclsHeaders(TeaModel):
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


class ListAclsResponseBodyAclsScope(TeaModel):
    def __init__(
        self,
        scope_type: str = None,
        user_id: str = None,
    ):
        # 权限类型
        self.scope_type = scope_type
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_type is not None:
            result['scopeType'] = self.scope_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListAclsResponseBodyAcls(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        privilege: str = None,
        scope: ListAclsResponseBodyAclsScope = None,
    ):
        # acl资源ID
        self.acl_id = acl_id
        # 权限信息
        self.privilege = privilege
        # 权限范围
        self.scope = scope

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['aclId'] = self.acl_id
        if self.privilege is not None:
            result['privilege'] = self.privilege
        if self.scope is not None:
            result['scope'] = self.scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclId') is not None:
            self.acl_id = m.get('aclId')
        if m.get('privilege') is not None:
            self.privilege = m.get('privilege')
        if m.get('scope') is not None:
            temp_model = ListAclsResponseBodyAclsScope()
            self.scope = temp_model.from_map(m['scope'])
        return self


class ListAclsResponseBody(TeaModel):
    def __init__(
        self,
        acls: List[ListAclsResponseBodyAcls] = None,
    ):
        # 访问控制列表
        self.acls = acls

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['acls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('acls') is not None:
            for k in m.get('acls'):
                temp_model = ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        return self


class ListAclsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAclsResponseBody = None,
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
            temp_model = ListAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAttendeesHeaders(TeaModel):
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


class ListAttendeesRequest(TeaModel):
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


class ListAttendeesResponseBodyAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否当前用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListAttendeesResponseBody(TeaModel):
    def __init__(
        self,
        attendees: List[ListAttendeesResponseBodyAttendees] = None,
        next_token: str = None,
    ):
        # 参与人
        self.attendees = attendees
        # 翻页token
        self.next_token = next_token

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = ListAttendeesResponseBodyAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAttendeesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAttendeesResponseBody = None,
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
            temp_model = ListAttendeesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCalendarsHeaders(TeaModel):
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


class ListCalendarsResponseBodyResponseCalendars(TeaModel):
    def __init__(
        self,
        description: str = None,
        e_tag: str = None,
        id: str = None,
        privilege: str = None,
        summary: str = None,
        time_zone: str = None,
        type: str = None,
    ):
        # 日历描述
        self.description = description
        # Calendar资源的ETag，用于检测该Calendar以及内部的Event是否有被更新
        self.e_tag = e_tag
        # 日历id
        self.id = id
        # 权限信息
        self.privilege = privilege
        # 日历标题
        self.summary = summary
        # 时区
        self.time_zone = time_zone
        # 日历类型
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
        if self.e_tag is not None:
            result['eTag'] = self.e_tag
        if self.id is not None:
            result['id'] = self.id
        if self.privilege is not None:
            result['privilege'] = self.privilege
        if self.summary is not None:
            result['summary'] = self.summary
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('eTag') is not None:
            self.e_tag = m.get('eTag')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('privilege') is not None:
            self.privilege = m.get('privilege')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListCalendarsResponseBodyResponse(TeaModel):
    def __init__(
        self,
        calendars: List[ListCalendarsResponseBodyResponseCalendars] = None,
    ):
        self.calendars = calendars

    def validate(self):
        if self.calendars:
            for k in self.calendars:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['calendars'] = []
        if self.calendars is not None:
            for k in self.calendars:
                result['calendars'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calendars = []
        if m.get('calendars') is not None:
            for k in m.get('calendars'):
                temp_model = ListCalendarsResponseBodyResponseCalendars()
                self.calendars.append(temp_model.from_map(k))
        return self


class ListCalendarsResponseBody(TeaModel):
    def __init__(
        self,
        response: ListCalendarsResponseBodyResponse = None,
    ):
        # 日历信息
        self.response = response

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response is not None:
            result['response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('response') is not None:
            temp_model = ListCalendarsResponseBodyResponse()
            self.response = temp_model.from_map(m['response'])
        return self


class ListCalendarsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCalendarsResponseBody = None,
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
            temp_model = ListCalendarsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventsHeaders(TeaModel):
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


class ListEventsRequest(TeaModel):
    def __init__(
        self,
        max_attendees: int = None,
        max_results: int = None,
        next_token: str = None,
        show_deleted: bool = None,
        sync_token: str = None,
        time_max: str = None,
        time_min: str = None,
    ):
        # 每个日程的参与者查询个数，默认100，最大100
        self.max_attendees = max_attendees
        # 返回的最大日程数，最大100个，默认100个
        self.max_results = max_results
        # 查询翻页token
        self.next_token = next_token
        # 是否返回删除事件
        self.show_deleted = show_deleted
        # 增量查询token
        self.sync_token = sync_token
        # 查询截止时间
        self.time_max = time_max
        # 查询开始时间
        self.time_min = time_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_attendees is not None:
            result['maxAttendees'] = self.max_attendees
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.show_deleted is not None:
            result['showDeleted'] = self.show_deleted
        if self.sync_token is not None:
            result['syncToken'] = self.sync_token
        if self.time_max is not None:
            result['timeMax'] = self.time_max
        if self.time_min is not None:
            result['timeMin'] = self.time_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAttendees') is not None:
            self.max_attendees = m.get('maxAttendees')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('showDeleted') is not None:
            self.show_deleted = m.get('showDeleted')
        if m.get('syncToken') is not None:
            self.sync_token = m.get('syncToken')
        if m.get('timeMax') is not None:
            self.time_max = m.get('timeMax')
        if m.get('timeMin') is not None:
            self.time_min = m.get('timeMin')
        return self


class ListEventsResponseBodyEventsAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsResponseBodyEventsEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsResponseBodyEventsLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        # 展示名称
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListEventsResponseBodyEventsOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        url: str = None,
    ):
        self.conference_id = conference_id
        self.extra_info = extra_info
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEventsResponseBodyEventsOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsResponseBodyEventsRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        # 循环模式类型(type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsResponseBodyEventsRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        # 范围类型(endDate, noEnd, numbered)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsResponseBodyEventsRecurrence(TeaModel):
    def __init__(
        self,
        pattern: ListEventsResponseBodyEventsRecurrencePattern = None,
        range: ListEventsResponseBodyEventsRecurrenceRange = None,
    ):
        # 重复模式
        self.pattern = pattern
        # 重复范围
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = ListEventsResponseBodyEventsRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = ListEventsResponseBodyEventsRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class ListEventsResponseBodyEventsReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class ListEventsResponseBodyEventsStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日期，格式：yyyyMMdd
        self.date = date
        # 时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        attendees: List[ListEventsResponseBodyEventsAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: ListEventsResponseBodyEventsEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: ListEventsResponseBodyEventsLocation = None,
        online_meeting_info: ListEventsResponseBodyEventsOnlineMeetingInfo = None,
        organizer: ListEventsResponseBodyEventsOrganizer = None,
        recurrence: ListEventsResponseBodyEventsRecurrence = None,
        reminders: List[ListEventsResponseBodyEventsReminders] = None,
        series_master_id: str = None,
        start: ListEventsResponseBodyEventsStart = None,
        status: str = None,
        summary: str = None,
        update_time: str = None,
    ):
        # 日程参与人
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        # 日程描述
        self.description = description
        # 日程结束时间
        self.end = end
        # 日程事件id
        self.id = id
        # 是否为全天日程
        self.is_all_day = is_all_day
        # 日程地点
        self.location = location
        self.online_meeting_info = online_meeting_info
        # 日程组织人
        self.organizer = organizer
        # 日程重复规则
        self.recurrence = recurrence
        self.reminders = reminders
        # 重复日程的主日程id，非重复日程为空
        self.series_master_id = series_master_id
        # 日程开始时间
        self.start = start
        # 日程状态
        self.status = status
        # 日程标题
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.series_master_id is not None:
            result['seriesMasterId'] = self.series_master_id
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = ListEventsResponseBodyEventsAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = ListEventsResponseBodyEventsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = ListEventsResponseBodyEventsLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = ListEventsResponseBodyEventsOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('organizer') is not None:
            temp_model = ListEventsResponseBodyEventsOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = ListEventsResponseBodyEventsRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = ListEventsResponseBodyEventsReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('seriesMasterId') is not None:
            self.series_master_id = m.get('seriesMasterId')
        if m.get('start') is not None:
            temp_model = ListEventsResponseBodyEventsStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[ListEventsResponseBodyEvents] = None,
        next_token: str = None,
        sync_token: str = None,
    ):
        # 日程
        self.events = events
        # 翻页token
        self.next_token = next_token
        # 增量同步token
        self.sync_token = sync_token

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.sync_token is not None:
            result['syncToken'] = self.sync_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = ListEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('syncToken') is not None:
            self.sync_token = m.get('syncToken')
        return self


class ListEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEventsResponseBody = None,
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
            temp_model = ListEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventsInstancesHeaders(TeaModel):
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


class ListEventsInstancesRequest(TeaModel):
    def __init__(
        self,
        max_attendees: int = None,
        max_results: int = None,
        series_master_id: str = None,
        start_recurrence_id: str = None,
    ):
        # listInstances每个日程的参与者查询个数，默认100，最大100。
        self.max_attendees = max_attendees
        # listInstances返回的最大日程数，最大100个，默认100个。
        self.max_results = max_results
        # 循环主日程id。
        self.series_master_id = series_master_id
        # 大于等于次序列id的所有实例
        self.start_recurrence_id = start_recurrence_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_attendees is not None:
            result['maxAttendees'] = self.max_attendees
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.series_master_id is not None:
            result['seriesMasterId'] = self.series_master_id
        if self.start_recurrence_id is not None:
            result['startRecurrenceId'] = self.start_recurrence_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAttendees') is not None:
            self.max_attendees = m.get('maxAttendees')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('seriesMasterId') is not None:
            self.series_master_id = m.get('seriesMasterId')
        if m.get('startRecurrenceId') is not None:
            self.start_recurrence_id = m.get('startRecurrenceId')
        return self


class ListEventsInstancesResponseBodyEventsAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsInstancesResponseBodyEventsEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日期，格式：yyyyMMdd
        self.date = date
        # 时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsInstancesResponseBodyEventsLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        # 展示名称
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListEventsInstancesResponseBodyEventsOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        type: str = None,
        url: str = None,
    ):
        # 会议ID
        self.conference_id = conference_id
        # 线上会议类型，目前支持：  dingtalk：钉钉视频会议
        self.type = type
        # 会议url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEventsInstancesResponseBodyEventsOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsInstancesResponseBodyEventsRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        # 每月的第几天
        self.day_of_month = day_of_month
        # 每周的第几天
        self.days_of_week = days_of_week
        # 指定事件发生在daysOfsWeek中指定的允许天数的哪个实例上，从该月的第一个实例开始计算。取值为:first, second, third, fourth, last。默认是first。如果类型是relativMonthly或relativeYear，则可选并使用
        self.index = index
        # 循环间隔
        self.interval = interval
        # 循环模式类型(type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsInstancesResponseBodyEventsRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        # 循环终止日期
        self.end_date = end_date
        # 循环出现次数
        self.number_of_occurrences = number_of_occurrences
        # 范围类型(endDate, noEnd, numbered)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsInstancesResponseBodyEventsRecurrence(TeaModel):
    def __init__(
        self,
        pattern: ListEventsInstancesResponseBodyEventsRecurrencePattern = None,
        range: ListEventsInstancesResponseBodyEventsRecurrenceRange = None,
    ):
        # 重复模式
        self.pattern = pattern
        # 重复范围
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class ListEventsInstancesResponseBodyEventsReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
    ):
        # 提醒方式
        self.method = method
        # 在日程开始前N分钟发出提醒
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class ListEventsInstancesResponseBodyEventsStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日期，格式：yyyyMMdd
        self.date = date
        # 时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsInstancesResponseBodyEvents(TeaModel):
    def __init__(
        self,
        attendees: List[ListEventsInstancesResponseBodyEventsAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: ListEventsInstancesResponseBodyEventsEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: ListEventsInstancesResponseBodyEventsLocation = None,
        online_meeting_info: ListEventsInstancesResponseBodyEventsOnlineMeetingInfo = None,
        organizer: ListEventsInstancesResponseBodyEventsOrganizer = None,
        recurrence: ListEventsInstancesResponseBodyEventsRecurrence = None,
        reminders: List[ListEventsInstancesResponseBodyEventsReminders] = None,
        series_master_id: str = None,
        start: ListEventsInstancesResponseBodyEventsStart = None,
        status: str = None,
        summary: str = None,
        update_time: str = None,
    ):
        # 日程参与人
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        # 日程描述
        self.description = description
        # 日程结束时间
        self.end = end
        # 日程事件id
        self.id = id
        # 是否为全天日程
        self.is_all_day = is_all_day
        # 日程地点
        self.location = location
        # 线上会议
        self.online_meeting_info = online_meeting_info
        # 日程组织人
        self.organizer = organizer
        # 日程重复规则
        self.recurrence = recurrence
        # 日程提醒
        self.reminders = reminders
        # 重复日程的主日程id，非重复日程为空
        self.series_master_id = series_master_id
        # 日程开始时间
        self.start = start
        # 日程状态
        self.status = status
        # 日程标题
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.series_master_id is not None:
            result['seriesMasterId'] = self.series_master_id
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = ListEventsInstancesResponseBodyEventsAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('organizer') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = ListEventsInstancesResponseBodyEventsReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('seriesMasterId') is not None:
            self.series_master_id = m.get('seriesMasterId')
        if m.get('start') is not None:
            temp_model = ListEventsInstancesResponseBodyEventsStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListEventsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        events: List[ListEventsInstancesResponseBodyEvents] = None,
    ):
        # 日程
        self.events = events

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = ListEventsInstancesResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        return self


class ListEventsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEventsInstancesResponseBody = None,
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
            temp_model = ListEventsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventsViewHeaders(TeaModel):
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


class ListEventsViewRequest(TeaModel):
    def __init__(
        self,
        max_attendees: int = None,
        max_results: int = None,
        next_token: str = None,
        time_max: str = None,
        time_min: str = None,
    ):
        # 每个日程的参与者查询个数，默认100，最大100。
        self.max_attendees = max_attendees
        # 返回的最大日程数，最大100个，默认100个。
        self.max_results = max_results
        # 查询翻页token
        self.next_token = next_token
        # 查询截止时间
        self.time_max = time_max
        # 查询开始时间
        self.time_min = time_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_attendees is not None:
            result['maxAttendees'] = self.max_attendees
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.time_max is not None:
            result['timeMax'] = self.time_max
        if self.time_min is not None:
            result['timeMin'] = self.time_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAttendees') is not None:
            self.max_attendees = m.get('maxAttendees')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('timeMax') is not None:
            self.time_max = m.get('timeMax')
        if m.get('timeMin') is not None:
            self.time_min = m.get('timeMin')
        return self


class ListEventsViewResponseBodyEventsAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsViewResponseBodyEventsEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsViewResponseBodyEventsLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        # 展示名称
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListEventsViewResponseBodyEventsOnlineMeetingInfo(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        url: str = None,
    ):
        self.conference_id = conference_id
        self.extra_info = extra_info
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEventsViewResponseBodyEventsOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        # 用户id
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class ListEventsViewResponseBodyEventsRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        # 循环模式类型(type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsViewResponseBodyEventsRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        # 范围类型(endDate, noEnd, numbered)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEventsViewResponseBodyEventsRecurrence(TeaModel):
    def __init__(
        self,
        pattern: ListEventsViewResponseBodyEventsRecurrencePattern = None,
        range: ListEventsViewResponseBodyEventsRecurrenceRange = None,
    ):
        # 重复模式
        self.pattern = pattern
        # 重复范围
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = ListEventsViewResponseBodyEventsRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = ListEventsViewResponseBodyEventsRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class ListEventsViewResponseBodyEventsStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        # 日期，格式：yyyyMMdd
        self.date = date
        # 时间戳，按照ISO 8601格式
        self.date_time = date_time
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class ListEventsViewResponseBodyEvents(TeaModel):
    def __init__(
        self,
        attendees: List[ListEventsViewResponseBodyEventsAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: ListEventsViewResponseBodyEventsEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: ListEventsViewResponseBodyEventsLocation = None,
        online_meeting_info: ListEventsViewResponseBodyEventsOnlineMeetingInfo = None,
        organizer: ListEventsViewResponseBodyEventsOrganizer = None,
        recurrence: ListEventsViewResponseBodyEventsRecurrence = None,
        series_master_id: str = None,
        start: ListEventsViewResponseBodyEventsStart = None,
        status: str = None,
        summary: str = None,
        update_time: str = None,
    ):
        # 日程参与人
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        # 日程描述
        self.description = description
        # 日程结束时间
        self.end = end
        # 日程事件id
        self.id = id
        # 是否为全天日程
        self.is_all_day = is_all_day
        # 日程地点
        self.location = location
        self.online_meeting_info = online_meeting_info
        # 日程组织人
        self.organizer = organizer
        # 日程重复规则
        self.recurrence = recurrence
        # 重复日程的主日程id，非重复日程为空
        self.series_master_id = series_master_id
        # 日程开始时间
        self.start = start
        # 日程状态
        self.status = status
        # 日程标题
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.online_meeting_info is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        if self.series_master_id is not None:
            result['seriesMasterId'] = self.series_master_id
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = ListEventsViewResponseBodyEventsAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = ListEventsViewResponseBodyEventsEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = ListEventsViewResponseBodyEventsLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('onlineMeetingInfo') is not None:
            temp_model = ListEventsViewResponseBodyEventsOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m['onlineMeetingInfo'])
        if m.get('organizer') is not None:
            temp_model = ListEventsViewResponseBodyEventsOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = ListEventsViewResponseBodyEventsRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        if m.get('seriesMasterId') is not None:
            self.series_master_id = m.get('seriesMasterId')
        if m.get('start') is not None:
            temp_model = ListEventsViewResponseBodyEventsStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListEventsViewResponseBody(TeaModel):
    def __init__(
        self,
        events: List[ListEventsViewResponseBodyEvents] = None,
        next_token: str = None,
    ):
        # 日程
        self.events = events
        # 翻页token
        self.next_token = next_token

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = ListEventsViewResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListEventsViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEventsViewResponseBody = None,
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
            temp_model = ListEventsViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PatchEventHeaders(TeaModel):
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


class PatchEventRequestAttendees(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
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


class PatchEventRequestEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class PatchEventRequestLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class PatchEventRequestRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PatchEventRequestRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PatchEventRequestRecurrence(TeaModel):
    def __init__(
        self,
        pattern: PatchEventRequestRecurrencePattern = None,
        range: PatchEventRequestRecurrenceRange = None,
    ):
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = PatchEventRequestRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = PatchEventRequestRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class PatchEventRequestReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: int = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class PatchEventRequestStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class PatchEventRequest(TeaModel):
    def __init__(
        self,
        attendees: List[PatchEventRequestAttendees] = None,
        description: str = None,
        end: PatchEventRequestEnd = None,
        extra: Dict[str, str] = None,
        id: str = None,
        is_all_day: bool = None,
        location: PatchEventRequestLocation = None,
        recurrence: PatchEventRequestRecurrence = None,
        reminders: List[PatchEventRequestReminders] = None,
        start: PatchEventRequestStart = None,
        summary: str = None,
    ):
        self.attendees = attendees
        self.description = description
        self.end = end
        # 扩展信息
        self.extra = extra
        # 日程id
        self.id = id
        self.is_all_day = is_all_day
        self.location = location
        self.recurrence = recurrence
        self.reminders = reminders
        # 日程开始时间
        self.start = start
        # 日程标题
        self.summary = summary

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = PatchEventRequestAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = PatchEventRequestEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = PatchEventRequestLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('recurrence') is not None:
            temp_model = PatchEventRequestRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = PatchEventRequestReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = PatchEventRequestStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        return self


class PatchEventResponseBodyAttendees(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class PatchEventResponseBodyEnd(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class PatchEventResponseBodyLocation(TeaModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class PatchEventResponseBodyOrganizer(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        # 用户名
        self.display_name = display_name
        self.id = id
        # 回复状态
        self.response_status = response_status
        # 是否是当前登陆用户
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        if self.self_ is not None:
            result['self'] = self.self_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        if m.get('self') is not None:
            self.self_ = m.get('self')
        return self


class PatchEventResponseBodyRecurrencePattern(TeaModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.index is not None:
            result['index'] = self.index
        if self.interval is not None:
            result['interval'] = self.interval
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PatchEventResponseBodyRecurrenceRange(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PatchEventResponseBodyRecurrence(TeaModel):
    def __init__(
        self,
        pattern: PatchEventResponseBodyRecurrencePattern = None,
        range: PatchEventResponseBodyRecurrenceRange = None,
    ):
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()
        if self.range is not None:
            result['range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = PatchEventResponseBodyRecurrencePattern()
            self.pattern = temp_model.from_map(m['pattern'])
        if m.get('range') is not None:
            temp_model = PatchEventResponseBodyRecurrenceRange()
            self.range = temp_model.from_map(m['range'])
        return self


class PatchEventResponseBodyReminders(TeaModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.minutes is not None:
            result['minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')
        return self


class PatchEventResponseBodyStart(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.date_time is not None:
            result['dateTime'] = self.date_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class PatchEventResponseBody(TeaModel):
    def __init__(
        self,
        attendees: List[PatchEventResponseBodyAttendees] = None,
        create_time: str = None,
        description: str = None,
        end: PatchEventResponseBodyEnd = None,
        id: str = None,
        is_all_day: bool = None,
        location: PatchEventResponseBodyLocation = None,
        organizer: PatchEventResponseBodyOrganizer = None,
        recurrence: PatchEventResponseBodyRecurrence = None,
        reminders: List[PatchEventResponseBodyReminders] = None,
        start: PatchEventResponseBodyStart = None,
        summary: str = None,
        update_time: str = None,
    ):
        self.attendees = attendees
        # 创建时间
        self.create_time = create_time
        self.description = description
        self.end = end
        self.id = id
        self.is_all_day = is_all_day
        self.location = location
        self.organizer = organizer
        self.recurrence = recurrence
        self.reminders = reminders
        # 日程开始时间
        self.start = start
        self.summary = summary
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for k in self.attendees:
                if k:
                    k.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.organizer:
            self.organizer.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for k in self.reminders:
                if k:
                    k.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendees'] = []
        if self.attendees is not None:
            for k in self.attendees:
                result['attendees'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.end is not None:
            result['end'] = self.end.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.is_all_day is not None:
            result['isAllDay'] = self.is_all_day
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.organizer is not None:
            result['organizer'] = self.organizer.to_map()
        if self.recurrence is not None:
            result['recurrence'] = self.recurrence.to_map()
        result['reminders'] = []
        if self.reminders is not None:
            for k in self.reminders:
                result['reminders'].append(k.to_map() if k else None)
        if self.start is not None:
            result['start'] = self.start.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('attendees') is not None:
            for k in m.get('attendees'):
                temp_model = PatchEventResponseBodyAttendees()
                self.attendees.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('end') is not None:
            temp_model = PatchEventResponseBodyEnd()
            self.end = temp_model.from_map(m['end'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAllDay') is not None:
            self.is_all_day = m.get('isAllDay')
        if m.get('location') is not None:
            temp_model = PatchEventResponseBodyLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('organizer') is not None:
            temp_model = PatchEventResponseBodyOrganizer()
            self.organizer = temp_model.from_map(m['organizer'])
        if m.get('recurrence') is not None:
            temp_model = PatchEventResponseBodyRecurrence()
            self.recurrence = temp_model.from_map(m['recurrence'])
        self.reminders = []
        if m.get('reminders') is not None:
            for k in m.get('reminders'):
                temp_model = PatchEventResponseBodyReminders()
                self.reminders.append(temp_model.from_map(k))
        if m.get('start') is not None:
            temp_model = PatchEventResponseBodyStart()
            self.start = temp_model.from_map(m['start'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class PatchEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PatchEventResponseBody = None,
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
            temp_model = PatchEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAttendeeHeaders(TeaModel):
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


class RemoveAttendeeRequestAttendeesToRemove(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
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


class RemoveAttendeeRequest(TeaModel):
    def __init__(
        self,
        attendees_to_remove: List[RemoveAttendeeRequestAttendeesToRemove] = None,
    ):
        self.attendees_to_remove = attendees_to_remove

    def validate(self):
        if self.attendees_to_remove:
            for k in self.attendees_to_remove:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attendeesToRemove'] = []
        if self.attendees_to_remove is not None:
            for k in self.attendees_to_remove:
                result['attendeesToRemove'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees_to_remove = []
        if m.get('attendeesToRemove') is not None:
            for k in m.get('attendeesToRemove'):
                temp_model = RemoveAttendeeRequestAttendeesToRemove()
                self.attendees_to_remove.append(temp_model.from_map(k))
        return self


class RemoveAttendeeResponse(TeaModel):
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


class RespondEventHeaders(TeaModel):
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


class RespondEventRequest(TeaModel):
    def __init__(
        self,
        response_status: str = None,
    ):
        self.response_status = response_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_status is not None:
            result['responseStatus'] = self.response_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('responseStatus') is not None:
            self.response_status = m.get('responseStatus')
        return self


class RespondEventResponse(TeaModel):
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


class SignInHeaders(TeaModel):
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


class SignInResponseBody(TeaModel):
    def __init__(
        self,
        check_in_time: int = None,
    ):
        # 签到时间戳
        self.check_in_time = check_in_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['checkInTime'] = self.check_in_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkInTime') is not None:
            self.check_in_time = m.get('checkInTime')
        return self


class SignInResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SignInResponseBody = None,
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
            temp_model = SignInResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignOutHeaders(TeaModel):
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


class SignOutResponseBody(TeaModel):
    def __init__(
        self,
        check_out_time: int = None,
    ):
        # 签退时间戳
        self.check_out_time = check_out_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_out_time is not None:
            result['checkOutTime'] = self.check_out_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkOutTime') is not None:
            self.check_out_time = m.get('checkOutTime')
        return self


class SignOutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SignOutResponseBody = None,
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
            temp_model = SignOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeCalendarHeaders(TeaModel):
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


class SubscribeCalendarResponse(TeaModel):
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


