Sure! Here are two implementations of the K-Heapsort algorithm:

### Implementation 1

```
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
```

### Implementation 2

```
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
```

Both implementations take an array `arr` and an integer `k` as parameters. The function returns the sorted array. 

The first implementation uses the `heappushpop` and `heappop` methods of the `heapq` module to optimize the heap operations. 

The second implementation is simpler and only uses the `heappush` and `heappop` methods of the `heapq` module. It also avoids the use of the `min` function to calculate the range of the loops.