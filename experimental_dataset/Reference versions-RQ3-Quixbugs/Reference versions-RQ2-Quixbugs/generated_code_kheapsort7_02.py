
import heapq

def k_heap_sort(arr, k):
    n = len(arr)
    heap = []
    for i in range(n):
        heapq.heappush(heap, arr[i])
        if i >= k:
            arr[i-k] = heapq.heappop(heap)
    while len(heap) > 0:
        arr[n-len(heap)] = heapq.heappop(heap)
    return arr
