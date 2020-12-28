from bus.eventBus import EventBus
from schedule.base_mgr import BaseMgr
from time import sleep


class OrderMgr(BaseMgr):
    def __init__(self):
        BaseMgr.__init__(self)
        self.name = 'order-mgr'
        self.order_count = 0
        EventBus.on('add-order', self.add_order)

    def add_order(self, data=None):
        self.push_event_queue('add-order', data)

    def hanlde_add_order(self):
        self.order_count = self.order_count + 1
        print('{0}, add-order, {1}'.format(self.name, self.order_count))

    def handle_events(self):
        while not self.event_queue.empty():
            data = self.event_queue.get()
            event_name = data.get('event_name')
            if (event_name=='add-order'):
                self.hanlde_add_order()

    def run(self):
        while True:
            sleep(1)
            self.handle_events()
            # print('{0}, count: {1}'.format(self.name, self.order_count))