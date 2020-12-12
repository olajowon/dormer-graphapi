# 运行
## 开发运行
### 创建环境文件
	cd dormer-graphapi
	echo development > env

### 修改配置文件
    cd configure
    cp example.ini development.ini # 与env同名
    vim development.ini

### 创建日志目录
	mkdir /var/log/dormer-graphapi

### 启动服务
	uwsgi uwsgi.ini


## 生产运行
### 创建环境文件
	cd dormer-graphapi
	echo production > env

### 修改配置文件
    cd configure
    cp example.ini production.ini # 与env同名
    vim production.ini

### 创建日志目录
	mkdir /var/log/dormer-graphapi

### 启动、停止、重启服务
	python3 server.py start|stop|restart

