# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 15:03

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not inorder or len(inorder) != len(preorder):
            return None

        return self.impl(preorder, inorder, 0, len(preorder), 0, len(inorder))

    def impl(self, preorder, inorder, preleft, preright, inleft, inright):
        if inleft >= inright:
            return None
        if inleft == inright-1:
            return TreeNode(inorder[inleft])

        root = TreeNode(preorder[preleft])
        i = inorder.index(preorder[preleft], inleft, inright)
        root.left = self.impl(preorder, inorder, preleft+1, preleft+i-inleft+1, inleft, i)
        root.right = self.impl(preorder, inorder, preleft+i-inleft+1, preright, i+1, inright)
        return root



def outputTree(root, height):
    if not root:
        return
    q = [(root, 1, 1 << height)]
    preLeve = 0
    while q:
        node, level, space = q.pop(0)
        if level != preLeve:
            print()
            preLeve = level
            print(''.join([' ']*max(space-2, 1)), end='')

        print(' {}'.format(+node.val), end='')
        if node.left:
            q.append((node.left, level+1, space-2))
        if node.right:
            q.append((node.right, level+1, space+1))

s = Solution()
outputTree(s.buildTree([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]), 3)