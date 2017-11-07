# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 21:14

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
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
    # @return a list of integers
    def rightSideView(self, root):
        if not root:
            return []

        node = root
        result = []
        q = [(root, 0)]
        pre_level = -1
        while q:
            node, level = q.pop(0)
            if q:
                next_node, next_level = q[0]
                if level != next_level:
                    result.append(node.val)
            else:
                result.append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return result




s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
print(s.rightSideView(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(s.rightSideView(root))