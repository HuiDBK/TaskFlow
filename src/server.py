from fastapi import FastAPI

from src import dao
from src.routers import api_router

app = FastAPI(description="任务管理系统")

# 加载路由
app.include_router(api_router)


async def init_setup():
    """初始化项目配置"""

    log_util.setup_logging()

    await dao.init_orm()
    await dao.init_redis()

    log_util.setup_tortoise_orm_logging_debug()


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

    # 关闭orm
    await Tortoise.close_connections()
