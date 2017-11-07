# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 08:58

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

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
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return

        ret = ListNode(0)
        ret.next = head
        h = ret
        while h and h.next:
            while h.next and h.next.val == val:
                h.next = h.next.next
            h = h.next
        return ret.next
