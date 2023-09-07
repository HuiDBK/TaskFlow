#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { DAO层初始化模块 }
# @Date: 2023/08/29 16:56
import asyncio

from py_tools.connections.db.mysql import DBManager, SQLAlchemyManager

from src import settings


async def init_orm():
    """初始化"""
    db_client = SQLAlchemyManager(
        host=settings.mysql_host,
        port=settings.mysql_port,
        user=settings.mysql_user,
        password=settings.mysql_password,
        db_name=settings.mysql_dbname,
    )
    db_client.init_mysql_engine()
    DBManager.init_db_client(db_client)
    return db_client
