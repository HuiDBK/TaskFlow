#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:07
from datetime import date, datetime
from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, Field

from src.data_models.api_models.base import ListPageBaseModel
from src.enums import TaskPriorityEnum, TaskStatusEnum


class TaskCreateIn(BaseModel):
    """任务创建入参"""

    task_name: str = Field(..., min_length=1, max_length=20, description="任务名称")
    task_desc: Optional[str] = Field(default=None, min_length=1, max_length=1024, description="任务描述")
    task_status: Optional[TaskStatusEnum] = Field(default=None, description="任务状态")
    task_priority: Optional[TaskPriorityEnum] = Field(default=None, description="任务优先级")
    task_tags: Optional[List[dict]] = Field(default=[], description="任务标签")
    start_time: Optional[datetime] = Field(default=None, description="任务开始时间")
    end_time: Optional[datetime] = Field(default=None, description="任务结束时间")

    class Config:
        use_enum_values = True


class TaskUpdateIn(TaskCreateIn):
    """任务更新入参"""

    id: int = Field(description="任务唯一标识id")
    task_name: Optional[str] = Field(default=None, min_length=1, max_length=20, description="任务名称")


class TaskQueryIn(ListPageBaseModel):
    """任务查找入参"""

    project_ids: str = Field(Query(description="项目id, 多个用逗号隔开"))
    task_name: Optional[str] = Field(Query(default=None, description="任务名称模糊查询"))
    task_priority: Optional[TaskPriorityEnum] = Field(Query(default=None, description="项目优先级"))
    task_status: Optional[TaskStatusEnum] = Field(Query(default=None, description="项目状态"))
    start_time: Optional[date] = Field(Query(default=None, description="任务开始时间"))
    end_time: Optional[date] = Field(Query(default=None, description="任务结束时间"))

    class Config:
        use_enum_values = True


class TaskDeleteIn(BaseModel):
    project_id: Optional[int] = Field(default=None, description="项目id")
    task_ids: List[int] = Field(description="任务id列表")
