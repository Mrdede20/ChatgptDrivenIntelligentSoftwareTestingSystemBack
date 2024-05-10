
from heapq import heappush, heappop

def kheapsort(arr, k):
    heap = arr[:k]
    heapify(heap)

    i = 0
    for value in arr[k:]:
        arr[i] = heappushpop(heap, value)
        i += 1

    while heap:
        arr[i] = heappop(heap)
        i += 1

    return arr
