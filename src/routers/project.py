#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from fastapi import APIRouter

from src.data_models.api_models import project_api
from src.controllers.project import ProjectCreateControllers, ProjectQueryControllers, ProjectUpdateControllers, \
    ProjectDeleteControllers, ProjectDetailControllers
from src.data_models.api_models.base import SuccessResp

router = APIRouter()

router.add_api_route(
    path="/create",
    endpoint=ProjectCreateControllers.create,
    response_model=project_api.ProjectCreateOut,
    methods=["POST"],
    summary="项目创建"
)

router.add_api_route(
    path="/update",
    endpoint=ProjectUpdateControllers.update,
    response_model=SuccessResp,
    methods=["PUT"],
    summary="项目更新"
)

router.add_api_route(
    path="/query",
    endpoint=ProjectQueryControllers.query,
    response_model=project_api.ProjectQueryOut,
    methods=["GET"],
    summary="项目查询"
)

router.add_api_route(
    path="/delete",
    endpoint=ProjectDeleteControllers.delete,
    response_model=SuccessResp,
    methods=["DELETE"],
    summary="项目删除"
)

router.add_api_route(
    path="/detail",
    endpoint=ProjectDetailControllers.detail,
    response_model=project_api.ProjectDetailOut,
    methods=["GET"],
    summary="项目详情"
)
