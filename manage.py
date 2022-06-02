#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: manage.py


import os
import unittest
from app import create_app

dyno = os.getenv('DYNO')
if dyno is not None:
    config = 'heroku'
else:
    config = os.getenv('FLASK_CONFIG') or 'default'

app = create_app(config)


@app.cli.command('test')
def tests_cli():
    all_test = unittest.TestLoader().discover('app/tests/')
    unittest.TextTestRunner(verbosity=2).run(all_test)


if __name__ == '__main__':
    from gevent import pywsgi

    app.logger.info('服务运行在 http://127.0.0.1:5000')
    try:
        server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
        server.serve_forever()
    except KeyboardInterrupt:
        app.logger.info('已退出')
    except OSError:
        app.logger.critical('5000 端口已被占用')
        exit(1)
