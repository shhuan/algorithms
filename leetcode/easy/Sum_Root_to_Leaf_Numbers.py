# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 21:59


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

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
    def sumNumbers(self, root):
        if not root:
            return 0
        return self.sumImpl(root, 0)


    def sumImpl(self, root, num):
        # print('root {} num={}'.format(root, num))
        if not root:
            return int(num)
        if not root.left and not root.right:
            return int('{}{}'.format(num, root.val))
        l = 0
        if root.left:
            l = self.sumImpl(root.left, '{}{}'.format(num, root.val))
        r = 0
        if root.right:
            r = self.sumImpl(root.right, '{}{}'.format(num, root.val))
        # print('{}+{}={}'.format(l, r, l+r))
        result = l + r
        return result



s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(s.sumNumbers(root))