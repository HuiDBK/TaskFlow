#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:05
from src.data_models.api_models import user
from src.data_models.api_models.base import SuccessRespModel


class UserRegisterControllers:
    """用户登录注册路由处理"""

    @classmethod
    async def login(cls, req_model: user.UserLoginIn):
        # 参数校验

        # 业务逻辑处理

        # 响应返参
        return SuccessRespModel(data=req_model.dict())

    @classmethod
    async def register(cls, req_model: user.UserRegisterIn):
        print(req_model)
        return SuccessRespModel(data=req_model.dict())
