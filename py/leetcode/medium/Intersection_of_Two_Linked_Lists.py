# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 09:37


Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.



"""
__author__ = 'huash'

import sys
import os

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):

        if not headA or not headB:
            return None

        lenA = 1
        ha = headA
        while ha.next:
            lenA += 1
            ha = ha.next

        lenB = 1
        hb = headB
        while hb.next:
            lenB += 1
            hb = hb.next

        ha = headA
        hb = headB
        if lenA > lenB:
            for k in range(lenA-lenB):
                ha = ha.next
        elif lenA < lenB:
            for k in range(lenB-lenA):
                hb = hb.next

        while ha and hb and ha.val != hb.val:
            ha = ha.next
            hb = hb.next

        if ha:
            return ha
        return None




s = Solution()

l1 = ListNode('a1')
l1.next = ListNode('a2')
nn = l1.next
nn.next = ListNode('c1')
nn = nn.next
nn.next = ListNode('c2')
nn = nn.next
nn.next = ListNode('c3')

l2 = ListNode('b1')
l2.next = ListNode('b2')
nn = l2.next
nn.next = ListNode('b3')
nn = nn.next
nn.next = ListNode('c1')
nn = nn.next
nn.next = ListNode('c2')
nn = nn.next
nn.next = ListNode('c3')

print(s.getIntersectionNode(l1, l2))
