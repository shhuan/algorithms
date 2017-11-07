# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq

"""
created by shhuan at 2017/9/24 08:46

"""

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers or len(flowers) < 2:
            return -1


        N = len(flowers)
        BIT = [0] * (N+1)
        BLOOM = [0] * (N+1)

        def update(index):
            BLOOM[index] = 1
            while index < len(BIT):
                BIT[index] += 1
                index += index & -index

        def presum(x):
            if x <= 0:
                return 0
            s = 0
            while x > 0:
                s += BIT[x]
                x -= x & -x
            return s

        for i,v in enumerate(flowers):
            update(v)

            if v-k-1 >= 1 and BLOOM[v-k-1] == 1:
                if presum(v) == presum(v-k-1)+1:
                    return i+1
            if v+k+1 <= N and BLOOM[v+k+1] == 1:
                if presum(v)+1 == presum(v+k+1):
                    return i+1

        return -1

s = Solution()
print(s.kEmptySlots([1, 3, 2], 1))
print(s.kEmptySlots([1, 2, 3], 1))









s = Solution()

# print(s.kEmptySlots([1,5,3,2,4], 2))
# print(s.kEmptySlots([1,2,3], 1))
# print(s.kEmptySlots([10,1,6,4,2,8,9,7,5,3], 1))
print(s.kEmptySlots([23,36,49,20,9,75,11,96,38,91,78,43,58,98,47,32,18,46,69,71,66,16,87,10,82,86,59,34,73,15,79,8,90,42,19,45,27,37,6,31,53,22,100,85,26,54,70,63,80,81,7,5,52,68,3,17,74,1,94,99,35,83,93,62,55,64,56,21,84,40,41,33,89,51,72,60,88,48,39,4,12,65,44,29,24,13,28,77,76,25,97,57,30,2,92,14,61,50,95,67], 17))
print(s.kEmptySlots([5,39,25,28,16,58,70,29,67,24,78,13,9,64,98,38,44,96,27,88,75,84,69,34,55,12,47,33,77,15,31,74,2,26,76,10,17,72,100,36,6,90,4,95,49,21,94,79,62,32,1,35,60,18,3,53,82,48,54,30,19,87,40,85,68,57,11,42,92,61,71,37,14,51,50,83,22,93,91,65,99,52,7,46,89,80,20,8,97,86,23,66,81,59,56,63,43,41,73,45], 4))