#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户模块 }
# @Date: 2023/08/30 17:36
from src.data_models.api_models import user
from src.data_models.api_models.base import SuccessResp
from fastapi import Query


class UserDetailControllers:
    """ 用户详情信息路由处理 """

    @classmethod
    async def detail(cls):
        return SuccessResp(data={"username": username})
