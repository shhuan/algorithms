# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 09:49

Given an array S of n integers, are there elements a, b, c in S such
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
Show Tags

"""
__author__ = 'huash06'

import sys
import os

import itertools
import collections
import functools
import bisect
import re

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        result = set()
        nums.sort()
        N = len(nums)
        K = N - 1
        i = 0
        while i < K-1:
            j = i+1
            while j < K:
                v = 0 - (nums[i] + nums[j])
                nextK = -1
                for k in range(K, j, -1):
                    if v == nums[k]:
                        result.add((nums[i], nums[j], nums[k]))
                        if nextK < 0:
                            nextK = k
                    elif v > nums[k]:
                        if nextK < 0:
                            nextK = k
                        break
                if nextK > 0:
                    K = nextK
                j += 1
            i += 1

        return list(result)

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

print(s.threeSum([13,9,1,12,-7,-12,7,3,9,6,-7,4,9,5,5,-7,4,11,1,-2,12,3,-12,-15,0,-12,-6,-1,7,-5,-4,-3,12,4,-14,-10,-1,8,1,-6,-1,9,13,-14,-1,-5,-6,-12,-8,2,2,11,13,-3,11,-2,1,-10,4,-15,-8,7,-11,11,-4,-10,-13,3,5,3,12,11,-11,2,12,3,13,13,-2,12,-7,-15,8,-9,-10,-4,-4,6,1,-15,-2,0,-1,2,-3,10,-1,-9,-10,-11,1,-13,-15,5,-3,5,-7,-5,-5,6,14,3,-1,7,1,-4,-12,12,-13,-4,4,0,3,-12,9,-15,6]))
