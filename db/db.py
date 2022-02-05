#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/4
# @File Name: db.py

import sqlite3

"""
使用python3自带的Sqlite3进行数据库操作
"""


def insert_data(name: str):
    """
    插入数据
    :param name:
    :return:
    """
    cursor.execute('insert into ReqCount values(?, ?)', (name, 1))
    conn.commit()


def fetch_data(name: str) -> int:
    """
    获取数据
    :param name:
    :return:
    """
    cursor.execute('select * from ReqCount')
    conn.commit()
    data = cursor.fetchall()

    # 将返回的元组转换为字典
    temp_dict = {}
    for k, v in data:
        temp_dict.setdefault(k, []).append(v)
    # 上方代码将元组转换为字典后字典的值会变成只有一个值的列表, 用下面两行代码去除
    for i, c in zip(temp_dict.keys(), temp_dict.values()):
        temp_dict[i] = c[0]

    if name in temp_dict.keys():
        count = temp_dict[name]  # 获取原数字 为 整型
        update_data(name, count)
        return count
    else:
        # 新建用户数据
        insert_data(name)
        return 0


def update_data(name: str, times: int):
    """
    更新数据
    :param name:
    :param times:
    :return:
    """
    times += 1
    cursor.execute('update ReqCount set times=? where name=?', (times, name))
    conn.commit()


if __name__ != '__main__':
    conn = sqlite3.connect('./db/data.db', check_same_thread=False)
    cursor = conn.cursor()
