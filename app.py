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

app = Flask(__name__)


def is_new_user(name: str) -> str:
    """
    判断填入的参数是否为已有本地已有
    如果有则该名称值加一
    如果没有则新建一个
    :param name:
    :return:
    """
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
                return str(data[name])

            else:
                data[name] = 0  # 加用户
                return str(0)
        finally:
            with open('./static/data.json', 'w', encoding='utf-8') as dump:
                json.dump(data, dump)


def build_page(name: str) -> str:
    """
    渲染最终的页面
    :param name:
    :return:
    """
    count = is_new_user(name)

    if count == 0:  # 新id生成十个0
        return '0000000000'
    else:
        if len(str(count)) <= 10:
            zero_counter = 10 - len(str(count))
            final_number = '0' * zero_counter + str(count)
            return render_template('index.html',
                                   owner=name,
                                   b64_0=f'./static/number/{final_number[0]}.svg',
                                   b64_1=f'./static/number/{final_number[1]}.svg',
                                   b64_2=f'./static/number/{final_number[2]}.svg',
                                   b64_3=f'./static/number/{final_number[3]}.svg',
                                   b64_4=f'./static/number/{final_number[4]}.svg',
                                   b64_5=f'./static/number/{final_number[5]}.svg',
                                   b64_6=f'./static/number/{final_number[6]}.svg',
                                   b64_7=f'./static/number/{final_number[7]}.svg',
                                   b64_8=f'./static/number/{final_number[8]}.svg',
                                   b64_9=f'./static/number/{final_number[9]}.svg'
                                   )


def arg_not_be_full() -> Response:
    """
    参数不完整
    :return:
    """
    response = make_response('<h2 style="text-align: center">参数填写不完整 -> owner</h2>')
    response.status_code = 200
    return response


@app.route('/API', methods=['GET'])
def api_page() -> Response or str:
    """
     API页面主函数
    :return:
    """
    if request.method == 'GET':
        if 'owner' in request.args.keys():
            owner = request.args['owner']
            if owner != '':
                html_template = build_page(owner)
                response = make_response(html_template)
                response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
                return response
            else:
                return arg_not_be_full()
        else:
            arg_not_be_full()

    else:
        return 'Method Not Allowed'


@app.route('/', methods=['GET'])
def index():
    """
    索引页面
    :return:
    """
    if request.method == 'GET':
        return send_from_directory('./static', 'index.html')
    else:
        return 'Method Not Allowed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
