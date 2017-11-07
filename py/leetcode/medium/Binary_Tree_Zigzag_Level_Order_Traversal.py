# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 15:14

Given a binary tree, return the zigzag level order traversal of its nodes' values.

(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

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
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        qp = [root]
        qr = []
        positive = True
        result = []
        while True:
            row = []
            if positive:
                if not qp:
                    break
                while qp:
                    node = qp.pop(0)
                    row.append(node.val)
                    if node.left:
                        qr.append(node.left)
                    if node.right:
                        qr.append(node.right)
            else:
                if not qr:
                    break
                while qr:
                    node = qr.pop(0)
                    row.insert(0, node.val)
                    if node.left:
                        qp.append(node.left)
                    if node.right:
                        qp.append(node.right)
            result.append(row)
            positive = not positive
        return result

s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.zigzagLevelOrder(root))