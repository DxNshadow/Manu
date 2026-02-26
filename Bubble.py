import time
import random

def bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Testing setup
sizes = [10, 100, 1_000, 10_000] # Limited for O(n^2)
for size in sizes:
    data = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    bubble(data)
    print(f"Bubble Sort size {size}: {time.time() - start:.5f}s")
