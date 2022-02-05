#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/5
# @File Name: t.py

import sqlite3


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('select * from ReqCount')
print(cursor.fetchall())
cursor.execute('update ReqCount set times=99999998 where name="MarkusJoe"')
conn.commit()