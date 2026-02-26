import time
import random

def linear(arr, x):
    for i, v in enumerate(arr):
        if v == x: return i
    return -1

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
for size in sizes:
    data = list(range(size))
    start = time.time()
    linear(data, -1) # Worst case
    print(f"Linear Search size {size}: {time.time() - start:.5f}s")
