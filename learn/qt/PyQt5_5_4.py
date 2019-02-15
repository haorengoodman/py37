#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_5_3.py
# @Date    : 2019-02-15
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox


#  自定义信号源
class Signal(QObject):
    showmouse = pyqtSignal()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.s = Signal()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')
        # 信号与槽位关联
        self.s.showmouse.connect(self.about) # 信号和槽位关联
        self.show()

    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    def mousePressEvent(self, e):
        self.s.showmouse.emit() # emit 发射信号

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
