# -*- coding: utf-8 -*-

"""
created by '' at 2015/9/3 17:50

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.dfs(root, "")
        
        
    def dfs(self, node, path):
        if not node:
            return [path]

        path = "{}".format(node.val) if not path else "{}->{}".format(path, node.val)
        if not node.left and not node.right:
            return [path]
        
        result = []
        if node.left:
            result.extend(self.dfs(node.left, path))
        if node.right:
            result.extend(self.dfs(node.right, path))
            
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(root))

root = TreeNode(1)
print(s.binaryTreePaths(root))