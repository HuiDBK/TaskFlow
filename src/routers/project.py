#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from fastapi import APIRouter

from src.controllers.project import ProjectControllers, ProjectDetailControllers
from src.data_models.api_models import base_api, project_api
from src.data_models.api_models.base import SuccessRespModel

router = APIRouter()

router.add_api_route(
    path="/create",
    endpoint=ProjectControllers.create_project,
    response_model=base_api.PKRespModel,
    methods=["POST"],
    summary="项目创建",
)

router.add_api_route(
    path="/update",
    endpoint=ProjectControllers.update_project,
    response_model=SuccessRespModel,
    methods=["PUT"],
    summary="项目更新",
)

router.add_api_route(
    path="/query_list",
    endpoint=ProjectControllers.query_list_project,
    response_model=project_api.ProjectQueryOut,
    methods=["GET"],
    summary="项目分页查询",
)

router.add_api_route(
    path="/delete",
    endpoint=ProjectControllers.delete_project,
    response_model=SuccessRespModel,
    methods=["DELETE"],
    summary="项目删除",
)

router.add_api_route(
    path="/detail",
    endpoint=ProjectDetailControllers.detail_project,
    response_model=project_api.ProjectDetailOut,
    methods=["GET"],
    summary="项目详情",
)
