# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 22:34

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):

        return self.dfs(root, k)[0]

    def dfs(self, root, k):
        if not root:
            return 0, k
        v, lk = self.dfs(root.left, k)
        if lk == 0:
            return v, 0
        if lk == 1:
            return root.val, 0
        return self.dfs(root.right, lk - 1)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

s = Solution()
for i in range(1, 6):
    print(s.kthSmallest(root, i))
