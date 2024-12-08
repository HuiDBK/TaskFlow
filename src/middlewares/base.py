#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/07/11 12:17
import time
from http import HTTPStatus

from fastapi import Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from py_tools.enums.error import BaseErrCode
from py_tools.logging import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse

from src import settings
from src.dao.orm.managers import UserManager
from src.enums import BizErrCodeEnum
from src.services.user.user_service import UserService
from src.utils import TraceUtil, context_util, web


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    日志中间件
    记录请求参数信息、计算响应时间
    """

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.perf_counter()

        # 打印请求信息
        logger.info(f"--> {request.method} {request.url.path} {request.client.host}")
        if request.query_params:
            logger.info(f"--> Query Params: {request.query_params}")

        if "application/json" in request.headers.get("Content-Type", ""):
            await self.set_body(request)
            try:
                # starlette 中间件中不能读取请求数据，否则会进入循环等待 需要特殊处理或者换APIRoute实现
                body = await request.json()
                logger.info(f"--> Body: {body}")
            except Exception as e:
                logger.warning(f"Failed to parse JSON body: {e}")

        # 执行请求获取响应
        response = await call_next(request)

        # 计算响应时间
        process_time = time.perf_counter() - start_time
        response.headers["X-Response-Time"] = f"{process_time:.2f}s"
        logger.info(f"<-- {response.status_code} {request.url.path} (took: {process_time:.2f}s)\n")

        return response


class TraceReqMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # 设置请求id
        request_id = TraceUtil.set_req_id(request.headers.get("X-Request-ID"))
        response = await call_next(request)
        response.headers["X-Request-ID"] = f"{request_id}"  # 记录同一个请求的唯一id
        return response


class AuthMiddleware(BaseHTTPMiddleware):
    """鉴权中间件"""

    @staticmethod
    def set_auth_err_resp(err_code: BaseErrCode = BizErrCodeEnum.AUTH_ERR):
        return JSONResponse(status_code=HTTPStatus.OK, content=web.fail_api_resp_with_err_enum(err_code))

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.url.path.startswith(settings.auth_whitelist_urls):
            # 白名单路由，直接放行
            return await call_next(request)

        # 其他路由，进行鉴权
        token = request.headers.get("Authorization") or ""
        token = token.replace("Bearer ", "")
        logger.info(f"UserToken: {token}")

        # oauth2.0 token 鉴权
        oauth_token = request.cookies.get("oauth_token")
        logger.info(f"OAuthToken: {oauth_token}")
        token = token or oauth_token

        if not token:
            return self.set_auth_err_resp()

        # 验证token
        user_info = UserService().verify_user_token(token)
        if not user_info:
            return self.set_auth_err_resp()

        # 保存用户信息到上下文中
        user_id = user_info["user_id"]
        user = await UserManager().query_by_id(user_id)
        if not user:
            return self.set_auth_err_resp(err_code=BizErrCodeEnum.FORBIDDEN_ERR)
        context_util.USER_CTX.set(user)

        response = await call_next(request)
        return response


class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    """全局异常处理中间件"""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.exception(f"Global unhandled exception: {e}")
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content=web.fail_api_resp_with_err_enum(BizErrCodeEnum.SYSTEM_ERR),
            )


def register_middlewares():
    """注册中间件（逆序执行）"""
    return [
        # Middleware(LoggingMiddleware),
        Middleware(
            CORSMiddleware,
            allow_origins=settings.allow_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(TraceReqMiddleware),
        Middleware(AuthMiddleware),
        Middleware(GlobalExceptionMiddleware),
    ]
