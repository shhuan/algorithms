# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 17:24

"""

ax, ay, bx, by, cx, cy = map(int, input().split())

#(x2-x1)×(y3-y2)=(x3-x2)×(y2-y1)

if (bx-ax)*(cy-by) == (cx-bx)*(by-ay) or (by-ay)**2+(bx-ax)**2 != (cy-by)**2+(cx-bx)**2:
    print('No')
else:
    print('Yes')