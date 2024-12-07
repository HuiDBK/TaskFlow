#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: github_oauth_service.py
# @Desc: { github oauth service }
# @Date: 2024/12/07 18:30
import uuid
from datetime import timedelta

from py_tools.connections.http import AsyncHttpClient
from py_tools.logging import logger
from sqlalchemy import or_

from src.dao.orm.managers import UserManager
from src.dao.orm.tables import UserTable
from src.data_models.api_models.user import UserRegisterIn
from src.services.base import BaseService
from src.services.user.user_service import UserService


class GithubOAuthService(BaseService):
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    async def handle_callback(self, code: str, redirect_uri: str = None):
        """
        处理 github oauth 回调
        Args:
            code: 授权码
            redirect_uri: 回调地址，用于校验防攻击
        Returns:
        """
        access_token = await self.get_access_token(code, redirect_uri)
        github_user = await self.get_user_info(access_token)

        # 与业务系统用户绑定
        token = await self.bind_github_user(github_user)

        return token

    async def bind_github_user(self, github_user):
        """
        与业务系统用户绑定
        Args:
            github_user: github user info

        Notes:
            1. 先根据 github 的 id or email 查询用户，若存在，则直接登录
            2. 若不存在，则自动注册

        Returns:
            token
        """
        conds = [
            UserTable.github_uid == github_user["id"],
        ]
        if github_user.get("email"):
            conds.append(UserTable.email == github_user["email"])
        conds = [or_(*conds)]
        user: UserTable = await UserManager().query_one(conds=conds)
        logger.info(f"user: {user}")

        if user:
            logger.info("用户关联github账号，自动登录")
            if not user.github_uid:
                # 通过邮箱关联自动绑定
                user.github_uid = github_user["id"]
                await UserManager().update_or_add(user)
            token = UserService().gen_user_token(user.id, user.username)
        else:
            logger.info("用户未绑定github账号，自动注册")
            new_user = UserRegisterIn(
                username=github_user["login"],
                password=uuid.uuid4().hex[:12],
                github_uid=github_user["id"],
                email=github_user["email"],
            )
            token = await UserService().register(new_user)
        return token

    async def get_access_token(self, code: str, redirect_uri: str = None):
        """
        通过授权码 获取 access token
        Args:
            code: 授权码
            redirect_uri: 回调地址，用于校验防攻击

        Returns:
        """
        url = "https://github.com/login/oauth/access_token"
        data = {"client_id": self.client_id, "client_secret": self.client_secret, "code": code}
        if redirect_uri:
            data["redirect_uri"] = redirect_uri

        headers = {"Accept": "application/json"}
        access_token_info = (
            await AsyncHttpClient(timeout=timedelta(minutes=1)).post(url, json=data, headers=headers).json()
        )
        logger.info(access_token_info)
        return access_token_info["access_token"]

    async def get_user_info(self, access_token: str):
        """
        通过 access token 获取用户信息
        Args:
            access_token:
        Returns:
        """
        url = "https://api.github.com/user"
        headers = {
            "Authorization": f"Bearer {access_token}",
        }
        github_user = await AsyncHttpClient(timeout=timedelta(minutes=1)).get(url, headers=headers).json()
        logger.info(github_user)
        return github_user
