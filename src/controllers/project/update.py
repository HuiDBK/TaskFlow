#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:14
from src.data_models.api_models import project


class ProjectUpdateControllers:
    """ 项目更新路由管理 """

    @classmethod
    async def update(cls, req_model: project.ProjectUpdateIn):
        pass
