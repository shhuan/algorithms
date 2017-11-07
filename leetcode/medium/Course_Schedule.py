# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 14:44


There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists,
no topological ordering exists and therefore it will be impossible to take all courses.

Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.

Topological sort could also be done via BFS.

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):

        graph = collections.defaultdict(list)
        degreses = collections.defaultdict(int)
        for c, p in prerequisites:
            graph[p].append(c)
            degreses[c] += 1

        studied = [False] * numCourses
        canStudies = set()
        for i in range(numCourses):
            if degreses[i] == 0:
                canStudies.add(i)

        while canStudies:
            course = canStudies.pop()
            studied[course] = True
            for c in graph[course]:
                degreses[c] -= 1
                if degreses[c] == 0:
                    canStudies.add(c)
        return studied.count(False) == 0


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))


