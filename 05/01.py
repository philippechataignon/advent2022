#!/usr/bin/env python3
from parse import parse

def move1(s, n, a, b):
    for i in range(n):
        c = s[a-1].pop()
        s[b-1].append(c)
    return s

def move2(s, n, a, b):
    cc = []
    for i in range(n):
        cc.insert(0, s[a-1].pop())
    s[b-1] += cc
    return s

def traite(func):
    f = open("input.txt")
    #f = open("test.txt")
    s = {}
    while True:
        l = f.readline()[:-1]
        cs = [l[x+1:x+2] for x in range(0, len(l), 4)]
        if cs[0] == "1":
            break
        for i, c in enumerate(cs):
            if s.get(i) is None:
                s[i] = []
            if c.strip() != "":
                s[i].insert(0, c)
    f.readline()
    while True:
        l = f.readline()
        if l == "":
            break
        n, a, b = [int(x) for x in parse("move {} from {} to {}", l)]
        s = func(s, n, a, b)
    print("".join([s[x][-1] for x in s]))

if __name__ == '__main__':
    traite(move1)
    traite(move2)
