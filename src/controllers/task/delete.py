#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 模块描述 }
# @Date: 2023/09/01 14:41
from src.data_models.api_models import task


class TaskDeleteControllers:
    """ 任务创建路由管理 """

    @classmethod
    async def delete(cls, req_model: task.TaskDeleteIn):
        pass
