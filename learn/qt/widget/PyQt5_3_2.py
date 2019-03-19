#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_3_1.py
# @Date    : 2019-02-14
# @Author  : gaotao
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QT Learning")
        self.setGeometry(300, 200, 300, 300)

        btn = QPushButton("退出", self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(80, 30)
        btn.move(30, 30)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ico = Ico()
    sys.exit(app.exec_())

