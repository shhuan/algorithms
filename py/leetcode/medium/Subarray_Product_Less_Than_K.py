# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/10/22 12:09


Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # !!!
        nums.append(10**6+5)
        ans = 0
        N = len(nums)
        l, r, rb = 0, 0, 0

        m = 1
        while r < N:
            while l < N and nums[l] >= k:
                l += 1
                r = l
                rb = r
            while r < N and m*nums[r] < k:
                m *= nums[r]
                r += 1
            b = r - rb
            a = rb - l
            ans += a * b + b*(b+1)//2

            if r < N:
                m *= nums[r]
                rb = r
                r += 1
                while l < min(r, N) and m >= k:
                    m //= nums[l]
                    l += 1


        return ans

s = Solution()
print(s.numSubarrayProductLessThanK([1, 1, 1], 2))
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))