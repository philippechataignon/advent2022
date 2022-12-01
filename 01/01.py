#!/usr/bin/env python3

if __name__ == '__main__':
    f = open("input.txt")
    maxi = 0
    cum = 0
    for ll in f:
        l = ll[:-1]
        if l == "":
            cum = 0
        else:
            cum += int(l)
            if cum > maxi:
                maxi = cum
    print(maxi)



