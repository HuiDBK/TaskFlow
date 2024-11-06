#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/07/11 12:17
import time

from fastapi import Request
from fastapi.middleware import Middleware
from fastapi.responses import Response
from py_tools.logging import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.utils import TraceUtil


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
        # 设置请求id
        request_id = TraceUtil.set_req_id()

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
        response.headers["X-Request-ID"] = f"{request_id}"  # 记录同一个请求的唯一id
        logger.info(f"<-- {response.status_code} {request.url.path} (took: {process_time:.2f}s)\n")

        return response


class TraceReqMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # 设置请求id
        request_id = TraceUtil.set_req_id(request.headers.get("X-Request-ID"))
        response = await call_next(request)
        response.headers["X-Request-ID"] = f"{request_id}"  # 记录同一个请求的唯一id
        return response


def register_middlewares():
    """注册中间件"""
    return [
        # Middleware(LoggingMiddleware),
        Middleware(TraceReqMiddleware),
    ]
