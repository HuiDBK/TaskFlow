#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/04 14:04
from fastapi import Depends

from src.controllers.base import BaseController
from src.data_models.api_models import project
from src.data_models.api_models.base import PageRespModel, PKRespModel, SuccessRespModel
from src.services.project import ProjectService


class ProjectController(BaseController):
    """项目路由管理"""

    @classmethod
    async def create_project(cls, req_model: project.ProjectCreateIn):
        project_id = await ProjectService().create_project(req_model)
        return PKRespModel(pk_id=project_id)

    @classmethod
    async def delete_project(cls, req_model: project.ProjectDeleteIn):
        await ProjectService().delete_project(req_model.project_ids, cls.current_user().id)
        return SuccessRespModel()

    @classmethod
    async def query_projects(cls, req_model=Depends(project.ProjectQueryIn)):
        total, data_list = await ProjectService().list_projects(req_model)
        return PageRespModel(total=total, data_list=data_list)

    @classmethod
    async def update_project(cls, req_model: project.ProjectUpdateIn):
        await ProjectService().update_project(req_model)
        return SuccessRespModel()


class ProjectDetailControllers:
    """项目详情路由管理"""

    @classmethod
    async def detail_project(cls, req_model: project.ProjectDetailIn):
        pass
