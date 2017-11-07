# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 11:28

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#'
signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
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
    def levelOrderBottom(self, root):
        if not root:
            return []

        result = list()
        q = list()
        q.append((root, 1))
        while q:
            h, l = q.pop(0)
            if len(result) < l:
                result.append([h.val])
            else:
                result[l-1].append(h.val)
            if h.left:
                q.append((h.left, l+1))
            if h.right:
                q.append((h.right, l+1))
        return list(reversed(result))




s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
right = root.right
right.left = TreeNode(15)
right.right = TreeNode(7)

t = s.levelOrderBottom(root)
for r in t:
    print(','.join(list(map(str, r))))