#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from src.controllers.task import TaskController
from src.data_models.api_models import task_api
from src.data_models.api_models.base import PKRespModel, SuccessRespModel
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()

router.add_api_route(
    path="/v1/projects/{project_id}/tasks",
    endpoint=TaskController.create_task,
    response_model=PKRespModel,
    methods=["POST"],
    summary="任务创建",
)

router.add_api_route(
    path="/v1/projects/{project_id}/tasks",
    endpoint=TaskController.update_task,
    response_model=SuccessRespModel,
    methods=["PUT"],
    summary="任务更新",
)

router.add_api_route(
    path="/v1/projects/{project_id}/tasks",
    endpoint=TaskController.query_tasks,
    response_model=task_api.TaskListOut,
    methods=["GET"],
    summary="任务分页查询",
)

router.add_api_route(
    path="/v1/projects/{project_id}/tasks",
    endpoint=TaskController.delete_task,
    response_model=SuccessRespModel,
    methods=["DELETE"],
    summary="任务删除",
)
