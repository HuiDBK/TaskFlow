#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 通用逻辑 }
# @Date: 2023/08/29 16:46
from src.settings import auth_setting
from src.utils.context_util import ContextMixin


class BaseService(ContextMixin):
    @property
    def auth_settings(self):
        return auth_setting
