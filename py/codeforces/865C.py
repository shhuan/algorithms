# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 11:55

C. Gotta Go Fast
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You're trying to set the record on your favorite video game. The game consists of N levels, which must be completed sequentially in order to beat the game. You usually complete each level as fast as possible, but sometimes finish a level slower. Specifically, you will complete the i-th level in either Fi seconds or Si seconds, where Fi < Si, and there's a Pi percent chance of completing it in Fi seconds. After completing a level, you may decide to either continue the game and play the next level, or reset the game and start again from the first level. Both the decision and the action are instant.

Your goal is to complete all the levels sequentially in at most R total seconds. You want to minimize the expected amount of time playing before achieving that goal. If you continue and reset optimally, how much total time can you expect to spend playing?

Input
The first line of input contains integers N and R , the number of levels and number of seconds you want to complete the game in, respectively. N lines follow. The ith such line contains integers Fi, Si, Pi (1 ≤ Fi < Si ≤ 100, 80 ≤ Pi ≤ 99), the fast time for level i, the slow time for level i, and the probability (as a percentage) of completing level i with the fast time.

Output
Print the total expected time. Your answer must be correct within an absolute or relative error of 10 - 9.

Formally, let your answer be a, and the jury's answer be b. Your answer will be considered correct, if .

Examples
input
1 8
2 8 81
output
3.14

input
2 30
20 30 80
3 9 85
output
31.4


(0.2+0.2**2+...+0.2**k)*30+20+0.15*9+0.83*3
= 0.2*(1-0.2**N)/(1-0.2)*30+...
= 0.25*30




input
4 319
63 79 89
79 97 91
75 87 88
75 90 83
output
314.159265358
Note
In the first example, you never need to reset. There's an 81% chance of completing the level in 2 seconds and a 19% chance of needing 8 seconds, both of which are within the goal time. The expected time is 0.81·2 + 0.19·8 = 3.14.

In the second example, you should reset after the first level if you complete it slowly. On average it will take 0.25 slow attempts before your first fast attempt. Then it doesn't matter whether you complete the second level fast or slow. The expected time is 0.25·30 + 20 + 0.85·3 + 0.15·9 = 31.4.


"""


# N, R = map(int, input().split())
# levels = []
# for i in range(N):
#     levels.append([int(x) for x in input().split()])

N, R = 50, 5000
levels = [(99, 100, 80) for _ in range(N)]

t0 = time.time()

F = [x[0] for x in levels]
S = [x[1] for x in levels]
P = [1.0*x[2]/100.0 for x in levels]

lo = 0.0
hi = 1e10
for p in range(1200):
    t1 = time.time()
    ans = (lo+hi)/2
    # EXP[j][i]，用时i完成关卡j，所需要的总时间的期望值
    EXP = [[0.0 for _ in range(R+1)] for _ in range(N+1)]

    # 倒推
    for j in range(N-1, -1, -1):
        for i in range(R+1):
            if i+F[j] <= R:
                # i+F[i]完成第j+1关，完成第j关花费时间F[j]
                play = (F[j]+EXP[j+1][i+F[j]]) * P[j]
                if i+S[j] <= R:
                    # 龟速通关第j关，且不超时
                    play += (S[j]+EXP[j+1][i+S[j]]) * (1-P[j])
                else:
                    # 龟速通过第j关，超时了，重启游戏
                    play += (S[j]+ans) * (1-P[j])
                EXP[j][i] = min(play, ans)
            else:
                EXP[j][i] = ans
    if EXP[0][0] < ans:
        hi = ans
    else:
        lo = ans
    print(time.time()-t1)
    if hi-lo < 1e-9:
        break
print(lo, hi)

print(time.time() - t0)