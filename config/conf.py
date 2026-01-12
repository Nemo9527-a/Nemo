# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: conf.py
# @Software: PyCharm
"""
    Description:配置信息
"""

import os
import datetime

class ConfigManager(object):
    # 获取项目根目录路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'reports/')

    # 配置文件
    CONFIG_FILE = os.path.join(BASE_DIR, 'config/')

    # 数据文件
    DATA_FILE = os.path.join(BASE_DIR, 'data/')

    # 日志文件
    LOG_FILE = os.path.join(BASE_DIR, 'logs/')

    # 地址信息
    URL_INFO = {
        'ip': '127.0.0.1',
        'port_http': 8086,
        'port_websocket': 8090
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': 'xxxxxxx@qq.com',
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }


    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        fmt = "%Y-%m-%d"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(datetime.datetime.now().strftime(fmt)))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.yaml')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file

    @property
    def data_file(self):
        """配置文件"""
        data_file = os.path.join(self.BASE_DIR, 'data', 'param.xlsx')
        if not os.path.exists(data_file):
            raise FileNotFoundError("数据文件%s不存在！" % data_file)
        return data_file

cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
    print(cm.REPORT_FILE)
    print(cm.CONFIG_FILE)
    print(cm.LOG_FILE)
    print(cm.URL_INFO)
    print(cm.log_file)
    print(cm.ini_file)
    print(cm.data_file)

