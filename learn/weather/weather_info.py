# -*- coding:utf-8 -*-
"""
@author:dell
@file: weather_info.py
@time: 2020/01/13
"""
import os
import sys

import pandas as pd
import re
import json

from PyQt5.QtWidgets import QApplication
from pandas.core import config_init
from pip._vendor import requests

from learn.weather.my_ui import my_ui


def read_file(path):
    # 将下载好的文件命名为 'china-city-list.csv'，并删除 header
    df = pd.read_csv(path, skiprows=1)  # DataFrame
    # 选取需要的两列信息
    df = df.loc[:, ['City_ID', 'City_CN']]
    return df


# 将df 中City_ID 中的前缀CN   去掉
def convert(city_id):
    # 匹配 City_ID 中的数字
    pat = re.compile('(\d+)')
    return pat.search(city_id).group()


# 从df 中构建  name -> id 的映射
def city2id(file):
    code_dict = {}
    for k, v in zip(file['City_CN'], file['City_ID_map']):
        code_dict[k] = v
    return code_dict


# 保存json数据到文件
def save_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


# 读取json文件
def read_json_file(path):
    with open(path) as f:
        text = json.load(f)
        return text


# 将china-city-list 转换为 name -> id 映射
def get_name_id_dict():
    base_name = os.path.dirname(os.path.realpath(sys.argv[0]))
    # path = os.path.join(base_name, "china-city-list.csv")
    # f = read_file(path)
    # f['City_ID_map'] = f['City_ID'].map(convert)
    # name2id_dict = city2id(f)
    target_path = os.path.join(base_name, "city_code.json")
    # print(target_path)
    # save_file(name2id_dict, target_path)
    txt = read_json_file(target_path)
    return txt


if __name__ == '__main__':
    app = QApplication(sys.argv)
    name_id_dict = get_name_id_dict()
    ui = my_ui(name_id_dict)
    ui.btn_1.clicked.connect(app.quit)
    sys.exit(app.exec_())


