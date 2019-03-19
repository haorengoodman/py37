#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_5_3.py
# @Date    : 2019-02-15
# @Author  : gaotao
from random import randint
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QMessageBox


#  剪刀、石头、布
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 新建三个按钮
        self.bt1 = QPushButton("石头",self)
        self.bt2 = QPushButton("剪刀",self)
        self.bt3 = QPushButton("布",self)
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setWindowTitle("信号、槽")
        self.setGeometry(200, 200, 500, 300)
        # 设置按钮属性
        self.bt1.setGeometry(115,200,70,40)
        self.bt2.setGeometry(215,200,70,40)
        self.bt3.setGeometry(315,200,70,40)
        # 事件与槽位关联
        self.bt1.clicked.connect(self.buttonClick)
        self.bt2.clicked.connect(self.buttonClick)
        self.bt3.clicked.connect(self.buttonClick)

        # 窗口显示
        self.show()

    def buttonClick(self):
        # 1:石头 2:剪刀 3:布
        guess_num = randint(1,3)
        sender = self.sender()
        btn_text = sender.text()
        if btn_text == "石头":
            if guess_num == 1:
                QMessageBox.about(self,"石头","平手")
            elif guess_num == 2:
                QMessageBox.about(self,"剪刀","赢了")
            elif guess_num == 3:
                QMessageBox.about(self,"布","输了")
        if btn_text == "剪刀":
            if guess_num == 1:
                QMessageBox.about(self,"石头","输了")
            elif guess_num == 2:
                QMessageBox.about(self,"剪刀","平手")
            elif guess_num == 3:
                QMessageBox.about(self,"布","赢了")
        if btn_text == "布":
            if guess_num == 1:
                QMessageBox.about(self,"石头","赢了")
            elif guess_num == 2:
                QMessageBox.about(self,"剪刀","输了")
            elif guess_num == 3:
                QMessageBox.about(self,"布","平手")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())

