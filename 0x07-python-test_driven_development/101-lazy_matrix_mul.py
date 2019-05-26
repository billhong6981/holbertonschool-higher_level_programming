#!/usr/bin/python3
"""Nump Matrix Multification Module
Args:
    m_a: matrix a
    m_b: matrix b
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function makes two matrix multification
    Return:
        return new matrix after multification
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for sub in m_a:
        if not isinstance(sub, list):
            raise TypeError('m_a must be a list of lists')
    for sub in m_b:
        if not isinstance(sub, list):
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or m_a is None:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_a is None:
        raise ValueError("m_b can't be empty")
    b = [a for sub in m_a for a in sub]
    for i in b:
        if type(i) is not int and type(i) is not float:
            raise TypeError('m_a should contain only integers or floats')
    b = [a for sub in m_b for a in sub]
    for i in b:
        if type(i) is not int and type(i) is not float:
            raise TypeError('m_b should contain only integers or floats')
    c = [len(sub) == len(m_a[0]) for sub in m_a]
    if not all(c):
        raise TypeError('each row of m_a must should be of the same size')
    c = [len(sub) == len(m_b[0]) for sub in m_b]
    if not all(c):
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = np.dot(m_a, m_b)
    return res
