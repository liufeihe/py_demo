#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Num:
    def __init__(self, count):
        self.count = count
    def __str__(self):
        return "count:{0}".format(self.count)
    def set_count(self, count):
        self.count = count

def test():
    n1 = Num(1)
    n2 = Num(2)
    s = set()
    s.add(n1)
    s.add(n2)
    for v in s:
        print(v)
        v.set_count(10)
        print(v)
    s.remove(n1)
    print(len(s))
    print(n1)
    print(n2)

if __name__ == "__main__":
    test()