#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 项目枚举 }
# @Date: 2023/08/29 14:32
from py_tools.enums import StrEnum


class TaskStatusEnum(StrEnum):
    todo = "todo"  # 代办
    inProgress = "inProgress"  # 进行中
    completed = "completed"  # 已完成


class TaskPriorityEnum(StrEnum):
    low = "low"  # 低
    medium = "medium"  # 中
    high = "high"  # 高
