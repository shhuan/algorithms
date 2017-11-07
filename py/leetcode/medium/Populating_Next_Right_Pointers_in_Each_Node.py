# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 09:11


Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree
(ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        需要使用常数空间

        :param root:
        :return:
        """
        if not root:
            return



        # 使用辅助队列，O(n)空间
        # q = [(root, 1)]
        # while len(q) > 0:
        #     node, level = q.pop(0)
        #     if q:
        #         nextNode, nextNodeLevel = q[0]
        #         if nextNodeLevel == level:
        #             node.next = nextNode
        #     if node.left:
        #         q.append((node.left, level+1))
        #     if node.right:
        #         q.append((node.right, level+1))


        # 常数空间
        if root.left and root.right:
            leftRight = root.left
            rightLeft = root.right
            while leftRight and rightLeft:
                leftRight.next = rightLeft
                leftRight = leftRight.right
                rightLeft = rightLeft.left
        self.connect(root.left)
        self.connect(root.right)



s = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.left = TreeLinkNode(4)
node = root.left.left
node.left = TreeLinkNode(8)
node.right = TreeLinkNode(9)
root.left.right = TreeLinkNode(5)
node = root.left.right
node.left = TreeLinkNode(10)
node.right = TreeLinkNode(11)
root.right = TreeLinkNode(3)
root.right.left = TreeLinkNode(6)
node = root.right.left
node.left = TreeLinkNode(12)
node.right = TreeLinkNode(13)
root.right.right = TreeLinkNode(7)
node = root.right.right
node.left = TreeLinkNode(14)
node.right = TreeLinkNode(15)
s.connect(root)

q = [root]
while q:
    node = q.pop(0)
    if node.left:
        q.append(node.left)
    while node:
        sys.stdout.write('{} -> '.format(node.val))
        node = node.next
    print('')