# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 21:50

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect


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
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        h = head
        hn = head.next
        result = head.next
        pre = None
        while hn:
            hnn = hn.next
            h.next = hnn
            hn.next = h
            if pre:
                pre.next = hn
            pre = h
            h = hnn
            if h:
                hn = hnn.next
            else:
                hn = None
        return result



s = Solution()

l = ListNode(1)
l.next = ListNode(2)
node = l.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)

rl = s.swapPairs(l)
rl.output()