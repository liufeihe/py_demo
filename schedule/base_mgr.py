from queue import Queue
from bus.eventBus import EventBus


class BaseMgr:
    def __init__(self):
        # 事件处理队列
        self.event_queue = Queue(maxsize=1000)

    def push_event_queue(self, event_name, event_data=None):
        # 将事件发到队列中
        self.event_queue.put({'event_name':event_name, 'event_data': event_data if event_data is not None else None})

    def on(self, event_name, cb):
        # 监听事件
        EventBus.on(event_name, cb)
    
    def emit(self, event_name, event_data=None):
        # 发出事件
        EventBus.emit(event_name, event_data)