# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 19:42

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

"""
__author__ = 'huash'

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
    # @return an integer
    def maxPathSum(self, root):

        return max(self.dfs(root))

    def dfs(self, root):
        """
        返回最大和，以及能够向上累加的最大和
        :param root:
        :return: max sum of this sub-tree, acuumulatable sum of left child, acuumulatable sum of left child
        """
        if not root:
            return -1000000, -1000000
        if not root.left and not root.right:
            return root.val, root.val

        leftMax, left = self.dfs(root.left)
        rightMax, right = self.dfs(root.right)

        return max(leftMax, rightMax, root.val+max(left, 0)+max(right, 0)),\
                max(root.val + max(left, 0), root.val + max(right, 0))


s = Solution()

root = TreeNode(-1)
root.left = TreeNode(5)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(2)
root.left.left.right.left = TreeNode(-4)
print(s.maxPathSum(root) == 11)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
print(s.maxPathSum(root) == 48)

root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(-3)
root.right.right = TreeNode(-1)
print(s.maxPathSum(root) == 3)

root = TreeNode(-1)
root.left = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
print(s.maxPathSum(root) == 3)

print(s.maxPathSum(TreeNode(1)) == 1)

root = TreeNode(1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
print(s.maxPathSum(root) == 1)

root = TreeNode(1)
root.left = TreeNode(-1)
root.right = TreeNode(1)
print(s.maxPathSum(root) == 2)

root = TreeNode(-1)
root.left = TreeNode(-1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print(s.maxPathSum(root) == 6)

root = TreeNode(-1)
root.left = TreeNode(-2)
print(s.maxPathSum(root) == -1)