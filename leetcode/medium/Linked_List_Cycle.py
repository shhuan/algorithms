# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:03

Given a linked list, determine if it has a cycle in it.

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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False

        h = head
        hh = h.next
        if hh:
            hh = hh.next
        else:
            return False

        while h and hh:
            if h == hh:
                return True
            h = h.next
            hh = hh.next
            if hh:
                hh = hh.next
            else:
                return False

        return False