# -*- coding: utf-8 -*-

"""
created by 'palad' at 

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
Subscribe to see which companies asked this question

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        def count(nums):
            c = {}
            for i in nums:
                if i not in c:
                    c[i] = 1
                else:
                    c[i] += 1
            return c

        c1 = count(nums1)
        c2 = count(nums2)

        result = []
        for k, v1 in c1.items():
            if k in c2:
                v2 = c2[k]
                result.extend([k]*min(v1, v2))

        return result

s = Solution()
print s.intersect([1, 2, 2, 1], [2, 2])