class FibonacciGenerator:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return result

    def __iter__(self):
        return self

if __name__ == '__main__':

    for i in FibonacciGenerator():
        print(i)

        if i > 100:
            break