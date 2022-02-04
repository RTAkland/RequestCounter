#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


import time
from flask import Flask
from flask import request
from flask import Response
from flask import make_response
from flask import render_template
from flask import send_from_directory
from bin.b64img import re_sort_number_image
from db.db import (
    fetch_data,
    update_data
)

app = Flask(__name__)


def is_new_user(name: str):
    """
    判断名称是否在数据库内
    如果在则将该名称的值加1
    如果不在数据库内则新加此名称到数据库
    :param name:
    :return:
    """
    """fetch_data 函数返回的是当前名称下访问次数的数值 为整型"""
    count = fetch_data(name)
    if count == 0:
        return [True, 0]
    elif len(str(count)) <= 10:
        return [True, count]
    else:
        update_data(name, 0)
        return [False, 0]


def build_page(name: str) -> Response or str:
    """
    渲染最终的页面
    :param name:
    :return:
    """
    status, count = is_new_user(name)
    if status:
        """
        计算出要在数字前加上几个0, 其实就是10减去数字位数
        假如当前访问数字是300, 先将整形转换为字符串, 再使用len()计算出长度
        使用10 - 去长度, 剩下的结果就是要在前面加上几个0
        """
        zero_counter = 10 - len(str(count))
        if count != 0:  # 不是新名称时直接计算要添加几个零
            final_number = '0' * zero_counter + str(count)  # 拼接
        else:  # 是新名称直接设置为10个零
            final_number = '0000000000'
        sorted_image = re_sort_number_image(final_number)
        return render_template('index.html',
                               title=name,
                               svg_img_0=f'{sorted_image[0]}',
                               svg_img_1=f'{sorted_image[1]}',
                               svg_img_2=f'{sorted_image[2]}',
                               svg_img_3=f'{sorted_image[3]}',
                               svg_img_4=f'{sorted_image[4]}',
                               svg_img_5=f'{sorted_image[5]}',
                               svg_img_6=f'{sorted_image[6]}',
                               svg_img_7=f'{sorted_image[7]}',
                               svg_img_8=f'{sorted_image[8]}',
                               svg_img_9=f'{sorted_image[9]}'
                               )  # 渲染模板
    else:
        return 'LONG'


def too_long_to_count() -> Response:
    """
    数值太长显示此页面
    :return:
    """
    response = make_response({'code': 200,
                              'message': '当前数值超过了最大可计数范围(10位)已将此名称的数据重置'})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def arg_not_be_full() -> Response:
    """
    参数不完整
    :return:
    """
    response = make_response({'code': 200,
                              'message': '参数填写不完整',
                              'timestamp': time.time()})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


@app.route('/API', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def api_page() -> Response or str:
    """
    API 页面函数
    :return:
    """
    if 'name' in request.args:
        name = request.args['name']
        if name != '':  # 数据为空返回参数不完整界面
            resp = build_page(name)
            if resp != 'LONG':
                response = make_response(resp)
                response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
                response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
                response.headers['date'] = time.ctime()
                return response
            else:
                return too_long_to_count()
        else:
            return arg_not_be_full()
    else:
        return arg_not_be_full()


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    索引页面
    :return:
    """
    return send_from_directory('./static', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
