#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/07/13 16:24
from typing import List

from fastapi import File, UploadFile


class FileUploadController:
    @staticmethod
    async def upload_file(file: UploadFile = File(..., description="上传的文件")):
        """单文件上传"""
        pass

    @staticmethod
    async def batch_upload_file(files: List[UploadFile] = File(..., description="上传的文件列表")):
        """批量文件上传"""
        pass
