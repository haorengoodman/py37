#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 10:01
# @Author  : journal
# @File    : Note_3_1_tensor.py
# @Software: PyCharm

import tensorflow as tf

if __name__ == '__main__':
    # 定义 tensor
    a = tf.constant([1.0, 2.0], name="a")
    b = tf.constant([3.0, 4.0], name="b")
    c = tf.constant([5.0, 6.0], name="c")
    # result_ab = a + b
    # result_bc = b + c
    result_ab = tf.add(a, b, name="add")
    result_bc = tf.add(b, c, name="add")
    print(result_ab)
    print(result_bc)
    # 获取计算图的结果
    with tf.Session() as session:
        result = session.run(result_ab)
        print(result)
