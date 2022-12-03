#!/usr/bin/env python3

def score(c):
    if "a" <= c <= "z":
        return ord(c) - 96
    elif "A" <= c <= "Z":
        return ord(c) - 38
    return 0

if __name__ == '__main__':
    f = open("input.txt")
    cum = 0
    for ll in f:
        l = ll[:-1]
        m = len(l) // 2
        a, b = l[:m], l[m:]
        c = set(a).intersection(set(b)).pop()
        cum += score(c)
    print(cum)



