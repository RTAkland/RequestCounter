#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/4
# @File Name: sqlite.py

import sqlite3
from typing import Any


def insert_data(name: str) -> None:
    """
    插入数据
    :param name:
    :return:
    """
    conn = sqlite3.connect('./bin/db/count.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute('insert into ReqCount values(?, ?)', (name, 1))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def fetch_data(name: str) -> int:
    """
    获取数据
    :param name:
    :return:
    """
    conn = sqlite3.connect('./bin/db/count.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute('select * from ReqCount')
        conn.commit()
        data = cursor.fetchall()

        temp_dict = {}
        for k, v in data:  # 遍历数据将元组数据转换为字典类型
            temp_dict.setdefault(k, []).append(v)
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
    finally:
        cursor.close()
        conn.close()


def update_data(name: str, times: int) -> None:
    """
    更新数据
    :param name:
    :param times:
    :return:
    """
    conn = sqlite3.connect('./bin/db/count.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        times += 1
        cursor.execute('update ReqCount set times=? where name=?', (times, name))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def fetch_table() -> list:
    """
    返回已有主题列表
    :return:
    """
    conn_temp = sqlite3.connect('./bin/db/style.db', check_same_thread=False)
    cursor_temp = conn_temp.cursor()
    try:
        lst = []
        cursor_temp.execute("select * from sqlite_master where type='table'")
        for i in cursor_temp.fetchall():
            lst.append(i[1])
        return lst
    finally:
        cursor_temp.close()
        conn_temp.close()


def fetch_style_data(style: str) -> list[dict[str, Any]]:
    """
    获取主题数据库内的数据
    :param style:
    :return:
    """
    conn = sqlite3.connect('./bin/db/style.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute('select * from %(style_name)s' % {'style_name': style})
        data = cursor.fetchall()
        data_set = []
        for i in data:
            data_set.append({'index': i[0], 'base64': i[1], 'width': i[2], 'height': i[3]})
        return data_set
    finally:
        cursor.close()
        conn.close()


__all__ = ['fetch_table', 'fetch_data', 'fetch_style_data', 'update_data', 'insert_data']