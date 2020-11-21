from threading import Thread, Timer
from time import sleep
from task import Task

class Job (Thread):
    def __init__(self, name='job', event=None):
        Thread.__init__(self)
        self.name = name
        self.event = event
        self.task_list = []
        for i in range(100):
            self.task_list.append(Task("task-{0}".format(i), event))

    def next(self):
        task = None
        for _, t in enumerate(self.task_list):
            if not t.is_over:
                task = t
                break
        if task is None:
            print("job is done")
        else:
            self.event.clear()
            task.run('abc')

    def run(self):
        self.event.set()
        while True:
            sleep(1)
            # self.event.wait()
            if not self.event.is_set():
                print("{0} is waiting".format(self.name))
            else:
                print("{0} is running".format(self.name))
                self.next()