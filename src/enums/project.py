#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 项目枚举 }
# @Date: 2023/08/29 14:32
from py_tools.enums import IntEnum


class ProjectStatusEnum(IntEnum):
    One = 1  # 进行中
    Tow = 2  # 已完成
    Three = 3  # 已超期
    Four = 4  # 已停止
