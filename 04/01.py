#!/usr/bin/env python3

if __name__ == '__main__':
    f = open("input.txt")
    cum = 0
    for ll in f:
        l,m = ll[:-1].split(",")
        l = [int(x) for x in l.split("-")]
        m = [int(x) for x in m.split("-")]
        l[1] += 1
        m[1] += 1
        a = list(range(*l))
        b = list(range(*m))
        i = set(a).intersection(set(b))
        if len(i) == len(a) or len(i) == len(b):
            cum += 1
    print(cum)



