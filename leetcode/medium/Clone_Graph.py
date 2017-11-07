# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 14:10

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""
__author__ = 'huash06'

import sys
import os


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        mirror = UndirectedGraphNode(node.label)
        q = [node]
        mq = [mirror]
        created_node = {mirror.label: mirror}
        visited = {node}
        while q:
            h = q.pop(0)
            m = mq.pop(0)

            for neighbor in h.neighbors:
                nd = created_node.get(neighbor.label)
                if not nd:
                    nd = UndirectedGraphNode(neighbor.label)
                    created_node[neighbor.label] = nd

                m.neighbors.append(nd)
                if neighbor not in visited:
                    q.append(neighbor)
                    mq.append(nd)
                    # not same with add while enter while loop
                    visited.add(neighbor)

        return mirror

g = UndirectedGraphNode(0)
a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)
# may have more than one edge to same target
g.neighbors = [a, b, a]
b.neighbors = [a, g]
a.neighbors = [b, g]
# g.neighbors = [g, g]

s = Solution()
cg = s.cloneGraph(g)
# print(cg)

q = [cg]
visited = {cg}
while q:
    n = q.pop()
    print('{} {} : {}'.format(n, n.label, list(v.label for v in n.neighbors)))
    for nb in n.neighbors:
        if nb not in visited:
            q.append(nb)
            visited.add(nb)
