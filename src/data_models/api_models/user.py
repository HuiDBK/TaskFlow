#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户模块参数校验 }
# @Date: 2023/08/29 15:45
from pydantic import BaseModel, Field, EmailStr


class UserRegisterCreateIn(BaseModel):
    """用户注册参数校验"""
    username: str = Field(...,description="用户昵称")
    email: EmailStr = Field(..., description="邮箱")
    password: str = Field(...,description="用户密码")
    phone: int =Field(...,description="手机号")


class UserLoginQueryIn(BaseModel):

    username: str = Field(..., description="用户昵称")
    # 我们也得拿到用户密码 用密码去数据库比对，用户输入了正确的密码才能正常登录
    password: str = Field(..., description="用户密码")

