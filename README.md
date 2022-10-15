# 新的项目仓库 https://github.com/MarkusJoe/Counter

<p align="center">
    <a href="https://github.com/MarkusJoe/FlaskRequestCounter">
        <img src="https://img.shields.io/badge/Python-3.10.x-blue.svg" alt="PythonVersion">
        <img src="https://img.shields.io/badge/LINCESE-Apache2.0-orange.svg" alt="LICENSE">
        <img src="https://img.shields.io/badge/Falsk-2.0.3-purple" alt="FlaskVersion">
    </a>
</p>

<div align="center">
    <img src="https://requestcounters.herokuapp.com/get?name=MarkusJoe" alt="Counter">
</div>

* 上方的计数器为不更新版本只保留了最基本的功能

## Python 版访问次数计数器 使用了flask 作为服务端接收请求

* [文档](https://request-counter-docs.vercel.app/#/)

### 开源

- 本项目以[Apache-2.0](./LICENSE)许可开源, 即:
    - 你可以直接使用该项目提供的功能, 无需任何授权
    - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 部署

> 在部署之前你需要先安装`python3.10.x`以上的版本

### 已部署好的地址

* [Click to enter](https://requestcounter.herokuapp.com/count/MarkusJoe)
* 默认主题: `lewd`

### 部署到Heroku

1. `fork` 本项目到你的仓库
2. 在[Heroku](https://www.heroku.com/) 注册账号
3. 在[Dashboard](https://dashboard.heroku.com/apps) 新建App
4. 流程: 进入网址 -> 点击右上角`New` -> 点击 `Create new app` -> 输入App名称 -> `Create app` -> 选择`Github` (登陆完成后) -> 点击`Search` ->
   选择你fork的项目并点击`Connect` -> 滑到末尾点击`Deploy branch`(如果你想在仓库更新时自动部署的话可以把`Enable Automatic Deploy`勾选) -> 等待完成
5. App的地址就是 `App名称` + `.herokuapp.com`

### 部署到本地服务器

```shell
$ git clone https://github.com/MarkusJoe/RequestCounter.git
$ cd RequestCounter
$ pip3 install -r requirements.txt
```

### 启动服务

```shell
$ python3 manage.py or gunicorn manage:app or waitress-serve --port=5000 manage:app
```

## 调用须知

- API支持`GET` 和 `POST` 方法请求
- 最大可以计数`10`位数, 超过则重置
- 可以自定义显示位数默认`7`位数最大`10`位
- 可以自己选择更多的主题只需要加上请求参数: `theme` 再加上想要的主题即可

# 一些信息

- 使用了Python3.6 的标准库`Sqlite3`进行数据库操作
- 你可以在`api`获取原始数据, 文档地址: [文档](https://markusjoe.github.io/RequestCounter/#/?id=api)
