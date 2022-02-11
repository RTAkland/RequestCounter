#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/11
# @File Name: get_all_theme.py


import random
import base64
import sqlite3


conn = sqlite3.connect('../assets/theme.db')
cursor = conn.cursor()


def get_all_theme():
    cursor.execute('select * from sqlite_master where type="table"')
    table_list = cursor.fetchall()
    table_name_list = []
    for i in table_list:
        table_name_list.append(i[1])

    for n in table_name_list:
        cursor.execute('select * from %(name)s' % {'name': n})
        for i in cursor.fetchall():
            img_data = base64.b64decode(i[1].replace('data:image/gif;base64,', ''))
            with open(str(random.randint(0, 9999)) + '.gif', 'wb') as fp:
                fp.write(img_data)
            # if i[1] == '':
            #     print(n)
get_all_theme()