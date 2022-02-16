#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2021/12/15
# @File Name: logger.py


import time
import logging.handlers
from colorlog import ColoredFormatter


class Logger:
    def __init__(self):
        self.date_format = '%H:%M:%S'
        self.info_format_console = '%(log_color)s[%(asctime)s] |%(filename)s[%(lineno)-3s] |%(levelname)-8s |%(message)s'
        self.info_format_file = '[%(asctime)s] |%(filename)s[%(funcName)sline:%(lineno)d] |%(levelname)-8s |%(message)s'

    def set_logger(self):
        formatter = ColoredFormatter(fmt=self.info_format_console,
                                     datefmt=self.date_format,
                                     reset=True,
                                     log_colors={
                                         'DEBUG': 'light_purple',
                                         'INFO': 'light_cyan',
                                         'WARNING': 'yellow',
                                         'ERROR': 'red',
                                         'CRITICAL': 'red,bold_red'})
        formatter_file = logging.Formatter(fmt=self.info_format_file,
                                           datefmt=self.date_format)

        _logger = logging.getLogger('MainLogger')
        _logger.setLevel(logging.DEBUG)

        ConsoleLogger = logging.StreamHandler()  # 输出到终端
        ConsoleLogger.setFormatter(formatter)
        log_name = time.strftime('%Y-%m-%d %H')  # 一小时内使用的日志文件都是同一个
        FileLogger = logging.handlers.RotatingFileHandler(filename=f'./log/{log_name}.log',
                                                          maxBytes=102400,
                                                          backupCount=5)  # 每个日志文件最大102400字节(100Kb)
        FileLogger.setFormatter(formatter_file)
        _logger.addHandler(ConsoleLogger)
        _logger.addHandler(FileLogger)
        return _logger


if __name__ != '__main__':
    logger = Logger().set_logger()
