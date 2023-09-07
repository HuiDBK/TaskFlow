#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/07/10 16:41
from http import HTTPStatus

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from py_tools.exceptions.base import BusinessException
from py_tools.logging import logger

from src.enums import ErrorCodeEnum
from src.utils import web


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """全局捕捉参数验证异常"""

    # 格式化参数校验错误信息
    message = ".".join([f'{".".join(map(lambda x: str(x), error.get("loc")))}:{error.get("msg")};' for error in exc.errors()])
    error_tip = f"参数校验错误 {message}"
    logger.error(error_tip)

    error_detail = {"error_detail": exc.errors()}

    return JSONResponse(
        status_code=HTTPStatus.OK,  # 200
        content=web.fail_api_resp_with_err_enum(ErrorCodeEnum.PARAM_ERR, error_tip, error_detail),
    )


async def global_exception_handler(request: Request, exc: Exception):
    """全局系统异常处理器"""

    if isinstance(exc, ConnectionError):
        message = f"网络异常, {exc}"
        err_enum = ErrorCodeEnum.SOCKET_ERR
    else:
        message = f"系统异常, {exc}"
        err_enum = ErrorCodeEnum.SYSTEM_ERR

    logger.error(f"global_exception_handler {message}")
    return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=web.fail_api_resp_with_err_enum(err_enum))  # 500


def biz_error_handler(request: Request, exc: BusinessException):
    """业务错误处理"""
    logger.error(f"biz_error_handler {exc}")
    return JSONResponse(status_code=HTTPStatus.OK, content=web.fail_api_resp(exc.msg))


def register_exception_handler():
    """注册异常处理器"""
    return {
        RequestValidationError: validation_exception_handler,  # 请求参数校验错误处理
        BusinessException: biz_error_handler,  # 业务错误处理
        Exception: global_exception_handler,  # 全局未捕获的异常处理
    }
