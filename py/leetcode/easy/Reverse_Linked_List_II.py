# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 08:27


Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head or m > n:
            return
        listLen = 0
        h = head
        while h:
            h = h.next
            listLen += 1
        if m > listLen:
            return
        n = min(n, listLen)

        # 需要构造一个头结点
        result = ListNode(0)
        result.next = head
        h = result

        # 找到反转的第一个节点h
        l = 1
        while l < m:
            h = h.next
            l += 1

        # Reverse consecutive n-m nodes
        rh_pre = h.next
        rh = rh_pre.next
        for i in range(n-m):
            rh_next = rh.next
            rh.next = rh_pre
            rh_pre = rh
            rh = rh_next

        # revese front and tail
        h.next.next = rh
        h.next = rh_pre
        return result.next


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
node = l.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)
node = node.next
l.output()
print()

s.reverseBetween(l, 1, 7).output()
