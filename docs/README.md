# 这里是Request Counter的文档
> 虽然说项目很小根本不需要文档

# 灵感来源
[Moe-Counter](https://github.com/MarkusJoe/Moe-counter)
> 看到这个项目感觉挺有意思就用Python写了一个 此项目中添加了原项目中没有的功能 `Length` `设置长度`

# 工作原理
使用Flask建立服务器接收请求分析获取到的数据写入数据库

# 部署
> 在部署之前你需要先安装`python3.9.x`以上的版本 
## 部署到本地服务器
 ```shell
 $ git clone https://git@github.com:MarkusJoe/RequestCounter.git
 $ cd RequestCounter
 $ pip3 install -r requirements.txt
 $ python3 app.py 
 ```


# 基本信息
- Python版本: `3.9.9`
- 请求方法: `GET` `POST`
- 请求地址: `/API`
- 请求参数: `name` : `str`
  - 可选参数: `length` : `int`
  - 可选参数: `theme` : `str`
  

# 注意事项
- Python版能最新版就最新版
- 项目使用了标准库`Sqlite3`进行了数据库操作某些可以部署项目的服务器可能不支持例如`vercel`(可能是我不会)


# 快速响应
测试用代码如下
```python
import requests

for i in range(100):
    res = requests.get('http://127.0.0.1/API?name=2&length=10&theme=t2').elapsed.microseconds
    print(res)  # 返回响应速度 单位: 微秒
```
>在`AMD Athlon(tm) X4 830 Quad Core Processor 2.99 GHz` `4G` 内存的电脑上运行项目  
> 在本机上使用`Requests`库`GET`方法请求`100`次 (名称为`2`长度为`10`主题为`t2`)  
> 使用`elapsed.microseconds`属性 获取响应速度返回的值如下
<details>
单位: 微秒<br>
参考: 1秒(second)(s) = 1000毫秒(millisecond)(ms) = 1000000微秒(microseconds)(us)<br>
61764<br>
22125<br>
25059<br>
16524<br>
13396<br>
12787<br>
20579<br>
18987<br>
25500<br>
14910<br>
11303<br>
11787<br>
16949<br>
17094<br>
15264<br>
10934<br>
10526<br>
11943<br>
16967<br>
17205<br>
12887<br>
11386<br>
11547<br>
17743<br>
18625<br>
17208<br>
14763<br>
12858<br>
12708<br>
18598<br>
16879<br>
16216<br>
14655<br>
12089<br>
11588<br>
17287<br>
20115<br>
14403<br>
12857<br>
11596<br>
15006<br>
18246<br>
18013<br>
13623<br>
10673<br>
12064<br>
17838<br>
16651<br>
16483<br>
13522<br>
13231<br>
15624<br>
11043<br>
10765<br>
16317<br>
17200<br>
13250<br>
11230<br>
11533<br>
16727<br>
16781<br>
16253<br>
14658<br>
13762<br>
13194<br>
17700<br>
17933<br>
15686<br>
12051<br>
10904<br>
17163<br>
16591<br>
16464<br>
15271<br>
12405<br>
17173<br>
26737<br>
15964<br>
12363<br>
12653<br>
12893<br>
17524<br>
20084<br>
14165<br>
12037<br>
13427<br>
17245<br>
18652<br>
18438<br>
14811<br>
14233<br>
14555<br>
17998<br>
16949<br>
16445<br>
12120<br>
11695<br>
14257<br>
17557<br>
16587<br>
</details>
<br>

# 关于
## 开源
- 本项目以Apache-2.0许可开源, 即:
  - 你可以直接使用该项目提供的功能, 无需任何授权
  - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 关于此页面
此文档由 [docsify](https://github.com/docsifyjs/docsify) 生成. docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 .md 转成 .html 文件，所有转换工作都是在运行时进行。
 