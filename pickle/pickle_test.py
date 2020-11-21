import pickle


class PTest:
    def __init__(self, name):
        self.name = name
        self.count = 0
    def __str__(self):
        return "{0}, {1}".format(self.name, self.count)
    def add(self):
        self.count = self.count+1


def save():
    p1 = PTest('p1')
    p1.add()
    p1.add()
    with open('./text.txt', 'wb') as f:
        pickle.dump(p1, f)

def get():
    p1 = None
    with open('./text.txt', 'rb') as f:
        p1 = pickle.load(f)
    print(p1)

def main():
    # save()
    get()

if __name__ == "__main__":
    main()