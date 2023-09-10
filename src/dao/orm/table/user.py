#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户数据表模型 }
# @Date: 2023/08/29 16:56
from py_tools.connections.db.mysql import BaseOrmTable
from sqlalchemy.orm import Mapped, mapped_column


class UserTable(BaseOrmTable):
    """用户表"""

    __tablename__ = "user"
    username: Mapped[str] = mapped_column(comment="用户昵称")
    password: Mapped[str] = mapped_column(comment="用户密码")
    phone: Mapped[str] = mapped_column(comment="手机号")
    email: Mapped[str] = mapped_column(comment="邮箱")
