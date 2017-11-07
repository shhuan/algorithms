
# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 17:13

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
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
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        """
        二叉查找树中序遍历是递增序列，通过中序遍历即可找出两个位置错误的节点
        :param root:
        :return:
        """
        if not root:
            return

        if not root:
            return []

        q = []
        node = root
        wrong1 = None
        wrong2 = None
        preNode = None
        while node:
            q.append(node)
            node = node.left
        while q:
            node = q.pop()
            # ret.append(node.val)
            if preNode and preNode.val > node.val:
                if not wrong1:
                    wrong1 = preNode
                wrong2 = node
            preNode = node
            if node.right:
                q.append(node.right)
                node = node.right.left
                while node:
                    q.append(node)
                    node = node.left
        if wrong1 and wrong2:
            wrong1.val, wrong2.val = wrong2.val, wrong1.val


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
        wrong1 = None
        wrong2 = None
        preNode = None
        while node:
            if not node.left:
                # res.append(node.val)
                if preNode and preNode.val > node.val:
                    if not wrong1:
                        wrong1 = preNode
                    wrong2 = node
                preNode = node
                node = node.right
            else:
                tmp = node.left
                while tmp.right and tmp.right != node:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = node
                    node = node.left
                else:
                    # res.append(node.val)
                    if preNode and preNode.val > node.val:
                        if not wrong1:
                            wrong1 = preNode
                        wrong2 = node
                    preNode = node
                    tmp.right = None
                    node = node.right
        if wrong1 and wrong2:
            wrong1.val, wrong2.val = wrong2.val, wrong1.val




s = Solution()

root = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(1)
Utils.outputBinaryTree(root)
s.recoverTree(root)
Utils.outputBinaryTree(root)


root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.recoverTree(root)
Utils.outputBinaryTree(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)
Utils.outputBinaryTree(root)


root = TreeNode(2)
root.right = TreeNode(1)
root.right.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.recoverTree(root)
Utils.outputBinaryTree(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.recoverTree(root)
Utils.outputBinaryTree(root)

root = TreeNode(2)
Utils.outputBinaryTree(root)
s.recoverTree(root)
Utils.outputBinaryTree(root)

s.recoverTree(None)


print('======Morris======')
root = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(1)
Utils.outputBinaryTree(root)
s.morris(root)
Utils.outputBinaryTree(root)


root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.morris(root)
Utils.outputBinaryTree(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)
Utils.outputBinaryTree(root)


root = TreeNode(2)
root.right = TreeNode(1)
root.right.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.morris(root)
Utils.outputBinaryTree(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
Utils.outputBinaryTree(root)
s.morris(root)
Utils.outputBinaryTree(root)

root = TreeNode(2)
Utils.outputBinaryTree(root)
s.morris(root)
Utils.outputBinaryTree(root)

s.morris(None)