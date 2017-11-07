# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq

"""
created by shhuan at 2017/10/2 22:00

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.


"""

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        N = len(edges)

        def check(egs):
            # 检查是否有环
            ancestor = [i for i in range(1 + N)]
            for edge in egs:
                as1 = ancestor[edge[0]]
                while as1 != ancestor[as1] and ancestor[as1] > 0:
                    as1 = ancestor[as1]
                as2 = ancestor[edge[1]]
                while as2 != ancestor[as2] and ancestor[as2] > 0:
                    as2 = ancestor[as2]
                if as1 > 0 and as1 == as2:
                    return edge
                ancestor[edge[1]] = edge[0]

        parents = collections.defaultdict(list)
        for ei, edge in enumerate(edges):
            parents[edge[1]].append(ei)
            if len(parents[edge[1]]) > 1:
                for i in reversed(parents[edge[1]]):
                    if not check(edges[:i]+edges[i+1:]):
                        return edges[i]

        return check(edges)





s = Solution()
print(s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
print(s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
print(s.findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))


