# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/7 16:52

"""

a = [int(x) for x in input().split()]

print(sum(a[:3])**2-a[0]**2-a[2]**2-a[4]**2)

