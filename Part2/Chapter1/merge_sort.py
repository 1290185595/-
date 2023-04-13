def merge(A: list, p: int, q: int, r: int) -> None:
    B = A[q + 1: r + 1]
    i = q
    j = r - q - 1
    k = r
    while i >= p and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1


def merge_sort(A: list, p: int = None, r: int = None) -> None:
    if p is None: p = 0
    if r is None: r = len(A) - 1
    if p >= r: return
    q = (p + r) >> 1
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)


__all__ = ["merge_sort"]
