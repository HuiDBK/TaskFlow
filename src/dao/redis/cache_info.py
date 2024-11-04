#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { redis缓存信息 }
# @Date: 2022/10/31 22:00
from datetime import timedelta
from typing import Union

from py_tools.enums.pub_biz import RedisTypeEnum


class RedisCacheInfo(object):
    """统一缓存信息类"""

    def __init__(self, key, timeout: Union[int, timedelta] = timedelta(seconds=60), data_type=RedisTypeEnum.String):
        """
        缓存信息类初始化
        Args:
            key: 缓存的key
            timeout: 缓存过期时间, 单位秒
            data_type: 缓存采用的数据结构 (不传并不影响，用于标记业务采用的是什么数据结构)
        """
        self.key = key
        self.timeout = timeout
        self.data_type = data_type

    def __str__(self):
        return f"cache key {self.key} timeout {self.timeout}s"


class RedisKey(object):
    """Redis Key 统一管理"""

    prefix_key = "tf"
