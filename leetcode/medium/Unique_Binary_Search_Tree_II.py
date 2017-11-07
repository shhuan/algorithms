# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:42

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

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
    # @return a list of tree node
    def generateTrees(self, n):
        if n <= 0:
            return [None]

        return self.impl(1, n)

    def impl(self, left, right):
        if left == right:
            return [TreeNode(left)]
        elif left > right:
            return [None]

        result = []
        for i in range(left, right+1):
            lefts = self.impl(left, i-1)
            rights = self.impl(i+1, right)
            for lc in lefts:
                for rc in rights:
                    root = TreeNode(i)
                    root.left = lc
                    root.right = rc
                    result.append(root)

        return result