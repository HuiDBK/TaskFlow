#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户数据表模型 }
# @Date: 2023/08/29 16:56
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.dao.orm.tables import BaseTable


class UserTable(BaseTable):
    """用户表"""

    __tablename__ = "user"
    username: Mapped[str] = mapped_column(String(20), comment="用户昵称")
    password: Mapped[str] = mapped_column(String(20), comment="用户密码")
    phone: Mapped[str] = mapped_column(String(11), comment="手机号")
    email: Mapped[str] = mapped_column(String(20), comment="邮箱")