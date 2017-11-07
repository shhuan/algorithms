# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 09:36


Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections
import heapq


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        # 48ms
        # return sorted(nums, reverse=True)[k-1]


        # 48ms
        if k < len(nums) // 2:
            return sorted(nums, reverse=True)[k - 1]
        else:
            return sorted(nums)[len(nums) - k]

    def findKthLargest2(self, nums, k):
        # 52ms
        l = 0
        r = len(nums) - 1
        k -= 1
        while l <= r:
            pivot = self.partition(nums, l, r)
            if pivot == k:
                return nums[pivot]
            elif pivot > k:
                r = pivot - 1
            else:
                l = pivot + 1
        return -1


    def partition(self, nums, left, right):
        if left == right:
            return left
        tmp = nums[right]
        ret = left - 1
        i = left
        while i < right:
            while nums[i] < tmp and i < right:
                i += 1
            if i >= right:
                break

            ret += 1
            nums[ret], nums[i] = nums[i], nums[ret]
            i += 1
        ret += 1
        nums[right], nums[ret] = nums[ret], nums[right]
        return ret


    def findKthLargest3(self, nums, k):
        # 48ms
        # return heapq.nlargest(k, nums)[-1]


        # 104ms
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            heapq.heappush(h, nums[i])
            heapq.heappop(h)

        return h[0]

    def findKthLargest4(self, nums, k):
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]


s = Solution()
for k in range(1, 7):
    nums = [1, 5, 3, 2, 4, 7, 3]
    print(s.findKthLargest(nums, k), s.findKthLargest2(nums, k), s.findKthLargest3(nums, k), s.findKthLargest4(nums, k))
