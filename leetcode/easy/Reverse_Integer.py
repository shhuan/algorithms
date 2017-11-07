# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 10:07

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.

"""
__author__ = 'huash'

import sys
import os


class Solution:
    # @return an integer
    def reverse(self, x):
        negative = False if x > 0 else True
        x = -x if negative else x
        result = 0

        while x > 0:
            if result > 214748364:
                return 0
            result = result*10 + x % 10
            x //= 10

        return result if not negative else -result


    def reverse2(self, x):
        x = str(x)
        negative = True if x[0] == '-' else False
        x = x[1:] if negative else x
        x = int(''.join(reversed(x)))

        if x > 2147483647:
            return 0

        return x if not negative else -x


s = Solution()
print(s.reverse(123))
print(s.reverse(-231))
print(s.reverse(1000000003))
print(s.reverse(100))
print(s.reverse(1534236469))
print(s.reverse(-2147483412))
print(s.reverse(1563847412))