#!/usr/bin/env python3
def all_diff(l):
    return len(l) == len(set(l))

def traite(l, d):
    for i in range(len(l) - d + 1):
        if all_diff(l[i:i+d]):
            return i + d
    return None

def go(func):
    f = open("input.txt")
    cum = 0
    for l in f:
        l = l[:-1]
        r = func(l)
        cum += r
    print(cum)

def main():
    go(lambda x: traite(x, 4))
    go(lambda x: traite(x, 14))

if __name__ == '__main__':
    main()
