# 这里是Request Counter的文档

> 虽然说项目很小根本不需要文档

# 灵感来源

[Moe-Counter](https://github.com/journey-ad/Moe-counter)
> 看到这个项目感觉挺有意思就用Python写了一个 此项目中添加了原项目中没有的功能 `Length` `设置长度`

# 工作原理

使用Flask建立服务器接收请求分析获取到的数据写入数据库

# 部署

> 在部署之前你需要先安装`python3.10.x`以上的版本

## 部署到本地服务器

 ```shell
 $ git clone https://github.com/MarkusJoe/RequestCounter.git
 $ cd RequestCounter
 $ pip3 install -r requirements.txt
 $ python3 app.py 
 ```

# 基本信息

- Python版本: `3.10.x`
- 请求方法: `GET` `POST`
- 请求地址: `/count/<string:name>` or `/api/v1/<string:name>`
- 你需要在 请求地址末尾加入你需要使用的名称来进行计数
- 可选参数: `theme` `length`

# API
> 注意事项: ***调用接口必须在路径末尾加入 `/` (不是参数末尾)***

> 地址前缀: `/api/`

- 接口地址: `/overall/`, `/query/`, `/theme/`
- 请求方法: `GET` `POST`

## `/overall/` 接口

> 使用此接口获取数据库中所有的数据  
> 必选参数: `limit: int` > 自定义查询数量, 输入的数字大于等于最大值时, 将返回最大值

### 调用示例

```shell
$ curl -X GET https://requestcounter.herokuapp.com/api/overall/?limit=20
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
$ curl -X GET https://requestcounter.herokuapp.com/api/query/?name=main&nochange=1
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
$ curl -X GET https://requestcounter.herokuapp.com/api/theme/?name=lewd
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
$ curl -X GET https://requestcounter.herokuapp.com/api/alltables/
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

# 关于

## 开源

- 本项目以Apache-2.0许可开源, 即:
    - 你可以直接使用该项目提供的功能, 无需任何授权
    - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 关于此页面

此文档由 [docsify](https://github.com/docsifyjs/docsify) 生成. docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 .md 转成 .html
文件，所有转换工作都是在运行时进行。
 
