#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/04 14:04


from src.data_models.api_models import project


class ProjectControllers:
    """项目创建路由管理"""

    @classmethod
    async def create_project(cls, req_model: project.ProjectCreateIn):
        pass

    @classmethod
    async def delete_project(cls, req_model: project.ProjectDeleteIn):
        pass

    @classmethod
    async def query_list_project(cls, req_model: project.ProjectQueryIn):
        pass

    @classmethod
    async def update_project(cls, req_model: project.ProjectUpdateIn):
        pass


class ProjectDetailControllers:
    """项目详情路由管理"""

    @classmethod
    async def detail_project(cls, req_model: project.ProjectDetailIn):
        pass
