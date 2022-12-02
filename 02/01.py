#!/usr/bin/env python3

def win(a, b):
    n = 0
    if (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
        n = 3
    if (a == "A" and b == "Y") or (a == "B" and b == "Z") or (a == "C" and b == "X"):
        n = 6
    n += ord(b) - 87
    return n

if __name__ == '__main__':
    f = open("input.txt")
    cum = 0
    for ll in f:
        a, b = ll[:-1].split(" ")
        cum += win(a,b)
    print(cum)



