# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 20:25

Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


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
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head:
            return None
        ret = ListNode(0)
        ret.next = head
        hl = ret.next
        hg = ret.next
        while True:
            while hl and hl.val < x:
                hl = hl.next
            if not hl:
                break
            hg = hl.next

            #把所以大于x的node右移动一位
            while hg and hg.val >= x:
                hg = hg.next
            if not hg:
                break

            h = hl.next
            tmp = hl.val
            hl.val = hg.val
            while True:
                v = h.val
                h.val = tmp
                tmp = v
                if h == hg:
                    break
                h = h.next
        return ret.next





s = Solution()
l = ListNode(1)
l.next = ListNode(4)
node = l.next
vals = [3, 2, 5, 2]
for val in vals:
    node.next = ListNode(val)
    node = node.next
l.output()
print()
s.partition(l, 3).output()
print()

s.partition(ListNode(0), 1).output()