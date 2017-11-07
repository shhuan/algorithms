# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 09:38

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


以下来自：http://zhedahht.blog.163.com/blog/static/25411174201283084246412/

１.　找出两个字出现一次的数字
    我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。
    因为其他数字都出现了两次，在异或中全部抵消掉了。由于这两个数字肯定不一样，那么这个异或结果肯定不为0，
    也就是说在这个结果数字的二进制表示中至少就有一位为1。我们在结果数字中找到第一个为1的位的位置，记为第N位。
    现在我们以第N位是不是1为标准把原数组中的数字分成两个子数组，第一个子数组中每个数字的第N位都为1，
    而第二个子数组的每个数字的第N位都为0。
２. 找出三个只出现一次的数字

    如果我们把数组中所有数字都异或起来，那最终的结果（记为x）就是a、b、c三个数字的异或结果（x=a^b^c）。
    其他出现了两次的数字在异或运算中相互抵消了。

    我们可以证明异或的结果x不可能是a、b、c三个互不相同的数字中的任何一个。我们用反证法证明。
    假设x等于a、b、c中的某一个。比如x等于a，也就是a=a^b^c。因此b^c等于0，即b等于c。这与a、b、c是三个互不相同的三个数相矛盾。

    由于x与a、b、c都各不相同，因此x^a、x^b、x^c都不等于0。

    我们定义一个函数f(n)，它的结果是保留数字n的二进制表示中的最后一位1，而把其他所有位都变成0。
    比如十进制6表示成二进制是0110，因此f(6)的结果为2（二进制为0010）。f(x^a)、f(x^b)、f(x^c)的结果均不等于0。

    接着我们考虑f(x^a)^f(x^b)^f(x^c)的结果。由于对于非0的n，f(n)的结果的二进制表示中只有一个数位是1，
    因此f(x^a)^f(x^b)^f(x^c)的结果肯定不为0。这是因为对于任意三个非零的数i、j、k，f(i)^f(j)的结果要么为0，
    要么结果的二进制结果中有两个1。不管是那种情况，f(i)^f(j)都不可能等于f(k)，因为f(k)不等于0，并且结果的二进制中只有一位是1。

    于是f(x^a)^f(x^b)^f(x^c)的结果的二进制中至少有一位是1。假设最后一位是1的位是第m位。
    那么x^a、x^b、x^c的结果中，有一个或者三个数字的第m位是1。

    接下来我们证明x^a、x^b、x^c的三个结果第m位不可能都是1。还是用反证法证明。如果x^a、x^b、x^c的第m位都是1，
    那么a、b、c三个数字的第m位和x的第m位都相反，因此a、b、c三个数字的第m位相同。如果a、b、c三个数字的第m位都是0，
    x=a^b^c结果的第m位是0。由于x和a两个数字的第m位都是0，x^a结果的第m位应该是0。同理可以证明x^b、x^c第m位都是0。
    这与我们的假设矛盾。如果a、b、c三个数字的第m位都是1，x=a^b^c结果的第m位是1。由于x和a两个数字的第m位都是1，
    x^a结果的第m位应该是0。同理可以证明x^b、x^c第m位都是0。这还是与我们的假设矛盾。

    因此x^a、x^b、x^c三个数字中，只有一个数字的第m位是1。于是我们找到了能够区分a、b、c三个数字的标准。
    这三个数字中，只有一个数字满足这个标准，而另外两个数字不满足。一旦这个满足标准数字找出来之后，另外两个数字也就可以找出来了。

"""
__author__ = 'huash06'

import sys
import os
import functools

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):

        return functools.reduce(lambda x, y: x ^ y, A)


s = Solution()
print(s.singleNumber([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))