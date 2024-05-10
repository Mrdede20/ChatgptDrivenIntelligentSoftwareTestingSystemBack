
import heapq


def k_heapsort(arr, k):

    heap = arr[:k]
    heapq.heapify(heap)

    for elem in arr[k:]:
        smallest = heapq.heappushpop(heap, elem)
        yield smallest

    while heap:
        smallest = heapq.heappop(heap)
        yield smallest
