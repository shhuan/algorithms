# -*- coding: utf-8 -*-
"""

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.


"""

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        sums = collections.defaultdict(int)

        def dfs(node):
            if not node:
                return None

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            if not lsum:
                lsum = 0

            if not rsum:
                rsum = 0

            val = lsum + rsum + node.val
            sums[val] += 1

            return val

        dfs(root)

        print(sums)

        sums = sorted(sums.items(), key=lambda x: x[1], reverse=True)

        freq = sums[0][1]
        ret = []
        for k, v in sums:
            if v == freq:
                ret.append(k)

        return ret

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)

s = Solution()
print(s.findFrequentTreeSum(root))
