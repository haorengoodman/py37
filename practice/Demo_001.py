# -*- coding:utf-8 -*-
"""
QMainWindow  状态栏

@author:dell
@file: Demo_001.py
@time: 2020/01/15
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(20, 100, 300, 80)
        self.statusBar().showMessage("准备就绪......")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())