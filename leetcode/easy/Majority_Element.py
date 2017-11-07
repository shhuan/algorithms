# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 08:06
"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):

        result = num[0]
        count = 1
        for i in range(1, len(num)):
            v = num[i]
            if v == result:
                count += 1
            elif count == 0:
                count += 1
                result = v
            else:
                count -= 1
        return result




s = Solution()
# print(s.majorityElement([1,1,1,1,1,2,3,4,5]))
#
# print(s.majorityElement([2,1,3,2,2]))
print(s.majorityElement([6,6,6,7,7]))