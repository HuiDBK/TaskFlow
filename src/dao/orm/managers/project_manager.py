#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: project_manager.py
# @Desc: { 模块描述 }
# @Date: 2024/11/11 18:15
from datetime import datetime, timedelta

from src.dao.orm.managers.base import BaseManager
from src.dao.orm.tables import ProjectTable, UserProjectMappingTable


class UserProjectManager(BaseManager):
    orm_table = UserProjectMappingTable

    async def bind_user_project(self, user_id, project_id):
        await self.add(self.orm_table(user_id=user_id, project_id=project_id))

    async def delete_by_project_ids(self, project_ids: list[int]):
        return await self.delete(conds=[self.orm_table.project_id.in_(project_ids)])

    async def delete_by_user_ids(self, user_ids: list[int]):
        return await self.delete(conds=[self.orm_table.user_id.in_(user_ids)])

    async def get_user_project_ids(self, user_ids: list[int], project_ids: list[int] = None) -> list[int]:
        conds = [self.orm_table.user_id.in_(user_ids)]
        if project_ids:
            conds.append(self.orm_table.project_id.in_(project_ids))

        return await self.query_all(
            cols=[self.orm_table.project_id],
            conds=conds,
            flat=True,
        )


class ProjectManager(BaseManager):
    orm_table = ProjectTable

    async def create_user_default_todo_project(self, user_id: int, project_name="默认待办", project_desc="默认待办"):
        start_time = datetime.now()
        end_time = start_time + timedelta(weeks=1)
        project_id = await self.add(
            ProjectTable(project_name=project_name, project_desc=project_desc, start_time=start_time, end_time=end_time)
        )
        await UserProjectManager(self.session).bind_user_project(user_id, project_id)
        return project_id

    async def create_user_project(self, user_id: int, project_info: dict):
        async with self.transaction() as session:
            project_id = await self.add(project_info, session=session)
            await UserProjectManager(session).bind_user_project(user_id, project_id)
            return project_id

    async def delete_projects(self, project_ids: list[int]):
        async with self.transaction() as session:
            del_ret = await self.bulk_delete_by_ids(project_ids, session=session)
            await UserProjectManager(session).delete_by_project_ids(project_ids)
            return del_ret
