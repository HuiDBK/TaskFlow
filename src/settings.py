#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 配置文件 }
# @Date: 2023/08/29 13:54
import uvicorn
from src.server import app

uvicorn.run(app, host="127.0.0.1", port=8000)

mysql_host = "127.0.0.1"
mysql_port = "3306"
mysql_user = "root"
mysql_password = "56qwertyuiop"
mysql_charset = "utf8mb4"