#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/06 10:45
from py_tools.connections.db.mysql import BaseOrmTable
from sqlalchemy.orm import Mapped, mapped_column

class  UserProjectMappingModel(BaseOrmTable):
    __tablename__ = "user_project_mapping"
    user_id: Mapped[int] = mapped_column(comment="用户id")
    project_id: Mapped[int] = mapped_column(comment="项目id")


class UserTaskMappingModel(BaseOrmTable):
    __tablename__ = "user_task_mapping"
    user_id: Mapped[int] = mapped_column(comment="用户id")
    task_id: Mapped[int] = mapped_column(comment="任务id")


class TaskTagMappingModel(BaseOrmTable):
    __tablename__ = "task_tag_mapping"
    task_id: Mapped[int] = mapped_column(comment="任务id")
    tag_id: Mapped[int] = mapped_column(comment="标签id")


class ProjectTagMappingModel(BaseOrmTable):
    __tablename__ = "project_tag_mapping"
    project_id: Mapped[int] = mapped_column(comment="项目id")
    tag_id: Mapped[int] = mapped_column(comment="标签id")