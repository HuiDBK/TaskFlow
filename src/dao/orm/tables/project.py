#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/05 17:53
from datetime import datetime

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from src.dao.orm.tables import BaseTable
from src.enums import ProjectPriority


class ProjectTable(BaseTable):
    """项目表"""

    __tablename__ = "project"
    project_name: Mapped[str] = mapped_column(String(100), comment="项目名称")
    project_desc: Mapped[str] = mapped_column(String(1024), comment="项目描述")
    project_status: Mapped[str] = mapped_column(String(100), comment="项目状态")
    project_tags: Mapped[list] = mapped_column(JSON, default=[], comment="项目标签")
    project_type: Mapped[int] = mapped_column(default=0, comment="项目类型")
    project_priority: Mapped[str] = mapped_column(String(100), default=ProjectPriority.medium.value, comment="项目优先级")
    project_icon: Mapped[str] = mapped_column(String(100), default="", comment="项目展示图")
    start_time: Mapped[datetime] = mapped_column(nullable=True, comment="项目开始时间")
    end_time: Mapped[datetime] = mapped_column(nullable=True, comment="项目结束时间")
