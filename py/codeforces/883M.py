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
created by shhuan at 2017/10/22 12:19

"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print(2*(2+max(abs(x1-x2), 1)+max(abs(y1-y2), 1)))