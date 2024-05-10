
import heapq

def k_heapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            yield heapq.heappushpop(heap, arr[i])
        else:
            yield arr[i]

    while heap:
        yield heapq.heappop(heap)
