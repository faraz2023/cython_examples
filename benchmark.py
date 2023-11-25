import time
from memory_profiler import memory_usage
from utils import cython_sort
from utils_interface import c_sort_interface
import random
import numpy as np



def python_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



# Generate a random array
array_size = 10000
array = [random.randint(0, 10000) for _ in range(array_size)]

# Time and memory benchmarking function
def benchmark(sort_func, arr):

    # Convert to actually 
    arr_copy = np.array(arr.copy(), dtype=np.int32)  
    start_time = time.time()
    peak_memory = max(memory_usage((sort_func, (arr_copy,))))
    end_time = time.time()

    return end_time - start_time, peak_memory


# Benchmaring must be done in a __main__ block to avoid errors
if __name__ == '__main__':

    # Benchmark each implementation
    time_python, mem_python = benchmark(python_sort, array)
    time_cython, mem_cython = benchmark(cython_sort, array)
    time_c, mem_c = benchmark(c_sort_interface, array)

    print(f"Python Sort - Time: {time_python:.4f} s, Memory: {mem_python:.2f} MiB")
    print(f"Cython Sort - Time: {time_cython:.4f} s, Memory: {mem_cython:.2f} MiB")
    print(f"C Sort - Time: {time_c:.4f} s, Memory: {mem_c:.2f} MiB")
