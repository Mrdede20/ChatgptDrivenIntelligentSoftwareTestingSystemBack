Sure, here are two Python programs that implement k-Heapsort as described:

Program 1:

```python
import heapq

def k_heapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            yield heapq.heappushpop(heap, arr[i])
        else:
            yield arr[i]

    while heap:
        yield heapq.heappop(heap)
```

Program 2:

```python
import heapq

def k_heapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    i = k
    while heap:
        yield heapq.heappop(heap)
        if i < len(arr):
            heapq.heappush(heap, arr[i])
            i += 1
```

Both programs take the same input parameters and return a generator that yields sorted elements of the input array. The first program implements the k-Heapsort algorithm using a for loop, while the second program implements it using a while loop.