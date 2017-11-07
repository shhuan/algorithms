# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 14:19

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

"""
__author__ = 'huash'

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
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k < 1:
            return None
        if k == 1:
            return head

        h = head
        listLen = 0
        while h:
            listLen += 1
            h = h.next
        if listLen < k:
            return head

        h = head
        helpNode = ListNode(0)
        res = None
        hnext = h
        pres = None
        while listLen >= k:
            helpNode.next = h

            hnext = h
            hbk = h
            h = helpNode
            dk = 0
            while dk < k:
                tmp = hnext.next
                hnext.next = h
                h = hnext
                hnext = tmp
                dk += 1
            hbk.next = hnext
            if pres:
                pres.next = h
            pres = hbk
            if not res:
                res = h
            h = hnext
            listLen -= k
        return res



s = Solution()
l = ListNode(1)
h = l
for i in range(2, 6):
    h.next = ListNode(i)
    h = h.next

l.output()
print()
s.reverseKGroup(l, 2).output()