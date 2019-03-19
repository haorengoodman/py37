#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 17:07
# @Author  : journal
# @File    : OneLineCode.py
# @Software: PyCharm

__author__ = 'journal'

# ❤型图案
print('\n'.join([''.join([('ilove敬树萍'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))