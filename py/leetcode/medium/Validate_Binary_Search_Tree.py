# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 22:15

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

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
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True

        valid = True
        if root.left:
            left = root.left
            while left.right:
                left = left.right
            valid = left.val < root.val

        if valid and root.right:
            right = root.right
            while right.left:
                right = right.left
            valid = right.val > root.val

        return valid and self.isValidBST(root.left) and self.isValidBST(root.right)

s = Solution()


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

print(s.isValidBST(root))
root.right.right = TreeNode(3)
print(s.isValidBST(root))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(s.isValidBST(root))