
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    yield from heapq.nsmallest(len(arr), (heapq.heappushpop(heap, x) for x in arr[k:]))
