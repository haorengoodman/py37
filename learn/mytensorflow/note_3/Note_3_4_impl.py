#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:47
# @Author  : journal
# @File    : Note_3_4_impl.py
# @Software: PyCharm

import tensorflow as tf


# 定义输入、参数、向前传播过程
def practice_1_param():
    # 定义输入
    x = tf.constant([[0.7, 0.5]])
    # 定义参数
    w1 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    w2 = tf.Variable(tf.random_normal(shape=[3, 1], mean=0, stddev=2, seed=1))
    # 定义向前传播过程
    a = tf.matmul(x, w1)
    b = tf.matmul(a, w2)
    return b


# 定义输入、参数、向前传播过程
def practice_1_param():
    # 定义输入
    x = tf.placeholder(tf.float32, shape=(1, 2))
    # 定义参数
    w1 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    w2 = tf.Variable(tf.random_normal(shape=[3, 1], mean=0, stddev=2, seed=1))
    # 定义向前传播过程
    a = tf.matmul(x, w1)
    b = tf.matmul(a, w2)
    return b


# 变量初始化、图节点计算
def compute(graph_ele):
    with tf.Session() as session:
        # 1. 变量初始化
        session.run(tf.global_variables_initializer())
        # 2. 图节点计算
        result = session.run(graph_ele)
        return result


# 变量初始化、图节点计算
def compute(graph_ele, feed_dict):
    with tf.Session() as session:
        # 1. 变量初始化
        session.run(tf.global_variables_initializer())
        # 2. 图节点计算
        result = session.run(graph_ele, feed_dict)
        return result


if __name__ == '__main__':
    c = practice_1_param()
    result_c = compute(c)
    print("result in Note_3_4_impl is:", result_c)
