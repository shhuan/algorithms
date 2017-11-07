# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:03


Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import py.lib.Utils as Utils

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        q = []
        node = root
        while node:
            q.append(node)
            node = node.left
        res = []
        while q:
            node = q.pop()
            res.append(node.val)
            if node.right:
                q.append(node.right)
                node = node.right.left
                while node:
                    q.append(node)
                    node = node.left
        return res

    def inorderTraversal2(self, root):
        q = []
        res = []
        p = root
        while p or q:
            while p:
                q.append(p)
                p = p.left
            if q:
                p = q.pop()
                res.append(p.val)
                p = p.right
        return res

    def morris(self, root):
        """
        while not end:
            if current node doesn't have left child:
                visit current node
                travel on right node
            else:
                find the most right child of the left child, and make it's right point to current node
                travel on left node
        :param root:
        :return:
        """
        if not root:
            return []
        node = root
        res = []
        while node:
            if not node.left:
                res.append(node.val)
                node = node.right
            else:
                tmp = node.left
                while tmp.right and tmp.right != node:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = node
                    node = node.left
                else:
                    res.append(node.val)
                    tmp.right = None
                    node = node.right
        return res


s = Solution()

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(3)
Utils.outputBinaryTree(root)
print(s.morris(root))
print(s.inorderTraversal(root))
