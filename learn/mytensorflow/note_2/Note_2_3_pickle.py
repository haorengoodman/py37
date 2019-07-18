#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 15:03
# @Author  : journal
# @File    : Note_2_3_pickle.py
# @Software: PyCharm

# 将数据序列化，然后再将序列化数据反序列化，转换为对象
import pickle
msg = {'name': 'Tom', 'age': 22}
file_name = "D:/aaaa/data/a.log"


def write_msg_2_file(message, f):
    save_file = open(f, mode="wb")
    pickle.dump(message, save_file)
    save_file.close()


def read_msg_from_file(f):
    load_file = open(f, mode="rb")
    load_file_data = pickle.load(load_file)
    print(str(load_file_data))
    load_file.close()


def write_msg_2_file_(message, f):
    with open(f, mode="wb") as save_file:
        pickle.dump(message, save_file)


def read_msg_from_file_(f):
    with open(f, mode="rb") as load_file:
        load_file_data = pickle.load(load_file)
        print(type(load_file_data))
        print(load_file_data)


if __name__ == '__main__':
    write_msg_2_file_(msg, file_name)
    read_msg_from_file_(file_name)



