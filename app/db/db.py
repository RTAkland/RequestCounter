#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: db.py


import sqlite3
from typing import List


class SQLite:
    """操作SQLite数据库"""

    def __init__(self) -> None:
        """
        初始化SQLite对象
        完成后会自动提交, 自动关闭
        """
        self.__path = './app/db/data.db'
        self.__conn = sqlite3.connect(self.__path)
        self.__cursor = self.__conn.cursor()

    def __del__(self) -> None:
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
        列出所有在数据库内的表
        :return:
        """
        self.__cursor.execute('select * from sqlite_master where type="table"')
        tables = self.__cursor.fetchall()
        lst = []
        for table in tables:
            lst.append(table[1])
        del tables
        return lst

    def exists_name(self, name: str) -> bool:
        """
        判断当前名称是否在数据库内
        调用self.fetch()方法
        :param name:
        :return:
        """
        status = self.fetch(name, True)
        if not bool(status):
            return False
        else:
            return True

    def exists_table(self, table: str) -> bool:
        """
        判断表是否在数据库内
        调用self.fetching_table()方法
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
        self.__cursor.execute(
            'insert into reqcount (name, times) values("%(name)s", %(times)s)' % {'name': name, 'times': times})
        return True

    def delete(self, name: str) -> bool:
        """
        删除数据
        暂时不会用到此接口
        :param name:
        :return:
        """
        self.__cursor.execute('delete from reqcount where name="%(name)s"' % {'name': name})
        return True

    def fetch(self, name: str, is_check: bool = False) -> tuple:
        """
        抓取数据
        :param name:
        :param is_check:
        :return:
        """
        self.__cursor.execute('select * from reqcount where name="%(name)s"' % {'name': name})
        data = self.__cursor.fetchone()
        if not is_check:
            self.update(name, data[-1])
        return data

    def update(self, name: str, times: int) -> bool:
        """
        更新数据
        :param name:
        :param times:
        :return:
        """
        self.__cursor.execute(
            'update reqcount set times=%(times)s where name="%(name)s"' % {'times': times + 1, 'name': name})
        return True

    def fetching_table(self, table: str) -> List[dict]:
        """
        抓取主题表的数据
        :param table:
        :return:
        """
        status = self.exists_table(table)
        if status:
            tables = self.__cursor.execute('select * from %(table)s' % {'table': table})
            lst = []
            for data in tables:
                lst.append({'index': data[0],
                            'base64': data[1],
                            'width': data[2],
                            'height': data[3]})
            del tables
            return lst
        else:
            return []
