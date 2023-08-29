#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zxq
# @Desc: { 公共模型 }
# @Date: 2023/08/29 14:28


from enum import Enum


class BaseEnum(Enum):
    # 枚举基类

    @classmethod
    def get_member_values(cls):
        return [item.value for item in cls._member_map_.values()]

    @classmethod
    def get_member_names(cls):
        return [name for name in cls._member_names_]


class StrEnum(str, BaseEnum):
    # 字符串枚举

    pass


class IntEnum(int, BaseEnum):
    # 整型枚举
    pass


class ImageFormatEnum(StrEnum):
    """支持的图片文件格式枚举"""

    JPG = ".jpg"
    JPEG = ".jpeg"
    PNG = ".png"


class ImageTypeEnum(StrEnum):
    """图片类型枚举"""

    File = "file"
    Base64Str = "str"