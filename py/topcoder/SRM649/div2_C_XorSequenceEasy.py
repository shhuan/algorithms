# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-19 13:30

Problem Statement
You are given a A and an N that is a power of 2. All elements of A are between 0 and N-1, inclusive.

You can now choose an integer B which is between 0 and N-1, inclusive.
This integer determines a new sequence C defined as follows: For each valid i, C[i] = (A[i] xor B).

Given the sequence C, we will count the pairs of indices (i,j) such that both i<j and C[i]<C[j].
Compute and return the largest result we can obtain.


Definition
Class: XorSequenceEasy
Method: getmax
Parameters: tuple (integer), integer
Returns: integer
Method signature: def getmax(self, A, N):


Limits
Time limit (s): 2.000
Memory limit (MB): 256


Notes
- XOR (exclusive or) is a binary operation, performed on two numbers in binary notation.
First, the shorter number is prepended with leading zeroes until both numbers have the same number of digits (in binary).
Then, the result is calculated as follows: for each bit where the numbers differ the result has 1 in its binary
representation. It has 0 in all other positions.
- For example 42 XOR 7 is performed as follows. First, the numbers are converted to binary: 42 is 101010 and 7 is 111.
Then the shorter number is prepended with leading zeros until both numbers have the same number of digits. This means 7
becomes 000111. Then 101010 XOR 000111 = 101101 (the result has ones only in the positions where the two numbers differ).
Then the result can be converted back to decimal notation. In this case 101101 = 45, so 42 XOR 7 = 45.


Constraints
- N will be between 2 and 1,073,741,824 (2^30), inclusive.
- N will be a power of 2.
- The number of elements in A will be between 1 and 50, inclusive.
- Each element in A will be between 0 and N-1, inclusive.



分析：

两个数字a, b的大小关系由它们二进制下第一个不同的高位决定。

When comparing two numbers a and b, we need to find a biggest number k such that the k-th bit of a is different from the
k-th bit of b. The relation between a and b depends solely on that pair of bits. Denote that k for pair (a,b) as p(a,b).
The fact is that p(a,b)=p(a⊕x,b⊕x) for an arbitrary x because of the following statement: if c=d then c⊕x=d⊕x.

Now, what we need to do is to find a number B and xor all the elements of the given array A with B to create a new
sequence named C such that the number of pairs of indices i and j satisfy i<j and C(i)<C(j) is maximal. Consider two
elements A(i) and A(j) where i<j, based on the above observation, we need to consider the pair consists of the
p(A(i),A(j))-th bits of A(i) and A(j), denote it as (x,1−x). There are two possibilities:

    x=0: It means we have pair (0,1). If we set the bit at this position of B to 0. The pair remains the same and the
        result is increased by one. Otherwise, the pair changes to (1,0), the result remains the same.
    x=1: It means we have pair (1,0). In order to increase the result by one, we must set the bit at this position of
        B to 1.
By iterating all pairs of elements in array A, it is possible for us to calculate the profit of setting the i-th bit of
B to 0 and to 1. For each position i, we should choose the bit value which brings us the higher profit.

Overall, we have an algorithm with the complexity of O(size(A)2logn).

"""
__author__ = 'huash06'

import datetime
import sys


class XorSequenceEasy:
    def getmax(self, A, N):
        # len(bin(num))-2
        # int(math.log(n, 2)) + 1
        bitlen = N.bit_length()
        profits = [[0 for c in range(2)] for r in range(bitlen)]
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for b in range(bitlen-1, -1, -1):
                    if ((A[i] >> b) & 1) != ((A[j] >> b) & 1):
                        profits[b][(A[i] >> b) & 1] += 1
                        break
        result = 0
        for i in range(len(profits)):
            result += max(profits[i])

        return result





s = XorSequenceEasy()
print(s.getmax([3, 2, 1, 0, 3, 2], 4))
print(s.getmax([3, 0, 4, 6, 1, 5, 7, 6], 8))
print(s.getmax([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9], 16))
print(s.getmax([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], 8))
print(s.getmax([408024109,11635919,196474438,117649705,812669700,553475508,445349752,271145432,730417256,738416295 ,
                147699711,880268351,816031019,686078705,1032012284,182546393,875376506,220137366,906190345,16216108 ,
                799485093,715669847,413196148,122291044,777206980,68706223,769896725,212567592,809746340,964776169 ,
                928126551,228208603,918774366,352800800,849040635,941604920,326686120,920977486,964528038,659998484 ,
                207195539,607901477,725914710,655525412,949610052,142750431,766838105,1024818573,836758851,97228667],
               1073741824))