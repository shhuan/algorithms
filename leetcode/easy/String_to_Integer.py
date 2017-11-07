# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 16:04

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.



Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes an optional
initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.


The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0

        i = 0
        while i < len(str):
            if str[i] != ' ':
                break
            i += 1
        if i >= len(str):
            return 0

        val_str = str[i:]
        negative = False
        if val_str[0] == '-':
            negative = True
            val_str = val_str[1:]
        elif val_str[0] == '+':
            val_str = val_str[1:]

        result = 0
        for ch in val_str:
            if ord(ch) not in range(ord('0'), ord('9')+1):
                if negative:
                    return -result
                return result

            if result <= (2147483647-int(ch)) // 10:
                result *= 10
                result += int(ch)
            else:
                if not negative:
                    return 2147483647
                else:
                    return -2147483648
        if negative:
            return -result
        return result


s = Solution()
print(s.atoi('-2147483649'))
print(s.atoi('1221   122222222'))
print(s.atoi('  -0012a42'))
print(s.atoi('   +0 123'))
