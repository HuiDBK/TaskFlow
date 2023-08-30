#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/29 12:15
from fastapi import APIRouter
from src.controllers.user import UserRegisterControllers
from src.data_models.api_models.base import SuccessResp

router = APIRouter()

router.add_api_route(
    path="/login",
    endpoint=UserRegisterControllers.login,
    response_model=SuccessResp,
    methods=["POST"],
    summary="用户登录"
)

router.add_api_route(
    path="/register",
    endpoint=UserRegisterControllers.register,
    response_model=SuccessResp,
    methods=["POST"],
    summary="用户注册"
)
