
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for elem in arr[k:]:
        smallest = heapq.heappushpop(heap, elem)
        yield smallest
    while heap:
        yield heapq.heappop(heap)
