#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:06
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.data_models.api_models.base import ListPageBaseModel
from src.enums import ProjectStatusEnum
from src.enums.project import ProjectPriority


class ProjectCreateIn(BaseModel):
    """项目创建入参"""

    project_name: str = Field(min_length=1, description="项目名称")
    project_desc: str = Field(description="项目描述")
    project_status: Optional[ProjectStatusEnum] = Field(description="项目状态")
    project_type: Optional[int] = Field(description="项目类型")
    project_priority: Optional[ProjectPriority] = Field(description="项目优先级")
    start_time: Optional[datetime] = Field(description="项目开始时间")
    end_time: Optional[datetime] = Field(description="项目结束时间")
    project_tags: Optional[List[str]] = Field(description="项目标签")
    project_icon: Optional[str] = Field(description="项目展示图地址-oss key")


class ProjectUpdateIn(BaseModel):
    """项目更新入参"""

    id: int = Field(description="项目唯一标识id")
    project_name: Optional[str] = Field(default=None, description="项目名称")
    project_desc: Optional[str] = Field(default=None, description="项目描述")
    project_status: Optional[ProjectStatusEnum] = Field(default=None, description="项目状态")
    project_type: Optional[int] = Field(default=None, description="项目类型")
    project_priority: Optional[ProjectPriority] = Field(default=None, description="项目优先级")
    start_time: Optional[datetime] = Field(default=None, description="开始时间")
    end_time: Optional[datetime] = Field(default=None, description="结束时间")
    project_tags: Optional[List[str]] = Field(default=None, description="项目标签")
    project_icon: Optional[str] = Field(default=None, description="项目展示图地址-oss key ")


class ProjectQueryIn(ListPageBaseModel):
    """项目查找入参"""

    project_name: Optional[str] = Field(default=None, description="项目名称模糊查询")
    project_priority: Optional[ProjectPriority] = Field(default=None, description="项目优先级")


class ProjectDeleteIn(BaseModel):
    project_ids: List[int] = Field(description="项目唯一标识id")


class ProjectDetailIn(ListPageBaseModel):
    id: int = Field(description="项目唯一标识id")
