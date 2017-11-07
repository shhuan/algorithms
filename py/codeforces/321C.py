"""

created by huash06 at 2015-07-14

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools
import math

N = int(input())
A = [int(x) for x in input().split()]

l = int(math.pow(2, math.log2(min(A))))

res = 0

# for t in range(1, max(A)+1):
