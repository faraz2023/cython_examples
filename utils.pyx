def cython_sort(int[:] arr):
    cdef int i, j, n
    n = arr.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
