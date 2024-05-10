Sure, here are two programs that implement k-heapsort algorithm using the same method name and parameter types:

Program 1:

```
import heapq

def k_heapsort(arr, k):
    heap = []
    for i in range(min(k+1, len(arr))):
        heapq.heappush(heap, arr[i])
    
    for i in range(k+1, len(arr)):
        yield heapq.heappushpop(heap, arr[i])
    
    while heap:
        yield heapq.heappop(heap)
```

Program 2:

```
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
```

Both programs use the heapq module to implement the heap queue and are designed to work on an almost-sorted array where each element is at most k places from its final sorted position. Both take an input of an array (arr) and an integer (k), and return a generator that yields the elements of arr in sorted order. The time complexity of both programs is O(n log k).