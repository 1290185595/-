import math

from Part2.Chapter1.insertion_sort import insertion_sort


def bucket_sort(A: list[float]) -> list[float]:
    n = len(A)
    B = [[] for i in range(0, n)]
    C = []
    for i in range(0, n): B[math.floor(n * A[i])].append(A[i])
    for i in range(0, n):
        insertion_sort(B[i])
        C.extend(B[i])
    return C


__all__ = ["bucket_sort"]
