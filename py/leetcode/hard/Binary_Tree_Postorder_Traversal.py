# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 22:26

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""
__author__ = 'huash'

import sys
import os
import collections

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        """
        使用一个变量pre纪录当前节点的孩子节点是否访问过，
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        q = [root]
        pre = None
        while q:
            cur = q[-1]
            if (not cur.left and not cur.right) or \
                (pre and (pre == cur.left or pre == cur.right)):
                res.append(cur.val)
                pre = q.pop()
            else:
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return res
    def postorderTraversal2(self, root):
        """
        使用一个变量纪录是第几次访问当前节点
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        q = [(root, 0)]

        while q:
            node, time = q.pop()
            if time > 0 or (not node.left and not node.right):
                res.append(node.val)
            else:
                q.append((node, 1))
                if node.right:
                    q.append((node.right, 0))
                if node.left:
                    q.append((node.left, 0))
        return res



s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
print(s.postorderTraversal(root))
print(s.postorderTraversal2(root))