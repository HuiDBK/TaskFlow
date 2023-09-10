#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/07/13 16:30
from typing import List

from pydantic import BaseModel, Field

from src.data_models.api_models.base import BaseRespModel


class UploadFileDataItem(BaseModel):
    """文件上传出参信息"""

    file_name: str = Field(description="文件名称")
    file_key: str = Field(description="文件唯一key")


class BatchUploadDataItem(BaseModel):
    """批量文件上传出参信息"""

    file_list: List[UploadFileDataItem] = Field(description="文件列表")


class UploadFileOut(BaseRespModel):
    """上传文件出参"""

    data: UploadFileDataItem


class BatchUploadFileOut(BaseRespModel):
    """批量上传文件出参"""

    data: BatchUploadDataItem
