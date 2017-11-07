# -*- coding: utf-8 -*-
"""

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?


"""

import time
import bisect
import collections

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        M = len(matrix)
        N = len(matrix[0])
        target = k

        if M > N:
            data = [[0 for _ in range(M)] for _ in range(N)]

            for i in range(M):
                for j in range(N):
                    data[j][i] = matrix[i][j]

            matrix = data
            M, N = N, M

        # sms[r][c] means sum of matrix[0:r,0:c]
        sms = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for r in range(1, M + 1):
            for c in range(1, N + 1):
                sms[r][c] += sms[r][c - 1] + matrix[r - 1][c - 1]

        for c in range(1, N + 1):
            for r in range(1, M + 1):
                sms[r][c] += sms[r - 1][c]

        maxsum = float('-inf')
        for r in range(1, M + 1):
            for i in range(r):
                smrow = [sms[r][c] - sms[i][c] for c in range(N + 1)]
                # tmp = max([smrow[b]-smrow[a] for a in range(N+1) for b in range(a+1, N+1) if smrow[b]-smrow[a] <= k])
                # if tmp == target:
                #     return target
                # maxsum = max(maxsum, tmp)

                # find range whose sum is near target
                smidx0 = {} # k,v means minimum index of value k
                smidx1 = {} # k,v means maximum index of value k
                smkeys = set()
                for iv, v in enumerate(smrow):
                    if v in smkeys:
                        smidx1[v] = iv
                    else:
                        smkeys.add(v)
                        smidx0[v] = iv
                        smidx1[v] = iv

                smkeys = list(sorted(smkeys))

                for l, v in enumerate(smkeys):
                    j = bisect.bisect_right(smkeys, v + target, l, len(smkeys)) if target >= 0 else bisect.bisect_right(smkeys, v + target)
                    u = smkeys[j - 1]
                    if smidx0[v] >= smidx1[u] and j > 1:
                        j -= 1
                        u = smkeys[j-1]
                    d = u-v
                    if smidx0[v] < smidx1[u] and d <= target:
                        maxsum = max(maxsum, d)
                        if maxsum == target:
                            return target
        return maxsum








s = Solution()
print(s.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], -1) == -1)
print(s.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 0) == 0)
print(s.maxSumSubmatrix([[2,2,-1]], 0) == -1)
print(s.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 1) == 1)
print(s.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 3) == 2)
print("="*80)

t0 = time.time()
A = [[-5,12,24,18,-17,-5,-11,-1,24,-6,20,3,1,12,1,3,15,20,-7,20,8,29,1,-14,17,6,19,0,-15,15,22,-10,8,29,26,18,19,22,20,-6,4,-14,25,-1,13,-16,9,-7,16,12,-6,-11,-15,8,16,-3,18,-19,-13,4,10,0,24,-8,-16,3,-16,20,13,-17,26,-16,-7,-20,13,7,-9,-5,-8,5,5,12,26,3,10,-20,17,-4,4,28,-10,24,-17,16,-18,-11,-18,2,1,13],[-5,-6,-16,27,29,7,18,15,28,20,17,-7,4,3,-5,-8,16,22,-2,27,0,9,-12,23,19,12,12,-18,15,-9,7,4,22,-17,28,-5,12,-9,26,-20,9,25,22,11,22,-3,12,6,-4,13,10,-20,-19,-4,-10,4,-10,29,-17,15,-10,11,6,19,-14,9,-19,17,3,3,0,-19,26,-8,-12,16,25,17,0,-19,13,3,9,2,20,4,0,21,-7,-15,-4,10,18,-18,-8,22,-10,5,16,25],[14,-10,-12,-20,-19,-20,15,4,23,-20,0,25,8,15,-3,10,22,-18,9,-20,-1,-4,13,-18,4,3,15,28,11,17,-19,19,16,28,-10,13,-4,26,-1,20,-19,14,-3,-19,10,18,26,6,26,1,23,-7,18,20,-1,13,26,17,-12,25,14,-10,14,-12,23,21,-18,-19,-14,-5,-10,2,22,26,17,26,-9,-9,-20,-4,3,-3,29,5,16,29,-13,7,-1,10,4,17,-8,-11,13,-13,-11,2,28,26],[7,12,-2,-16,-9,-15,-9,27,-6,26,11,-10,-14,-20,-5,-16,22,21,18,0,17,15,11,13,26,-4,-20,28,23,-2,4,24,3,-17,-13,25,27,21,25,20,4,27,-19,-2,-1,29,24,14,0,-10,5,-15,13,27,16,27,3,-12,10,-9,10,-20,20,20,12,-10,-19,1,24,25,1,-7,12,25,6,18,-15,9,-18,20,7,22,-8,8,-7,-16,11,-11,21,-16,2,9,8,-1,-16,-18,10,10,27,9],[16,-1,21,21,5,29,-15,-14,17,-13,-14,28,6,-13,20,15,-13,20,22,-16,-1,-16,4,-14,15,-1,6,-6,-18,16,-3,-1,-1,10,-19,-16,-14,11,10,24,4,-13,-14,15,20,28,-19,26,-17,12,5,19,-3,29,25,-6,-10,-16,23,13,2,-10,-2,-11,2,-3,15,28,4,2,26,-10,17,29,-5,-1,10,-16,-19,-5,-6,-15,0,16,-15,-9,-7,9,11,9,25,-4,19,13,5,-14,1,-18,19,4],[14,-3,14,10,-5,13,-7,-4,29,-10,-6,13,20,22,9,21,-14,5,18,10,-17,1,-18,24,6,-10,22,-18,26,-2,-13,18,-4,0,-6,-2,7,29,26,13,-14,-10,-10,-11,6,3,5,14,-17,-20,10,15,1,-16,-2,27,28,-11,21,-9,17,3,-17,9,-17,-4,12,24,9,-15,20,-10,-18,26,7,6,1,-13,6,13,16,6,7,6,-18,11,11,21,2,23,21,26,1,20,-16,-11,21,12,7,23],[-20,29,21,-10,25,-1,29,-4,-3,23,-19,5,-19,-18,19,22,5,-7,17,-2,27,-17,23,7,-20,-2,-20,4,26,-12,0,16,-8,21,-13,27,12,24,-6,-5,8,11,29,-5,1,-12,17,-10,17,24,4,-20,18,5,-19,22,17,15,-1,5,7,-9,-17,-16,-8,-15,10,-15,0,7,1,28,8,-10,-16,29,20,-19,-13,4,-5,22,-13,12,-14,20,10,-6,-20,10,13,12,11,2,23,21,-18,20,-5,17],[2,-15,0,5,-11,-18,28,-13,7,-4,0,-6,-15,20,-20,8,-1,1,26,20,6,2,-4,29,14,-7,10,-7,5,23,0,-19,-13,23,22,-14,26,20,24,-18,-13,-5,27,-3,10,28,13,-16,28,-12,27,-4,-2,17,-16,19,9,-16,8,19,-6,-1,13,5,-2,14,16,6,8,8,1,4,-5,21,18,-19,-4,-4,0,-6,21,25,-7,8,9,14,19,-9,16,22,-11,6,9,0,-12,18,24,10,-7,17],[8,-9,7,5,4,9,23,22,-15,10,-15,11,-14,27,4,-8,22,28,-16,-18,-18,14,17,-3,29,-11,9,4,21,11,0,-12,-18,-4,17,14,-3,-11,25,-4,16,-5,-4,12,16,11,4,-12,-12,5,15,6,25,-1,24,18,-6,-10,-20,-19,-12,26,15,17,13,19,-9,25,27,4,-11,-18,26,23,9,11,0,12,-13,-12,20,2,-4,21,20,-10,-7,1,2,23,17,22,15,-4,-19,26,24,-19,23,20],[26,25,29,-17,-11,-5,-2,-12,12,6,-2,26,-14,23,-5,-15,16,-5,18,-16,-12,2,-12,4,2,18,5,-16,28,1,-13,0,29,-18,-8,-17,-13,6,-11,-3,-14,-1,25,-17,-5,1,-8,26,5,-12,-4,1,-2,-14,-8,23,16,-12,-3,9,-18,6,-13,20,12,4,4,6,27,27,-11,11,-17,25,27,-6,14,23,5,9,-1,16,24,-20,-18,27,23,27,6,29,14,19,12,-16,15,22,29,-7,-5,12],[7,-6,0,4,-15,28,-5,-18,0,-19,10,-14,5,-10,24,13,18,-9,-2,2,6,23,28,7,21,5,25,18,-13,18,-9,28,12,-15,-3,-12,13,-18,-1,-9,0,6,-11,-7,1,16,26,-1,3,-13,28,18,-8,19,-7,0,19,0,-13,-14,3,4,-18,-13,21,8,-19,12,-2,-11,-5,-17,19,22,-14,22,22,27,2,3,27,22,24,17,-1,4,13,28,24,22,-12,-4,-3,-7,-6,-7,21,-3,-11,-6],[9,11,-14,5,20,4,-20,-2,13,16,-4,-3,5,10,-5,13,1,0,25,-7,23,-7,10,1,3,0,17,0,3,0,20,3,11,22,21,-8,-12,17,9,5,7,25,27,3,-7,12,19,1,29,-16,13,-3,19,10,23,-10,6,21,5,16,16,27,28,-16,-15,-8,-12,-13,-16,-13,-15,7,29,-14,19,0,-16,0,19,0,5,-18,28,-4,-3,-18,-9,7,2,-3,-1,2,21,10,8,12,-6,1,4,8],[10,-9,14,-10,28,16,-9,-2,15,11,2,29,11,-3,21,17,-10,-7,-2,16,-6,11,-17,-10,-20,17,-6,1,4,-9,15,-13,5,-8,4,-20,-9,-15,-3,-17,13,18,8,-20,15,10,4,-11,0,10,22,-18,-9,-5,27,-2,-18,5,-1,1,20,-19,-11,4,20,-14,-10,2,1,-5,6,4,-5,-1,26,-4,-5,-3,-7,12,19,8,11,-7,8,22,15,-3,5,15,19,-16,25,22,4,-7,-8,-16,-5,1],[-6,-4,-16,21,18,21,8,7,2,29,18,4,0,9,-6,3,6,29,-1,-7,-11,-8,17,-12,22,20,6,9,20,-17,-11,26,-19,11,-17,22,15,13,26,13,29,-13,-9,5,19,-4,-19,-11,-20,12,9,13,7,14,2,25,10,-16,-9,25,8,-19,-9,-19,-3,26,-16,-12,-8,16,28,1,26,15,-12,22,7,28,15,11,3,16,-3,5,-20,-13,18,23,22,-7,19,-18,-3,4,1,-14,-17,-10,1,17],[10,-18,19,27,14,-16,-11,18,-11,11,22,3,5,-8,-10,3,-20,28,-12,-3,5,25,1,-19,25,3,-15,16,-10,12,-3,10,24,27,13,-1,-9,29,17,-9,-6,11,27,-18,5,22,20,8,9,-20,22,-16,-10,3,9,18,19,27,-7,19,25,15,3,7,29,24,7,-19,-3,26,14,25,27,9,-14,-13,13,1,15,10,4,1,-7,8,4,27,18,15,-7,19,5,23,19,27,11,12,-8,12,-15,20],[25,-1,-14,26,16,8,22,26,17,16,17,20,-3,24,5,-9,-5,10,3,26,-12,-20,3,-3,9,28,16,-10,6,5,-6,-15,-4,-19,7,-19,-2,13,21,9,4,-1,22,16,25,12,13,-4,-14,-11,0,12,-15,-6,-1,29,-7,8,-5,19,-14,-4,26,-18,-16,19,15,6,-19,-18,-12,2,11,12,-14,-2,-17,-11,-12,23,24,18,17,18,5,-13,4,8,4,13,5,16,24,8,29,-13,-8,20,12,-5],[16,27,-7,-13,24,12,19,15,6,-10,14,-12,-20,-8,19,-8,13,-18,28,14,20,-9,-15,5,-1,21,28,-8,-8,1,18,-1,27,-18,-13,19,25,-2,9,27,-13,12,27,-20,-19,20,11,-14,-7,10,14,-7,25,-19,9,-12,-17,-20,-18,12,-16,10,3,4,29,-7,20,21,1,14,-20,22,9,13,-6,7,-3,2,11,5,-12,-1,21,10,28,18,-16,28,6,-8,-17,17,-11,21,16,-1,-5,2,8,3],[-18,21,-15,-5,13,-20,13,11,19,-14,2,7,-16,24,21,21,26,29,28,-13,-15,7,4,7,5,21,7,29,21,-19,-17,-5,1,0,28,11,-19,-6,-3,25,-3,15,0,4,21,0,6,-20,27,-10,27,-19,-19,-15,-15,9,0,7,8,25,26,-8,-7,14,-13,0,12,7,0,-3,14,-17,-10,-8,-15,-6,-2,-11,13,14,-8,-14,-15,29,-4,19,14,-18,22,21,-17,15,4,-3,17,28,21,-7,22,16],[-17,9,-9,2,28,-2,-13,-8,22,0,13,4,-9,29,2,-11,18,-8,27,-10,18,-14,28,19,24,16,0,11,12,17,23,-1,1,15,-10,26,16,10,22,-13,5,0,10,-3,3,-2,28,-17,14,-15,12,-1,-2,-1,-11,13,10,-19,20,20,7,1,16,-19,-3,22,-11,11,-17,0,-2,3,17,-15,21,29,14,-8,27,8,24,5,-13,12,13,20,-6,1,13,20,4,3,13,24,-17,9,4,-11,-3,22],[-18,-2,27,-18,21,-3,-2,4,-1,-5,-1,-4,25,2,-14,19,-15,22,18,-1,-12,4,10,6,8,3,3,18,-1,29,22,25,-10,-17,18,6,3,-11,-9,-16,7,-18,22,-18,23,-6,-9,12,11,19,23,1,16,2,12,16,-5,4,6,-8,13,6,5,5,9,-6,13,6,-14,8,-2,-7,11,23,11,4,-4,20,18,20,-20,10,12,-6,18,22,18,2,18,-12,21,23,21,-10,20,2,-20,15,3,20],[-14,-1,19,0,-6,19,24,18,27,3,0,27,-13,-4,-19,-19,23,9,16,-8,-19,26,8,3,-15,-16,-10,-10,17,7,29,-14,-19,29,-2,3,10,-5,-9,5,-7,23,-3,15,-17,13,15,4,-17,26,28,12,-13,16,28,9,8,-15,15,-2,11,27,25,13,-18,-20,0,24,20,25,2,9,26,7,-11,25,-2,-8,4,-9,-9,5,25,26,7,4,-11,-7,-13,-3,-13,-8,-8,9,1,-20,12,-2,-15,-13],[27,-8,-17,-1,-2,8,4,13,29,-12,-15,-13,-3,3,-9,18,29,13,-18,-11,23,7,-12,-10,-2,0,6,5,-1,-14,14,-15,26,7,25,11,10,12,-14,27,0,19,10,-6,9,20,29,9,-3,8,13,2,-7,-4,-12,12,-13,25,11,2,29,-5,-4,2,-18,8,15,3,-18,-6,28,-6,12,-16,-20,-18,8,7,22,-12,4,-14,5,-11,28,20,20,15,16,0,0,28,13,1,-11,16,-12,0,11,18],[7,27,17,17,19,6,13,6,-17,-13,2,-1,-8,3,12,-18,-11,18,16,28,-9,26,22,-7,-15,-5,-15,17,-7,25,-18,2,8,-5,-1,18,18,-11,10,28,-19,-20,3,6,-4,-5,21,9,-12,18,-9,-19,-4,-8,27,-11,2,26,-12,27,-16,10,16,-13,8,-7,11,-15,12,-4,1,-8,21,-15,22,24,-7,8,-16,5,14,17,25,10,-12,-14,-3,-2,15,8,22,7,-6,20,29,27,10,9,7,-20],[28,3,2,-19,-19,27,-14,-9,16,-2,21,8,-4,16,15,-19,-1,22,28,-13,29,-2,6,-16,-9,23,23,-7,22,0,25,-2,3,-1,-11,-19,12,28,9,-7,8,-13,-20,-8,21,-19,-11,-13,-18,-5,16,-7,7,29,-7,25,-14,-8,-18,12,7,23,1,25,27,15,28,13,23,3,-14,-7,14,-11,-5,16,16,21,-9,3,-14,-8,7,24,2,-19,-13,16,-18,14,4,28,-11,-10,5,-5,-17,27,-5,23],[-5,-4,25,-17,7,28,-3,14,16,29,-18,9,-6,28,-7,6,-7,-2,5,-5,20,-15,-13,7,-19,-16,1,15,28,-9,-16,17,21,-2,-14,29,-15,8,-1,-2,28,15,0,5,-15,-19,-15,19,-18,-19,13,19,19,17,-6,-18,19,3,-8,11,-7,-10,4,-20,-6,22,9,-16,-1,28,-1,23,-15,29,6,-7,27,23,23,14,12,-7,-7,-14,-18,14,21,11,16,24,8,10,15,4,11,-4,23,-18,18,1],[27,-17,24,29,10,-7,4,-6,27,22,1,8,-2,13,-7,-8,26,-10,-4,16,21,-18,-20,-2,23,1,15,3,-1,17,3,6,3,24,20,9,17,23,19,20,-16,-12,-13,26,-19,10,27,-12,-12,7,29,8,-5,28,-9,23,20,19,-14,6,-7,13,-16,9,-14,19,29,-9,-7,-1,3,-5,3,29,25,-7,-8,14,26,-20,15,-13,-20,-13,3,-16,15,10,-3,19,12,20,-1,-19,-3,26,9,-20,25,25],[-17,-5,28,-12,16,13,15,4,2,-13,-20,7,25,-6,5,17,19,26,0,-19,-9,25,-1,6,16,12,-1,7,12,28,0,28,4,29,10,14,11,18,29,26,8,-16,20,-19,29,26,14,19,22,-16,20,-1,24,-12,-19,-2,1,27,20,3,5,-2,29,-8,3,15,3,-3,-2,-12,-15,8,11,4,21,-20,26,23,28,16,21,18,5,-4,29,23,11,-18,-13,-14,-5,-9,-3,-15,-2,5,10,29,24,9],[11,4,19,23,7,7,7,23,25,-1,18,20,-11,20,26,20,-5,5,21,0,11,-15,25,13,-18,11,-4,-20,-19,5,2,-5,29,19,14,-3,11,-14,-14,-20,9,20,-10,-7,1,-11,7,28,-1,0,-4,26,4,24,25,-1,-7,-4,12,15,1,9,7,19,-16,20,0,24,17,-12,14,23,0,25,29,1,28,4,5,-8,-18,26,17,-9,19,19,22,-2,9,20,10,-6,24,0,-18,15,15,29,11,-16],[5,-7,-19,11,9,-15,3,14,25,20,-8,-10,1,25,-2,11,18,-4,-16,-18,11,23,-20,22,-5,-1,-9,-13,20,-5,9,28,14,-8,22,8,-8,27,-2,1,-3,7,3,1,9,-1,3,20,-18,10,-12,3,8,25,-14,21,17,21,-4,-10,7,26,-8,9,9,20,25,12,-8,-5,14,9,11,27,-6,9,16,16,-8,-8,-10,28,9,22,15,-8,-4,20,1,10,25,1,19,28,18,-13,28,5,7,26],[13,-9,-2,-20,7,-11,-2,18,3,18,29,0,-11,7,9,1,21,28,-12,-18,-2,-12,18,-16,27,-1,-14,-14,-4,7,22,21,12,-20,-2,14,-6,10,-17,15,10,-7,21,-9,19,5,-19,22,4,25,-20,24,17,-12,4,5,23,2,-16,-12,-1,11,1,-9,6,23,11,29,29,23,14,9,-13,-9,12,-20,14,5,-19,-14,17,12,-17,-18,-10,5,-11,14,27,23,21,6,-2,-18,10,28,-14,4,-17,28],[23,18,25,0,1,25,9,-18,24,1,17,-2,22,0,9,-6,-10,27,-6,2,28,14,24,13,-9,-3,13,15,-19,10,-7,-12,9,17,13,-18,1,0,4,22,11,2,28,-18,-13,10,2,22,29,25,28,11,-6,-14,-19,-19,-15,23,9,-14,-19,-2,-1,-15,-4,18,24,27,3,-1,18,7,-20,7,-16,18,1,8,-12,11,12,-8,9,3,-4,-4,-20,18,-5,28,-8,13,-3,6,-5,-15,19,13,-12,-13],[19,18,5,-6,23,-20,6,2,17,22,-7,10,3,19,-7,-9,15,-4,9,22,26,4,-11,2,0,21,21,-14,0,8,-3,22,-2,15,-12,0,23,10,-20,-14,23,25,25,20,17,8,-20,29,-12,15,-12,5,-9,8,-3,14,-19,-14,3,25,20,-15,-19,28,-18,25,1,9,21,-17,9,-13,-19,0,6,-19,-1,7,22,-14,-6,10,20,-14,8,-13,22,-3,8,-11,-4,28,-1,-12,14,18,20,29,-5,23],[16,-18,23,-2,-2,-6,9,-18,17,-11,-12,-11,-18,-17,4,22,22,3,7,-17,-9,17,-12,3,18,7,4,25,-2,0,-12,-3,29,12,8,-5,2,27,22,23,8,25,23,13,15,-2,10,-13,-18,-3,-7,9,26,-19,-1,29,-5,25,26,4,16,24,-1,11,7,29,12,-8,10,21,14,-4,20,-20,-5,-10,9,0,1,9,-19,18,21,-2,-13,23,-16,23,7,-13,0,-3,-9,-1,22,-9,-13,-4,-19,-14],[17,4,-10,22,12,12,17,2,1,22,9,-17,-17,-6,8,28,3,-7,-7,23,21,0,-16,11,4,-13,-9,-12,29,24,-4,1,-12,0,-2,-11,12,26,19,21,10,15,-20,-3,-4,18,-20,25,-4,-10,-4,-19,13,-18,12,-20,3,-12,0,-12,-16,-1,18,5,-2,-19,8,3,21,2,11,3,21,-14,-4,3,16,23,4,24,9,-13,7,24,28,-2,6,0,-18,-14,15,12,28,21,-9,25,28,25,1,24],[-16,20,5,-8,15,-9,17,24,11,21,-18,25,26,7,25,-18,-10,2,0,-6,-10,-8,9,20,27,1,-6,7,1,-8,26,-17,18,18,-7,-2,11,12,-14,22,-4,6,0,20,9,28,-2,3,-1,-2,12,0,-17,27,-5,4,20,-5,-17,17,29,18,13,13,-16,29,2,-10,20,-6,-3,9,-13,-3,5,-20,6,-5,24,21,2,2,8,-6,-8,-10,-19,-1,22,-15,16,22,-1,20,25,0,12,-3,4,19],[-9,10,7,18,27,25,0,3,7,-5,16,23,15,21,21,4,-10,25,8,21,21,-1,-15,-7,3,7,-10,-16,-9,-6,-10,9,1,24,9,2,16,15,-20,3,-7,10,-2,2,4,-9,29,-19,2,7,0,25,9,12,-6,6,29,-16,4,9,3,-11,-1,0,16,17,7,-15,-20,4,-8,13,19,17,-16,18,13,12,16,8,17,-15,13,19,25,24,-19,-11,-18,15,-9,-14,1,-5,1,-13,23,-6,9,-9],[28,-10,-2,7,14,20,-20,3,-9,27,24,-9,27,-11,17,-3,-5,-18,1,22,-19,-2,11,-4,15,18,0,-12,-13,-9,-17,16,21,17,12,-12,-18,-10,-18,-11,26,-9,-17,6,-19,25,18,-12,18,9,22,5,12,-14,20,-4,-6,11,-20,1,29,3,-17,9,17,8,-7,22,-20,-1,-8,15,17,-16,17,13,5,-20,0,10,19,8,-5,25,25,-18,28,17,17,3,13,15,26,-11,-4,22,-14,12,-1,1],[11,-6,20,19,-14,-13,6,9,-2,-17,-16,17,13,7,23,-9,7,13,-13,8,0,2,12,-12,29,-1,5,-7,23,-11,8,-6,16,2,19,29,10,20,-11,14,-2,-10,16,-19,5,2,18,-5,20,19,4,10,0,13,10,-2,17,0,10,13,-4,-4,6,-11,-8,25,11,8,28,18,-11,-4,0,-8,17,-5,-10,11,16,-1,15,2,15,4,13,-1,-9,24,22,-17,12,-6,28,16,21,-10,15,16,14,3],[29,-8,12,-18,27,-18,0,22,7,14,-20,-12,-15,-8,6,9,14,20,16,18,-17,16,23,15,18,11,3,6,10,14,-18,4,0,0,-1,-5,5,6,29,-4,-1,23,3,-2,-3,-3,9,29,-3,-4,-1,15,17,15,9,-20,23,8,-6,-13,1,-4,-3,-3,-18,25,0,-15,-15,-17,18,1,18,7,1,-1,10,19,-4,4,-17,26,2,-9,-7,-9,14,7,22,-13,13,27,-1,-12,9,25,-12,16,21,0],[-9,28,27,25,21,1,-1,2,3,24,-5,-5,-3,21,17,20,8,-3,0,21,2,15,-8,15,4,28,18,-16,-6,12,12,11,-8,1,20,-5,26,-20,-7,19,-17,-16,24,16,26,4,6,-1,15,0,-20,-18,26,-19,19,4,27,13,6,6,9,-1,8,-10,28,-7,22,22,5,16,5,0,-4,23,-20,-1,11,5,-7,12,9,-6,-8,-15,-6,-11,26,-12,-1,-14,-16,-9,22,23,25,29,28,1,9,-12],[22,27,-5,-8,27,20,7,-3,16,4,-13,9,6,17,-19,-18,-17,4,11,-5,11,17,-18,10,-6,13,-6,26,13,3,-11,11,13,24,-15,4,-12,4,-15,-16,0,25,-8,13,-3,3,6,25,-8,17,6,4,28,-11,11,-10,-6,20,-20,-6,-4,-10,1,-5,-7,-2,-1,10,-3,28,8,19,7,-17,-19,1,-18,14,19,-13,-4,16,9,-15,4,13,0,8,-5,10,-3,18,-4,12,19,29,-4,16,-9,4],[29,26,20,-18,-7,8,11,-17,-16,6,-6,26,24,-18,-20,10,18,27,21,9,0,-8,6,6,-12,-19,-3,-5,-18,-11,-19,0,15,-9,11,21,19,8,-20,25,-17,-1,19,22,-1,26,-1,17,23,14,18,12,13,-13,20,-4,25,5,23,3,1,11,-12,-18,-3,-3,-11,-13,4,2,-4,-5,-2,19,14,22,16,20,9,17,28,3,-18,3,-17,13,-20,-14,13,-15,-2,20,-6,-18,-20,3,-13,-6,12,-12],[7,2,-10,-19,-6,26,-18,-20,11,11,20,26,1,0,18,8,12,13,-3,21,-17,-15,8,-17,10,-1,26,20,6,10,-16,-4,-5,17,-5,-10,3,-11,4,0,29,29,-10,8,2,24,-20,-15,0,-8,11,4,-6,13,3,18,2,-11,7,-5,18,20,28,8,8,0,13,-17,18,5,0,7,-14,15,25,18,27,18,-9,13,12,2,-3,21,21,4,2,-3,3,4,22,6,22,-10,-4,-12,12,-17,-9,-10],[23,-1,1,29,23,-18,-17,11,14,24,3,-8,11,19,-7,-4,21,25,-1,4,-3,-7,0,-14,12,2,7,-14,-6,23,-7,-3,-7,-9,-11,11,8,12,-15,15,14,28,0,25,29,20,-11,-9,-15,-2,-4,1,12,-19,7,5,6,-3,-20,-9,18,11,-19,-12,24,14,10,9,10,-6,0,24,27,11,-16,17,24,-14,-13,-16,18,-2,19,24,-17,22,-14,3,-6,26,0,8,3,-8,-17,-12,-13,-8,28,-11],[-4,14,2,5,-18,-4,-11,-5,11,0,23,8,28,-12,16,15,-14,16,-18,3,-10,21,12,17,26,12,11,22,-19,-3,3,-8,2,1,6,26,13,6,-5,-13,14,-15,17,0,12,-6,-4,12,2,-8,5,-13,-1,22,18,-20,4,9,-11,-12,-11,29,-18,-2,-13,14,-2,11,-18,2,19,23,-6,-7,19,16,13,-9,-14,-3,6,19,14,-15,-13,4,-19,-19,-2,0,29,18,-10,-1,-13,-18,-11,-13,12,-1],[-14,12,-11,7,5,4,-5,0,8,-8,-20,-2,27,0,17,14,-13,13,-4,22,-12,-4,20,-18,2,-5,11,16,-1,-13,-6,20,0,22,18,25,27,13,28,29,-13,9,19,-14,20,28,2,-19,27,-9,-7,-7,-19,20,0,-17,14,17,29,14,17,-11,28,-12,20,17,1,21,9,-13,-18,21,14,-2,-9,12,13,-7,28,-6,8,10,-1,4,5,-12,-6,-17,10,28,13,19,-16,11,10,4,-16,6,-20,3],[-6,26,18,24,-11,-4,-12,-12,-7,13,-19,13,24,5,6,-17,-14,-2,-11,24,-20,-17,21,23,-19,21,2,24,7,-7,-17,-15,-2,-9,3,13,4,28,12,4,0,-15,-20,4,23,-15,-8,-20,-3,24,3,7,-15,18,3,4,11,13,-17,19,-11,-19,16,19,-5,1,9,-4,28,5,1,25,21,-18,13,-1,10,22,-4,-19,27,16,-8,-3,0,28,-1,-7,-11,-10,13,-13,-9,29,-11,-6,-2,22,18,-18],[-13,8,-7,19,-20,6,-19,-15,17,18,-10,-11,-16,6,21,18,-2,22,-8,-4,17,2,17,-12,-20,-5,5,-5,-3,17,3,21,-8,3,-13,-10,6,6,-16,3,13,-15,-1,13,16,-17,7,10,-16,18,1,29,-12,9,4,23,15,-5,22,3,19,7,21,29,18,14,19,-9,-10,-11,6,13,-4,-4,25,1,18,-12,0,18,-16,14,-6,-13,3,4,-18,-20,-7,26,7,-6,17,-8,16,-5,10,28,2,-14],[28,-9,-7,-5,-1,1,7,29,17,-2,-1,-12,-20,-15,18,13,3,-16,7,-19,22,-4,16,-12,-16,19,-9,9,5,-8,-11,17,-11,-5,29,-2,-18,16,13,2,21,23,16,4,14,-16,21,-11,-14,11,16,-15,13,23,-16,18,-11,-8,-16,-19,-18,16,8,19,17,10,7,8,-3,-2,11,6,25,2,-3,-12,-19,10,19,-17,12,11,-2,6,4,-13,-7,-8,20,16,-15,8,-10,19,5,-6,-19,24,-10,-1],[0,-18,1,-1,-19,-1,-10,9,-11,22,6,-19,7,3,-11,-8,6,13,29,0,28,0,10,6,25,-16,-6,-3,5,18,24,28,21,-2,1,7,-15,-7,1,-2,16,24,26,23,-9,15,24,28,5,21,7,21,17,22,13,11,-18,-11,-15,4,-10,21,18,25,17,24,-10,27,21,3,10,15,16,0,10,20,13,-13,5,3,8,26,-11,4,2,-1,28,14,19,21,-11,9,-9,5,-20,22,1,29,-17,26],[-5,-19,-9,-6,14,-7,-4,17,-13,-9,14,11,0,21,-10,1,3,-5,-12,-12,17,12,-4,27,-11,2,-16,20,-7,-3,26,24,-8,4,-15,21,12,10,11,-16,8,24,17,-6,4,27,-11,-17,-5,3,7,-17,-18,-7,0,-6,5,-9,-12,24,2,18,-2,27,-16,-4,-18,2,-15,-1,14,-13,-8,-5,-4,-15,17,24,-2,25,-17,10,0,-7,24,-17,5,-4,19,13,-20,9,-4,-2,-7,-5,2,24,19,26],[-17,7,-7,17,-5,6,13,18,11,26,-8,-14,8,-3,-2,8,-5,4,19,8,-2,-15,-18,-16,3,20,5,5,-19,-1,3,8,9,23,4,0,-18,9,-17,15,15,3,-18,-18,1,24,-5,-20,24,-3,-4,7,2,-15,15,-16,19,-5,6,26,17,-3,18,28,12,-1,-1,-20,26,-4,-2,-18,13,21,9,-4,6,29,-13,1,-7,7,22,-8,-2,6,13,6,18,11,-10,-10,-18,-13,-14,22,29,14,2,-10],[5,4,19,12,-15,-6,28,-18,0,11,-18,17,26,-2,19,26,-6,-1,29,-11,-3,23,-20,5,14,14,6,27,-11,-7,12,-17,-13,17,-9,21,-4,9,15,-20,-10,-1,8,-9,-11,-14,19,0,21,12,14,22,28,20,14,29,-1,20,11,-16,9,20,14,12,-17,29,-14,-9,-11,-15,25,15,19,-2,-12,6,-13,-3,27,19,-14,18,14,-19,22,-20,-3,-12,26,26,3,4,-2,28,-8,3,-5,13,-4,27],[28,1,-8,-13,-8,24,-20,3,17,14,-13,24,-17,23,-1,16,14,-14,16,15,29,11,29,19,26,6,-5,-2,-2,-14,25,-2,19,-19,22,-8,18,-10,-10,20,14,19,0,12,-17,8,-20,7,12,-16,5,9,-7,19,17,25,12,10,5,-1,-11,-6,-17,18,-9,12,-1,1,14,-15,21,1,9,6,-1,1,14,-3,20,-11,-12,1,-16,-6,0,4,-17,-2,6,4,18,-14,-9,-7,3,-19,-16,4,25,20],[5,-5,13,9,0,28,10,-9,-7,-3,15,5,28,-12,19,8,-14,-19,-13,-10,-18,-3,-20,-17,17,4,6,-14,23,20,-2,5,6,16,2,11,13,-17,-19,22,-4,23,-8,27,14,9,-6,-4,10,-5,23,-19,-1,-6,1,28,6,21,28,19,10,-7,-16,5,23,5,20,12,-17,0,-11,19,22,1,-5,19,-13,23,-11,6,25,17,1,-19,12,-4,-4,-3,1,18,4,18,7,5,-19,0,-15,-1,4,-3],[-2,-18,-7,9,10,4,16,-3,-10,16,20,18,21,-3,-3,-9,-3,27,-13,-10,22,1,-18,8,25,-17,-13,-9,-3,29,2,-5,-11,13,-13,26,25,17,-5,10,13,23,14,-13,14,-4,17,12,22,-5,-1,22,-6,15,12,-13,-7,13,29,18,18,1,14,19,11,4,12,4,22,-17,6,15,13,17,-15,21,-5,-13,2,18,28,18,-7,-6,-18,3,-8,15,-11,-20,3,3,1,21,21,-2,7,-6,6,13],[10,-8,-11,3,10,6,25,9,-8,22,6,17,-1,20,5,13,-5,1,18,29,-17,25,19,-7,21,21,17,-13,-16,-14,11,26,28,12,14,17,-20,3,12,-17,28,28,-15,-14,22,-5,-7,-11,14,27,21,17,8,-12,1,16,11,-9,2,6,-2,-12,-3,-9,-16,-10,-15,-10,21,-11,20,25,-20,-3,7,-7,12,11,25,17,-8,7,27,0,14,-14,27,7,-5,7,16,-1,-16,28,-16,-16,-5,-1,23,21],[-13,1,-9,2,1,14,28,4,22,10,-9,13,-6,-7,13,-6,-6,14,-14,4,2,-1,23,-10,-18,-11,-8,-8,18,-9,26,-3,13,-11,-19,-12,16,26,-6,-10,15,4,24,-7,4,6,-10,-9,1,26,-1,-5,4,27,-4,-20,9,18,6,1,-14,15,-3,27,-17,-17,-3,7,8,-9,-7,27,-8,28,26,16,-17,3,-18,10,-10,-7,-10,7,-2,15,-8,-15,-15,8,-6,-18,4,28,19,-15,28,22,25,-14],[18,-5,-10,7,28,27,12,-14,-1,10,-3,21,12,-9,-20,6,-14,12,5,9,9,-7,-13,-20,17,16,-11,19,-19,27,-14,8,-4,21,-19,13,9,-4,18,1,9,23,23,14,-12,-19,19,4,-7,-17,6,11,-18,5,2,8,-4,12,20,29,2,24,-17,24,11,11,-18,11,-12,-15,23,23,29,-7,0,-20,-1,12,29,6,6,15,-17,-18,-16,4,-15,-2,3,25,12,-2,11,24,16,-14,-7,-17,21,-14],[0,28,7,3,-2,-11,-1,1,-17,0,-8,-16,13,10,22,4,29,-8,0,-16,-13,25,24,3,28,-6,3,20,-2,23,10,14,-18,18,0,12,13,17,22,-11,-19,-16,26,-4,-3,-20,11,25,-20,19,-6,24,-9,-3,17,0,19,0,27,4,15,-12,27,-13,-5,8,-3,24,12,-14,-14,-17,-2,3,-5,-11,-20,2,18,16,-15,13,24,9,-2,16,3,19,23,17,-15,-2,-1,-14,-20,-16,28,-17,8,-1],[6,25,-5,-14,-9,-13,13,27,10,11,27,17,17,26,-14,-16,13,4,-11,24,3,-2,-9,23,6,-18,-3,-11,22,-16,10,1,27,-1,16,-8,-5,28,13,27,4,4,-11,20,23,-6,23,-4,-15,11,-1,-16,-3,-9,10,-5,18,21,-18,20,14,19,-7,11,22,-8,29,11,15,0,21,13,26,-10,0,5,-8,26,25,-1,17,2,-9,22,28,24,18,6,28,10,28,-18,-6,4,-16,17,-11,12,16,8],[16,15,17,-9,-6,21,25,17,-17,-19,-18,10,-12,-4,22,-5,18,2,9,-2,12,-19,5,2,27,0,-15,7,17,-4,8,17,20,19,27,-12,-18,13,-5,-5,19,24,16,25,17,14,26,-6,23,-10,-5,-2,27,16,3,8,19,-18,6,8,7,-7,-1,28,20,18,9,20,-9,11,4,11,25,1,17,18,-18,16,-8,22,11,17,16,26,-16,5,-12,16,-14,16,-19,-19,11,14,2,29,22,-8,-11,3],[-7,18,16,21,0,2,21,20,-20,-6,24,-6,2,4,-20,-2,-16,14,0,8,29,-15,16,26,7,27,27,-19,2,5,25,24,21,-2,21,-13,4,-2,-4,-3,-12,2,-11,-5,-3,-15,-5,19,4,9,-13,8,-5,-9,28,11,2,-14,-17,0,25,-19,22,-10,27,15,-3,-10,18,16,-4,5,19,16,3,18,-4,6,15,14,-7,-18,-15,5,2,25,3,7,-14,17,28,-18,2,-14,-15,11,8,8,-15,15],[-3,-18,22,-18,-20,16,-16,-11,-18,8,-5,29,-6,-17,-7,28,25,-2,4,6,12,26,4,18,-3,16,18,1,1,-7,25,-2,20,17,4,5,-18,-14,12,4,-14,24,5,10,19,-20,23,-11,-20,20,1,-14,19,29,-16,27,-2,-6,8,24,29,-2,22,-19,8,-16,25,-15,-20,8,19,-3,2,18,15,10,25,-20,25,24,-8,10,7,29,26,8,3,5,-12,25,7,-16,13,-3,0,8,-12,-8,0,-10],[-16,-8,18,-15,16,-1,9,17,-10,6,-7,-15,11,1,-14,16,2,17,19,-4,17,-12,-19,20,24,25,28,25,29,27,-9,-12,13,-8,2,-7,0,18,3,19,18,-11,-9,29,4,18,16,20,28,-8,17,17,-18,7,14,23,-19,11,24,-3,7,-9,-4,18,7,6,19,29,-14,-11,-19,12,19,21,27,-1,-12,-1,12,13,-7,12,-19,-14,17,18,23,23,4,13,26,11,-13,9,6,22,18,-4,26,-11],[29,7,-9,-9,11,8,-3,25,-4,-6,-4,25,22,22,14,9,-2,6,-14,0,-10,-14,17,9,7,2,17,28,-1,17,1,-11,8,5,14,25,1,-15,23,-11,7,-20,15,-18,21,21,16,-7,8,26,2,-9,8,-11,29,-19,19,5,-16,-15,1,4,-2,10,-5,1,-4,14,-10,13,-3,11,21,12,25,3,11,23,19,-14,4,18,-17,18,21,-14,-5,22,6,-6,19,27,26,-19,27,27,-3,21,-3,-16],[-17,-4,28,12,13,8,1,24,28,6,19,16,0,-19,6,-15,-4,26,14,0,1,-6,-5,-8,2,27,10,-1,-16,-14,-20,-7,12,21,-16,-14,-1,13,-17,-1,-20,23,-1,20,-16,-8,-1,-11,26,27,12,-1,-14,-15,0,21,-18,-11,-1,-17,0,-5,3,20,28,15,-11,-7,19,-18,-7,7,-5,-11,3,0,-15,5,4,12,26,14,21,-10,7,18,22,8,28,-3,-15,-20,7,11,-6,-4,12,20,11,-2],[16,1,17,-11,13,-1,9,-19,-11,23,13,18,-12,10,-15,17,29,14,-19,15,3,10,0,-11,13,21,25,9,-1,3,-12,20,-17,1,27,-17,13,5,12,25,7,-13,-18,28,-9,-5,14,21,10,7,16,11,18,12,-19,15,-19,11,3,-3,14,-3,2,-3,11,-13,-8,19,14,-9,2,28,-12,5,18,1,7,0,-2,20,-17,-20,-9,-1,2,-16,13,13,17,7,-16,-16,-10,6,5,19,19,-5,28,20],[-7,21,25,5,-9,-20,-7,-4,16,28,-17,12,-14,21,9,-15,28,19,8,11,-2,-16,-11,15,-14,21,12,-19,1,24,0,12,18,13,17,12,-1,-11,11,-10,17,29,6,4,-1,3,-13,29,9,17,2,-11,-7,-5,4,6,16,-13,5,-3,-11,-4,12,-11,-20,21,-12,21,15,22,-11,2,25,17,25,0,-8,5,21,-6,16,-3,-10,29,-6,16,0,5,-15,14,14,1,24,-14,-7,-1,10,-11,24,-9],[20,-1,-17,1,2,-1,-8,14,-9,19,10,-4,25,0,19,18,21,26,-6,3,-12,22,-16,11,22,21,5,25,-17,-9,13,-14,20,-15,25,-8,26,8,-3,21,17,18,-15,-13,21,-4,1,-7,11,-8,18,4,14,28,29,-14,-16,-19,-4,20,10,29,-8,-14,24,19,-19,0,28,7,-8,9,-7,-1,7,5,28,2,29,0,-3,-6,8,-13,20,25,9,-15,-7,1,29,-6,14,16,-3,12,1,-10,-16,-11],[-20,-11,27,-4,21,22,19,27,-18,28,-1,15,1,-7,-7,16,-7,-14,16,5,-15,-3,10,-11,4,27,26,-15,26,10,-2,5,-5,4,22,-13,-12,28,-1,-3,20,13,-17,-12,19,24,21,23,24,-8,-7,9,-16,-2,-16,1,16,-19,-17,-19,-2,26,-13,2,25,-16,9,-9,-6,-4,-10,-5,-9,8,9,20,-12,3,21,11,-6,21,12,-14,27,-7,27,-3,27,8,-20,10,26,-13,-20,15,20,22,-13,-10],[-9,-10,-18,7,13,7,-19,-2,2,-10,7,22,-4,15,16,-9,4,-1,-20,-4,18,2,17,6,7,-5,21,21,-9,19,-14,-4,-8,14,15,-11,-16,-17,5,-17,-6,-10,4,11,24,23,25,-19,16,-8,-19,7,14,0,24,1,-5,-7,4,14,19,9,19,-19,-16,-11,29,-20,23,21,3,16,25,-14,6,12,-1,-8,10,3,-16,14,4,17,12,-17,-3,-1,19,-13,-13,24,18,19,1,-3,25,24,28,-9],[22,-1,13,14,8,-11,21,-13,0,-6,8,23,-12,17,-17,9,17,-20,12,26,-19,10,14,17,28,-16,6,-13,16,28,-16,3,14,27,-14,10,-16,-12,25,23,28,16,6,23,0,27,-8,-20,-8,-9,16,-8,11,-10,-11,16,-4,22,14,12,-1,-16,-3,-18,7,23,-10,-11,1,-1,23,-8,28,-11,3,8,-4,-10,-20,-1,23,-12,15,27,-12,0,-12,-7,28,12,-18,20,4,-8,21,-2,-15,-1,26,-6],[28,18,21,2,13,1,17,20,-20,21,1,-13,-13,29,3,-19,9,-9,-20,24,-15,23,20,29,4,6,7,-8,-16,17,11,-17,11,-14,6,14,12,9,-3,3,11,-15,18,4,0,20,-14,9,-17,27,21,6,22,7,-1,8,13,-17,-15,-10,16,11,26,-12,-12,22,1,9,19,-9,9,-12,5,25,1,-8,-10,13,4,-20,5,13,13,-12,-6,27,9,17,-17,18,6,4,4,-5,18,25,-4,-14,22,-11],[23,-6,-20,6,-15,11,-5,0,18,-14,-4,8,1,-14,-10,8,-10,21,7,14,-8,5,17,17,7,-3,17,11,8,23,21,-8,-11,-17,28,15,-17,-11,-18,12,11,29,-19,19,25,25,22,18,-18,-8,-5,12,-7,-3,-19,15,-7,-12,-16,3,27,16,-18,24,0,28,26,-14,5,22,-10,16,28,28,15,-20,9,-10,7,13,19,19,27,-4,8,11,25,19,21,-17,14,-5,20,-3,-11,13,19,20,22,28],[-4,11,-2,17,-6,12,-19,27,16,17,11,5,-11,10,-13,-15,22,-13,-3,-11,7,27,-15,-3,-7,25,23,22,13,-16,-9,4,25,25,-18,27,17,-10,15,16,-9,19,0,-8,23,-16,25,0,9,18,20,-15,7,-10,20,25,22,-13,29,-16,7,16,7,-18,4,7,3,8,-1,-3,15,-14,-1,9,1,8,7,21,-6,20,14,17,21,24,-14,25,-5,14,14,-3,5,-15,16,-20,27,-5,15,-5,-15,11],[-14,-3,-19,-15,-17,-13,-4,-10,-14,-2,6,-10,10,-4,26,22,-19,-8,16,-15,11,0,14,-17,13,-2,27,17,17,7,21,21,-11,0,11,9,21,-12,26,-1,13,18,-8,7,26,29,-10,3,20,-2,24,15,-20,0,-2,4,-2,4,28,6,-6,-12,-3,-6,20,9,1,27,1,-11,22,27,27,-4,-15,-10,29,-1,-13,-14,22,26,-13,11,16,14,17,-9,4,28,0,25,-17,11,21,-10,23,25,-19,9],[-12,-6,-10,6,-3,-10,27,13,15,-15,19,-14,-19,24,10,24,-2,1,-19,-20,12,26,-3,-12,-1,26,-20,5,6,-11,-20,12,0,-12,8,-14,29,8,-2,-2,15,-6,10,-1,13,15,13,3,1,19,-4,21,-11,-16,21,-3,13,-18,25,3,-4,-11,-10,-2,12,16,-3,2,2,29,-9,9,-13,28,-5,-7,-7,1,-3,-15,-11,17,4,-16,28,-16,8,5,-16,-17,28,19,13,9,4,13,27,14,-4,-18],[7,-16,15,7,-2,2,6,-14,-14,-19,12,11,-3,7,26,-1,-1,-2,7,6,-1,-14,-10,26,-16,27,-19,8,18,21,29,-18,3,-6,-6,-20,-14,5,14,-14,11,12,-8,-9,23,14,-2,7,5,-4,-16,24,19,18,9,14,27,15,-7,3,-14,-18,17,15,29,9,19,-4,-4,25,18,18,3,-20,-17,-13,-15,5,27,-11,28,-6,2,-8,8,5,0,-5,15,-9,-18,20,-16,1,10,-18,-8,8,-20,14],[-17,-9,14,-5,12,18,19,17,8,10,-20,-18,25,1,11,26,23,18,-19,16,15,17,3,-14,-7,16,12,-13,11,-4,-3,25,-10,-19,2,1,14,-15,11,-18,-5,22,25,4,8,-12,6,-3,13,6,-19,13,16,-1,-9,-3,1,-8,23,-2,9,11,-8,29,20,-18,10,20,14,19,-14,5,15,-10,-20,-1,12,2,-1,27,-17,-8,13,4,-3,-11,-14,-17,-15,18,11,13,21,29,17,24,15,-9,2,26],[18,0,26,-4,5,-2,10,6,16,5,-18,-6,12,-16,-13,-18,13,18,-13,-17,-4,-17,22,21,-17,-5,-10,13,6,-14,20,24,27,9,4,17,1,3,-20,11,21,19,-14,9,-15,12,-2,21,9,-7,-4,0,27,-18,25,25,26,26,-5,-14,2,-11,10,-3,-4,0,-4,-18,-1,26,22,-8,0,9,-3,6,15,5,4,2,3,1,13,28,-5,27,28,-8,3,19,0,-15,14,17,-3,23,6,-11,-6,-8],[-14,-17,-3,-12,21,-12,-8,21,17,-16,-18,9,4,22,4,9,5,20,-4,25,25,0,-15,-10,-1,-2,21,-12,28,-12,20,-12,6,17,-15,23,-11,12,-5,9,2,1,-12,-6,11,-18,15,27,-10,-20,8,2,11,5,1,-18,-16,2,22,14,-8,-12,-2,27,-8,-20,12,20,-16,-2,11,11,16,17,13,-20,-1,-14,-20,-18,22,14,22,-3,2,18,-10,-4,6,15,-10,-10,-3,-13,-18,0,23,27,22,27],[11,25,8,-9,-16,21,12,-7,15,-3,-8,28,-6,-4,-18,26,15,13,18,22,-10,0,-3,-6,-11,2,-7,10,26,29,23,-8,-2,-17,28,-3,1,15,-12,-5,14,-6,11,23,26,9,-4,-11,8,14,9,-16,-11,-2,29,-10,17,4,15,4,-4,14,-9,2,14,27,-15,29,22,-4,-6,-17,-9,-5,-16,27,12,14,4,23,26,-15,11,-6,9,23,22,13,-11,-2,1,3,27,-3,-20,-7,0,-16,17,-7],[8,3,18,29,17,4,20,-12,3,17,29,1,25,2,13,15,-19,27,-6,-4,-14,10,2,14,24,6,-19,9,10,-4,7,28,12,24,27,1,-15,15,-9,6,24,-14,9,-16,0,-9,24,-18,28,0,-18,-17,-3,2,-18,-1,15,0,14,-7,13,-16,19,13,25,6,3,10,29,-20,7,-18,-12,-16,-19,18,5,17,18,-1,-3,10,-2,-4,20,12,25,18,20,12,16,-5,-7,-5,18,28,-19,-13,-5,-2],[6,-13,22,25,-14,3,-1,-15,-19,-7,0,-10,-9,23,-6,-13,22,0,10,23,-20,6,-8,-3,5,5,20,9,21,-6,19,14,17,-5,28,27,-2,27,-18,-12,13,8,10,-1,-13,-3,-18,-18,-19,-20,0,-19,14,23,22,-12,-5,18,-14,-10,10,2,-12,10,-1,15,26,0,28,2,-4,-18,27,-20,0,-10,-14,-14,-8,21,0,-13,9,17,-7,-18,26,-9,-18,17,12,10,1,25,-1,-12,1,12,19,11],[-14,-13,26,12,18,23,24,10,0,24,-14,24,-13,4,28,21,2,-3,2,18,11,29,24,16,7,-18,-4,21,9,-16,29,10,7,-14,18,20,10,-6,-16,14,-10,-13,26,1,-9,26,-13,25,11,-5,16,13,-1,25,0,-16,15,5,4,-11,0,22,-13,-11,17,-2,-11,22,-15,12,-20,8,16,11,-11,-20,1,-9,-8,-9,0,27,-1,14,21,-12,-19,0,-14,25,19,17,26,29,27,-13,-16,-4,1,22],[-6,26,29,18,26,-2,-1,-7,-18,15,19,22,22,11,29,19,-7,-20,7,-20,20,-7,16,27,-18,19,-1,-16,12,3,17,20,-19,25,11,21,21,9,-3,-11,-11,29,-8,-11,5,6,20,-14,4,-9,19,-19,-8,14,17,19,-18,16,-17,26,-16,1,-3,-4,16,-1,25,21,-16,1,9,-9,-18,-14,-3,1,-2,-1,-4,-7,0,4,-12,-3,0,-6,29,-18,-1,27,-7,0,20,16,-14,22,25,-6,-14,-20],[-3,23,22,7,-2,23,8,1,28,8,3,1,20,-18,2,2,1,-5,9,8,0,-1,-8,8,17,6,11,17,-11,-11,4,-9,-12,5,24,13,-5,3,11,22,28,9,15,25,-6,17,-17,-3,27,17,26,29,6,26,24,25,11,-15,11,-6,14,3,-9,12,-10,3,22,24,-8,14,27,-5,19,9,24,0,3,8,-3,-17,-5,20,17,-10,10,13,-2,13,27,-17,11,9,17,2,-11,-16,-3,-14,-2,22],[-5,26,22,-7,1,7,18,18,-6,-12,-20,16,-14,-2,18,29,-14,-9,11,0,0,21,17,-14,-16,16,-8,-7,20,19,-13,29,-13,-12,13,21,-9,-17,21,16,-3,-3,17,18,-16,18,-20,-2,23,7,-17,-13,-11,2,0,16,28,-18,25,19,-17,9,9,16,23,7,1,7,-13,12,22,-8,5,22,-13,2,-2,29,19,24,7,15,26,-6,-9,21,-18,-3,2,18,-6,19,-16,-10,13,11,-1,-13,-17,-19],[7,25,21,26,14,-7,24,-4,28,22,1,19,-18,1,24,11,-5,-14,-19,-5,13,18,-12,15,6,-20,13,-8,1,25,-10,25,-6,-11,-10,19,-19,23,25,20,15,1,23,-6,25,8,21,29,0,-18,1,29,-2,-10,-3,-15,14,21,-9,-6,-10,-2,-14,8,15,26,11,-7,18,11,-14,-8,7,-4,-14,3,29,13,-16,-2,8,21,24,21,-2,17,6,26,-10,-3,25,-17,18,-6,16,21,-7,6,-12,20],[28,25,1,3,9,-14,-1,14,23,-3,19,-20,-4,-18,0,-3,26,16,3,-14,26,-6,29,0,28,-7,23,20,11,-6,17,-20,4,26,-2,13,-18,6,7,20,-6,10,7,28,1,14,29,-14,-10,-11,-11,-13,23,4,13,3,-1,26,1,21,23,15,-2,16,15,19,3,16,15,-9,4,-5,-12,9,20,-19,-20,1,-7,2,-15,11,14,16,21,-3,-13,-14,8,14,-7,20,25,22,28,-19,-16,2,9,-4],[-1,17,-16,-12,-13,-5,7,-17,0,0,3,-20,-18,25,11,19,-1,9,-6,-18,-18,-10,5,18,22,-19,19,9,-3,5,22,-9,4,-9,-12,-3,3,2,16,8,2,-15,-11,26,-8,25,14,3,-4,17,24,-9,-4,-19,-5,6,-10,-15,0,10,-9,-16,-19,20,3,-6,-10,10,-15,2,11,-10,-17,3,12,14,16,-20,2,5,7,26,-15,-15,25,11,20,23,-20,23,-1,-10,28,-10,-5,-6,28,24,13,14],[-11,-14,-9,-3,-17,15,-17,3,13,6,-11,10,1,-13,17,21,6,-18,14,-4,17,25,9,12,0,17,-18,6,21,2,-20,3,15,17,0,15,27,9,28,27,0,-2,-13,-12,22,14,-12,26,17,7,16,-8,18,5,-11,9,14,-9,-20,-10,9,-20,-6,7,-17,5,-17,20,3,4,-13,-17,17,23,24,-4,3,11,-12,17,5,25,-20,-6,-12,18,-5,-1,25,12,7,-4,15,4,8,5,22,-11,0,4],[22,25,19,29,27,17,-6,-19,0,17,3,-10,-3,-10,23,5,25,-3,18,22,24,13,15,11,-17,-17,-8,1,18,2,-4,15,2,-4,11,-17,0,-9,21,-9,14,9,-16,15,6,-19,29,14,16,-11,-20,-14,-4,0,-13,13,-19,19,-19,-1,14,-12,-7,21,15,-14,21,10,-14,-18,-19,8,17,13,-3,-14,-11,25,-20,1,-11,-18,-15,-15,-19,27,22,-8,18,24,-11,-8,-20,-12,-17,23,-7,23,18,20],[0,24,-1,5,-12,-18,-7,25,7,6,-8,26,-18,12,-12,16,9,-10,20,-3,-5,8,-16,21,5,-17,-11,-6,-5,16,4,13,5,-3,-5,-12,-20,-3,5,15,-17,-9,11,-9,18,11,23,-18,3,18,26,-5,20,8,-20,-12,-10,-13,-18,12,-3,-2,-1,-8,-17,24,-9,-17,-11,-16,-5,2,-9,23,-14,13,16,-1,10,3,27,-20,20,-10,22,-11,23,-9,4,7,-16,-11,-11,1,5,13,24,22,-7,-11],[14,-4,11,-10,18,-12,-8,17,-3,-2,-3,3,14,25,-2,21,7,-6,27,18,14,12,-20,24,-19,-2,2,0,-3,6,1,-13,-19,0,29,19,5,-13,27,11,14,-10,-14,-9,-5,13,18,15,5,-7,20,-7,5,-4,-10,-15,8,-20,24,-16,4,-1,-15,-18,7,22,-3,28,1,29,-2,23,19,-1,-10,1,1,0,26,-15,18,18,12,24,6,-14,-19,-4,28,-11,19,-5,10,3,-5,-4,-2,-17,6,-20],[-19,2,15,19,-8,11,-9,-5,-7,-15,13,13,23,0,13,29,1,-16,3,-4,27,5,18,-16,1,16,15,19,-15,0,16,23,6,26,-14,16,-14,-7,16,-4,1,-3,19,18,20,8,16,-13,1,21,5,-17,27,0,13,-9,-11,-3,28,-15,23,-15,0,27,-1,10,17,21,29,4,-5,26,0,9,17,24,18,10,25,17,-11,-10,-14,-15,7,2,-14,6,-9,17,12,22,23,27,-16,-6,-13,11,-20,25],[-12,17,23,-8,-14,-13,14,21,1,1,16,12,2,27,-10,-11,23,-9,11,-10,18,22,-17,17,20,-8,5,16,-9,-2,-19,3,22,28,-8,12,13,29,-20,4,24,22,25,28,25,-3,16,-17,22,7,16,25,0,-9,1,26,9,-5,19,20,19,-17,7,6,-4,-15,-6,-4,26,-9,1,-9,16,5,-8,29,11,12,6,-12,-10,-4,7,-8,29,-7,28,-11,-9,7,-3,-15,6,7,26,-17,-15,-9,21,-17],[10,23,-3,-2,-2,-1,3,28,7,9,23,2,-16,-12,26,-3,-14,12,24,-16,-12,-2,7,-3,9,-13,-11,21,17,-1,12,-7,9,-7,-14,28,15,27,26,-20,14,5,7,-15,25,9,-20,-4,25,-7,-17,8,-17,15,-16,-8,25,23,-1,11,-1,4,-11,-14,21,22,-16,25,-14,25,-20,22,9,10,18,6,18,5,4,16,-9,7,-6,-1,-3,-18,-6,9,-5,22,-14,-5,-11,10,23,21,23,15,-9,-1],[4,6,-19,28,-4,-19,-4,17,-4,-8,22,19,-13,22,-20,7,11,-14,8,26,-4,20,18,21,27,5,3,-18,-8,-15,-12,29,19,-4,-5,-8,12,1,15,26,16,9,19,-11,6,-1,1,-9,12,24,-14,3,17,18,-10,21,-16,19,11,-15,22,10,5,-1,2,16,2,14,-8,-18,11,6,-9,9,13,28,-1,28,26,-8,-7,-12,28,25,2,-12,-19,14,-1,24,19,-15,4,-7,6,-2,-13,29,0,26]]

K = 45000

print(s.maxSumSubmatrix(A, K))
print(time.time() - t0)