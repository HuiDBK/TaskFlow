#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 上下文模块描述 }
# @Date: 2023/10/30 15:11
import contextvars
from typing import Union

from fastapi import Request

from src.dao.orm.tables import UserTable

# 请求对象上下文
REQUEST_CTX: contextvars.ContextVar[Union[Request, None]] = contextvars.ContextVar("request", default=None)

# 用户对象上下文
USER_CTX: contextvars.ContextVar[Union[UserTable, None]] = contextvars.ContextVar("user", default=None)

# 请求唯一id
REQUEST_ID: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="")

# 任务追踪唯一id
TRACE_ID: contextvars.ContextVar[str] = contextvars.ContextVar("trace_id", default="")


class ContextMixin:
    @classmethod
    def current_user(cls):
        return USER_CTX.get()

    @classmethod
    def current_request(cls):
        return REQUEST_CTX.get()
