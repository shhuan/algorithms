# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:55

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

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
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return None
        if k == 0:
            return head

        h = head
        l = 0
        while h:
            h = h.next
            l +=1
        if l == 1:
            return head
        k %= l
        if l == k or k == 0:
            return head

        h = head
        l0 = 1
        while l0 < l-k:
            h = h.next
            l0 += 1
        hn = h.next
        ret = hn
        h.next = None
        while hn.next:
            hn = hn.next
        hn.next = head
        return ret