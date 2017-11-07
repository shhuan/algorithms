# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-08 19:19
"""
__author__ = 'huash'

import sys
import os
from functools import lru_cache


class Reader:
    def __init__(self, path=None):
        self.path = path
        self.index = -1
        self.data = []

    def next_int(self):
        self.index += 1
        if self.index < len(self.data):
            return int(self.data[self.index])
        else:
            return None

    def next_str(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        return None

    def read(self):
        self.data = list(self.read_impl())

    def read_impl(self):
        if self.path is not None:
            for line in open(self.path):
                for val in line.strip().split():
                    yield val
        else:
            for line in sys.stdin:
                for val in line.strip().split():
                    yield val


def getBit(num, i):
    return (num >> i) & 1  # Returns the i-th bit value of num.


@lru_cache(maxsize=None)
def count(i, lessM, M):
    """
    We will refer to the i-th bit as mi. Let’s say we have generated value 1 for m4,
    value 0 for m3, and we want to generate the feasible values for the bit at position i = 2.
    We can represent our current state as: 10cyy, where 1 and 0 are the values we have chosen,
    ‘c’ is the current (i-th) bit we want to generate and ‘y’ denotes the bits we will try to
    generate in the future. We call the bits to the left of position i as prefix. The prefix
    for the partially generated mi = 10cyy is 10 (where i = 2). Now we explain the rules which
    help us decide the feasible values to use for the i-th bit c:

    Rule 1: we can always use value 0 for bit at position i.
    We can use value 1 for bit at position i if either:
    Rule 2a: The prefix of the bits before position i in m (which is already generated) is
            less than the prefix of the bits before position i in M, or
    Rule 2b: The i-th bit of M is 1.
    :param i:
    :param lessM:
    :param M:
    :return:
    """
    if i == -1:  # The base case.
        return lessM  # only count if it is strictly less than M.

    maxM = lessM or getBit(M, i) == 1

    res = count(i - 1, maxM, M)  # Value 0 is always feasible. See (1) below.

    if maxM:  # Value 1 is feasible if maxM is true. See (2) below.
        res += count(i - 1, lessM, M)  # See (3) below.

    """
    (1): To compute the boolean value of lessM for the next bit of m in the recurrence,
        we look at the value of the current lessM. If the current lessM is already true,
        then lessM for the next bit in the recurrence will also be true. Another case when lessM for
        the next bit is true is when the i-th bit of M is equal to 1. Since we pick value 0 for the
        current (i-th) bit in m and it is less than the i-th bit of M (which is 1), it means that
        lessM is true for the next bit. maxM captures what we described just now, therefore the
        next value for lessM for the next bit in the recursion is set to maxM.
    (2): Value 1 is feasible if lessM is true (which means we are free to use both values 0 and 1)
        or the i-th bit of M is 1 (which means we are still generating feasible partial number m
        that is less than or equal to M).
    (3): The value for lessM in the next bit can only be true if lessM is previously true.
        If the current lessM is false, then we know that the i-th bit of M is 1.
        Since we picked value 1 for the current bit, the next value for lessM will not change
        (since 1 is not less than 1).
    """

    return res

# Prints how many non-negative numbers that are less than 123456789
# print(count(31, False, 123456789))


@lru_cache(maxsize=None)
def countPairs(i, lessA, lessB, lessK, A, B, K):
    if i == -1:  # The base case.
        return lessA and lessB and lessK  # Count those that are strictly less.

    maxA = lessA or getBit(A, i) == 1
    maxB = lessB or getBit(B, i) == 1
    maxK = lessK or getBit(K, i) == 1

    # Use value 0 for a, b, and k which is always possible. See (1).
    count = countPairs(i - 1, maxA, maxB, maxK, A, B, K)

    if maxA:  # Use value 1 for a, and 0 for b and k. See (2).
        count += countPairs(i - 1, lessA, maxB, maxK, A, B, K)

    if maxB:  # Use value 1 for b, and 0 for a and k. See (3)
        count += countPairs(i - 1, maxA, lessB, maxK, A, B, K)

    if maxA and maxB and maxK:  # Use value 1 for a, b, and k. See (4)
        count += countPairs(i - 1, lessA, lessB, lessK, A, B, K)
    """
    Notes:
    (1): If we choose 0 for a and 0 for b, the value for k should be 0 since 0 & 0 = 0
    (2): If we choose 1 for a and 0 for b, the value for k should be 0 since 0 & 1 = 0
    (3): If we choose 0 for a and 1 for b, the value for k should be 0 since 1 & 0 = 0
    (4): If we choose 1 for a and 1 for b, the value for k should be 1 since 1 & 1 = 1

    To avoid overflows, you should take care to use 64-bit integers. Also, this solution
    pattern is a standard way to solve these kinds of problems and can be generalized to
    any number system (and not just base 2 as was the case in our problem).

    The complexity of this solution is based on the size of the DP table which here is 31 * 2 * 2 * 2.
    """

    return count

# sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

reader = Reader()
reader.read()

T = reader.next_int()
for ti in range(1, T + 1):
    A = reader.next_int()
    B = reader.next_int()
    K = reader.next_int()
    result = countPairs(54, False, False, False, A, B, K)

    print('Case #{}: {}'.format(ti, result))