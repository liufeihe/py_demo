from time import sleep
from threading import Thread
from schedule.base_mgr import BaseMgr
from schedule.order_mgr import OrderMgr
from schedule.io_mgr import IOMgr

schedular = None


def init_schedular():
    global schedular
    if schedular is None:
        schedular = Schedular('schedular')
    return schedular

def add_order():
    schedular.add_order()

class Schedular(BaseMgr):
    def __init__(self, name):
        BaseMgr.__init__(self)
        self.order_mgr = OrderMgr()
        self.io_mgr = IOMgr()
        self.name = name
        self.count = 0
   
    def __str__(self):
        return "{0}, {1}".format(self.name, self.count)

    def add_order(self):
        self.order_mgr.add_order()
        
    def run(self):
        # 启动 order mgr
        t1 = Thread(target=self.order_mgr.run)
        t1.start()

        # 启动 io mgr
        t2 = Thread(target=self.io_mgr.run)
        t2.start()

        while True:
           sleep(1)
           self.count = self.count+1
           print('schedule, {0}'.format(self.count))

