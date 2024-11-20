#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/04 14:08
from src.data_models.api_models import task
from src.data_models.api_models.base import PageRespModel, PKRespModel, SuccessRespModel
from src.services.task import TaskService


class TaskController:
    """任务创建路由管理"""

    @classmethod
    async def create_task(cls, project_id: int, req_model: task.TaskCreateIn):
        task_id = await TaskService().create_project_task(project_id, req_model)
        return PKRespModel(pk_id=task_id)

    @classmethod
    async def delete_task(cls, req_model: task.TaskDeleteIn):
        await TaskService().delete_project_task(req_model.project_id, req_model.task_ids)
        return SuccessRespModel()

    @classmethod
    async def query_tasks(cls, project_id: int, req_model: task.TaskQueryIn):
        total, data_list = await TaskService().query_tasks(project_id, req_model)
        return PageRespModel(total=total, data_list=data_list)

    @classmethod
    async def update_task(cls, req_model: task.TaskUpdateIn):
        await TaskService().update_task(req_model)
        return SuccessRespModel()