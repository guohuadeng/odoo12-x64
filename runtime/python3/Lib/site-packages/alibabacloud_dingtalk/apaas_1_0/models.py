# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BatchCreateTemplateHeaders(TeaModel):
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


class BatchCreateTemplateRequestTemplateList(TeaModel):
    def __init__(
        self,
        adapt_env: List[str] = None,
        app_desc: str = None,
        app_icon: str = None,
        case_video_list: List[str] = None,
        category_code: str = None,
        cover_img_list: List[str] = None,
        exp_url: str = None,
        industry_label_list: List[str] = None,
        install_times: int = None,
        mobile_preview_media_list: List[str] = None,
        name: str = None,
        preview_media_list: List[str] = None,
        provider_name: str = None,
        role_label_list: List[str] = None,
        simple_desc: str = None,
        template_key: str = None,
        use_cases_media_list: List[str] = None,
    ):
        # adaptEnv
        self.adapt_env = adapt_env
        # appDesc
        self.app_desc = app_desc
        # appIcon
        self.app_icon = app_icon
        # caseVideoList
        self.case_video_list = case_video_list
        # category
        self.category_code = category_code
        # coverImgList
        self.cover_img_list = cover_img_list
        # expUrl
        self.exp_url = exp_url
        # industryLabelList
        self.industry_label_list = industry_label_list
        # installTimes
        self.install_times = install_times
        # mobilePreviewMediaList
        self.mobile_preview_media_list = mobile_preview_media_list
        # name
        self.name = name
        # previewMediaList
        self.preview_media_list = preview_media_list
        # providerName
        self.provider_name = provider_name
        # roleLabelList
        self.role_label_list = role_label_list
        # simpleDesc
        self.simple_desc = simple_desc
        # templateKey
        self.template_key = template_key
        # useCasesMediaList
        self.use_cases_media_list = use_cases_media_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_env is not None:
            result['adaptEnv'] = self.adapt_env
        if self.app_desc is not None:
            result['appDesc'] = self.app_desc
        if self.app_icon is not None:
            result['appIcon'] = self.app_icon
        if self.case_video_list is not None:
            result['caseVideoList'] = self.case_video_list
        if self.category_code is not None:
            result['categoryCode'] = self.category_code
        if self.cover_img_list is not None:
            result['coverImgList'] = self.cover_img_list
        if self.exp_url is not None:
            result['expUrl'] = self.exp_url
        if self.industry_label_list is not None:
            result['industryLabelList'] = self.industry_label_list
        if self.install_times is not None:
            result['installTimes'] = self.install_times
        if self.mobile_preview_media_list is not None:
            result['mobilePreviewMediaList'] = self.mobile_preview_media_list
        if self.name is not None:
            result['name'] = self.name
        if self.preview_media_list is not None:
            result['previewMediaList'] = self.preview_media_list
        if self.provider_name is not None:
            result['providerName'] = self.provider_name
        if self.role_label_list is not None:
            result['roleLabelList'] = self.role_label_list
        if self.simple_desc is not None:
            result['simpleDesc'] = self.simple_desc
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.use_cases_media_list is not None:
            result['useCasesMediaList'] = self.use_cases_media_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptEnv') is not None:
            self.adapt_env = m.get('adaptEnv')
        if m.get('appDesc') is not None:
            self.app_desc = m.get('appDesc')
        if m.get('appIcon') is not None:
            self.app_icon = m.get('appIcon')
        if m.get('caseVideoList') is not None:
            self.case_video_list = m.get('caseVideoList')
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')
        if m.get('coverImgList') is not None:
            self.cover_img_list = m.get('coverImgList')
        if m.get('expUrl') is not None:
            self.exp_url = m.get('expUrl')
        if m.get('industryLabelList') is not None:
            self.industry_label_list = m.get('industryLabelList')
        if m.get('installTimes') is not None:
            self.install_times = m.get('installTimes')
        if m.get('mobilePreviewMediaList') is not None:
            self.mobile_preview_media_list = m.get('mobilePreviewMediaList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('previewMediaList') is not None:
            self.preview_media_list = m.get('previewMediaList')
        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')
        if m.get('roleLabelList') is not None:
            self.role_label_list = m.get('roleLabelList')
        if m.get('simpleDesc') is not None:
            self.simple_desc = m.get('simpleDesc')
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('useCasesMediaList') is not None:
            self.use_cases_media_list = m.get('useCasesMediaList')
        return self


class BatchCreateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_list: List[BatchCreateTemplateRequestTemplateList] = None,
    ):
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['templateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['templateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_list = []
        if m.get('templateList') is not None:
            for k in m.get('templateList'):
                temp_model = BatchCreateTemplateRequestTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class BatchCreateTemplateResponseBodyCreateResultList(TeaModel):
    def __init__(
        self,
        template_key: str = None,
        value: str = None,
    ):
        self.template_key = template_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchCreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        create_result_list: List[BatchCreateTemplateResponseBodyCreateResultList] = None,
    ):
        self.create_result_list = create_result_list

    def validate(self):
        if self.create_result_list:
            for k in self.create_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createResultList'] = []
        if self.create_result_list is not None:
            for k in self.create_result_list:
                result['createResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_result_list = []
        if m.get('createResultList') is not None:
            for k in m.get('createResultList'):
                temp_model = BatchCreateTemplateResponseBodyCreateResultList()
                self.create_result_list.append(temp_model.from_map(k))
        return self


class BatchCreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchCreateTemplateResponseBody = None,
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
            temp_model = BatchCreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryByTemplateKeyHeaders(TeaModel):
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


class BatchQueryByTemplateKeyRequest(TeaModel):
    def __init__(
        self,
        template_keys: List[str] = None,
    ):
        self.template_keys = template_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_keys is not None:
            result['templateKeys'] = self.template_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateKeys') is not None:
            self.template_keys = m.get('templateKeys')
        return self


class BatchQueryByTemplateKeyResponseBodyTemplateList(TeaModel):
    def __init__(
        self,
        adapt_env: List[str] = None,
        app_desc: str = None,
        app_icon: str = None,
        case_video_list: List[str] = None,
        category: str = None,
        cover_img_list: List[str] = None,
        exp_url: str = None,
        industry_label_list: List[str] = None,
        install_times: float = None,
        mobile_preview_media_list: List[str] = None,
        name: str = None,
        preview_media_list: List[str] = None,
        provider_name: str = None,
        role_label_list: List[str] = None,
        simple_desc: str = None,
        template_key: str = None,
        use_cases_media_list: List[str] = None,
    ):
        self.adapt_env = adapt_env
        self.app_desc = app_desc
        self.app_icon = app_icon
        self.case_video_list = case_video_list
        self.category = category
        self.cover_img_list = cover_img_list
        self.exp_url = exp_url
        self.industry_label_list = industry_label_list
        self.install_times = install_times
        self.mobile_preview_media_list = mobile_preview_media_list
        self.name = name
        self.preview_media_list = preview_media_list
        self.provider_name = provider_name
        self.role_label_list = role_label_list
        self.simple_desc = simple_desc
        self.template_key = template_key
        self.use_cases_media_list = use_cases_media_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_env is not None:
            result['adaptEnv'] = self.adapt_env
        if self.app_desc is not None:
            result['appDesc'] = self.app_desc
        if self.app_icon is not None:
            result['appIcon'] = self.app_icon
        if self.case_video_list is not None:
            result['caseVideoList'] = self.case_video_list
        if self.category is not None:
            result['category'] = self.category
        if self.cover_img_list is not None:
            result['coverImgList'] = self.cover_img_list
        if self.exp_url is not None:
            result['expUrl'] = self.exp_url
        if self.industry_label_list is not None:
            result['industryLabelList'] = self.industry_label_list
        if self.install_times is not None:
            result['installTimes'] = self.install_times
        if self.mobile_preview_media_list is not None:
            result['mobilePreviewMediaList'] = self.mobile_preview_media_list
        if self.name is not None:
            result['name'] = self.name
        if self.preview_media_list is not None:
            result['previewMediaList'] = self.preview_media_list
        if self.provider_name is not None:
            result['providerName'] = self.provider_name
        if self.role_label_list is not None:
            result['roleLabelList'] = self.role_label_list
        if self.simple_desc is not None:
            result['simpleDesc'] = self.simple_desc
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.use_cases_media_list is not None:
            result['useCasesMediaList'] = self.use_cases_media_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptEnv') is not None:
            self.adapt_env = m.get('adaptEnv')
        if m.get('appDesc') is not None:
            self.app_desc = m.get('appDesc')
        if m.get('appIcon') is not None:
            self.app_icon = m.get('appIcon')
        if m.get('caseVideoList') is not None:
            self.case_video_list = m.get('caseVideoList')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('coverImgList') is not None:
            self.cover_img_list = m.get('coverImgList')
        if m.get('expUrl') is not None:
            self.exp_url = m.get('expUrl')
        if m.get('industryLabelList') is not None:
            self.industry_label_list = m.get('industryLabelList')
        if m.get('installTimes') is not None:
            self.install_times = m.get('installTimes')
        if m.get('mobilePreviewMediaList') is not None:
            self.mobile_preview_media_list = m.get('mobilePreviewMediaList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('previewMediaList') is not None:
            self.preview_media_list = m.get('previewMediaList')
        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')
        if m.get('roleLabelList') is not None:
            self.role_label_list = m.get('roleLabelList')
        if m.get('simpleDesc') is not None:
            self.simple_desc = m.get('simpleDesc')
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('useCasesMediaList') is not None:
            self.use_cases_media_list = m.get('useCasesMediaList')
        return self


class BatchQueryByTemplateKeyResponseBody(TeaModel):
    def __init__(
        self,
        template_list: List[BatchQueryByTemplateKeyResponseBodyTemplateList] = None,
    ):
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['templateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['templateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_list = []
        if m.get('templateList') is not None:
            for k in m.get('templateList'):
                temp_model = BatchQueryByTemplateKeyResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class BatchQueryByTemplateKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchQueryByTemplateKeyResponseBody = None,
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
            temp_model = BatchQueryByTemplateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateTemplateHeaders(TeaModel):
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


class BatchUpdateTemplateRequestTemplateList(TeaModel):
    def __init__(
        self,
        adapt_env: List[str] = None,
        app_desc: str = None,
        app_icon: str = None,
        case_video_list: List[str] = None,
        category_code: str = None,
        cover_img_list: List[str] = None,
        exp_url: str = None,
        industry_label_list: List[str] = None,
        mobile_preview_media_list: List[str] = None,
        name: str = None,
        preview_media_list: List[str] = None,
        provider_name: str = None,
        role_label_list: List[str] = None,
        simple_desc: str = None,
        template_key: str = None,
        use_cases_media_list: List[str] = None,
    ):
        # adaptEnv
        self.adapt_env = adapt_env
        # appDesc
        self.app_desc = app_desc
        # appIcon
        self.app_icon = app_icon
        # caseVideoList
        self.case_video_list = case_video_list
        # category
        self.category_code = category_code
        # coverImgList
        self.cover_img_list = cover_img_list
        # expUrl
        self.exp_url = exp_url
        # industryLabelList
        self.industry_label_list = industry_label_list
        # mobilePreviewMediaList
        self.mobile_preview_media_list = mobile_preview_media_list
        # name
        self.name = name
        # previewMediaList
        self.preview_media_list = preview_media_list
        # providerName
        self.provider_name = provider_name
        # roleLabelList
        self.role_label_list = role_label_list
        # simpleDesc
        self.simple_desc = simple_desc
        # templateKey
        self.template_key = template_key
        # useCasesMediaList
        self.use_cases_media_list = use_cases_media_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_env is not None:
            result['adaptEnv'] = self.adapt_env
        if self.app_desc is not None:
            result['appDesc'] = self.app_desc
        if self.app_icon is not None:
            result['appIcon'] = self.app_icon
        if self.case_video_list is not None:
            result['caseVideoList'] = self.case_video_list
        if self.category_code is not None:
            result['categoryCode'] = self.category_code
        if self.cover_img_list is not None:
            result['coverImgList'] = self.cover_img_list
        if self.exp_url is not None:
            result['expUrl'] = self.exp_url
        if self.industry_label_list is not None:
            result['industryLabelList'] = self.industry_label_list
        if self.mobile_preview_media_list is not None:
            result['mobilePreviewMediaList'] = self.mobile_preview_media_list
        if self.name is not None:
            result['name'] = self.name
        if self.preview_media_list is not None:
            result['previewMediaList'] = self.preview_media_list
        if self.provider_name is not None:
            result['providerName'] = self.provider_name
        if self.role_label_list is not None:
            result['roleLabelList'] = self.role_label_list
        if self.simple_desc is not None:
            result['simpleDesc'] = self.simple_desc
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.use_cases_media_list is not None:
            result['useCasesMediaList'] = self.use_cases_media_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptEnv') is not None:
            self.adapt_env = m.get('adaptEnv')
        if m.get('appDesc') is not None:
            self.app_desc = m.get('appDesc')
        if m.get('appIcon') is not None:
            self.app_icon = m.get('appIcon')
        if m.get('caseVideoList') is not None:
            self.case_video_list = m.get('caseVideoList')
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')
        if m.get('coverImgList') is not None:
            self.cover_img_list = m.get('coverImgList')
        if m.get('expUrl') is not None:
            self.exp_url = m.get('expUrl')
        if m.get('industryLabelList') is not None:
            self.industry_label_list = m.get('industryLabelList')
        if m.get('mobilePreviewMediaList') is not None:
            self.mobile_preview_media_list = m.get('mobilePreviewMediaList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('previewMediaList') is not None:
            self.preview_media_list = m.get('previewMediaList')
        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')
        if m.get('roleLabelList') is not None:
            self.role_label_list = m.get('roleLabelList')
        if m.get('simpleDesc') is not None:
            self.simple_desc = m.get('simpleDesc')
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('useCasesMediaList') is not None:
            self.use_cases_media_list = m.get('useCasesMediaList')
        return self


class BatchUpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_list: List[BatchUpdateTemplateRequestTemplateList] = None,
    ):
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['templateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['templateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_list = []
        if m.get('templateList') is not None:
            for k in m.get('templateList'):
                temp_model = BatchUpdateTemplateRequestTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class BatchUpdateTemplateResponseBodyUpdateResultList(TeaModel):
    def __init__(
        self,
        template_key: str = None,
        value: str = None,
    ):
        self.template_key = template_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class BatchUpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        update_result_list: List[BatchUpdateTemplateResponseBodyUpdateResultList] = None,
    ):
        self.update_result_list = update_result_list

    def validate(self):
        if self.update_result_list:
            for k in self.update_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['updateResultList'] = []
        if self.update_result_list is not None:
            for k in self.update_result_list:
                result['updateResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.update_result_list = []
        if m.get('updateResultList') is not None:
            for k in m.get('updateResultList'):
                temp_model = BatchUpdateTemplateResponseBodyUpdateResultList()
                self.update_result_list.append(temp_model.from_map(k))
        return self


class BatchUpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUpdateTemplateResponseBody = None,
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
            temp_model = BatchUpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIndustryTagListHeaders(TeaModel):
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


class QueryIndustryTagListResponseBody(TeaModel):
    def __init__(
        self,
        industry_list: List[str] = None,
    ):
        self.industry_list = industry_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry_list is not None:
            result['industryList'] = self.industry_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industryList') is not None:
            self.industry_list = m.get('industryList')
        return self


class QueryIndustryTagListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIndustryTagListResponseBody = None,
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
            temp_model = QueryIndustryTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRoleTagListHeaders(TeaModel):
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


class QueryRoleTagListResponseBody(TeaModel):
    def __init__(
        self,
        role_list: List[str] = None,
    ):
        self.role_list = role_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_list is not None:
            result['roleList'] = self.role_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleList') is not None:
            self.role_list = m.get('roleList')
        return self


class QueryRoleTagListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRoleTagListResponseBody = None,
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
            temp_model = QueryRoleTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTemplateCategorysHeaders(TeaModel):
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


class QueryTemplateCategorysResponseBodyCategoryList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # 分类编码
        self.code = code
        # 分类名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryTemplateCategorysResponseBody(TeaModel):
    def __init__(
        self,
        category_list: List[QueryTemplateCategorysResponseBodyCategoryList] = None,
        total: str = None,
    ):
        self.category_list = category_list
        # 总数
        self.total = total

    def validate(self):
        if self.category_list:
            for k in self.category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['categoryList'] = []
        if self.category_list is not None:
            for k in self.category_list:
                result['categoryList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('categoryList') is not None:
            for k in m.get('categoryList'):
                temp_model = QueryTemplateCategorysResponseBodyCategoryList()
                self.category_list.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryTemplateCategorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTemplateCategorysResponseBody = None,
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
            temp_model = QueryTemplateCategorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallAuditTemplateHeaders(TeaModel):
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


class RecallAuditTemplateRequest(TeaModel):
    def __init__(
        self,
        template_keys: List[str] = None,
    ):
        self.template_keys = template_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_keys is not None:
            result['templateKeys'] = self.template_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateKeys') is not None:
            self.template_keys = m.get('templateKeys')
        return self


class RecallAuditTemplateResponseBodyRecallResult(TeaModel):
    def __init__(
        self,
        template_key: str = None,
        value: str = None,
    ):
        self.template_key = template_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RecallAuditTemplateResponseBody(TeaModel):
    def __init__(
        self,
        recall_result: List[RecallAuditTemplateResponseBodyRecallResult] = None,
    ):
        self.recall_result = recall_result

    def validate(self):
        if self.recall_result:
            for k in self.recall_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['recallResult'] = []
        if self.recall_result is not None:
            for k in self.recall_result:
                result['recallResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recall_result = []
        if m.get('recallResult') is not None:
            for k in m.get('recallResult'):
                temp_model = RecallAuditTemplateResponseBodyRecallResult()
                self.recall_result.append(temp_model.from_map(k))
        return self


class RecallAuditTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecallAuditTemplateResponseBody = None,
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
            temp_model = RecallAuditTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


