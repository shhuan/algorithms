# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 10:48

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Show Tags


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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        result = ListNode(0)
        h1 = l1
        h2 = l2
        hr = result
        while h1 and h2:
            if h1.val <= h2.val:
                hr.next = ListNode(h1.val)
                hr = hr.next
                h1 = h1.next
            else:
                hr.next = ListNode(h2.val)
                hr = hr.next
                h2 = h2.next
        while h1:
            hr.next = ListNode(h1.val)
            hr = hr.next
            h1 = h1.next
        while h2:
            hr.next = ListNode(h2.val)
            hr = hr.next
            h2 = h2.next
        return result.next



s = Solution()

l1 = ListNode(2)
l1.next = ListNode(7)

l2 = ListNode(3)
l2.next = ListNode(9)

s.mergeTwoLists(l1, l2).output()