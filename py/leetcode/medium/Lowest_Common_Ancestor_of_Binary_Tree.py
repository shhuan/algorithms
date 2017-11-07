# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/4 15:05


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        168ms
        Your runtime beats 97.93% of python coders.

        使用LCA的在线算法，找p、q的最近公共祖先即找p到q的最短路径中的深度最小的结点。
        1. 做DFS，把每次遇到的结点和它的深度存储在E当中
        2. 使用字典R记录每个结点第一次出现时候在E中的下标
        3. 找E[R[p]: R[q]+1]中深度最小的结点

        在多次查询中，步骤3可以使用ST实现，ST是在线算法
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if q == p:
            return q

        E = []
        R = {}

        self.dfs(root, 0, E, R)

        start = R[p]
        end = R[q]
        if start > end:
            start, end = end, start

        result = 0
        height = 1 << 31
        for i in range(start, end+1):
            v, h = E[i]
            if h < height:
                height = h
                result = v

        return result


    def dfs(self, node, height, E, R):
        if not node:
            return
        E.append((node.val, height))
        if node.val not in R:
            R[node] = len(E) - 1

        if node.left:
            self.dfs(node.left, height + 1, E, R)
            # dfs回溯的时候也要记录
            E.append((node.val, height))

        if node.right:
            self.dfs(node.right, height + 1, E, R)
            E.append((node.val, height))


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(-2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

s = Solution()
print(s.lowestCommonAncestor(root, root.left, root.right))
print(s.lowestCommonAncestor(root, root.left, root.left.right.right))