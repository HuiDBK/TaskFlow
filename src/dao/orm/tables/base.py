#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: base.py
# @Desc: { 模块描述 }
# @Date: 2024/11/15 15:52
from py_tools.connections.db.mysql import BaseOrmTableWithTS


class BaseTable(BaseOrmTableWithTS):
    """不直接继承第三方库的基类，用于扩展"""

    __abstract__ = True
