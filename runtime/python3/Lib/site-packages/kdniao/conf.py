#!/usr/bin/env python
# coding=utf-8
"""
API 相关配置
"""
from kdniao.mdutils import urljoin


class KdNiaoConfig(object):
    DEFAULT_TIMEOUT = (10, 10)  # seconds


HEADERS = {
    "Accept": "application/x-www-form-urlencoded;charset=utf-8",
    "Accept-Encoding": "utf-8",
}


class APIPath(object):
    """
    api  path
    """
    OrderCreate = "/api/oorderservice"  # 预约取件接口 1001
    EOrderService = "/api/EOrderService"  # 电子面单 1007
    EbusinessOrderHandle = "/Ebusiness/EbusinessOrderHandle.aspx"  # 物流轨迹（即时查询）1002,  单号识别 2002
    DIST = "/api/dist"  # 物流轨迹（订阅查询） 1008
    ExRecommend = "/api/dist"  # 智选物流 2001
    SafeNumber = "/api/apiservice"  # 安全号码接口 3001,
    UserReg = "/api/reg"  # 用户注册 9001,
    Agency = "/api/agencyfund"  # 代理商接口
    UserUpdate = "/api/agencyfund"  # 更新用户 cmd1002,
    UserGet = "/api/agencyfund"  # 更新用户 cmd1003,


# 指令类型与 API 网址映射
RequestTypeAPIPathMap = {
    "1001": APIPath.OrderCreate,  # 预约取件接口 1001
    "1002": APIPath.EbusinessOrderHandle,  # 物流轨迹（即时查询）1002
    "1007": APIPath.EOrderService,  # 电子面单 1007
    "1008": APIPath.DIST,  # 物流轨迹（订阅查询） 1008
    "2001": APIPath.EbusinessOrderHandle,  # 智选物流 2001
    "2002": APIPath.EbusinessOrderHandle,  # 单号识别 2002
    "8001": APIPath.EbusinessOrderHandle,  # 在途监控 8001
    "8008": APIPath.ExRecommend,  # 订阅(增值版)接口 8008
    "3001": APIPath.SafeNumber,  # 安全号码接口 3001,
    "9001": APIPath.UserReg,  # 用户注册 9001,
    "cmd1002": APIPath.UserUpdate,  # 更新用户 CMD1002,
    "cmd1003": APIPath.UserGet,  # 查询用户信息 cmd1003,
    "cmd1004": APIPath.Agency,  # 垫付业务申请CMD1004
    "cmd1005": APIPath.Agency,  # 直退业务申请CMD1005
    "cmd1006": APIPath.Agency,  # 普通代收货款申请CMD1006
    "cmd1007": APIPath.Agency,  # 查询服务申请状态CMD1007,
    "cmd1008": APIPath.Agency,  # 查询返款银行信息CMD1008
    "cmd1009": APIPath.Agency,  # 提交返款银行信息CMD1009
    "cmd1010": APIPath.Agency,  # 获取订单货款状态CMD1010
}

# 部分接口的API 网址，生产环境和测试环境是一样的
RequestTypeUsingProdHost = {
    "1002",  # 即时查询
    "8001",  # 在途监控
}


class APIErrorCode(object):
    """
    API Reuqest Error Code
    """
    Success = 0
    Failed = 0


class BizRespCode(object):
    """
    Biz Response Code
    """
    Success = 100
    Failed = -100


# 生产与测试环境相关配置
class APIPathBuilder(object):
    """
    env type
    """
    PROD = "api.kdniao.cc"
    TEST = "testapi.kdniao.cc:8081"

    @classmethod
    def env_list(cls):
        """
        env type list
        """
        return ["prod", "test"]

    @classmethod
    def get_host(cls, env_type):
        """
        get host by env type
        :param env_type:
        :return:
        """
        assert env_type in cls.env_list()
        return getattr(cls, env_type.upper())

    @classmethod
    def gen_api_url(cls, env_type, req_type):
        """
        gen api url by env type and req type
        :param str env_type:
        :param str req_type:
        :return:
        """
        if req_type in RequestTypeUsingProdHost:
            env_type = "prod"

        host = cls.get_host(env_type)
        api_prefix = "http://%s" % host

        api_path = RequestTypeAPIPathMap[req_type]
        url = urljoin(api_prefix, api_path)

        return url
