#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 10:59
from fastapi import APIRouter

from src.routers import common, project, task, user

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user.router, prefix="/user", tags=["用户模块"])
api_router.include_router(project.router, prefix="/project", tags=["项目模块"])
api_router.include_router(task.router, prefix="/task", tags=["任务模块"])
api_router.include_router(common.router, prefix="/common", tags=["公共模块"])
# api_router.include_router(user.router, prefix="user", tags=["用户模块"])
