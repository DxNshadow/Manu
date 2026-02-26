import time

def binary(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
for size in sizes:
    data = list(range(size)) # Must be sorted
    start = time.time()
    binary(data, size - 1)
    print(f"Binary Search size {size}: {time.time() - start:.8f}s")
