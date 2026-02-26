import time
import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: return -1
    for i in range(prev, min(step, n)):
        if arr[i] == x: return i
    return -1

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
for size in sizes:
    data = list(range(size)) # Must be sorted
    start = time.time()
    jump_search(data, size - 1)
    print(f"Jump Search size {size}: {time.time() - start:.8f}s")
