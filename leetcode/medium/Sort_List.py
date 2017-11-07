# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 20:47

Sort a linked list in O(n log n) time using constant space complexity.

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
    # @return {ListNode}
    def sortList(self, head):
        if not head:
            return None
        l = 0
        h = head
        while h:
            l += 1
            h = h.next
        return self.mergeSort(head, l)


    def mergeSort(self, head, lenlist):
        if lenlist == 1:
            return head
        elif lenlist == 2:
            if head.val > head.next.val:
                tmp = head.val
                head.val = head.next.val
                head.next.val = tmp
            return head

        h = head
        l = 1
        while l < lenlist // 2:
            h = h.next
            l += 1
        nh = h.next
        h.next = None
        h1 = self.mergeSort(head, l)
        h2 = self.mergeSort(nh, lenlist-l)
        return self.mergeList(h1, h2)


    def mergeList(self, head1, head2):
        if not head2:
            return head1
        elif not head1:
            return head2

        ret = ListNode(-1000000)
        h1 = head1
        h2 = head2
        h = ret
        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        if h1:
            h.next = h1
        if h2:
            h.next = h2

        return ret.next



s = Solution()
s.sortList(ListNode(0)).output()
print()

l = ListNode(1)
l.next = ListNode(4)
node = l.next
vals = [3, 2, 5, 2]
for val in vals:
    node.next = ListNode(val)
    node = node.next
l.output()
print()
s.sortList(l).output()
print()
