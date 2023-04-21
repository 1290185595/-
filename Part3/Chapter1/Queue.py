class Queue:
    def __init__(self, n):
        self.size = n + 1
        self.arr = [0] * self.size
        self.head = 0
        self.tail = 0
        self.forward = lambda x: 0 if x == n else x + 1

    def empty(self):
        return self.head == self.tail

    def push(self, x):
        assert self.forward(self.tail) != self.head, "overflow"
        self.arr[self.tail] = x
        self.tail = self.forward(self.tail)

    def pop(self):
        assert not self.empty(), "underflow"
        x = self.arr[self.head]
        self.head = self.forward(self.head)
        return x


__all__ = ["Queue"]
