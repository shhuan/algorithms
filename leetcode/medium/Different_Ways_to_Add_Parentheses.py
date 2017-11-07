# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/3 18:22

Given a string of numbers and operators,
return all possible results from computing all the
different possible ways to group numbers and operators.

The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return 0
        if '+' not  in input\
            and '-' not in input\
            and '*' not in input:
            return [int(input)]
        result = []
        for ci, ch in enumerate(input):
            if ch in ['+', '-', '*']:
                lr = self.diffWaysToCompute(input[:ci])
                rr = self.diffWaysToCompute(input[ci+1:])
                for v1 in lr:
                    for v2 in rr:
                        if ch == '+':
                            result.append(v1 + v2)
                        elif ch == '-':
                            result.append(v1 - v2)
                        else:
                            result.append(v1 * v2)
        return result


s = Solution()
input = '2-1-1'
print(s.diffWaysToCompute(input))

input = "2*3-4*5"
print(s.diffWaysToCompute(input))