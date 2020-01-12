#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 19:20
# @File    : Day08.py
# @Software: PyCharm

# Definition for singly-linked list
class ListNode(object):
     def __init__(self,x):
          self.val = x
          self.next = None
     def __str__(self):
         return str(self.val)


class Solution(object):
    def _addTwoNumbers(self,l1,l2):
        """
        :param l1: ListNode 
        :param l2: ListNode
        :return: ListNode
        """
        p = dummy = ListNode(-1)
        carry = 0
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            carry = p.next.val/10
            p.next.val %=10
            p = p.next
            l1 = l1.next
            l2 = l2.next

        res = l1 or l2
        while res:
            p.next = ListNode(res.val + carry)
            carry  = p.next.val / 10
            p.next.val %=10
            p = p.next
            res = res.next
        if carry:
            p.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    #sol = Solution()
    #sol._addTwoNumbers(l1,l2)