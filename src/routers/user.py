#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/29 12:15
from src.controllers.manage import user
from src.server import app
@app.post(path="/api/v1/login")
async def user_login():
    return {}


routes = [
    (r"/api/v1/register", user.UserRegisterControllers),
]
