from fastapi import FastAPI
from py_tools.logging import logger

from src import dao, settings
from src.controllers.common.error_handler import register_exception_handler
from src.middlewares import register_middlewares
from src.routers import api_router
from src.utils import log_util

app = FastAPI(
    description="任务管理系统",
    middleware=register_middlewares(),  # 注册web中间件
    exception_handlers=register_exception_handler(),  # 注册web错误处理
)


async def init_setup():
    """初始化项目配置"""

    log_util.setup_logging(settings.logging_conf)

    await dao.init_orm()
    await dao.init_redis()


@app.on_event("startup")
async def startup_event():
    """项目启动时准备环境"""

    await init_setup()

    # 加载路由
    app.include_router(api_router, prefix="/api")

    logger.info("fastapi startup success")


@app.on_event("shutdown")
async def shutdown_event():
    logger.error("app shutdown")
