#!/usr/bin/python
# -*- coding: UTF-8 -*-
from threading import Thread,Timer
from time import sleep

def asyncf(f):
    def wrapper(*args, **kwargs):
        # thr = Thread(target=f, args=args, kwargs=kwargs)
        thr = Timer(0.1, f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper

@asyncf
def test(a):
    # sleep(10)
    print(a)

if __name__ == "__main__":
    print(1)
    test(2)
    print(3)