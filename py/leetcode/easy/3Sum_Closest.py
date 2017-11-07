# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 20:39
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect

class Solution:
    # @return an integer
    def threeSumClosest1(self, num, target):
        """
        暴力解法也能过O(n^3)
        :param num:
        :param target:
        :return:
        """
        if not num:
            return 0

        # sl = sorted(num)
        result = 0
        diff = 1000000
        for i in range(len(num)-2):
            for j in range(i+1, len(num)-1):
                for k in range(j+1, len(num)):
                    v = num[i] + num[j] + num[k]
                    df = abs(v - target)
                    if df == 0:
                        return target
                    if df < diff:
                        diff = df
                        result = v
        return result

    def threeSumClosest2(self, num, target):
        """
        依然不够快
        :param num:
        :param target:
        :return:
        """
        if not num:
            return 0

        ls = list(sorted(num))

        q = list()
        q.append((0, 1, len(num)-1))
        diff = 1000000
        result = 0
        visited = set()
        while q:
            v3 = q.pop(0)
            val = ls[v3[0]] + ls[v3[1]] + ls[v3[2]]
            # print('visiting {}, val={}'.format(v3, val))
            if val == target:
                return target
            else:
                df = abs(val - target)
                if df < diff:
                    diff = df
                    result = val
                if val > target:
                    if v3[2] > v3[1]+1:
                        nv3 = (v3[0], v3[1], v3[2]-1)
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
                    if v3[1] > v3[0]+1:
                        nv3 = (v3[0], v3[1]-1, v3[2])
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
                    if v3[0] > 0:
                        nv3 = (v3[0]-1, v3[1], v3[2])
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
                else:
                    if v3[1] < v3[2]-1:
                        nv3 = (v3[0], v3[1]+1, v3[2])
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
                    if v3[0] < v3[1]-1:
                        nv3 = (v3[0]+1, v3[1], v3[2])
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
                    if v3[2] < len(num)-1:
                        nv3 = (v3[0], v3[1], v3[2]+1)
                        if nv3 not in visited:
                            q.append(nv3)
                            visited.add(nv3)
        return result
    
    def threeSumClosest(self, num, target):
        """
        169ms, about 1/5 of above 2 methods
        :param num:
        :param target:
        :return:
        """
        if not num or len(num) < 3:
            return []

        result = 0
        diff = 100000
        sl = sorted(num)
        for i in range(len(sl)-2):
            v = self.twoSumCloses(sl[i+1:], target-sl[i])
            df = abs(v-(target-sl[i]))
            if diff == 0:
                return target
            if df < diff:
                diff = df
                result = v+sl[i]
        return result


    def twoSumCloses(self, num, target):
        if not num or len(num) < 2:
            return []

        result = 0
        diff = 1000000
        l = 0
        r = len(num)-1
        while l < r:
            v = num[l] + num[r]
            if v == target:
                return target
            else:
                df = abs(v-target)
                if df < diff:
                    diff = df
                    result = v
                if v > target:
                    r -= 1
                elif v < target:
                    l += 1
        return result



s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0,1,2], 0))
print(s.threeSumClosest([-71,-82,-14,-64,-23,-33,-77,93,27,36,-19,94,-65,65,-58,-68,-2,29,60,20,59,-49,91,31,98,-28,-12,-14,-49,55,-70,0,-3,-21,54,12,94,-81,-35,33,11,15,15,34,-40,36,-43,-48,-98,76,42,30,-14,85,56,-82,11,-23,92,56,-11,41,60,67,23,-75,96,0,-14,-25,-70,-70,70,-74,-16,-94,-20,-48,56,-70,-55,-10,47,92,-63,98,91,-45,26,88,47,35,-48,79,-96,-48,24,-32,-36,-100,-7,-63,-64,23,-59,98,92,-38,-48,-8,31,60,82,93,-15,82,-89,86,50,-74,20,-46,35,50,-67,-26,81,18,-43,-45,-69,-13,2,41,-75,94,-17,-38,-90,35,79,-19,79,54,-82,-47,-58,-74,-25,-45,-96,-26,45,-31,85,-57,26,89,-46,94,6,-78,-66,-91], -250))