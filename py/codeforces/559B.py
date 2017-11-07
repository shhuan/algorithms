# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/7 17:04


 Two strings a and b of equal length are called equivalent in one of the two cases:

They are equal.
If we split string a into two halves of the same size a1 and a2, and string b into two halves of the same size b1 and b2,
then one of the following is correct:
a1 is equivalent to b1, and a2 is equivalent to b2
a1 is equivalent to b2, and a2 is equivalent to b1




Let us note that "equivalence" described in the statements is actually equivalence relation, 
it is reflexively, simmetrically and transitive. 
It is meant that set of all string is splits to equivalence classes. Let's find lexicographic minimal strings 
what is equivalent to first and to second given string. And then check if its are equals.

"""

a = input()
b = input()

def smallest(s):
    n = len(s)

    if n % 2 == 1:
        return s

    s1 = smallest(s[:n//2])
    s2 = smallest(s[n//2:])

    if s1 < s2:
        return s1+s2
    return s2+s1


a = smallest(a)
b = smallest(b)

if a == b:
    print('YES')
else:
    print('NO')