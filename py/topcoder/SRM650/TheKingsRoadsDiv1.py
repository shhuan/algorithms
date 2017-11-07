# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-17 11:55

You live in the Kingdom of Byteland.
The kingdom has a very interesting history. It has already existed for h years.
During the first year of its existence the inhabitants built the first city.
During each of the next h-1 years the following procces occurred:
For each city built in the previous year, two additional cities were built and the older city
was connected to each the two new cities by a bidirecional road. Now, after h full years,
the kingdom contains exactly (2^h)-1 cities and (2^h)-2 roads.

Recently the King did two changes to the kingdom.
First, he numbered the cities from 1 to (2^h)-1 in an arbitrary way.
Then, he added exactly three new roads to the kingdom.
(After the addition there may be multiple roads connecting the same pair of cities.
Also, some of the new roads may connect some city to itself.)

You are given the h and two s a and b with (2^h)+1 elements each.
For each valid i, there is a road between the cities a[i] and b[i].

Return "Correct" if it is possible that the given list of roads is the current road network in the Kingdom of Byteland.
Otherwise, return "Incorrect".



分析：
和div2的问题相比，这里多了三条边，如果直接枚举C(n,3)=1000^3/6肯定会超时。
所以先找出可能是非法的边，然后在组合其中三条移除。

对于完全二叉树加入三条边之后，顶点最大的度是6，如果有超过6的，肯定是"Incorrect"。
高度H的完全二叉树树有2^(H-1)个叶子结点，如果新加入的三条边全部连接叶节点，也有
2^(H-1)-6个叶结点即，这些度数为2的结点的个数在[2^(H-1)-6,2^(H-1)]之间。
它们是合法的，通过它们找出合法的父亲结点，直到找出所以的合法结点。


"""
__author__ = 'huash06'

import datetime
import sys
import collections
import random

class TheKingsRoadsDiv1:
    def getAnswer(self, h, a, b):
        graph = collections.defaultdict(list)
        badEdgeCount = 3
        for i in range(len(a)):
            if b[i] in graph[a[i]] or a[i] == b[i]:
                badEdgeCount -= 1
                if badEdgeCount < 0:
                    return 'Incorrect'
                continue
            graph[a[i]].append(b[i])
            graph[b[i]].append(a[i])

        if self.isValidBinaryTree(graph, h, badEdgeCount):
                return 'Correct'
        return 'Incorrect'


    def isValidBinaryTree(self, graph, h, badEdgeCount):
        n = 1 << h
        leaves = list(filter(lambda x: len(x[1]) == 1, graph.items()))
        if not leaves:
            return False
        leaves, nodes = zip(*leaves)

        validNodes = [False] * n
        # visitedNodes = [False] * n
        for node in leaves:
            validNodes[node] = True
            # visitedNodes[node] = True

        if len(leaves) < (1 << (h-1)) - 6:
            return False


        m3 = list(filter(lambda x: len(x[1]) > 3, graph.items()))
        if len(m3) > 6:
            return False
        # q = list(leaves)
        # while q:
        #     node = q.pop(0)
        #     for parent in graph[node]:
        #         if not visitedNodes[parent] and len(graph[parent]) == 3:
        #             c = 0
        #             for sib in graph[parent]:
        #                 if visitedNodes[sib]:
        #                     c += 1
        #             if c == 2:
        #                 validNodes[parent] = True
        #                 visitedNodes[parent] = True
        #                 q.append(parent)
        #                 break

        for i in range(h):
            for x in graph.keys():
                if not validNodes[x]:
                    d = 0
                    for y in graph[x]:
                        if not validNodes[y]:
                            d += 1
                    if d <= 1:
                        validNodes[x] = True


        # del visitedNodes

        if validNodes.count(False) > 100:
            return False

        cutEdges = set()
        for s, v in graph.items():
            if not validNodes[s]:
                for t in v:
                    if s < t and not validNodes[t]:
                        cutEdges.add((s, t))

        # print(graph)
        # print(sorted(list(cutEdges)))
        # print(badEdgeCount)
        return self.backtrace(graph, h, list(cutEdges), 0, badEdgeCount)

    def backtrace(self, graph, h, cutEdges, ci, badEgdeCount):
        if badEgdeCount == 0:
            roots, children = zip(*(filter(lambda x: len(x[1]) == 2, graph.items())))
            if len(roots) != 1:
                return False
            return self.bfs(graph, roots[0], h)

        if ci >= len(cutEdges):
            return False

        # don't cut edge cutEgdes[ci]
        if self.backtrace(graph, h, cutEdges, ci+1, badEgdeCount):
            return True

        # cutting edge cutEgdes[ci]
        s, t = cutEdges[ci]
        graph[s].remove(t)
        graph[t].remove(s)
        if self.backtrace(graph, h, cutEdges, ci+1, badEgdeCount-1):
            return True
        graph[s].append(t)
        graph[t].append(s)

        return False



    def bfs(self, graph, root, h):
        # 使用bfs判断是平衡、完全二叉树
        # 按层次遍历即可
        n = 1 << h
        q = [root]
        visited = [False]*n
        visited[0] = True
        visited[root] = True
        while q:
            node = q.pop(0)
            children = 0

            for i in graph[node]:
                if not visited[i]:
                    children += 1
                    visited[i] = True
                    q.append(i)

            if children == 0:
                break
            elif children != 2:
                return False
        # if visited.count(False) == 0:
        #     print("Graph rooted at {} is valid".format(root))
        #     print(graph)
        return visited.count(False) == 0

s = TheKingsRoadsDiv1()

print(s.getAnswer(3, [1, 3, 2, 2, 3, 7, 1, 5, 4], [6, 5, 4, 7, 4, 3, 3, 1, 7]))
print(s.getAnswer(2, [1, 2, 1, 3, 3], [2, 1, 2, 3, 3]))
print(s.getAnswer(3, [1, 3, 2, 2, 6, 6, 4, 4, 7], [2, 1, 4, 5, 4, 4, 7, 7, 6]))
print(s.getAnswer(2, [1, 2, 2, 1, 1], [1, 2, 2, 1, 2]))
print(s.getAnswer(5, [6, 15, 29, 28, 7, 13, 13, 23, 28, 13, 30, 27, 14, 4, 14, 19, 27, 20, 20, 19, 10, 15, 7, 7, 19, 29, 4, 24, 10, 23, 30, 6, 24],
                  [9, 22, 30, 20, 26, 25, 8, 7, 24, 21, 27, 31, 4, 28, 29, 6, 16, 1, 17, 10, 3, 12, 30, 18, 14, 23, 19, 21, 5, 13, 15, 2, 11]))
print(s.getAnswer(2, [1,1,1,2,1], [2,3,1,2,2]))



a = [0]*1025
b = [0]*1025

q = [1]
i = 0
nextNode = 2
while i < 1022:
    node = q.pop(0)

    a[i] = node
    b[i] = nextNode
    q.append(nextNode)
    i += 1
    nextNode += 1

    a[i] = node
    b[i] = nextNode
    q.append(nextNode)
    i += 1
    nextNode += 1

a[1022] = 1
b[1022] = 100
a[1023] = 11
b[1023] = 110
a[1024] = 13
b[1024] = 103

for i in range(5):
    j = random.randint(0, 1024)
    si = random.randint(1, 1022)
    ti = random.randint(1, 1022)
    a[j] = si
    b[j] = ti

st = datetime.datetime.now()
print(s.getAnswer(10, a, b))
print('Time Cost: {}'.format(datetime.datetime.now() - st))