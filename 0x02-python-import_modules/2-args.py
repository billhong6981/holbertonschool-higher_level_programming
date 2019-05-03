#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print('1 argument:')
    else:
        if len(sys.argv) == 1:
            print('0 arguments.')
        else:
            print('{:d} arguments:'.format(len(sys.argv) - 1))
    for i, c in list(enumerate(sys.argv, start=0)):
        if i != 0:
            print('{:d}: {}'.format(i, c))
