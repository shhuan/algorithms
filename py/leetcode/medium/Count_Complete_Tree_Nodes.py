# -*- coding: utf-8 -*-
"""

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h

"""
__author__ = 'huash'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    180ms
    Your runtime beats 94.83% of python coders.

    如果当前沿着最左边和沿着最右边走到底的高度是一样的，说明是一颗完全二叉树，结点数量是2^h-1;
    否则只可能左边高度大于右边，分别计算左右子树结点的数量。

    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        lh, rh = 1, 1
        lc, rc = root.left, root.right
        while lc:
            lh += 1
            lc = lc.left
        while rc:
            rh += 1
            rc = rc.right

        if lh == rh:
            return (1 << lh) - 1
        else:
            # lh > rh
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    def countNodes2(self, root):
        """

        假设二叉树的高度是H，那么总结点数量是前H-1的结点数量+最后一层的结点数量。
        Sum = f(H-1) + g(H)
        f(h) = 2^h - 1

        问题转化为求最后一层结点的数量

        :param root:
        :return:
        """


    def brutal(self, root):
        """
        TLE
        :param root:
        :return:
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        result = 1
        if root.left:
            result += self.brutal(root.left)
        if root.right:
            result += self.brutal(root.right)

        return result


s = Solution()
root = TreeNode(1)
print(s.brutal(root), s.countNodes(root))

root.left = TreeNode(2)
print(s.brutal(root), s.countNodes(root))

root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(s.brutal(root), s.countNodes(root))

root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(s.brutal(root), s.countNodes(root))

