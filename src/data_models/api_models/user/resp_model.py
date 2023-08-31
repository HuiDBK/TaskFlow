#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:26
from pydantic import BaseModel, Field

from src.data_models.api_models.base import BaseRespModel


# 用户详情
class UserDetailItem(BaseModel):
    id: int = Field(description="用户唯一标识id")
    username: str = Field(description="用户昵称")
    email: str = Field(description="用户邮箱")
    phone: int = Field(description="手机号")


class UserDetailOut(BaseRespModel):
    """ 用户详情出参 """

    data: UserDetailItem = Field(description="用户详情信息")
