# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 11:26

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

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
    def outputRight(self):
        print(self.val, end='->')
        if self.right:
            self.right.outputRight()

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return

        left = root.left
        if left:
            right = root.right
            root.left = None
            root.right = left

            leftRight = left
            while leftRight and (leftRight.left or leftRight.right):
                leftRight = leftRight.right if leftRight.right else leftRight.left
            if leftRight:
                leftRight.right = right

        self.flatten(root.right)




    def impl(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root

        left = self.impl(root.left)
        if left:
            root.left = None
            left.right = root.right
            root.right = left
        return self.impl(root.right)




def outputTree(root):
    if not root:
        return
    q = [(root, 1)]
    preLeve = 0
    while q:
        node, level = q.pop(0)
        if level != preLeve:
            print()
            preLeve = level
        print(node.val, end='  ')
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))

s = Solution()

print('======CASE 1======')
troot = TreeNode(1)
troot.left = TreeNode(2)
troot.right = TreeNode(5)
troot.left.left = TreeNode(3)
troot.left.right = TreeNode(4)
troot.right.right = TreeNode(6)
outputTree(troot)
print()
print('======AFTER FLATTED======')
s.flatten(troot)
troot.outputRight()
outputTree(troot)
print()

print('======CASE 2======')
troot = TreeNode(1)
troot.right = TreeNode(2)
troot.right.left = TreeNode(3)
outputTree(troot)
print()
print('======AFTER FLATTED======')
s.flatten(troot)
troot.outputRight()
outputTree(troot)
print()


print('======CASE 3======')
troot = TreeNode(3)
troot.right = TreeNode(4)
troot.left = TreeNode(1)
troot.left.right = TreeNode(2)
outputTree(troot)
print()
print('======AFTER FLATTED======')
s.flatten(troot)
troot.outputRight()
outputTree(troot)
print()


print('======CASE 4======')
troot = TreeNode(1)
troot.right = TreeNode(3)
troot.right.left = TreeNode(2)
troot.right.right = TreeNode(4)
outputTree(troot)
print()
print('======AFTER FLATTED======')
s.flatten(troot)
troot.outputRight()
outputTree(troot)