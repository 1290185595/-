import math

from Part3.Chapter1.LinkedList import ListNode, LinkedList


class HashFunctions:
    class division:
        def __init__(self, m):
            self.m = m

        def __call__(self, k):
            return k % self.m

    class multiplication:
        def __init__(self, m, A=None):
            self.m = m
            self.A = A or (5 ** 0.5 - 1) / 2

        def __call__(self, k):
            return math.floor(self.m * ((k * self.A) % 1))

    __functions = tuple([name for name in dir() if not name.startswith('_')])

    def __new__(cls, h, *args, **kwargs):
        assert h in cls.__functions, "invalid hash function"
        h = getattr(cls, h)(*args, **kwargs)
        return h, h.m


class HashTable:
    def __init__(self, *args, h="division", **kwargs):
        self.hash, m = HashFunctions(h, *args, **kwargs)
        self.chains = [LinkedList() for _ in range(m)]

    def search(self, k):
        x = self.chains[self.hash(k)].search(k)
        return x and x.value

    def insert(self, k, v):
        chain = self.chains[self.hash(k)]
        x = chain.search(k)
        if x is None:
            x = ListNode(k)
            chain.prepend(x)
        x.value = v

    def delete(self, k):
        chain = self.chains[self.hash(k)]
        x = chain.search(k)
        if x is not None:
            chain.delete(x)


__all__ = ["HashTable"]
