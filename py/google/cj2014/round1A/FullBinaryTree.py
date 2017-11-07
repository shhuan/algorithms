# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-08 10:48
"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils
from datetime import datetime

# sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/B-large-practice.in', 'r')
# sys.stdout = open('output/B-large-practice.out', 'w')

MAXNN = 301

def count_node(graph, node, parent):
    cc = 1
    for i in range(len(graph)):
        if i != parent and graph[node][i]:
            cc += count_node(graph, i, node)
    return cc

def dfs(graph, node, parent, memo):
    """
    返回以node為根的子樹變成完全二叉樹時，剪掉的節點數量和剩餘的節點數量

    :param graph:
    :param node:
    :param parent:
    :param memo: record calculated result
    :return: how many node in this full-binary tree rooted at node
    """

    max1 = -1
    max2 = -1
    if memo[node][parent] == -1 or True:
        for child in graph[node]:
            if child != parent:
                nc = dfs(graph, child, node, memo)
                if nc > max1:
                    max2 = max1
                    max1 = nc
                elif nc > max2:
                    max2 = nc
        if max2 == -1:
            memo[node][parent] = 1
        else:
            memo[node][parent] = 1 + max1 + max2
    return memo[node][parent]


T = int(sys.stdin.readline())
sys.setrecursionlimit(3000)
# start_time = datetime.now()
for ti in range(1, T + 1):
    N = int(sys.stdin.readline())
    GRAPH = dict()
    for ei in range(1, N+1):
        GRAPH[ei] = list()
    for ni in range(N-1):
        S, T = map(int, sys.stdin.readline().strip().split(' '))
        GRAPH[S].append(T)
        GRAPH[T].append(S)

    count = N
    memo = [[-1 for c in range(N+1)] for r in range(N+1)]
    for r in range(1, N+1):

        c = N - dfs(GRAPH, r, 0, memo)
        if c < count:
            count = c
    print('Case #{}: {}'.format(ti, count))

# end_time = datetime.now()
# time_cost = end_time-start_time
# print('Time Cost: {}s'.format(time_cost.seconds))

