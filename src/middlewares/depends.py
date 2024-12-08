from fastapi import Depends, Request
from fastapi.security import HTTPBearer

from src.utils import context_util

security = HTTPBearer(auto_error=False)


async def get_token(authorization: str = Depends(security)) -> str:
    """获取token"""
    return authorization


async def set_request_ctx(request: Request) -> Request:
    """设置请求上下文"""
    context_util.REQUEST_CTX.set(request)
    return request


def register_depends():
    """注册全局依赖"""
    return [Depends(get_token), Depends(set_request_ctx)]
