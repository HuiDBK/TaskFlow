#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/11/16 14:10
import fastapi

from src.middlewares.api_route import LoggingAPIRoute


class APIRouter(fastapi.APIRouter):
    def __init__(self, *args, api_log=True, **kwargs):
        super().__init__(*args, **kwargs)
        if api_log:
            # 开启api请求日志信息
            self.route_class = LoggingAPIRoute
