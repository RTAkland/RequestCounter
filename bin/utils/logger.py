#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2021/12/15
# @File Name: logger.py


import time
import logging.handlers
from logging import Logger
from colorlog import ColoredFormatter


class MakeLogger:
    def __init__(self) -> None:
        self.date_format = '%H:%M:%S'
        self.format_console = '%(log_color)s[%(asctime)s] |%(filename)s[%(lineno)-3s] |%(levelname)-8s |%(message)s'
        self.format_file = '[%(asctime)s] |%(filename)s[%(funcName)sline:%(lineno)d] |%(levelname)-8s |%(message)s'

    def setup_logger(self) -> Logger:
        """
        建立日志器
        :return:
        """
        formatter = ColoredFormatter(fmt=self.format_console,
                                     datefmt=self.date_format,
                                     reset=True,
                                     log_colors={
                                         'DEBUG': 'light_purple',
                                         'INFO': 'light_cyan',
                                         'WARNING': 'yellow',
                                         'ERROR': 'red',
                                         'CRITICAL': 'red,bold_red'})  # 定义终端输出颜色
        formatter_file = logging.Formatter(fmt=self.format_file,
                                           datefmt=self.date_format)  # 文件输入不使用颜色

        _logger = logging.getLogger('RequestCounter')  # 设置日志器名称
        _logger.setLevel(logging.DEBUG)  # 设置等级

        console_logger = logging.StreamHandler()  # 输出到终端
        console_logger.setFormatter(formatter)  # 设置输出格式化
        log_name = time.strftime('%Y-%m-%d %H')  # 一小时内使用的日志文件都是同一个
        file_logger = logging.handlers.RotatingFileHandler(filename=f'./bin/log/{log_name}.log',
                                                           maxBytes=102400,
                                                           backupCount=5,
                                                           encoding='utf-8')  # 每个日志文件最大102400字节(100Kb)
        file_logger.setFormatter(formatter_file)
        _logger.addHandler(console_logger)
        _logger.addHandler(file_logger)
        return _logger


if __name__ != '__main__':
    logger = MakeLogger().setup_logger()
