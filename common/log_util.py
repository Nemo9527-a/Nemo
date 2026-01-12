# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: log_util.py
# @Software: PyCharm
"""
    Description:日志封装
"""
import logging
import colorlog
from LEDsetting.config.conf import cm

class Log:
    """
    继承logging模块中的Logger类
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 设置日志格式
    fmt = "[%(asctime)s] - [%(filename)s -->line:%(lineno)d] - %(levelname)s: %(message)s"
    formatter = logging.Formatter(fmt)

    # 定义日志输出格式，添加颜色支持
    console_formatter = colorlog.ColoredFormatter(
        '%(log_color)s[%(asctime)s] - [%(filename)s -->line:%(lineno)d] - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    # 控制台渠道
    handle1 = logging.StreamHandler()
    handle1.setFormatter(console_formatter)
    logger.addHandler(handle1)
    # 文件输出渠道
    handle2 = logging.FileHandler(cm.log_file, encoding="utf-8")
    handle2.setFormatter(formatter)
    logger.addHandler(handle2)


# 因为一个项目的日志都是写入到一个日志文件的，所以可以把file这个参数写死，直接实例化
# 后期每个模块调用就不用实例化，导入可以直接使用
log = Log().logger


if __name__ == '__main__':
    log.debug("这是一条DEBUG级别的日志")
    log.info("这是一条INFO级别的日志")
    log.warning("这是一条WARNING级别的日志")
    log.error("这是一条ERROR级别的日志")
    log.critical("这是一条CRITICAL级别的日志")

