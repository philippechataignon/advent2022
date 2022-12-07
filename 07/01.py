#!/usr/bin/env python3
from parse import parse
from collections import defaultdict

def main():
    # f = open("input.txt")
    f = open("input.txt")
    wd = []
    # sz = defaultdict(int)
    sz = {('/',): 0}
    for l in f:
        l = l[:-1]
        if l[:4] == "$ ls":
            continue
        elif l[:4] == "$ cd":
            param = l[5:]
            if param == "..":
                wd.pop()
            else:
                wd.append(param)
            twd = tuple(wd)
        elif l[:3] == "dir":
            param = l[4:]
            if twd + (param,) not in sz:
                sz[twd + (param,)] = 0
        else:
            size, _ = parse("{:d} {}", l)
            sz[tuple(wd)] += size
    for k in sorted(sz, key=len, reverse=True):
        if k[:-1] in sz:
            sz[k[:-1]] += sz[k]
        else:
            sz[k[:-1]] = sz[k]

    print(sum([v for v in sz.values() if v < 100_000]))

    free = 70_000_000 - sz[('/',)]
    needed = 30_000_000 - free

    print(min([v for v in sz.values() if v > needed]))

if  __name__ == '__main__':
    main()
