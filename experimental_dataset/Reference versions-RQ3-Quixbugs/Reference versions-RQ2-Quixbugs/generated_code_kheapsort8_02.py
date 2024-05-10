
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    i = k
    while heap:
        if i < len(arr):
            el = heapq.heappushpop(heap, arr[i])
            yield el
            i += 1
        else:
            yield heapq.heappop(heap)
