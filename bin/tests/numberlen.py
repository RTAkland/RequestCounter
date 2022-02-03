#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: numberlen.py


number = 1576451745

if len(str(number)) <= 10:
    zero_count = 10 - len(str(number))
    final_str = '0' * zero_count + str(number)
    print(final_str[9])
else:
    print('Too much to count')