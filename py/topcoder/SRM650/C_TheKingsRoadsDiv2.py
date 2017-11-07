# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-16 11:57


判断一个图是否是一颗平衡完全二叉树添加一条边得到的。


分析：
1. 如果输入有超过一条非法边，结果就是Incorrect。
    非法边包括重复边和指向自身的边
2. 如果有一条非法边，判断其他边是否能组成一个完全二叉树。
3. 如果没有非法边，尝试移除一条边之后判断剩下的边是否能够组成一个完全二叉树。


如果使用二维数组存储，复杂度O(n^3)在n=1000时会超时。
所以使用字典存储。


TopCoder超时也只是提示Fail System Test

"""
__author__ = 'huash06'

import datetime
import sys
import collections



class TheKingsRoadsDiv2:
    def getAnswer(self, h, a, b):

        # if h == 1:
        #     return 'Correct'
        # elif h < 1:
        #     return 'Incorrect'

        graph = collections.defaultdict(list)
        badEdgeCount = 0
        for i in range(len(a)):
            if b[i] in graph[a[i]] or a[i] == b[i]:
                badEdgeCount += 1
                if badEdgeCount > 1:
                    return 'Incorrect'
                continue
            graph[a[i]].append(b[i])
            graph[b[i]].append(a[i])

        if badEdgeCount == 1:
            if self.isValidBinaryTree(graph, h):
                return 'Correct'
        else:
            for i in range(len(a)):
                graph[a[i]].remove(b[i])
                graph[b[i]].remove(a[i])
                if self.isValidBinaryTree(graph, h):
                    return 'Correct'
                graph[a[i]].append(b[i])
                graph[b[i]].append(a[i])
        return 'Incorrect'

    def isValidBinaryTree(self, graph, h):
        # 只有一个度数是2的结点是根
        root = 0
        for k, v in graph.items():
            if len(v) == 2:
                if root != 0:
                    return False
                root = k
        # return self.bfs(graph, root, h)
        return self.dfs(graph, root, h, {root})



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

        return visited.count(False) == 0

    def dfs(self, graph, root, h, visited):
        # 使用dfs判断完全二叉树
        if h == 1:
            return True
        elif h < 1:
            return False

        children = []
        for node in graph[root]:
            if node not in visited:
                children.append(node)
                visited.add(node)
        if len(children) != 2:
            return False
        return self.dfs(graph, children[0], h-1, visited) and \
                self.dfs(graph, children[1], h-1, visited)















s = TheKingsRoadsDiv2()
# print(s.getAnswer(1, [1], [1]))
print(s.getAnswer(3, [1, 2, 3, 7, 1, 5, 4], [6, 7, 4, 3, 3, 1, 7]))
print(s.getAnswer(2, [1, 2, 3], [2, 1, 3]))
print(s.getAnswer(3, [7, 1, 1, 2, 2, 3, 1], [7, 1, 7, 4, 5, 2, 6]))
print(s.getAnswer(2, [1, 3, 3], [2, 1, 2]))
print(s.getAnswer(3, [6, 5, 3, 3, 5, 5, 6], [1, 5, 5, 6, 4, 7, 2]))



a = [0]*1023
b = [0]*1023

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
st = datetime.datetime.now()
print(s.getAnswer(10, a, b))
print('Time Cost: {}'.format(datetime.datetime.now() - st))