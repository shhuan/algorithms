# -*- coding: utf-8 -*-

"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

f[i][j][l] 表示nums1的前i个数字，nums2的前j个数字，组成的长度最l的数字的最大值

f[i][j][l] = max { f[i-1][j][l], f[i][j-1][l], f[i-1][j][l-1]*10+nums1[i-1], f[i][j-1][l-1]*10+nums2[j-1]}

TLE



"""
__author__ = 'huash'

import sys
import os
import time
import collections

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = 0
        table = [[[0 for l in range(len(nums1)+len(nums2) + 2)] for j in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]

        for i in range(len(nums1)+1):
            for j in range(len(nums2)+1):
                for l in range(1, i+j+1): # how about start from loc[i][j]
                    table[i][j][l] = max(table[i][j-1][l] if j > 0 else 0,
                                         table[i-1][j][l] if i > 0 else 0,
                                         table[i-1][j][l-1]*10+nums1[i-1] if i > 0 and l > 0 else 0,
                                         table[i][j-1][l-1]*10+nums2[j-1] if j > 0 and l > 0 else 0)
                result = max(result, table[i][j][k])

        return [int(i) for i in str(result)]

s = Solution()
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print s.maxNumber(nums1, nums2, k)

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print s.maxNumber(nums1, nums2, k)

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
print s.maxNumber(nums1, nums2, k)

nums1 = [1,5,8,1,4,0,8,5,0,7,0,5,7,6,0,5,5,2,4,3,6,4,6,6,3,8,1,1,3,1,3,5,4,3,9,5,0,3,8,1,4,9,8,8,3,4,6,2,5,4,1,1,4,6,5,2,3,6,3,5,4,3,0,7,2,5,1,5,3,3,8,2,2,7,6,7,5,9,1,2]
nums2 = [7,8,5,8,0,1,1,6,1,7,6,9,6,6,0,8,5,8,6,3,4,0,4,6,7,8,7,7,7,5,7,2,5,2,1,9,5,9,3,7,3,9,9,3,1,4,3,3,9,7,1,4,4,1,4,0,2,3,1,3,2,0,2,4,0,9,2,0,1,3,9,1,2,2,6,6,9,3,6,0]
k = 80

start_time = time.time()
print s.maxNumber(nums1, nums2, k)
print time.time() - start_time

nums1 = [6,3,1,7,6,6,1,4,7,8,4,1,4,6,1,0,8,9,6,2,3,1,5,4,9,5,4,2,1,7,7,1,4,0,6,2,8,6,2,4,9,8,5,5,5,1,3,5,4,2,3,8,4,1,1,1,0,9,6,7,2,3,8,9,0,3,3,4,6,3,7,7,0,7,9,7,2,8,8,9,8,0,8,2,1,9,8,0,8,4]
nums2 = [6,4,1,5,0,8,7,6,3,2,7,7,4,1,1,5,3,5,5,9,2,2,0,8,0,5,7,3,9,9,1,2,2,4,2,7,4,5,1,5,6,4,7,5,5,0,0,9,7,3,4,2,3,1,6,8,9,8,3,7,2,8,5,8,5,4,4,7,6,8,1,0,0,5,7,9,5,1,6,8,9,7,8,6,8,6,7,5,2,7]
k = 90

start_time = time.time()
print s.maxNumber(nums1, nums2, k)
print time.time() - start_time