#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 15:39
# @Author  : journal
# @File    : Test.py
# @Software: PyCharm
import json

if __name__ == '__main__':
    data = '{"c": 3, "a": 1, "b": 2}'  # 定义一个字符串类型
    json_data = json.loads(data)
    x = json_data["c"]
    print(x)
