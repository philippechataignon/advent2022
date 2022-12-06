#!/usr/bin/env python3
def all_diff(l):
    return len(l) == len(set(l))

def traite(l):
    for i in range(len(l) - 3):
        if all_diff(l[i:i+4]):
            return i + 4
    return None

def traite2(l):
    for i in range(len(l) - 13):
        if all_diff(l[i:i+14]):
            return i + 14
    return None

def go(func):
    f = open("input.txt")
    cum = 0
    for l in f:
        l = l[:-1]
        r = func(l)
        cum += r
    print(cum)

def main():
    go(traite)
    go(traite2)

if __name__ == '__main__':
    main()
