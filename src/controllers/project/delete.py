#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/31 16:15
from src.data_models.api_models import project


class ProjectDeleteControllers:
    """ 项目删除路由管理 """

    @classmethod
    async def delete(cls, req_model: project.ProjectDeleteIn):
        pass
