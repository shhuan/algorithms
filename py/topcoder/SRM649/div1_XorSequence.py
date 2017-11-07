# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-19 16:08



Problem Statement
You are given an integer sequence A and an N that is a power of 2.
All elements of A are between 0 and N-1, inclusive.

You can now choose an integer B which is between 0 and N-1, inclusive.
This integer determines a new sequence C defined as follows: For each valid i, C[i] = (A[i] xor B).

Given the sequence C, we will count the pairs of indices (i,j) such that both i<j and C[i]<C[j].
Compute and return the largest result we can obtain.

You are given the N. You are also given s sz, A0, A1, P, Q, and R.
Use the following pseudocode to generate the sequence A:

    A[0] = A0;
    A[1] = A1;
    for (i = 2; i < sz; i++) {
        A[i] = (A[i - 2] * P + A[i - 1] * Q + R) modulo N;
    }


Definition
Class: XorSequence
Method: getmax
Parameters: integer, integer, integer, integer, integer, integer, integer
Returns: long integer
Method signature: def getmax(self, N, sz, A0, A1, P, Q, R):


Limits
Time limit (s): 2.000
Memory limit (MB): 256


Notes
- Watch out for integer overflow when generating the sequence A.


Constraints
- N will be between 2 and 1,073,741,824 (2^30), inclusive.
- N will be a power of 2.
- sz will be between 2 and 131,072, inclusive.
- A0 will be between 0 and N-1, inclusive.
- A1 will be between 0 and N-1, inclusive.
- P will be between 0 and N-1, inclusive.
- Q will be between 0 and N-1, inclusive.
- R will be between 0 and N-1, inclusive.

"""
__author__ = 'huash06'

import datetime
import sys
import collections
class XorSequence:
    def getmax(self, N, sz, A0, A1, P, Q, R):

        A = [0] * sz
        A[0] = A0
        A[1] = A1
        for i in range(2, sz):
            A[i] = (A[i - 2] * P + A[i - 1] * Q + R) % N

        # sys.stderr.write('{}\n'.format(A))

        bitlen = N.bit_length()
        # profits = [[0 for c in range(2)] for r in range(bitlen)]
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         for b in range(bitlen-1, -1, -1):
        #             if ((A[i] >> b) & 1) != ((A[j] >> b) & 1):
        #                 profits[b][(A[i] >> b) & 1] += 1
        #                 break
        # result = 0
        # for i in range(len(profits)):
        #     result += max(profits[i])

        print(A)
        nums = list(sorted([(v, i) for i, v in enumerate(A)]))
        print(nums)

        groups = collections.defaultdict(list)

        simk = self.firstDifferentBits(nums[0][0], nums[1][0], bitlen)
        groups[simk].extend(nums[:2])
        i = 0
        while i < sz:
            j = i + 1
            while j < sz:
                nextK = self.firstDifferentBits(nums[i][i], nums[j][0], bitlen)
                if nextK == simk:
                    groups[simk].append(nums[j])
                else:
                    break




        result = 0
        return result

    def firstDifferentBits(self, numA, numB, bitLen):
        simk = bitLen
        for i in range(bitLen-1, -1, -1):
            if ((numA >> i) & 1) != ((numB >> i) & 1):
                simk = i
                break
        return simk

s = XorSequence()
print(s.getmax(4, 6, 3, 2, 0, 1, 3))