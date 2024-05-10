Here are two programs that implement the k-heapsort algorithm to sort an almost-sorted array:

Program 1:

```
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for elem in arr[k:]:
        smallest = heapq.heappushpop(heap, elem)
        yield smallest
    while heap:
        yield heapq.heappop(heap)
```

Program 2:

```
import heapq

def k_heap_sort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    i = k
    while heap:
        yield heapq.heappop(heap)
        if i < len(arr):
            heapq.heappush(heap, arr[i])
            i += 1
``` 

Both programs take an array `arr` and an integer `k` as parameters, and return a generator that yields the sorted elements of the array. The first `k` elements of the array are added to a heap using `heapq.heapify`, and then the remaining elements are iterated over. Each element is pushed onto the heap, and the smallest element is popped using `heapq.heappushpop(heap, elem)`. Finally, the remaining elements are popped from the heap in order to output the sorted elements.

Program 1 iterates over the array using a `for` loop, while Program 2 iterates over the array using a `while` loop and a separate counter variable `i`. Both programs achieve the same result and have a time complexity of O(n log k).