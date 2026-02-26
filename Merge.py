import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1

sizes = [10, 100, 1_000, 10_000, 100_000]
for size in sizes:
    data = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    merge_sort(data)
    print(f"Merge Sort size {size}: {time.time() - start:.5f}s")
