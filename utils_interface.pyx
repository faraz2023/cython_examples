import numpy as np

# Importing C function
cdef extern from "src/utils.h":
    void c_sort(int* arr, int n)


# Cython wrapper function
def c_sort_interface(int[:] arr):
    cdef int n = len(arr)
    c_sort(&arr[0], n)
    return [arr[i] for i in range(n)]



# Unfair because of the type conversion
#def c_sort_interface(arr):
#    cdef int[:] c_arr = np.ascontiguousarray(arr, dtype=np.int32)
#    c_sort(&c_arr[0], len(c_arr))
#    return [c_arr[i] for i in range(len(c_arr))]
