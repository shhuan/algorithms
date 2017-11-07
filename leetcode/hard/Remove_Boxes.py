# -*- coding: utf-8 -*-
"""


Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.

"""

import time

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        A = boxes
        N = len(A)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and A[m + 1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i + 1, j, 0) + (k + 1) ** 2
                for m in range(i + 1, j + 1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, N - 1, 0)


s = Solution()
print(s.removeBoxes([1,2,3,4,5,6,7,8,9,10]))

t0 = time.time()
print(s.removeBoxes([3, 8, 8, 5, 5, 3, 9, 2, 4, 4, 6, 5, 8, 4, 8, 6, 9, 6, 2, 8, 6, 4, 1, 9, 5, 3, 10, 5, 3, 3, 9, 8, 8, 6, 5, 3, 7, 4, 9, 6, 3, 9, 4, 3, 5, 10, 7, 6, 10, 7]))
print(time.time() - t0)