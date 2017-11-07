# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 08:40

"""

N = int(input())
A = [int(x) for x in input().split()]

if N%2==0:
    print("No")
else:
    if A[0]%2!=0 and A[-1]%2!=0:
        print('Yes')
    else:
        print('No')