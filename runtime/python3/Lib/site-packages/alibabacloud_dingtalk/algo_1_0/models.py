# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class NlpWordDistinguishHeaders(TeaModel):
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


class NlpWordDistinguishRequestAttachExtractDecisionInfo(TeaModel):
    def __init__(
        self,
        black_words: List[str] = None,
        candidate_words: List[str] = None,
        corp_id: str = None,
        dept_ids: List[str] = None,
        user_id: str = None,
    ):
        self.black_words = black_words
        self.candidate_words = candidate_words
        self.corp_id = corp_id
        self.dept_ids = dept_ids
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_words is not None:
            result['blackWords'] = self.black_words
        if self.candidate_words is not None:
            result['candidateWords'] = self.candidate_words
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blackWords') is not None:
            self.black_words = m.get('blackWords')
        if m.get('candidateWords') is not None:
            self.candidate_words = m.get('candidateWords')
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class NlpWordDistinguishRequest(TeaModel):
    def __init__(
        self,
        attach_extract_decision_info: NlpWordDistinguishRequestAttachExtractDecisionInfo = None,
        isv_app_id: str = None,
        text: str = None,
    ):
        self.attach_extract_decision_info = attach_extract_decision_info
        self.isv_app_id = isv_app_id
        self.text = text

    def validate(self):
        if self.attach_extract_decision_info:
            self.attach_extract_decision_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_extract_decision_info is not None:
            result['attachExtractDecisionInfo'] = self.attach_extract_decision_info.to_map()
        if self.isv_app_id is not None:
            result['isvAppId'] = self.isv_app_id
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachExtractDecisionInfo') is not None:
            temp_model = NlpWordDistinguishRequestAttachExtractDecisionInfo()
            self.attach_extract_decision_info = temp_model.from_map(m['attachExtractDecisionInfo'])
        if m.get('isvAppId') is not None:
            self.isv_app_id = m.get('isvAppId')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class NlpWordDistinguishResponseBodyWordEntities(TeaModel):
    def __init__(
        self,
        word: str = None,
    ):
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class NlpWordDistinguishResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        word_entities: List[NlpWordDistinguishResponseBodyWordEntities] = None,
    ):
        self.request_id = request_id
        self.word_entities = word_entities

    def validate(self):
        if self.word_entities:
            for k in self.word_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['wordEntities'] = []
        if self.word_entities is not None:
            for k in self.word_entities:
                result['wordEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.word_entities = []
        if m.get('wordEntities') is not None:
            for k in m.get('wordEntities'):
                temp_model = NlpWordDistinguishResponseBodyWordEntities()
                self.word_entities.append(temp_model.from_map(k))
        return self


class NlpWordDistinguishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: NlpWordDistinguishResponseBody = None,
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
            temp_model = NlpWordDistinguishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OkrOpenRecommendHeaders(TeaModel):
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


class OkrOpenRecommendRequestCandidateOkrItemsOkrInfosKeyResultInfos(TeaModel):
    def __init__(
        self,
        kr: str = None,
        kr_id: str = None,
        words: List[str] = None,
    ):
        self.kr = kr
        self.kr_id = kr_id
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kr is not None:
            result['kr'] = self.kr
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kr') is not None:
            self.kr = m.get('kr')
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class OkrOpenRecommendRequestCandidateOkrItemsOkrInfos(TeaModel):
    def __init__(
        self,
        key_result_infos: List[OkrOpenRecommendRequestCandidateOkrItemsOkrInfosKeyResultInfos] = None,
        objective: str = None,
        objective_id: str = None,
        words: List[str] = None,
    ):
        self.key_result_infos = key_result_infos
        self.objective = objective
        self.objective_id = objective_id
        self.words = words

    def validate(self):
        if self.key_result_infos:
            for k in self.key_result_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keyResultInfos'] = []
        if self.key_result_infos is not None:
            for k in self.key_result_infos:
                result['keyResultInfos'].append(k.to_map() if k else None)
        if self.objective is not None:
            result['objective'] = self.objective
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_result_infos = []
        if m.get('keyResultInfos') is not None:
            for k in m.get('keyResultInfos'):
                temp_model = OkrOpenRecommendRequestCandidateOkrItemsOkrInfosKeyResultInfos()
                self.key_result_infos.append(temp_model.from_map(k))
        if m.get('objective') is not None:
            self.objective = m.get('objective')
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class OkrOpenRecommendRequestCandidateOkrItems(TeaModel):
    def __init__(
        self,
        okr_infos: List[OkrOpenRecommendRequestCandidateOkrItemsOkrInfos] = None,
        relation: str = None,
        user_id: str = None,
    ):
        self.okr_infos = okr_infos
        self.relation = relation
        self.user_id = user_id

    def validate(self):
        if self.okr_infos:
            for k in self.okr_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['okrInfos'] = []
        if self.okr_infos is not None:
            for k in self.okr_infos:
                result['okrInfos'].append(k.to_map() if k else None)
        if self.relation is not None:
            result['relation'] = self.relation
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.okr_infos = []
        if m.get('okrInfos') is not None:
            for k in m.get('okrInfos'):
                temp_model = OkrOpenRecommendRequestCandidateOkrItemsOkrInfos()
                self.okr_infos.append(temp_model.from_map(k))
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OkrOpenRecommendRequest(TeaModel):
    def __init__(
        self,
        candidate_okr_items: List[OkrOpenRecommendRequestCandidateOkrItems] = None,
        corp_id: str = None,
        dept_ids: List[str] = None,
        isv_app_id: str = None,
        user_id: str = None,
        words: List[str] = None,
    ):
        self.candidate_okr_items = candidate_okr_items
        self.corp_id = corp_id
        self.dept_ids = dept_ids
        self.isv_app_id = isv_app_id
        self.user_id = user_id
        self.words = words

    def validate(self):
        if self.candidate_okr_items:
            for k in self.candidate_okr_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['candidateOkrItems'] = []
        if self.candidate_okr_items is not None:
            for k in self.candidate_okr_items:
                result['candidateOkrItems'].append(k.to_map() if k else None)
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        if self.dept_ids is not None:
            result['deptIds'] = self.dept_ids
        if self.isv_app_id is not None:
            result['isvAppId'] = self.isv_app_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.candidate_okr_items = []
        if m.get('candidateOkrItems') is not None:
            for k in m.get('candidateOkrItems'):
                temp_model = OkrOpenRecommendRequestCandidateOkrItems()
                self.candidate_okr_items.append(temp_model.from_map(k))
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        if m.get('deptIds') is not None:
            self.dept_ids = m.get('deptIds')
        if m.get('isvAppId') is not None:
            self.isv_app_id = m.get('isvAppId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class OkrOpenRecommendResponseBodyOkrRecommendItemsKrResultRelatedResults(TeaModel):
    def __init__(
        self,
        kr_id: str = None,
        words: List[str] = None,
    ):
        # krId
        self.kr_id = kr_id
        # words
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kr_id is not None:
            result['krId'] = self.kr_id
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('krId') is not None:
            self.kr_id = m.get('krId')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class OkrOpenRecommendResponseBodyOkrRecommendItemsObjectiveRelatedResults(TeaModel):
    def __init__(
        self,
        objective_id: str = None,
        words: List[str] = None,
    ):
        # objectiveId
        self.objective_id = objective_id
        # words
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.objective_id is not None:
            result['objectiveId'] = self.objective_id
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectiveId') is not None:
            self.objective_id = m.get('objectiveId')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class OkrOpenRecommendResponseBodyOkrRecommendItems(TeaModel):
    def __init__(
        self,
        kr_result_related_results: List[OkrOpenRecommendResponseBodyOkrRecommendItemsKrResultRelatedResults] = None,
        objective_related_results: List[OkrOpenRecommendResponseBodyOkrRecommendItemsObjectiveRelatedResults] = None,
        related_level: int = None,
        user_id: str = None,
    ):
        # krResultRelatedResults
        self.kr_result_related_results = kr_result_related_results
        # objectiveRelatedResults
        self.objective_related_results = objective_related_results
        # relatedLevel
        self.related_level = related_level
        # userId
        self.user_id = user_id

    def validate(self):
        if self.kr_result_related_results:
            for k in self.kr_result_related_results:
                if k:
                    k.validate()
        if self.objective_related_results:
            for k in self.objective_related_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['krResultRelatedResults'] = []
        if self.kr_result_related_results is not None:
            for k in self.kr_result_related_results:
                result['krResultRelatedResults'].append(k.to_map() if k else None)
        result['objectiveRelatedResults'] = []
        if self.objective_related_results is not None:
            for k in self.objective_related_results:
                result['objectiveRelatedResults'].append(k.to_map() if k else None)
        if self.related_level is not None:
            result['relatedLevel'] = self.related_level
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kr_result_related_results = []
        if m.get('krResultRelatedResults') is not None:
            for k in m.get('krResultRelatedResults'):
                temp_model = OkrOpenRecommendResponseBodyOkrRecommendItemsKrResultRelatedResults()
                self.kr_result_related_results.append(temp_model.from_map(k))
        self.objective_related_results = []
        if m.get('objectiveRelatedResults') is not None:
            for k in m.get('objectiveRelatedResults'):
                temp_model = OkrOpenRecommendResponseBodyOkrRecommendItemsObjectiveRelatedResults()
                self.objective_related_results.append(temp_model.from_map(k))
        if m.get('relatedLevel') is not None:
            self.related_level = m.get('relatedLevel')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OkrOpenRecommendResponseBody(TeaModel):
    def __init__(
        self,
        okr_recommend_items: List[OkrOpenRecommendResponseBodyOkrRecommendItems] = None,
        request_id: str = None,
    ):
        # okrRecommendItems
        self.okr_recommend_items = okr_recommend_items
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.okr_recommend_items:
            for k in self.okr_recommend_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['okrRecommendItems'] = []
        if self.okr_recommend_items is not None:
            for k in self.okr_recommend_items:
                result['okrRecommendItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.okr_recommend_items = []
        if m.get('okrRecommendItems') is not None:
            for k in m.get('okrRecommendItems'):
                temp_model = OkrOpenRecommendResponseBodyOkrRecommendItems()
                self.okr_recommend_items.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OkrOpenRecommendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OkrOpenRecommendResponseBody = None,
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
            temp_model = OkrOpenRecommendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


