#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:17
# @Author  : journal
# @File    : Note_3_3_impl.py
# @Software: PyCharm

import tensorflow as tf


# 第一个练习
def practice_1():
    x = tf.constant([[0.7, 0.5]])
    w1 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    a = tf.matmul(x, w1)
    w2 = tf.Variable(tf.random_normal(shape=[3, 1], mean=0, stddev=2, seed=1))
    b = tf.matmul(a, w2)
    return b


def compute(tensor_param):
    with tf.Session() as session:
        # 1. 变量初始化
        init_op = tf.global_variables_initializer()
        session.run(init_op)
        # 2. 图节点计算
        result = session.run(tensor_param)
        return result


if __name__ == '__main__':
    c = practice_1()
    result_c = compute(c)
    print("result in Note_3_3_impl.py is:", result_c)
