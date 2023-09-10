#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:07
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.data_models.api_models.base import ListPageBaseModel


class TaskCreateIn(BaseModel):
    """ 任务创建入参 """
    task_name: str = Field(..., description="任务名称")
    task_tag: Optional[List[str]] = Field(default=None, description="任务标签")
    start_time: datetime = Field(..., description="任务开始时间")
    end_time: datetime = Field(..., description="任务结束时间")


class TaskUpdateIn(BaseModel):
    """ 任务更新入参 """
    id: int = Field(description="任务唯一标识id")
    task_name: Optional[str] = Field(..., description="任务名称")
    task_tag: Optional[List[str]] = Field(default=None, description="任务标签")
    start_time: Optional[datetime] = Field(..., description="任务开始时间")
    end_time: Optional[datetime] = Field(..., description="任务结束时间")


class TaskQueryIn(ListPageBaseModel):
    """ 任务查找入参 """
    task_name: Optional[str] = Field(default=None, description="任务名称模糊查询")


class TaskDeleteIn(BaseModel):
    task_ids: List[int] = Field(description="任务唯一标识id")
