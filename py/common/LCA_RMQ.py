# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-05 12:08

LCA转RMQ主要是通过DFS（深度优先搜索）完成，时间复杂度为O(n)。

DFS时每次进入以及回溯到某一个节点时，我们都记录访问到的节点val，同时记录下这个节点的深度depth。
因为进入及回溯时都要记录，所以一个节点可能会被记录多次。
另外，为了后面应用RMQ的方便，还使用数组first记录每个元素第一次访问的下标。

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


MAX_X = 100

# 树的邻接表，不一定是二叉树
tree = None

depth = None
val = None
first = None
index = 0


def dfs(x, dep):
    global index
    depth[index] = dep
    val[index] = x
    first[x] = index
    index += 1

    if x in tree:
        for child in tree[x]:
            dfs(child, dep+1)
            depth[index] = dep
            val[index] = x
            index += 1

    if x in queries:
        for y in queries[x]:
            if first[y] >= 0:
                minDep = 100
                ancestor = 0
                for i in range(min(first[y], first[x]), max(first[y], first[x])+1):
                    # 这里需要优化从RMQ最小值查询
                    if depth[i] >= 0 and depth[i] < minDep:
                        minDep = depth[i]
                        ancestor = i
                print('LCA({}, {}) = {}'.format(x, y, val[ancestor]))


def test():

    global tree, queries, ancestor

    tree = {}
    tree[0] = [1, 2, 3]
    tree[1] = [4, 5]
    tree[3] = [6]
    tree[5] = [7]

    #              0
    #            / | \
    #           1  2  3
    #          /\      \
    #         4 5       6
    #            \
    #            7

    queries = {}
    for i in range(8):
        queries[i] = [j for j in range(8)]
    # queries[3] = [7]
    global first, depth, val
    first = [-1] * MAX_X
    depth = [-1] * MAX_X
    val = [0] * MAX_X
    dfs(0, 0)


if __name__ == '__main__':
    test()


