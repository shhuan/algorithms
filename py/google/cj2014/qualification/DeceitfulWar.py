# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-07 16:04


Naomi 和 Ken玩一個叫War的遊戲， 遊戲的過程是：
    1. Naomi 和 Ken各自有一些重為(0.0,1.0)的石頭， 他們都只知道自己的石頭的重量
    2. 重複以下過程
        1. Naomi選一塊石頭，重為Wn
        2. Naomi告訴Ken她選的石頭的重量
        3. Ken選一塊石頭，重為Wk
        4. 把兩塊石頭放到天平上比較，較重的人得一分
        5. 把這兩塊石頭扔掉
玩了一段時間後Naomi發現:
    1. 她總是輸
    2. Ken有一個最優策略,並卻Ken總是使用這個策略
    3. 她非常討厭輸

Naomi決定玩Deceitful War代替War, Deceitful War有趣的地方在於Ken以為他玩的War.
Deceitful War的玩法是:
    1. 兩個玩家分別稱自己的石頭的重量, 但是Naomi在Ken沒注意的時候偷偷也稱了Ken的石頭的重量,所以Naomi知道他們兩個人的所有石頭的重量.
    2. 重複下面的過程N次:
        1. Naomi選一塊石頭,重為Wn
        2. Naomi告訴Ken她選的石頭的重量是W'n, (0.0 < W'n < 1.0)， 由於Ken以為他玩的是War，所以他認為Naomi沒有撒謊。
        3. Ken按照他的策略選一塊石頭，重為Wk
        4. 把兩塊石頭放到天平上比較，較重的人得一分
        5. 把這兩塊石頭扔掉
Naomi為了不讓Ken知道她玩的是Deceitful War而不是War, 就不能讓Ken知道Wn != W'n。
所以Naomi告訴Ken的重量必須滿足條件:
    1. 只有Wn>Wk時，才W'n>Wk。
    2. W'n != Wk
否則會被Ken發現。

例子1：
    Naomi有一塊石頭重0.5， Ken有一塊石頭中0.6。 Naomi不能說她的石頭重大於等於0.6，這樣Ken會發現。
    這個例子中Naomi只能得到0分， Ken得1分
例子2：
    Naomi有兩款石頭重[0.7, 0.2]， Ken的兩塊石頭重[0.8, 0.3]。
    Naomi可以先選重為0.2的石頭，然後告訴Ken她選的石頭中0.6，Ken信以為真就出0.8kg的石頭，贏得1分。
    Ken不會發現是因為他出的石頭和他預想的一樣比Naomi出的石頭重。
    現在Naomi出0.7的石頭對Ken的0.3的石頭，Naomi得1分。
    結果是Naomi和Ken分別得1分，但是如果按照War的話Naomi只能得0分


給出Naomi和Ken的石頭的重量，要求計算兩種遊戲下Naomi分別能夠得多少分？


分析：
Ken的策略明顯是貪心策略，即只要Naomi報出一個重量，他就從自己的石頭當中選擇一塊重量和Naomi的最接近但是比她的石頭重的一塊。
這種策略在War下面可以得到最大收益。
計算很簡單，把他們的石頭按照重量排序後按照下面的方式對齊，相交部分的長度就是Ken的得分
Naomi: 3, 5, 9; Ken: 2, 4, 6; _是佔位符
_, 3, 5, 9
2, 4, 6

在Deceitful War裡面，Naomi可以使用最輕的石頭幹掉Ken的最重的石頭，剩下的就是Naomi贏。
Naomi: 3, 5, 7; Ken: 2, 4, 9, Naomi使用3並告訴Ken重量是8，Ken出9，相當於如下對齊方式：
3, 5, 7
_, 2, 4, 9
即從Naomi的第i塊石頭開始， 石頭Naomi[i, N]分別大於石頭Ken[0, N-i]



"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

if __DEBUG__:
    sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/D-large-practice.in', 'r')
sys.stdout = open('output/D-large-practice.out', 'w')

MAXNN = 301

T = int(sys.stdin.readline())
for ti in range(1, T+1):
    N = int(sys.stdin.readline())
    A = map(float, input().split(' '))
    B = map(float, input().split(' '))
    A = sorted(A)
    B = sorted(B)

    l = 0
    r = 0
    z = 0
    for i in range(N):
        for j in range(l, N):
            if A[j] < B[i]:
                l = j+1
                z += 1
                break
    z = N - z

    y = 0
    for l in range(N):
        found = True
        for i in range(l, N):
            if A[i] < B[i-l]:
                found = False
                break
        if found:
            y = N-l
            break

    print('Case #{}: {} {}'.format(ti, y, z))
