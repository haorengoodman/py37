# -*- coding:utf-8 -*-
"""
@author:dell
@file: MyTimer.py
@time: 2020/01/15
"""
import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class MyTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.myThread = MyThread()
        self.myThread.my_signal.connect(self.set_label_func)  # 3 信号和槽链接
        self.label_1 = QLabel("0")
        self.bt_1 = QPushButton("start")
        self.bt_2 = QPushButton("stop")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("手动计时器")
        self.setGeometry(70, 100, 400, 250)

        hbox = QHBoxLayout()  # 水平方向的空白被分成了 20 等份儿
        hbox.addStretch(10)
        hbox.addWidget(self.bt_1)
        hbox.addWidget(self.bt_2)
        hbox.addStretch(10)

        hbox_1 = QHBoxLayout()  # 水平布局
        hbox_1.addStretch(10)
        hbox_1.addWidget(self.label_1)
        hbox_1.addStretch(10)

        vbox = QVBoxLayout()  # 垂直布局
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox)

        # bt_1 添加事件
        self.bt_1.clicked.connect(self.count_func)
        self.bt_2.clicked.connect(self.stop_count_func)

        self.setLayout(vbox)
        self.show()

    def count_func(self):
        self.myThread.is_on = True
        self.myThread.start()

    def set_label_func(self, signal_value):  # 4
        self.label_1.setText(signal_value)

    def stop_count_func(self):
        self.myThread.is_on = False
        self.myThread.count = 0


# 线程类
class MyThread(QThread):
    my_signal = pyqtSignal(str)  # 1

    def __init__(self):
        super().__init__()
        self.count = 0
        self.is_on = True

    def run(self):
        while self.is_on:
            self.count += 1
            self.my_signal.emit(str(self.count))  # 2
            self.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTimer = MyTimer()
    sys.exit(app.exec_())
