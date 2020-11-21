from threading import Thread, Timer
from time import sleep

class Task (Thread):
    def __init__(self, name='task', event=None):
        Thread.__init__(self)
        self.name = name
        self.event = event
        self.is_over = False
        self.count = 0
        self.a = None

    def add(self):
        self.count = self.count+1
        if self.count==3:
            print("event is trigger from {0}".format(self.name))
            self.is_over = True
            self.event.set()
        else:
            print("{0} is counting".format(self.name))
            timer = Timer(1, self.add)
            timer.start()

    def run(self, a=None):
        self.a = a
        print("{0} is running, {1}".format(self.name, a))
        self.add()
            
        