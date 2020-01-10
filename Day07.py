#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 7:34
# @File    : Day07.py
# @Software: PyCharm

#给定一个整数数组和一个目标值,找出数组中和为目标值的两个数
#你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用
#示例：nums =[2,7,11,15],target = 9
#因为 nums[0] + nums[1] = 2 + 7 =9
#所以返回 [0，1]


nums = [1,2,3,4,5,6,7,8,9,10]
target = 9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print("[{0},{1}]".format(i,j))

# 提供的答案
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        d ={}
        #print(enumerate(nums))
        for i,num in enumerate(nums):
            if target - num in d:
                return [d[target-num],i]
            d[num]=i
            print(d)

if __name__ == "__main__":
    solu = Solution()
    print(solu.twoSum(nums,target))