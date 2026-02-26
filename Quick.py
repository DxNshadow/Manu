import time
import random

# Using the optimized built-in Timsort/Quicksort
def quick_sort(arr):
    arr.sort()

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
for size in sizes:
    data = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    quick_sort(data)
    print(f"Quick Sort size {size}: {time.time() - start:.5f}s")
