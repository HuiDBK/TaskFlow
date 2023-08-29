|-- task_manage_system

    |-- docs:  项目文档
    |-- logs:  项目日志
    |-- src:   源代码
         |-- data_models:  数据模型
             |-- api_models:       接口出入参校验模型
             |-- logic_models:     业务数据模型
         |-- constants:    常量模块
             |-- enums:     枚举模块
         |-- dao:          数据访问层，例如mysql
         |-- controllers:  控制层，调用services 
         |-- routers:      路由层，调用handlers
         |-- logics:       逻辑层，业务逻辑
             |-- user:      用户模块 
             |-- project:   项目模块
             |-- task:      任务模块
             |-- tag:       标签模块
         |-- utils:        常用工具
         |-- server.py:    服务入口
         |-- settings.py:  配置文件
    |-- tests: 单元测试用例
    |-- .pre-commit-config.yaml: 代码格式规范
    |-- CHANGELOG.md        版本日志
    |-- requirements.txt    依赖文件
    |-- README.md           项目说明文档
    |-- main.py             项目主入口模块