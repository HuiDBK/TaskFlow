#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: user_manager.py
# @Desc: { 模块描述 }
# @Date: 2024/11/11 15:19
from py_tools.utils import RegexUtil
from sqlalchemy import or_

from src.dao.orm.managers.base import BaseManager
from src.dao.orm.tables.user import UserTable


class UserManager(BaseManager):
    orm_table = UserTable

    async def user_login(self, account: str, password: str) -> UserTable:
        """
        用户登录
        Args:
            account: 用户账号（支持 用户名/手机号/邮箱）
            password: 用户密码

        Returns:
            user
        """
        if RegexUtil.find_chinese_phone_numbers(account):
            # 手机号登陆
            conds = [UserTable.phone == account, UserTable.password == password]
        elif RegexUtil.find_emails(account):
            # 邮箱登陆
            conds = [UserTable.email == account, UserTable.password == password]
        else:
            # 用户名登陆
            conds = [UserTable.username == account, UserTable.password == password]

        user = await self.query_one(conds=conds)
        return user

    async def user_exists(self, username: str = None, phone: str = None, email: str = None) -> bool:
        """
        用户是否存在，用户名、手机号、邮箱至少一个存在即可
        Args:
            username: 用户名
            phone: 手机号
            email: 邮箱

        Returns:
            bool
        """
        conds = []
        if username:
            conds.append(UserTable.username == username)

        if email:
            conds.append(UserTable.email == email)

        if phone:
            conds.append(UserTable.phone == phone)

        conds = or_(*conds)
        user = await UserManager().query_one(cols=[UserTable.id], conds=conds)
        return bool(user)
