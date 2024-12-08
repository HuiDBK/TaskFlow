#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/29 12:15
from src.controllers.user import UserDetailControllers, UserRegisterController
from src.data_models.api_models import base_api, user_api
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()

router.add_api_route(
    path="/v1/users/login",
    endpoint=UserRegisterController.login,
    response_model=base_api.TokenRespModel,
    methods=["POST"],
    summary="用户登录",
)

router.add_api_route(
    path="/v1/users/register",
    endpoint=UserRegisterController.register,
    response_model=base_api.TokenRespModel,
    methods=["POST"],
    summary="用户注册",
)

router.add_api_route(
    path="/v1/users/detail",
    endpoint=UserDetailControllers.detail,
    response_model=user_api.UserDetailOut,
    methods=["GET"],
    summary="用户详情",
)
