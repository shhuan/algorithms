# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-07 08:40


最长公共子序列的结构有如下表示：

设序列X=<x1, x2, …, xm>和Y=<y1, y2, …, yn>的一个最长公共子序列Z=<z1, z2, …, zk>，则：
1. 若xm=yn，则zk=xm=yn且Zk-1是Xm-1和Yn-1的最长公共子序列；
2. 若xm≠yn且zk≠xm，则Z是Xm-1和Y的最长公共子序列；
3. 若xm≠yn且zk≠yn，则Z是X和Yn-1的最长公共子序列。
其中Xm-1=<x1, x2,…, xm-1>，Yn-1=<y1, y2, …, yn-1>，Zk-1=<z1, z2, …, zk-1>。

直接使用这个公式递归的计算LCS是指数复杂度，使用动态规划自底向上的计算。

计算最长公共子序列长度的动态规划算法LCS_LENGTH(X,Y)以序列X=<x1, x2, …, xm>和Y=<y1, y2, …, yn>作为输入。
输出两个数组c[0..m ,0..n]和b[1..m ,1..n]。其中c[i,j]存储Xi与Yj的最长公共子序列的长度，
b[i,j]记录指示c[i,j]的值是由哪一个子问题的解达到的，这在构造最长公共子序列时要用到。
最后，X和Y的最长公共子序列的长度记录于c[m,n]中。


"""
__author__ = 'huash06'

import sys
import os
import matplotlib.pyplot as plt

MAXN = 100
C = [[0 for col in range(MAXN)] for row in range(MAXN)]
B = [['-' for col in range(MAXN)] for row in range(MAXN)]
PATH = list()

def LCS_LENGTH(X, Y):
    lx = len(X)
    ly = len(Y)
    for r in range(lx+1):
        for c in range(ly+1):
            C[r][c] = 0
            B[r][c] = '-'

    for i in range(0, lx):
        for j in range(0, ly):
            # 情况1
            if X[i] == Y[j]:
                # 坐标从(1,1)开始处理起来会更简单
                if i == 0 or j == 0:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1]+1
                    B[i][j] = '$\\nwarrow$'
            # 情况2
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                B[i][j] = '$\uparrow$'
            # 情况3
            else:
                C[i][j] = C[i][j-1]
                B[i][j] = '$\leftarrow$'

def LCS(X, xlen, ylen):
    if xlen < 0 or ylen < 0:
        return
    if B[xlen][ylen] == '$\\nwarrow$' or B[xlen][ylen] == '-':
        LCS(X, xlen-1, ylen-1)
        sys.stdout.write(X[xlen])
        PATH.append((xlen-1, ylen-1))
    elif B[xlen][ylen] == '$\uparrow$':
        LCS(X, xlen-1, ylen)
        PATH.append((xlen-1, ylen))
    else:
        LCS(X, xlen, ylen-1)
        PATH.append((xlen, ylen-1))

def show(X, Y):

    lenr = len(X)
    lenc = len(Y)

    plt.figure('LCS')
    plt.xlim(-1, lenc+1)
    plt.ylim(-1, lenr+1)
    for r in range(0, lenr+1):
        plt.plot((0, lenc), (r, r), color='black')
    for r in range(lenr):
        plt.text(-0.3, r+0.3, X[lenr-r-1])
    for c in range(0, lenc+1):
        plt.plot((c, c), (0, lenr), color='black')
    for c in range(lenc):
        plt.text(c+0.4, lenr+0.3, Y[c])

    for r in range(lenr):
        for c in range(lenc):

            if B[r][c] != '-':
                if (r, c) in PATH:
                    plt.text(c+0.4, lenr-r-1+0.6, C[r][c], color='red')
                    plt.text(c+0.3, lenr-r-1+0.3, r'{}'.format(B[r][c]), color='red')
                else:
                    plt.text(c+0.4, lenr-r-1+0.6, C[r][c])
                    plt.text(c+0.3, lenr-r-1+0.3, r'{}'.format(B[r][c]))
            else:
                if (r, c) in PATH:
                    plt.text(c+0.4, lenr-r-1+0.6, C[r][c], color='red')
                    plt.text(c+0.3, lenr-r-1+0.3, r'$\bigstar$', color='red')
                else:
                    plt.text(c+0.4, lenr-r-1+0.6, C[r][c])

    plt.show()

if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'
    PATH = list()
    LCS_LENGTH(X, Y)
    LCS(X, len(X)-1, len(Y)-1)
    show(X, Y)

