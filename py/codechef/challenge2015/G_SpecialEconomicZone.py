# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-12 09:06
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# sys.stdin = open('input/sampleG.txt', 'r')
# sys.stdin = open('input/B-small-practice.in', 'r')
# sys.stdout = open('output/B-small-practice.out', 'w')




N, M = list(map(int, input().split()))
Links = collections.defaultdict(list)
economic = set()
neighbors = set()

def canEco(city):
    return len(list(filter(lambda x: x in economic, Links[city]))) == 0
def dfs(links, visited):
    if not links:
        return 0
    for k, v in links.items():
        if canEco(city):
            economic.add(city)

            economic.remove(city)




for i in range(M):
    a, b = list(map(int, input().split()))
    Links[a].append(b)
    Links[b].append(a)





# for city in range(1, N+1):
#     if len(Links[city]) <= 1:
#         economic.add(city)
#         # for i in Links[city]:
#         #     neighbors.add(i)
#         # dfs(city, True, set())
# for city in economic.copy():
#     dfs(city, True, set())
for city in economic:
    for i in Links[city]:
        neighbors.add(i)

# print(economic)
# print(neighbors)
print(len(economic) - len(neighbors))