# -*- coding: utf-8 -*-

"""

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.


"""

import collections
import time
import copy

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        def vanish(bexp):
            while bexp:
                l = 0
                r = 1
                c = 1
                n = len(bexp)
                while r < n:
                    if bexp[r] != bexp[l]:
                        if c > 2:
                            break
                        c = 0
                        l = r
                    c += 1
                    r += 1
                if r-l<3:
                    return bexp
                bexp = bexp[:l]+bexp[r:]

            return ""

        def dfs(b, h, s):
            # print(b, vanish(b), h, s)
            # remove touching balls
            b = vanish(b)
            if b == '#':
                return s

            maxint = float('inf')

            ret = maxint

            l = 0
            for r in range(len(b)):
                if b[r] != b[l]:
                    # consecutive balls
                    csb = r - l
                    needed = 3-csb
                    if h[b[l]] >= needed:
                        nh = copy.deepcopy(h)
                        nh[b[l]] -= needed
                        # p.append((b[:l] + b[r:], nh))
                        ret = min(dfs(b[:l]+b[r:], nh, s+needed), ret)
                    l = r

            return ret

        hand = collections.Counter(hand)
        t0 = time.time()
        steps = dfs(board+"#", hand, 0)
        ret = -1 if steps == float('inf') else steps
        t1 = time.time()

        return ret


s = Solution()
print(s.findMinStep("RGGBYRRYWWYYBBGRGG", "RRYWG"))
# print(s.findMinStep("RBYYBBRRB", "YRBGB"))
# print(s.findMinStep("WWRRBBWW", "WRBRW"))
#
# t0 = time.time()
# print(s.findMinStep("RGGBYRRYWWYYBBGRGG", "RRYWG"))
# print(time.time() - t0)