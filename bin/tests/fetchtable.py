#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/26
# @File Name: fetchtable.py


import sqlite3

conn = sqlite3.connect('../db/data.db')
cursor = conn.cursor()
cursor.execute('select * from sqlite_master where type="table"')
tables = []
for i in cursor.fetchall():
    tables.append(i[1])

print(tables)
