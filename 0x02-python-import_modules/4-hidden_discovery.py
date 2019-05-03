#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for c in list(dir(hidden_4)):
        if c[0:2] != '__':
            print(c)
