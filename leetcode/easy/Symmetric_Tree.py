# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 11:44

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

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
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        mirror = TreeNode(root.val)
        self.mirror_of_tree(root, mirror)
        return self.is_same(root, mirror)
    def mirror_of_tree(self, root, mirror):
        if not root:
            return
        if not root.left and not root.right:
            return
        if root.left and root.right:
            mirror.right = TreeNode(root.left.val)
            mirror.left = TreeNode(root.right.val)
            self.mirror_of_tree(root.left, mirror.right)
            self.mirror_of_tree(root.right, mirror.left)
        elif not root.left:
            mirror.left = TreeNode(root.right.val)
            self.mirror_of_tree(root.right, mirror.left)
        else:
            mirror.right = TreeNode(root.left.val)
            self.mirror_of_tree(root.left, mirror.right)
    def is_same(self, root, mirror):
        if not root and not mirror:
            return True
        elif not root or not mirror:
            return False
        if root.val != mirror.val:
            return False
        return self.is_same(root.left, mirror.left) and self.is_same(root.right, mirror.right)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
mirror = TreeNode(root.val)
s.mirror_of_tree(root, mirror)
print(mirror)
print(s.isSymmetric(root))

root.right.right = TreeNode(3)
# root.right.left = TreeNode(3)
print(s.isSymmetric(root))