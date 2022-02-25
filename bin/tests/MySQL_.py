#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/25
# @File Name: MySQL_.py


import pymysql


class MySQL:
    """操作MySQL数据库"""

    def __init__(self,
                 host: str,
                 user: str,
                 password: str,
                 database: str,
                 charset: str = 'utf8',
                 port: int = 3306
                 ) -> None:
        """
        初始化类
        :param host: 数据库地址
        :param user: 数据库用户
        :param password: 数据库密码
        :param database: 数据库名称
        :param charset: 字符集 默认utf8
        :param port: 端口地址
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        # self.__create_database()  # 自动创建数据库

    def __create_database(self) -> bool:
        """
        创建数据库
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   local_infile=True,
                                   charset=self.charset)
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS %(db)s DEFAULT CHARSET utf8;' % {'db': self.database})
            conn.commit()
            return True
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def __import_database(self):
        """
        导入本地数据库
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   local_infile=True,
                                   charset=self.charset)
            cursor = conn.cursor()
            cursor.execute(f'use {self.database};')
            cursor.execute(f'source ./static/cache/db.sql;')
            conn.commit()
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def insert(self, name: str) -> bool:
        """
        新增数据
        :param name: 名称
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            cursor = conn.cursor()
            cursor.execute(
                'insert into reqcount (name, times) values("%(name)s", 0);' % {'name': name})
            conn.commit()
            return True
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def update(self, name: str, times: int) -> bool:
        """
        更新数据
        :param name: 名称
        :param times: 次数
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            cursor = conn.cursor()
            cursor.execute(
                'insert into reqcount (name, times) values("%(name)s", %(times)s);' % {'name': name, 'times': times})
            conn.commit()
            return True
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def delete(self, name: str) -> bool:
        """
        删除数据
        :param name: 名称
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            cursor = conn.cursor()
            cursor.execute('delete from reqcount where name"=%(name)s"' % {'name': name})
            conn.commit()
            return True
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def fetch(self, name: str, fetchall: bool = False):
        """
        抓取数据
        :param fetchall: 是否抓取全部
        :param name: 名称
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            cursor = conn.cursor()
            if not fetchall:
                cursor.execute('select * from reqcount where name="%(name)s"' % {'name': name})
                return cursor.fetchall()
            else:
                cursor.execute('select * from reqcount')
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()

    def fetch_table(self, table_name: str, fetchall: bool = False):
        """
        抓取已有表名称
        :param table_name:
        :param fetchall: 是否抓取全部
        :return:
        """
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset)
            cursor = conn.cursor()
            if not fetchall:
                cursor.execute('select * from reqcount where name="%(name)s"' % {'name': table_name})
                return cursor.fetchall()
            else:
                cursor.execute('select * from reqcount')
        except pymysql.err.OperationalError:
            print(f'无法连接到数据库: {self.database}')
            return False
        finally:
            cursor.close()
            conn.close()
