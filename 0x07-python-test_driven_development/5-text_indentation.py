#!/usr/bin/python3
"""Text Indentation
Args:
    text: a string
"""


def text_indentation(text):
    """function prints a text
    Return: None
    """

    if type(text) is not str:
        raise TypeError('text must be a string')
    A = [word for word in text.split()]
    for i in range(len(A)):
        j = len(A[i]) - 1
        print(A[i], end='')
        if i != len(A) - 1:
            if A[i][j] == '.' or A[i][j] == '?' or A[i][j] == ':':
                print('\n\n', end='')
            else:
                print(' ', end='')
        else:
            if A[i][j] == '.' or A[i][j] == '?' or A[i][j] == ':':
                print('\n\n', end='')
