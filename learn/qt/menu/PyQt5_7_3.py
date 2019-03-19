#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_7_3.py
# @Date    : 2019-02-18
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QIcon

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow, QAction, QMenu


# 软件界面DIY - 上下文菜单(右键菜单)
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪...")
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('软件界面 DIY')
        # 创建动作，设置快捷键、提示、信号与槽位的关联
        exitAct = QAction("退出(&E)",self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出程序")
        exitAct.triggered.connect(app.quit) # triggered 触发
        # 创建菜单 -> 添加动作
        saveMenu = QMenu("保存方式(&S)",self)
        saveAct = QAction(QIcon(""),"保存...",self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.setStatusTip("保存文件")
        saveAsAct = QAction(QIcon(""),"另存为...(&O)",self)
        saveAsAct.setStatusTip("另存为")
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveAsAct)
        # 创建动作
        newAct = QAction(QIcon(''),'新建(&N)',self)
        newAct.setShortcut('Ctrl+N')

        # 创建菜单栏(menuBar) -> 创建菜单(Menu) -> 添加动作/菜单(addAction/addMenu)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        self.show()

    # 要使用上下文菜单，必须重新实现contextMenuEvent()方法
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("新建")
        saveAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        # 使用exec_()方法显示上下文菜单   mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
           app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
