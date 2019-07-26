#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 11:24
# @Author  : journal
# @File    : Note_4_3_learning_rate_1.py
# @Software: PyCharm

import tensorflow as tf

##################################################
# ############ 指数衰减学习率 #######################
# ### exponential_decay_learning_rate  ###########
##################################################

LEARNING_RATE_BASE = 0.1  # 初始学习率
LEARNING_RATE_DECAY = 0.99  # 学习衰减率
LEARNING_RATE_STEP = 1  # 喂入多少轮 BATCH_SIZE 后，更新一次学习率，一般认为:

# 运行了几轮 BATCH_SIZE 的计数器
global_step = tf.Variable(0, trainable=False)
# 定义指数下降学习率
learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,    # 初始学习率
                                           global_step,           # 当前运行的轮数
                                           LEARNING_RATE_STEP,    # 说少轮更新一次学习率（总样本数/BATCH_SIZE）
                                           LEARNING_RATE_DECAY,   # 学习衰减率
                                           staircase=True)

# 定义待优化参数w的初始值为 10
w = tf.Variable(tf.constant(10, dtype=tf.float32))
# 定义损失函数
loss = tf.square(w + 1)
# 定义反向传播方法
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

with tf.Session() as session:
    init_op = tf.global_variables_initializer()
    session.run(init_op)
    for i in range(100):
        session.run(train)
        learning_rate_val = session.run(learning_rate)
        global_step_val = session.run(global_step)
        w_val = session.run(w)
        loss_val = session.run(loss)
        print("After {0} steps: w is {1}, loss is {2}".format(i, w_val, loss_val))
        print("After {0} steps: global_step is {1}, w is {2}, learning_rate is {3}, loss is {4}".
              format(i, global_step_val, w_val, learning_rate_val, loss_val))
