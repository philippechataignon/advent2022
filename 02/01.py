#!/usr/bin/env python3

def win(a, b):
    n = 0
    if (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
        n = 3
    if (a == "A" and b == "Y") or (a == "B" and b == "Z") or (a == "C" and b == "X"):
        n = 6
    n += " XYZ".index(b)
    return n

def answer(a, s):
    d = {
            "X": {"A": "Z", "B": "X", "C": "Y"},
            "Y": {"A": "X", "B": "Y", "C": "Z"},
            "Z": {"A": "Y", "B": "Z", "C": "X"},
        }
    return d[a][s]

if __name__ == '__main__':
    f = open("input.txt")
    cum1 = 0
    cum2 = 0
    for ll in f:
        a, b = ll[:-1].split(" ")
        cum1 += win(a,b)
        c = answer(b, a)
        cum2 += win(a,c)
    print(cum1)
    print(cum2)
