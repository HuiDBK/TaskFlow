#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/29 12:15
from src.controllers.user import UserDetailControllers, UserRegisterControllers
from src.data_models.api_models import base_api, user_api
from src.routers.base import APIRouter

router = APIRouter()

router.add_api_route(
    path="/login",
    endpoint=UserRegisterControllers.login,
    response_model=base_api.SuccessRespModel,
    methods=["POST"],
    summary="用户登录",
)

router.add_api_route(
    path="/register",
    endpoint=UserRegisterControllers.register,
    response_model=base_api.SuccessRespModel,
    methods=["POST"],
    summary="用户注册",
)

router.add_api_route(
    path="/detail",
    endpoint=UserDetailControllers.detail,
    response_model=user_api.UserDetailOut,
    methods=["GET"],
    summary="用户详情",
)
