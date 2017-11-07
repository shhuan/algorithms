# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 10:59

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a
binary tree in which the depth of the two subtrees of every node never differ by more than 1.



需要注意记录高度


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
    # @return a boolean
    def isBalanced(self, root):
        return self.is_banlance_impl(root, 1)[0]
    def is_banlance_impl(self, root, level):
        if not root:
            return True, 1
        if not root.left and not root.right:
            return True, level
        if not root.left:
            r, l = self.is_banlance_impl(root.right, level+1)
            if r and l <= level + 1:
                return True, l
            else:
                return False, l
        if not root.right:
            r, l = self.is_banlance_impl(root.left, level+1)
            if r and l <= level + 1:
                return True, l
            else:
                return False, l
        r1, l1 = self.is_banlance_impl(root.left, level+1)
        r2, l2 = self.is_banlance_impl(root.right, level+1)
        if r1 and r2 and abs(l1 - l2) <= 1:
            return True, max(l1, l2)
        return False, max(l1, l2)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
left = root.left
left.left = TreeNode(3)
left.right = TreeNode(3)
left.left.left = TreeNode(3)
left.left.right = TreeNode(3)
print(s.isBalanced(root))

