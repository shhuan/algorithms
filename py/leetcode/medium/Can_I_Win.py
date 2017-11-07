# -*- coding: utf-8 -*-
"""


In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

"""

import time

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        if desiredTotal > maxChoosableInteger*(maxChoosableInteger+1) // 2:
            return False

        t = desiredTotal
        memo = {}

        def dfs(digits, target):
            if digits == 0:
                return False

            key = (digits, target)
            if key in memo:
                return memo[key]

            if target <= maxChoosableInteger:
                for i in range(maxChoosableInteger-1, target-2, -1):
                    if digits & (1 << i):
                        memo[key] = True
                        return True

            for i in range(maxChoosableInteger):
                if digits & (1 << i):
                    if not dfs(digits ^ (1 << i), target - i - 1):
                        memo[key] = True
                        return True

            memo[key] = False
            return False

        d = 0
        for i in range(maxChoosableInteger):
            d |= 1 << i

        return dfs(d, t)

s = Solution()
t0 = time.time()
print(s.canIWin(5, 14))
print(time.time() - t0)