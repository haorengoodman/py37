#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_6_1.py
# @Date    : 2019-02-16
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber


# 格子布局
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('自定义布局')
        # 创建并设置格子布局
        grid = QGridLayout()
        self.setLayout(grid)
        self.lcd = QLCDNumber()
        # 参数1:控件名 ，参数2:行，参数3:列，参数4:占用的行数，参数5:占用的列数，参数6:对齐方式
        grid.addWidget(self.lcd,0,0,4,0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, position[0],position[1],1,1)
            # grid.addWidget(button, *position)
            button.clicked.connect(self.bt_cli)

        self.show()

    def bt_cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display("U")
        else:
            self.lcd.display(sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
