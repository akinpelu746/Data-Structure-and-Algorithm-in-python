def longest(A):
    start = 0
    current = 1
    largest_sequence = 0
    for i in range(len(A)-1):
        if A[i] < A[current]:
            current += 1
            pass
        else:
            if largest_sequence < current - start:
                largest_sequence = current - start
            start = current
            current += 1
    return largest_sequence


print(longest([2, 3, 4, 5, 2, 3, 5, 6, 7, 4, 2, 7, 8, 9]))
