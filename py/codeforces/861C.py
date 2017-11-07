# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 10:54

"""

s = input()

ans = ""

VOL = {'a', 'e', 'i', 'o', 'u'}
i = 0
while i < len(s):
    v = s[i]
    if v not in VOL:
        j = i + 1
        while j < len(s) and s[j] not in VOL:
            j += 1

        t = s[i:j]
        if len(set(t)) == 1:
            ans += t
        else:
            c = 0
            for k in range(i, j):
                ans += s[k]
                c += 1
                if s[k] != s[k-1] and c >= 2:
                    if c > 2:
                        ans = ans[:-1]
                        ans += ' '
                        ans += s[k]
                        c = 1
                    else:
                        if k != j-1:
                            ans += ' '
                        c = 0
        i = j - 1
    else:
        ans += v
    i += 1

print(ans)
