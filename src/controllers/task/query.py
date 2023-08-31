#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:41
from src.data_models.api_models import task


class TaskQueryControllers:
    """ 任务创建路由管理 """

    @classmethod
    async def query(cls, req_model: task.TaskQueryIn):
        pass
