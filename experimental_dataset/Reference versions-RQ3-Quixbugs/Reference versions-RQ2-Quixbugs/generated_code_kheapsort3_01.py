
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for elem in arr[k:]:
        min_elem = heapq.heappushpop(heap, elem)
        yield min_elem
    while heap:
        yield heapq.heappop(heap)
