#!/usr/bin/python3
"""my module"""


def pascal_triangle(n):
    """creats pascal triangle function"""

    def one_more(i, ls):
        """adds one more list to lists"""
        l = [1]
        ls = ls + [0]
        for i in range(i-1):
            l.append((ls[i]+ls[i+1]))
        return l

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    base = [[1], [1, 1]]
    for i in range(3, n+1):
        lis = one_more(i, base[i-2])
        base.extend([lis])
    return base
