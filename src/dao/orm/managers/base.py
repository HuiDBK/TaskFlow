#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: BaseDBManager.py
# @Desc: { 模块描述 }
# @Date: 2024/11/12 14:24
import asyncio
from typing import Any, List, Type, Union

from py_tools.connections.db.mysql import BaseOrmTable, DBManager
from py_tools.connections.db.mysql.client import T_BaseOrmTable, with_session
from sqlalchemy import Result, column, func, select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseManager(DBManager):
    def __init__(self, session: AsyncSession = None):
        self.session = session

    @with_session
    async def _query(
        self,
        *,
        cols: list = None,
        orm_table: BaseOrmTable = None,
        join_tables: list = None,
        conds: list = None,
        orders: list = None,
        limit: int = None,
        offset: int = 0,
        session: AsyncSession = None,
    ) -> Result[Any]:
        """
        通用查询
        Args:
            cols: 查询的列表字段
            orm_table: orm表映射类
            join_tables: 连表信息 [(table, conds, join_type), ...]
                eg: [(UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id, "left")]
            conds: 查询的条件列表
            orders: 排序列表, 默认id升序
            limit: 限制数量大小
            offset: 偏移量
            session: 数据库会话对象，如果为 None，则通过装饰器在方法内部开启新的事务

        Returns: 查询结果集
            cursor_result
        """
        cols = cols or []
        cols = [column(col_obj) if isinstance(col_obj, str) else col_obj for col_obj in cols]  # 兼容字符串列表

        join_tables = join_tables or []
        conditions = conds or []
        orders = orders or []
        orm_table = orm_table or self.orm_table

        # 构造查询
        if not cols:
            if join_tables:
                # 没有指定查询列，查询连表的所有列
                all_tables = [orm_table] + [join_table[0] for join_table in join_tables]
                cols = [col for table in all_tables for col in table.__table__.columns]
                query_sql = select(*cols).select_from(orm_table)
            else:
                # 没有指定查询列，没有连表，查询所有列（返回orm 实例）
                query_sql = select(orm_table)

        else:
            query_sql = select(*cols).select_from(orm_table)

        # 构造连表
        if join_tables:
            query_sql = await self._build_join(join_tables, query_sql)

        query_sql = query_sql.where(*conditions).order_by(*orders)
        if limit:
            query_sql = query_sql.limit(limit).offset(offset)

        # 执行查询
        cursor_result = await session.execute(query_sql)
        return cursor_result

    async def _build_join(self, join_tables: list, query_sql):
        """
        构造连表
        Args:
            join_tables: 连表信息 [(table, conds, join_type)]
                eg: [(UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id, "left")]
            query_sql: 查询sql

        Returns:
            query_sql
        """
        for join_entry in join_tables:
            join_entry_num = len(join_entry)
            if join_entry_num < 2:
                raise ValueError("join_tables must have at least 2 columns")

            if join_entry_num == 2:
                join_table, join_condition = join_entry
                join_type = None  # Default to inner join
            else:
                join_table, join_condition, join_type, *_ = join_entry

            # Determine join type
            isouter = join_type == "left"
            query_sql = query_sql.join(join_table, join_condition, isouter=isouter)
        return query_sql

    @with_session
    async def query_one(
        self,
        *,
        cols: list = None,
        orm_table: Type[BaseOrmTable] = None,
        join_tables: list = None,
        conds: list = None,
        orders: list = None,
        flat: bool = False,
        session: AsyncSession = None,
    ) -> Union[dict, T_BaseOrmTable, Any]:
        """
        查询单行
        Args:
            cols: 查询的列表字段
            orm_table: orm表映射类
            join_tables: 连表信息(table, conds, join_type)
                eg: (UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id, "left")
            conds: 查询的条件列表
            orders: 排序列表
            flat: 单字段时扁平化处理
            session: 数据库会话对象，如果为 None，则通过装饰器在方法内部开启新的事务

        Examples:
            # 指定列名
            ret = await UserManager().query_one(cols=["username", "age"], conds=[UserTable.id == 1])
            sql => select username, age from user where id=1
            ret => {"username": "hui", "age": 18}

            # 指定列名，单字段扁平化处理
            ret = await UserManager().query_one(cols=["username"], conds=[UserTable.id == 1])
            sql => select username from user where id=1
            ret => {"username": "hui"} => "hui"

            # 计算总数
            ret = await UserManager().query_one(cols=[func.count()])
            sql => select count(*) as count from user
            ret => {"count": 10} => 10

            # 不指定列名，查询全部字段, 返回表实例对象
            ret = await UserManager().query_one(conds=[UserTable.id == 1])
            sql => select id, username, age from user where id=1
            ret => UserTable(id=1, username="hui", age=18)

        Returns:
            Union[dict, BaseOrmTable(), Any(flat=True)]
        """
        cursor_result = await self._query(
            cols=cols, orm_table=orm_table, join_tables=join_tables, conds=conds, orders=orders, session=session
        )
        if cols:
            if flat and len(cols) == 1:
                # 单行单字段查询: 直接返回字段结果
                # eg: select count(*) as count from user 从 {"count": 100} => 100
                # eg: select username from user where id=1 从 {"username": "hui"} => "hui"
                return cursor_result.scalar_one()

            # eg: select username, age from user where id=1 => {"username": "hui", "age": 18}
            return cursor_result.mappings().one() or {}
        else:
            # 未指定列名查询默认全部字段，返回的是表实例对象 BaseOrmTable()
            # eg: select id, username, age from user where id=1 => UserTable(id=1, username="hui", age=18)
            if join_tables:
                # 连表还是返回 dict
                return cursor_result.mappings().one() or {}
            return cursor_result.scalar_one()

    @with_session
    async def query_all(
        self,
        *,
        cols: list = None,
        orm_table: BaseOrmTable = None,
        join_tables: list = None,
        conds: list = None,
        orders: list = None,
        flat: bool = False,
        limit: int = None,
        offset: int = None,
        session: AsyncSession = None,
    ) -> Union[List[dict], List[T_BaseOrmTable], Any]:
        """
        查询多行
        Args:
            cols: 查询的列表字段
            orm_table: orm表映射类
            join_tables: 连表信息[(table, conds, join_type)]
                eg: [(UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id, "left")]
            conds: 查询的条件列表
            orders: 排序列表
            flat: 单字段时扁平化处理
            limit: 限制数量大小
            offset: 偏移量
            session: 数据库会话对象，如果为 None，则通过装饰器在方法内部开启新的事务
        """
        cursor_result = await self._query(
            cols=cols,
            orm_table=orm_table,
            join_tables=join_tables,
            conds=conds,
            orders=orders,
            limit=limit,
            offset=offset,
            session=session,
        )
        if cols:
            if flat and len(cols) == 1:
                # 扁平化处理
                # eg: select id from user 从 [{"id": 1}, {"id": 2}, {"id": 3}] => [1, 2, 3]
                return cursor_result.scalars().all()

            # eg: select username, age from user => [{"username": "hui", "age": 18}, [{"username": "dbk", "age": 18}]]
            return cursor_result.mappings().all() or []
        else:
            # 未指定列名查询默认全部字段，
            if join_tables:
                # 连表查询还是返回 dict 列表
                return cursor_result.mappings().all() or []

            # 返回的是表实例对象 [BaseOrmTable()]
            # eg: select id, username, age from user
            # [User(id=1, username="hui", age=18), User(id=2, username="dbk", age=18)
            return cursor_result.scalars().all()

    async def list_page(
        self,
        cols: list = None,
        orm_table: BaseOrmTable = None,
        join_tables: list = None,
        conds: list = None,
        orders: list = None,
        curr_page: int = 1,
        page_size: int = 20,
        session: AsyncSession = None,
    ):
        """
        单表通用分页查询
        Args:
            cols: 查询的列表字段
            orm_table: orm表映射类
            join_tables: 连表信息[(table, conds, join_type)]
                eg: [(UserProjectMappingTable, ProjectTable.id == UserProjectMappingTable.project_id, "left")]
            conds: 查询的条件列表
            orders: 排序列表
            curr_page: 页码
            page_size: 每页数量
            session: 数据库会话对象，如果为 None，则通过装饰器在方法内部开启新的事务

        Returns: total_count, data_list
        """
        conds = conds or []
        orders = orders or []
        orm_table = orm_table or self.orm_table

        limit = page_size
        offset = (curr_page - 1) * page_size
        total_count, data_list = await asyncio.gather(
            self.query_one(
                cols=[func.count()],
                orm_table=orm_table,
                join_tables=join_tables,
                conds=conds,
                orders=orders,
                flat=True,
                session=session,
            ),
            self.query_all(
                cols=cols,
                orm_table=orm_table,
                join_tables=join_tables,
                conds=conds,
                orders=orders,
                limit=limit,
                offset=offset,
                session=session,
            ),
        )

        return total_count, data_list
