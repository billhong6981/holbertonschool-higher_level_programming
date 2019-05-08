#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ls = list(zip(*matrix))
    if len(ls) == 0:
        print()
        return
    for j in range(len(matrix)):
        for i, d in enumerate(ls):
            print('{:d}'.format(d[j]), end=' ')
        print()
