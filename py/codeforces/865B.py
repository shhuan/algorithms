# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
"""
created by shhuan at 2017/10/3 12:35

C. Ordering Pizza
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
It's another Start[c]up finals, and that means there is pizza to order for the onsite contestants. There are only 2 types of pizza (obviously not, but let's just pretend for the sake of the problem), and all pizzas contain exactly S slices.

It is known that the i-th contestant will eat si slices of pizza, and gain ai happiness for each slice of type 1 pizza they eat, and bi happiness for each slice of type 2 pizza they eat. We can order any number of type 1 and type 2 pizzas, but we want to buy the minimum possible number of pizzas for all of the contestants to be able to eat their required number of slices. Given that restriction, what is the maximum possible total happiness that can be achieved?

Input
The first line of input will contain integers N and S (1 ≤ N ≤ 105, 1 ≤ S ≤ 105), the number of contestants and the number of slices per pizza, respectively. N lines follow.

The i-th such line contains integers si, ai, and bi (1 ≤ si ≤ 105, 1 ≤ ai ≤ 105, 1 ≤ bi ≤ 105), the number of slices the i-th contestant will eat, the happiness they will gain from each type 1 slice they eat, and the happiness they will gain from each type 2 slice they eat, respectively.

Output
Print the maximum total happiness that can be achieved.

Examples
input
3 12
3 5 7
4 6 7
5 9 5
output
84
input
6 10
7 4 7
5 8 8
12 5 8
6 11 6
3 3 7
5 9 6
output
314
Note
In the first example, you only need to buy one pizza. If you buy a type 1 pizza, the total happiness will be 3·5 + 4·6 + 5·9 = 84, and if you buy a type 2 pizza, the total happiness will be 3·7 + 4·7 + 5·5 = 74.



先计算出需要买的披萨个数，等于所有人要吃的片数之和除以每个披萨的片数。
如果某个人吃第一种披萨幸福值更高，就尽量让他吃第一种，否则吃第二种。
如果第一种披萨不能满足所有更喜欢吃第一种披萨的人，那么优先满足吃第一种比吃第二种差值更大的人，所有先对差值排序。


"""

N, S = map(int, input().split())

M = []
for i in range(N):
    M.append([int(x) for x in input().split()])
#
# N, S = 100000, 100000
# M = [[random.randint(10000, 100000), random.randint(1, 100), random.randint(1, 100)] for _ in range(N)]
# t0 = time.time()

s = [M[i][0] for i in range(N)]
a = [M[i][1] for i in range(N)]
b = [M[i][2] for i in range(N)]

total = sum(s)
numpizza = int(math.ceil(total/S))
numslice = numpizza * S

sab = sorted([(a[i]-b[i], i) for i in range(N)], reverse=True)

pa = 0
pb = 0
pab = 0
maxHappiness = 0
for i in range(N):
    if a[i] > b[i]:
        pa += s[i]
    elif a[i] < b[i]:
        pb += s[i]
    else:
        pab += s[i]

sa = int(math.ceil(pa/S)) * S
sb = int(math.ceil(pb/S)) * S
pab -= sa+sb-pa-pb
pab = max(pab, 0)
if sa//S + sb//S + int(math.ceil(pab/S)) == numpizza:
    print(sum([s[i]*(a[i] if a[i] > b[i] else b[i]) for i in range(N)]))
    exit(0)



if pa == 0 and pb == 0:
    print(sum([s[i]*a[i] for i in range(N)] or [0]))
    exit(0)
if pa == 0:
    print(sum([s[i]*b[i] for i in range(N)] or [0]))
    exit(0)
if pb == 0:
    print(sum([s[i]*a[i] for i in range(N)] or [0]))
    exit(0)

# print(time.time()-t0)
sbak = s
for pza in range(pa//S, (pa+pab)//S+2):
    pzb = numpizza - pza

    aslice = pza*S
    bslice = pzb*S

    h = 0
    s = [x for x in sbak]
    for j in range(N):
        d, i = sab[j]
        if d > 0:
            if aslice >= s[i]:
                h += s[i]*a[i]
                aslice -= s[i]
                s[i] = 0
            elif aslice > 0:
                h += a[i]*aslice
                s[i] -= aslice
                aslice = 0
        else:
            break
    for j in range(N-1, -1, -1):
        d, i = sab[j]
        if d < 0:
            if bslice >= s[i]:
                h += s[i]*b[i]
                bslice -= s[i]
                s[i] = 0
            elif bslice > 0:
                h += bslice * b[i]
                s[i] -= bslice
                bslice = 0
        else:
            break

    if aslice == 0:
        for i in range(N):
            if s[i] != 0:
                h += s[i]*b[i]
                bslice -= s[i]
    elif bslice == 0:
        for i in range(N):
            if s[i] != 0:
                h += s[i]*a[i]
                aslice -= s[i]
    else:
        remain = [(s[i], a[i], b[i]) for i in range(N) if s[i] > 0 and a[i] != b[i]]
        for u,v,w in remain:
            if v > w:
                if aslice > 0:
                    if aslice > u:
                        h += u * v
                        aslice -= u
                    else:
                        h += aslice * v
                        h += (u-aslice) * w
                        bslice -= u-aslice
                        aslice = 0
                else:
                    h += u*w
                    bslice -= u

            else:
                if bslice > 0:
                    if bslice > u:
                        h += u * w
                        bslice -= u
                    else:
                        h += bslice * w
                        h += (u - bslice) * v
                        aslice -= u - bslice
                        bslice = 0
                else:
                    h += u*v
                    aslice -= u
        h += sum([s[i]*a[i] for i in range(N) if a[i] == b[i]] or [0])

    maxHappiness = max(maxHappiness, h)

print(maxHappiness)

# print(time.time() - t0 )