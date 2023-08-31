#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:29
from datetime import date

from pydantic import BaseModel, Field, validator
from typing import Optional

from src.constants import constants


class ListPageBaseModel(BaseModel):
    """分页入参模型"""
    current_page: Optional[int] = Field(default=1, gt=0, description="页码")
    page_size: Optional[int] = Field(
        default=constants.DEFAULT_PAGE_SIZE, gt=0, le=constants.MAX_PAGE_SIZE, description="每页数量，默认10，最大1000")


class DateModel(BaseModel):
    """日期模型"""

    start_date: Optional[date] = Field(None, description="开始日期")
    end_date: Optional[date] = Field(None, description="结束日期")

    @validator("end_date", always=True)
    def validate_end_date(cls, end_date, values):
        start_date = values.get("start_date")
        if all([start_date, end_date]) and end_date < start_date:
            raise ValueError("结束日期必须大于等于开始日期")
        return end_date
