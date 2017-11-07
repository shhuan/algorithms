# -*- coding: utf-8 -*-
# from __future__ import print_function
# __author__ = 'huash06'

# import py.lib.TreeViewer as TreeViewer
import re
import sys
# import random

__DEBUG = False


class Expression:
    def __init__(self, _left_exp, _right_exp, _operator, _exp, _deviration):
        self.leftExp = _left_exp
        self.rightExp = _right_exp
        self.operator = _operator
        self.expression = _exp
        self.deviration = _deviration
        self.children = [self.leftExp, self.rightExp]

    def __str__(self):
        if self.expression is not None:
            return self.expression + '\n' + self.deviration
        return self.operator

    @staticmethod
    def make_expression(_exp):
        """
        构造表达式树，然后再调用parse_expression计算导数。
        处理的优先级是(),+/-,*/x,ln。
        构造的时候不处理符号
        :param _exp:
        :return:
        """
        if _exp is None:
            return None
        _exp = _exp.strip()
        if len(_exp) <= 0:
            return None

        # 构造(X)的表达式树
        if _exp.startswith('('):
            pcount = 0
            for i in range(len(_exp)):
                if _exp[i] == '(':
                    pcount += 1
                elif _exp[i] == ')':
                    pcount -= 1
                if pcount == 0:
                    if i == len(_exp) - 1:
                        exp_right = Expression.make_expression(_exp[1:-1])
                        return Expression(None, exp_right, '()', _exp, None)
                        # dev.expression = '({})'.format(dev.deviration)
                    else:
                        break

        # 构造A＋B和A-B的表达式
        pcount = 0
        for i in range(len(_exp)):
            if _exp[i] == '(':
                pcount += 1
            elif _exp[i] == ')':
                pcount -= 1
            elif pcount == 0:
                if i != 0 and (_exp[i] == '+' or _exp[i] == '-'):
                    exp_left = Expression.make_expression(_exp[0:i])
                    exp_right = Expression.make_expression(_exp[i + 1:])
                    return Expression(exp_left, exp_right, _exp[i], _exp, None)

        # 构造A*B和A/B的表达式
        pcount = 0
        last_index = -1
        for i in range(len(_exp)):
            if _exp[i] == '(':
                pcount += 1
            elif _exp[i] == ')':
                pcount -= 1
            elif pcount == 0:
                if _exp[i] == '*' or _exp[i] == '/':
                    last_index = i
        if last_index >= 0:
            exp_left = Expression.make_expression(_exp[0:last_index])
            exp_right = Expression.make_expression(_exp[last_index + 1:])
            return Expression(exp_left, exp_right, _exp[last_index], _exp, None)

        # 构造ln函数的表达式树
        if _exp.startswith('ln'):
            exp_right = Expression.make_expression(_exp[3:-1])
            return Expression(None, exp_right, 'ln', _exp, None)

        return Expression(None, None, None, _exp, None)


def parse_expression(_exp):
    """
    遍历表达式树计算导数，注意处理符号
    :param _exp:
    :return:
    """
    if _exp is None:
        return
    if _exp.operator is not None:
        parse_expression(_exp.leftExp)
        parse_expression(_exp.rightExp)
        if _exp.operator in ['+', '-']:
            _exp.deviration = '{0}{1}{2}'.format(_exp.leftExp.deviration, _exp.operator,
                                                 _exp.rightExp.deviration)
        elif _exp.operator == '*':
            _exp.deviration = '({0}*{1}+{2}*{3})'.format(_exp.leftExp.deviration, _exp.rightExp.expression,
                                                         _exp.leftExp.expression, _exp.rightExp.deviration)
        elif _exp.operator == '/':
            _exp.deviration = '({0}*{1}-{2}*{3})/{4}^2'.format(_exp.leftExp.deviration,
                                                               _exp.rightExp.expression,
                                                               _exp.leftExp.expression,
                                                               _exp.rightExp.deviration,
                                                               _exp.rightExp.expression)
        elif _exp.operator == 'ln':
            _exp.deviration = '({0})/({1})'.format(_exp.rightExp.deviration, _exp.rightExp.expression)
        elif _exp.operator == '()':
            _exp.deviration = '({})'.format(_exp.rightExp.deviration)
    elif _exp.leftExp is None and _exp.rightExp is None:
        if _exp.expression == 'x':
            _exp.deviration = '1'
        else:
            _exp.deviration = '0'
    if _exp.deviration is None:
        return
    pattern = re.compile('[+-]{2,}')

    # print('find pattern in %s' % _exp.deviration)
    iters = pattern.finditer(_exp.deviration)
    matches = list(iters) if iters is not None else None
    if matches is not None and len(matches) > 0:
        # g = lambda m: m.span()
        # print('Math {0} at {1}'.format(_exp.deviration, map(g, matches)))
        deviration = ''
        pend = -1
        for m in matches:
            deviration += _exp.deviration[pend:m.start()] if pend >= 0 else _exp.deviration[:m.start()]
            operator = _exp.deviration[m.start(): m.end()]
            if operator == '++' or operator == '--':
                deviration += '+'
            elif operator == '+-' or operator == '-+':
                deviration += '-'
            # deviration += _exp.deviration[]
            pend = m.end()
        deviration += _exp.deviration[pend:]
        # print('%s --> %s' % (_exp.deviration, deviration))
        _exp.deviration = deviration


p = re.compile('[^\w]')

if __DEBUG:
    sys.stdin = open('input/input_1138.txt', 'r')
    sys.stdout = open('output/output_1138.txt', 'w')
for line in sys.stdin:
    # print('Handling expressing {0}'.format(line))
    exp = Expression.make_expression(line)
    parse_expression(exp)
    print(exp.deviration)
    # sys.stdout.writelines(exp.deviration)

    # if __DEBUG:
    # fname = exp.expression if exp.expression is not None else 'None-{0}'.format(random.randrange(100))
    # fname = p.sub('', fname)
    #     p.sub('', fname)
    #     TreeViewer.draw_tree(exp, fname + '.png')
