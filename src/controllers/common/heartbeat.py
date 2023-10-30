#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Yuchen
# @Desc: { 心跳接口 }
# @Date: 2023/07/13 20:42
from loguru import logger

from src.data_models.api_models.base import SuccessRespModel


class HeartBeatController:
    @staticmethod
    async def heart():
        """心跳接口"""
        logger.info("ping request_id test")
        return SuccessRespModel()
