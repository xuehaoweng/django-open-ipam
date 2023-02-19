# django-open-ipam

#### 介绍
#### 软件架构
软件架构说明
### 功能说明
django_open-ipam 第一版本
基本功能
- 支持地址在线分配
- 支持定时地址自动更新
- 支持定时地址回收

### 准备工作
- redis部署 
- celery-flower 部署
- 数据库新建django_open_ipam表
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


# OpenAxeIpam
## 自建OpenAxeIpam
- 基础模型和字段定义
- 原ipam数据导入
- ipam接口适配
 - 获取子网树结构
 - 根据子网获取地址使用详情
- 定制化
## 定制化admin 后台
 1.后台树结构
 2.后台矩阵展示使用状况
 3.后台运行定时任务
## 自动化任务
 1. 地址回收 回收IPAM中最后在线时间大于90天的IP地址，将其置为自定义空闲 暂未细分 √
 2. 定时修改特殊网段描述 为特殊的子网段添加描述，每天8:00 √
 3. 地址信息更新  IPAM地址全网更新main  根据现网中所有IP地址 Total_ip_list来进行地址更新 √
 
 ## 前端适配、功能验证
 1. ipv4、ipv6 地址展示适配
 2. 功能验证:地址分配、地址批量分配、地址回收、ipv6地址动态滚动刷新
 
 ![](https://cdn.staticaly.com/gh/xuehaoweng/netaxe-image@master/image.3uxeaoy3gn60.webp)