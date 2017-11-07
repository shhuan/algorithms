# -*- coding: utf-8 -*-
'''

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.






32位整数，从最后一位开始，如果1的数量大于一半，那么重复的数字最后一位是1，否则是0。
同样的操作处理每一位， 记录下目标数值的每一位。




'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums) - 1

        last = 0
        for i in range(32):
            c0 = 0
            for v in nums:
                u = v ^ last
                if u % (1 << i) == 0 and (v >> i) & 1 == 0:
                    c0 += 1

            if c0 > N // 2:
                N = c0
            else:
                last |= 1 << i
                N = N - c0

        return last

s = Solution()
print(s.findDuplicate([1, 2, 3, 4, 5, 4]))