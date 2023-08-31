#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:58
from src.data_models.api_models import project


class ProjectDetailControllers:
    """ 项目详情路由管理 """

    @classmethod
    async def detail(cls, req_model: project.ProjectDetailIn):
        pass
