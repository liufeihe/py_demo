class EventBus:
    events_map = {}

    @classmethod
    def on(cls, event_type, cb):
        events = cls.events_map.get(event_type)
        if events is None:
            cls.events_map[event_type] = set([cb])
        else:
            events.add(cb)
    
    @classmethod
    def emit(cls, event_type, data=None):
        print("emit {0}".format(event_type))
        events = cls.events_map.get(event_type)
        if events is not None:
            for _, cb in enumerate(events):
                cb(data)