#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/06 16:49
from src.enums import ErrorCodeEnum


def success_api_resp(data=None):
    """成功的响应"""
    data = data or {}
    resp_content = {"code": ErrorCodeEnum.OK.value, "message": ErrorCodeEnum.OK.desc, "data": data or {}}
    return resp_content


def fail_api_resp_with_err_enum(err_enum: ErrorCodeEnum, err_msg: str = None, data=None):
    """失败的响应携带错误码"""
    resp_content = {
        "code": err_enum.value,
        "message": err_msg or err_enum.desc,
        "data": data or {},
    }
    return resp_content


def fail_api_resp(err_msg: str = None, data=None):
    """失败的响应 默认Failed错误码"""
    resp_content = {
        "code": ErrorCodeEnum.FAILED.value,
        "message": err_msg or ErrorCodeEnum.FAILED.desc,
        "data": data or {},
    }
    return resp_content
