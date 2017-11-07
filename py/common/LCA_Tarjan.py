# -*- coding: utf-8 -*-DisjointSet

"""
created by huash06 at 2015-05-05 09:25

参考http://blog.csdn.net/v_july_v/article/details/18312089


function TarjanOLCA(u)
    MakeSet(u);
    u.ancestor := u;
    for each v in u.children do
        TarjanOLCA(v);
        Union(u,v);
        Find(u).ancestor := u;
    u.colour := black;
    for each v such that {u,v} in P do
        if v.colour == black
            print "Tarjan's Lowest Common Ancestor of " + u +
                  " and " + v + " is " + Find(v).ancestor + ".";


function MakeSet(x)
     x.parent := x
     x.rank   := 0

function Union(x, y)
    xRoot := Find(x)
    yRoot := Find(y)
    if xRoot.rank > yRoot.rank
        yRoot.parent := xRoot
    else if xRoot.rank < yRoot.rank
        xRoot.parent := yRoot
    else if xRoot != yRoot
        yRoot.parent := xRoot
        xRoot.rank := xRoot.rank + 1

function Find(x)
    if x.parent == x
        return x
    else
        x.parent := Find(x.parent)
        return x.parent

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import py.common.UnionFind as UnionFind


MAX_X = 100
father = [0] * MAX_X
rank = [0] * MAX_X

def makeSet():
    for i in range(MAX_X):
        father[i] = i
        rank[i] = 0


def findSet(x):
    """
    并查集的优化1：
    称为“路径压缩”，是一种在执行“查找”时扁平化树结构的方法。关键在于在路径上的每个节点都可以直接连接到根上；
    他们都有同样的表示方法。为了达到这样的效果，Find递归地经过树，改变每一个节点的引用到根节点。
    得到的树将更加扁平，为以后直接或者间接引用节点的操作加速。
    :param x:
    :return:
    """
    if x != father[x]:
        father[x] = findSet(father[x])
    return father[x]

def unionSet(x, y):
    """
    并查集的优化2：
    称为“按秩合并”，即总是将更小的树连接至更大的树上。因为影响运行时间的是树的深度，
    更小的树添加到更深的树的根上将不会增加秩除非它们的秩相同。在这个算法中，术语“秩”替代了“深度”，
    因为同时应用了路径压缩时（见下文）秩将不会与高度相同。单元素的树的秩定义为0，当两棵秩同为r的树联合时，
    它们的秩r+1。只使用这个方法将使最坏的运行时间提高至每个MakeSet、Union或Find操作O(\log n)。
    :param x:
    :param y:
    :return:
    """
    x = findSet(x)
    y = findSet(y)
    if x != y:
        if rank[x] > rank[y]:
            father[y] = x
            rank[x] += rank[y]
        else:
            father[x] = y
            rank[y] != rank[x]

# 已访问节点的祖先
ancestor = None

# 已访问节点
visited = [False] * MAX_X

# 树的邻接表，不一定是二叉树
tree = None

# 查询，queries[x] = [y1, y2]表示查询(x, y1), (x, y2)的LCA
queries = None


def tarjan(x):
    """
    Tarjan算法流程为：

        Procedure dfs（u）；
            begin
                设置u号节点的祖先为u
                若u的左子树不为空，dfs（u - 左子树）；
                若u的右子树不为空，dfs（u - 右子树）；
                访问每一条与u相关的询问u、v
                    -若v已经被访问过，则输出v当前的祖先t（t即u,v的LCA）
                标记u为已经访问，将所有u的孩子包括u本身的祖先改为u的父亲
            end

    普通的dfs 不能直接解决LCA问题，故Tarjan算法的原理是dfs + 并查集，它每次把两个结点对的最近公共祖先的查询保存起来，
    然后dfs 更新一次。如此，利用并查集优越的时空复杂度，此算法的时间复杂度可以缩小至O(n＋Q)，其中，n为数据规模，Q为询问个数。
    :return:
    """
    if x in tree:
        for child in tree[x]:
            tarjan(child)
            unionSet(x, child)
        # 设置x所在的集合的祖先x
        ancestor[findSet(x)] = x

    visited[x] = True

    if x in queries:
        for y in queries[x]:
            if visited[y]:
                print('LCA({}, {}) = {}'.format(x, y, ancestor[findSet(y)]))


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

    makeSet()
    ancestor = [i for i in range(MAX_X)]
    tarjan(0)


if __name__ == '__main__':
    test()

