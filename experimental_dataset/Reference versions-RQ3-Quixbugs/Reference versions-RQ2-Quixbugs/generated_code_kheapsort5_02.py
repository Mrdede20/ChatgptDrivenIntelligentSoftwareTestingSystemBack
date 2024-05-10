
import heapq

def k_heapsort(arr, k):
    heap = [-x for x in arr[:k]]
    heapq.heapify(heap)
    i = k
    for x in arr[k:]:
        heapq.heappush(heap, -x)
        yield -heapq.heappop(heap)
    while heap:
        yield -heapq.heappop(heap)
