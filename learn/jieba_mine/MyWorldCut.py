#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : MyWorldCut.py
# @Date    : 2019-02-22
# @Author  : gaotao
import jieba


class MyWorldCut(object):
    # def getText(self,strPath):
    #     with open(strPath,mode="r",encoding="utf-8",errors="ignore") as f:
    #         line = f.readline().lower()
    #         while line:
    #             print(line)
    #             line = f.readline().lower()

    def getText(self,strPath):
        with open(strPath,mode="r",encoding="utf-8",errors="ignore") as f:
            line = f.read().lower()
            for ch in '|"#$%&()*+,_.?:;<=>@[\\]^_`{|}~':
                line.replace(ch, " ")
            return line

    def getcount(self, strPath):
        data = self.getText(strPath)
        words = data.split(" ")
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x:x[1], reverse=True)
        for i in range(10):
            word, count = items[i]
            print("{0:<10}{1:>5}".format(word,count))


if __name__ == '__main__':
    # strPath = "/Users/gaotao/PycharmProjects/py37/learn/jieba_mine/__init__.py"
    # cut = MyWorldCut()
    # cut.getcount(strPath)
    re = jieba.lcut("姚明是中国最牛的篮球运动员，乔丹是地球最牛篮球运动员，科比是我最喜欢的篮球运动员。")
    print(re)

