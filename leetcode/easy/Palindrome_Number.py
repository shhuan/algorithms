# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 17:36

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @return a boolean
    def isPalindrome(self, x):

        if x < 0:
            return False

        # Your runtime beats 87.42% of python submissions.
        #
        # x = str(x)
        # N = len(x)
        # for i in range(N//2):
        #     if x[i] != x[N-1-i]:
        #         return False
        #
        # return True

        if x != 0 and x % 10 == 0:
            return False

        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x*10 == y











s = Solution()
print(s.isPalindrome(11))
print(s.isPalindrome(-2147483648))
print(s.isPalindrome(12321))
print(s.isPalindrome(12212))
print(s.isPalindrome(0))
print(s.isPalindrome(10))