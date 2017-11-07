# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:53


Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

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
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []

        q = []
        result = []
        node = root
        while node:
            result.append(node.val)
            q.append(node)
            node = node.left
        while q:
            node = q.pop()
            right = node.right
            if right:
                result.append(right.val)
                q.append(right)
                rleft = right.left
                while rleft:
                    q.append(rleft)
                    result.append(rleft.val)
                    rleft = rleft.left
        return result

    def preorderTraversal2(self, root):
        q = []
        res = []
        p = root
        while p or q:
            while p:
                res.append(p.val)
                q.append(p)
                p = p.left
            if q:
                p = q.pop()
                p = p.right

        return res
