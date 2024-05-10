Here's the first program:

```python
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        yield heapq.heappushpop(heap, arr[i])
    while heap:
        yield heapq.heappop(heap)
```

And here's the second program which is a more optimized version of the first program:

```python
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    i = k
    while heap:
        if i < len(arr):
            el = heapq.heappushpop(heap, arr[i])
            yield el
            i += 1
        else:
            yield heapq.heappop(heap)
```

Both programs have the same method name and parameter type and they implement the k-Heapsort algorithm as described. The second program is more optimized because it doesn't iterate over the array using a range function like the first program. Instead, it uses a while loop and an index variable to iterate over the array, which saves some processing time.