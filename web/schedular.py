schedular = None

class Schedular:
    def __init__(self, name):
        self.name = name
        self.count = 0
    
    def __str__(self):
        return "{0}, {1}".format(self.name, self.count)

    def add_count(self):
        self.count = self.count+1


def get_schedular():
    global schedular
    if schedular is None:
        schedular = Schedular('a')
    # schedular = Schedular('a')
    schedular.add_count()
    return schedular