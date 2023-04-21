from Part3.Chapter1.BinaryHeap import parent, BinaryHeap


class PriorityQueue:
    def __init__(self, n, cmp=None):
        self.size = n
        self.heap = BinaryHeap([], cmp)
        self.heap.arr = [0] * n

    def __push(self, i, x):
        while i > 0 and self.heap.cmp(x, self.heap.arr[parent(i)]):
            self.heap.arr[i] = self.heap.arr[parent(i)]
            i = parent(i)
        self.heap.arr[i] = x
        return i

    def empty(self):
        return self.heap.size == 0

    def push(self, x):
        assert self.heap.size < self.size, "overflow"
        self.__push(self.heap.size, x)
        self.heap.size += 1

    def top(self):
        assert not self.empty(), "underflow"
        return self.heap.arr[0]

    def pop(self):
        assert not self.empty(), "underflow"
        self.heap.size -= 1
        self.heap.arr[0], self.heap.arr[self.heap.size] = self.heap.arr[self.heap.size], self.heap.arr[0]
        self.heap.heapify(0)
        return self.heap.arr[self.heap.size]

    def change(self, i, x):
        assert 0 <= i < self.heap.size, "invalid index"
        self.heap.heapify(self.__push(i, x))


__all__ = ["PriorityQueue"]
