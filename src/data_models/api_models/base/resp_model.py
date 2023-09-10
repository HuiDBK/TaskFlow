#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 11:29
from pydantic import BaseModel, Field

from src.enums import BizErrCodeEnum


class BaseRespModel(BaseModel):
    code: str = Field(..., description="响应吗")
    message: str = Field(..., description="响应消息")
    data: dict = Field(..., description="响应数据")


class SuccessRespModel(BaseRespModel):
    code: str = Field(default=BizErrCodeEnum.OK.code, description="响应码")
    message: str = Field(default=BizErrCodeEnum.OK.msg, description="响应消息")
    data: dict = Field(default={}, description="响应数据")


class PKModel(BaseModel):
    id: int = Field(description="主键id")


class PKRespModel(SuccessRespModel):
    data: PKModel = Field(description="主键响应模型")
