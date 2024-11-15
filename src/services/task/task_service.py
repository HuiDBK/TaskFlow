#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: task_service.py
# @Desc: { 模块描述 }
# @Date: 2024/11/14 15:13
from src.dao.orm.managers import TaskManager
from src.dao.orm.tables import TaskTable
from src.data_models.api_models.task import TaskCreateIn, TaskQueryIn, TaskUpdateIn
from src.services.base import BaseService


class TaskService(BaseService):
    async def create_project_task(self, project_id, task: TaskCreateIn, user_id: int = None):
        task_info = task.model_dump(exclude_none=True)
        user_id = user_id or self.current_user().id
        task_info["user_id"] = user_id
        task_info["project_id"] = project_id

        await self.validate_user_project(user_id, [project_id])

        task_id = await TaskManager().add(task_info)
        return task_id

    async def clear_project_tasks(self, project_ids: list[int], user_id: int = None):
        user_id = user_id or self.current_user().id
        return await TaskManager().delete(conds=[TaskTable.project_id.in_(project_ids), TaskTable.user_id == user_id])

    async def delete_project_task(self, project_id: int, task_ids: list[int], user_id: int = None):
        user_id = user_id or self.current_user().id

        await self.validate_user_project(user_id, [project_id])

        return await TaskManager().delete(
            conds=[TaskTable.project_id == project_id, TaskTable.user_id == user_id, TaskTable.id.in_(task_ids)]
        )

    async def update_task(self, task: TaskUpdateIn, user_id: int = None):
        user_id = user_id or self.current_user().id
        task_info = task.model_dump(exclude_none=True)

        await self.validate_user_task(user_id, [task.id])

        update_ret = await TaskManager().update_or_add(task_info)
        return update_ret

    async def query_tasks(self, project_id: int, task_query_model: TaskQueryIn, user_id: int = None):
        """项目任务分页查询"""
        user_id = user_id or self.current_user().id
        conds = [TaskTable.user_id == user_id, TaskTable.project_id == project_id]
        if task_query_model.task_name:
            # 项目名称模糊查询
            conds.append(TaskTable.task_name.like(f"%{task_query_model.task_name}%"))

        if task_query_model.task_priority:
            # 项目优先级查询
            conds.append(TaskTable.task_priority == task_query_model.task_priority)

        total, data_list = await TaskManager().list_page(
            conds=conds,
            curr_page=task_query_model.current_page,
            page_size=task_query_model.page_size,
        )
        return total, data_list
