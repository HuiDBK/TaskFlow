#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Yuchen
# @Desc: { 心跳接口 }
# @Date: 2023/07/13 20:42
from src.utils import web


class HeartBeatController:
    @staticmethod
    async def heart():
        """心跳接口"""
        return web.success_api_resp()
