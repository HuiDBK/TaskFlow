#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from src.controllers.task import TaskControllers
from src.data_models.api_models import base_api, task_api
from src.data_models.api_models.base import SuccessRespModel
from src.routers.base import APIRouter

router = APIRouter()

router.add_api_route(
    path="/create",
    endpoint=TaskControllers.create_task,
    response_model=base_api.PKRespModel,
    methods=["POST"],
    summary="任务创建",
)

router.add_api_route(
    path="/update", endpoint=TaskControllers.update_task, response_model=SuccessRespModel, methods=["PUT"], summary="任务更新"
)

router.add_api_route(
    path="/query_list",
    endpoint=TaskControllers.query_list_task,
    response_model=task_api.TaskQueryOut,
    methods=["GET"],
    summary="任务分页查询",
)

router.add_api_route(
    path="/delete", endpoint=TaskControllers.delete_task, response_model=SuccessRespModel, methods=["DELETE"], summary="任务删除"
)
