# -*- coding: utf-8 -*-
"""

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test ca


"""
__author__ = 'huash'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        result = 0
        for i, num in enumerate(nums):
            result ^= i
            result ^= num
        return result ^ len(nums)


s = Solution()
print(s.missingNumber([0, 1, 3]))
print(s.missingNumber([]))
print(s.missingNumber([0]))
print(s.missingNumber([0, 2, 4, 6, 1, 5]))