def selectionSort(A):
    for i in range(0, len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i] , A[minIndex] = A[minIndex], A[i]
    return(A)

A = [3, 7, 2, 5, 9, 1]
print(selectionSort(A))