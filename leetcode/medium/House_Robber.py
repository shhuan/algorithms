# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 19:06


You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.



f(i,j)表示从房间i到j(包含i,j)中能拿最大数量的值

f(i, j) = max{f(i,k)+f(k+2,j), f(k+1)} i<=k<=j



另外一种解法

For every house k, there are two options: either to rob it (include this house: i) or not rob it (exclude this house: e).

Include this house: i = num[k] + e (money of this house + money robbed excluding the previous house)

Exclude this house: e = max(i, e) (max of money robbed including the previous house or money
robbed excluding the previous house) (note that i and e of the previous step, that's why
we use tmp here to store the previous i when calculating e, to make O(1) space)


"""
__author__ = 'huash'

import sys
import os


# class Solution:
#     # @param num, a list of integer
#     # @return an integer
#     def rob(self, num):
#         if not num:
#             return 0
#
#         n = len(num)
#         v = [[0 for c in range(n)] for r in range(n)]
#         gap = 1
#
#         for i in range(n-1):
#             v[i][i+1] = max(num[i], num[i+1])
#         for i in range(n):
#             v[i][i] = num[i]
#
#         for gap in range(2, n):
#             for i in range(n-gap):
#                 j = i+gap
#                 max_count = 0
#                 for k in range(i, j-1):
#                     max_count = max(max_count, v[i][k] + v[k+2][j])
#                     max_count = max(max_count, v[i][k+1])
#                 v[i][j] = max_count
#         return v[0][n-1]

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        i = 0
        e = 0
        for v in num:
            tmp = i
            i = e + v
            e = max(tmp, e)
        return max(i, e)



s = Solution()

print(s.rob([1, 3, 1]))

print(s.rob([1, 4, 7, 5]))

print(s.rob([1, 4, 7]))

print(s.rob([1, 4]))

print(s.rob([7]))

print(s.rob([1, 4, 7, 3, 2, 5, 6]))

print(s.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))