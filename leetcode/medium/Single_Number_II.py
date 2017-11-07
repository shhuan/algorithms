# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 09:08

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


本题目抄袭网上解答
http://blog.csdn.net/u011960402/article/details/17750993

"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if not A:
            return -1
        # 题目中，如果数组中的元素都是三个三个出现的，那么从二进制表示的角度，每个位上的1加起来，应该可以整除3。
        # 如果某个特定位上的1加起来，可以被3整除，说明对应x的那位是0，因为如果是1，不可能被3整除
        # 如果某个特定位上的1加起来，不可以被3整除，说明对应x的那位是1
        # 我们可以开辟一个大小为32的数组，第0个元素表示，A中所有元素的二进制表示的最低位的和，依次类推。
        # 最后，再转换为十进制数即可。这里要说明的是，用一个大小为32的整数数组表示，同样空间是O(1)的
        count = [0]*32
        for v in A:
            for i in range(32):
                if ((v >> i) & 1) > 0:
                    count[i] += 1
        print(count)
        result = 0
        for i in range(31, -1, -1):
            result <<= 1
            if count[i] % 3 != 0:
                result += 1
        # python3 没有int, 是自动类型
        if result & (1 << 31):
            result -= (1 << 32)
        return result

    def singleNumber2(self, A):
        """
        看了上面的分析之后，我们突然会想是否有一些更简洁的方法来实现这个问题。
        同样从位运算的角度来看，我希望一个数用来表示出现一次的位，也就是说这个数的为1的位就表示这个位上面的数出现过了一次，
        比如0x10001，就表示bit[0]和bit[4]就是出现过了一次的位。然后再用一个数表示出现过了两次的位，再用一个数表示出现过了3次的位。
        只要这个位出现过了3次，我就把这个位拿清除掉，这样剩余的最后出现过一次的位的这个数就是我们要找的数了。
        :param A:
        :return:
        """

        ones = 0
        twos = 0
        threes = 0
        for v in A:
            twos |= ones & v
            ones ^= v
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones

s = Solution()
# print(s.singleNumber([1, 2, 3, 1, 1, 3, 3]))
# print(s.singleNumber([6, 3, 3, 3]))
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
print(s.singleNumber2([-2,-2,1,1,-3,1,-3,-3,-4,-2]))