#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/27
# @File Name: MySQL_.py


import pymysql


class MySQL:
    """操作MySQL数据库"""

    def __init__(self,
                 host: str,
                 user: str,
                 pwd: str,
                 database: str
                 ) -> None:
        """
        初始化MySQL对象并创建一个连接
        创建的连接会在执行完毕后自动提交以及自动关闭
        :param host: 数据库地址
        :param user: 数据库用户名
        :param pwd: 数据库密码
        :param database: 数据库名
        """
        self.__host = host
        self.__user = user
        self.__password = pwd
        self.__database = database
        self.__conn = pymysql.connect(user=self.__user,
                                      password=self.__password,
                                      host=self.__host,
                                      database=self.__database)  # 创建连接
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        """
        自动提交
        自动关闭连接
        :return:
        """
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()

    @property
    def show_tables(self) -> list:
        """
        查询已有的表
        :return:
        """
        self.__cursor.execute('show tables;')  # 列出所有的表名
        tuple_tables = self.__cursor.fetchall()
        # 将元组类型转换为列表
        tables = []
        for origin in tuple_tables:
            tables.append(origin[0])
        del tuple_tables
        return tables

    def exists_name(self, name: str):
        """
        判断是否存在于数据库内
        :param name:
        :return:
        """
        status = self.fetch(name)
        if status == ():
            return False
        else:
            return True

    def exists_table(self, table: str) -> bool:
        """
        判断表是否在数据库内
        :param table:
        :return:
        """
        tables = self.show_tables
        if table in tables:
            return True
        else:
            return False

    def insert(self, name: str, times: int = 0) -> bool:
        """
        插入数据
        :param name:
        :param times:
        :return:
        """
        try:
            self.__cursor.execute(
                'insert into reqcount(name, times) values("%(name)s", %(times)s);' % {'name': name, 'times': times})
            return True
        except pymysql.err.IntegrityError:
            return False

    def delete(self, name: str) -> bool:
        """
        删除数据
        :param name:
        :return:
        """
        self.__cursor.execute('delete from reqcount where name="%(name)s";' % {'name': name})
        return True

    def fetch(self, name: str) -> bool or tuple:
        """
        抓取数据
        :param name:
        :return:
        """
        self.__cursor.execute('select * from reqcount where name="%(name)s";' % {'name': name})
        data = self.__cursor.fetchall()
        if data == ():
            return False
        else:
            return data[0]

    def update(self, name: str, times: int) -> bool:
        """
        更改数据
        :param name:
        :param times:
        :return:
        """
        self.__cursor.execute(
            'update reqcount set times="%(times)s where name="%(name)s"";' % {'times': times, 'name': name})
        return True

    def fetching_table(self, table: str) -> list:
        """
        抓取主题表内的数据
        :param table:
        :return:
        """
        self.__cursor.execute('select * from %(table)s' % {'table': table})
        datas = self.__cursor.fetchall()
        lst = []
        for i in datas:
            lst.append({'k': i[0],
                        'v': i[1],
                        'w': i[2],
                        'h': i[3]}
                       )  # 向空列表内添加抓取到的数据 -> 将元组数据转换为列表

        del datas
        return lst


__all__ = ['MySQL']