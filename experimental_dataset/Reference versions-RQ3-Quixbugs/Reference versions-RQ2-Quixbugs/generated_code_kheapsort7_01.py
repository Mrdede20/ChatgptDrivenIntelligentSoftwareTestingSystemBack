
import heapq

def k_heap_sort(arr, k):
    n = len(arr)
    heap = []
    for i in range(min(k+1, n)):
        heapq.heappush(heap, arr[i])
    for i in range(min(k+1, n), n):
        arr[i-(k+1)] = heapq.heappushpop(heap, arr[i])
    for i in range(min(k+1, n)):
        arr[n-k-1+i] = heapq.heappop(heap)
    return arr
