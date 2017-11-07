# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/4 21:33

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        l = 0
        N = len(citations)
        r = N

        result = 0
        while l < r:
            mid = l + (r - l) // 2
            if citations[mid] >= N - mid:
                result = N - mid
                r = mid
            else:
                l = mid + 1
        return result

s = Solution()
print(s.hIndex([0, 1, 3, 5, 6]))


