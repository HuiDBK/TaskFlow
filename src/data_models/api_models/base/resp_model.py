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


class PageDataModel(BaseModel):
    total: int = Field(default=0, description="总条数")
    data_list: list = Field(default=[], description="分页数据列表")


class PageRespModel(SuccessRespModel):
    data: PageDataModel = Field(None, description="分页数据")

    def __init__(self, total: int, data_list: list, **kwargs):
        super().__init__(**kwargs)
        self.data = PageDataModel(total=total, data_list=data_list)


class PKModel(BaseModel):
    id: int = Field(description="主键id")


class PKRespModel(SuccessRespModel):
    data: PKModel = Field(None, description="主键响应模型")

    def __init__(self, pk_id: int, **kwargs):
        super().__init__(**kwargs)
        self.data = PKModel(id=pk_id)


class TokenModel(BaseModel):
    token: str = Field(description="token")


class TokenRespModel(SuccessRespModel):
    data: TokenModel = Field(None, description="token响应模型")

    def __init__(self, token: str, **kwargs):
        super().__init__(**kwargs)
        self.data = TokenModel(token=token)
