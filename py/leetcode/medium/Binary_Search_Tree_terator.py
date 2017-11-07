"""

created by huash06 at 2015-04-15

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.nodeTrace = []
        node = root
        while node:
            self.nodeTrace.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.nodeTrace) > 0

    # @return an integer, the next smallest number
    def next(self):
        if len(self.nodeTrace) <= 0:
            return None
        node = self.nodeTrace.pop(-1)
        result = node.val
        node = node.right
        while node:
            self.nodeTrace.append(node)
            node = node.left
        return result

# Your BSTIterator will be called like this:

root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print(v)

root = TreeNode(1)
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print(v)

