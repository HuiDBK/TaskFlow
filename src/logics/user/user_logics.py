#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 用户模块逻辑 }
# @Date: 2023/08/29 16:43
from src.dao.orm.user import UserModel
from src.data_models.api_models import user


# 用户注册逻辑模块所引用的base模块还没写，所以先None
class UserRegisterLogics(None):

    async def create_User_Register(self,req_model: user.UserRegisterCreateIn):
        User_Register = await UserModel.create(**req_model.dict())
        resp_data = User_Register.to_dict(alias_dict={"id":"id"})
        return resp_data