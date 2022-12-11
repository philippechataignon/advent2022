#!/usr/bin/env python3
import numpy as np
from parse import parse

def main():
    f = open("test.txt")
    g = np.array([[int(x) for x in l[:-1]] for l in f], dtype=np.int8)
    print(g)
    print(g.shape)
    v = np.zeros(g.shape, dtype=np.bool)
    # top
    for c in range(g.shape[1]):
        for r in range(g.shape[0]):
            if r == 0:
                v[r, c] = True
            elif g[r - 1, c] < g[r, c]:
                v[r, c] = True
            else:
                break
    # bottom
    for c in range(g.shape[1]):
        for r in reversed(range(g.shape[0])):
            if r == g.shape[0] - 1:
                v[r, c] = True
            elif g[r + 1, c] < g[r, c]:
                v[r, c] = True
            else:
                break
    # left
    for r in range(g.shape[0]):
        for c in range(g.shape[1]):
            if c == 0:
                v[r, c] = True
            elif g[r, c - 1] < g[r, c]:
                v[r, c] = True
            else:
                break
    # right
    for r in range(g.shape[0]):
        for c in reversed(range(g.shape[1])):
            if c == g.shape[1] - 1:
                v[r, c] = True
            elif g[r, c + 1] < g[r, c]:
                v[r, c] = True
            else:
                break

    print(v)
    print(sum(sum(v)))

if  __name__ == '__main__':
    main()
