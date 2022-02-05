#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/5
# @File Name: evaltest.py


cmd = """return ('index.html', title=name, svg_img_0=f'{sorted_image[0]}', svg_img_1=f'{sorted_image[1]}', svg_img_2=f'{sorted_image[2]}', svg_img_3=f'{sorted_image[3]}', svg_img_4=f'{sorted_image[4]}', svg_img_5=f'{sorted_image[5]}', svg_img_6=f'{sorted_image[6]}', svg_img_7=f'{sorted_image[7]}', svg_img_8=f'{sorted_image[8]}', svg_img_9=f'{sorted_image[9]}' )"""

print(eval(cmd))