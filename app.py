#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


import json
from flask import Flask
from flask import request
from flask import Response
from flask import make_response
from flask import render_template
from flask import send_from_directory
from bin.b64img import re_sort_number_image

app = Flask(__name__)


def is_new_user(name: str, reset: bool = False) -> int:
    """
    判断填入的参数是否为已有本地已有
    如果有则该名称值加一
    如果没有则新建一个
    :param reset:
    :param name:
    :return:
    """
    if not reset:
        with open('./static/data.json', 'r', encoding='utf-8') as fp:
            try:
                data = json.load(fp)
            except json.decoder.JSONDecodeError:
                with open('./static/data.json', 'w', encoding='utf-8') as init_fp:
                    json.dump({}, init_fp)
            all_user = data.keys()
            try:
                if name in all_user:  # 加次数
                    data[name] += 1
                    return data[name]

                else:
                    data[name] = 0  # 新加名称
                    return 0
            finally:
                with open('./static/data.json', 'w', encoding='utf-8') as dump:
                    json.dump(data, dump)
    else:
        with open('./static/data.json', 'r', encoding='utf-8') as reset_fp:
            data = json.load(reset_fp)
            data[name] = 0  # 重置该名称的值
            with open('./static/data.json', 'w', encoding='utf-8') as reset_dump:
                json.dump(data, reset_dump)


def build_page(name: str) -> str:
    """
    渲染最终的页面
    :param name:
    :return:
    """
    count = is_new_user(name)
    if len(str(count)) <= 10:
        """
        计算出要在数字前加上几个0, 其实就是10减去数字位数
        假如当前访问数字是300, 先将整形转换为字符串, 再使用len()计算出长度
        使用10 - 去长度, 剩下的结果就是要在前面加上几个0
        """
        zero_counter = 10 - len(str(count))
        if count != 0:
            final_number = '0' * zero_counter + str(count)  # 拼接
        else:
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
        is_new_user(name, reset=True)
        return render_template('long.html',
                               title=name)


def arg_not_be_full() -> Response:
    """
    参数不完整
    :return:
    """
    response = make_response({'code': 200,
                              'message': 'Incomplete parameters'})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


@app.route('/API', methods=['GET', 'POST'])
def api_page() -> Response or str:
    """
     API页面主函数
    :return:
    """
    if 'name' in request.args:
        name = request.args['name']
        if name != '':
            resp = build_page(name)
            response = make_response(resp)
            response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
            return response

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
