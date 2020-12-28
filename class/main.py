class Father:
    def __init__(self):
        self.queue = []
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        self.queue.pop()


class Son(Father):
    def __init__(self):
        # Father.__init__(self)
        super().__init__()
        self.name = 'son'
    def print(self):
        print(self.queue)

if __name__ == "__main__":
    son = Son()
    son.push(1)
    son.print()