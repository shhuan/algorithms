# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-02 19:06

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""
__author__ = 'huash'

import sys
import os
import collections

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)

        res = 0
        kmap = collections.defaultdict(int)
        for pa in points:
            kmap.clear()
            same = 0
            for pb in points:
                if not (pa.x == pb.x and pa.y == pb.y):
                    if pb.x == pa.x:
                        kmap['NAN'] += 1
                    else:
                        k = float(pb.y - pa.y)/float(pb.x - pa.x)
                        kmap[k] += 1
                else:
                    same += 1
            res = max(res, max(same, 1) + (max(kmap.values()) if kmap else 0))
            del pa
        return res


def pointsFromRawPoints(rapoints):
    points = []
    for x, y in rawpoints:
        points.append(Point(x, y))
    return points

s = Solution()
rawpoints = [(0, 0), (1, 1), (1, -1), (2, 2), (3, 3)]
print(s.maxPoints(pointsFromRawPoints(rawpoints)) == 4)
rawpoints = [[1,1],[1,1],[2,2],[2,2]]
print(s.maxPoints(pointsFromRawPoints(rawpoints)) == 4)

rawpoints = [[1,1],[1,1],[1,1]]
print(s.maxPoints(pointsFromRawPoints(rawpoints)) == 3)

rawpoints = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
print(s.maxPoints(pointsFromRawPoints(rawpoints)) == 6)

