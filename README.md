<p align="center">
    <a href="https://github.com/MarkusJoe/FlaskRequestCounter">
        <img src="https://img.shields.io/badge/Python-3.9.x-blue.svg" alt="PythonVersion">
        <img src="https://img.shields.io/badge/LINCESE-Apache2.0-orange.svg" alt="LICENSE">
        <img src="https://img.shields.io/badge/Falsk-2.0.2-purple" alt="FlaskVersion">
    </a>
</p>

## Python 版访问次数计数器使用了flask 作为服务端接收请求
## 借鉴于(仿制): [Moe Counter](https://github.com/journey-ad/Moe-counter)  (应该算借鉴吧) 作者:[journey-ad](https://github.com/journey-ad/Moe-counter/commits?author=journey-ad)

### 开源
- 本项目以[Apache-2.0](./LICENSE)许可开源, 即:
  - 你可以直接使用该项目提供的功能, 无需任何授权
  - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生
  
***示例:***
<details>

![LocalCounter](https://geminitay.pythonanywhere.com/API?name=main)

</details>

## 调用须知
- API支持`GET` 和 `POST` 方法请求
- 最大可以计数`10`位数, 超过则重置


# 一些信息
- 使用了Python3.6 的标准库`Sqlite3`进行数据库操作
- 开启时占用了`32Mb`的内存




