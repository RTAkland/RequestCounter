#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/26
# @File Name: MySQL.py


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tables import *  # 导入所有的主题表模型
from typing import List, Tuple

Base = declarative_base()


class MySQL:
    """使用SQLAlchemy进行的MySQL数据库操作"""

    @property
    def session(self):
        """
        创建会话
        :return:
        """
        return self.Session()

    def __init__(self,
                 host: str,
                 user: str,
                 pwd: str,
                 database: str,
                 charset: str = 'utf8',
                 port: int = 3306
                 ) -> None:
        """
        初始化
        :param host: 数据库地址
        :param port: 数据库端口默认3306
        :param user: 用户名
        :param pwd: 登陆密码
        :param database: 数据库名
        :param charset: 字符集 默认utf8
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = pwd
        self.database = database
        self.charset = charset
        self.engine = create_engine(
            f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')  # 连接到数据库
        self.Session = sessionmaker(bind=self.engine)  # 创建引擎

    def __del__(self):
        """
        自动提交
        自动关闭连接
        :return:
        """
        self.session.commit()
        self.session.close()

    def insert(self, name: str, times: int = 0) -> bool:
        """
        插入数据
        :param name: 名称
        :param times: 次数 默认0
        :return:
        """
        new_data = ReqCount(name=name, times=times)
        self.session.add(new_data)
        self.session.commit()
        return True

    def update(self, name: str, times: int) -> bool:
        """
        更新数据
        :param name: 名称
        :param times: 次数
        :return:
        """
        self.session.query(ReqCount).filter(ReqCount.name == name).update({'name': name, 'times': times})
        return True

    def delete(self, name: str) -> bool:
        """
        删除数据
        :param name: 名称
        :return:
        """
        self.session.query(ReqCount).filter(ReqCount.name == name)
        return True

    def fetch(self, name: str) -> int:
        """
        查询数据
        :param name:
        :return:
        """
        data = self.session.query(ReqCount).filter(ReqCount.name == name).all()
        for i in data:
            print(i.times)

    def fetchall(self) -> List[Tuple]:
        """
        抓取全部数据
        :return:
        """
        data_list = []
        data = self.session.query(ReqCount).filter().all()
        for tup in data:
            data_list.append((tup.name, tup.times))

        return data_list

    def fetch_table(self, table_name: str) -> List[Tuple] or bool:
        """
        抓取指定名称的表
        :param table_name:
        :return:
        """
        table_list = []
        tables = self.session.query(eval(table_name)).filter().all()  # 使用eval函数将字符串转换为Python对象
        for tup in tables:
            table_list.append((tup.k, tup.v, tup.w, tup.h))
        return table_list
