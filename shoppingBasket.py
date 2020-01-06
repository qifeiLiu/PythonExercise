#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 16:35
# @File    : shoppingBasket.py
# @Software: PyCharm

Goods_List=[
    ("iphone6s",58),
    ("mac book",9000),
    ("python book", 80),
    ("bicycle", 1500)
]
Goods_basket=[]
salary = input("请输入你的薪资:")
#print(Goods_List)
if salary.isdigit():
    for Good in enumerate(Goods_List,1):
        print(Good)
    while True:
        index = input(">>>")
        if index.isdigit():
            if((index >=1) and(index <=len(Goods_List))):
                Goods_basket.append((Goods_List[index-1][0], Goods_List[index-1][1]))
                print(index,".",Goods_List[index-1][0],Goods_List[index-1][1])
            if index == 0:
                break
        print(Goods_basket)




