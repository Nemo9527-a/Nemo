# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: websocket_util.py
# @Software: PyCharm
"""
    Description:websocket接口封装
"""

import json
from websocket import create_connection, WebSocketTimeoutException
from LEDsetting.config.conf import cm
from LEDsetting.common.log_util import log
from LEDsetting.common.excel_util import DoExcel


class ApiWebsocket:

    def __init__(self, parameter, conf=None):
        self.parameter = parameter
        self.url = f"{parameter['protocol']}://{cm.URL_INFO['ip']}:{cm.URL_INFO['port_websocket']}{parameter['url']}"
        self.ws = None
        self._connect()

    def _connect(self):
        """
        建立 WebSocket 连接
        """
        try:
            log.info(f"正在创建 WebSocket 连接: {self.url}")
            self.ws = create_connection(self.url, timeout=5)
            log.info("WebSocket 连接成功！")
        except WebSocketTimeoutException as e:
            log.error(f"WebSocket 连接超时: {e}")
            return 'Connection timed out'
        except Exception as e:
            log.error(f"WebSocket 连接失败: {e}")
            return e


    def close(self):
        """
        关闭 WebSocket 连接
        """
        if self.ws:
            self.ws.close()
            log.info("WebSocket 连接已关闭！")
        else:
            log.warning("WebSocket 连接未建立，无需关闭！")

    def send(self):
        """
        发送数据
        :return: 服务器返回的数据
        """
        if not self.ws:
            raise RuntimeError("WebSocket 连接未建立！")
        else:
            log.info(f"开始执行【{self.parameter['port_name']}-{self.parameter['case_title']}】接口测试用例")
            replay_data = json.loads(self.parameter['data'])
            new_replay_data = json.dumps(replay_data, ensure_ascii=False)
            try:
                # 发送数据
                self.ws.send(new_replay_data)
                log.info(f"请求参数：{new_replay_data}")
                # 接收服务器响应
                response = self.ws.recv()
                log.info(f'返回参数：{response}')
                return response
            except WebSocketTimeoutException as e:
                log.error(f"请求超时: %s" % e)
                return "Connection timed out"

            except Exception as e:
                log.error(f"请求错误: %s" % e)
                return e


if __name__ == '__main__':
    parameter1_test = DoExcel('param.xlsx', '查询已初始化客户端').read()[0]
    # parameter2_test = read_yaml('config.yaml')['test']
    abc = ApiWebsocket(parameter1_test)
    cd = abc.send()
    abc.close()
    print(f"返回结果：{cd}，{type(cd)}")
    print(json.loads(cd))
    print(abc.ws.getstatus())
