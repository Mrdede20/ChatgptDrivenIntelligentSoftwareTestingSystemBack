
from heapq import heappush, heappop

def kheapsort(arr, k):
    heap = arr[:k]
    heapify(heap)

    for value in arr[k:]:
        heappush(heap, value)
        yield heappop(heap)

    while heap:
        yield heappop(heap)
