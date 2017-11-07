# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 14:14

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        h = head
        hn = h.next
        h.next = None
        while h and hn:
            hnn = hn.next
            hn.next = h
            h = hn
            hn = hnn
        return h


    def reverseListUsingRecursion(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


s = Solution()

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)

h = s.reverseList(head)
hs = []
while h:
    hs.append(str(h.val))
    h = h.next
print(''.join(hs))


