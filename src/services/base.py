#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 通用逻辑 }
# @Date: 2023/08/29 16:46
from typing import Type

from py_tools.enums.error import BaseErrCodeEnum
from py_tools.exceptions import BizException

from src.dao.orm.managers import TaskManager, UserProjectManager
from src.dao.orm.managers.base import BaseManager
from src.dao.orm.tables import TaskTable, UserProjectMappingTable
from src.settings import auth_setting
from src.utils.context_util import ContextMixin


class BaseService(ContextMixin):
    @property
    def auth_settings(self):
        return auth_setting

    async def _validate(self, manager_cls: Type[BaseManager], conds: list):
        if not await manager_cls().query_all(cols=["id"], conds=conds):
            raise BizException(BaseErrCodeEnum.NOT_FOUND_ERR)

    async def validate_user_task(self, user_id, task_ids: list[int]):
        conds = [TaskTable.user_id == user_id, TaskTable.id.in_(task_ids)]
        await self._validate(TaskManager, conds)

    async def validate_project_task(self, project_id, task_ids: list[int]):
        conds = [TaskTable.project_id == project_id, TaskTable.id.in_(task_ids)]
        await self._validate(TaskManager, conds)

    async def validate_user_project(self, user_id, project_ids: list[int]):
        conds = [UserProjectMappingTable.user_id == user_id, UserProjectMappingTable.project_id.in_(project_ids)]
        await self._validate(UserProjectManager, conds)
