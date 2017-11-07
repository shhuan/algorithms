"""

旋转字符串，把后面k个字符串移到前面，要求只用O(1)的空间。

"""
__author__ = 'huash06'

import sys

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums:
            return

        n = len(nums)
        k %= n

        if k <= 0:
            return

        left = 0
        right = n
        reverse_right = True
        if right - left <= 2*k:
            reverse_right = False
            k = right-left-k
        while left < right and k > 0:
            if right - left <= 2*k:
                reverse_right = not reverse_right
                k = right-left-k

            if reverse_right:
                for d in range(k):
                    l = left+d
                    r = right-k+d
                    v = nums[l]
                    nums[l] = nums[r]
                    nums[r] = v
                # print('Reversing Right {}, {}, {}'.format(left, right, k))
                # print(nums)
                left += k
            else:
                for d in range(k):
                    r = right - d - 1
                    l = left + k - d - 1
                    v = nums[r]
                    nums[r] = nums[l]
                    nums[l] = v
                # print('Reversing Left {}, {}, {}'.format(left, right, k))
                # print(nums)
                right -= k
        # print(nums)

# sys.stdout = 'output/rotate_array.txt'
s = Solution()

for n in [6, 7]:
    for k in range(1, 10):
        # print('Rotating {}, {}'.format(n, k))
        s.rotate([i for i in range(1, n+1)], k)