# 这里是Request Counter的文档

> 虽然说项目很小根本不需要文档

# 资源来源

* 数据库内的`base64`图片来自`booru`

# 工作原理

> Flask 建立服务器来接收请求并返回对应的响应体

# 部署

> 在部署之前你需要先安装`python3.10.x`以上的版本

## 部署到本地服务器

 ```shell
 $ git clone https://github.com/MarkusJoe/RequestCounter.git
 $ cd RequestCounter
 $ pip3 install -r requirements.txt
 $ python3 app.py 
 ```

# 普通接口

## `/count/` 接口

> 此接口为基本接口请求此接口可以获取`svg矢量图`的响应体

> 必选参数: `name`: `str` 可选参数: `length`: `int` ; `theme`: `str`

### 调用示例

```shell
$ curl -L -X https://requestcounter.herokuapp.com/count/main/
```

```json
<...>
```

# API

* 注意事项

1. `/api/v1/`内的接口需要`key`来访问的有: `/export/`
2. `key`是从环境变量中获取或自动生成, 这取决与你部署到`Heroku`时是否设置了`ACCESS_KEY`环境变量
3. `key`的长度为`32`位的随机英文字母大小写字符串

> 地址前缀: `/api/v1/`

- 接口地址: `/overall/`, `/query/`, `/theme/`
- 请求方法: `GET` `POST`

## `/overall/` 接口

> 使用此接口获取数据库中所有的数据

> 必选参数: `limit: int` > 自定义查询数量, 输入的数字大于等于最大值时, 将返回最大值

### 调用示例

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/overall/?limit=20&key=<key>
```

```json
{
  "code": 200,
  "msg": "Success. Total: 7 row(s)",
  "data": [
    {
      "name": "sda",
      "times": 72
    },
    {
      "name": "main",
      "times": 59
    }
  ]
}
```

## `/query/` 接口

> 使用此接口获取数据库中指定的数据

***使用此接口查询的名称计数数值会加一***

> 必选参数: `name: str`  > 查询指定名称的计数数据

> 可选参数: `nochange: Any`

> `nochange`: 'Any` > 将参数值设置为任意值则仅查询不增加

### 调用示例

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/query/?name=main&nochange=1&key=<key>
```

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    "main",
    59
  ]
}
```

## `/theme/` 接口

> 使用此接口获取数据库内原始的base64编码的主题图片

> 必选参数: `theme: str`

### 调用示例

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/theme/?name=lewd&key=<key>
```

```json

{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "index": "0",
      "base64": "...",
      "width": 45,
      "height": 100
    },
    ...
  ]
}
```

## `/alltables/` 接口

> 此接口可以获取数据库内所有的表名  > 返回的数据中不包含`ReqCount`

> 无参数

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/alltables/&key=<key>
```

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    ...
  ]
}
```

## `/export/` 接口

> 此接口可以导出应用的数据库文件

> 无参数

### 调用示例

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/export/&key=<key>
```

> 该接口请求成功后返回文件

## `/test`接口

> 此接口仅用于测试 只能增加`test-example`名称的计数次数

> 无需`key`即可请求

### 调用示例

```shell
$ curl -L -X GET https://requestcounter.herokuapp.com/api/v1/test
```

```json
622
```

> 返回一个`int`数字

# 关于

## 开源

- 本项目以Apache-2.0许可开源, 即:
    - 你可以直接使用该项目提供的功能, 无需任何授权
    - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 关于此页面

此文档由 [docsify](https://github.com/docsifyjs/docsify) 生成. docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 .md 转成 .html
文件，所有转换工作都是在运行时进行。
 
