# -*- coding: utf-8 -*-
# @Time    : 2025/3/3  16:05
# @Author  : Nemo
# @FileName: assert_util.py
# @Software: PyCharm
"""
    Description:断言封装
"""

import json
from LEDsetting.common.log_util import log

class Assertions:
    @staticmethod
    def assert_status_code(response_code, expected_code):
        """
        断言状态码
        :param response_code: 请求响应对象
        :param expected_code: 预期的状态码
        """
        try:
            assert response_code == expected_code, \
                f"状态码断言失败！预期: {expected_code}, 实际: {response_code}"
            log.info(f"状态码断言成功！预期: {expected_code}, 实际: {response_code}")
            result = True
            return result
        except AssertionError as e:
            result = False
            return result

    @staticmethod
    def assert_response_body(response, expected_body):
        """
        断言响应体
        :param response: 请求响应对象
        :param expected_body: 预期的响应体（字典格式）
        """
        try:
            if type(response) is str:
                actual_body = Assertions.try_convert_to_json(response)
                assert actual_body == expected_body, \
                    f"响应体断言失败！预期: {expected_body}, 实际: {actual_body}"
                log.info(f"响应体断言成功！预期: {expected_body}, 实际: {actual_body}")
            else:
                actual_body = response.json()
                assert actual_body == expected_body, \
                    f"响应体断言失败！预期: {expected_body}, 实际: {actual_body}"
                log.info(f"响应体断言成功！预期: {expected_body}, 实际: {actual_body}")
            result = True
            return result

        except AssertionError as e:
            result = False
            return result

    @staticmethod
    def assert_field_value(response, field, expected_value):
        """
        断言响应体中某个字段的值
        :param response: 请求响应对象
        :param field: 字段名
        :param expected_value: 预期的字段值
        """
        try:
            if type(response) is str:
                actual_body = Assertions.try_convert_to_json(response)
                assert field in actual_body, f"字段 {field} 不存在于响应体中！"
                assert actual_body[field] == expected_value, \
                    f"字段值断言失败！字段: {field}, 预期: {expected_value}, 实际: {actual_body[field]}"
                log.info(f"字段值断言成功！字段: {field}, 预期: {expected_value}, 实际: {actual_body[field]}")
            else:
                actual_body = actual_body = response.json()
                assert field in actual_body, f"字段 {field} 不存在于响应体中！"
                assert actual_body[field] == expected_value, \
                    f"字段值断言失败！字段: {field}, 预期: {expected_value}, 实际: {actual_body[field]}"
                log.info(f"字段值断言成功！字段: {field}, 预期: {expected_value}, 实际: {actual_body[field]}")
            result = True
            return result

        except AssertionError as e:
            result = False
            return result

    @staticmethod
    def assert_exception(exception, expected_exception):
        """
        断言异常类型
        :param exception: 捕获的异常
        :param expected_exception: 预期的异常类型
        """
        # assert isinstance(exception, expected_exception), \
        #     f"异常断言失败！预期: {expected_exception}, 实际: {type(exception)}"
        try:
            assert exception == expected_exception, \
                f"异常断言失败！预期: {expected_exception}, 实际: {exception}"
            log.info(f"响应体断言成功！预期: {expected_exception}, 实际: {exception}")
            result = True
            return result
        except AssertionError as e:
            result = False
            return result

    @staticmethod
    def try_convert_to_json(value):
        """
        尝试将值转换为 JSON 格式
        :param value: 需要转换的值
        :return: 转换后的 JSON 数据（如果可转换），否则返回原值
        """
        if isinstance(value, (str, bytes, bytearray)):
            try:
                # 尝试将字符串解析为 JSON
                return json.loads(value)
            except json.JSONDecodeError:
                # 如果解析失败，返回原值
                return value
        else:
            try:
                # 尝试将对象序列化为 JSON
                json.dumps(value)
                return value  # 如果能序列化，说明已经是 JSON 兼容的类型
            except (TypeError, OverflowError):
                # 如果序列化失败，返回原值
                return value
