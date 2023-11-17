#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/09/07 17:01
import logging
import sys

from py_tools.logging import logger

from src.utils import context_util


def _logger_filter(record):
    """日志过滤器补充request_id或trace_id"""
    req_id = context_util.REQUEST_ID.get()
    trace_id = context_util.TRACE_ID.get()

    trace_msg = f"{req_id} | {trace_id}"
    record["trace_msg"] = trace_msg
    return record


def setup_logging(logging_conf: dict, console_log_level=logging.DEBUG):
    """
    配置项目日志信息
    Args:
        logging_conf: 项目日志配置
        console_log_level: 控制台日志级别，默认DEBUG
    """
    logger.remove()
    logger.add(sys.stdout, level=console_log_level)
    for log_handler, log_conf in logging_conf.items():
        log_file = log_conf.pop("file", None)
        log_conf["filter"] = _logger_filter
        logger.add(log_file, **log_conf)
    logger.info("setup logging success")
