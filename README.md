# netaxe-ipam

#### 介绍
#### 软件架构
软件架构说明
### 功能说明
netaxe-ipam 第一版本
基本功能
- 支持地址在线分配
- 支持定时地址自动更新
- 支持定时地址回收

### 准备工作
- redis部署 
- celery-flower 部署
- 数据库新建netaxe_ipam表
- nacos 部署
- docker\docker-compose 需要


1. 新建`ipam`数据库:数据迁移
2. 按需初始化数据(tags+users)
3. 注册`nacos`，前端页面调试
4. `ipam`管理页面`ip:38001`
5. 自动更新和自动回收任务配置(仅支持管理页面配置？)


## 测试环境
1. 启动redis
2. 启动celery-flower
3. 启动celery任务队列
4. 启动项目runserver即可
5. admin后台数据展示、任务运行等
