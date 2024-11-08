#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 10:59
from src.routers import common, project, task, user
from src.routers.base import BaseAPIRouter

api_router = BaseAPIRouter(prefix="/api")

api_router.include_router(user.router, tags=["用户模块"])
api_router.include_router(project.router, tags=["项目模块"])
api_router.include_router(task.router, tags=["任务模块"])
api_router.include_router(common.router, tags=["公共模块"])
# api_router.include_router(user.router, prefix="user", tags=["用户模块"])
