#!/usr/bin/env python3
import numpy as np
from parse import parse

def main():
    f = open("input.txt")
    o = np.array([[int(x) for x in l[:-1]] for l in f], dtype=np.int8)
    print(o.shape)
    g = np.zeros(o.shape, dtype=np.int8)
    print(g)


if  __name__ == '__main__':
    main()
