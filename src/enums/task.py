#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 项目枚举 }
# @Date: 2023/08/29 14:32
from py_tools.enums import IntEnum


class TaskStatusEnum(IntEnum):
    default = 0  # 默认
    pending = 1  # 进行中
    finished = 2  # 已完成
    overdue = 3  # 已超期
    end = 4  # 已停止


class TaskPriority(IntEnum):
    default = 0  # 默认
    low = 1  # 低
    middle = 2  # 中
    high = 3  # 高
