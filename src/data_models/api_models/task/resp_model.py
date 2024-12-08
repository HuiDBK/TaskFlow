#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:24
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.data_models.api_models.base import PageDataModel, PageRespModel
from src.enums import TaskPriorityEnum, TaskStatusEnum


class TaskItem(BaseModel):
    """查找任务返参信息"""

    id: int = Field(description="任务唯一标识id")
    project_id: int = Field(description="项目id")
    task_name: str = Field(..., description="任务名称")
    task_desc: str = Field(..., description="任务描述")
    task_status: TaskStatusEnum = Field(description="任务状态")
    task_priority: TaskPriorityEnum = Field(description="任务优先级")
    task_tags: Optional[List[dict]] = Field(default=None, description="任务标签")
    start_time: datetime = Field(..., description="任务开始时间")
    end_time: datetime = Field(..., description="任务结束时间")
    username: Optional[List[str]] = Field(default=None, description="任务所属人")


class TaskListData(PageDataModel):
    data_list: List[TaskItem] = Field(description="项目列表")


class TaskListOut(PageRespModel):
    """任务查找出参"""

    data: TaskListData
