# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 11:57

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

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
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and \
               self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)
        

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.isSameTree(root, root))

root1 = TreeNode(1)
root1.right = TreeNode(2)
print(s.isSameTree(root, root1))
