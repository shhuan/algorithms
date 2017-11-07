# -*- coding: utf-8 -*-

"""
created by huash06 at 27 17:09
"""
__author__ = 'huash06'

import sys
import os
import random
import py.lib.Utils as Utils
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# class Grid:
# def __init__(self):
#         self._grids = []
#


def draw_rect(width, height, colors, title='GridImage', defaultcolr='k', edgecolor='g'):
    plt.figure(title)

    plt.xlim(- 1, width + 1)
    plt.ylim(- 1, height + 1)

    currentAxis = plt.gca()
    for r in range(height):
        for c in range(width):
            crc = colors.get((r, c))
            crc = crc if crc else defaultcolr
            currentAxis.add_patch(Rectangle((c, r), 1, 1, fc=crc, ec=edgecolor, fill=True, lw=3))
    plt.show()




def draw_grid(grid, left=0, right=0, bottom=0, top=0, color=None, xlabel=None, ylabel=None, xmarks=None, ymarks=None):
    """

    :param grid:
    :param left:
    :param right:
    :param bottom:
    :param top:
    :param color: each item indicates color of corresponding item in grid
    :param xlabel:
    :param ylabel:
    :param xmarks: list of marks
    :param ymarks: list of marks
    :return:
    """
    plt.figure('GridImage')

    top = len(grid) - 1 if top == 0 else top
    right = len(grid[0]) - 1 if right == 0 else right

    xlen = right - left + 1
    ylen = top - bottom + 1
    plt.xlim(left - 1, right + 1)
    plt.ylim(bottom - 1, top + 1)

    if xlabel is not None:
        plt.xlabel(str(xlabel))
    if ylabel is not None:
        plt.ylabel(str(xlabel))

    if ymarks is not None and isinstance(ymarks, list):
        y = 0
        for ymark in ymarks:
            plt.text(-0.4, y + 0.4, ymark)
            y += 1

    if xmarks is not None and isinstance(xmarks, list):
        x = 0
        for xmark in xmarks:
            plt.text(x + 0.4, -0.5, xmark)
            x += 1

    print('DRAW ({},{},{},{})'.format(left, right, bottom, top))

    for x in range(left, right + 1):
        plt.plot((x, x), (bottom, top), 'gray')
    for y in range(bottom, top + 1):
        plt.plot((left, right), (y, y), 'gray')

    for ri in range(top, bottom, -1):
        for ci in range(left, right):
            if color is not None and color[ri][ci] is not None:
                plt.text(ci + 0.4, ylen - ri - 0.6, '{}'.format(grid[ri][ci]), color=color[ri][ci])
            else:
                plt.text(ci + 0.4, ylen - ri - 0.6, '{}'.format(grid[ri][ci]))
    plt.show()

if __name__ == 'main':
    grid = [[row for row in range(1, 11)] for col in range(1, 11)]
    color = [[row for row in range(1, 11)] for col in range(1, 11)]
    xmarks = ['A', 'B', 'C', 'C', 'D', 'E', 'F', 'G', 'H']
    ymarks = [j for j in range(1, 11)]

    for ri in range(len(color)):
        r = color[ri]
        for ci in range(len(r)):
            c = str(hex(
                random.randint(1, 255) * (16 ** 4) + random.randint(1, 255) * (16 ** 2)
                + random.randint(1, 255))).upper()[2:]
            if len(c) < 6:
                c += '0' * (6 - len(c))
            elif len(c) > 6:
                c = c[:6]
            r[ci] = '#{}'.format(c)
            # r[ci] = '#FFC1C1'
    print(color)
    print(xmarks)
    print(ymarks)
    viewer = draw_grid(grid, color=color, xmarks=xmarks, ymarks=ymarks)