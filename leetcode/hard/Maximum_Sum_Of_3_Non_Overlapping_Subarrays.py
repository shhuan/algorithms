# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 10:03

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).

"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        N = len(nums)

        W = []
        s = sum(nums[:k])
        for i in range(k, N):
            W.append(s)
            s -= nums[i-k]
            s += nums[i]
        W.append(s)

        NW = len(W)
        best = 0
        left = [0] * NW
        for i in range(NW):
            if W[i] > W[best]:
                best = i
            left[i] = best

        best = NW-1
        right = [0] * NW
        for i in range(NW-1, -1, -1):
            if W[i] > W[best]:
                best = i
            right[i] = best

        maxSum = 0
        ans = 0, 0, 0
        for i in range(k, NW-k):
            tsum = W[i] + W[left[i-k]] + W[right[i+k]]
            if tsum > maxSum:
                maxSum = tsum
                ans = left[i-k], i, right[i+k]
        return ans


s = Solution()
print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))