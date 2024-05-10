
import heapq

def k_heap_sort(arr, k):
    heap = []
    for elem in arr:
        if len(heap) < k:
            heapq.heappush(heap, elem)
        else:
            min_elem = heapq.heappushpop(heap, elem)
            yield min_elem
    while heap:
        yield heapq.heappop(heap)
