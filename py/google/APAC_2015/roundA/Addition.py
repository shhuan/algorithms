# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-06 19:48

已知一些等式x+y=z，求给表达式a+b的值


由表达式a+b=v1, b+c=v2 可以推出a+(-c) = v1-v2，
就是说两个表达式之间至少有一个未知数一样，他们可以关联起来

"""
__author__ = 'huash'

import sys
import os
import re
sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/C-small-practice.in', 'r')
sys.stdout = open('output/C-small-practice.out', 'w')


def normalize(exp):
    if exp is None or len(exp) != 4:
        return None

    if exp[0] < exp[2]:
        return exp
    else:
        if exp[1] == '+':
            return exp[2], exp[1], exp[0], exp[3]
        else:
            return exp[2], exp[1], exp[0], str(0-int(exp[3]))


def solve(AT, exps):
    A = {AT.pop()}
    D = set()
    DT = set()

    while True:
        if len(AT) <= 0 and len(DT) <= 0:
            break
        while len(AT) > 0:
            e1 = AT.pop()
            if e1 not in A:
                for e2 in A:
                    if e1[0] == e2[0]:
                        # print('{} {} ==> {}-{}={}'.format(e1, e2, e1[1], e2[1], int(e1[2])-int(e2[2])))
                        DT.add((e1[1], e2[1], int(e1[2])-int(e2[2])))
                    elif e1[0] == e2[1]:
                        # print('{} {} ==> {}-{}={}'.format(e1, e2, e1[1], e2[0], int(e1[2])-int(e2[2])))
                        DT.add((e1[1], e2[0], int(e1[2])-int(e2[2])))
                    elif e1[1] == e2[0]:
                        # print('{} {} ==> {}-{}={}'.format(e1, e2, e1[0], e2[1], int(e1[2])-int(e2[2])))
                        DT.add((e1[0], e2[1], int(e1[2])-int(e2[2])))
                    elif e1[1] == e2[1]:
                        # print('{} {} ==> {}-{}={}'.format(e1, e2, e1[0], e2[0], int(e1[2])-int(e2[2])))
                        DT.add((e1[0], e2[0], int(e1[2])-int(e2[2])))
                A.add(e1)
        while len(DT) > 0:
            ed = DT.pop()
            if ed not in D:
                for ea in A:
                    if ed[1] == ea[0]:
                        # print('{} {} ==> {}+{}={}'.format(ed, ea, ed[0], ea[0], int(ea[2])+int(ed[2])))
                        AT.add((ed[0], ea[1], int(ea[2])+int(ed[2])))
                    elif ed[1] == ea[1]:
                        # print('{} {} ==> {}+{}={}'.format(ed, ea, ed[0], ea[1], int(ea[2])+int(ed[2])))
                        AT.add((ed[0], ea[0], int(ea[2])+int(ed[2])))
                    elif ed[0] == ea[0]:
                        AT.add((ed[1], ea[1], int(ea[2])-int(ed[2])))
                    elif ed[0] == ea[1]:
                        AT.add((ed[1], ea[0], int(ea[2])-int(ed[2])))
                for d in D:
                    if ed[1] == d[1]:
                        DT.add((ed[0], d[0], int(ed[2])-int(d[2])))
                    elif ed[1] == d[0]:
                        DT.add((ed[0], d[1], int(ed[2])+int(d[2])))
                    elif ed[0] == d[0]:
                        DT.add((ed[1], d[1], int(d[2])-int(ed[2])))
                    elif ed[0] == d[1]:
                        DT.add((d[0], ed[1], int(d[2])+int(ed[2])))
                D.add(ed)

    # print('======================')
    # print(A)
    # print('======================')
    result = dict()
    for exp in exps:
        for e in A:
            if e[:2] == exp or e[-2:-4:-1] == exp:
                result[exp] = e[2]
            # # print('{}+{}={}'.format(e[0], e[1], e[2]))
    for exp in exps:
        if exp in result.keys():
            print('{}+{}={}'.format(exp[0], exp[1], result[exp]))
        # else:
        #     print('{}+{}=Unknown'.format(exp[0], exp[1]))


T = int(input())
for ti in range(1, T+1):
    # print('Case #{}:'.format(ti))
    N = int(input())
    exps = set()
    for i in range(N):
        exp = re.split(r'[+=]', input())
        exps.add((exp[0], exp[1], exp[2]))

    Q = int(input())

    queries = list()
    for qi in range(Q):
        exp = sys.stdin.readline().strip().split('+')
        queries.append((exp[0], exp[1]))

    print('Case #{}:'.format(ti))

    solve(exps, queries)


    # for q in queries:
    #     for exp in exps:
    #         if (exp[1] == '+' and exp[0] == q[0] and exp[2] == q[2]) or \
    #                 (exp[1] == '+' and exp[0] == q[2] and exp[2] == q[0]):
    #             # print('{}+{}={}'.format(q[0], q[2], int(exp[3])))
    #             break







