#!/usr/bin/env python3
import numpy as np
from parse import parse

def main():
    f = open("input.txt")
    g = np.array([[int(x) for x in l[:-1]] for l in f], dtype=np.int8)
    print(g)
    print(g.shape)
    v = np.zeros(g.shape, dtype=np.bool)
    for c in range(g.shape[1]):
        # top
        r = 0
        l1 = -1
        while r < g.shape[0]:
            if g[r, c] > l1:
                v[r, c] = True
                l1 = g[r, c]
            r += 1
        # bottom
        r = g.shape[0] - 1
        l2 = -1
        while r >= 0:
            if g[r, c] > l2:
                v[r, c] = True
                l2 = g[r, c]
            r -= 1
    for r in range(g.shape[0]):
        # left
        c = 0
        l1 = -1
        while c < g.shape[1]:
            if g[r, c] > l1:
                v[r, c] = True
                l1 = g[r, c]
            c += 1
        # right
        c = g.shape[1] - 1
        l2 = -1
        while c >= 0:
            if g[r, c] > l2:
                v[r, c] = True
                l2 = g[r, c]
            c -= 1
    print(v)
    print(sum(sum(v)))

if  __name__ == '__main__':
    main()
