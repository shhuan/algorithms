# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 21:26

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
__author__ = 'huash'

import sys
import os




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def output(self):
        print(self.val, end='->')
        if self.next:
            self.next.output()

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        """
        使用加减法代替除法和求余，是的速度从167ms -> 132ms
        %51 -> 95%
        :param l1:
        :param l2:
        :return:
        """

        if not l1:
            return l2
        if not l2:
            return l1

        h1 = l1.next
        h2 = l2.next

        v = l1.val + l2.val
        result = ListNode(v if v < 10 else v - 10)
        cap = 1 if v >= 10 else 0
        hr = result
        while h1 and h2:
            v = h1.val + h2.val + cap
            hr.next = ListNode(v if v < 10 else v - 10)
            hr = hr.next
            cap = 1 if v >= 10 else 0
            h1 = h1.next
            h2 = h2.next
        while h1:
            v = h1.val + cap
            hr.next = ListNode(v if v < 10 else v - 10)
            hr = hr.next
            h1 = h1.next
            cap = 1 if v >= 10 else 0
        while h2:
            v = h2.val + cap
            hr.next = ListNode(v if v < 10 else v - 10)
            hr = hr.next
            h2 = h2.next
            cap = 1 if v >= 10 else 0
        if cap > 0:
            hr.next = ListNode(cap)

        return result



s = Solution()

s1 = ListNode(2)
node = ListNode(4)
s1.next = node
node.next = ListNode(3)
node = node.next
node.next = ListNode(7)
s1.output()
print()

s2 = ListNode(5)
node = ListNode(6)
s2.next = node
node.next = ListNode(4)

s2.output()
print()

s.addTwoNumbers(s1, s2).output()
print()
print()

s1 = ListNode(9)
s1.next = ListNode(8)
s1.output()
print()

s2 = ListNode(1)
s2.output()
print()
s.addTwoNumbers(s1, s2).output()
print()
print()

s1 = ListNode(9)
s1.next = ListNode(8)
s2 = ListNode(1)
s.addTwoNumbers(s1, s2).output()