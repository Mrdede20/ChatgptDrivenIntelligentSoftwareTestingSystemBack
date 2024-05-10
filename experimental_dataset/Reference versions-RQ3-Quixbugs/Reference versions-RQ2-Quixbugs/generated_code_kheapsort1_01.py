
import heapq

def k_heapsort(arr, k):
    heap = []
    for i in range(min(k+1, len(arr))):
        heapq.heappush(heap, arr[i])
    
    for i in range(k+1, len(arr)):
        yield heapq.heappushpop(heap, arr[i])
    
    while heap:
        yield heapq.heappop(heap)
