# -*- coding: utf-8 -*-
"""


Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
since they don't influence the operation priority. So you should return "1000/(100/10/2)".

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.

"""


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        N = len(nums)

        memo = {}

        def dfs(l, r):
            if l >= r:
                return 1, 1, "", ""

            if l == r - 1:
                return nums[l], nums[l], str(nums[l]), str(nums[l])

            k = l,r
            if k in memo:
                return memo[k]
            mxv, mnv, mxexp, mnexp = float('-inf'), float('inf'), "", ""

            for m in range(l+1, r):
                mxvl, mnvl, mxexpl, mnexpl = dfs(l, m)
                mxvr, mnvr, mxexpr, mnexpr = dfs(m, r)

                tmxv = (1.0*mxvl) / mnvr
                tmnv = (1.0*mnvl) / mxvr

                if tmnv < mnv:
                    mnv = tmnv
                    mnexp = "%s/%s" % (mnexpl, "(%s)" % mxexpr if mxexpr.find('/') >= 0 else mxexpr)
                if tmxv > mxv:
                    mxv = tmxv
                    mxexp = "%s/%s" % (mxexpl, "(%s)" % mnexpr if mnexpr.find('/') >= 0 else mnexpr)

            memo[k] = mxv, mnv, mxexp, mnexp
            return mxv, mnv, mxexp, mnexp


        _, _, exp, _ = dfs(0, N)
        return exp




s = Solution()
print(s.optimalDivision([2,3,4]))