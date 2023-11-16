#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 路由中间件 }
# @Date: 2023/11/16 13:38
import time
from typing import Callable

from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.routing import APIRoute
from py_tools.logging import logger


class LoggingAPIRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def log_route_handler(request: Request) -> Response:
            """日志记录请求信息与处理耗时"""
            start_time = time.perf_counter()
            log_info = f"\n--> {request.method} {request.url.path} {request.client.host}:{request.client.port}\n"
            if request.query_params:
                log_info += f"--> Query Params: {request.query_params}\n"

            if "application/json" in request.headers.get("Content-Type", ""):
                try:
                    json_body = await request.json()
                    log_info += f"--> json_body: {json_body}\n"
                except Exception:
                    logger.exception("Failed to parse JSON body")

            response: Response = await original_route_handler(request)
            process_time = time.perf_counter() - start_time
            response.headers["X-Response-Time"] = str(process_time)
            log_info += f"<-- {response.status_code} {request.url.path} (took: {process_time:.2f}s)"
            logger.info(log_info)
            return response

        return log_route_handler
