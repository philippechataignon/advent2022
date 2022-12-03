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
    end = False
    while True:
        g = []
        for n in range(3):
            ll = f.readline()
            if not ll:
                end = True
            g.append(ll[:-1])
        if end:
            break
        c = set(g[0]).intersection(set(g[1])).intersection(set(g[2])).pop()
        cum += score(c)

    print(cum)



