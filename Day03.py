#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 10:16
# @File    : Day03.py
# @Software: PyCharm

#题目：10万以内 的一个整数，它加上100后是一个完全平方数
#再加上268 又是一个完全平方数
#请问该数是多少？

from math import sqrt

#如何判断一个数是不是完全平方数
#for num in range(1,20):
#    x= int(sqrt(num))
#    #print(x)
#    if (x*x == num):
#        print("{}是完全平方数".format(num))

for num in range(1,100000):
    x= int(sqrt(num+100))
    y = int(sqrt(num+268))
    if((x*x == num+100) and (y*y ==num+268 )):
        print("满足条件的数:{}".format(num))