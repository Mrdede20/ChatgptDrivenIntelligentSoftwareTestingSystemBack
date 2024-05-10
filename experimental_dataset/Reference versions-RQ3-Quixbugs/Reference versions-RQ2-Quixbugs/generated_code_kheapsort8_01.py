
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        yield heapq.heappushpop(heap, arr[i])
    while heap:
        yield heapq.heappop(heap)
