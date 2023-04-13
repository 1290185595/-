from Part2.Chapter1.insertion_sort import insertion_sort
from Part2.Chapter1.quick_sort import partition


def bfptr_partition(A: list, p: int, r: int) -> int:
    g = (r - p + 1) // 5
    for i in range(p, p + g):
        B = A[i:(r + 1):g]
        insertion_sort(B)
        A[i:(r + 1):g] = B
    i = (p + r) >> 1
    bfptr_select(A, i, p + (g << 1), r - (g << 1))
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def bfptr_select(A: list, i: int = None, p: int = None, r: int = None):
    if p is None: p = 0
    if r is None: r = len(A) - 1
    if p == r: return A[p]
    if i is None: i = p
    while (r - p + 1) % 5 != 0:
        j = min(range(p, r + 1), key=A.__getitem__)
        if j != p: A[j], A[p] = A[p], A[j]
        if i == p: return A[p]
        p += 1
    q = bfptr_partition(A, p, r)
    if i == q:
        return A[q]
    elif i < q:
        return bfptr_select(A, i, p, q - 1)
    else:
        return bfptr_select(A, i, q + 1, r)


__all__ = ["bfptr_select"]
