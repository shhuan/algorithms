# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:59

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return None


        h1 = head
        h2 = head.next
        k1 = 1
        k2 = 2

        while h1 and h2 and h1 != h2:
            h1 = h1.next
            h2 = h2.next
            if not h1 or not h2:
                return None
            h2 = h2.next
            k1 += 1
            k2 += 2
        if not h1 or not h2:
            return None

        dk = k2-k1
        for k in range(1, dk+1):
            if dk % k == 0:
                h1 = head
                h2 = head
                for i in range(k):
                    h2 = h2.next
                for i in range(k1):
                    if h1 == h2:
                        return h1
                    h1 = h1.next
                    h2 = h2.next
        return None