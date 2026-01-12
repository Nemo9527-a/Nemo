# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: yaml_util.py
# @Software: PyCharm
"""
    Description:yaml读写封装
"""

import yaml
from LEDsetting.config.conf import cm


# 读取yaml
def read_yaml(filename):
    # filename文件名称
    path = cm.CONFIG_FILE + "/" + filename
    with open(path, "r", encoding='utf-8') as f:
        return yaml.load(stream=f, Loader=yaml.FullLoader)


# 写入yaml
def write_yaml(filename, data):
    # filename文件名称
    # data：写入数据
    path = cm.CONFIG_FILE + "/" + filename
    with open(path, 'a', encoding='utf-8') as f:
        # allow_unicode 允许unicode编码格式
        yaml.dump(data, f, allow_unicode=True)


if __name__ == '__main__':
    print(read_yaml('config.yaml'))


