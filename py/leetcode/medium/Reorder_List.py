# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:57

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

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
    # @return nothing
    def reorderList(self, head):
        if not head:
            return

        q = []
        h = head
        while h:
            q.append(h)
            h = h.next
        for i in range(len(q)//2):
            q[i].next = q[len(q)-i-1]
            q[len(q)-i-1].next = q[i+1]
        q[len(q)//2].next = None