#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/5
# @File Name: render_.py


from flask import render_template


def render_temp_(length: int, name: str, image_list: list, width: int, height: int) -> str:
    """
    代码很烂写到隐蔽的地方就看不见了
    :param height:
    :param width:
    :param length:
    :param name:
    :param image_list:
    :return:
    """
    position_list = []
    for i in range(0, length):
        position_list.append(i * width)
    file_name = f'index{length}.html'

    # 自己写的都看不下去了
    if length == 7:
        return render_template(file_name,
                               title=name,
                               g_width=length * width,
                               width=width,
                               height=height,
                               x_position_0=position_list[0],
                               x_position_1=position_list[1],
                               x_position_2=position_list[2],
                               x_position_3=position_list[3],
                               x_position_4=position_list[4],
                               x_position_5=position_list[5],
                               x_position_6=position_list[6],
                               svg_img_0=f'{image_list[0]}',
                               svg_img_1=f'{image_list[1]}',
                               svg_img_2=f'{image_list[2]}',
                               svg_img_3=f'{image_list[3]}',
                               svg_img_4=f'{image_list[4]}',
                               svg_img_5=f'{image_list[5]}',
                               svg_img_6=f'{image_list[6]}'
                               )
    elif length == 8:
        return render_template(file_name,
                               title=name,
                               g_width=length * width,
                               width=width,
                               height=height,
                               x_position_0=position_list[0],
                               x_position_1=position_list[1],
                               x_position_2=position_list[2],
                               x_position_3=position_list[3],
                               x_position_4=position_list[4],
                               x_position_5=position_list[5],
                               x_position_6=position_list[6],
                               x_position_7=position_list[7],
                               svg_img_0=f'{image_list[0]}',
                               svg_img_1=f'{image_list[1]}',
                               svg_img_2=f'{image_list[2]}',
                               svg_img_3=f'{image_list[3]}',
                               svg_img_4=f'{image_list[4]}',
                               svg_img_5=f'{image_list[5]}',
                               svg_img_6=f'{image_list[6]}',
                               svg_img_7=f'{image_list[7]}'
                               )
    elif length == 9:
        return render_template(file_name,
                               title=name,
                               g_width=length * width,
                               width=width,
                               height=height,
                               x_position_0=position_list[0],
                               x_position_1=position_list[1],
                               x_position_2=position_list[2],
                               x_position_3=position_list[3],
                               x_position_4=position_list[4],
                               x_position_5=position_list[5],
                               x_position_6=position_list[6],
                               x_position_7=position_list[7],
                               x_position_8=position_list[8],
                               svg_img_0=f'{image_list[0]}',
                               svg_img_1=f'{image_list[1]}',
                               svg_img_2=f'{image_list[2]}',
                               svg_img_3=f'{image_list[3]}',
                               svg_img_4=f'{image_list[4]}',
                               svg_img_5=f'{image_list[5]}',
                               svg_img_6=f'{image_list[6]}',
                               svg_img_7=f'{image_list[7]}',
                               svg_img_8=f'{image_list[8]}',
                               )
    elif length == 10:
        return render_template(file_name,
                               title=name,
                               g_width=length * width,
                               width=width,
                               height=height,
                               x_position_0=position_list[0],
                               x_position_1=position_list[1],
                               x_position_2=position_list[2],
                               x_position_3=position_list[3],
                               x_position_4=position_list[4],
                               x_position_5=position_list[5],
                               x_position_6=position_list[6],
                               x_position_7=position_list[7],
                               x_position_8=position_list[8],
                               x_position_9=position_list[9],
                               svg_img_0=f'{image_list[0]}',
                               svg_img_1=f'{image_list[1]}',
                               svg_img_2=f'{image_list[2]}',
                               svg_img_3=f'{image_list[3]}',
                               svg_img_4=f'{image_list[4]}',
                               svg_img_5=f'{image_list[5]}',
                               svg_img_6=f'{image_list[6]}',
                               svg_img_7=f'{image_list[7]}',
                               svg_img_8=f'{image_list[8]}',
                               svg_img_9=f'{image_list[9]}'
                               )
