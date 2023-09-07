#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 公共模型 }
# @Date: 2023/08/29 14:28
from py_tools.enums.base import BaseEnum


class ErrorCodeEnum(BaseEnum):
    """错误码枚举类"""

    OK = (0, "SUCCESS")
    FAILED = (-1, "FAILED")

    AUTHORIZATION_ERR = (4001, "权限认证错误")

    SOCKET_ERR = (5000, "网络异常")
    SYSTEM_ERR = (5001, "系统异常")
    PARAM_ERR = (5002, "参数错误")
