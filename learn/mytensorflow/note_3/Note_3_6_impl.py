#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 14:29
# @Author  : journal
# @File    : Note_3_6_impl.py
# @Software: PyCharm

# step_0: 倒入模块，生成模拟数据
import tensorflow as tf
import numpy as np

BATCH_SIZE = 8
seed = 23455

# 基于seed 生成随机数
randomState = np.random.RandomState(seed)
# 随机返回32行2列的矩阵，32行表示32组，2列表示体积和重量
X = randomState.rand(32, 2)
# (按行)遍历矩阵X，如果 (体积+重量)和 < 1 ,则给Y赋值1(表示合格)，如果 (体积+重量)和 >= 1, 则给Y赋值0(表示不合格)
Y = [[int(x0 + x1 < 1)] for (x0, x1) in X]
print("X:\n", X)
print("Y:\n", Y)

# step_1: 定义神经网络的输入、参数和输出，定义向前传播过程
x = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

w1 = tf.random_normal(shape=[2, 3], mean=0, stddev=1, seed=1)
w2 = tf.random_normal(shape=[3, 1], mean=0, stddev=1, seed=1)

a = tf.matmul(x, tf.Variable(w1))
y = tf.matmul(a, tf.Variable(w2))

# step_2: 定义损失函数及 反向传播方法
loss = tf.reduce_mean(tf.square(y - y_))
# train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# train_step = tf.train.MomentumOptimizer(0.001, 0.9).minimize(loss)
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# step_3: 生成会话，训练 STEPS 轮
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    # 输出目前参数(未训练)取值
    print("w1:\n", session.run(w1))
    print("w2:\n", session.run(w2))
    print("\n")

    # 训练模型
    STEPS = 3000
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        session.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 500 == 0:
            total_loss = session.run(loss, feed_dict={x: X, y_: Y})
            print("After %d training step(s), loss on all data is %g" % (i, total_loss))
    # 输出训练后的参数
    print("w1:\n", session.run(w1))
    print("w2:\n", session.run(w2))
