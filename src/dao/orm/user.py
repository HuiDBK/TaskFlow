#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户数据表模型 }
# @Date: 2023/08/29 16:56
from pydantic import fields


# (BaseOrmModel)
class UserModel(None):
    """用户表"""
    username = fields.CharField(max_length=20, description="用户昵称")
    password = fields.CharField(max_length=20, description="用户密码")
    phone = fields.IntField(length=11,description="手机号")
    email= fields.EmailField(description="邮箱")

    class Meta:
        table = "user"
