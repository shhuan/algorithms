# -*- coding: utf-8 -*-

"""

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.


令f(i, j) = sum(A[i: i+2^j+1])

sum(i, j) = f(i,k) + f(i+2^k,j)


f(i,j) = sum(0,j) - sum(0,i-1)

"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.data = []
            return

        n = len(nums) + 1
        data = [0 for _ in range(n)]

        s = 0
        for i, v in enumerate(nums):
            s += v
            data[i + 1] = s
        self.data = data
        # print(data)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.data:
            return 0

        return self.data[j + 1] - self.data[i]

s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.sumRange(0, 2))
print(s.sumRange(2, 5))
print(s.sumRange(0, 5))

s = NumArray([-2])
print(s.sumRange(0, 0))

s = NumArray([])