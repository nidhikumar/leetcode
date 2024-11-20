def bubbleSort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return(A)

A = [3, 7, 2, 5, 9, 1]
print(bubbleSort(A))