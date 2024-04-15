#!/usr/bin/env python
# coding=utf-8
"""
client, 同步、异步
"""
import json
import tornado.gen
import requests
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from kdniao.api import API
from kdniao.mdutils import utf8, urlencode

from kdniao.conf import HEADERS, KdNiaoConfig, APIErrorCode, BizRespCode


class KdNiaoClient(API):
    """
    Blocking Client
    """

    def __init__(self, app_id, app_key, is_prod=True):
        """
        init
        :param int app_id: app id
        :param str app_key: app key
        :param bool is_prod: env type, prod or test, default is True
        """
        env_type = "prod" if is_prod else "test"
        super(KdNiaoClient, self).__init__(app_id, app_key, env_type=env_type)

    def _request(self, rtype, data, **kwargs):
        """
        prepare request
        :param str rtype:
        :param dict data:
        :param kwargs:
        :return:
        """
        timeout = kwargs.get("timeout")
        timeout = self._parese_time_out(timeout)

        url = self._gen_api_url(rtype)
        rdata = self._prepare_req_params(rtype, data)

        try:
            res = self._post(url, rdata, timeout)
        except requests.exceptions.Timeout:
            res = requests.Response()
            res.status_code = 599
            res._content = ""
            res.encoding = "utf-8"
            res.url = url
            res.reason = "timeout"

        resp = self._parse_http_resp(res.status_code, res.reason, res.text, res.url)
        res = self._parse_api_resp(resp)

        return res

    @classmethod
    def _post(cls, url, data, timeout=(10, 10)):
        """
        send post request
        :param str url:
        :param dict data:
        :param object timeout: tuple or an int object
        :return:
        """
        r = requests.post(url, data, headers=HEADERS, timeout=timeout)
        r.encoding = "utf-8"
        return r

    @classmethod
    def _parese_time_out(cls, timeout):
        """
        parse timeout value
        :param object timeout:
        :return:
        """
        res = KdNiaoConfig.DEFAULT_TIMEOUT  # seconds
        is_valid = True
        if isinstance(timeout, type(None)):
            pass
        elif isinstance(timeout, (int, float)):
            res = (timeout, timeout)
        elif isinstance(timeout, tuple):
            for i in timeout:
                if not isinstance(i, (int, float)):
                    is_valid = False
            res = timeout
        else:
            is_valid = False
        if not is_valid:
            raise ValueError("timeout must be an int or a tuple include int object")
        return res

    def _parse_http_resp(self, code, reason, body, url):
        """
        parse http response
        :param int code: http resp code
        :param str reason: http reason
        :param str body: resp body
        :param str url: request url
        :return dict: {
            "code_http": http code,
            "Message": error message,
            "data": origin dict
        }
        """

        resp = {
            "code_http": code,
        }

        if code != 200:  # if not success
            if code == 404:  # may be not found, get kdniao's json data or other
                try:
                    resp.update(json.loads(body))
                except ValueError:
                    resp["_msg"] = "API Not Found: %s " % url
            elif code == 599:
                resp["_msg"] = "HTTP Timeout"
            else:
                resp["_msg"] = "API ERROR: %s" % code
        else:
            resp.update(json.loads(body))
        return resp

    def _parse_api_resp(self, data):
        """
        parse resp data
        :param dict data:
        :return:
        """
        api_ecode = APIErrorCode.Success
        biz_ecode = BizRespCode.Success

        http_code = data["code_http"]

        msg = "Success"

        # API Error
        if http_code != 200:
            api_ecode = APIErrorCode.Failed
            biz_ecode = BizRespCode.Failed
            msg = data.pop("_msg", "Unknow Error")

        data_keys = list(data.keys())
        data_keys.remove("code_http")
        if data_keys == 1 and data_keys[0] == "Message":
            api_ecode = APIErrorCode.Failed
            biz_ecode = BizRespCode.Failed
            msg = data["Message"]

        # Biz Error
        if "Reason" in data:
            msg = data["Reason"]
        if "Success" in data:
            biz_ecode = {True: BizRespCode.Success, False: BizRespCode.Failed}[data["Success"]]

        res = {
            "code_api": api_ecode,
            "code_biz": biz_ecode,
            "code_http": data.pop("code_http"),
            "msg": msg,
            "data": data
        }

        return res


class KdNiaoAsyncClient(KdNiaoClient):
    """
    Non-Blocking Client
    """

    def __init__(self, app_id, app_key, is_prod=True):
        """
        init
        :param int app_id: app id
        :param str app_key: app key
        :param bool is_prod: env type, prod or test, default is True
        """
        super(KdNiaoAsyncClient, self).__init__(app_id, app_key, is_prod=is_prod)

    @tornado.gen.coroutine
    def _request(self, rtype, data, **kwargs):
        """
        prepare and send request
        :param str rtype:
        :param data:
        :param timeout:
        :return:
        """
        timeout = kwargs.get("timeout")
        timeout = self._parese_time_out(timeout)

        callback = kwargs.get("callback")

        url = self._gen_api_url(rtype)
        rdata = self._prepare_req_params(rtype, data)

        res = yield self._post(url, rdata, timeout, callback)
        resp = self._parse_http_resp(res.code, res.reason, res.body, res.request.url)
        res = self._parse_api_resp(resp)

        raise tornado.gen.Return(res)

    @classmethod
    @tornado.gen.coroutine
    def _post(cls, url, data, timeout=(10, 10), callback=None):
        """
        :param str url: URL
        :param dict data: request parms
        :param tuple timeout: tuple or an int object
        :param function callback: callback function
        :return:
        """
        _timeout = {
            "connect_timeout": timeout[0],
            "request_timeout": timeout[1],
        }

        if isinstance(data, dict):
            data = urlencode(data)
        req = HTTPRequest(url, "POST", HEADERS, utf8(data), **_timeout)
        resp = yield AsyncHTTPClient().fetch(req, callback, raise_error=False)
        raise tornado.gen.Return(resp)


__all__ = ["KdNiaoClient", "KdNiaoAsyncClient"]
