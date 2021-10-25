from typing import List


def InsertionSort(A: List) -> List:
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


A = [5, 2, 4, 6, 1, 3]
InsertionSort(A)
print(A)
