#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户模块 }
# @Date: 2023/08/30 17:36
from fastapi import Query

from src.data_models.api_models import user
from src.data_models.api_models.base import SuccessRespModel


class UserDetailControllers:
    """用户详情信息路由处理"""

    @classmethod
    async def detail(cls):
        return SuccessRespModel()
