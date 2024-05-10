Sure, here is one implementation of the K-Heapsort algorithm as a function named `kheapsort`:

```
from heapq import heappush, heappop

def kheapsort(arr, k):
    heap = arr[:k]
    heapify(heap)

    for value in arr[k:]:
        heappush(heap, value)
        yield heappop(heap)

    while heap:
        yield heappop(heap)
```

Here is another implementation of the K-Heapsort algorithm as a function named `kheapsort` using a sliding window approach:

```
from heapq import heappush, heappop

def kheapsort(arr, k):
    heap = arr[:k]
    heapify(heap)

    i = 0
    for value in arr[k:]:
        arr[i] = heappushpop(heap, value)
        i += 1

    while heap:
        arr[i] = heappop(heap)
        i += 1

    return arr
```

Both functions take the same two arguments:
- `arr`: a list of integers to sort
- `k`: an integer indicating how far each element of the list is from its final sorted position

Both functions return a generator that yields the sorted integers of `arr`.