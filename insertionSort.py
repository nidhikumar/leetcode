def insertionSort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return(A)

A = [3, 7, 2, 5, 9, 1]
print(insertionSort(A))