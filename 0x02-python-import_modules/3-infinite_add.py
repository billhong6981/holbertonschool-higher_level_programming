#!/usr/bin/python3
def inf_add(av, sum):
    if len(av) == 1:
        return (sum)
    for i, c in list(enumerate(av, start=0)):
        if i != 0:
            sum += int(c)
    return (sum)


if __name__ == '__main__':
    import sys
    sum = 0
    print(inf_add(sys.argv, sum))
