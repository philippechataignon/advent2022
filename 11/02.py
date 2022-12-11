#!/usr/bin/env python3
from parse import parse

class Monkey:
    def __init__(self, mks, items, oper, div, mt, mf):
        self.mks = mks
        self.items = items
        self.oper = oper
        self.div = div
        self.mt = mt
        self.mf = mf
        self.count = 0

    def __str__(self):
        return f"{self.div}: #{self.count}"

    def calc(self, old):
        return eval(self.oper)

    def get(self, num):
        self.items.append(num)

    def inspect(self):
        while self.items:
            self.count += 1
            item = self.items.pop(0)
            w = self.calc(item) % modulo

            if w % self.div == 0:
                self.mks[self.mt].get(w)
            else:
                self.mks[self.mf].get(w)

def main():
    global modulo

    # f = open("test.txt")
    f = open("input.txt")
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

    modulo = 1
    for mk in mks:
        modulo *= mk.div

    print("supermodulo: ", modulo)

    print([str(mk) for mk in mks])
    for round in range(10000):
        for mk in mks:
            mk.inspect()
    print([str(mk) for mk in mks])

    lp = sorted([mk.count for mk in mks], reverse=True)
    print(lp[0] * lp[1])

if  __name__ == '__main__':
    main()
