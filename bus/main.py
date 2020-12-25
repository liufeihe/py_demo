#!/usr/bin/python
# -*- coding: UTF-8 -*-
from eventBus import EventBus
from threading import Thread,Timer
from queue import Queue

count = 1
q = Queue(maxsize=1000)

def test_bus(data=None):
    global q
    if q.empty():
        print('test_bus, {0}'.format(data))
    else:
        print('test_bus, {0}, {1}'.format(data, q.get()))

def start_timer():
    global count
    count = count + 1
    t1 = Timer(0.01, start_timer)
    t1.start()
    EventBus.emit('test', count)

def main():
    EventBus.on('test', test_bus)
    q.put({'type':'a'})
    q.put({'type':'b'})
    start_timer()


if __name__ == "__main__":
    main()