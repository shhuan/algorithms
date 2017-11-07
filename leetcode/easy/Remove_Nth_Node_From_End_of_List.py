# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 18:47


Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

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
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return head

        len_list = 0
        h = head
        while h:
            len_list += 1
            h = h.next

        if len_list <= 1:
            return None

        # remove the first node
        if len_list-n-1 < 0:
            h = head
            head = h.next
            h.next = None
            return head

        # remove other node
        l = head
        for i in range(len_list-n-1):
            l = l.next
        r = l.next
        l.next = r.next
        r.next = None
        return head



s = Solution()


root = ListNode(1)
node = ListNode(2)
root.next = node

node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)
node = node.next

root.output()
print()

print(s.removeNthFromEnd(root, 2).output())

root = ListNode(1)
root.next = ListNode(2)
print(s.removeNthFromEnd(root, 1).output())

root = ListNode(1)
root.next = ListNode(2)
print(s.removeNthFromEnd(root, 2).output())