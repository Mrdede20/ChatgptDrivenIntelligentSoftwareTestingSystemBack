
import heapq

def k_heapsort(arr, k):
    heap = []
    gen = (arr[i] for i in range(min(len(arr), k+1)))
    for element in gen:
        heapq.heappush(heap, element)
        
    idx = k+1
    while heap:
        yield heapq.heappop(heap)
        if idx < len(arr):
            heapq.heappush(heap, arr[idx])
            idx += 1
