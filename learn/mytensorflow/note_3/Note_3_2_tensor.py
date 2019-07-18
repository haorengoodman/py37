#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 14:31
# @Author  : journal
# @File    : Note_3_2_tensor.py
# @Software: PyCharm

import tensorflow as tf


def inti_tensor():
    # 定义一个 2 阶 张量等于 [[1.0,2.0]]
    x = tf.constant([[1.0, 2.0]])
    # 定义一个 2 阶 张量等于 [[3 .0], [4.0]]
    w = tf.constant([[3.0], [4.0]])
    # 实现 x w 矩阵乘法
    y = tf.matmul(x, w)
    # 打印出结果
    print(y)
    compute_tensor(y)


def compute_tensor(y):
    with tf.Session() as session:
        print(session.run(y))


def get_variable():
    # 生成正态分布随机数,形状：2行3列, 标准差:0, 期望值(平均值):0, 种子:1
    tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    # 去掉偏离过大的正态分布，也就是说：如果随机出来的数据偏离平均值超过两个标准差，这个数据将重新生成
    tf.Variable(tf.truncated_normal(shape=[2, 3], mean=0, stddev=2, seed=1))
    # 表示从一个均匀分布 [minval, maxval) 中随机采样，注意定义域是左闭右开。注：生成一维数组时，shape=[length, ]
    tf.Variable(tf.random_uniform(shape=[7, ], minval=0, maxval=100, dtype=tf.int32, seed=1))
    # 生成常量 [[0, 0],[0, 0],[0, 0]]
    tf.Variable(tf.zeros(shape=[3, 2], dtype=tf.int32))
    # 生成常量 [[1, 1],[1, 1],[1, 1]]
    tf.Variable(tf.ones(shape=[3, 2], dtype=tf.int32))
    # 生成常量 [[6, 6],[6, 6],[6, 6]]
    tf.Variable(tf.fill(dims=[3, 2], value=6))
    return tf.Variable(tf.random_normal(shape=[2, 3], mean=0, stddev=2, seed=1))


if __name__ == '__main__':
    # w = get_variable()
    # print(w)
    compute_tensor(tf.fill(dims=[3, 2], value=6))
