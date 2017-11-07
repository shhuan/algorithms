# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq

"""
created by shhuan at 2017/10/2 20:36


Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
    
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def dfs(node, val):
            if not node:
                return None

            if node.val == val:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    right = node.right
                    while right.left:
                        right = right.left
                    rightMin = right.val
                    node.val = rightMin
                    node.right = dfs(node.right, rightMin)
                    return node

            node.left = dfs(node.left, val)
            node.right = dfs(node.right, val)

            return node

        return dfs(root, key)




s = Solution()
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right.right = TreeNode(7)
print(s.deleteNode(t, 3))