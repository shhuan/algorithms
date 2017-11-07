# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 18:59

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

"""
__author__ = 'huash'

import sys
import os
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
        BFS
        :param root:
        :return:
        """
        if not root:
            return

        currentLevel, nextLevel = collections.deque([root]), collections.deque()
        while currentLevel:
            node = currentLevel.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            node.next = currentLevel[0] if currentLevel else None
            if not currentLevel and nextLevel:
                currentLevel, nextLevel = nextLevel, currentLevel


    def connect2(self, root):
        """
        把上面的bfs转换为常数空间
        :param root:
        :return:
        """
        if not root:
            return

        # 遍历上一层的时候把构建下一层的next
        currentLevel, nextLevel, currentNode = root, None, None
        while currentLevel:
            if currentLevel.left:
                if not nextLevel:
                    nextLevel = currentNode = currentLevel.left
                else:
                    currentNode.next = currentLevel.left
                    currentNode = currentNode.next
            if currentLevel.right:
                if not nextLevel:
                    nextLevel = currentNode = currentLevel.right
                else:
                    currentNode.next = currentLevel.right
                    currentNode = currentNode.next
            currentLevel = currentLevel.next
            if not currentLevel and nextLevel:
                currentLevel, nextLevel, currentNode = nextLevel, None, None




s = Solution()
# root = TreeLinkNode(1)
# root.left = TreeLinkNode(2)
# root.left.left = TreeLinkNode(4)
# root.left.right = TreeLinkNode(5)
# root.right = TreeLinkNode(3)
# root.right.right = TreeLinkNode(7)
# s.connect(root)
#
# q = [root]
# while q:
#     node = q.pop(0)
#     if node.left:
#         q.append(node.left)
#     while node:
#         sys.stdout.write('{} -> '.format(node.val))
#         node = node.next
#     print('')

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.right = TreeLinkNode(5)
root.left.left = TreeLinkNode(4)
root.left.left.left = TreeLinkNode(7)
root.left.right = TreeLinkNode(5)
root.right = TreeLinkNode(3)
root.right.right = TreeLinkNode(6)
root.right.right.right = TreeLinkNode(8)
s.connect2(root)

q = [root]
while q:
    node = q.pop(0)

    nextLevel = None
    while node:
        if not nextLevel:
            if node.left:
                nextLevel = node.left
            elif node.right:
                nextLevel = node.right
        sys.stdout.write('{} -> '.format(node.val))
        node = node.next
    if nextLevel:
        q.append(nextLevel)
    print('')