from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer
from py_tools.logging import logger

from src import dao
from src.middlewares import register_middlewares
from src.middlewares.error_handler import register_exception_handler
from src.routers import api_router
from src.utils import TraceUtil, log_util


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()


security = HTTPBearer(auto_error=False)


async def get_token(authorization: str = Depends(security)) -> str:
    return authorization


app = FastAPI(
    description="任务管理系统",
    lifespan=lifespan,
    dependencies=[Depends(get_token)],
    middleware=register_middlewares(),  # 注册web中间件
    exception_handlers=register_exception_handler(),  # 注册web错误处理
)


async def init_setup():
    """初始化项目配置"""

    log_util.setup_logger()

    await dao.init_orm()
    # await dao.init_redis()


async def startup():
    """项目启动时准备环境"""
    TraceUtil.set_trace_id(title="app-server")

    await init_setup()

    # 加载路由
    app.include_router(api_router)

    logger.info("fastapi startup success")


async def shutdown():
    logger.error("app shutdown")
