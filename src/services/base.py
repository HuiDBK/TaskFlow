#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 通用逻辑 }
# @Date: 2023/08/29 16:46
from src.settings import auth_setting
from src.utils import context_util


class BaseService:
    @property
    def auth_settings(self):
        return auth_setting

    @property
    def current_user(self):
        return context_util.USER_CTX.get()
