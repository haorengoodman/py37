#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_8_4.py
# @Date    : 2019-02-22
# @Author  : gaotao
from PyQt5.QtGui import QRegExpValidator, QKeyEvent, QKeySequence
from PyQt5.QtWidgets import  QApplication, QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox
from PyQt5.QtCore import Qt, QRegExp, QEvent, QObject
import sys


# 软件界面DIY - 自定义对话框
class PasswdDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350,100)
        self.setWindowTitle('自定义对话框')

        self.lb = QLabel("请输入密码",self)
        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)
        self.bt1 = QPushButton("确定",self)
        self.bt2 = QPushButton("取消",self)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)
        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # 使用布局
        self.setLayout(vbox)

        # 设置密码框属性 1.密码框禁止右键 2.密码框为空时，设置密码框规则提示 3.设置输入框显示字符模式
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码6-15位，只能有数字和字母，必须以字母开头")
        self.edit.setEchoMode(QLineEdit.Password)

        # 密码校验
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)
        object = QObject()
        # self.show()

    # 事件过滤器
    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)

    def Ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)          # 结束对话框返回1

    def Cancel(self):
        self.done(0) # 结束对话框返回0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pd = PasswdDialog()
    sys.exit(app.exec_())
