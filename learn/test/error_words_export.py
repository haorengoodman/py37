#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
纠错结果报表生成工具
"""

import pymysql
import xlwt
import xlrd
import argparse

import json

db = pymysql.connect("10.125.8.31", 'vision', 'Xinhuanet603888', 'depart', charset='utf8')
# ap = argparse.ArgumentParser()
# ap.add_argument("-type", default="cms", required=False, help="type name")
# ap.add_argument("-strategyName", default="混淆集纠错", required=False, help="strattegyName")
# ap.add_argument("-time", default="", required=True, help="time")
# args = ap.parse_args()


def create_errors_2_excel(type, strategy, time):
    beginTime = "20190308000000"
    endTime = "20190308235959"
    c_cursor = db.cursor()
    c_cursor.execute(
        "select id,errorWord,txt,url,siteName,origin,strategyName,releaseTime from errordata  where ntype = '" + type + "' and strategyName = '" + strategy + "' and releaseTime between '" + beginTime + "' and '" + endTime + "'")

    c_res = c_cursor.fetchall()

    # with io.open(file_name, 'w', encoding='utf-8') as f:
    book = xlwt.Workbook()
    sheet = book.add_sheet('case1_sheet')
    # style = xlwt.easyxf('align: wrap on')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    style.font = font  # 设定样式
    style.alignment.wrap = 1  # 自动换行

    zero_col = sheet.col(0)  # xlwt中是行和列都是从0开始计算的
    zero_col.width = 256 * 20

    first_col = sheet.col(1)  # xlwt中是行和列都是从0开始计算的
    first_col.width = 256 * 50

    sec_col = sheet.col(2)  # xlwt中是行和列都是从0开始计算的
    sec_col.width = 256 * 150

    r = 0  # 行
    for row in c_res:
        # s = "%s %d %s \n" % (row[1], row[2], str.strip(row[3]))
        xx = json.loads(row[1])
        txt = []
        for c in range(8):
            estr = ""
            if c == 1:
                # print(xx)
                for x in xx:
                    estr += x["errorWord"] + " : " + "|".join(x["corWord"]) + '\n'
                    pos = int(x["pos"])
                    start = pos - 30
                    mid = len(x["errorWord"])
                    if start < 0:
                        start = 0
                    end = pos + 30
                    if end > len(row[2]):
                        end = len(row[2])
                    txt.append(
                        row[2][start:pos] + "####" + row[2][pos:pos + mid] + "####" + row[2][pos + mid:end] + "\n")
                sheet.write(r, c, estr, style)
            elif c == 3:
                estr = xlwt.Formula('HYPERLINK("' + row[c] + '";"' + row[c] + '")')
                sheet.write(r, c, estr)
            elif c == 2:
                estr = "".join(txt)
                sheet.write(r, c, estr, style)
            else:
                estr = row[c]
                sheet.write(r, c, str(estr))
        r += 1
    c_cursor.close()
    book.save("D:\\a-doc\\Users\\tmp\\"+beginTime+"-"+type+"-"+strategy+".xls")


if __name__ == '__main__':
    create_errors_2_excel('cms', '混淆集纠错', 'time')
    # create_errors_2_excel(args.type, args.strategyName, args.time)
