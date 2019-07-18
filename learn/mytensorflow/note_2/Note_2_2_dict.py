#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 12:18
# @Author  : journal
# @File    : Note_2_2_dict.py
# @Software: PyCharm


#  字典  使用{} 初始化
def init_dict():
    dict_1 = {"k1": "v1", "k2": "v2"}
    print(dict_1)
    # 索引
    print("k1="+dict_1.get("k1"))
    print("k2="+dict_1["k2"])
    # 修改
    dict_1["k2"] = "v2_new"
    print("k2=" + dict_1["k2"])
    # 删除
    del dict_1["k2"]
    print(dict_1)
    # 添加
    dict_1["k3"] = "v3"
    print(dict_1)


if __name__ == '__main__':
    init_dict()
