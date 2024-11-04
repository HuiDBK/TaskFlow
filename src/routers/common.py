#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: 2023/09/07 17:48
from src.controllers.common import FileUploadController, HeartBeatController
from src.data_models.api_models import common_api
from src.data_models.api_models.base import SuccessRespModel
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()

router.add_api_route(
    "/files/upload",
    endpoint=FileUploadController.upload_file,
    response_model=common_api.UploadFileOut,
    methods=["post"],
    summary="单文件上传",
)

router.add_api_route(
    "/files/upload/batch",
    endpoint=FileUploadController.batch_upload_file,
    methods=["post"],
    response_model=common_api.BatchUploadFileOut,
    summary="多文件上传",
)

router.add_api_route(
    "/ping",
    endpoint=HeartBeatController.heart,
    methods=["get"],
    response_model=SuccessRespModel,
    summary="心跳",
)
