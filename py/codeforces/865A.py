# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 18:13


输入A，输出
N M
D1,D2,...,DM

使用M个面值为D1,...,DM的硬币组合成总价值N的方法的数量是A

只使用1，2两种面值，生成2*A-1的方法数量是A。
因为可以使用0到A-1个2，剩下的都使用1

"""

A = int(input())

print(2*A-1, 2)
print(1, 2)