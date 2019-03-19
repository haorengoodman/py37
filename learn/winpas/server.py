#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 16:40
# @Author  : journal
# @File    : server.py
# @Software: PyCharm


import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(('127.0.0.1', 55555))  # 绑定IP/端口
ser.listen(5)  # 监听
print('starting....')
conn, addr = ser.accept()  # 连接
print(conn)
print('client addr', addr)
print('ready to recv the passwd...')
client_msg = conn.recv(1024)
print('client passwd changed: %s' % client_msg)
conn.send(client_msg.upper())
conn.close()
ser.close()