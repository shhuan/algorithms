# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
# import matplotlib.pyplot as plt
"""
created by shhuan at 2017/11/4 01:33

"""

x1, y1, x2, y2 = map(int, input().split())

n = int(input())

C = []
for i in range(n):
    C.append([int(x) for x in input().split()])


def check(X, Y, R):
    for x, y, r in C:
        d = math.sqrt((X-x)**2 + (Y-y)**2)
        if abs(R-r) < d - 1e-5 and d + 1e-5 < R+r:
            return False, (x, y, r)

    return True, None


def check2(c1, c2):
    if not c2:
        return True
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = math.sqrt((x1-x2)**2 +(y1-y2)**2)
    return not (abs(r1-r2) < d < r1+r2)


hi = 10**12
lo = 0
L = math.sqrt((x1-x2)**2 + (y1-y2)**2) / 2
L2 = L**2
xm, ym = (x1+x2)/2, (y1+y2)/2
xm2, ym2 = xm**2, ym**2
vectv = x2-x1, y2-y1
dy, dx = y2-y1, x2-x1
c = dy/dx
c2 = c**2
c21 = c2+1
d = c*ym + xm
e = d - xm
e2 = e**2
f = (e*c+ym)/c21
f2 = f**2
rd = L2+ym2+e2


def cal(R):
    g = (R ** 2 - rd) / c21 + f2
    if abs(g) < 1e-6:
        g = 0

    if g < 0:
        return []

    Y = math.sqrt(g)
    Y1 = Y + f
    Y2 = -Y + f
    X1 = -c * Y1 + d
    X2 = -c * Y2 + d
    return [(X1, Y1), (X2, Y2)]


R = L
while True:
    XY = cal(R)
    X1, Y1 = XY[0]

    u1, c1 = check(X1, Y1, R)
    if u1:
        break

    lo = R
    hi = 1e12
    while abs(lo-hi) > 1e-6:
        r = lo + (hi-lo) / 2
        xy = cal(r)
        X1, Y1 = xy[0]
        if check2((X1, Y1, r), c1):
            hi = r
        else:
            lo = r
    if abs(R-lo) < 1e-6:
        break
    R = lo

ans = R

R = L
while True:
    XY = cal(R)
    X2, Y2 = XY[1]
    u2, c2 = check(X2, Y2, R)
    if u2:
        break

    lo = R
    hi = 1e12
    while abs(lo-hi) > 1e-6:
        r = lo + (hi-lo) / 2
        xy = cal(r)
        X2, Y2 = xy[1]
        if check2((X2, Y2, r), c2):
            hi = r
        else:
            lo = r
    if abs(R-lo) < 1e-6:
        break
    R = lo

ans = min(ans, R)
R = ans
print(ans)

# XY = cal(ans)
#
# plt.figure()
# fig, ax = plt.subplots()
# circles = []
# xs = [x for x, _, _ in C]
# ys = [y for _, y, _ in C]
# xlim = [min(xs), max(xs)]
# ylim = [min(ys), max(ys)]
# ll, lr = min(xlim[0], ylim[0])-R, max(xlim[1], ylim[1])+R
# ax.set_xlim([ll, lr])
# ax.set_ylim([ll, lr])
#
# for x, y, r in C:
#     circles.append(plt.Circle((x, y), r, color='b'))
#
#
# plt.plot([x1, x2], [y1, y2])
#
# circles.append(plt.Circle(XY[0], R, color='r'))
# circles.append(plt.Circle(XY[1], R, color='r'))
# for c in circles:
#     ax.add_artist(c)
#     c.set_clip_box(ax.bbox)
#     c.set_facecolor("none")  # "none" not None
#
# plt.show()








