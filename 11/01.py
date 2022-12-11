#!/usr/bin/env python3
from parse import parse

# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3


class Monkey:
    def __init__(self, mks, items, oper, div, mt, mf):
        self.items = items
        self.oper = oper
        self.div = div
        self.mt = mt
        self.mf = mf
        self.count = 0

    def __str__(self):
        return f"{self.div}: {self.items} -> {self.count}"

    def calc(self, old):
        return eval(self.oper)

    def get(self, num):
        self.items.append(num)
        self.count += 1

    def inspect(self):
        while self.items:
            w = calc(item) // 3
            m = w % self.div

            if m == 0:
                mks[self.mt].get(self.items.pop(0))
            else:
                mks[self.mf].get(self.items.pop(0))

def main():
    f = open("test.txt")
    # f = open("input.txt")
    mks = []
    while True:
        l = f.readline()
        numm = int(parse("Monkey {}:", l)[0])
        l = f.readline()
        s = eval(f'[ {parse("  Starting items: {}", l)[0]} ]')
        l = f.readline()
        o = parse("  Operation: new = {}", l)[0]
        l = f.readline()
        d = int(parse("  Test: divisible by {}", l)[0])
        l = f.readline()
        mt = int(parse("    If true: throw to monkey {}", l)[0])
        l = f.readline()
        mf = int(parse("    If false: throw to monkey {}", l)[0])
        mks.append(Monkey(mks, s, o, d, mt, mf))
        l = f.readline()
        if l == "":
            break

    for mk in mks:
        print(mk)

if  __name__ == '__main__':
    main()
