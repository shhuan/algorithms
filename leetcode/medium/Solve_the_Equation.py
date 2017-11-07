# -*- coding: utf-8 -*-
"""

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        def parse(exp):
            if not exp:
                return None, None

            a, b = 0, 0  # ax+b

            expLen = len(exp)
            l = 0
            add = True
            for r, ch in enumerate(exp):
                if ch in {'-', '+'}:
                    if r > 0 and exp[r - 1] == 'x':
                        if add:
                            a += int(exp[l:r - 1]) if l < r - 1 else 1
                        else:
                            a -= int(exp[l:r - 1]) if l < r - 1 else 1
                    else:
                        if add:
                            b += int(exp[l:r]) if l < r else 0
                        else:
                            b -= int(exp[l:r]) if l < r else 0
                if ch == '-':
                    add = False
                    l = r + 1
                elif ch == '+':
                    add = True
                    l = r + 1
            if exp[-1] == 'x':
                if add:
                    a += int(exp[l:expLen - 1]) if l < expLen - 1 else 1
                else:
                    a -= int(exp[l:expLen - 1]) if l < expLen - 1 else 1
            else:
                if add:
                    b += int(exp[l:]) if l < expLen else 0
                else:
                    b -= int(exp[l:]) if l < expLen else 0

            return a, b

        left, right = equation.split('=')
        a, b = parse(left)
        c, d = parse(right)

        if a == c:
            if b != d:
                return "No solution"
            else:
                return "Infinite solutions"

        return 'x=%d' % ((d - b) // (a - c))





s = Solution()
print(s.solveEquation("-x=-1"))
print(s.solveEquation("x+5-3+x=6+x-2"))
print(s.solveEquation("x=x"))
print(s.solveEquation("2x=x"))
print(s.solveEquation("2x+3x-6x=x+2"))
print(s.solveEquation("x=x+2"))