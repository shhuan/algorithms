# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 09:16

"""

K = int(input())

ans = ""
for i in range(26):
    cnt = 1
    while (cnt+1)*cnt//2 <= K:
        cnt += 1
    K -= cnt*(cnt-1)//2
    ans += chr(ord('a')+i)*cnt

print(ans)
