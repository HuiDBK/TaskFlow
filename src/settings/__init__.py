#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 项目配置包初始化 }
# @Date: 2023/09/07 16:38
from .base_setting import server_host, server_log_level, server_port
from .db_setting import (
    mysql_host, mysql_port, mysql_user, mysql_password, mysql_dbname,
    redis_db, redis_host, redis_password, redis_port,
)
from .log_setting import logging_conf
