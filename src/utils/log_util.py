#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 日志工具模块 }
# @Date: 2023/09/07 17:01

from py_tools.logging import setup_logging

from src.settings import log_setting
from src.utils import TraceUtil


def _logger_filter(record):
    """日志过滤器补充request_id或trace_id"""
    req_id = TraceUtil.get_req_id()
    trace_id = TraceUtil.get_trace_id()

    trace_msg = f"{req_id} | {trace_id}"
    record["trace_msg"] = trace_msg
    return record


def setup_logger():
    """配置项目日志信息"""
    setup_logging(
        log_dir=log_setting.logging_dir,
        log_filter=_logger_filter,
        log_format=log_setting.log_format,
        console_log_level=log_setting.console_log_level,
        log_retention=log_setting.server_logging_retention,
        log_rotation=log_setting.server_logging_rotation,
    )
