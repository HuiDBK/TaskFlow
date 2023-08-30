from fastapi import FastAPI

from src.routers import api_router

app = FastAPI(description="任务管理系统")

# 加载路由
app.include_router(api_router)