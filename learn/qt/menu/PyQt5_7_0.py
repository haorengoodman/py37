#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_7_0.py
# @Date    : 2019-02-18
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow


# 软件界面DIY - 状态栏
class Example(QMainWindow):
    # QMainWindow 是一个主应用程序窗口(包括了 状态栏、工具栏、菜单栏)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 首次调用QWidget.QMainWindow类的statusBar() 将创建一个状态栏并返回状态栏对象
        # 后续调用，则只是返回首次创建的状态栏对象
        self.statusBar().showMessage("准备就绪...")
        # 设置窗口属性
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('软件界面 DIY')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
