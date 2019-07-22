#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 11:41
# @Author  : journal
# @File    : Note_3_5_impl.py
# @Software: PyCharm

import tensorflow as tf


# **************************
# ******** 前向传播 *********
# **************************

# 使用 placeholder 定义输入
# 定义输入、参数、向前传播过程
def practice_1_param(input_x):
    # 定义参数
    w1 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    w2 = tf.Variable(tf.random_normal(shape=[3, 1], mean=0, stddev=2, seed=1))
    # 定义向前传播过程
    a = tf.matmul(input_x, w1)
    b = tf.matmul(a, w2)
    return b


# 变量初始化、图节点计算
def compute(graph_ele, feed_dict):
    with tf.Session() as session:
        # 1. 变量初始化
        session.run(tf.global_variables_initializer())
        # 2. 图节点计算
        result = session.run(graph_ele, feed_dict)
        return result


# 使用 placeholder 定义 一组 特征(输入)
def run_with_placeholder():
    # 1.使用占位符定义输入(1行2列)
    input_x = tf.placeholder(tf.float32, shape=(1, 2))
    # 2.定义计算图
    graph_element = practice_1_param(input_x)
    # 3.实际的输入参数
    feed_data = {input_x: [[0.7, 0.5]]}
    # 4.运算 计算图
    result_c = compute(graph_element, feed_data)
    print("result in Note_3_4_impl is:\n", result_c)


# 使用 placeholder 定义 多组 特征(输入)
def run_with_placeholder_2():
    # 1.使用占位符定义输入(多行行2列)
    input_x = tf.placeholder(tf.float32, shape=(None, 2))
    # 2.定义计算图
    graph_element = practice_1_param(input_x)
    # 3.实际的输入参数
    feed_data = {input_x: [[0.7, 0.5], [0.7, 0.7]]}
    # 4.运算 计算图
    result_c = compute(graph_element, feed_data)
    print("result in Note_3_4_impl is:\n", result_c)


if __name__ == '__main__':
    run_with_placeholder()
    run_with_placeholder_2()
