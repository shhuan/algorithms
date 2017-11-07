# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 10:51

你和小弟弟玩一个战船游戏，你闭上眼睛，然后小弟弟把大小为1*W的船放在R*C的地图上某个位置。
你开始指定攻击某个位置，小弟弟根据你的位置回答你是否命中船身。
小弟弟会撒谎，他可以在任意时刻改变船的位置，但是前后的说法必须保持一致而不被你发现。
你也知道小弟弟会撒谎，要求就算最少需要多少次攻击才能把船身的每一格都命中。



分析：
你和小弟弟都采用最优策略，地图有R行，你一行一行的攻击，小弟弟最终会把船挪到最后一行来躲避你的攻击。
所以你需要把前面每一个都完全排除，每行需要攻击self.C // self.W次，每次他都会说miss，然后这一行就没有可以放船的地方了。
最后一行第self.C // self.W次攻击一定能攻击到船的某个位置，如果攻击到的是船的最后一节，只需要再攻击W-1次即可；
如果不是最后一节，小弟弟最多还有一次撒谎的机会，就是需要再攻击W次



"""
__author__ = 'huash06'

import datetime
import sys

# sys.stdin = open('input/A-small-practice.in', 'r')
# sys.stdout = open('output/A-small-practice.out', 'w')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

class Solution:
    def __init__(self):
        self.R = 0
        self.C = 0
        self.W = 0

    def test(self):
        self.R = 1
        self.C = 10
        self.W = 3
        sys.stderr.write('{}\n'.format(self.solve()))

    def readInput(self):
        self.R, self.C, self.W = [int(x) for x in input().split()]

    def readMockInput(self):
        pass

    def solve(self):
        hitRow = (self.C // self.W + self.W - (1 if self.C % self.W == 0 else 0))
        misRow = self.C // self.W
        return (self.R - 1) * misRow + hitRow


startTime = datetime.datetime.now()
Solution().test()
T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))