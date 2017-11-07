# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/16 08:46

"""

s = []


def xorshift128plus():
    global s
    x, y = s
    x ^= (x << 23) & (2 ** 64 - 1)
    s[0] = y
    s[1] = x ^ y ^ (x >> 17) ^ (y >> 26)
    return y


def solve(C, H, N):
    ans = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, N-1):
        ans[0][i] = 1
        ans[i][0] = 1
    minCost = float('inf')
    for epoch in range(10):
        A = collections.defaultdict(list)
        # A[0] = [i for i in range(1, N)]
        # for i in range(1, N):
        #     A[i] = [0]
        #
        # cost = sum([C[0][i] for i in range(1, N)])
        # cost += H[0][N-1]
        # cost += sum([H[i][1] for i in range(1, N)])

        used = {random.randint(0, N-1)}
        notused = {i for i in range(N)} - used

        while len(used) < N:
            u = list(used)[random.randint(0, len(used)-1)]
            v = list(notused)[random.randint(0, len(notused)-1)]
            A[u].append(v)
            A[v].append(u)
            used.add(v)
            notused.remove(v)
        cost = 0
        hub = 0
        for u, vs in A.items():
            hub += H[u][len(vs)]
            for v in vs:
                cost += C[u][v]
        cost = cost//2+hub

        steps = 0
        while steps < 10000:
            steps += 1
            u = random.randint(0, N-1)

            found = False
            for v in [v for v in A[u]]:
                if found:
                    break
                steps += 1
                if len(A[v]) > 1:
                    for w in [w for w in A[v]]:
                        if len(A[w]) >= N-1:
                            continue
                        steps += 1
                        if w != u:
                            c = cost
                            c -= C[u][v]
                            c += C[u][w]
                            c -= H[v][len(A[v])]
                            c += H[v][len(A[v]) - 1]
                            c -= H[w][len(A[w])]
                            c += H[w][len(A[w]) + 1]
                            if c < cost:
                                # print((u, v), ' => ', (u, w), cost, ' -> ', c)
                                cost = c
                                A[u].remove(v)
                                A[v].remove(u)
                                A[u].append(w)
                                A[w].append(u)
                                found = True
                                break
        if cost < minCost:
            minCost = cost
            ans = [[0 for _ in range(N)] for _ in range(N)]
            for u, vs in A.items():
                for v in vs:
                    ans[u][v] = 1
                    ans[v][u] = 1
    # print(minCost)
    return ans


def main():
    global s
    T = int(input())
    # T = 1000
    for t in range(T):
        n, Cmax, Hmax = map(int, input().split())
        # n, Cmax, Hmax =t+1, 1000000, 1000000
        C = [[0] * n for x in range(n)]
        for i in range(n):
            s = list(map(int, input().split()))
            # s = [random.randint(0, 2**18), random.randint(0, 2**18)]
            for j in range(i + 1, n):
                C[i][j] = C[j][i] = xorshift128plus() % (Cmax + 1)

        H = [[0] * n for x in range(n)]
        for i in range(n):
            s = list(map(int, input().split()))
            # s = [random.randint(2 ** 11, 2 ** 12), random.randint(2 ** 11, 2 ** 12)]
            for j in range(n):
                H[i][j] = xorshift128plus() % (Hmax + 1)

        # print("==============C==================")
        # for row in C:
        #     print(row)
        # print("=============H===================")
        # for row in H:
        #     print(row)
        # print("================================")
        # solve here
        # print(n, s)
        ans = solve(C, H, n)
        for row in ans:
            print(''.join(map(str, row)))



if __name__ == "__main__":
    main()
