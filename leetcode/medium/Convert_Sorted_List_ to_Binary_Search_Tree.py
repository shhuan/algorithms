# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 10:55

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None

        hlen = 0
        h = head
        while h:
            hlen += 1
            h = h.next

        mid = hlen // 2

        h = head
        i = 0
        while i < mid:
            i += 1
            h = h.next
        troot = TreeNode(h.val)
        troot.left = self.impl(head, mid)
        troot.right = self.impl(h.next, hlen-mid-1)

        return troot

    def impl(self, head, length):
        if not head or length <= 0:
            return None

        h = head
        i = 0
        mid = length // 2
        while i < mid:
            h = h.next
            i += 1
        troot = TreeNode(h.val)
        troot.left = self.impl(head, mid)
        troot.right = self.impl(h.next, length-mid-1)
        return troot


s = Solution()

ls = [1, 3, 5, 7, 8, 9, 10]
l = ListNode(ls[0])
node = l
for i in range(1, len(ls)):
    node.next = ListNode(ls[i])
    node = node.next

l.output()

troot = s.sortedListToBST(l)

q = [(troot, 1)]
preLeve = 0
while q:
    node, level = q.pop(0)
    if level != preLeve:
        print()
        preLeve = level
    print(node.val, end='  ')
    if node.left:
        q.append((node.left, level+1))
    if node.right:
        q.append((node.right, level+1))
