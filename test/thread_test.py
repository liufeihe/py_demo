#!/usr/bin/python
# -*- coding: UTF-8 -*-
from threading import Thread,Timer
from time import sleep, ctime, time
import json


def loop(idx, t):
    print("start loop {0} at: {1}".format(idx, ctime()))
    sleep(t)
    print("end loop {0} at: {1}".format(idx, ctime()))


def loop_with_thread(idx, t):
    print("start loop {0} at: {1}".format(idx, ctime()))
    if idx==1:
        t3 = MyThread(loop_with_thread, (3,3))
        t3.start()
        t3.join()
    elif idx==2:
        t4 = MyThread(loop_with_thread, (4,4))
        t4.start()
        t4.join()
    print("end loop {0} at: {1}".format(idx, ctime()))
        
    

def with_single():
    loop(1, 4)
    loop(2, 2)

def with_threading():
    # t1 = Thread(target=loop, args=(1, 4))
    # t2 = Thread(target=loop, args=(2, 2))

    t1 = MyThread(loop, (1,4))
    t2 = MyThread(loop, (2,2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t1 = MyThread(loop_with_thread, (1,4))
    t2 = MyThread(loop_with_thread, (2,2))
    t1.start()
    t1.join()
    t2.start()
    t2.join()

class MyThread(Thread):
    def __init__(self, func, args, name=""):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        self.res = None
    def run(self):
        self.res = self.func(*self.args)
    def getResult(self):
        return self.res

def with_timer():
    timer = Timer(3, loop, (1,4))
    timer.start()
    timer.join()

def fib(x):
    sleep(0.05)
    if x<2:
        return 1
    return fib(x-2)+fib(x-1)

def fac(x):
    sleep(0.1)
    if x<2:
        return 1
    return x*fac(x-1)

def sum2(x):
    sleep(0.1)
    if x<2:
        return 1
    return x+sum2(x-1)


def number_test():
    n = 12
    funcs = [fib, fac, sum2]
    nfuncs = range(len(funcs))
    print("single thread")
    for i in nfuncs:
        s = time()
        print("starting {0} at: {1}".format(funcs[i].__name__, ctime()))
        funcs[i](n)
        e = time()
        print("finished {0} at: {1}, cost{2}".format(funcs[i].__name__, ctime(), e-s))

    print("multi thread")
    threads = []
    s2 = time()
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    for i in nfuncs:
        print(threads[i].getResult())
    e2 = time()
    print("all done, cost: {0}".format(e2-s2))

def print_params(p):
    print(p)
    # p = json.loads(p)
    # p['a'] = 3
    print('params: {0}'.format(p))

def print_params2(p):
    print(p)
    print('params2: {0}'.format(p))

def params_timer():
    b = {'a':2}
    b1 = 'b1'
    timer = Timer(2, print_params, args=(b1,))
    timer.start()

    # timer = Timer(2, print_params2, args=(a))
    # timer.start()

class TimerTest:
    def __init__(self, name):
        self.name = name
    def start(self, p):
        print('start')
        timer = Timer(3, self.print_p, args=(p))
        timer.start()
    def print_p(self,p):
        print('p: {0}'.format(p))


def main():
    print("starting at: {0}".format(ctime()))
    # with_single()
    # with_threading()
    # with_timer()
    # number_test()
    # params_timer()
    tt = TimerTest('test')
    tt.start('abc')
    print("all done at:{0}".format(ctime()))

if __name__ == "__main__":
    main()