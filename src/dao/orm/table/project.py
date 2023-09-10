#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/05 17:53
from datetime import datetime

from py_tools.connections.db.mysql import BaseOrmTable
from sqlalchemy.orm import Mapped, mapped_column


class ProjectTable(BaseOrmTable):
    """项目表"""

    __tablename__ = "project"
    project_name: Mapped[str] = mapped_column(comment="项目名称")
    project_desc: Mapped[str] = mapped_column(comment="项目描述")
    project_status: Mapped[int] = mapped_column(default=0, comment="项目状态")
    project_icon: Mapped[str] = mapped_column(default="", comment="项目展示图")
    start_time: Mapped[datetime] = mapped_column(comment="项目开始时间")
    end_time: Mapped[datetime] = mapped_column(comment="项目结束时间")
