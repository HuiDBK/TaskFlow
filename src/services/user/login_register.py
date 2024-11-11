#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: login_register.py
# @Desc: { 登陆注册模块 }
# @Date: 2024/11/11 15:12

from py_tools.exceptions import BizException
from py_tools.logging import logger
from py_tools.utils import JWTUtil

from src.dao.orm.managers import UserManager
from src.data_models.api_models.user import UserLoginIn, UserRegisterIn
from src.enums import BizErrCodeEnum
from src.services.base import BaseService


class UserLoginRegisterService(BaseService):
    async def login(self, login_info: UserLoginIn):
        user = await UserManager().user_login(login_info.account, login_info.password)
        if not user:
            raise BizException(err_code=BizErrCodeEnum.USER_PWD_ERR)

        token = await self.gen_user_token(user_id=user.id, username=user.username)
        logger.info(f"login success, user: {user}")
        return token

    async def gen_user_token(self, user_id: int, username: str) -> str:
        user_info = {"user_id": user_id, "username": username}
        jwt_util = JWTUtil(secret_key=self.auth_settings.auth_secret_key, algorithm=self.auth_settings.auth_algorithm)
        token = jwt_util.generate_token(data=user_info, expires_delta=self.auth_settings.auth_expires_delta)
        return token

    async def register(self, register_info: UserRegisterIn) -> str:
        """用户注册"""
        # save to db
        user_info = register_info.model_dump(exclude_none=True)
        user_id = await UserManager().add(user_info)

        # gen jwt
        user_info.pop("password", None)
        user_info["user_id"] = user_id
        token = await self.gen_user_token(user_id=user_id, username=register_info.username)
        logger.info(f"register success, user: {register_info}")
        return token
