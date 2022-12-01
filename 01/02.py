#!/usr/bin/env python3

if __name__ == '__main__':
    f = open("input.txt")
    c = []
    cum = 0
    for ll in f:
        l = ll[:-1]
        if l == "":
            c.append(cum)
            cum = 0
        else:
            cum += int(l)
    c.sort(reverse=True)
    print(c[0] + c[1] + c[2])



