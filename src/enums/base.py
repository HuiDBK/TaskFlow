#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 公共模型 }
# @Date: 2023/08/29 14:28
from py_tools.enums.error import BaseErrCode, BaseErrCodeEnum


class BizErrCodeEnum(BaseErrCodeEnum):
    """
    错误码前缀
     - 000-通用基础错误码前缀
     - 100-待定
     - 200-通用业务错误码前缀
        eg:
        - 201-用户模块
        - 202-订单模块
     - 300-待定
     - 400-通用请求错误
     - 500-通用系统错误码前缀
    """

    # 用户模块
    USER_PWD_ERR = BaseErrCode("201-0001", "账号或密码错误")
