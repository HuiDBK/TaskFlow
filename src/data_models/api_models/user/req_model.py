#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:26
from typing import Optional

from py_tools.utils import RegexUtil
from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRegisterIn(BaseModel):
    """用户注册入参"""

    username: str = Field(..., min_length=1, max_length=10, description="用户昵称")
    password: str = Field(..., min_length=6, max_length=12, description="用户密码")
    email: Optional[EmailStr] = Field(default=None, description="邮箱")
    phone: Optional[str] = Field(default=None, min_length=11, description="手机号")
    github_uid: Optional[int] = Field(default=0, description="github uid")

    @field_validator("phone")
    def validate_phone(cls, phone: str):
        """手机号校验"""
        if not RegexUtil.find_chinese_phone_numbers(phone):
            raise ValueError("手机号格式不正确")
        return phone


class UserLoginIn(BaseModel):
    account: str = Field(..., min_length=1, max_length=20, description="用户账号（用户名/手机号/邮箱）")
    password: str = Field(..., min_length=6, max_length=12, description="用户密码")
