def max_heapify(A: list, i: int, heap_size: int) -> None:
    largest = i
    if (l := (i << 1) + 1) < heap_size and A[l] > A[largest]:
        largest = l
    if (r := (i + 1) << 1) < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, heap_size)


def build_max_heap(A: list, n: int) -> None:
    for i in range((n >> 1) - 1, -1, -1):
        max_heapify(A, i, n)


def heap_sort(A: list) -> None:
    n = len(A)
    build_max_heap(A, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)


__all__ = ["heap_sort"]
