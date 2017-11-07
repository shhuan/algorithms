# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/3 19:24

Given an array nums, there is a sliding window of size k which is moving from the very
 left of the array to the very right. You can only see the k numbers in the window.
 Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements that need to be considered.

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def maxSlidingWindow2(self, nums, k):
        """
        200ms

        maxVal是前一个窗口的最大值。
        当把第i个元素加入到当前窗口时，
        if maxVal不是前一个窗口的第一个值：
            当前窗口的最大值是max(maxVal, nums[i])
        else:
            当前窗口的最大值需要从整个窗口中查找

        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return []

        maxVal = max(nums[:k])
        result = [maxVal]
        for i in range(k, len(nums)):
            if nums[i-k] < maxVal:
                maxVal = max(maxVal, nums[i])
            else:
                maxVal = max(nums[i-k+1:i+1])
            result.append(maxVal)
        return result

    def maxSlidingWindow(self, nums, k):
        """
        220ms
        这个算法更巧妙，应该是题目想要求的

        记住这个算法，遇到的次数还比较多，
        使用栈或者双端队列求最大值

        :param nums:
        :param k:
        :return:
        """
        if not nums:
            return []

        result = []
        q = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.pop(0)
            if i >= k - 1:
                result.append(nums[q[0]])

        return result



s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7] , 3))