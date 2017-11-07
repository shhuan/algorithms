# -*- coding: utf-8 -*-

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""

import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1, m2 = sys.maxint, sys.maxint
        for num in nums:
            if m1 >= num:
                m1 = num
            elif m2 >= num:
                m2 = num
            else:
                return True

        return False

s = Solution()
print s.increasingTriplet([1, 2, 3, 4, 5])
print s.increasingTriplet([5, 4, 3, 2, 1])
print s.increasingTriplet([])
print s.increasingTriplet([2, 5, 3, 2, 4])
print s.increasingTriplet([2, 1, 5, 0, 3, 4])
print s.increasingTriplet([2, 4, -2, -3])

print s.increasingTriplet([1, 0, 0, 0, 1000])