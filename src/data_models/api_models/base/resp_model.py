#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:29
from pydantic import BaseModel, Field


class BaseRespModel(BaseModel):
    code: int = Field(..., description="响应吗")
    message: str = Field(..., description="响应消息")
    data: dict = Field(..., description="响应数据")


class SuccessResp(BaseRespModel):
    code: int = Field(default=1, description="响应吗")
    message: str = Field(default="OK", description="响应消息")
    data: dict = Field(default={}, description="响应数据")
