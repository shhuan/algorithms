# -*- coding: utf-8 -*-
"""
created by huash at 2016/6/18 19:56

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?'


"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        return [self.numOfOne(x) for x in range(num + 1)]

    def numOfOne(self, num):
        count = 0
        while num > 0:
            count += 1
            num &= num - 1

        return count

    def countBits2(self, num):

        c = [0 for x in range(num+1)]
        c[1] = 1

        i = 2
        while i <= num:
            c[i] = 1
            i <<= 1

        for i in range(num+1):
            b = 1
            j = i
            while j > 0:
                j >>= 1
                b <<= 1
            if i | b > num:
                break
            c[i | b] = c[i] + 1
        return c

def test(f):
    t0 = datetime.datetime.now()
    for i in range(3000):
        f(i)
    print("{} cost: {}".format(f.func_name, datetime.datetime.now() - t0))
s = Solution()
test(s.countBits)

print(s.countBits2(5))