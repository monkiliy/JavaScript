# -*- coding: utf-8 -*-
import logging
import os
import time


class Logger(object):
    def __init__(self, loggername):
        self.logger = logging.getLogger(loggername)  # RootLogger的实例
        self.logger.setLevel(logging.DEBUG)

        # 控制台格式
        stream = logging.StreamHandler()
        stream.setLevel(logging.INFO)

        times = time.strftime('%Y-%m-%d')
        log_path = os.path.dirname(os.path.abspath('.')) + '\\ecshop_automation\\logs\\'

        log_name = log_path + times + '.log'

        # 文件格式
        file = logging.FileHandler(log_name, encoding='utf-8')
        file.setLevel(logging.INFO)

        # 定义输出样式
        DATEFMT = '%Y-%m-%d %H:%M:%S'
        FORMAT = "%(asctime)s %(name)s [%(levelname)s] %(message)s"
        formatter = logging.Formatter(
            fmt=FORMAT,
            datefmt=DATEFMT,
        )

        # 设置控制台和文件样式
        stream.setFormatter(formatter)
        file.setFormatter(formatter)

        # 加入Handler
        self.logger.addHandler(stream)
        self.logger.addHandler(file)

    # 获得logger
    def getlog(self):
        return self.logger
