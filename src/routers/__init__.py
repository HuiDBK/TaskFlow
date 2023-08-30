#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 10:59
from fastapi import APIRouter

from src.routers import user

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user.router, prefix="/user", tags=["用户模块"])
# api_router.include_router(user.router, prefix="user", tags=["用户模块"])
# api_router.include_router(user.router, prefix="user", tags=["用户模块"])
# api_router.include_router(user.router, prefix="user", tags=["用户模块"])