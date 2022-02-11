# 这里是Request Counter的文档
> 虽然说项目很小根本不需要文档

# 灵感来源
[Moe-Counter](https://github.com/MarkusJoe/Moe-counter)
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
- 请求地址: `/get`
- 请求参数: `name` : `str`
  - 可选参数: `length` : `int`
  - 可选参数: `theme` : `str`
  

# 响应速度
* `flask` 服务端使用的是`同步`编程


# 关于
## 开源
- 本项目以Apache-2.0许可开源, 即:
  - 你可以直接使用该项目提供的功能, 无需任何授权
  - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 关于此页面
此文档由 [docsify](https://github.com/docsifyjs/docsify) 生成. docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 .md 转成 .html 文件，所有转换工作都是在运行时进行。
 
