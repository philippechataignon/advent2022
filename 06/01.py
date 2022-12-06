#!/usr/bin/env python3
def all_diff(l):
    return len(l) == len(set(l))

def traite(l):
    for i in range(len(l) - 3):
        if all_diff(l[i:i+4]):
            return i + 4
    return None

def main():
    f = open("input.txt")
    cum = 0
    for l in f:
        l = l[:-1]
        cum += traite(l)
    print(cum)

if __name__ == '__main__':
    main()
