
import heapq


def k_heapsort(arr, k):

    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    for i in range(k, len(arr)):
        smallest = heapq.heappushpop(heap, arr[i])
        yield smallest

    while heap:
        smallest = heapq.heappop(heap)
        yield smallest
