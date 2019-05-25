#!/usr/bin/python3
"""Matrix divided by number
Args:
    matrix: a matrix, two dimemsion lists
    div: a number
"""


def matrix_divided(matrix, div):
    """Function makes matrix divided by a number
    Return:
        returns a matrix after division
    """

    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    b = [a for sub in matrix for a in sub]
    for i in b:
        if type(i) is not int and type(i) is not float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    c = [len(sub) == len(matrix[0]) for sub in matrix]
    if not all(c):
        raise TypeError('Each row of the matrix must have the same size')
    A = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(round(matrix[i][j]/div, 2))
        A.append(row)
    return A
