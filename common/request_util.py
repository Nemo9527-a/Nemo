# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: requests_util.py
# @Software: PyCharm
"""
    Description:HTTP接口封装
"""

import json
import requests
from LEDsetting.common.log_util import log
from LEDsetting.common.excel_util import DoExcel
from LEDsetting.common.yaml_util import read_yaml
from LEDsetting.config.conf import cm


def api_requests(parameter, conf=None):
    sess = requests.session()
    log.info(f"开始执行【{parameter['port_name']}-{parameter['case_title']}】接口测试用例")
    if parameter['protocol'] == 'http':
        url = f"{parameter['protocol']}://{cm.URL_INFO['ip']}:{cm.URL_INFO['port_http']}{parameter['url']}"
        method = parameter['method']
        headers = json.loads(parameter['header'])
        data = json.loads(parameter['data'])
        # excepted = json.loads(parameter1['excepted'])
        try:
            log.info(f"请求地址: {url}")
            log.info(f"请求参数：{data}")
            response = sess.request(url=url, method=method, headers=headers, json=data, timeout=5)
            log.info(f'返回参数：{response.text}')
            # log.handlers[0].flush()  # 强制刷新日志
            return response
        except Exception as e:
            log.error(f"请求错误: %s" % e)
            raise

'''
    elif parameter['protocol'] == 'ws':
        url = f"{parameter['protocol']}://{conf['IP']}:{conf['PORT_WEBSOCKET']}{parameter['url']}"
        replay_data = json.loads(parameter['data'])
        # 创建websocket连接
        try:
            log.info(f'创建websocket连接！')
            ws = create_connection(url=url, timeout=5)
            new_replay_data = json.dumps(replay_data, ensure_ascii=False)
            # 发送数据
            ws.send(new_replay_data)
            log.info(f"请求参数：{new_replay_data}")
            # 接收服务器响应
            try:
                response = ws.recv()
                log.info(f'返回参数：{response}')
                ws.close()
                log.info("关闭websocket连接!")
                return response
            except WebSocketTimeoutException as e:
                log.error(f"请求超时: %s" % e)
            except Exception as e:
                log.error(f"请求错误: %s" % e)

        except WebSocketTimeoutException as e:
            log.error(f"创建连接失败！: %s" % e)

    else:
        log.error(f'暂无{parameter['protocol']}协议接口，请检查参数！')
'''


if __name__ == '__main__':
    parameter1_test = DoExcel('param.xlsx', '获取详细版本').read()[4]
    parameter2_test = read_yaml('config.yaml')['test']
    abc = api_requests(parameter1_test, parameter2_test)
    print(f"返回结果：{abc.json()}，{type(abc.json())}")
