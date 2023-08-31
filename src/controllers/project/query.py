#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:15
from src.data_models.api_models import project


class ProjectQueryControllers:
    """ 项目查找路由管理 """

    @classmethod
    async def query(cls, req_model: project.ProjectQueryIn):
        pass
