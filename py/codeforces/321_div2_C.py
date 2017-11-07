# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-15 09:21



注意可能从A->B->C，其中A>B, B<C，即先增大后减小或者反之。
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections
import random

# sys.stdout = open("input.txt", "w")
# def generateCase():
# print(100)
#     for i in range(100):
#         n = random.randint(1000, 100000)
#         print(n)
#         line = []
#         for j in range(n):
#             line.append(random.randint(1, 1000000))
#         print(' '.join(map(str, line)))
#
# generateCase()
# sys.exit(0)


def solve():
    N = int(input())
    chemicals = [int(x) for x in input().split()]
    # possibleVolumes = set()

    steps = collections.defaultdict(int)
    maxV = 100001
    matchTimes = [0 for x in range(maxV + 1)]
    # maxV = int(math.pow(2, 2*int(math.log(maxV, 2))))
    # maxV = 1 << 60
    for v in chemicals:
        vsteps = {v: 0}
        q = [(v, 0)]
        while q:
            tv, step = q.pop()
            dtv = tv * 2
            if dtv < maxV:
                if dtv not in vsteps or step + 1 < vsteps[dtv]:
                    vsteps[dtv] = step + 1
                    q.append((dtv, step + 1))
            htv = tv // 2
            if htv >= 1:
                if htv not in vsteps or step + 1 < vsteps[htv]:
                    vsteps[htv] = step + 1
                    q.append((htv, step + 1))

        for tv, step in vsteps.items():
            steps[tv] += step
            matchTimes[tv] += 1

            # if not possibleVolumes:
            #     possibleVolumes = set(vsteps.keys())
            # else:
            #     possibleVolumes &= set(vsteps.keys())

    # print(sorted(steps.items()))
    # print(possibleVolumes)
    res = 100000000
    target = 0
    for i in range(1, maxV):
        # res = min(res, steps[v])
        if matchTimes[i] == N and res > steps[i]:
            res = steps[i]
            target = i

    # print('{}, {}'.format(res, target))
    print(res)


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
caseCount = int(input())
for ci in range(caseCount):
    startTime = datetime.datetime.now()
    solve()
    sys.stderr.write('{}\r\n'.format(datetime.datetime.now() - startTime))

solve()