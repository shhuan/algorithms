# -*- coding: utf-8 -*-
"""


Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.
"""

import collections

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        def isSame(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1 == t2:
                return False

            if t1.val != t2.val:
                return False

            return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)

        nodedict = collections.defaultdict(list)

        def nodehash(node):
            if not node:
                return ""

            hv = str(node.val) + nodehash(node.left) + nodehash(node.right)
            nodedict[hv].append(node)

            return hv

        nodehash(root)
        print(nodedict)

        ret = []
        for k, nds in nodedict.items():
            N = len(nds)
            visited = [False for _ in range(N)]
            for i, nd in enumerate(nds):
                if not visited[i]:
                    found = False
                    for j in range(i + 1, N):
                        if isSame(nd, nds[j]):
                            found = True
                            visited[j] = True
                    if found:
                        ret.append(nd)

        return ret



def arr2Tree(nodes, start):
    N = len(nodes)
    if start > N - 1:
        return None

    if nodes[start] == '#':
        return None

    root = TreeNode(nodes[start])

    root.left = arr2Tree(nodes, 2*start+1)
    root.right = arr2Tree(nodes, 2*start+2)

    return root

A = [1,2,3,4,'#',2,4,'#','#','#','#',4]

s = Solution()
print(s.findDuplicateSubtrees(arr2Tree(A, 0)))



