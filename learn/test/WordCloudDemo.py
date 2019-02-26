#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 16:32
# @Author  : journal
# @File    : WordCloudDemo.py
# @Software: PyCharm
import sys
from PyQt5.QtGui import QPixmap, QPicture
import wordcloud
import jieba
import matplotlib.pyplot as plt
import string, random
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QFileDialog, QLabel

__author__ = 'journal'


# 中文词云生成器
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("词云")
        self.setGeometry(200,200,600,400)
        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(10,25,280,360)
        self.label = QLabel(self)
        self.label.setGeometry(310,25,280,360)

        # 添加工具栏
        toolBar = self.addToolBar("工具栏")
        # 创建动作
        openFileAction = QAction("选择文件",self)
        # 生成词云图片
        createImgAction = QAction("生成词云",self)
        # 添加动作到工具栏
        toolBar.addAction(openFileAction)
        toolBar.addAction(createImgAction)

        openFileAction.triggered.connect(self.open_file)
        createImgAction.triggered.connect(self.create_img)
        self.show()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self,caption="打开文件",directory="./files/",filter='(txt (*.txt))')
        if fname[0]:
            with open(fname[0],"r",encoding="utf-8",errors="ignore") as f:
                self.fileContent = f.read()
                self.textedit.setText(self.fileContent)

    # C:\\Windows\\Fonts\\msyhbd.ttf windows 系统字体默认存储位置
    def create_img(self):
        cutResult = jieba.lcut(self.fileContent)
        wc = wordcloud.WordCloud(background_color="white",width=280,height=360,font_path="./files/msyh.ttf").generate(" ".join(cutResult))
        # plt.imshow(wc)
        # plt.axis("off")
        # plt.show()
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        imagePath = "./files/"+ran_str+".jpg"
        wc.to_file(imagePath)
        # QPicture、QImage、QPicture
        self.label.setPixmap(QPixmap(imagePath))
        self.label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())