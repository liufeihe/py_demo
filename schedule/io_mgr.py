from bus.eventBus import EventBus
from schedule.base_mgr import BaseMgr
from time import sleep


class IOMgr(BaseMgr):
    def __init__(self):
        BaseMgr.__init__(self)
        self.name = 'io-mgr'
        self.count = 0

    def run(self):
        while True:
            sleep(1)
            print('{0}, {1}'.format(self.name, self.count))
            self.count = self.count+1
            if self.count%3==0:
                EventBus.emit('add-order')