# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-15 22:55

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        return list(self.pathSumImpl(root, sum, root.val, [root.val]))

    def pathSumImpl(self, root, target, count, nums):
        # 从叶子节点返回
        if not root or (not root.left and not root.right):
            if count == target:
                return [nums]
            else:
                return []

        ln = []
        rn = []
        if root.left:
            ln = self.pathSumImpl(root.left, target, count+root.left.val, nums+[root.left.val])
        if root.right:
            rn = self.pathSumImpl(root.right, target, count+root.right.val, nums+[root.right.val])
        # 其他节点只负责传递结果
        ln.extend(rn)
        return ln








s = Solution()
root = TreeNode(5)
node = TreeNode(4)
node.left = TreeNode(11)
node.left.left = TreeNode(7)
node.left.right = TreeNode(2)
root.left = node
node = TreeNode(8)
node.left = TreeNode(13)
node.right = TreeNode(4)
node.right.left = TreeNode(5)
node.right.right = TreeNode(1)
root.right = node

# l = [1, 2, 3]
# print(l)
# l.extend([])
# print(l)
# l.extend([2])
# print(l)
print(s.pathSum(root, 22))
print('')
print('')

root = TreeNode(7)
node = TreeNode(0)
root.left = node
node.left = TreeNode(-1)
node.right = TreeNode(-6)
node = node.left
node.right = TreeNode(1)
node = node.right
node.right = TreeNode(-7)
print(s.pathSum(root, 0))