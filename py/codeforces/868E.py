# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 17:32

"""

N = int(input())

NN = N+1
G = [[float('inf') for _ in range(NN)] for _ in range(NN)]
GG = collections.defaultdict(list)
for i in range(N-1):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w
    GG[u].append((v, w))
    GG[v].append((u, w))

S = int(input())
M = int(input())

T = [int(x) for x in input().split()]

D = [[G[r][c] for c in range(NN)] for r in range(NN)]

for k in range(1, NN):
    for i in range(1, NN):
        for j in range(1, NN):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

def dfs(t, s, c):

    t = [x for x in t if x!=s]
    for v, w in GG[s]:
        # s->v
        # bloc v->s
        # go to farthest location away v
        wvs = G[v][s]
        G[v][s] = float('inf')

        # for each leaf from v
        nodes = [(x, G[v][x]) for x in range(1, NN) if G[v][x] < float('inf')]
        visited = set([x[0] for x in nodes])
        leafs = []
        poorCriminals = []
        while nodes:
            next_nodes = []
            for node, distance in nodes:
                if node in t:
                    poorCriminals.append(node)
                children = [(x, distance+G[node][x]) for x in range(1, NN) if G[node][x] < float('inf')]
                children = [x for x in children if x[0] not in visited]
                if not children:
                    leafs.append((node, distance))
                else:
                    next_nodes.extend(children)
            nodes = next_nodes

        luckyCriminals = [x for x in t if x not in poorCriminals]
        # for criminal in poorCriminals:






q = [(T, S, 0)]
while q:
    t, s, c = q.pop(0)

    for v, w in GG[s]:






