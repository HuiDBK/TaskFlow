#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/06 11:08
from datetime import datetime

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from src.dao.orm.tables import BaseTable
from src.enums.task import TaskPriorityEnum, TaskStatusEnum


class TaskTable(BaseTable):
    __tablename__ = "task"
    project_id: Mapped[int] = mapped_column(default=0, comment="项目id")
    user_id: Mapped[int] = mapped_column(default=0, comment="用户id")
    task_name: Mapped[str] = mapped_column(String(100), comment="任务名称")
    task_desc: Mapped[str] = mapped_column(String(1024), comment="任务描述")
    task_status: Mapped[str] = mapped_column(String(100), default=TaskStatusEnum.todo.value, comment="任务状态")
    task_priority: Mapped[str] = mapped_column(String(100), default=TaskPriorityEnum.low.value, comment="任务优先级")
    task_tags: Mapped[list] = mapped_column(JSON, default=[], comment="任务标签")
    start_time: Mapped[datetime] = mapped_column(nullable=True, comment="项目开始时间")
    end_time: Mapped[datetime] = mapped_column(nullable=True, comment="项目结束时间")
