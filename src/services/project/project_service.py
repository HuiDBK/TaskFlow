#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: project_service.py
# @Desc: { 模块描述 }
# @Date: 2024/11/12 11:12
from src.dao.orm.managers.project_manager import ProjectManager, UserProjectManager
from src.dao.orm.tables import ProjectTable, UserProjectMappingTable
from src.data_models.api_models.project import (
    ProjectCreateIn,
    ProjectQueryIn,
    ProjectUpdateIn,
)
from src.services.base import BaseService


class ProjectService(BaseService):
    async def create_project(self, project: ProjectCreateIn, user_id: int = None):
        project_info = project.model_dump(exclude_none=True)
        user_id = user_id or self.current_user().id
        project_id = await ProjectManager().create_user_project(user_id, project_info)
        return project_id

    async def delete_project(self, project_ids: list[int], user_id: int = None):
        user_id = user_id or self.current_user().id
        can_project_ids = await UserProjectManager().get_user_project_ids([user_id], project_ids)
        return await ProjectManager().delete_projects(can_project_ids)

    async def update_project(self, project: ProjectUpdateIn):
        project_info = project.model_dump(exclude_none=True)
        update_ret = await ProjectManager().update_or_add(project_info)
        return update_ret

    async def list_projects(self, project_query_model: ProjectQueryIn, user_id: int = None):
        """项目分页查询"""
        user_id = user_id or self.current_user().id
        conds = self.build_query_project_conds(project_query_model, user_id)

        total, data_list = await ProjectManager().list_page(
            cols=ProjectTable.all_columns(),
            join_tables=[(UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id)],
            conds=conds,
            orders=[ProjectTable.end_time.asc()],
            curr_page=project_query_model.current_page,
            page_size=project_query_model.page_size,
        )
        return total, data_list

    def build_query_project_conds(self, project_query_model: ProjectQueryIn, user_id: int):
        conds = [UserProjectMappingTable.user_id == user_id]
        if project_query_model.project_name:
            # 项目名称模糊查询
            conds.append(ProjectTable.project_name.like(f"%{project_query_model.project_name}%"))
        if project_query_model.project_priority:
            # 项目优先级查询
            conds.append(ProjectTable.project_priority == project_query_model.project_priority)
        if project_query_model.project_status:
            # 项目状态查询
            conds.append(ProjectTable.project_status == project_query_model.project_status)
        if project_query_model.start_time and project_query_model.end_time:
            # 项目时间范围查询
            conds.append(ProjectTable.start_time >= project_query_model.start_time)
            conds.append(ProjectTable.end_time <= project_query_model.end_time)
        return conds
