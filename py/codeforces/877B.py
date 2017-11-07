# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/10/30 11:20

"""


S = input()
N = len(S)

dp = [[0 for _ in range(5)] for _ in range((N+1))]

for i in range(1, N+1):
    a = 1 if S[i-1] == 'a' else 0
    b = 1 - a
    dp[i][0] = dp[i-1][0] + a # only a
    dp[i][1] = dp[i-1][1] + b # only b
    dp[i][2] = max(dp[i-1][2], dp[i-1][0]) + b # a*b*
    dp[i][3] = max(dp[i-1][1], dp[i-1][3]) + a # b*a*
    dp[i][4] = max(dp[i-1][4], dp[i-1][2]) + a # a*b*a*

print(max(dp[N]))