class Stack:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * self.size
        self.top = 0

    def empty(self):
        return self.top == 0

    def push(self, x):
        assert self.top < self.size, "overflow"
        self.arr[self.top] = x
        self.top += 1

    def pop(self):
        assert not self.empty(), "underflow"
        self.top -= 1
        return self.arr[self.top]


__all__ = ["Stack"]
