#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 10:15
# @Author  : journal
# @File    : Note_4_3_learning_rate.py
# @Software: PyCharm

import tensorflow as tf

##################################################
# ############# learning_rate ####################
# #############      学习率    ####################
##################################################

# 定义待优化参数w的初始值为5
w = tf.Variable(tf.constant(5, dtype=tf.float32))
# 定义损失函数
loss = tf.square(w + 1)
# 定义反向传播方法
train = tf.train.GradientDescentOptimizer(0.2).minimize(loss)  # 能找到最优参数
# train = tf.train.GradientDescentOptimizer(1).minimize(loss)  # 学习率过大，出现震荡不收敛
# train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)  # 学习率过小，出现收敛速度慢

with tf.Session() as session:
    init_op = tf.global_variables_initializer()
    session.run(init_op)
    for i in range(100):
        session.run(train)
        w_val = session.run(w)
        loss_val = session.run(loss)
        print("After {0} steps: w is {1}, loss is {2}".format(i, w_val, loss_val))
