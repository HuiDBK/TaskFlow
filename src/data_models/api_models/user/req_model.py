#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:26


from pydantic import BaseModel, Field, EmailStr


class UserRegisterIn(BaseModel):
    """用户注册入参"""
    username: str = Field(..., description="用户昵称")
    email: EmailStr = Field(..., description="邮箱")
    password: str = Field(..., description="用户密码")
    phone: int = Field(..., description="手机号")


class UserLoginIn(BaseModel):
    username: str = Field(..., description="用户昵称")
    # 我们也得拿到用户密码 用密码去数据库比对，用户输入了正确的密码才能正常登录
    password: str = Field(..., description="用户密码")
