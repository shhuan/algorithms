# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 16:07
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums:
            return False

        return len(set(nums)) != len(nums)


s = Solution()

print(s.containsDuplicate([1, 2, 3, 2]))
print(s.containsDuplicate([1, 2, 3, 42]))
