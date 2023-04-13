def counting_sort(A: list[int]) -> list[int]:
    n = len(A)
    k = max(A)
    B = [0] * n
    C = [0] * (k + 1)
    for i in range(0, n): C[A[i]] += 1
    for j in range(0, k): C[j + 1] += C[j]
    while n > 0:
        n -= 1
        C[A[n]] -= 1
        B[C[A[n]]] = A[n]
    return B


__all__ = ["counting_sort"]
