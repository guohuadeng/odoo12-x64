#!/usr/bin/env python
# coding=utf-8
"""
API 封装
"""
import json
import hashlib
import base64
from kdniao.mdutils import utf8
from kdniao.conf import APIPathBuilder


class ClientMixin(object):
    """
    client mixin
    """

    def __init__(self, client):
        """
        :param client:
        """
        self._client = client
        self._name = type(self).__name__.lower()

    def _send(self, req_type, data, **kwargs):
        """
        :param str req_type: 指令类型
        :param dict data: 数据
        :param dict kwargs: 其他参数，如 timeout=(10, 10)
        :return:
        """
        return self._client._request(req_type, data, **kwargs)


class API(object):
    """
    API Wrapper for http://www.kdniao.com/api-all
    """
    REQ_TYPE = None

    def __init__(self, app_id, app_key, env_type="prod"):
        """
        init
        :param int app_id: app id
        :param str app_key: app key
        :param str env_type: env type, prod or test, default is prod
        """

        # config
        self._app_id = app_id
        self._app_key = app_key
        self._env_type = env_type

        # API group exported API 分组
        self.api_track = APITrack(self)
        self.api_follow = APIFollow(self)
        self.api_recognise = APIRecognise(self)
        self.api_eorder = APIEOrder(self)
        self.api_order = APIOrder(self)
        self.api_monitor = APIMonitor(self)
        self.api_user = APIUser(self)
        self.api_collect = APICollectionMoney(self)

        # Method exported 常用接口导出
        self.track = self.api_track.track
        self.recognise = self.api_recognise.recognise
        self.follow = self.api_follow.follow
        self.create_eorder = self.api_eorder.create

    @classmethod
    def __sign(cls, data, app_key):
        """
        sign
        b64(md5(REQUEST_DATA))
        """
        m = hashlib.md5()
        s = utf8(data + app_key)
        m.update(s)
        digest = utf8(m.hexdigest())
        b64_str = base64.b64encode(digest)
        return b64_str

    def _prepare_req_params(self, req_type, data):
        """
        :param str req_type:
        :param dict data:
        :return:
        """
        json_data = json.dumps(data, sort_keys=True)
        sign = self.__sign(json_data, self._app_key)
        req_params = {
            "RequestData": json_data,
            "EBusinessID": self._app_id,
            "RequestType": req_type,  # "1002"
            "DataSign": sign,
            "DataType": 2,
        }
        return req_params

    def valid_sign(self, sign, data):
        """
        :param str sign: 签名
        :param str data: 数据
        :return bool:
        """
        return sign == self.__sign(data, self._app_key)

    def _gen_api_url(self, req_type):
        """
        generate api url
        :param tr req_type: request type
        :return str: url
        """
        return APIPathBuilder.gen_api_url(self._env_type, req_type)


class APITrack(ClientMixin):
    """
    即时查询 路由查询 轨迹跟踪
    http://www.kdniao.com/api-track
    """

    def track(self, logistic_code, shipper_code, order_code="", **kwargs):
        """
        即时查询 路由查询 轨迹跟踪
        :param str logistic_code: 运单编号
        :param str shipper_code: 物流公司编号
        :param str order_code: 订单编号
        :return dict:
        """
        rtype = "1002"
        params = {
            "LogisticCode": logistic_code,
            "ShipperCode": shipper_code,
            "OrderCode": order_code,
        }
        return self._send(rtype, params, **kwargs)


class APIFollow(ClientMixin):
    """
    物流跟踪 http://www.kdniao.com/api-follow
    """

    def follow(self, logistic_code, shipper_code, params=None, **kwargs):
        """
        物流跟踪
        :param str logistic_code: 运单编号
        :param str shipper_code: 物流公司编号
        :param dict params: 其他选填参数，见 http://www.kdniao.com/api-follow 二、接口参数 订阅接口 请求内容字段定义：
        :return dict:
        """
        rtype = "1008"
        params = params or {}
        params.update(
            {"LogisticCode": logistic_code,
             "ShipperCode": shipper_code}
        )
        return self._send(rtype, params, **kwargs)


class APIEOrder(ClientMixin):
    """
    电子面单 http://www.kdniao.com/api-eorder
    """

    def create(self, params, **kwargs):
        """
        电子面单下单
        :param dict params: 下单参数
        :param dict kwargs: 其他可选参数
        :return:
        """
        rtype = "1007"
        return self._send(rtype, params, **kwargs)


class APIOrder(ClientMixin):
    """
    预约取件接口 http://www.kdniao.com/api-order
    """

    def create(self, params, **kwargs):
        """
        预约取件
        :param params:
        :param kwargs:
        :return:
        """
        rtype = "1001"
        return self._send(rtype, params, **kwargs)

    def cancle(self, logistic_code, shipper_code, order_code, **kwargs):
        """
        取消订单
        :param str logistic_code: 运单编号
        :param str shipper_code: 物流公司编号
        :param str order_code: 订单编号
        :return dict:
        """
        rtype = "1004"
        params = {
            "LogisticCode": logistic_code,
            "ShipperCode": shipper_code,
            "OrderCode": order_code,
        }
        return self._send(rtype, params, **kwargs)


class APIRecognise(ClientMixin):
    """
    单号识别 http://www.kdniao.com/api-recognise
    """

    def recognise(self, logistic_code, **kwargs):
        """
        单号识别 http://www.kdniao.com/api-recognise
        :return:
        """
        rtype = "2002"
        params = {
            "LogisticCode": logistic_code,
        }
        return self._send(rtype, params, **kwargs)


class APIMonitor(ClientMixin):
    """
    在途监控 http://www.kdniao.com/api-monitor
    """

    def track(self, logistic_code, shipper_code, order_code, **kwargs):
        """
        即时查询(增值版)接口 http://www.kdniao.com/api-monitor
        :param str logistic_code: 运单编号
        :param str shipper_code: 物流公司编号
        :param str order_code: 订单编号
        :return dict:
        """
        rtype = "8001"
        params = {
            "LogisticCode": logistic_code,
            "ShipperCode": shipper_code,
            "OrderCode": order_code,
        }
        return self._send(rtype, params, **kwargs)

    def subscribe(self, params, **kwargs):
        """
        订阅(增值版)接口 http://www.kdniao.com/api-monitor
        :return:
        """
        rtype = "8008"
        return self._send(rtype, params, **kwargs)


class APISafeMail(ClientMixin):
    """
    隐私快递 http://www.kdniao.com/api-safemail
    """

    def safe_number(self, params, **kwargs):
        """
        安全号码 http://www.kdniao.com/api-safemail
        :param dict params: 接口请求参数
        :param dict kwargs: 其他参数
        :return dict:
        """
        rtype = "3001"
        return self._send(rtype, params, **kwargs)

    def safe_order(self, params, **kwargs):
        """
        隐私电子面单 http://www.kdniao.com/api-safemail
        :param dict params: 接口请求参数
        :param dict kwargs: 其他参数
        :return:
        """
        rtype = "1007"
        return self._send(rtype, params, **kwargs)


class APIUser(ClientMixin):
    """
    用户类
    """

    def reg(self, data, **kwargs):
        """
        注册用户
        :param data:
        :param kwargs:
        :return:
        """
        rtype = "9001"
        return self._send(rtype, data, **kwargs)

    def update(self, params, **kwargs):
        """
        更新用户信息
        详细参数见 http://www.kdniao.com/CollectionMoneyAPI.aspx 1.2.6 JSON请求示例
        :return:
        """
        rtype = "cmd1002"
        return self._send(rtype, params, **kwargs)

    def get(self, **kwargs):
        """
        获取用户信息
        :param kwargs:
        :return:
        """
        rtype = "cmd1003"
        return self._send(rtype, {}, **kwargs)


class APICollectionMoney(ClientMixin):
    """
    代收货款
    """

    def submit_bank(self, params, **kwargs):
        """
        提交返款银行信息 - CMD1009。设置用户代收货款订单的银行返款信息。
        :param dict params: 接口参数， 如：{
                                "BankType": "0",
                                "BankAccountNo": "62266226622662266226",
                                "BankAccountName": "hoo",
                                "BankName": "招商银行",
                                "BankBranch": "",
                                "BankCardPicA": "",
                                "BankCardPicB": ""
                            }
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1009"
        return self._send(rtype, params, **kwargs)

    def get_order_bank(self, bank_type, **kwargs):
        """
        查询代收货款订单的银行返款信息 - CMD1008。
        :param str bank_type: 信息类型：0-直退，1-垫付
        :return:
        """
        rtype = "CMD1008"
        params = {
            "BankType": bank_type
        }
        return self._send(rtype, params, **kwargs)

    def get_credit(self, services_code, **kwargs):
        """
        查询用户额度 CMD1014 - 查询用户的代收货款的额度限制和当前可用额度。
        :param str services_code: 服务代码：普通代收货款 COD，货款直退 CODBACK，货款垫付 CODPAY 网点速退 CODFAST
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1014"
        params = {
            "ServicesCode": services_code
        }
        return self._send(rtype, params, **kwargs)

    def request_advance(self, params, **kwargs):
        """
        垫付业务申请 CMD1004
        :param dict params: 接口参数，如: {
                                            "BankAccountNo": "62266226622662266226",
                                            "BankAccountName": "hoo",
                                            "BankName": "招商银行",
                                            "BankBranch": "深圳深圳支行",
                                            "BankCardPicA": "",
                                            "BankCardPicB": ""
                                        }
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1004"
        return self._send(rtype, params, **kwargs)

    def request_direct_refund(self, params, **kwargs):
        """
        直退业务申请 CMD1005 - 申请直退业务的权限。
        :param dict params: 接口参数，如: {
                                            "BankAccountNo": "62266226622662266226",
                                            "BankAccountName": "hoo",
                                            "BankName": "招商银行",
                                            "BankBranch": "深圳深圳支行",
                                            "BankCardPicA": "",
                                            "BankCardPicB": ""
                                        }
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1005"
        return self._send(rtype, params, **kwargs)

    def request_normal_ollection(self, **kwargs):
        """
        普通代收货款申请 CMD1006 - 申请普通代收货款业务的权限。
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1006"
        return self._send(rtype, {}, **kwargs)

    def get_srv_status(self, services_code, **kwargs):
        """
        查询服务申请状态 CMD1007 - 查询某用户的服务开通情况。
        :param str services_code: 服务代码：普通代收货款 COD，货款直退 CODBACK，货款垫付 CODPAY 网点速退 CODFAST
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1007"
        params = {
            "ServicesCode": services_code
        }
        return self._send(rtype, params, **kwargs)

    def get_payment_status(self, params, **kwargs):
        """
        获取订单货款状态 CMD1010 - 获取订单货款状态。
        :param dict params: 接口参数，如: {
                                            "OrderNos": "",
                                            "BeginTime": "",
                                            "EndTime": "",
                                            "PageIndex": "1",
                                            "PageSize": "10"
                                        }
        :param dict kwargs:
        :return:
        """
        rtype = "CMD1010"
        return self._send(rtype, params, **kwargs)
