#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 15:52
# @Author  : journal
# @File    : Note_3_0_tensor.py
# @Software: PyCharm

import tensorflow as tf

if __name__ == '__main__':
    a = tf.constant([1.0, 2.0], name="a")
    b = tf.constant([2.0, 3.0], name="b")
    result = tf.add(a, b, name="add")
    print(result)
    print(type(result))
    res = tf.Session().run(result)
    print(res)

# Tensor("add:0", shape=(2,), dtype=float32)
# 三个属性：名字(name)、维度(shape)和类型(type)








