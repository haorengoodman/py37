#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_7_1.py
# @Date    : 2019-02-18
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QIcon

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow, QAction


# 软件界面DIY - 菜单
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪...")
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('软件界面 DIY')
        # 创建一个具有特定图标和“退出”标签的动作
        exitAction = QAction(QIcon("D://aaaa//image//11558369_l0h.jpg"), "退出(&E)", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(app.quit)

        # 创建菜单栏
        menubar = self.menuBar()
        # 创建菜单,设置快捷键(Alt+F)
        fileMenu = menubar.addMenu('文件(&F)')
        # 在菜单上添加动作
        fileMenu.addAction(exitAction)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
