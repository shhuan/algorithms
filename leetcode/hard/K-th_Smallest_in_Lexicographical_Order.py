# -*- coding: utf-8 -*-
"""

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.



denary tree


先序遍历10叉树，计算遍历过的数字的数量。

数字i的子树范围是[i*10, (i+1)*10), [i*100, (i+1)*100),...
1. 如果i和i的子树中的数字个数<K，增加i。
2. 否则查看i的第1个子树的数字个数是否<K-1(因为数字i也在前k个数字之中)，转1，否者继续执行步骤2



"""

import math

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """



        cur = 1
        k -= 1
        while k > 0:
            step, first, last = 0, cur, cur+1
            while first <= n:
                step += min(n+1, last) - first
                first *= 10
                last *= 10
            if step <= k:
                k -= step
                cur += 1
            else:
                cur *= 10
                k -= 1

        return cur



s = Solution()
for i in range(1, 10):
    print(s.findKthNumber(10, i))
print(s.findKthNumber(10, 3))