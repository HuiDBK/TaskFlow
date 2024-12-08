#!/bin/bash

# 创建目录（如果不存在）
mkdir -p /opt/hui/projects/TaskFlow/data/mysql/{conf,data,log}
mkdir -p /opt/hui/projects/TaskFlow/data/nginx/{conf,data,log}
mkdir -p /opt/hui/projects/TaskFlow/{settings,logs}


# 定义源文件路径和目标文件路径
mysql_src_file="conf/mysql.cnf"
mysql_tgt_file="/opt/hui/projects/TaskFlow/data/mysql/conf/mysql.cnf"

nginx_src_file="conf/nginx.conf"
nginx_tgt_file="/opt/hui/projects/TaskFlow/data/nginx/conf/nginx.conf"

# 将源文件内容写入目标文件
cat "$mysql_src_file" > "$mysql_tgt_file"
cat "$nginx_src_file" > "$nginx_tgt_file"

# 将settings挂载到目标目录
cp -r src/settings /opt/hui/projects/TaskFlow

# 前端打包后文件放到nginx中
cp -r res/front_dist /opt/hui/projects/TaskFlow/data/nginx/data

# 启动 Docker Compose
docker-compose up -d
