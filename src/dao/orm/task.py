#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/06 11:08
from datetime import datetime

from py_tools.connections.db.mysql import BaseOrmTable
from sqlalchemy.orm import Mapped, mapped_column


class TaskTable(BaseOrmTable):
    __tablename__ = "task"
    task_name: Mapped[str] = mapped_column(comment="任务名称")
    start_time: Mapped[datetime] = mapped_column(comment="项目开始时间")
    end_time: Mapped[datetime] = mapped_column(comment="项目结束时间")
