#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 15:22
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from src.data_models.api_models.base import ListPageBaseModel


class TagCreateIn(BaseModel):
    """ 标签创建入参"""
    tag: str = Field(..., description="标签内容")
    pass


class TagUpdateIn(BaseModel):
    """ 标签更新入参 """
    pass
