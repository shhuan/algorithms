# -*- coding: utf-8 -*-

"""
C. Vasya and String
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
High school student Vasya got a string of length n as a birthday present. This string consists of letters 'a' and 'b' only. Vasya denotes beauty of the string as the maximum length of a substring (consecutive subsequence) consisting of equal letters.

Vasya can change no more than k characters of the original string. What is the maximum beauty of the string he can achieve?

Input
The first line of the input contains two integers n and k (1 ≤ n ≤ 100 000, 0 ≤ k ≤ n) — the length of the string and the maximum number of characters to change.

The second line contains the string, consisting of letters 'a' and 'b' only.

Output
Print the only integer — the maximum beauty of the string Vasya can achieve by changing no more than k characters.

Examples
input
4 2
abba
output
4
input
8 1
aabaabaa
output
5
Note
In the first sample, Vasya can obtain both strings "aaaa" and "bbbb".

In the second sample, the optimal answer is obtained with the string "aaaaabaa" or with the string "aabaaaaa".

"""

import os
import sys
import functools
import collections
import itertools
import math

N, K = [int(x) for x in raw_input().split()]
S = raw_input()

def find(N, K, S, ch):
    if not S:
        return 0
    if K >= N:
        return N

    crange = [0, 0]
    result = 0
    for i, v in enumerate(S):
        if v == ch:
            crange[1] += 1
        else:
            if K > 0:
                crange[1] += 1
                K -= 1
            else:
                j = crange[0]
                while S[j] == ch:
                    j += 1
                if j < crange[1]:
                    crange[0] = j + 1
                    crange[1] += 1
                else:
                    crange[0] = j
                    crange[1] += 1
        # print crange
        result = max(result, crange[1] - crange[0])
    return result

print max(find(N, K, S, 'a'), find(N, K, S, 'b'))