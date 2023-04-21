from Part3.Chapter2.HashTable import HashFunctions


class OpenAddressHashFunction:
    class linear_probing:
        def __init__(self, m, h0=None):
            if h0 is None:
                h0 = "division", tuple(), dict()
            self.h0, self.m = HashFunctions(h0[0], m, *h0[1], **h0[2])

        def __call__(self, k, i):
            return (self.h0(k) + i) % self.m

    class quadratic_probing:
        def __init__(self, m, h0=None, c1=0, c2=1):
            if h0 is None:
                h0 = "division", tuple(), dict()
            self.h0, self.m = HashFunctions(h0[0], m, *h0[1], **h0[2])
            self.c1 = c1
            self.c2 = c2

        def __call__(self, k, i):
            return (self.h0(k) + self.c1 * i + self.c2 * (i ** 2)) % self.m

    __functions = tuple([name for name in dir() if not name.startswith('_')])

    def __new__(cls, h, *args, **kwargs):
        assert h in cls.__functions, "invalid hash function"
        h = getattr(cls, h)(*args, **kwargs)
        return h, h.m


class OpenAddressHashTable:
    def __init__(self, *args, h="linear_probing", **kwargs):
        self.hash, self.size = OpenAddressHashFunction(h, *args, **kwargs)
        self.arr = [None] * self.size

    def insert(self, k, v):
        i = 0
        while i < self.size:
            if self.arr[idx := self.hash(k, i)] is None:
                self.arr[idx] = (k, v)
                return idx
            i += 1
        assert False, "overflow"

    def search(self, k):
        for i in range(0, self.size):
            if self.arr[idx := self.hash(k, i)] is None:
                break
            elif (x := self.arr[idx])[0] == k:
                return x[1]
        return None


__all__ = ["OpenAddressHashTable"]
