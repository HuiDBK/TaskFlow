#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 日志配置模块 }
# @Date: 2023/09/07 16:46
import logging
import os

# 项目基准路径
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 项目日志目录
logging_dir = os.path.join(base_dir, "logs/")

# 项目日志配置
console_log_level = logging.DEBUG
log_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | {trace_msg} | {name}:{function}:{line} - {message}"

# 项目服务综合日志滚动配置（每天 0 点新创建一个 log 文件）
# 错误日志 超过10 MB就自动新建文件扩充
server_logging_rotation = "00:00"
error_logging_rotation = "10 MB"

# 服务综合日志文件最长保留 7 天，错误日志 30 天
server_logging_retention = "7 days"
error_logging_retention = "30 days"
