#!/usr/bin/env python3
from parse import parse

def main():
    #f = open("input.txt")
    f = open("test.txt")
    wd = []
    sz = {}
    for l in f:
        l = l[:-1]
        # print(l)
        if l[0] == "$": # command
            if l[2:4] == "ls":
                continue
            else:
                cmd, param = parse("$ {} {}", l)
                print(cmd, param)
                if param == "..":
                    wd.pop()
                elif param == "/":
                    continue
                else:
                    wd.append(param)
                print(wd)
        elif l[:3] == "dir":
            continue
        else:
            size, name = parse("{:d} {}", l)
            print(size, name)
            for d in wd:
                if d not in sz:
                    sz[d] = 0
                sz[d] += size
    print(sz)
    cum = 0
    for v in sz.values():
        if v <= 100000:
            cum += v
    print(cum)

if  __name__ == '__main__':
    main()
