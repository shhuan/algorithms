# -*- coding: utf-8 -*-
"""


You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.


"""

import time
import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        zeros = nums.count(0)
        nums = list(sorted([x for x in nums if x != 0], reverse=True))

        if not nums:
            if S == 0:
                return 2**zeros
            else:
                return 0

        N = len(nums)

        vc = collections.defaultdict(int)
        vc[nums[0]] = 1
        vc[-nums[0]] = 1

        for i, a in enumerate(nums[1:]):
            # print(vc)
            nvc = collections.defaultdict(int)
            for b, c in vc.items():
                nvc[b+a] += c
                nvc[b-a] += c
            vc = nvc

        if S not in vc:
            return 0

        return 2 ** zeros * vc[S]

s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1))
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0))

print(s.findTargetSumWays([25,33,27,23,46,16,10,27,33,2,12,2,29,44,49,40,32,46,7,50], 4))

print(s.findTargetSumWays([20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39], 1))

t0 = time.time()
print(s.findTargetSumWays([40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15], 3))
print(time.time()-t0)