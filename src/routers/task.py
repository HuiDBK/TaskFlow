#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/08/30 12:11
from fastapi import APIRouter

from src.controllers.task import TaskCreateControllers, TaskUpdateControllers, TaskQueryControllers, \
    TaskDeleteControllers
from src.data_models.api_models import task_api
from src.data_models.api_models.base import SuccessResp

router = APIRouter()

router.add_api_route(
    path="/create",
    endpoint=TaskCreateControllers.create,
    response_model=task_api.TaskCreateOut,
    methods=["POST"],
    summary="任务创建"
)

router.add_api_route(
    path="/update",
    endpoint=TaskUpdateControllers.update,
    response_model=SuccessResp,
    methods=["PUT"],
    summary="任务更新"
)

router.add_api_route(
    path="/query",
    endpoint=TaskQueryControllers.query,
    response_model=task_api.TaskQueryOut,
    methods=["GET"],
    summary="任务查询"
)

router.add_api_route(
    path="/delete",
    endpoint=TaskDeleteControllers.delete,
    response_model=SuccessResp,
    methods=["DELETE"],
    summary="任务删除"
)
