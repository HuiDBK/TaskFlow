#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: auth.py
# @Desc: { 鉴权回调路由模块 }
# @Date: 2024/12/07 16:05
from src.controllers.auth.callback import AuthCallback
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()


router.add_api_route(
    path="/v1/auth/github/callback",
    endpoint=AuthCallback.github_callback,
    methods=["GET"],
    summary="Github callback",
)
