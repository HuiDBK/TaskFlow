#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Yuchen
# @Desc: { 心跳接口 }
# @Date: 2023/07/13 20:42
from loguru import logger

from src.data_models.api_models.base import SuccessRespModel


class HeartBeatController:
    mock_user_id = 0  # 模拟用户ID 用户区分不同的用户请求

    @classmethod
    async def heart_handler(cls):
        """模拟业务处理函数"""
        logger.info(f"user {cls.mock_user_id} heart_handler")
        return SuccessRespModel()

    @classmethod
    async def heart(cls):
        """心跳接口"""
        cls.mock_user_id += 1
        logger.info(f"user {cls.mock_user_id} ping request_id test")
        resp = await cls.heart_handler()
        return resp
