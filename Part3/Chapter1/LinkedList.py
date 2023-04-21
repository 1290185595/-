class ListNode:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def prepend(self, x):
        x.prev = None
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x

    def insert(self, x, y=None):
        if y is None:
            self.prepend(x)
        else:
            x.next = y.next
            x.prev = y
            if y.next is not None:
                y.next.prev = x
            y.next = x

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev


class LinkedListWithSentinel:
    def __init__(self):
        self.sentinel = ListNode(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def search(self, k):
        self.sentinel.key = k
        x = self.sentinel.next
        while x.key != k:
            x = x.next
        return None if x == self.sentinel else x

    def prepend(self, x):
        self.insert(x)

    def insert(self, x, y=None):
        if y is None:
            y = self.sentinel
        x.next = y.next
        x.prev = y
        y.next.prev = x
        y.next = x

    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev


__all__ = ["ListNode", "LinkedList", "LinkedListWithSentinel"]
