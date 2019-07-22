#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 12:49
# @Author  : journal
# @File    : Note_4_0_MSE.py
# @Software: PyCharm


import tensorflow as tf
import numpy as np

##################################################
# ############# 损失函数:均方误差 ###################
##################################################
# 单次训练喂入的数据量、随机种子
BATCH_SIZE = 8
SEED = 23455

randomState = np.random.RandomState(SEED)
X = randomState.rand(32, 2)
Y_ = [[x1 + x2 + (randomState.rand() / 10 - 0.05)] for (x1, x2) in X]

# 1. 定义神经网络的输入、参数、定义前向传播过程、标准答案
x = tf.placeholder(tf.float32, shape=(None, 2))
w1 = tf.random_normal(shape=[2, 1], mean=0, stddev=1, seed=1)
y = tf.matmul(x, tf.Variable(w1))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

# 2. 定义损失函数及反向传播方法
loss_mes = tf.reduce_mean(tf.square(y_ - y))
train = tf.train.GradientDescentOptimizer(0.001).minimize(loss_mes)


# 3. 生成会话，训练 N 轮
def my_train():
    with tf.Session() as session:
        init_op = tf.global_variables_initializer()
        session.run(init_op)
        train_steps = 20001
        for i in range(train_steps):
            start = (i * BATCH_SIZE) % 32
            end = start + BATCH_SIZE
            session.run(train, feed_dict={x: X[start:end], y_: Y_[start:end]})
            if i % 500 == 0:
                # loss_x = session.run(loss_mes, feed_dict={x: X, y_: Y_})
                print("After {0} training, w1 is: {1}".format(str(i), session.run(w1)))


if __name__ == '__main__':
    my_train()
