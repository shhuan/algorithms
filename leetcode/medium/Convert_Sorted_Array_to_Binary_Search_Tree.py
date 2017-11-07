# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 11:21

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.



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

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None

        return self.impl(num, 0, len(num))

    def impl(self, num, left, right):
        if left >= right:
            return None

        mid = (left + right) // 2
        root = TreeNode(num[mid])
        root.left = self.impl(num, left, mid)
        root.right = self.impl(num, mid+1, right)

        return root


s = Solution()
ls = [1, 3, 5, 7, 8, 9, 10]
print(ls)
troot = s.sortedArrayToBST(ls)

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