#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:06
from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from src.data_models.api_models.base import BaseRespModel, PageDataModel, PageRespModel
from src.enums.project import ProjectPriority


class ProjectQueryItem(BaseModel):
    """查找项目返参信息"""

    id: int = Field(description="项目唯一标识id")
    project_name: str = Field(description="项目名称")
    project_desc: str = Field(description="项目描述")
    project_status: int = Field(description="项目状态")
    project_priority: ProjectPriority = Field(default=None, description="项目优先级")
    start_time: Union[datetime, None] = Field(description="项目开始时间")
    end_time: Union[datetime, None] = Field(description="项目结束时间")
    project_tags: Optional[List[str]] = Field(default=None, description="项目标签")
    project_icon: str = Field(..., description="项目展示图地址-oss key..此时返回的是一个URL")


class ProjectDetailItem(BaseModel):
    """项目详情返参"""

    id: int = Field(description="项目唯一标识id")
    created_at: datetime = Field(description="项目创建时间")
    project_name: str = Field(description="项目名称")
    project_desc: str = Field(description="项目描述")
    project_status: int = Field(description="项目状态")
    start_time: datetime = Field(description="项目开始时间")
    end_time: datetime = Field(..., description="项目结束时间")
    project_tag: Optional[List[str]] = Field(default=None, description="项目标签")
    username: Optional[List[str]] = Field(default=None, description="项目所属人")
    project_icon: str = Field(..., description="项目展示图地址-oss key")


# class ProjectCreateItem(BaseModel):
#     """ 创建项目返参 """
#     id: int = Field(description="项目主键id")


class ProjectDetailOut(BaseRespModel):
    """项目详情出参"""

    data: ProjectDetailItem


class ProjectListData(PageDataModel):
    data_list: List[ProjectQueryItem] = Field(description="项目列表")


class ProjectListOut(PageRespModel):
    """项目列表出参"""

    data: ProjectListData
