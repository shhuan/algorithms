# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 14:25

Given inorder and postorder traversal of a tree, construct the binary tree.



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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or len(inorder) != len(postorder):
            return None

        # out of memory, too many string split
        # root = TreeNode(postorder[-1])
        # i = inorder.index(postorder[-1])
        #
        # root.left = self.buildTree(inorder[:i], postorder[:i])
        # root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        #
        # return root


        return self.impl(inorder, postorder, 0, len(inorder), 0, len(postorder))

    def impl(self, inorder, postorder, inleft, inright, postleft, postright):
        if inleft >= inright:
            return None
        if inleft == inright-1:
            return TreeNode(inorder[inleft])
        root = TreeNode(postorder[postright-1])
        i = inorder.index(postorder[postright-1], inleft, inright)
        root.left = self.impl(inorder, postorder, inleft, i, postleft, postleft+i-inleft)
        root.right = self.impl(inorder, postorder, i+1, inright, postleft+i-inleft, postright-1)
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
outputTree(s.buildTree([2, 1, 4, 3, 5], [2, 4, 5, 3, 1]), 3)