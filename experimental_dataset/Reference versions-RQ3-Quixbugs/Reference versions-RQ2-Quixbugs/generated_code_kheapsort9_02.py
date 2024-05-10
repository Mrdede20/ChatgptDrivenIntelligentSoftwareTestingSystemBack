
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    i = k
    while heap:
        yield heapq.heappop(heap)
        if i < len(arr):
            heapq.heappush(heap, arr[i])
            i += 1
