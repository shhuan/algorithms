# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:47


Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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
    def deleteDuplicates(self, head):
        if not head:
            return None
        if not head.next:
            return head

        ret = ListNode(0)
        ret.next = head
        hp = ret
        h = hp.next
        hn = h.next
        while h and hn:
            if hn.val == h.val:
                while hn and h.val == hn.val:
                    hn = hn.next
                h = hn
                if h:
                    hn = h.next
                continue
            hp.next = h
            hp = h
            h = None
            hn = None
            if hp:
                h = hp.next
                if h:
                    hn = h.next
        hp.next = h
        return ret.next