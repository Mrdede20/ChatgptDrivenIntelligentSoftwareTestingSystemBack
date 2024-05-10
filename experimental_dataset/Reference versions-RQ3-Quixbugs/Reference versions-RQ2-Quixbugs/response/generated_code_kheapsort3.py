Here are two programs that achieve the intended purpose:

Program 1:
```python
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for elem in arr[k:]:
        min_elem = heapq.heappushpop(heap, elem)
        yield min_elem
    while heap:
        yield heapq.heappop(heap)
```

Program 2:
```python
import heapq

def k_heap_sort(arr, k):
    heap = []
    for elem in arr:
        if len(heap) < k:
            heapq.heappush(heap, elem)
        else:
            min_elem = heapq.heappushpop(heap, elem)
            yield min_elem
    while heap:
        yield heapq.heappop(heap)
```

Both programs have the same time complexity of `O(n*log(k))` and use the same method name and parameter type. The only difference between the two is the approach used to initialize the heap. Program 1 uses the first k elements of the array to initialize the heap, while Program 2 adds elements to the heap one at a time, maintaining a heap of size k at all times.