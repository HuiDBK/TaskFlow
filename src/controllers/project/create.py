#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 15:57
from src.data_models.api_models import project


class ProjectCreateControllers:
    """ 项目创建路由管理 """

    @classmethod
    async def create(cls, req_model: project.ProjectCreateIn):
        pass
