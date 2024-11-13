#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from src.controllers.project import ProjectController, ProjectDetailControllers
from src.data_models.api_models import base_api, project_api
from src.data_models.api_models.base import SuccessRespModel
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.create_project,
    response_model=base_api.PKRespModel,
    methods=["POST"],
    summary="项目创建v1",
)

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.update_project,
    response_model=SuccessRespModel,
    methods=["PUT"],
    summary="项目更新",
)

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.query_list_project,
    response_model=project_api.ProjectListOut,
    methods=["GET"],
    summary="项目分页查询",
)

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.delete_project,
    response_model=SuccessRespModel,
    methods=["DELETE"],
    summary="项目删除",
)

router.add_api_route(
    path="/v1/projects/detail",
    endpoint=ProjectDetailControllers.detail_project,
    response_model=project_api.ProjectDetailOut,
    methods=["GET"],
    summary="项目详情",
)
