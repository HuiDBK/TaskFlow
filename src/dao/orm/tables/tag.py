#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/06 11:38
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.dao.orm.tables import BaseTable


class TagTable(BaseTable):
    __tablename__ = "tag"
    tag: Mapped[str] = mapped_column(String(100), comment="标签内容")
    parent_id: Mapped[int] = mapped_column(default=0, comment="父级id")
