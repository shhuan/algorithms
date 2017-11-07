# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 10:56

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
    def minDepth1(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth(self, root):
        if not root:
            return 0

        q = []
        q.append((root, 1))
        while q:
            h, l = q.pop(0)
            if not h.left and not h.right:
                return l
            if h.left:
                q.append((h.left, l+1))
            if h.right:
                q.append((h.right, l+1))



s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.minDepth(root))

root = TreeNode(1)
root.right = TreeNode(2)
print(s.minDepth(root))

root = TreeNode(1)
print(s.minDepth(root))
root.left = TreeNode(2)
print(s.minDepth(root))

root = TreeNode('#')
root.left = TreeNode(1)
root.right = TreeNode(2)
print(s.minDepth(root))



