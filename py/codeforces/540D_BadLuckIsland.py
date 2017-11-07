# -*- coding: utf-8 -*-


"""
created by huash06 at 2015-05-07 09:23

有r，s，p个石头，剪刀，布，他们中任意两个碰到一起就会打起来，
石头吃掉剪刀，剪刀吃掉布，布吃掉石头。

问最后只剩下石头、剪刀、布的概率分别是多少
"""
__author__ = 'huash06'


import datetime
import sys

r, s, p = map(int, input().split(' '))

def test(r, s, p):
    """
    有r, s, p个石头剪刀布的情况下，任选两个的概率是：
    total = r*s + s*p + r*p
    P1 = P(rock, scissor) = r*s / total,
    P2 = P(rock, paper) = r*p / total,
    P3 = P(paper, scissor) = p*s / total
    因为如果选择的是两个一样的，比如石头和石头的概率是P(rock, rock)，
    这个概率还是会按照上面的比例分配到3种组合上

    即有P1的概率转换到新的状态r, s-1, p,
    有P2的概率转换到状态r-1, s, p,
    有P3的概率转换到状态r, s, p-1.


    :param r:
    :param s:
    :param p:
    :return:
    """
    if r == s == p:
        print(0.33333333333333, 0.33333333333333, 0.33333333333333)
        return

    g = [[[0.0 for k in range(p+2)] for j in range(s+2)] for i in range(r+2)]
    g[r][s][p] = 1

    for i in range(r, -1, -1):
        for j in range(s, -1, -1):
            ij = i*j
            for k in range(p, -1, -1):
                v = g[i][j][k]
                d = 3 - (i, j, k).count(0)
                if d <= 0:
                    continue
                if d == 1:
                    if i > 0:
                        g[i-1][j][k] += v
                    elif j > 0:
                        g[i][j-1][k] += v
                    elif k > 0:
                        g[i][j][k-1] += v
                elif d == 2:
                    if i > 0 and j > 0:
                        g[i][j-1][k] += v
                    elif j > 0 and k > 0:
                        g[i][j][k-1] += v
                    elif k > 0 and i > 0:
                        g[i-1][j][k] += v
                else:
                    pass
                    # ij = i*j
                    ik = i*k
                    jk = j*k
                    t = v/sum((ij, ik, jk))
                    g[i][j-1][k] += t*ij
                    g[i][j][k-1] += t*jk
                    g[i-1][j][k] += t*ik

    print(g[1][0][0], g[0][1][0], g[0][0][1])

starttime = datetime.datetime.now()
test(r, s, p)
sys.stderr.write('Time Cost: {}\n'.format(datetime.datetime.now()-starttime))