# cython_examples
In this repo I keep cython practices and benchmarking that I do for my research. 


## Cases:

### Case 1: Bubble sort

You can run the the `benchmark.py` file to see the difference between the python, cython, and c implementation of the bubble sort algorithm for arrays of integers.

Results: 


For 10,000 random integers:

```
Python Sort - Time: 8.5990 s, Memory: 58.91 MiB
Cython Sort - Time: 0.4879 s, Memory: 59.02 MiB
C Sort - Time: 0.8932 s, Memory: 60.14 MiB
```

For 100,000 random integers (bubble sort is $n^2$ !!)

```
Python Sort - Time: 855.1741 s, Memory: 63.23 MiB
Cython Sort - Time: 5.4149 s, Memory: 34.38 MiB
C Sort - Time: 8.6251 s, Memory: 38.77 MiB
```
