#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 主入口模块 }
# @Date: 2023/08/29 12:13
import uvicorn
from src.server import app

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == '__main__':
    main()
