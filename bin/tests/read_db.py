#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/18
# @File Name: read_db.py


# import sqlite3
#
#
# conn = sqlite3.connect('../../db/style.db')
# cursor = conn.cursor()
# cursor.execute('drop table dollstuffing')


import requests
import threading
from bs4 import BeautifulSoup

saved = ['gelbooru', 'moebooru', 'g', 'cripple', 'blacked', 'rule34', 'steambanner', 'lefty', 'crewbooru', 'sthg',
         'rfck', 'lisu', 'tv', 'lewd', 'amibooru', 'blankatlas', 'mmballbusting', 'sss', 'legolamb', 'goldengator',
         'r6gdrawfriends', 'vivi', 'twifanartsfw', 'hololive', 'vglobby', 'jaypee', 'melanin', 'orb', 'min', 'mjg',
         'cloppers', 'townofgravityfalls', 'brown', 'enacdoa', 'daifuku', 'osc', 'girlsfeet', 'hybreedsgeneral', 'sr',
         'mono', 'riskofrain', 'neovb', 'ffsr']


def req(name):
    print(name)
    resp = requests.get(f'http://127.0.0.1:5000/get?name=sdsa&theme={name}')
    soup = BeautifulSoup(resp.text, 'html.parser').findAll('image')
    for i in soup:
        with open(f'{name}.txt', 'w') as fp:
            fp.write(f'{i}\n')


for i in saved:
    a = threading.Thread(target=req, args=(i,))
    a.start()
    a.join()
