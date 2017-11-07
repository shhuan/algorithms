# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:51

Sort a linked list using insertion sort.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None

        helper = ListNode(-1000000)
        last = helper
        node = head
        maxval = -1000000
        minval = 1000000
        while node:
            nn = node.next

            if node.val <= minval:
                minval = node.val
                node.next = helper.next
                helper.next= node
                if last == helper:
                    last = node
                    maxval = node.val
            elif node.val >= maxval:
                maxval = node.val
                node.next = None
                last.next = node
                last = node
            else:
                h = helper
                while h.next and h.next.val < node.val:
                    h = h.next
                hn = h.next
                h.next = node
                node.next = hn
            node = nn

        return helper.next

