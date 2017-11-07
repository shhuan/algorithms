# -*- coding: utf-8 -*-

"""
created by 'palad' at '2016/6/13'

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        return list(set(nums1).intersection(set(nums2)))

s = Solution()
print s.intersection([1, 2, 2, 3], [2, 2])