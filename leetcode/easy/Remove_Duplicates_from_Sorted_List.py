# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 13:56

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""
__author__ = 'huash06'

import sys
import os


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
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return

        h = head
        while h:
            n = h.next
            while n and n.val == h.val:
                n = n.next
            h.next = n
            h = h.next
        return head


s = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.output()
print()

s.deleteDuplicates(head)
head.output()
print()

head = ListNode(1)
head.output()
print()
s.deleteDuplicates(head)
head.output()