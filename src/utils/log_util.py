#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/09/07 17:01
from py_tools.logging import logger


def setup_logging(logging_conf: dict):
    """
    配置项目日志信息
    Args:
        logging_conf: 项目日志配置
    """
    for log_handler, log_conf in logging_conf.items():
        log_file = log_conf.pop("file", None)
        logger.add(log_file, **log_conf)
    logger.info("setup logging success")
