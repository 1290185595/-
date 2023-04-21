class DirectAddressTable:
    def __init__(self, m):
        self.size = m
        self.arr = [None] * m

    def search(self, k):
        return self.arr[k]

    def insert(self, k, v):
        self.arr[k] = v

    def delete(self, k):
        self.arr[k] = None
