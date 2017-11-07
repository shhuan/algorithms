# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/8 09:18
    
"""


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))


s = Solution()
print(s.maxNumber([6,7], [6,0,4], 5))