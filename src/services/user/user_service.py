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
from src.dao.orm.managers.project_manager import ProjectManager
from src.data_models.api_models.user import UserLoginIn, UserRegisterIn
from src.enums import BizErrCodeEnum
from src.services.base import BaseService


class UserService(BaseService):
    async def login(self, login_info: UserLoginIn):
        user = await UserManager().user_login(login_info.account, login_info.password)
        if not user:
            raise BizException(err_code=BizErrCodeEnum.USER_PWD_ERR)

        token = self.gen_user_token(user_id=user.id, username=user.username)
        logger.info(f"login success, user: {user}")
        return token

    def gen_user_token(self, user_id: int, username: str) -> str:
        user_info = {"user_id": user_id, "username": username}
        jwt_util = JWTUtil(secret_key=self.auth_settings.auth_secret_key, algorithm=self.auth_settings.auth_algorithm)
        token = jwt_util.generate_token(data=user_info, expires_delta=self.auth_settings.auth_expires_delta)
        return token

    async def verify_user_exists(self, username: str = None, phone: str = None, email: str = None):
        err_msgs = []
        if username and await UserManager().user_exists(username=username):
            err_msgs.append("用户名已存在")

        if phone and await UserManager().user_exists(phone=phone):
            err_msgs.append("手机号已存在")

        if email and await UserManager().user_exists(email=email):
            err_msgs.append("邮箱已存在")

        if err_msgs:
            raise BizException(err_code=BizErrCodeEnum.USER_EXISTS, msg=",".join(err_msgs))

    async def register(self, register_info: UserRegisterIn) -> str:
        """用户注册"""
        user_info = register_info.model_dump(exclude_none=True)

        # check if user exists
        await self.verify_user_exists(
            username=register_info.username, phone=register_info.phone, email=register_info.email
        )

        # save to db
        async with UserManager.transaction() as session:
            user_id = await UserManager(session).add(user_info)

            # bind default project
            await ProjectManager(session).create_user_default_todo_project(user_id)

        # gen jwt
        user_info.pop("password", None)
        user_info["user_id"] = user_id
        token = self.gen_user_token(user_id=user_id, username=register_info.username)
        logger.info(f"register success, user: {register_info}")
        return token

    def verify_user_token(self, token: str):
        jwt_util = JWTUtil(secret_key=self.auth_settings.auth_secret_key, algorithm=self.auth_settings.auth_algorithm)
        user_info = jwt_util.verify_token(token=token)
        return user_info
