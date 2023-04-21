def parent(i):
    return (i - 1) >> 1


def left(i):
    return (i << 1) + 1


def right(i):
    return (i + 1) << 1


class BinaryHeap:
    def __init__(self, arr, cmp=None):
        self.arr = arr
        self.size = len(arr)
        self.cmp = (lambda x, y: x > y) if cmp is None else cmp
        self.build()

    def build(self):
        for i in range((self.size >> 1) - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest = i
        if (l := left(i)) < self.size and self.cmp(self.arr[l], self.arr[largest]):
            largest = l
        if (r := right(i)) < self.size and self.cmp(self.arr[r], self.arr[largest]):
            largest = r
        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.heapify(largest)


__all__ = ["BinaryHeap"]
