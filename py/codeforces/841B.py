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
created by shhuan at 2017/10/21 12:16

"""

N = int(input())

A = [int(x) for x in input().split()]

S = sum(A)

if S%2 != 0:
    print("First")
else:
    for a in A:
        if a%2==1:
            print("First")
            exit(0)

    print("Second")

