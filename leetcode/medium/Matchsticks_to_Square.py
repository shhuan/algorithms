# -*- coding: utf-8 -*-


"""

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

"""

import time
import random

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums or len(nums) < 4:
            return False
        total = sum(nums)
        if total % 4 != 0:
            return False

        d = sum(nums) // 4
        if d < max(nums):
            return False
        n = len(nums)

        random.shuffle(nums)
        self.c = 0
        def dfs(index, edges):
            #print(edges)
            self.c += 1
            if edges.count(d) > 2:
                return True

            if index >= n:
                return False

            for i in range(len(edges)):
                if edges[i] + nums[index] > d:
                    continue
                edges[i] += nums[index]
                if dfs(index + 1, edges):
                    return True
                edges[i] -= nums[index]
            return False

        ret = dfs(0, [0, 0, 0, 0])
        print(ret, self.c, nums)

s = Solution()
t0 = time.time()
print(s.makesquare([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]))
print(time.time() - t0)