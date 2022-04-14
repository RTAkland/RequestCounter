#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/11
# @File Name: logger.py


import time
import logging.handlers
from colorlog import ColoredFormatter


class CreateLogger:
    """创建日志器"""

    def __init__(self) -> None:
        """
        初始化类
        """
        self.date_format = '%H:%M:%S'
        self.info_format_console = '%(log_color)s[%(asctime)s] |%(filename)-12s[%(lineno)s] |%(levelname)-8s |%(message)s'
        self.info_format_file = '[%(asctime)s] |%(filename)s[%(funcName)sline:%(lineno)d] |%(levelname)-8s |%(message)s'
        self.formatter = ColoredFormatter(fmt=self.info_format_console,
                                          datefmt=self.date_format,
                                          reset=True,
                                          log_colors={
                                              'DEBUG': 'light_purple',
                                              'INFO': 'light_cyan',
                                              'WARNING': 'yellow',
                                              'ERROR': 'red',
                                              'CRITICAL': 'red,bold_red'})
        self.formatter_file = logging.Formatter(fmt=self.info_format_file,
                                                datefmt=self.date_format)

    def get_logger(self) -> logging.Logger:
        """
        设置日志器
        :return:
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_logger = logging.StreamHandler()  # 输出到终端
        console_logger.setFormatter(self.formatter)
        log_name = time.strftime('%Y-%m-%d#%H')  # 一小时内使用的日志文件都是同一个
        file_logger = logging.handlers.RotatingFileHandler(filename=f'./app/logs/{log_name}.log',
                                                           maxBytes=102400,
                                                           backupCount=5)  # 每个日志文件最大102400字节(100Kb)
        file_logger.setFormatter(self.formatter_file)
        logger.addHandler(console_logger)
        logger.addHandler(file_logger)
        return logger

    @staticmethod
    def init_app(app):
        """
        虚假的init_app静态方法
        :param app:
        :return:
        """
        pass
