#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: manage.py


from app import create_app

app = create_app('default')

if __name__ == '__main__':
    from app import logger
    from gevent import pywsgi

    logger.info('服务运行在 http://127.0.0.1:5000')
    try:
        server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info('已退出')
    except OSError:
        logger.critical('5000 端口已被占用')
        exit(1)
