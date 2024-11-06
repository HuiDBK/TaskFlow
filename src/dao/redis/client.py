#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { redis 客户端模块 }
# @Date: 2023/07/10 21:23
from py_tools.connections.db.redis_client import BaseRedisManager

from src.dao.redis.cache_info import RedisCacheInfo


class RedisManager(BaseRedisManager):
    @classmethod
    async def set_with_cache_info(cls, redis_cache_info: RedisCacheInfo, value):
        """
        根据 RedisCacheInfo 设置 Redis 缓存
        :param redis_cache_info: RedisCacheInfo缓存信息对象
        :param value: 缓存的值
        :return:
        """
        await cls.client.setex(redis_cache_info.key, redis_cache_info.timeout, value)

    @classmethod
    async def get_with_cache_info(cls, redis_cache_info: RedisCacheInfo):
        """
        根据 RedisCacheInfo 获取 Redis 缓存
        :param redis_cache_info: RedisCacheInfo 缓存信息对象
        :return:
        """
        cache_info = await cls.client.get(redis_cache_info.key)
        return cache_info

    @classmethod
    async def del_with_cache_info(cls, redis_cache_info: RedisCacheInfo):
        """
        根据 RedisCacheInfo 删除 Redis 缓存
        :param redis_cache_info: RedisCacheInfo缓存信息对象
        :return:
        """
        await cls.client.delete(redis_cache_info.key)
