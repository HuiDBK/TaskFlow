#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { redis相关枚举 }
# @Date: 2023/09/07 17:13
from py_tools.enums import BaseEnum


class RedisTypeEnum(BaseEnum):
    """Redis 数据类型"""

    String = "String"
    List = "List"
    Hash = "Hash"
    Set = "Set"
    ZSet = "ZSet"
