import random


def partition(A: list, p: int, r: int) -> int:
    for i in range(p, r):
        if A[i] < A[r]:
            A[i], A[p] = A[p], A[i]
            p += 1
    A[r], A[p] = A[p], A[r]
    return p


def quick_sort(A: list, p: int = None, r: int = None) -> None:
    if p is None: p = 0
    if r is None: r = len(A) - 1
    if p >= r: return
    q = partition(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q + 1, r)


def randomized_partition(A: list, p: int, r: int) -> int:
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_quick_sort(A: list, p: int = None, r: int = None) -> None:
    if p is None: p = 0
    if r is None: r = len(A) - 1
    if p >= r: return
    q = randomized_partition(A, p, r)
    randomized_quick_sort(A, p, q - 1)
    randomized_quick_sort(A, q + 1, r)


__all__ = ["quick_sort", "randomized_quick_sort"]
