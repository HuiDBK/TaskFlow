#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:24
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.data_models.api_models.base import BaseRespModel


class TaskQueryItem(BaseModel):
    """ 查找任务返参信息 """
    id: int = Field(description="任务唯一标识id")
    task_name: str = Field(..., description="任务名称")
    task_tag: Optional[List[str]] = Field(default=None, description="任务标签")
    start_time: datetime = Field(..., description="任务开始时间")
    end_time: datetime = Field(..., description="任务结束时间")
    username: Optional[List[str]] = Field(default=None, description="任务所属人")


# 任务就不需要再查看详情信息了，直接显示出来就行了

class TaskCreateItem(BaseModel):
    """ 创建任务返参 """
    id: int = Field(description="任务主键id")


class TaskCreateOut(BaseRespModel):
    """ 任务创建出参 """

    data: TaskCreateItem


class TaskQueryOut(BaseRespModel):
    """ 任务查找出参 """

    data: TaskQueryItem
