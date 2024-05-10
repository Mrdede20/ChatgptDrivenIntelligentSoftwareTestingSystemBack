Sure, here's the first program:

```
import heapq

def k_heapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    i = k
    for x in arr[k:]:
        heapq.heappush(heap, x)
        yield heapq.heappop(heap)
    while heap:
        yield heapq.heappop(heap)
```

And here is the second program which sorts the elements in reverse order:

```
import heapq

def k_heapsort(arr, k):
    heap = [-x for x in arr[:k]]
    heapq.heapify(heap)
    i = k
    for x in arr[k:]:
        heapq.heappush(heap, -x)
        yield -heapq.heappop(heap)
    while heap:
        yield -heapq.heappop(heap)
```

Both programs implement the same K-Heapsort algorithm as described in the problem statement. The only difference between them is that the second program uses a heap of negative integers in order to sort the elements in reverse order.