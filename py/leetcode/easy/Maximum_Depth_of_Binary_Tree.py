# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 11:38

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
__author__ = 'huash06'

import sys
import os


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.maxDepth(root))

root = TreeNode(1)
root.right = TreeNode(2)
print(s.maxDepth(root))

root = TreeNode(1)
print(s.maxDepth(root))
root.left = TreeNode(2)
print(s.maxDepth(root))

root = TreeNode('#')
root.left = TreeNode(1)
root.right = TreeNode(2)
print(s.maxDepth(root))