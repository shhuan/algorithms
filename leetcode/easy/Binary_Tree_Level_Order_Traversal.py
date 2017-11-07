# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 11:40

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
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
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        q = list()
        q.append((root, 0))
        result = list()
        while q:
            h, l = q.pop(0)
            if l >= len(result):
                result.append([])
            result[l].append(h.val)
            if h.left:
                q.append((h.left, l+1))
            if h.right:
                q.append((h.right, l+1))
        return result


s = Solution()
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
right = root.right
right.left = TreeNode(15)
right.right = TreeNode(7)

t = s.levelOrder(root)
for r in t:
    print(','.join(list(map(str, r))))