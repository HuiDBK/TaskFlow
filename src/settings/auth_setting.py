#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: auth_setting.py
# @Desc: { 模块描述 }
# @Date: 2024/11/11 14:44
import datetime

# 鉴权白名单路由
auth_whitelist_urls = (
    "/docs",
    "/redoc",
    "/openapi",
    "/api/ping",
    "/api/v1/users/login",
    "/api/v1/users/register",
    "/api/v1/auth/github/callback",
)

auth_secret_key = "hasjdhaxbxasadjaklkj"
auth_algorithm = "HS256"
auth_expires_delta = datetime.timedelta(hours=6)


github_client_id = "your_github_client_id"
github_client_secret = "your_github_client_secret"
