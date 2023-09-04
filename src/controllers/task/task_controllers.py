#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/04 14:08
from src.data_models.api_models import task


class TaskControllers:
    """任务创建路由管理"""

    @classmethod
    async def create_task(cls, req_model: task.TaskCreateIn):
        pass

    @classmethod
    async def delete_task(cls, req_model: task.TaskDeleteIn):
        pass

    @classmethod
    async def query_list_task(cls, req_model: task.TaskQueryIn):
        pass

    @classmethod
    async def update_task(cls, req_model: task.TaskUpdateIn):
        pass
