#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/29 12:15
from src.server import app

@app.post(path="/api/v1/login")
async def user_login():
    return {}


@app.post(path="/api/v1/register")
async def user_register():
    return {}
