#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 项目服务配置模块 }
# @Date: 2023/09/07 16:44
import logging

server_host = "127.0.0.1"
server_port = 8099
server_log_level = logging.WARNING
server_access_log = True

allow_origins = [
    # "*",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]
frontend_index_url = "http://127.0.0.1:5173/"
