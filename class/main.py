class Father:
    def __init__(self):
        self.queue = []
        self.pos = (1,2,3)
    
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

class Sample:
    def __init__(self):
        self.pos = (1,2,3,0.1,0.2,0.3)

    def __getattr__(self, key):
        pos_idx_arr = ['x', 'y', 'z', 'rz', 'ry', 'rx']
        if key in pos_idx_arr:
            idx = pos_idx_arr.index(key)
            return getattr(self, 'pos')[idx]
        else:
            return getattr(self, key)

if __name__ == "__main__":
    # son = Son()
    # son.push(1)
    # son.print()
    s = Sample()
    print(s.x)
    print(s.rx)
    print(s.pos)