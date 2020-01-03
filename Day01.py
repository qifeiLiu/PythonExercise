#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 21:56
# @File    : Day01.py
# @Software: PyCharm

#题目：有1，2，3，4个数字，能组成多少个互不相同切无重复数字的三位数？都是多少
#方法1：
list = [1,2,3,4]
num=0
for i in list:
    for j in list:
        for k in list:
            if((i!=j) & (i!=k) & (j!=k)):
                num+=1
                print(num)
                print(i*100+j*10+k)

#方法2
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if((i!=j)and (i!=k) and (k!=j)):
                print(i,j,k)

