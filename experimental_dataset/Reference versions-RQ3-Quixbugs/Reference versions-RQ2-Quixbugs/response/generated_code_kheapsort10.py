First Program:

```python
import heapq


def k_heapsort(arr, k):

    heap = arr[:k]
    heapq.heapify(heap)

    for elem in arr[k:]:
        smallest = heapq.heappushpop(heap, elem)
        yield smallest

    while heap:
        smallest = heapq.heappop(heap)
        yield smallest
```

Second Program:

```python
import heapq


def k_heapsort(arr, k):

    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    for i in range(k, len(arr)):
        smallest = heapq.heappushpop(heap, arr[i])
        yield smallest

    while heap:
        smallest = heapq.heappop(heap)
        yield smallest
```

Both programs implement the k-heapsort algorithm and take an input array and maximum displacement k, and return a generator that yields the sorted elements of the array. The first program creates a heap of the first k elements of the array and then iteratively adds each element to the heap and removes the smallest element. The second program manually adds the first k elements to the heap and then iteratively adds each element to the heap and removes the smallest element.