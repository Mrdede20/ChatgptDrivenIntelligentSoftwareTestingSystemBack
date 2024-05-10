Here are two versions of the `kheapsort` function in Python:

Version 1: Using `heapq.nsmallest`
```python
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    yield from heapq.nsmallest(len(arr), (heapq.heappushpop(heap, x) for x in arr[k:]))
```

Version 2: Using `heappush` and `heappop`
```python
import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    for x in arr[k:]:
        yield heapq.heappushpop(heap, x)
    
    while heap:
        yield heapq.heappop(heap)
```

Both versions take an input array `arr` and a maximum allowed displacement `k` as parameters, and return a generator that yields the elements in sorted order. They both use the `heapq` module to create a heap and efficiently sort the array in `O(n log k)` time. The first version uses the `heapq.nsmallest` function to generate the sorted output, while the second version uses a combination of `heappush` and `heappop` to update the heap and generate the sorted output.