#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:05
from src.controllers.base import BaseController
from src.data_models.api_models import user
from src.data_models.api_models.base.resp_model import TokenRespModel
from src.services.user.user_service import UserService


class UserRegisterController(BaseController):
    """用户登录注册路由处理"""

    @classmethod
    async def login(cls, req_model: user.UserLoginIn):
        # 业务逻辑处理
        token = await UserService().login(req_model)

        # 响应返参
        return TokenRespModel(token=token)

    @classmethod
    async def register(cls, req_model: user.UserRegisterIn):
        token = await UserService().register(req_model)
        return TokenRespModel(token=token)
